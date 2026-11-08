"""Independent recomputation of T08 headline numbers (written separately from aq_analysis.py).

Recomputes from the Milestone 3 prepared views, 2013 rows only: the AQ1 populations and non-completion counts, and
the unadjusted AQ2 risk differences of a missed task (runs with a task due by day 27) and of inactivity in the last
seven days, then compares them with results/aq_results.json values quoted in the T08 hand-back.
Usage: venv/bin/python reports/milestone-5/code/verify_T08.py
"""
from pathlib import Path
import polars as pl

P = Path(__file__).resolve().parents[2] / "milestone-3" / "package" / "data" / "processed"
EXPECT = {"all": (13529, 6959), "d14": (12076, 5515), "d27": (11811, 5245), "task_due_pop": 9960,
          "rd_missed": 50.3, "rd_inactive": 25.3}


def rd(df: pl.DataFrame, flag: pl.Expr) -> float:
    d = df.with_columns(flag.alias("s"))
    return round((d.filter(pl.col("s"))["non_completion"].mean() - d.filter(~pl.col("s"))["non_completion"].mean()) * 100, 1)


e = pl.read_parquet(P / "enrolment.parquet").filter(pl.col("year") == 2013)
f = pl.read_parquet(P / "features_d27.parquet").filter(pl.col("year") == 2013)
assert set(e["year"]) == {2013} and set(f["year"]) == {2013}
d14 = e.filter(pl.col("enrolled_d14"))
runs = f.group_by("code_module", "code_presentation").agg(pl.col("tasks_due_c").max().alias("m")).filter(pl.col("m") > 0)
ft = f.join(runs.select("code_module", "code_presentation"), on=["code_module", "code_presentation"])
got = {"all": (e.height, int(e["non_completion"].sum())), "d14": (d14.height, int(d14["non_completion"].sum())),
       "d27": (f.height, int(f["non_completion"].sum())), "task_due_pop": ft.height,
       "rd_missed": rd(ft, pl.col("tasks_missed_c") > 0), "rd_inactive": rd(f, pl.col("inactive_last7").cast(pl.Boolean))}
bad = 0
for k, v in EXPECT.items():
    ok = got[k] == v
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {k}: recomputed {got[k]}, T08 {v}")
raise SystemExit(1 if bad else 0)
