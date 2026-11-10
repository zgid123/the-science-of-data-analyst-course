"""T26: every 'rate% (low–high)' written in the given report files, checked against the set of exact Wilson rates of
all AQ1 groups (year or 22 runs x denominator x overall/module/run/start month/subgroup x six measures) recomputed
from the prepared enrolment view and rounded once, half-up. Prints the rates not found.
Usage (from the repository root): venv/bin/python reports/milestone-5/code/t26_exact_text.py FILE...
"""
import re
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import polars as pl

TASK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TASK / "package" / "src" / "analysis"))
import aq_analysis as A  # noqa: E402


def f(v):
    return str(Decimal(repr(float(v))).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


enr = pl.read_parquet(A.PROC / "enrolment.parquet").with_columns(pl.col("code_presentation").str.slice(4, 1).alias("sm"))
known = set()
meas = {"nc": pl.col("non_completion"), "c": pl.col("completed")} | {
    o: pl.col("final_result") == o for o in ["Pass", "Distinction", "Fail", "Withdrawn"]}
for ycond in [pl.col("year") == 2013, pl.col("year") == 2014, pl.lit(True)]:
    for dcond in [pl.col("enrolled_d14"), pl.lit(True),
                  pl.col("enrolled_d14") & ~(pl.col("withdrawal_day_missing") | pl.col("registration_missing"))]:
        d = enr.filter(ycond & dcond)
        for keys in [[], ["code_module"], ["code_module", "code_presentation"], ["sm"], ["gender"], ["disability"],
                     ["imd_band"], ["age_band"]]:
            for _, g in (d.group_by(keys) if keys else [((), d)]):
                for e in meas.values():
                    p, lo, hi = A.wilson(int(g.select(e.sum()).item()), g.height)
                    known.add(f"{f(100 * p)}% ({f(100 * lo)}–{f(100 * hi)})")
bad = 0
for fn in sys.argv[1:]:
    text = Path(fn).read_text()
    for m in re.finditer(r"(\d+\.\d)% \((\d+\.\d)–(\d+\.\d)\)", text):
        if m.group(0) not in known:
            bad += 1
            print(f"NOT FOUND  {Path(fn).name}: {m.group(0)}   …{text[max(0, m.start() - 60):m.start()]}")
print(f"SUMMARY: {bad} rate strings not found among the exact AQ1 rates")
