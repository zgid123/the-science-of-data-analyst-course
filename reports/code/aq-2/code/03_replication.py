"""AQ2 step 3 – replication table: the 2013 estimates beside the 2014 re-estimates (Appendix III step 8; Change Log C14).

Runs only after the AQ3 test. For each sign it gives both years' adjusted risk difference with the n of its support,
the 2014 - 2013 change with a 95% interval from the two independent standard errors (PROTOCOL.md P17), and the verdict
of each year under both readings of the direction count. Writes results/replication.csv, replication_by_module.csv
and replication_sensitivity.csv (the verdict of every sign under every variant, both years side by side).
"""

import numpy as np
import polars as pl

from aq2_model import RESULTS, SIGNS, VARIANT_LABELS, Z, lib

lib.open_test_outcomes("aq-2/code/03_replication.py", "AQ2 replication table")
a, b = pl.read_csv(RESULTS / "associations_2013.csv"), pl.read_csv(RESULTS / "associations_2014.csv")
cols = ["sign", "n_support", "support_modules", "with_sign", "share_with_sign", "unadjusted_rd", "adjusted_rd", "adj_se", "adj_ci_low", "adj_ci_high",
        "modules_defined", "modules_same_direction", "modules_same_direction_interval_excludes_0", "modules_interval_includes_0", "verdict", "verdict_strict"]
rep = a.select(cols).join(b.select(cols), on="sign", suffix="_2014").with_columns(
    pl.col("sign").replace_strict(SIGNS).alias("label"),
    (pl.col("adjusted_rd_2014") - pl.col("adjusted_rd")).alias("change_2014_minus_2013"),
    (pl.col("adj_se") ** 2 + pl.col("adj_se_2014") ** 2).sqrt().alias("change_se"),
).with_columns(
    (pl.col("change_2014_minus_2013") - Z * pl.col("change_se")).alias("change_ci_low"),
    (pl.col("change_2014_minus_2013") + Z * pl.col("change_se")).alias("change_ci_high"),
).with_columns(
    ((pl.col("change_ci_low") <= 0) & (pl.col("change_ci_high") >= 0)).alias("change_interval_includes_0"),
    (pl.col("verdict") == pl.col("verdict_2014")).alias("same_verdict"),
    (pl.col("verdict_strict") == pl.col("verdict_strict_2014")).alias("same_verdict_strict"))
lib.banner("AQ2 replication: adjusted risk difference per sign, 2013 runs (estimation) and 2014 runs (replication)")
print(lib.md_table(rep.select("label", pl.col("n_support").alias("n_2013"), "adjusted_rd", "adj_ci_low", "adj_ci_high",
                              pl.col("n_support_2014").alias("n_2014"), "adjusted_rd_2014", "adj_ci_low_2014", "adj_ci_high_2014",
                              "change_2014_minus_2013", "change_ci_low", "change_ci_high", "change_interval_includes_0")))
print("\n**Verdicts**\n\n" + lib.md_table(rep.select("label", "modules_defined", "modules_same_direction", "modules_same_direction_interval_excludes_0",
                                                     "modules_interval_includes_0", "verdict", "verdict_strict", "modules_defined_2014", "modules_same_direction_2014",
                                                     "modules_same_direction_interval_excludes_0_2014", "modules_interval_includes_0_2014", "verdict_2014", "verdict_strict_2014")))
lib.save_csv(rep, RESULTS / "replication.csv")

ma, mb = pl.read_csv(RESULTS / "associations_by_module_2013.csv"), pl.read_csv(RESULTS / "associations_by_module_2014.csv")
bm = ma.join(mb, on=["sign", "code_module"], how="full", coalesce=True, suffix="_2014").sort("sign", "code_module").with_columns(
    ((pl.col("adjusted_rd") > 0) == (pl.col("adjusted_rd_2014") > 0)).alias("same_direction_point_estimates"),
    (pl.col("interval_excludes_0") & pl.col("interval_excludes_0_2014") & ((pl.col("adjusted_rd") > 0) == (pl.col("adjusted_rd_2014") > 0))).alias("both_intervals_exclude_0_same_side"))
