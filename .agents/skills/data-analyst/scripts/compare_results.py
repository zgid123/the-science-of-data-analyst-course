"""Compare a result table with another implementation's table of the same quantities.

    python compare_results.py mine.csv theirs.csv --keys run,sign --cols rate,n [--tol 0.0005] [--map rate:rd_adj] [-o diff.csv]

Rows are matched on the key columns. For each compared column the two values must be equal: numbers within
`--tol` (absolute), anything else as text. `--map mine:theirs` names a column that is called differently on the
other side. Prints every difference and every key present on one side only; exit status 1 if there is any.
Use it when a teammate's code, an earlier analysis or a reference table answers the same question: a difference
is either a definition, a population or an error, and each one is explained before the report is delivered.
Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def load(path: Path, keys: list[str]) -> dict:
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    table = {tuple(r[k] for k in keys): r for r in rows}
    if len(table) != len(rows):
        raise ValueError(f"{path}: the key columns {keys} do not identify a row")
    return table


def compare(mine: Path, theirs: Path, keys: list[str], cols: list[str], tol: float = 0.0, mapping: dict | None = None) -> list[dict]:
    mapping = mapping or {}
    a, b = load(mine, keys), load(theirs, [mapping.get(k, k) for k in keys])
    out = []
    for key in sorted(set(a) | set(b)):
        if key not in a or key not in b:
            out.append({"key": "|".join(key), "column": "", "mine": "present" if key in a else "absent",
                        "theirs": "present" if key in b else "absent", "difference": "", "status": "ONE SIDE ONLY"})
            continue
        for col in cols:
            x, y = a[key][col], b[key][mapping.get(col, col)]
            try:
                diff = float(x) - float(y)
                same, shown = abs(diff) <= tol, f"{diff:.6g}"
            except ValueError:
                same, shown = x == y, ""
            out.append({"key": "|".join(key), "column": col, "mine": x, "theirs": y, "difference": shown, "status": "EQUAL" if same else "DIFFERENT"})
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare two result tables on key columns.")
    parser.add_argument("mine", type=Path)
    parser.add_argument("theirs", type=Path)
    parser.add_argument("--keys", required=True)
    parser.add_argument("--cols", required=True)
    parser.add_argument("--tol", type=float, default=0.0)
    parser.add_argument("--map", default="")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    mapping = dict(pair.split(":", 1) for pair in args.map.split(",")) if args.map else {}
    rows = compare(args.mine, args.theirs, args.keys.split(","), args.cols.split(","), args.tol, mapping)
    if args.output:
        with open(args.output, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["key", "column", "mine", "theirs", "difference", "status"])
            writer.writeheader()
            writer.writerows(rows)
    bad = [r for r in rows if r["status"] != "EQUAL"]
    for r in bad:
        print(f"{r['status']}: {r['key']} {r['column']} mine={r['mine']} theirs={r['theirs']} {r['difference']}")
    print(f"{len(rows) - len(bad)} of {len(rows)} comparisons equal (tolerance {args.tol}); RESULT:", "PASS" if not bad else "FAIL")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
