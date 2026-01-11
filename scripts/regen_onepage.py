#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


EXPECTED_COUNTS: dict[str, int] = {
    "A": 20,
    "B": 50,
    "C": 21,
    "D": 29,
    "E": 38,
    "F": 32,
}

PROBLEM_FILE_RE = re.compile(r"^([A-F])([0-9]{1,3})\.md$")


def _collapse_ws(text: str) -> str:
    return " ".join(text.strip().split())


def _escape_table_cell(text: str) -> str:
    # Markdown tables treat '|' as column separators.
    return text.replace("|", "\\|")


def collect_entries(repo_root: Path, section: str) -> list[tuple[int, str, Path]]:
    section_dir = repo_root / section
    entries: list[tuple[int, str, Path]] = []
    for path in section_dir.iterdir():
        if not path.is_file():
            continue
        m = PROBLEM_FILE_RE.match(path.name)
        if not m:
            continue
        num = int(m.group(2))
        content = _collapse_ws(path.read_text(encoding="utf-8", errors="replace"))
        entries.append((num, content, path))
    entries.sort(key=lambda t: t[0])
    return entries


def validate_section(section: str, entries: list[tuple[int, str, Path]]) -> list[str]:
    problems: list[str] = []
    expected = EXPECTED_COUNTS.get(section)
    if expected is not None and len(entries) != expected:
        problems.append(f"{section}: expected {expected} files, found {len(entries)}")
    nums = [n for n, _, _ in entries]
    if expected is not None:
        missing = [n for n in range(1, expected + 1) if n not in set(nums)]
        if missing:
            problems.append(f"{section}: missing: {missing}")
    return problems


def build_onepage(repo_root: Path, sections: list[str], out_path: Path) -> str:
    out: list[str] = []
    out.append("# Unsolved Problems in Number Theory (Guy) — One-Page Index")
    out.append("")
    out.append(
        "This page is generated from the per-problem files (`A/A1.md`, `B/B1.md`, …). "
        "For now, `Solved?` is `Unknown` and `Research Notes` is blank (to be filled in later)."
    )
    out.append("")
    out.append("Regenerate with:")
    out.append("")
    out.append("```bash")
    out_rel = out_path.relative_to(repo_root).as_posix()
    if out_rel == "ONEPAGE.md":
        out.append("python3 scripts/regen_onepage.py")
    else:
        out.append(f"python3 scripts/regen_onepage.py --out {out_rel}")
    out.append("```")
    out.append("")

    for section in sections:
        entries = collect_entries(repo_root, section)
        out.append(f"## Section {section}")
        out.append("")
        out.append("| Problem | Solved? | Research Notes |")
        out.append("|---|---|---|")
        for num, content, path in entries:
            pid = f"{section}{num}"
            # Emit links relative to the output file location so that GitHub Pages
            # works correctly when `--out docs/index.md` is used.
            rel_target = path.relative_to(repo_root)
            rel_from = out_path.parent.relative_to(repo_root)
            link = os.path.relpath(rel_target.as_posix(), start=rel_from.as_posix()).replace("\\", "/")
            problem_cell = _escape_table_cell(f"[`{pid}`]({link}) — {content}")
            out.append(f"| {problem_cell} | Unknown | |")
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a single-page GitHub-friendly index with section tables.",
    )
    parser.add_argument(
        "--sections",
        nargs="*",
        default=["A", "B", "C", "D", "E", "F"],
        help="Sections to include (default: A B C D E F).",
    )
    parser.add_argument(
        "--out",
        default="ONEPAGE.md",
        help="Output path (default: ONEPAGE.md).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write any files.")
    parser.add_argument("--check", action="store_true", help="Exit nonzero if counts/gaps look wrong.")
    args = parser.parse_args(argv)

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    sections = [s.strip().upper() for s in args.sections]
    for s in sections:
        if s not in EXPECTED_COUNTS:
            print(f"Unknown section: {s} (expected one of A-F)", file=sys.stderr)
            return 2

    problems: list[str] = []
    for s in sections:
        problems.extend(validate_section(s, collect_entries(repo_root, s)))

    out_path = repo_root / args.out
    payload = build_onepage(repo_root, sections, out_path)
    if not args.dry_run:
        out_path.write_text(payload, encoding="utf-8")

    print(f"Wrote {out_path.name} with sections: {' '.join(sections)}")

    if args.check and problems:
        print("\nProblems:", file=sys.stderr)
        for p in problems:
            print(f"- {p}", file=sys.stderr)
        return 1
    if problems:
        print("\nWarnings:")
        for p in problems:
            print(f"- {p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
