"""AQ2 step 1 – extract the association table from the day-27 feature view.

--scope 2013  the 9 development runs (estimation; allowed before the AQ3 freeze)
--scope 2014  the 13 test runs (replication; only after the AQ3 test, Change Log C14 – the guard enforces it)

Writes extracted-datasets/aq2_signs_d27_<scope>.csv: one row per enrolment registered at day 27, with the outcome,
the five binary signs (PROTOCOL.md P16), their sensitivity variants, the adjustment columns and the audit columns.
"""

import argparse

import polars as pl

from aq2_model import EXTRACT, lib

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--scope", choices=["2013", "2014"], required=True)
scope = p.parse_args().scope
lib.banner(f"AQ2 extract, scope = {scope}")

if scope == "2013":
    f = lib.load_features(27, "train")
else:
    f = lib.load_features(27, "test", "aq-2/code/01_extract.py", "AQ2 replication on the 2014 runs (Appendix III step 8)")

med = f.group_by("run").agg(pl.col("clicks_0c_dedup").median().alias("run_median_dedup"))
f = f.join(med, on="run").with_columns(
    ((pl.col("clicks_0c_dedup") + 1) / (pl.col("run_median_dedup") + 1)).alias("activity_ratio_run_dedup"),
    (pl.col("tasks_due_c").max().over("run") > 0).alias("run_has_task_due"),
)
f = f.with_columns(
    pl.col("rule_missed").alias("sign_task_missed"),
    pl.col("rule_tma_late").alias("sign_tma_late"),
    pl.col("inactive_last7").alias("sign_inactive_last7"),
    (pl.col("activity_ratio_run") < 0.5).alias("sign_low_activity"),
    (pl.col("clicks_pre") == 0).alias("sign_no_pre_activity"),
    # sensitivity variants
    (pl.col("activity_ratio_run") < 0.25).alias("sign_low_activity_q25"),
    (pl.col("activity_ratio_run") < 1.0).alias("sign_low_activity_median"),
    (pl.col("activity_ratio_run_dedup") < 0.5).alias("sign_low_activity_dedup"),
    (pl.col("tasks_late_c") >= 1).alias("sign_any_task_late"),
    (pl.col("registration_missing") | pl.col("eval_withdrawal_day_unknown")).alias("flagged"),
    pl.when(pl.col("clicks_0c") == 0).then(pl.lit("none")).when(pl.col("activity_ratio_run") < 0.5).then(pl.lit("low")).otherwise(pl.lit("normal")).alias("activity_level"),
)
keep = lib.KEYS + ["run", "start_month", "final_result", "non_completion", "run_has_task_due", "tasks_due_c",
                   "sign_task_missed", "sign_tma_late", "sign_inactive_last7", "sign_low_activity", "sign_no_pre_activity",
                   "sign_low_activity_q25", "sign_low_activity_median", "sign_low_activity_dedup", "sign_any_task_late",
                   "num_of_prev_attempts", "studied_credits", "clicks_pre", "clicks_0c", "clicks_0c_dedup",
                   "activity_ratio_run", "activity_ratio_run_dedup", "activity_level", "flagged", "gender", "disability", "imd_band", "age_band"]
out = f.select(keep).sort(lib.KEYS)
lib.save_csv(out, EXTRACT / f"aq2_signs_d27_{scope}.csv")
print(f"\nenrolments: {out.height:,}; runs: {out['run'].n_unique()}; runs with a task due by day 27: "
      f"{out.filter(pl.col('run_has_task_due'))['run'].n_unique()}; non-completion rate: {out['non_completion'].mean():.4f}")
print("\n**Share of enrolments with each sign, by module**\n")
signs = ["sign_task_missed", "sign_tma_late", "sign_inactive_last7", "sign_low_activity", "sign_no_pre_activity"]
print(lib.md_table(out.group_by("code_module").agg(pl.len().alias("enrolments"), *[pl.col(s).sum().alias(s.replace("sign_", "")) for s in signs]).sort("code_module")))
