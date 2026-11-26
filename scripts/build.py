#!/usr/bin/env python3
"""OpenCSE static site generator.

Standard library only (Python 3.9+). Run from anywhere:

    python3 scripts/build.py

It reads `courses/`, writes `site/`, and needs no network access.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
COURSES_DIR = ROOT / "courses"
ASSETS_DIR = ROOT / "assets"
SITE_DIR = ROOT / "site"

SITE_NAME = "OpenCSE"
SITE_TAGLINE = "CSE course notes, shared by students"
SITE_DESC = (
    "An unofficial, student-run collection of notes, lab reports and exam "
    "preparation material for Computer Science & Engineering coursework."
)

# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip().lower()
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80].strip("-") or "page"


def human_size(num: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if num < 1024 or unit == "GB":
            return f"{num:.0f} {unit}" if unit == "B" else f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} GB"


def pretty_semester(name: str) -> str:
    if name == "first-year":
        return "First year"
    m = re.search(r"(\d+)", name)
    return f"Semester {m.group(1)}" if m else name.replace("-", " ").title()


YEAR_GROUPS = [
    ("First year", "01\u201302", ["first-year"]),
    ("Second year", "03\u201304", ["semester-3", "semester-4"]),
    ("Third year", "05\u201306", ["semester-5", "semester-6"]),
    ("Fourth year", "07\u201308", ["semester-7", "semester-8"]),
]


def year_label(sem: str | None) -> str | None:
    for label, _code, sems in YEAR_GROUPS:
        if sem in sems:
            return label
    return None


def course_sort(c: "Course") -> tuple:
    order = {"Physics": 0, "Chemistry": 1}
    return (order.get(c.meta.get("cycle", ""), 0), c.title.lower())


def sem_code(name: str) -> str:
    if name == "first-year":
        return "01–02"
    return name.split("-")[-1].zfill(2)


def read_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Parse a tiny `key: value` front-matter block at the top of a file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta: dict[str, str] = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip().strip("\"'")
    return meta, text[end + 4 :].lstrip("\n")


def first_heading(md: str) -> str | None:
    for line in md.splitlines():
        if line.startswith("# "):
            return strip_tags(inline(line[2:].strip()))
    return None


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


# ---------------------------------------------------------------------------
# Markdown -> HTML (the subset the notes actually use)
# ---------------------------------------------------------------------------

LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def inline(text: str) -> str:
    text = html.escape(text, quote=False)

    # Protect inline code first: emphasis must not look inside it, and code may
    # legitimately contain * or ** (e.g. `int **q`).
    codes: list[str] = []

    def stash(m: re.Match[str]) -> str:
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)

    text = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)\)",
        r'<img alt="\1" src="\2" loading="lazy">',
        text,
    )
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)

    for i, code in enumerate(codes):
        text = text.replace(f"\x00{i}\x00", f"<code>{code}</code>")
    return text


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def _list_html(items: list[tuple[int, bool, str]]) -> str:
    idx = 0

    def parse_level(indent: int) -> tuple[str, int]:
        nonlocal idx
        ordered = items[idx][1]
        tag = "ol" if ordered else "ul"
        parts = [f"<{tag}>"]
        while idx < len(items) and items[idx][0] == indent:
            parts.append("<li>" + inline(items[idx][2]))
            idx += 1
            while idx < len(items) and items[idx][0] > indent:
                sub, idx = parse_level(items[idx][0])
                parts.append(sub)
            parts.append("</li>")
        parts.append(f"</{tag}>")
        return "".join(parts), idx

    out = []
    while idx < len(items):
        chunk, idx = parse_level(items[idx][0])
        out.append(chunk)
    return "\n".join(out)


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # fenced code
        if line.lstrip().startswith("```"):
            lang = line.lstrip()[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            code = html.escape("\n".join(buf))
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{code}</code></pre>")
            continue

        # table
        if "|" in line and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            header = _split_row(line)
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(_split_row(lines[i]))
                i += 1
            head = "".join(f"<th>{inline(c)}</th>" for c in header)
            body = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                for row in rows
            )
            out.append(
                '<div class="tablewrap"><table><thead><tr>'
                f"{head}</tr></thead><tbody>{body}</tbody></table></div>"
            )
            continue

        # heading
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            anchor = slugify(strip_tags(inline(text)))
            out.append(
                f'<h{level} id="{anchor}">{inline(text)}'
                f'<a class="anchor" href="#{anchor}" aria-hidden="true">#</a></h{level}>'
            )
            i += 1
            continue

        # horizontal rule
        if re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # blockquote (with lazy continuation lines)
        if line.startswith(">"):
            buf = []
            while i < len(lines) and (lines[i].startswith(">") or (buf and lines[i].strip())):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>" + md_to_html("\n".join(buf)) + "</blockquote>")
            continue

        # lists
        if LIST_RE.match(line):
            items: list[tuple[int, bool, str]] = []
            while i < len(lines):
                m = LIST_RE.match(lines[i])
                if not m:
                    if not lines[i].strip():
                        j = i
                        while j < len(lines) and not lines[j].strip():
                            j += 1
                        if j < len(lines) and LIST_RE.match(lines[j]):
                            i = j
                            continue
                    break
                indent = len(m.group(1))
                items.append((indent, m.group(2)[0].isdigit(), m.group(3).strip()))
                i += 1
                # wrapped continuation lines belong to the same item
                cont = []
                while i < len(lines) and lines[i].strip():
                    if (
                        LIST_RE.match(lines[i])
                        or HEADING_RE.match(lines[i])
                        or lines[i].startswith(">")
                        or lines[i].lstrip().startswith("```")
                        or re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", lines[i])
                        or len(lines[i]) - len(lines[i].lstrip()) <= indent
                    ):
                        break
                    cont.append(lines[i].strip())
                    i += 1
                if cont:
                    ci, co, ct = items[-1]
                    items[-1] = (ci, co, ct + " " + " ".join(cont))
            out.append(_list_html(items))
            continue

        # blank
        if not line.strip():
            i += 1
            continue

        # paragraph
        buf = []
        while i < len(lines) and lines[i].strip() and not (
            HEADING_RE.match(lines[i])
            or LIST_RE.match(lines[i])
            or lines[i].startswith(">")
            or lines[i].lstrip().startswith("```")
            or re.match(r"^\s*([-*_])(\s*\1){2,}\s*$", lines[i])
            or ("|" in lines[i] and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]))
        ):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

    return "\n".join(out)



MATERIAL_CATEGORIES = [
    "Lab manuals & programs",
    "Notes",
    "Question banks & papers",
    "Slides",
    "Syllabus & scheme",
    "Books & references",
    "Other files",
]


def classify_material(rel: str) -> str:
    p = rel.lower()
    ext = Path(p).suffix
    if any(w in p for w in ("lab", "manual", "experiment", "program", "code")):
        return MATERIAL_CATEGORIES[0]
    if any(w in p for w in ("syllabus", "scheme", "calendar", "timetable")):
        return MATERIAL_CATEGORIES[4]
    if any(w in p for w in ("book", "textbook", "handbook", "reference")):
        return MATERIAL_CATEGORIES[5]
    if any(w in p for w in ("question", "ques", "model", "paper", "qp", "pyq",
                            "exam", "see", "internal", "bank")):
        return MATERIAL_CATEGORIES[2]
    if "note" in p:
        return MATERIAL_CATEGORIES[1]
    if ext in (".ppt", ".pptx"):
        return MATERIAL_CATEGORIES[3]
    if any(w in p for w in ("module", "unit", "chapter", "summary")):
        return MATERIAL_CATEGORIES[1]
    return MATERIAL_CATEGORIES[6]


def toc_html(body: str) -> str:
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, flags=re.S)
    if len(heads) < 4:
        return ""
    items = "".join(
        f'<li><a href="#{hid}">{html.escape(strip_tags(re.sub(r"<a class=\"anchor\".*?</a>", "", h)).strip())}</a></li>'
        for hid, h in heads
    )
    return f'<nav class="toc"><p class="toc-label">On this page</p><ol>{items}</ol></nav>'


# ---------------------------------------------------------------------------
# Content discovery
# ---------------------------------------------------------------------------


@dataclass
class Doc:
    title: str
    source: Path
    out_rel: str
    body_html: str
    text: str = ""


@dataclass
class Course:
    semester: str
    slug: str
    path: Path
    meta: dict[str, str] = field(default_factory=dict)
    docs: list[Doc] = field(default_factory=list)
    files: list[tuple[str, int, str]] = field(default_factory=list)

    @property
    def title(self) -> str:
        return self.meta.get("title") or self.path.name.replace("-", " ").title()

    @property
    def url_dir(self) -> str:
        return f"courses/{self.semester}/{self.slug}"


def load_doc(path: Path, out_rel: str, fallback_title: str, strip_title: bool = False) -> Doc:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = read_front_matter(raw)
    title = meta.get("title") or first_heading(body) or fallback_title
    if strip_title:
        lines = body.splitlines()
        for idx, line in enumerate(lines):
            if line.startswith("# "):
                del lines[idx]
                if idx < len(lines) and not lines[idx].strip():
                    del lines[idx]
                break
        body = "\n".join(lines)
    return Doc(
        title=title,
        source=path,
        out_rel=out_rel,
        body_html=md_to_html(body),
        text=re.sub(r"\s+", " ", strip_tags(md_to_html(body))),
    )


def discover() -> list[Course]:
    courses: list[Course] = []
    if not COURSES_DIR.exists():
        return courses
    for sem_dir in sorted(p for p in COURSES_DIR.iterdir() if p.is_dir()):
        for cdir in sorted(p for p in sem_dir.iterdir() if p.is_dir()):
            readme = cdir / "README.md"
            meta: dict[str, str] = {}
            if readme.exists():
                meta, _ = read_front_matter(readme.read_text(encoding="utf-8", errors="replace"))
            course = Course(semester=sem_dir.name, slug=cdir.name, path=cdir, meta=meta)
            base = course.url_dir

            if readme.exists():
                course.docs.append(
                    load_doc(readme, f"{base}/index.html", course.title, strip_title=True)
                )

            notes = sorted(cdir.rglob("*.md"))
            for note in notes:
                if note == readme:
                    continue
                out_name = slugify(note.stem) + ".html"
                course.docs.append(load_doc(note, f"{base}/{out_name}", note.stem, strip_title=True))

            for f in sorted(cdir.rglob("*")):
                if not f.is_file() or f.suffix.lower() == ".md":
                    continue
                if any(part.startswith(".") for part in f.relative_to(cdir).parts):
                    continue
                rel = f.relative_to(cdir).as_posix()
                course.files.append(
                    (rel, f.stat().st_size, f"files/{course.semester}/{course.slug}/{rel}")
                )
            courses.append(course)
    return courses


# ---------------------------------------------------------------------------
# HTML shell
# ---------------------------------------------------------------------------

PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="dark" data-type="docs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%%</title>
<meta name="description" content="%%DESC%%">
<meta name="theme-color" content="#121212">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Funnel+Display:wght@400;500;600&family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" href="%%ROOT%%assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="%%ROOT%%assets/style.css">
<script>
(function(){var t=null;try{var m=/[?&]theme=(light|dark|midnight|oled)/.exec(location.search);t=m?m[1]:localStorage.getItem("opencse-theme");}catch(e){}document.documentElement.setAttribute("data-theme",t||"dark");})();
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <a class="brand" href="%%ROOT%%index.html"><span class="mark">OC</span><span>OpenCSE</span></a>
  <div class="searchwrap">
    <input id="search" type="search" placeholder="Search courses and notes" autocomplete="off" aria-label="Search">
    <kbd class="kbd">⌘K</kbd>
    <div id="results" class="results" hidden></div>
  </div>
  <div class="themebar" role="group" aria-label="Colour theme">
    <button type="button" data-theme-set="light">Light</button>
    <button type="button" data-theme-set="dark">Dark</button>
    <button type="button" data-theme-set="midnight">Midnight</button>
  </div>
</header>
<div class="layout">
  <aside class="sidebar">%%SIDEBAR%%</aside>
  <main class="content" id="main">
%%BODY%%
  </main>
</div>
<footer class="footer">
  <p class="close-line">Built by students,<br>for the batch behind us.</p>
  <div class="footer-grid">
    <div>
      <p class="foot-label">Browse</p>
      <a href="%%ROOT%%index.html">Home</a>
      <a href="%%ROOT%%courses/index.html">All courses</a>
    </div>
    <div>
      <p class="foot-label">Project</p>
      <a href="https://github.com/morozoko07-maker/opencse/blob/main/DISCLAIMER.md">Disclaimer</a>
      <a href="https://github.com/morozoko07-maker/opencse/blob/main/CONTRIBUTING.md">Contributing</a>
      <a href="https://github.com/morozoko07-maker/opencse">Source</a>
    </div>
    <div>
      <p class="foot-label">Licence</p>
      <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
      <a href="https://github.com/morozoko07-maker/opencse/blob/main/LICENSE-CODE">MIT (code)</a>
      <span class="foot-note">Notes stay open; the generator is MIT.</span>
    </div>
  </div>
  <p class="fine">Unofficial and unaffiliated. Course names, codes and syllabus topics belong to their respective institutions. Material is shared for study only.</p>
</footer>
<script>window.SITE_ROOT = "%%ROOT%%";</script>
<script src="%%ROOT%%assets/app.js"></script>
</body>
</html>
"""


