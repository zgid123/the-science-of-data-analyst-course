"""Renumber table captions and table cross-references in the Milestone 4 report, English and Vietnamese together.

A move of a table between the main text and the appendices shifts table numbers. This script applies one mapping of
old to new numbers simultaneously (so A.1->A.5 and A.5->A.9 do not chain) to every table caption and every reference
list that follows the word "Table"/"Tables" (English) or "Bảng" (Vietnamese), for example "Table A.4", "Tables A.10
and A.11", "Tables 4.1–4.4", "Bảng A.10 và A.11". Figure, section and appendix numbers are left alone.

Usage (from the repository root):
    venv/bin/python reports/milestone-4/code/renumber_tables.py --map "A.1=A.5,A.2=A.6" [--write]
Without --write it prints each change and writes nothing.
"""
import argparse
import re
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent / "report"
NUM = r"[A-Z0-9]+\.\d+"
CONNECT = r"(?:\s*,\s*|\s+and\s+|\s+và\s+|\s+or\s+|\s+hoặc\s+|\s+to\s+|\s+đến\s+|\s*–\s*)"
LIST = re.compile(rf"(\b(?:Tables?|Bảng)\s+)({NUM}(?:{CONNECT}(?:{NUM}|\d+))*)")
TOKEN = re.compile(rf"(?<![\w.]){NUM}(?![\d])")


def apply(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    count = 0

    def fix_list(m: re.Match) -> str:
        nonlocal count

        def fix_token(t: re.Match) -> str:
            nonlocal count
            old = t.group(0)
            if old in mapping:
                count += 1
                return mapping[old]
            return old

        return m.group(1) + TOKEN.sub(fix_token, m.group(2))

    return LIST.sub(fix_list, text), count


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--map", required=True, help='comma-separated "old=new" pairs, e.g. "A.1=A.5,4.5=4.2"')
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--report", type=Path, default=REPORT)
    args = ap.parse_args()
    mapping = dict(pair.split("=") for pair in args.map.split(","))
    total = 0
    for path in sorted(args.report.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        new, n = apply(text, mapping)
        if n:
            total += n
            print(f"{path.name}: {n} reference(s)")
            if args.write:
                path.write_text(new, encoding="utf-8")
    print(f"{total} reference(s) {'renumbered' if args.write else 'to renumber (dry run)'}")


if __name__ == "__main__":
    main()
