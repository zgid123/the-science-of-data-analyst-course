"""Explain the change in enrolments without clicks between the raw data (3,365) and the prepared view (V10, 3,554).

Counts enrolments with no raw click row, and enrolments whose raw clicks all fall after their unregistration day,
which the pipeline leaves out (DQ03), so that they show zero clicks in the prepared enrolment view.
Usage: venv/bin/python reports/milestone-3/code/count_zero_click_change.py
"""
from pathlib import Path

import polars as pl

PKG = Path(__file__).resolve().parent.parent / "package" / "data"
k = ["code_module", "code_presentation", "id_student"]
reg = pl.read_csv(PKG / "raw" / "studentRegistration.csv", null_values=["", "?"])
vle = pl.scan_csv(PKG / "raw" / "studentVle.csv").group_by(k).agg(
    pl.col("date").min().alias("first"), pl.col("date").max().alias("last")).collect()
e = pl.read_parquet(PKG / "processed" / "enrolment.parquet").select(k + ["total_clicks"])
d = reg.join(vle, on=k, how="left").join(e, on=k, how="left")
no_row = d.filter(pl.col("first").is_null()).height
only_after = d.filter(pl.col("first").is_not_null() & pl.col("date_unregistration").is_not_null()
                      & (pl.col("first") > pl.col("date_unregistration"))).height
zero_prepared = d.filter(pl.col("total_clicks") == 0).height
print(f"no raw click row: {no_row:,}")
print(f"all raw clicks after the unregistration day: {only_after:,}")
print(f"zero clicks in the prepared enrolment view: {zero_prepared:,} (= {no_row:,} + {zero_prepared - no_row:,})")
