# TODO

## 0) Prep
- [x] Confirm PDF path: `coding/unsolved/guy2004.pdf`.
- [x] Decide extraction tooling (preferred: `pdftotext`, `pdfinfo`; fallback: `python` + `pypdf`).
- [x] Install missing tooling if needed (added `qpdf`, `ocrmypdf`).

## 1) Repository structure
- [x] Create section folders: `A/`, `B/`, `C/`, `D/`, `E/`, `F/`.
- [x] Create a scratch workspace directory for temporary text files (`_extraction/`).

## 2) Short-form output format (current phase)
- [x] Use the A1 example as the canonical format: single-line, short & sweet.
- [x] Each problem file should be one line, like:
  - `<Short title>: <concise problem statement/question>`
- [x] No page numbers, background, references, or status fields for now.

## 3) Extraction workflow (repeat per section)
- [x] For each section (A–F), iterate problems in order.
- [x] For each problem:
  - [x] Locate the problem in the PDF.
  - [x] Extract only the core problem prompt (usually the first question or the most direct problem statement).
  - [x] Keep it concise; omit background paragraphs and bibliographies.
  - [x] Save as a single line in the correct file path (e.g., `A/A1.md`).

## 4) File creation checklist by section
- [x] A: `A1.md` … `A20.md` (20 files)
- [x] B: `B1.md` … `B50.md` (50 files)
- [x] C: `C1.md` … `C21.md` (21 files)
- [x] D: `D1.md` … `D29.md` (29 files)
- [x] E: `E1.md` … `E38.md` (38 files)
- [x] F: `F1.md` … `F32.md` (32 files)

## 5) Quality checks
- [x] Verify total file count: 190.
- [x] Verify naming scheme and folder placement.
- [x] Spot-check at least 2 files per section against the PDF for accuracy of the concise prompt.
- [x] Ensure every file is a single non-empty line.

## 6) Tracking and exceptions
- [x] Maintain a running log in `_extraction/issues.md` for:
  - [x] Ambiguous numbering or titles.
  - [x] Problems where the “core prompt” is unclear.
  - [x] Multi-question problems that need a split or a judgment call.
- [ ] Defer page numbers, background, references, and research status to a later phase.

## 7) Later expansion (not part of this phase)
- [ ] Add page/section references.
- [ ] Add status fields (solved/unsolved).
- [ ] Add research status and bibliographic notes.

## 8) GitHub one-page view
- [x] Generate `ONEPAGE.md` with section tables (columns: Problem, Solved?, Research Notes).
- [x] Keep `Solved?` as `Unknown` until the status/research phase.
- [x] Ensure `ONEPAGE.md` is regenerated after prompt edits.