def root_prefix(out_rel: str) -> str:
    depth = len(Path(out_rel).parent.parts)
    return "../" * depth


def sidebar_html(courses: list[Course], active_dir: str | None, root: str) -> str:
    by_sem: dict[str, list[Course]] = {}
    for c in courses:
        by_sem.setdefault(c.semester, []).append(c)

    active_sem = active_dir.split("/")[1] if active_dir else None
    active_year = year_label(active_sem) if active_sem else None

    parts = ['<nav class="nav">', f'<a class="nav-home" href="{root}index.html">Home</a>']
    parts.append(f'<a class="nav-home" href="{root}courses/index.html">All courses</a>')
    for label, _code, sems in YEAR_GROUPS:
        present = [s for s in sems if by_sem.get(s)]
        if not present:
            continue
        opened = " open" if label == active_year else ""
        parts.append(
            f'<details class="nav-group"{opened}>'
            f'<summary class="nav-label">{label}</summary><ul>'
        )
        for sem in present:
            if label != "First year":
                parts.append(f'<li class="nav-sublabel">{pretty_semester(sem)}</li>')
            for c in sorted(by_sem[sem], key=course_sort):
                active = " active" if c.url_dir == active_dir else ""
                parts.append(
                    f'<li><a class="nav-link{active}" href="{root}{c.url_dir}/index.html">'
                    f'<span>{html.escape(c.title)}</span></a></li>'
                )
                if c.url_dir == active_dir and len(c.docs) > 1:
                    parts.append('<li><ul class="nav-sub">')
                    for d in c.docs[1:]:
                        parts.append(
                            f'<li><a href="{root}{d.out_rel}">{html.escape(d.title)}</a></li>'
                        )
                    parts.append("</ul></li>")
        parts.append("</ul></details>")
    parts.append("</nav>")
    return "\n".join(parts)


