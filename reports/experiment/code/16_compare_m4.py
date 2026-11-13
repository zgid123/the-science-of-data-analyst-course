"""Compare these results with the Milestone 4 Level 2 experiment (reports/milestone-4/package/results/).

The Milestone 4 tables are copied once into evidence/milestone-4/ (read-only use), so the comparison reruns from
this folder alone. Writes results/compare_m4.csv (one row per compared quantity) and results/compare_m4_runs.csv
(gate S1 per test run).
"""

import json
import shutil

import _tools  # noqa: F401
import pandas as pd

import common as c

SRC = c.ROOT.parent / "milestone-4" / "package"
EV = c.ROOT / "evidence" / "milestone-4"
FILES = ["results/aq2_replication.csv", "results/model_choice.csv", "results/s1_gate.csv", "results/s1_per_run.csv",
         "results/calibration.csv", "results/sensitivity.csv", "results/fairness.csv", "results/secondary.csv",
         "models/frozen_M1_d27.spec.json"]
for f in FILES:
    dest = EV / f.replace("/", "__")
    if not dest.exists():
        EV.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SRC / f, dest)
m4 = lambda f: EV / f.replace("/", "__")  # noqa: E731
R = c.RESULTS
rows = []


def add(aq, item, old, new, unit, same):
    rows.append({"aq": aq, "item": item, "milestone_4": old, "new": new,
                 "difference": (new - old) if isinstance(old, (int, float)) and isinstance(new, (int, float)) else "",
                 "unit": unit, "same_conclusion": same})


# ---- AQ2: adjusted risk differences, both years (points)
old = pd.read_csv(m4("results/aq2_replication.csv"))
old = old[old["module"] == "all"].set_index("sign")
new = pd.read_csv(R / "aq2_replication.csv").set_index("sign")
names = {"missed_task": "missed_task", "late_tma": "late_tma", "inactive_7d": "inactive_last7",
         "low_activity": "low_relative_activity", "no_prestart": "no_pre_start_activity"}
for s, o in names.items():
    for y in (2013, 2014):
        add("AQ2", f"{c.SIGN_LABEL[s]}, {y}", float(old.loc[o, f"estimate_{y}"]), round(new.loc[s, f"rd_{y}"] * 100, 2),
            "points", "yes")

# ---- AQ3 development choice (pooled normalised recall, 2013 folds, day 27, 5 per 20)
old = pd.read_csv(m4("results/model_choice.csv")).set_index("config")
new = pd.read_csv(R / "aq3_dev_summary.csv").set_index("config")
for o, n in [("M1", "M1"), ("B2", "RULE"), ("B3", "B3"), ("M2", "M2"), ("M3", "M3"), ("M4", "M4")]:
    add("AQ3 development", f"Development, {n if n != 'RULE' else 'rule'}", float(old.loc[o, "pooled_normalised_recall_d27_k5"]),
        float(new.loc[n, "norm_recall"]), "normalised recall", "yes")
add("AQ3 setup", "Chosen configuration", "M1", json.loads((R / "aq3_choices.json").read_text())["chosen_configuration"], "", "yes")
add("AQ3 setup", "M1 penalty C at day 27", str(json.loads(m4("models/frozen_M1_d27.spec.json").read_text())["params"]["C"]),
    str(json.loads((R / "aq3_choices.json").read_text())["final_hyperparameters"]["M1_d27"]["C"]), "", "no: tuning criterion differs")

# ---- AQ3 gate S1 on 2014
o = pd.read_csv(m4("results/s1_gate.csv")).iloc[0]
n = pd.read_csv(R / "aq3_s1.csv").iloc[0]
for item, oc, nc, unit in [("S1 normalised recall, model", "pooled_nr_model", "norm_recall_a", "normalised recall"),
                           ("S1 normalised recall, rule", "pooled_nr_rule", "norm_recall_b", "normalised recall"),
                           ("S1 difference", "difference", "difference", "normalised recall"),
                           ("S1 interval, low", "boot_ci_low", "low", "normalised recall"),
                           ("S1 interval, high", "boot_ci_high", "high", "normalised recall"),
                           ("S1 sign-flip p", "signflip_p", "signflip_p", "p"),
                           ("S1 runs won (of 13)", "wins", "wins", "runs")]:
    add("AQ3 test", item, float(o[oc]), float(n[nc]), unit, "yes")
