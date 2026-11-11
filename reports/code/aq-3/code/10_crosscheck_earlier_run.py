"""AQ3 step 10 – cross-check against the team's earlier prototype run (PROTOCOL.md P20).

The earlier run lives in reports/milestone-4/package/results/. It was not read while this prototype was built and
tested; this script is the first place where its numbers are opened. Two independent implementations of the same
frozen Level 1 design should agree on the baseline exactly and on the model closely.

Writes results/crosscheck_earlier_run.csv and results/crosscheck_per_run.csv. Skips quietly if the earlier run is absent.
"""

import sys

import polars as pl

from aq3_models import AQ, RESULTS, lib

OLD = lib.REPO / "reports" / "milestone-4" / "package" / "results"
if not (OLD / "s1_gate.csv").exists():
    print("earlier run not found – cross-check skipped")
    sys.exit(0)
lib.open_test_outcomes("aq-3/code/10_crosscheck_earlier_run.py", "cross-check with the earlier prototype run")
new, old = pl.read_csv(RESULTS / "s1_gate.csv").row(0, named=True), pl.read_csv(OLD / "s1_gate.csv").row(0, named=True)
ncal = pl.read_csv(RESULTS / "calibration.csv").filter((pl.col("cutoff") == 27) & (pl.col("model") == "M1")).row(0, named=True)
ocal = pl.read_csv(OLD / "calibration.csv").filter((pl.col("cutoff") == 27) & (pl.col("config") == "M1")).row(0, named=True)
nfz = pl.read_csv(RESULTS / "frozen_models.csv").filter((pl.col("name") == "M1") & (pl.col("cutoff") == 27))["hyperparameters"][0]
ofz = pl.read_csv(OLD / "freeze.csv").filter(pl.col("spec").str.contains("cutoff=27"))["spec"][0]
nf = pl.read_csv(AQ.parent / "aq-4" / "results" / "fairness_confirmatory.csv").filter((pl.col("ranking") == "model") & pl.col("confirmatory"))
of = pl.read_csv(OLD / "fairness.csv").filter((pl.col("cutoff") == 27) & (pl.col("k") == 5) & (pl.col("flagged") != "descriptive"))
rows = [
    ("Rule-ranked list, pooled normalised recall", new["pooled_nr_b"], old["pooled_nr_rule"]),
    ("Model M1, pooled normalised recall", new["pooled_nr_a"], old["pooled_nr_model"]),
    ("Difference model − rule", new["difference"], old["difference"]),
    ("Bootstrap interval, lower bound", new["boot_ci_low"], old["boot_ci_low"]),
    ("Bootstrap interval, upper bound", new["boot_ci_high"], old["boot_ci_high"]),
    ("Sign-flip p-value", new["signflip_p"], old["signflip_p"]),
    ("Runs won by the model (of 13)", float(new["wins"]), float(old["wins"])),
    ("Calibration-in-the-large, M1, day 27", ncal["citl"], ocal["citl"]),
    ("Calibration slope, M1, day 27", ncal["slope"], ocal["slope"]),
]
for g_new, g_old in [("Declared disability", "disability: declared"), ("Deprivation band 0–10%", "deprivation band: 0-10%"), ("Deprivation band missing", "deprivation band: missing")]:
    rows.append((f"Fairness gap in recall, {g_new}", nf.filter(pl.col("group") == g_new)["gap"][0], of.filter(pl.col("group") == g_old)["difference"][0]))
cc = pl.DataFrame({"quantity": [r[0] for r in rows], "this_prototype": [r[1] for r in rows], "earlier_run": [r[2] for r in rows]}).with_columns(
    (pl.col("this_prototype") - pl.col("earlier_run")).alias("difference"))
lib.banner("Cross-check: this prototype against the team's earlier run (same frozen Level 1 design, independent code)")
print(lib.md_table(cc, digits=4))
lib.save_csv(cc, RESULTS / "crosscheck_earlier_run.csv")
print(f"\nS1 verdict: this prototype {new['verdict']}; earlier run {old['verdict']}.")
print(f"S3 at day 27: this prototype {'met' if ncal['s3_bounds_met'] else 'not met'}; earlier run '{ocal['s3_verdict']}'.")
print(f"Frozen M1 penalty at day 27: this prototype {nfz}; earlier run: {ofz}")
pr_new = pl.read_csv(RESULTS / "s1_gate_per_run.csv").select("run", pl.col("tp_a").alias("model_new"), pl.col("tp_b").alias("rule_new"))
pr_old = pl.read_csv(OLD / "s1_per_run.csv").select(pl.col("test_run").str.replace("_", "-").alias("run"), pl.col("noncompleters_on_list_model").alias("model_earlier"),
                                                    pl.col("noncompleters_on_list_rule").alias("rule_earlier"))
pr = pr_new.join(pr_old, on="run").with_columns((pl.col("rule_new") == pl.col("rule_earlier")).alias("rule_identical"), (pl.col("model_new") - pl.col("model_earlier")).alias("model_difference")).sort("run")
print("\n**Non-completers on the list per run**\n\n" + lib.md_table(pr))
print(f"\nrule list identical in {int(pr['rule_identical'].sum())} of {pr.height} runs; model lists differ by {int(pr['model_new'].sum()) - int(pr['model_earlier'].sum()):+d} non-completers in total "
      f"(largest per-run difference {int(pr['model_difference'].abs().max())}).")
lib.save_csv(pr, RESULTS / "crosscheck_per_run.csv")
