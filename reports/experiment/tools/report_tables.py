"""Write the tables of a Markdown report from result files, so that no table is typed by hand.

Mark the place of a table in the report with a pair of HTML comments (a Markdown viewer does not show them):

    <!-- table: results/rates_by_run.csv cols=run,enrolments,rate names=run:Run,rate:Non-completion pct=rate digits=1 -->
    <!-- /table -->

    python report_tables.py fill  report.md     write every marked table from its CSV
    python report_tables.py check report.md     exit 1 if a table in the report differs from its CSV

Options inside the marker, all optional: `cols=` columns to show, in order (default: all); `names=` column:Header
pairs. Quote any option whose value has a space: `"names=rate:Non-completion rate"`, `"where=day:All days"`; `pct=` columns holding proportions, shown as percentages; `points=` proportions shown
as percentage points, without the sign %; `digits=` decimals for non-integer numbers
(default 1; `digits=1,density:4` sets one column apart, and a column named there keeps its decimals on whole numbers); `where=column:value,column:value` keeps the rows that match every pair; `text=` columns shown exactly as written (labels such as years: 2013, not 2,013). A column that mixes text and numbers is a label column and is always shown as written. The CSV path is relative to the report. An empty
cell is shown as an en dash: an undefined value is never printed as 0. Numbers are rounded half up on their decimal
value, the same rule `check_report.py` uses for quoted numbers. Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import re
import shlex
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

BLOCK = re.compile(r"<!-- table: (?P<spec>.*?) -->(?P<body>.*?)<!-- /table -->", re.S)


def number(text: str, digits: int, pct: bool, points: bool = False, fixed: bool = False) -> str:
    if text.strip() == "":
        return "–"
    try:
        value = Decimal(text)
    except Exception:
        return text
    if pct or points:
        value *= 100
    elif value == value.to_integral_value() and not fixed:                        # 355 and 355.0 are both shown as 355
        return f"{int(value):,}"
    shown = f"{value.quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP):,.{digits}f}"
    if shown.startswith("-"):
        shown = "−" + shown[1:] if Decimal(shown[1:].replace(",", "")) != 0 else shown[1:]
    return shown + ("%" if pct else "")


def parse(spec: str) -> dict:
    parts = shlex.split(spec)
    options = dict(part.split("=", 1) for part in parts[1:])
    return {
        "csv": parts[0],
        "cols": options["cols"].split(",") if "cols" in options else None,
        "names": dict(pair.split(":", 1) for pair in options["names"].split(",")) if "names" in options else {},
        "pct": set(options["pct"].split(",")) if "pct" in options else set(),
        "points": set(options["points"].split(",")) if "points" in options else set(),
        "digits": {(pair.split(":", 1)[0] if ":" in pair else ""): int(pair.split(":", 1)[-1]) for pair in options.get("digits", "1").split(",")},
        "where": [pair.split(":", 1) for pair in options["where"].split(",")] if "where" in options else [],
        "text": set(options["text"].split(",")) if "text" in options else set(),
    }


def is_number(text: str) -> bool:
    try:
        Decimal(text)
    except Exception:
        return False
    return True


def render(spec: str, base: Path) -> str:
    o = parse(spec)
    with open(base / o["csv"], newline="") as fh:
        rows = list(csv.DictReader(fh))
    rows = [r for r in rows if all(r[column] == value for column, value in o["where"])]
    cols = o["cols"] or (list(rows[0].keys()) if rows else [])
    head = [o["names"].get(c, c.replace("_", " ")) for c in cols]
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join(":----" for _ in cols) + " |"]
    default = o["digits"].get("", 1)
    labels = o["text"] | {c for c in cols if any(r[c].strip() and not is_number(r[c]) for r in rows)}

    def cell(r, c):
        if c in labels:
            return r[c] if r[c].strip() else "–"
        return number(r[c], o["digits"].get(c, default), c in o["pct"], c in o["points"], c in o["digits"])

    lines += ["| " + " | ".join(cell(r, c) for c in cols) + " |" for r in rows]
    return "\n".join(lines)


def process(report: Path, write: bool) -> list[str]:
    text, problems = report.read_text(), []

    def swap(match: re.Match) -> str:
        table = render(match["spec"], report.parent)
        if match["body"].strip() != table:
            problems.append(shlex.split(match["spec"])[0])
        return f"<!-- table: {match['spec']} -->\n{table}\n<!-- /table -->"

    new = BLOCK.sub(swap, text)
    if write:
        report.write_text(new)
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fill or check the marked tables of a Markdown report.")
    parser.add_argument("command", choices=["fill", "check"])
    parser.add_argument("report", type=Path)
    args = parser.parse_args(argv)
    blocks = len(BLOCK.findall(args.report.read_text()))
    problems = process(args.report, write=args.command == "fill")
    if args.command == "fill":
        print(f"{blocks} tables written from result files ({len(problems)} changed)")
        return 0
    for name in problems:
        print(f"FAIL table from {name} differs from the report")
    print(f"{blocks} tables compared; RESULT:", "PASS" if not problems else "FAIL")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
