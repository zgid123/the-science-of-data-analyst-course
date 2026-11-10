"""AQ1 year comparison restricted to the six modules that ran in both years (module CCC ran only in 2014).

Inputs: the run-level outcome counts Milestone 3 published (data/metadata/fig_outcome_by_run.csv; all enrolments,
non-completion = Withdrawn + Fail). Uses no 2014 row of the prepared views. Writes results/compare/aq1_year_shared_modules_published.csv:
the 2013 and 2014 non-completion rates over the shared modules, the difference in percentage points with a Wald 95%
interval (as in aq1_year_difference_published.csv), and the 2014 rate of CCC alone.
Usage (from the package folder): python src/analysis/aq1_year_shared_modules.py  (run_all.sh step 09)
"""
import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[1]                                # the package folder
SRC = PKG / "data" / "metadata" / "fig_outcome_by_run.csv"
OUT = PKG / "results" / "compare" / "aq1_year_shared_modules_published.csv"

tot = {}
for r in csv.DictReader(SRC.open()):
    year = r["code_presentation"][:4]
    nc = int(r["Withdrawn"]) + int(r["Fail"])
    n = nc + int(r["Pass"]) + int(r["Distinction"])
    key = ("CCC" if r["code_module"] == "CCC" else "shared", year)
    a = tot.setdefault(key, [0, 0])
    a[0] += nc
    a[1] += n
(e13, n13), (e14, n14) = tot[("shared", "2013")], tot[("shared", "2014")]
p13, p14 = e13 / n13, e14 / n14
se = math.sqrt(p13 * (1 - p13) / n13 + p14 * (1 - p14) / n14)
ec, nc_ = tot[("CCC", "2014")]
rows = [
    ["shared modules (6)", round(p13, 4), n13, round(p14, 4), n14, round((p14 - p13) * 100, 2),
     round((p14 - p13 - 1.96 * se) * 100, 2), round((p14 - p13 + 1.96 * se) * 100, 2)],
    ["CCC (2014 only)", "", 0, round(ec / nc_, 4), nc_, "", "", ""],
]
with OUT.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["unit", "rate_2013", "n_2013", "rate_2014_published", "n_2014", "diff_pp_2014_minus_2013", "ci_low_pp", "ci_high_pp"])
    w.writerows(rows)
for r in rows:
    print(r)
assert n13 == 13529, n13  # all 2013 enrolments (results/compare/aq1_year_comparison_published.csv)
