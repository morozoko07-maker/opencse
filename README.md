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
| 4 | Database Management Systems | — | exam guide + schema protocol (HTML) |

More courses, PDFs and slide decks will be added over time. The structure is
built for that: drop a folder in, rebuild, done.

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

```bash
mkdir -p courses/semester-3/computer-networks/notes
# create courses/semester-3/computer-networks/README.md with front matter
python3 scripts/build.py
```

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

Text and notes are shared under [CC BY-SA 4.0](LICENSE): use and adapt freely,
credit the authors, keep the same licence. Third-party material remains the
property of its owners.