print("\n**By module (CCC has no 2013 run; the late-TMA sign is not defined in CCC)**\n\n" + lib.md_table(bm.select(
    "sign", "code_module", "enrolments", "adjusted_rd", "adj_ci_low", "adj_ci_high", "enrolments_2014", "adjusted_rd_2014", "adj_ci_low_2014", "adj_ci_high_2014",
    "interval_excludes_0", "interval_excludes_0_2014", "same_direction_point_estimates", "both_intervals_exclude_0_same_side")))
lib.save_csv(bm, RESULTS / "replication_by_module.csv")
both = bm.filter(pl.col("adjusted_rd").is_not_null() & pl.col("adjusted_rd_2014").is_not_null())
only14 = bm.filter(pl.col("adjusted_rd").is_null())
print(f"\nsign x module cells estimated in both years: {both.height}; same direction of the point estimates: {int(both['same_direction_point_estimates'].sum())}; "
      f"interval excludes 0 on the same side in both years: {int(both['both_intervals_exclude_0_same_side'].sum())}; "
      f"2014 interval includes 0: {int((~both['interval_excludes_0_2014']).sum())}; 2013 interval includes 0: {int((~both['interval_excludes_0']).sum())}")
print(f"cells estimated in 2014 only (module CCC): {only14.height}; their interval excludes 0: {int(only14['interval_excludes_0_2014'].sum())}")
print(f"all 2014 module estimates: {mb.height}; interval excludes 0: {int(mb['interval_excludes_0'].sum())}; includes 0: {int((~mb['interval_excludes_0']).sum())}")

sa, sb = pl.read_csv(RESULTS / "sensitivity_2013.csv"), pl.read_csv(RESULTS / "sensitivity_2014.csv")
keep = ["variant", "status", "sign", "n", "adjusted_rd", "adj_ci_low", "adj_ci_high", "modules_defined", "modules_same_direction",
        "modules_same_direction_interval_excludes_0", "verdict", "verdict_strict"]
ss = sa.select(keep).join(sb.select(keep), on=["variant", "status", "sign"], suffix="_2014", maintain_order="left").with_columns(
    pl.col("sign").replace_strict({**SIGNS, **VARIANT_LABELS}).alias("label"))
print("\n**Every sign under every variant, both years (n = rows of the support)**\n\n" + lib.md_table(ss.select(
    "variant", "label", "n", "adjusted_rd", "adj_ci_low", "adj_ci_high", "modules_same_direction", "modules_defined", "verdict",
    "n_2014", "adjusted_rd_2014", "adj_ci_low_2014", "adj_ci_high_2014", "modules_same_direction_2014", "modules_defined_2014", "verdict_2014")))
lib.save_csv(ss, RESULTS / "replication_sensitivity.csv")
fails = ss.filter((pl.col("verdict") != "consistent association") | (pl.col("verdict_2014") != "consistent association"))
print(f"\nsign x variant rows where the Level 1 criterion is not met in at least one year: {fails.height} of {ss.height}")
if fails.height:
    print("\n" + lib.md_table(fails.select("variant", "status", "label", "adjusted_rd", "adj_ci_low", "verdict", "adjusted_rd_2014", "adj_ci_low_2014",
                                           "modules_same_direction_2014", "modules_defined_2014", "verdict_2014")))
assert np.isfinite(rep["change_se"].to_numpy()).all()

# What the average would be if rows without a slope were counted as differences of 0 (the error this rule prevents, P17).
cal = pl.read_csv(RESULTS / "sign_calendar_2014.csv")
any_task = int(cal.filter(pl.col("run_has_task_due"))["enrolments"].sum())
t = rep.filter(pl.col("sign") == "sign_tma_late").row(0, named=True)
diluted = t["adjusted_rd_2014"] * t["n_support_2014"] / any_task
chk = pl.DataFrame([{"sign": "sign_tma_late", "year": 2014, "n_support": t["n_support_2014"], "adjusted_rd_over_support": t["adjusted_rd_2014"],
                     "rows_of_runs_with_any_task_due": any_task, "rows_without_a_slope": any_task - t["n_support_2014"],
                     "average_if_those_rows_counted_as_0": diluted}])
print("\n**Late TMA in 2014: the average over the support against an average that counts rows without a slope as 0**\n\n" + lib.md_table(chk, digits=4))
lib.save_csv(chk, RESULTS / "late_tma_average_check.csv")
