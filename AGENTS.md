Ultimate Goal: Create separate .md files for each problem in Richard Guy's book "Unsolved Problems in Number Theory" (`/home/rahidz/coding/unsolved/guy2004.pdf`), including each problem's status (solved/unsolved) and, later, current research status for unsolved problems.

Scope and counts:
- A1 to A20
- B1 to B50
- C1 to C21
- D1 to D29
- E1 to E38
- F1 to F32

File layout and naming:
- One .md per problem, named like `A1.md`, `B37.md`, etc.
- Group by section folder: `A/A1.md`, `B/B37.md`, etc.

Environment:
- WSL on Windows 11.
- Work in `/home/rahidz/coding/unsolved`.

Workflow:
- Create `TODO.md` at repo root (from scratch) and follow it.
- For now, focus on text extraction, formatting, and categorization only.
- Defer research on current status for unsolved problems until later.

Extraction rules:
- Copy problem statements verbatim from the PDF.
- Include section references (e.g., section/heading/page as available in the PDF).

Proposed per-problem template (can adjust later):
```
# <Problem ID> — <Short Title if present in text>

## Source
- Book: Unsolved Problems in Number Theory (Richard K. Guy)
- Section: <section/heading>
- Page: <page number>

## Status
- Solved?: <Yes/No/Unknown>
- Notes: <blank for now unless stated in the text>

## Problem
<verbatim statement from PDF>

## References in Text
- <any internal references or cross-links mentioned in the problem statement>

## Research Status
- TODO (to be filled later)
```

If any software/tooling is needed to proceed, try to install it or ask the user to install it.
