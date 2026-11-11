"""AQ2 step 3 – replication table: the 2013 estimates beside the 2014 re-estimates (Appendix III step 8; Change Log C14).

Runs only after the AQ3 test. Writes results/replication.csv and results/replication_by_module.csv.
"""

import polars as pl

from aq2_model import RESULTS, SIGNS, lib

lib.open_test_outcomes("aq-2/code/03_replication.py", "AQ2 replication table")
a, b = pl.read_csv(RESULTS / "associations_2013.csv"), pl.read_csv(RESULTS / "associations_2014.csv")
cols = ["sign", "with_sign", "share_with_sign", "unadjusted_rd", "adjusted_rd", "adj_ci_low", "adj_ci_high", "modules_defined", "modules_same_direction", "verdict"]
rep = a.select(cols).join(b.select(cols), on="sign", suffix="_2014").with_columns(
    pl.col("sign").replace_strict(SIGNS).alias("label"),
    (pl.col("adjusted_rd_2014") - pl.col("adjusted_rd")).alias("change_2014_minus_2013"),
    ((pl.col("adj_ci_low") <= pl.col("adj_ci_high_2014")) & (pl.col("adj_ci_low_2014") <= pl.col("adj_ci_high"))).alias("intervals_overlap"),
    (pl.col("verdict") == pl.col("verdict_2014")).alias("same_verdict"))
lib.banner("AQ2 replication: adjusted risk difference per sign, 2013 runs (estimation) and 2014 runs (replication)")
print(lib.md_table(rep.select("label", "adjusted_rd", "adj_ci_low", "adj_ci_high", "adjusted_rd_2014", "adj_ci_low_2014", "adj_ci_high_2014",
                              "change_2014_minus_2013", "intervals_overlap", "verdict", "verdict_2014")))
lib.save_csv(rep, RESULTS / "replication.csv")
ma, mb = pl.read_csv(RESULTS / "associations_by_module_2013.csv"), pl.read_csv(RESULTS / "associations_by_module_2014.csv")
bm = ma.join(mb, on=["sign", "code_module"], how="full", coalesce=True, suffix="_2014").sort("sign", "code_module").with_columns(
    ((pl.col("adjusted_rd") > 0) == (pl.col("adjusted_rd_2014") > 0)).alias("same_direction"),
    ((pl.col("adj_ci_low_2014") > 0) | (pl.col("adj_ci_high_2014") < 0)).alias("interval_2014_excludes_0"))
print("\n**By module (CCC has no 2013 run)**\n\n" + lib.md_table(bm.select("sign", "code_module", "adjusted_rd", "adj_ci_low", "adj_ci_high", "adjusted_rd_2014", "adj_ci_low_2014", "adj_ci_high_2014", "same_direction", "interval_2014_excludes_0")))
lib.save_csv(bm, RESULTS / "replication_by_module.csv")
both = bm.filter(pl.col("adjusted_rd").is_not_null() & pl.col("adjusted_rd_2014").is_not_null())
print(f"\nsign x module cells estimated in both years: {both.height}; same direction: {int(both['same_direction'].sum())}; "
      f"2014 interval excludes 0: {int(both['interval_2014_excludes_0'].sum())}")
