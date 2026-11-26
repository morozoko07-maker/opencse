# OpenCSE

**CSE course notes, shared by students.**

An unofficial, student-run collection of notes and exam-preparation material for
Computer Science & Engineering coursework (VTU-style modules, CIE/SEE pattern).
Built so juniors start further ahead than we did.

> **Not affiliated** with any college or university. See [DISCLAIMER.md](DISCLAIMER.md).

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Build](https://github.com/morozoko07-maker/opencse/actions/workflows/pages.yml/badge.svg)](https://github.com/morozoko07-maker/opencse/actions/workflows/pages.yml)
[![Site](https://img.shields.io/badge/site-live-4f46e5)](https://morozoko07-maker.github.io/opencse/)

---

## What's inside

| Semester | Course | Code | Material |
|---|---|---|---|
| 3 | Operating Systems | 1BCS304 | syllabus outline, study order |
| 3 | Data Structures & Applications | BCS304 | 4-chapter study guide with traces and question banks |
| 3 | Object Oriented Programming with C++ | BCS306B | full Module 1–2 notes, 19 compiled programs |
| 4 | Database Management Systems | BCS403 | exam guide + schema protocol (HTML) |

Each covered subject ends with a **revision sheet** and a **question bank taken from its
actual model and IA papers**. The full syllabus is covered: **first year (both cycles) through semester 8, 49 courses**,
with 1,300+ files of model papers, question banks, notes and lab material. Anything
still missing is a folder waiting for a drop-in file.

## Themes

Two themes, no dependencies: **matte black** (default) and **warm paper**.
The toggle in the header remembers your choice; `?theme=light` or `?theme=dark`
forces one for a link.

## How it works

```
courses/
  semester-3/
    operating-systems/
      README.md      <- the course page (front matter + notes)
      notes/         <- any .md here becomes its own page
      pyq/           <- previous year questions (any file type)
      labs/          <- lab programs and reports
  semester-4/
    dbms/
      resources/     <- PDFs, PPTs, HTML guides -> shown as downloads
scripts/build.py     <- generator (Python 3.9+, no dependencies)
scripts/scaffold.py  <- creates a folder per subject from syllabus.json
syllabus.json        <- the subject list per semester
assets/              <- stylesheet and client-side JS
site/                <- generated output (git-ignored)
```

Each course `README.md` starts with a small front-matter block:

```yaml
---
title: Operating Systems
code: 1BCS304
semester: 3
credits: 3
cie: 50
see: 50
summary: One line shown on the course card.
---
```

## Build the site locally

```bash
python3 scripts/build.py
xdg-open site/index.html      # or just open the file in a browser
```

No pip install, no Node, no Hugo. Standard library only, works offline.

## Add a course

The subject list lives in `syllabus.json`. To scaffold any missing folders:

```bash
python3 scripts/scaffold.py     # safe to re-run; never overwrites a README
python3 scripts/build.py
```

That creates `courses/semester-<n>/<slug>/` with `notes/`, `pyq/`, `labs/` and a
starter README. To add a subject the file does not list, append it to
`syllabus.json` and run the two commands again.

Rules:

- One folder per course, inside `courses/semester-<n>/`.
- The folder name becomes the URL slug (`operating-systems`).
- A `.md` in the course root or in `notes/` becomes a page; everything else is
  copied and listed as a download.
- Keep files under 100 MB (GitHub's hard limit) and prefer your own writing.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections are the most valuable
contribution — if a definition is wrong or a step in a trace is missing, open an
issue or a PR.

## Licence

Two licences, split by what the file is:

- **Written content** — notes, revision sheets, course pages (`courses/`, `*.md`)
  are [CC BY-SA 4.0](LICENSE). Use and adapt freely, credit the authors, keep the
  same licence.
- **Code** — the generator, scripts and stylesheet (`scripts/`, `assets/`) are
  [MIT](LICENSE-CODE). Do whatever you like with them.

Why the split: MIT is a software licence and says nothing useful about prose,
and applying it to notes would let someone republish them under a stricter
licence. CC BY-SA keeps the notes open. Third-party material (model papers,
textbooks, slide decks) remains the property of its owners and is not covered by
either licence.
