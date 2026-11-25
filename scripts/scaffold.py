#!/usr/bin/env python3
"""Create a folder for every subject in syllabus.json.

Existing folders are left untouched, so it is safe to run repeatedly.

    python3 scripts/scaffold.py            # create what is missing
    python3 scripts/scaffold.py --dry-run  # only list what would be created
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES = ROOT / "courses"
SYLLABUS = ROOT / "syllabus.json"

README = """---
title: {title}
{code}semester: {sem}
{credits}summary: {summary}
---

# {title}

Material for this subject has not been written up yet. The folder structure is
ready — drop notes, question papers or reports in and rebuild.

## What belongs here

- `notes/` — written summaries; every `.md` file becomes its own page.
- `pyq/` — previous year and IA question papers.
- `labs/` — programs, outputs and lab reports.
- PDFs, slides and images — anywhere in this folder except `notes/`.

## Exam pattern

CIE 50 + SEE 50 is the usual split. Confirm the exact marks and modules against
your handout before relying on it.

> Add only material you wrote or have permission to share. No scanned textbooks
> or college slide decks.
"""


def front_matter_lines(entry: dict, sem: str) -> dict:
    return {
        "title": entry["title"],
        "code": f'code: "{entry["code"]}"\n' if entry.get("code") else "",
        "credits": f'credits: {entry["credits"]}\n' if entry.get("credits") else "",
        "summary": entry.get("summary", "Notes and resources."),
        "sem": sem,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    data = json.loads(SYLLABUS.read_text(encoding="utf-8"))
    made = 0
    for sem, entries in sorted(data.items()):
        for entry in entries:
            group = "first-year" if sem == "first-year" else f"semester-{sem}"
            cdir = COURSES / group / entry["slug"]
            if (cdir / "README.md").exists():
                continue
            print(f"create {cdir.relative_to(ROOT)}")
            made += 1
            if args.dry_run:
                continue
            for sub in ("notes", "pyq", "labs"):
                (cdir / sub).mkdir(parents=True, exist_ok=True)
                (cdir / sub / ".gitkeep").touch()
            (cdir / "README.md").write_text(
                README.format(**front_matter_lines(entry, sem)), encoding="utf-8"
            )
    print(f"{'would create' if args.dry_run else 'created'} {made} course folders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
