"""Check a Markdown report against the files behind it before it is delivered.

    python check_report.py report.md [--claims claims.json] [--forbid "phrase" ...] [--allow-history]

Four checks; the exit status is 1 if any fails:

1. File references: every relative path written in backticks or as a link target exists.
2. Tables: every table marked for `report_tables.py` equals the table built from its CSV.
3. Quoted numbers (`--claims`): each claim names a cell of a result file and the sentence fragment that quotes it;
   the fragment, with the value formatted as stated, must appear in the report. Example entry:
       {"text": "{value} of the enrolments", "csv": "results/rates.csv", "where": {"run": "All"},
        "column": "rate", "format": ".1%"}
   `format` is `.1%`, `.1f`, `.0f` and the like (a trailing `%` multiplies by 100); `"scale": 100` multiplies first, for
   a proportion quoted in points, and `"abs": true` drops the sign ("0.21 points lower" for a cell of −0.206). Rounding is half up on the decimal value, as in `report_tables.py`. Cover at least
   every number in the summary, the headlines and the recommendations; a number computed from several cells needs
   its own cell in a result file. Number words ("six", "half") cannot be checked: write a claimed number in digits.
   The check counts what it covered, so a report with no claims file says so.
4. Final state only: phrases that tell the history of the work ("the rerun", "was rerun", "first run", "second run",
   "third run", "previous version", "earlier draft") do not appear; "how to rerun" is an instruction and is allowed. Add phrases with `--forbid`; switch off with `--allow-history`.

Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import report_tables  # noqa: E402

HISTORY = ["the rerun", "was rerun", "first run", "second run", "third run", "previous version", "earlier draft"]
PATH = re.compile(r"`([\w./-]+\.(?:csv|tsv|py|md|json|png|svg|html|parquet|txt|sh|sql|ipynb))`|\]\(([^)#\s]+)(?:#[^)]*)?\)")


def shown(raw: str, spec: str, scale: float = 1) -> str:
    """Format a cell as the report quotes it: '.1%' -> 40.0%, '.1f' -> 54.5, ',.0f' -> 1,200; rounded half up."""
    match = re.fullmatch(r"(,?)\.(\d+)([f%])", spec)
    if not match:
        return format(float(raw), spec)
    value = Decimal(raw) * Decimal(str(scale)) * (100 if match[3] == "%" else 1)
    digits = int(match[2])
    text = f"{value.quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP):{match[1]}.{digits}f}"
    if text.startswith("-"):
        text = "−" + text[1:] if Decimal(text[1:].replace(",", "")) != 0 else text[1:]
    return text + ("%" if match[3] == "%" else "")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(report: Path, claims: Path | None = None, forbid: list[str] = (), allow_history: bool = False) -> dict:
    text, base = report.read_text(), report.parent
    failures, counts = [], {"references": 0, "tables": 0, "claims": 0, "phrases": 0}

    for match in PATH.finditer(text):
        target = match[1] or match[2]
        if target.startswith(("http:", "https:", "mailto:")) or "*" in target:
            continue
        counts["references"] += 1
        if not (base / target).exists():
            failures.append(f"missing file: {target}")

    counts["tables"] = len(report_tables.BLOCK.findall(text))
    failures += [f"table differs from {name}" for name in report_tables.process(report, write=False)]

    for claim in json.loads(claims.read_text()) if claims else []:
        counts["claims"] += 1
        with open(base / claim["csv"], newline="") as fh:
            rows = [r for r in csv.DictReader(fh) if all(r[k] == str(v) for k, v in claim.get("where", {}).items())]
        if len(rows) != 1:
            failures.append(f"claim '{claim['text']}': {len(rows)} rows match {claim.get('where', {})} in {claim['csv']}")
            continue
        raw = rows[0][claim["column"]]
        raw = raw.lstrip("-") if claim.get("abs") else raw
        value = shown(raw, claim["format"], claim.get("scale", 1)) if claim.get("format") else raw
        expected = claim["text"].format(value=value)
        if norm(expected) not in norm(text):
            failures.append(f"not found in the report: '{expected}' ({claim['csv']}, {claim['column']})")

    for phrase in ([] if allow_history else HISTORY) + list(forbid):
        counts["phrases"] += 1
        if phrase.lower() in text.lower():
            failures.append(f"the report contains '{phrase}'")
    return {"counts": counts, "failures": failures}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a Markdown report against its result files.")
    parser.add_argument("report", type=Path)
    parser.add_argument("--claims", type=Path)
    parser.add_argument("--forbid", nargs="*", default=[])
    parser.add_argument("--allow-history", action="store_true")
    args = parser.parse_args(argv)
    result = check(args.report, args.claims, args.forbid, args.allow_history)
    c = result["counts"]
    print(f"- file references checked: {c['references']}\n- tables compared with their result files: {c['tables']}")
    print(f"- quoted numbers compared with result files: {c['claims']}" + ("" if c["claims"] else " (no claims file: prose numbers are NOT VERIFIED)"))
    print(f"- phrases searched: {c['phrases']}")
    for failure in result["failures"]:
        print("  FAIL", failure)
    print("RESULT:", "PASS" if not result["failures"] else f"FAIL ({len(result['failures'])})")
    return 1 if result["failures"] else 0


if __name__ == "__main__":
    sys.exit(main())
