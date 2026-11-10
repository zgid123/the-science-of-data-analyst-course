"""T26 cross-check (task trail only, not in the package): the AQ2 2014 estimates of the Final Project Package against
the AQ2 replication computed separately by the local AQ3/AQ4 experiment (reports/milestone-4/package, not submitted).

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t26_crosscheck_replication.py
"""
from pathlib import Path

import polars as pl

ROOT = Path(__file__).resolve().parents[3]
pkg = pl.read_csv(ROOT / "reports/milestone-5/package/results/2014/aq2_associations.csv")
mods = pl.read_csv(ROOT / "reports/milestone-5/package/results/2014/aq2_module_effects.csv")
exp = pl.read_csv(ROOT / "reports/milestone-4/package/results/aq2_replication.csv")
n = bad = 0
for x in exp.iter_rows(named=True):
    if x["module"] == "all":
        a = pkg.filter(pl.col("sign") == x["sign"])["rd_adj_mutual_pp"]
    else:
        a = mods.filter((pl.col("sign") == x["sign"]) & (pl.col("module") == x["module"]))["rd_adj_mutual_pp"]
    if a.len() == 0:
        print(f"only in experiment: {x['sign']} {x['module']} {x['estimate_2014']}")
        continue
    n += 1
    ok = abs(a[0] - x["estimate_2014"]) <= 0.01
    bad += not ok
    print(f"{'MATCH' if ok else 'DIFF '} {x['sign']:<22} {x['module']:<4} package {a[0]:>7} experiment {x['estimate_2014']:>7}")
print(f"SUMMARY: {n - bad} of {n} estimates match to 0.01 pp")
