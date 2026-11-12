"""AQ2 step 1 – extract the association table from the day-27 feature view.

--scope 2013  the 9 development runs (estimation; allowed before the AQ3 freeze)
--scope 2014  the 13 test runs (replication; only after the AQ3 test, Change Log C14 – the guard enforces it)

Writes extracted-datasets/aq2_signs_d27_<scope>.csv: one row per enrolment registered at day 27, with the outcome,
the five binary signs (PROTOCOL.md P16), their sensitivity variants, the adjustment columns and the audit columns;
and results/sign_calendar_<scope>.csv: per run, which task types are due by day 27 and how many enrolments carry each
sign. The calendar decides where a task sign is defined: `run_has_task_due` (a TMA or CMA due by day 27) for the
missed-task sign, `run_has_tma_due` (a TMA due by day 27) for the late-TMA sign.
"""

import argparse

import polars as pl

from aq2_model import ACTIVITY_LEVELS5, CONTINUOUS_ACTIVITY, EXTRACT, RESULTS, activity_level5, lib

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--scope", choices=["2013", "2014"], required=True)
scope = p.parse_args().scope
lib.banner(f"AQ2 extract, scope = {scope}")

if scope == "2013":
    f = lib.load_features(27, "train")
else:
    f = lib.load_features(27, "test", "aq-2/code/01_extract.py", "AQ2 replication on the 2014 runs (Appendix III step 8)")

# Task calendar per run from the task table: which task types fall due by day 27 (no outcome column is read from it).
years = (2013,) if scope == "2013" else (2014,)
due = lib.load_view("assessment_due", years, "aq-2/code/01_extract.py", "AQ2 task calendar of the 2014 runs (due days only)")
cal = (due.filter(pl.col("due_day") <= 27).group_by("run").agg(
    (pl.col("assessment_type") == "TMA").any().alias("run_has_tma_due"),
    (pl.col("assessment_type") == "CMA").any().alias("run_has_cma_due"),
    pl.col("id_assessment").n_unique().alias("tasks_due_by_day27")))
f = f.join(cal, on="run", how="left").with_columns(pl.col("run_has_tma_due").fill_null(False), pl.col("run_has_cma_due").fill_null(False),
                                                   pl.col("tasks_due_by_day27").fill_null(0))

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
    pl.col("clicks_0c").cast(pl.Float64).log1p().alias(CONTINUOUS_ACTIVITY),
)
f = f.with_columns(pl.Series("activity_level5", activity_level5(f), dtype=pl.Utf8))
# the two definitions of "a task is due by day 27" must agree: the feature view's count and the task table's calendar
assert f.filter(pl.col("run_has_task_due") != (pl.col("run_has_tma_due") | pl.col("run_has_cma_due"))).height == 0
# a sign can only occur where it is defined
assert f.filter(pl.col("sign_tma_late") & ~pl.col("run_has_tma_due")).height == 0
assert f.filter(pl.col("sign_task_missed") & ~pl.col("run_has_task_due")).height == 0
keep = lib.KEYS + ["run", "start_month", "final_result", "non_completion", "run_has_task_due", "run_has_tma_due", "run_has_cma_due", "tasks_due_c",
                   "sign_task_missed", "sign_tma_late", "sign_inactive_last7", "sign_low_activity", "sign_no_pre_activity",
                   "sign_low_activity_q25", "sign_low_activity_median", "sign_low_activity_dedup", "sign_any_task_late",
                   "num_of_prev_attempts", "studied_credits", "clicks_pre", "clicks_0c", "clicks_0c_dedup",
                   "activity_ratio_run", "activity_ratio_run_dedup", "activity_level", "activity_level5", CONTINUOUS_ACTIVITY, "flagged", "gender", "disability", "imd_band", "age_band"]
out = f.select(keep).sort(lib.KEYS)
lib.save_csv(out, EXTRACT / f"aq2_signs_d27_{scope}.csv")
tma, task = out.filter(pl.col("run_has_tma_due")), out.filter(pl.col("run_has_task_due"))
print(f"\nenrolments: {out.height:,}; runs: {out['run'].n_unique()}; non-completion rate: {out['non_completion'].mean():.4f}")
print(f"runs with a TMA or CMA due by day 27: {task['run'].n_unique()} ({task.height:,} enrolments); "
      f"runs with a TMA due by day 27: {tma['run'].n_unique()} ({tma.height:,} enrolments)")
signs = ["sign_task_missed", "sign_tma_late", "sign_inactive_last7", "sign_low_activity", "sign_no_pre_activity",
         "sign_low_activity_q25", "sign_low_activity_median", "sign_low_activity_dedup", "sign_any_task_late"]
calendar = out.group_by("code_module", "run").agg(
    pl.len().alias("enrolments"), pl.col("run_has_task_due").first(), pl.col("run_has_tma_due").first(), pl.col("run_has_cma_due").first(),
    *[pl.col(s).sum().alias(s.replace("sign_", "with_")) for s in signs]).sort("run")
print("\n**Task calendar and number of enrolments with each sign and sensitivity variant, by run**\n")
print(lib.md_table(calendar))
lib.save_csv(calendar, RESULTS / f"sign_calendar_{scope}.csv")
lv = out.group_by("activity_level5").agg(pl.len().alias("enrolments")).sort("activity_level5")
assert set(lv["activity_level5"].to_list()) <= set(ACTIVITY_LEVELS5)
print("\n**Enrolments by activity level on days 0-27**\n\n" + lib.md_table(lv))
