---
title: Why this exists
---

## The problem

Every semester, the same material is collected again from scratch. Notes sit in WhatsApp groups that get archived, in personal Drive folders nobody else can open, and on the laptops of seniors who graduate and take their files with them. The next batch arrives, cannot find what it needs, and either pays for photocopies of notes that already exist or repeats the work of collecting them.

Exam patterns and internal assessment splits are passed on as folklore. A student finds out what a subject actually demands — which units carry weight, which questions repeat, how the IA marks are divided — in the week before the exam, usually from someone who learned it the same way a year earlier. Nothing is written down, so nothing improves.

## What exists today

OpenCSE is one indexed, searchable, versioned place for CSE course material. Every subject from first year to semester 8 has a page. Material on each page is sorted into manuals, notes, question banks and slides, so a student looking for a lab manual does not have to scroll past three semesters of unrelated files.

Most subjects also carry a revision sheet. Where real question papers exist, the sheet is paired with a question bank taken from those papers, showing what has actually been asked and how often. The site holds 49 courses, over 1,300 files and 47 revision sheets.

It is a static site built by a small Python script and hosted free on GitHub Pages. There are no accounts, no ads and no tracking.

Material is contributed by students through pull requests. Third-party textbooks and college slide decks are not hosted. A few source papers are image-only scans, so the question banks built from them are thinner, and say so on the page.

## What is missing

Hosting and institutional support. The site costs nothing to run, but it is not reliably reachable from campus networks, and most students will never find it by searching. It should be linked from department pages, so that a first-year student looking for a syllabus or an old paper lands on it without being told the address.

That is a small ask, and it is the bottleneck. One willing person with a server, a subdomain or a word to the department would do more for the project than another few hundred lines of code.

## What comes next: a club platform

The same approach could carry the part of student life that currently runs on group chats.

1. Every club in the college registers and gets its own page.
2. Each club posts what it does, who its office bearers are, and how to join.
3. Students apply to clubs through that page, instead of through a form that circulates once a year.
4. Clubs advertise hackathons, interviews, talks and events in one shared feed.
5. Students RSVP, see what they have attended, and check what is happening this week.

It belongs on the same site because it fails in the same way: information that lives in a chat disappears when the people holding it leave. A club page outlives its office bearers. It should follow the same rules as the notes — static where possible, no tracking, maintained by students.

## How you can help

- Send a pull request with material you already have, or a paper that is missing.
- Flag a syllabus topic or a paper we do not cover, even if you cannot supply the file.
- Volunteer to host, or point us at someone who can.
- Adopt a subject and keep its notes and question bank current as the syllabus changes.

Everything on the site began with someone deciding their own folder was worth sharing. That is still the whole method.
