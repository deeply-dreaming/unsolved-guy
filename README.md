# Unsolved Problems in Number Theory (Guy) — Problem Index

This repo is a structured, file-per-problem index for Richard K. Guy’s book **“Unsolved Problems in Number Theory” (3rd edition, 2004)**.

Current phase: **short & sweet extraction** — each problem is captured as a *single-line* prompt for quick browsing and navigation. Later phases will add page/section references, background notes, and (where appropriate) solved/unsolved + research status.

## Structure

- One Markdown file per problem, grouped by section:
  - `A/A1.md` … `A/A20.md`
  - `B/B1.md` … `B/B50.md`
  - `C/C1.md` … `C/C21.md`
  - `D/D1.md` … `D/D29.md`
  - `E/E1.md` … `E/E38.md`
  - `F/F1.md` … `F/F32.md`
- One generated section index at repo root:
  - `A.md`, `B.md`, `C.md`, `D.md`, `E.md`, `F.md`

## Conventions (current phase)

- Each per-problem file is **exactly one line**:
  - `<Short title>: <concise problem statement/question>`
- No page numbers, bibliographic references, or research notes yet.

## Regenerating section indexes

Root section index files (`A.md`, `B.md`, …) are generated from the per-problem files.

Run:

```bash
python3 scripts/regen_section_indexes.py
```

Validate counts and numbering:

```bash
python3 scripts/regen_section_indexes.py --check
```

Regenerate only a subset:

```bash
python3 scripts/regen_section_indexes.py --sections A B
```

## One-page GitHub index

If you want a single GitHub-friendly page with all sections (A–F) in tables (including placeholder columns for `Solved?` and `Research Notes`), use:

```bash
python3 scripts/regen_onepage.py
```

This generates `ONEPAGE.md`.

## Progress

- Section A: complete (`A1`–`A20`)
- Section B: complete (`B1`–`B50`)
- Section C: complete (`C1`–`C21`)
- Section D: complete (`D1`–`D29`)
- Section E: complete (`E1`–`E38`)
- Section F: complete (`F1`–`F32`)

## Task tracking

See `TODO.md` for the current workflow and checkpoints.
