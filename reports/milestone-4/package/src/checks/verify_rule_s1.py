"""Independent recomputation (written apart from the pipeline) of the early-sign rule's list on the 2014 test, day 27,
k = 5 per 20: listed non-completers, attainable maximum and pooled normalised recall, to compare with test_runs.csv.
Rule order: number of C10 signs (missed task, late TMA, inactive last 7 days) descending, then lower activity ratio,
then id_student ascending.
Usage: venv/bin/python reports/milestone-4/package/src/checks/verify_rule_s1.py
"""
from pathlib import Path

import polars as pl

HERE = Path(__file__).resolve()
P = HERE.parents[4] / "milestone-3" / "package" / "data" / "processed"
f = pl.read_parquet(P / "features_d27.parquet").filter(pl.col("year") == 2014)
cap = pl.read_parquet(P / "capacity_by_run.parquet").filter(pl.col("cutoff_day") == 27)
f = f.with_columns((pl.col("rule_missed").cast(pl.Int8) + pl.col("rule_tma_late").cast(pl.Int8)
                    + pl.col("inactive_last7").cast(pl.Int8)).alias("signs"))
listed = attain = 0
for (m, p), g in f.group_by(["code_module", "code_presentation"]):
    k = cap.filter((pl.col("code_module") == m) & (pl.col("code_presentation") == p))["list_tutor_5"][0]
    g = g.sort(["signs", "activity_ratio_run", "id_student"], descending=[True, False, False], nulls_last=True)
    listed += int(g.head(k)["non_completion"].sum())
    attain += min(k, int(g["non_completion"].sum()))
print(f"rule d27 k=5/20 on 2014: listed {listed}, attainable {attain}, pooled NR {listed / attain:.4f} "
      f"(pipeline: 2786, 3955, 0.704)")