runs = pd.read_csv(m4("results/s1_per_run.csv"))
runs["run"] = runs["test_run"].str.replace("_", "-")
mine = pd.read_csv(R / "aq3_test_by_run.csv")
mine = mine[mine["method"].isin(["M1", "RULE"])].pivot(index="run", columns="method", values=["tp", "norm_recall"])
mine.columns = [f"{a}_{b}" for a, b in mine.columns]
per = runs.merge(mine.reset_index(), on="run", validate="1:1")
add("AQ3 test", "Non-completers listed by the model, day 27, 5 per 20", int(per["noncompleters_on_list_model"].sum()),
    int(per["tp_M1"].sum()), "students", "yes")
add("AQ3 test", "Runs where the rule's list is identical (of 13)", 13,
    int((per["noncompleters_on_list_rule"] == per["tp_RULE"]).sum()), "runs", "yes")
out_runs = pd.DataFrame({"run": per["run"], "m4_model": per["nr_model"], "new_model": per["norm_recall_M1"],
                         "rule": per["norm_recall_RULE"], "m4_difference": per["difference"],
                         "new_difference": per["norm_recall_M1"] - per["norm_recall_RULE"]})
out_runs["same_winner"] = (out_runs["m4_difference"] > 0) == (out_runs["new_difference"] > 0)
c.write(out_runs, "compare_m4_runs.csv")

# ---- AQ3 calibration S3 (M1, day 27)
o = pd.read_csv(m4("results/calibration.csv")).query("config == 'M1' and cutoff == 27").iloc[0]
n = pd.read_csv(R / "aq3_discrimination_calibration.csv").query("method == 'M1' and cutoff == 27").iloc[0]
add("AQ3 test", "S3 calibration-in-the-large", float(o["citl"]), float(n["citl"]), "", "yes")
add("AQ3 test", "S3 calibration slope", float(o["slope"]), float(n["slope"]), "", "no: S3 fails in M4, passes pooled here")

# ---- AQ3 sensitivity views (difference model − rule)
o = pd.read_csv(m4("results/sensitivity.csv")).set_index("variant")
n = pd.read_csv(R / "aq3_sensitivity.csv").set_index("variant")
for ov, nv in [("day 13", "Day 13, 5 per 20"), ("k = 3 per 20", "Day 27, 3 per 20"), ("paired runs", "9 runs also run in 2013"),
               ("unpaired runs", "4 runs not run in 2013"), ("without module CCC", "Without module CCC"),
               ("module CCC only", "Module CCC only"), ("without students seen in 2013", "Without students seen in 2013"),
               ("without Withdrawn lacking a day", "Without Withdrawn lacking a withdrawal day")]:
    add("AQ3 sensitivity", f"{nv}", float(o.loc[ov, "difference"]), float(n.loc[nv, "difference"]),
        "normalised recall", "yes")

# ---- AQ4 fairness (day 27, 5 per 20)
o = pd.read_csv(m4("results/fairness.csv")).query("cutoff == 27 and k == 5").set_index("group")
n = pd.read_csv(R / "aq4_fairness_confirmatory.csv").set_index("group")
for og, ng in [("disability: declared", "Declared disability"), ("deprivation band: 0-10%", "Most deprived band (0–10%)"),
               ("deprivation band: missing", "Deprivation band missing")]:
    add("AQ4", f"Recall gap: {ng}", round(float(o.loc[og, "difference"]) * 100, 2), round(float(n.loc[ng, "gap"]) * 100, 2),
        "points", "yes (not flagged in both)")
d = pd.read_csv(R / "aq4_fairness_descriptive.csv").query("attribute == 'gender'").set_index("group")
add("AQ4 descriptive", "Recall, women", float(o.loc["gender: female", "recall_group"]), float(d.loc["F", "recall"]), "share", "yes")
add("AQ4 descriptive", "Recall, men", float(o.loc["gender: male", "recall_group"]), float(d.loc["M", "recall"]), "share", "yes")

out = pd.DataFrame(rows)
c.write(out, "compare_m4.csv")
print(out.to_string(index=False))

# ---- largest absolute difference per group, quoted in comparison.md
num = out[out["difference"] != ""].copy()
num["abs_difference"] = num["difference"].astype(float).abs()
summary = num.groupby("aq")["abs_difference"].max().reset_index(name="max_abs_difference")
excl = num[(num["aq"] == "AQ3 test") & ~num["item"].isin(["S1 sign-flip p", "S1 runs won (of 13)", "S3 calibration-in-the-large",
                                                         "S3 calibration slope", "Non-completers listed by the model, day 27, 5 per 20",
                                                         "Runs where the rule's list is identical (of 13)"])]
summary.loc[len(summary)] = ["AQ3 test, S1 quantities other than p and runs won", excl["abs_difference"].max()]
summary.loc[len(summary)] = ["Runs with the same winner (of 13)", int(out_runs["same_winner"].sum())]
c.write(summary, "compare_m4_summary.csv")
print(summary.to_string(index=False))
