#!/usr/bin/env python3
from __future__ import annotations

import argparse
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


def collect_entries(section_dir: Path) -> list[tuple[int, str]]:
    entries: list[tuple[int, str]] = []
    for path in section_dir.iterdir():
        if not path.is_file():
            continue
        m = PROBLEM_FILE_RE.match(path.name)
        if not m:
            continue
        num = int(m.group(2))
        content = _collapse_ws(path.read_text(encoding="utf-8", errors="replace"))
        if not content:
            content = "<EMPTY>"
        entries.append((num, content))
    entries.sort(key=lambda t: t[0])
    return entries


def write_index(repo_root: Path, section: str, entries: list[tuple[int, str]], dry_run: bool) -> None:
    out_path = repo_root / f"{section}.md"
    lines = [f"{section}{num}: {content}" for num, content in entries]
    payload = "\n".join(lines) + ("\n" if lines else "")
    if dry_run:
        return
    out_path.write_text(payload, encoding="utf-8")


def validate(section: str, entries: list[tuple[int, str]]) -> list[str]:
    problems: list[str] = []
    expected = EXPECTED_COUNTS.get(section)
    if expected is not None and len(entries) != expected:
        problems.append(f"{section}: expected {expected} files, found {len(entries)}")
    nums = [n for n, _ in entries]
    if nums:
        duplicates = {n for n in nums if nums.count(n) > 1}
        if duplicates:
            problems.append(f"{section}: duplicate numbers: {sorted(duplicates)}")
        missing = []
        if expected is not None:
            have = set(nums)
            missing = [n for n in range(1, expected + 1) if n not in have]
        if missing:
            problems.append(f"{section}: missing: {missing}")
    return problems


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate section index files (A.md, B.md, ...) from section folders (A/A1.md, ...).",
    )
    parser.add_argument(
        "--sections",
        nargs="*",
        default=["A", "B", "C", "D", "E", "F"],
        help="Sections to generate (default: A B C D E F).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write any files.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero if counts/gaps look wrong.",
    )
    args = parser.parse_args(argv)

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    sections = [s.strip().upper() for s in args.sections]
    for s in sections:
        if s not in EXPECTED_COUNTS:
            print(f"Unknown section: {s} (expected one of A-F)", file=sys.stderr)
            return 2

    all_problems: list[str] = []
    for section in sections:
        section_dir = repo_root / section
        if not section_dir.exists():
            print(f"Missing section folder: {section_dir}", file=sys.stderr)
            all_problems.append(f"{section}: missing folder")
            continue
        entries = collect_entries(section_dir)
        all_problems.extend(validate(section, entries))
        write_index(repo_root, section, entries, dry_run=args.dry_run)
        print(f"{section}: wrote {section}.md with {len(entries)} entries")

    if args.check and all_problems:
        print("\nProblems:", file=sys.stderr)
        for p in all_problems:
            print(f"- {p}", file=sys.stderr)
        return 1

    if all_problems:
        print("\nWarnings:")
        for p in all_problems:
            print(f"- {p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

