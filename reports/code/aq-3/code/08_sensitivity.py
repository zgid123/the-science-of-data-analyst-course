"""AQ3 step 8 – sensitivity analyses (Appendix III step 7). None of them can change the S1 verdict.

Each variant reports the S1 quantities for the chosen model against the rule-ranked list.
Writes results/sensitivity.csv and results/sensitivity_per_run_labels_available.csv.
"""

import json

import polars as pl

from aq3_models import EXTRACT, RESULTS, gate, lib

lib.open_test_outcomes("aq-3/code/08_sensitivity.py", "sensitivity analyses of the S1 comparison")
chosen = json.loads(lib.FREEZE_FILE.read_text())["chosen_config"]
d27 = pl.read_csv(EXTRACT / "aq3_test_scored_d27.csv")
d13 = pl.read_csv(EXTRACT / "aq3_test_scored_d13.csv")
LA = f"{chosen}_labels_available"

variants = [
    ("MAIN: all 13 runs, day 27, 5 per 20 (the S1 gate)", d27, chosen, "B2_rule", 5),
    ("Paired runs (9): module and start month also ran in 2013", d27.filter(pl.col("paired_run")), chosen, "B2_rule", 5),
    ("Unpaired runs (4): CCC-B, CCC-J, EEE-B, GGG-B", d27.filter(~pl.col("paired_run")), chosen, "B2_rule", 5),
    ("Module CCC only (2 runs; module absent from training)", d27.filter(pl.col("code_module") == "CCC"), chosen, "B2_rule", 5),
    ("Without module CCC (11 runs)", d27.filter(pl.col("code_module") != "CCC"), chosen, "B2_rule", 5),
    ("Without test enrolments of students seen in 2013", d27.filter(~pl.col("student_in_training_runs")), chosen, "B2_rule", 5),
    ("Without Withdrawn enrolments that lack a withdrawal day", d27.filter(~pl.col("eval_withdrawal_day_unknown")), chosen, "B2_rule", 5),
    ("Rule variant that also counts late CMAs", d27, chosen, "B2_rule_cma", 5),
    ("Labels-available: 2014 February runs, model trained on 2013 February runs only", d27.filter(pl.col("start_month") == "B"), LA, "B2_rule", 5),
    ("Same February runs, model trained on all 2013 runs (for comparison)", d27.filter(pl.col("start_month") == "B"), chosen, "B2_rule", 5),
    ("Day 27, 3 per 20", d27, chosen, "B2_rule", 3),
    ("Day 13, 5 per 20", d13, chosen, "B2_rule", 5),
    ("Day 13, 3 per 20", d13, chosen, "B2_rule", 3),
]
rows = []
for name, df, a, b, per20 in variants:
    g = gate(df, a, b, per20)
    s = g["summary"]
    rows.append({"variant": name, "runs": s["runs"], "enrolments": s["enrolments"], "model_nr": s["pooled_nr_a"], "rule_nr": s["pooled_nr_b"],
                 "difference": s["difference"], "boot_ci_low": s["boot_ci_low"], "boot_ci_high": s["boot_ci_high"], "signflip_p": s["signflip_p"],
                 "wins": s["wins"], "ties": s["ties"], "losses": s["losses"], "extra_non_completers_listed": s["tp_a"] - s["tp_b"],
                 "would_pass_s1_conditions": s["passes"]})
    if name.startswith("Labels-available"):
        lib.save_csv(g["per_run"], RESULTS / "sensitivity_per_run_labels_available.csv")
out = pl.DataFrame(rows)
lib.banner(f"Sensitivity of the comparison model ({chosen}) − rule")
print(lib.md_table(out, digits=4))
print("\nWith fewer than 6 runs the sign-flip test cannot reach p < 0.05 (2 runs: smallest p = 0.25; 4 runs: 0.0625), so "
      "'would_pass_s1_conditions' is not informative for the small subsets; read their difference and interval.")
lib.save_csv(out, RESULTS / "sensitivity.csv")
