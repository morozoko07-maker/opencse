# Contributing

Thanks for helping. Two ways to contribute: open an issue, or send a pull request.

## Before you add material

- **Write it yourself, or have permission.** Do not upload scanned textbooks,
  paid PDFs, or the college's own slide decks. Summaries, your own notes,
  question banks and your own lab reports are welcome.
- **Keep files under 100 MB.** GitHub rejects anything larger and this repo does
  not use Git LFS.
- **No personal data.** Remove names, roll numbers, marks and email addresses
  from screenshots and PDFs.

## Adding or improving a course

1. Fork the repo and create a branch: `git checkout -b add-subject-notes`.
2. Put the course in the right semester folder:

   ```
   courses/semester-3/operating-systems/
   ├── README.md      # required, with front matter
   ├── notes/         # your .md files -> become pages
   ├── pyq/           # previous year questions
   └── labs/          # programs and reports
   ```

3. Give the README front matter:

   ```yaml
   ---
   title: Operating Systems
   code: 1BCS304
   semester: 3
   credits: 3
   cie: 50
   see: 50
   summary: One sentence for the course card.
   ---
   ```

4. Write the body. Useful sections: what the paper covers, how CIE/SEE is split,
   a study order, common mistakes, and what to memorise.
5. Rebuild and check it renders:

   ```bash
   python3 scripts/build.py
   ```

6. Commit, push, open a PR. Describe what you added and where the material came
   from.

## Style

- British or American spelling — pick one per file and stay consistent.
- One topic per heading; keep paragraphs short.
- Prefer tables for mark splits and comparisons, code fences for anything you
  would type into a compiler, and `>` blockquotes for exam-ready definitions.
- Give every program its **output**. A program without output is half an answer.

## Reporting a mistake

Open an issue with the file path, the wrong line, and what it should say. If you
can cite the textbook page or the class where it was taught, even better.

## Licence of contributions

By contributing you agree that your text is released under
[CC BY-SA 4.0](../LICENSE), the same licence as the rest of the project.