def page(out_rel: str, title: str, body: str, courses: list[Course], active: str | None, desc: str = SITE_DESC) -> None:
    root = root_prefix(out_rel)
    full_title = SITE_NAME if title == SITE_NAME else f"{title} · {SITE_NAME}"
    out = (
        PAGE.replace("%%TITLE%%", html.escape(full_title))
        .replace("%%DESC%%", html.escape(desc))
        .replace("%%ROOT%%", root)
        .replace("%%SIDEBAR%%", sidebar_html(courses, active, root))
        .replace("%%BODY%%", body)
    )
    dest = SITE_DIR / out_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")


def badge(label: str, value: str, kind: str = "") -> str:
    cls = f"badge {kind}".strip()
    return f'<span class="{cls}"><span class="badge-k">{html.escape(label)}</span>{html.escape(value)}</span>'


def plural(n: int, word: str) -> str:
    return f"{n} {word}" + ("" if n == 1 else "s")


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def render_index(courses: list[Course]) -> None:
    by_sem: dict[str, list[Course]] = {}
    for c in courses:
        by_sem.setdefault(c.semester, []).append(c)

    total_docs = sum(len(c.docs) for c in courses)
    total_files = sum(len(c.files) for c in courses)
    total_bytes = sum(f[1] for c in courses for f in c.files)
    years = [g for g in YEAR_GROUPS if any(by_sem.get(s) for s in g[2])]
    first_anchor = slugify(years[0][0]) if years else "first-year"

    parts = [
        '<section class="hero">',
        '<div class="hero-copy">',
        '<p class="eyebrow">Unofficial · student-run</p>',
        '<h1>Notes for the<br>CSE syllabus.</h1>',
        '<p class="lede">Every subject from first year to final project, in one place: '
        "written summaries, previous year papers and lab work, organised so the next "
        "batch starts further ahead than we did.</p>",
        '<div class="hero-actions">'
        f'<a class="btn" href="#{first_anchor}">Start with {years[0][0].lower()}</a>'
        '<a class="link" href="courses/index.html">All courses<span class="arrow">→</span></a>'
        "</div>",
        "</div>",
        '<aside class="hero-index">',
        '<p class="index-label">Contents</p>',
        "<ol>",
    ]
    for label, code, sems in years:
        n = sum(len(by_sem.get(s, [])) for s in sems)
        parts.append(
            f'<li><a href="#{slugify(label)}"><span class="ix-n">{code}</span>'
            f'<span class="ix-t">{label}</span>'
            f'<span class="ix-c">{plural(n, "course")}</span></a></li>'
        )
    parts += [
        "</ol>",
        f'<p class="index-note">{plural(len(courses), "course")} · '
        f'{plural(total_docs, "page")}<br>{plural(total_files, "file")} · '
        f"{human_size(total_bytes)}</p>",
        "</aside>",
        "</section>",
    ]

    for label, code, sems in years:
        present = [s for s in sems if by_sem.get(s)]
        n = sum(len(by_sem[s]) for s in present)
        parts.append(
            f'<section class="sem-block" id="{slugify(label)}">'
            f'<div class="sem-head"><h2><span class="num">{code}</span>{label}</h2>'
            f'<span class="count">{plural(n, "course")}</span></div>'
        )
        if label == "First year":
            parts.append(
                '<p class="sem-note">First year runs two cycles. Both subject sets are '
                "listed here; you take one cycle each semester.</p>"
            )
        for sem in present:
            if label != "First year":
                parts.append(f'<p class="sem-sub">{pretty_semester(sem)}</p>')
            parts.append('<div class="cards">')
            for i, c in enumerate(sorted(by_sem[sem], key=course_sort), 1):
                chips = []
                if c.meta.get("cycle"):
                    chips.append(f'<span class="chip">{html.escape(c.meta["cycle"])} cycle</span>')
                if c.meta.get("credits"):
                    chips.append(
                        f'<span class="chip">{html.escape(c.meta["credits"])} credit'
                        f'{"s" if c.meta["credits"] != "1" else ""}</span>'
                    )
                summary = c.meta.get("summary", "")
                pending = not c.files and len(c.docs) <= 1
                cls = "card pending" if pending else "card"
                meta = (
                    "Awaiting material"
                    if pending
                    else f"{plural(len(c.docs), 'page')} · {plural(len(c.files), 'file')}"
                )
                parts.append(
                    f'<a class="{cls}" href="{c.url_dir}/index.html">'
                    f'<div class="card-top"><span class="card-num">{i:02d}</span>'
                    f'<span class="card-code">{html.escape(c.meta.get("code", "—"))}</span></div>'
                    f'<h3>{html.escape(c.title)}</h3>'
                    f'<p>{html.escape(summary) if summary else "Notes and resources."}</p>'
                    f'<div class="chips">{"".join(chips)}</div>'
                    f'<div class="card-foot"><span class="card-meta">{meta}</span>'
                    f'<span class="card-go">{"" if pending else "→"}</span></div>'
                    "</a>"
                )
            parts.append("</div>")
        parts.append("</section>")

    page("index.html", SITE_NAME, "\n".join(parts), courses, None)


def render_all_courses(courses: list[Course]) -> None:
    rows = []
    for c in sorted(courses, key=lambda x: (x.semester, x.title.lower())):
        rows.append(
            f'<tr><td><a href="../{c.url_dir}/index.html">{html.escape(c.title)}</a></td>'
            f'<td>{html.escape(c.meta.get("code", "—"))}</td>'
            f"<td>{pretty_semester(c.semester)}</td>"
            f"<td>{len(c.docs)}</td><td>{len(c.files)}</td></tr>"
        )
    body = (
        "<h1>All courses</h1>"
        '<table><thead><tr><th>Course</th><th>Code</th><th>Semester</th><th>Pages</th><th>Files</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )
    page("courses/index.html", "All courses", body, courses, None)


def render_course(course: Course, courses: list[Course]) -> None:
    out_rel = f"{course.url_dir}/index.html"
    main_doc = course.docs[0] if course.docs else None

    badges = []
    if course.meta.get("code"):
        badges.append(badge("Code", course.meta["code"]))
    if course.meta.get("credits"):
        badges.append(badge("Credits", course.meta["credits"]))
    if course.meta.get("cie"):
        badges.append(badge("CIE", course.meta["cie"], "cie"))
    if course.meta.get("see"):
        badges.append(badge("SEE", course.meta["see"], "see"))

    root = root_prefix(out_rel)
    parts = [
        f'<p class="crumb"><a href="{root}index.html">Courses</a> / '
        f'<a href="{root}courses/index.html">'
        f"{pretty_semester(course.semester)}</a></p>",
        f"<h1>{html.escape(course.title)}</h1>",
        f'<div class="badges">{"".join(badges)}</div>',
    ]
    if course.meta.get("summary"):
        parts.append(f'<p class="lede">{html.escape(course.meta["summary"])}</p>')

    rev = next((d for d in course.docs if d.title.lower().startswith("revision")), None)
    if rev:
        heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', rev.body_html, flags=re.S)
        skip = {"exam-pattern", "question-bank", "last-24-hours"}
        topics = [
            (hid, strip_tags(re.sub(r'<a class="anchor".*?</a>', "", h)).strip())
            for hid, h in heads if hid not in skip
        ]
        if len(topics) >= 3:
            link = Path(rev.out_rel).name
            parts.append('<nav class="topics"><p class="topics-label">Topics</p><ul>'
                         + "".join(f'<li><a href="{link}#{hid}">{html.escape(txt)}</a></li>'
                                   for hid, txt in topics)
                         + "</ul></nav>")

    if main_doc:
        parts.append(toc_html(main_doc.body_html))

    if course.files:
        total = sum(item[1] for item in course.files)
        cats = {}
        for item in course.files:
            cats.setdefault(classify_material(item[0]), []).append(item)
        parts.append('<section class="section"><h2>Material <span class="section-count">'
                     + plural(len(course.files), "file") + " \u00b7 " + human_size(total)
                     + '</span></h2>')
        parts.append('<p class="section-note">Grouped by what the file is: lab work, '
                     'notes, question banks, slides. Open a section to browse.</p>')
        for cat in MATERIAL_CATEGORIES:
            items = cats.get(cat)
            if not items:
                continue
            gsize = sum(i[1] for i in items)
            opened = " open" if len(items) <= 6 else ""
            parts.append('<details class="filegroup"' + opened + '><summary>'
                         '<span class="fg-name">' + cat + '</span>'
                         '<span class="fg-meta">' + plural(len(items), "file") + " \u00b7 "
                         + human_size(gsize) + '</span></summary><ul class="filelist">')
            for rel, size, url in sorted(items):
                ext = Path(rel).suffix.lstrip(".").upper() or "FILE"
                leaf = rel.rsplit("/", 1)[-1]
                folder = rel.rsplit("/", 2)[-2] if rel.count("/") >= 2 else ""
                if folder == "material":
                    folder = ""
                meta = " \u00b7 ".join(x for x in (folder, ext, human_size(size)) if x)
                parts.append('<li><a href="' + root + quote(url) + '">'
                             '<span class="fname">' + html.escape(leaf) + '</span>'
                             '<span class="fmeta">' + html.escape(meta) + '</span></a></li>')
            parts.append("</ul></details>")
        parts.append("</section>")
    else:
        parts.append('<section class="section"><h2>Material</h2><p class="empty">'
                     "No material yet. Drop files into <code>"
                     + html.escape(course.path.relative_to(ROOT).as_posix())
                     + "</code> and rebuild.</p></section>")

    if main_doc:
        parts.append(f'<article class="prose">{main_doc.body_html}</article>')
        if len(course.docs) > 1:
            parts.append('<section class="section"><h2>Study pages</h2><ul class="pagelist">')
            for d in course.docs[1:]:
                parts.append(
                    f'<li><a href="{Path(d.out_rel).name}">{html.escape(d.title)}</a></li>'
                )
            parts.append("</ul></section>")

    parts.append(
        '<p class="editnote">Have notes, a paper or a correction? '
        '<a href="https://github.com/morozoko07-maker/opencse/blob/main/CONTRIBUTING.md">'
        "Send a pull request</a> — that is how everything here gets added.</p>"
    )
    page(out_rel, course.title, "\n".join(parts), courses, course.url_dir,
         desc=course.meta.get("summary", SITE_DESC))

    # Sub-pages (notes/*.md)
    for d in course.docs[1:]:
        droot = root_prefix(d.out_rel)
        body = (
            f'<p class="crumb"><a href="{droot}index.html">Courses</a> / '
            f'<a href="index.html">{html.escape(course.title)}</a></p>'
            f"<h1>{html.escape(d.title)}</h1>"
            f"{toc_html(d.body_html)}"
            f'<article class="prose">{d.body_html}</article>'
            f'<p class="editnote">Source: <code>{html.escape(d.source.relative_to(ROOT).as_posix())}</code></p>'
        )
        page(d.out_rel, f"{course.title}: {d.title}", body, courses, course.url_dir)


def render_search_index(courses: list[Course]) -> None:
    entries = []
    for c in courses:
        for d in c.docs:
            entries.append(
                {
                    "t": d.title,
                    "c": c.title,
                    "code": c.meta.get("code", ""),
                    "u": d.out_rel,
                    "x": d.text[:6000],
                }
            )
    (SITE_DIR / "search-index.json").write_text(
        json.dumps(entries, ensure_ascii=False), encoding="utf-8"
    )


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="6" fill="#0c0c0c"/>
<rect x=".5" y=".5" width="63" height="63" rx="5.5" fill="none" stroke="#3a3a3a"/>
<text x="32" y="42" font-family="ui-monospace,Menlo,monospace" font-size="22" font-weight="700"
 fill="#e9e7e2" text-anchor="middle">OC</text></svg>
"""


def main() -> int:
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    shutil.copytree(ASSETS_DIR, SITE_DIR / "assets")
    (SITE_DIR / "assets" / "favicon.svg").write_text(FAVICON, encoding="utf-8")

    courses = discover()
    for course in courses:
        for rel, _size, url in course.files:
            src = course.path / rel
            dest = SITE_DIR / url
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)

    render_index(courses)
    render_all_courses(courses)
    for course in courses:
        render_course(course, courses)
    render_search_index(courses)

    print(f"Built {len(courses)} courses, {sum(len(c.docs) for c in courses)} pages, "
          f"{sum(len(c.files) for c in courses)} files -> {SITE_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
