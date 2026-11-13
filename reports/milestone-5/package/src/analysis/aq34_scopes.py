"""AQ3 and AQ4 views on one scope, in the same files for every scope, as aq_analysis.py does for AQ1 and AQ2.

Scopes (`--scope`) and the scores each one reads (every enrolment is scored by a model that did not see its run):
- `2013` (results/2013/): DEVELOPMENT ESTIMATES. Each of the 9 runs of 2013 is scored by the model of the
  leave-one-run-out fold that left it out (data/interim/aq3/scores_dev_d27.csv, written by aq3_develop.py). The
  Milestone 4 plan uses these folds to choose the model, not to state its performance; read them as development
  estimates beside the test.
- `2014` (results/2014/): THE TEST. The 13 runs of 2014 scored once by the models frozen on 2013
  (data/interim/aq3/scores_d27.csv and scores_d13.csv, written by aq3_test.py). The report's AQ3/AQ4 numbers come
  from this scope.
- `all` (results/all_runs/): the 22 runs pooled, 2013 runs with their development scores and 2014 runs with their
  test scores. No model is fitted on all 22 runs.

Views: lists of 5 (and 3) per 20 per run and pooled for the rule-ranked list, each configuration and a random list;
discrimination within run and calibration; recall against list length; the students on the model list only or the
rule list only; recall by slice; AQ4 yield of each contact per tutor group, list summary, reach and fairness rates.
Day 13 exists for the test scope only (the development folds were run at the main operating point, day 27).

Usage (from the package folder): python src/analysis/aq34_scopes.py --scope 2013|2014|all   (run_all.sh steps 22-24)
Writes aq3_by_run.csv, aq3_pooled.csv, aq3_discrimination_calibration.csv, aq3_capacity_curve.csv,
aq3_model_vs_rule.csv, aq3_errors_by_slice.csv, aq3_summary.md, aq4_contact_yield.csv, aq4_list_summary.csv,
aq4_reach.csv, aq4_fairness_descriptive.csv, aq4_summary.md in the scope's results folder.
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

import aq34_common as c

METHODS = ["RULE", "B3", "M1", "M2", "M3", "M4"]
NAMES = {"RULE": "Early-sign rule (ranked)", "B3": "Background-only model", "M1": "Logistic, primary predictors",
         "M2": "Logistic, extended predictors", "M3": "Boosted trees, primary", "M4": "Boosted trees, extended",
         "RANDOM": "Random list (expected)"}
BASIS = {"2013": "development estimate (2013 runs, out-of-fold)", "2014": "test (2014 runs, frozen 2013 model)"}
Z = 1.959963984540054


def wilson(k: int, n: int) -> tuple[float, float, float]:
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p, den = k / n, 1 + Z * Z / n
    mid = (p + Z * Z / (2 * n)) / den
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return (p, max(0.0, mid - half), min(1.0, mid + half))


def load(scope: str, cut: int) -> pd.DataFrame:
    """Scores of the scope joined to the audit and slice fields; each year read with its own year filter."""
    parts = []
    for year, path, basis in [(2013, c.WORK / f"scores_dev_d{cut}.csv", BASIS["2013"]),
                              (2014, c.WORK / f"scores_d{cut}.csv", BASIS["2014"])]:
        if (scope == "2013" and year != 2013) or (scope == "2014" and year != 2014) or not path.exists():
            continue
        s = pd.read_csv(path)
        f = c.features(cut, year=year)
        cols = ["final_result", "clicks_0c", "activity_ratio_run", "num_of_prev_attempts", "registration_lead",
                "rule_missed", "rule_tma_late", "inactive_last7", "gender", "age_band", "disability", "imd_band"]
        parts.append(s.merge(f[c.KEY + cols], on=c.KEY, validate="1:1").assign(basis=basis))
    if not parts:
        return pd.DataFrame()
    d = pd.concat(parts, ignore_index=True)
    d = d.merge(c.enrolment()[c.KEY + ["date_unregistration"]], on=c.KEY, how="left", validate="1:1")
    d["RULE"] = d["rule"]
    years = set(d["code_presentation"].str[:4])
    assert years <= {"2013", "2014"} and (scope == "all" or years == {scope}), f"rows outside scope {scope}: {years}"
    return d


def metrics(frame: pd.DataFrame, per20: int) -> pd.DataFrame:
    rows = [c.list_metrics(frame, m, per20).assign(method=m) for m in METHODS]
    r = c.list_metrics(frame, "RULE", per20)                  # expected values of a random list of the same length
    r["tp"] = r["k"] * r["positives"] / r["n"]
    r["recall"], r["precision"] = r["tp"] / r["positives"], r["tp"] / r["k"]
    r["lift"], r["norm_recall"] = 1.0, r["tp"] / r["attainable"]
    rows.append(r.assign(method="RANDOM"))
    return pd.concat(rows, ignore_index=True)


def main(scope: str) -> None:
    out = c.SCOPE_DIR[scope]
    label = {"2013": BASIS["2013"], "2014": BASIS["2014"], "all": "all 22 runs: 2013 out-of-fold, 2014 test"}[scope]
    chosen = json.loads((c.WORK / "freeze.json").read_text())["choices"]["chosen_configuration"]
    d27, d13 = load(scope, 27), load(scope, 13)
    assert not d27.empty, f"no scores for scope {scope}"

    by_run = metrics(d27, 5).assign(scores=label)
    c.write(by_run, out, "aq3_by_run.csv")
    pooled = []
    for cut, frame in [(27, d27), (13, d13)]:
        if frame.empty:
            continue
        for per20 in (5, 3):
            for meth, g in metrics(frame, per20).groupby("method", sort=False):
                pooled.append({"scores": label, "cutoff": cut, "per20": per20, "method": meth, "name": NAMES[meth], **c.pooled(g)})
    c.write(pd.DataFrame(pooled), out, "aq3_pooled.csv")

    disc = []
    for cut, frame in [(27, d27), (13, d13)]:
        if frame.empty:
            continue
        for meth in METHODS:
            row = {"scores": label, "cutoff": cut, "method": meth, "name": NAMES[meth],
                   "roc_auc_within_run": np.mean([roc_auc_score(g["y"], g[meth]) for _, g in frame.groupby("run")]),
                   "pr_auc_within_run": np.mean([average_precision_score(g["y"], g[meth]) for _, g in frame.groupby("run")]),
                   "base_rate_mean": frame.groupby("run")["y"].mean().mean()}
            if meth != "RULE":
                row.update(c.calibration(frame["y"].to_numpy(), frame[meth].to_numpy()))
                ok = 0
                for _, g in frame.groupby("run"):
                    cal = c.calibration(g["y"].to_numpy(), g[meth].to_numpy())
                    ok += int(-0.2 <= cal["citl"] <= 0.2 and 0.8 <= cal["slope"] <= 1.2)
                row["runs_within_s3_bounds"], row["runs"] = ok, frame["run"].nunique()
                row["s3_met_pooled"] = bool(-0.2 <= row["citl"] <= 0.2 and 0.8 <= row["slope"] <= 1.2)
            disc.append(row)
    c.write(pd.DataFrame(disc), out, "aq3_discrimination_calibration.csv")

    curve = []
    for per20 in range(1, 11):
        for meth, g in metrics(d27, per20).groupby("method", sort=False):
            if meth in (chosen, "RULE", "B3", "RANDOM"):
                curve.append({"scores": label, "per20": per20, "method": meth, "name": NAMES[meth], **c.pooled(g)})
    c.write(pd.DataFrame(curve), out, "aq3_capacity_curve.csv")

    d = d27
    d["G"] = d.groupby("run")["run"].transform(lambda x: int(np.ceil(len(x) / 20)))
    d["k"] = d.groupby("run")["run"].transform(lambda x: c.list_size(len(x), 5))
    d["rank"], d["rank_rule"] = c.rank_in_run(d, chosen), c.rank_in_run(d, "RULE")
    d["on_model"], d["on_rule"] = d["rank"] <= d["k"], d["rank_rule"] <= d["k"]
    d["n_rule_signs"] = d[["rule_missed", "rule_tma_late", "inactive_last7"]].astype(int).sum(axis=1)
    d["withdrew_7d"] = d["final_result"].eq("Withdrawn") & d["date_unregistration"].between(28, 34)
    who = []
    for name, mask in {"On both lists": d["on_model"] & d["on_rule"], "Model list only": d["on_model"] & ~d["on_rule"],
                       "Rule list only": ~d["on_model"] & d["on_rule"], "On neither list": ~d["on_model"] & ~d["on_rule"]}.items():
        g = d[mask]
        who.append({"scores": label, "group": name, "enrolments": len(g), "non_completers": int(g["y"].sum()),
                    "rate": g["y"].mean(), "fail": int((g["final_result"] == "Fail").sum()),
                    "withdrawn": int((g["final_result"] == "Withdrawn").sum()),
                    "share_with_rule_sign": (g["n_rule_signs"] > 0).mean(), "share_no_click": (g["clicks_0c"] == 0).mean(),
                    "median_activity_ratio": g["activity_ratio_run"].median(),
                    "share_previous_attempt": (g["num_of_prev_attempts"] > 0).mean()})
    c.write(pd.DataFrame(who), out, "aq3_model_vs_rule.csv")

    d["activity"] = np.select([d["clicks_0c"] == 0, d["activity_ratio_run"] < 0.5], ["none", "low"], "normal")
    d["history"] = np.where(d["num_of_prev_attempts"] > 0, "previous attempt", "first attempt")
    d["registration"] = np.where(d["registration_lead"] < 0, "registered after the start", "registered by the start")
    d["kind"] = d["final_result"]
    d["reach"] = np.where(d["withdrew_7d"], "withdrew within 7 days", "still reachable")
    err = []
    for by in ["activity", "history", "registration", "kind", "reach"]:
        for lev, g in d.groupby(by):
            pos = g[g["y"] == 1]
            err.append({"scores": label, "slice": by, "level": lev, "enrolments": len(g), "non_completers": len(pos),
                        "recall_model": pos["on_model"].mean() if len(pos) else np.nan,
                        "recall_rule": pos["on_rule"].mean() if len(pos) else np.nan,
                        "listed_model": int(g["on_model"].sum()),
                        "listed_completers_model": int((g["on_model"] & (g["y"] == 0)).sum())})
    c.write(pd.DataFrame(err), out, "aq3_errors_by_slice.csv")

    # ---- AQ4: yield of each contact, list summary, reach, fairness rates
    yld = []
    for j in range(1, 11):
        for name, col in [("model", "rank"), ("rule", "rank_rule")]:
            band = d[(d[col] > (j - 1) * d["G"]) & (d[col] <= j * d["G"])]
            p, lo, hi = wilson(int(band["y"].sum()), len(band))
            yld.append({"scores": label, "contact": j, "method": name, "students": len(band),
                        "non_completers": int(band["y"].sum()), "precision": p, "low": lo, "high": hi,
                        "base_rate": d["y"].mean()})
    c.write(pd.DataFrame(yld), out, "aq4_contact_yield.csv")
    summ = []
    for per20 in (3, 5):
        for meth in [chosen, "RULE"]:
            summ.append({"scores": label, "per20": per20, "method": "model" if meth == chosen else "rule",
                         **c.pooled(c.list_metrics(d, meth, per20))})
        r = c.list_metrics(d, "RULE", per20)
        tp = (r["k"] * r["positives"] / r["n"]).sum()
        summ.append({"scores": label, "per20": per20, "method": "random (expected)", "n": int(r["n"].sum()),
                     "k": int(r["k"].sum()), "positives": int(r["positives"].sum()), "tp": tp,
                     "attainable": int(r["attainable"].sum()), "norm_recall": tp / r["attainable"].sum(),
                     "recall": tp / r["positives"].sum(), "precision": tp / r["k"].sum(), "lift": 1.0})
    c.write(pd.DataFrame(summ), out, "aq4_list_summary.csv")
    listed = d[d["on_model"]]
    reach = {"scores": label, "listed": len(listed), "listed_non_completers": int(listed["y"].sum()),
             "withdrew_days_28_34": int((listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].between(28, 34)).sum()),
             "listed_fail": int(listed["final_result"].eq("Fail").sum()),
             "listed_withdrawn": int(listed["final_result"].eq("Withdrawn").sum())}
    reach["reachable_non_completers"] = reach["listed_non_completers"] - reach["withdrew_days_28_34"]
    c.write(pd.DataFrame([reach]), out, "aq4_reach.csv")
    desc = []
    for col in ["gender", "age_band", "disability", "imd_band"]:
        for lev, g in d.groupby(col):
            pos = g[g["y"] == 1]
            r, rlo, rhi = wilson(int(pos["on_model"].sum()), len(pos))
            lg = g[g["on_model"]]
            desc.append({"scores": label, "attribute": col, "group": lev, "enrolments": len(g), "base_rate": g["y"].mean(),
                         "selection_rate": g["on_model"].mean(), "recall": r, "recall_low": rlo, "recall_high": rhi,
                         "precision": lg["y"].mean() if len(lg) else np.nan,
                         "note": "insufficient data, not cleared" if len(g) < 400 else ""})
    c.write(pd.DataFrame(desc), out, "aq4_fairness_descriptive.csv")

    # ---- summaries
    p = pd.DataFrame(pooled).query("cutoff == 27 and per20 == 5").set_index("method")
    cal = pd.DataFrame(disc).query("cutoff == 27 and method == @chosen").iloc[0]
    act = pd.DataFrame(err).query("slice == 'activity'").set_index("level")
    head = {"2013": "Development estimates on the 9 runs of 2013 (each run scored by the leave-one-run-out model that left it out); "
                    "the plan uses them to choose the model, not to state its performance.",
            "2014": "The single test on the 13 runs of 2014 with the models frozen on 2013; gate S1 and the sensitivity views are in aq3_s1_gate.csv and aq3_sensitivity.csv.",
            "all": "The 22 runs pooled: 2013 runs with their development scores, 2014 runs with their test scores; no model is fitted on all 22 runs."}[scope]
    lines = [f"# AQ3, scope {scope}: {label}", "", head, "",
             f"- Lists of 5 per 20 at day 27, chosen model {chosen}: {int(p.loc[chosen, 'tp']):,} of {int(p.loc[chosen, 'positives']):,} "
             f"non-completers listed (recall {p.loc[chosen, 'recall']:.1%}, precision {p.loc[chosen, 'precision']:.1%}, "
             f"normalised recall {p.loc[chosen, 'norm_recall']:.3f}); rule {int(p.loc['RULE', 'tp']):,} "
             f"(normalised recall {p.loc['RULE', 'norm_recall']:.3f}); random list {p.loc['RANDOM', 'tp']:.1f}.",
             f"- Calibration of {chosen}: in the large {cal['citl']:.3f}, slope {cal['slope']:.3f}; "
             f"{int(cal['runs_within_s3_bounds'])} of {int(cal['runs'])} runs within the S3 bounds.",
             f"- Non-completers with normal activity at day 27: {int(act.loc['normal', 'non_completers']):,}; "
             f"the model lists hold {act.loc['normal', 'recall_model']:.1%} of them."]
    (out / "aq3_summary.md").write_text("\n".join(lines) + "\n")
    y5 = pd.DataFrame(yld).query("method == 'model'").set_index("contact")
    lines4 = [f"# AQ4, scope {scope}: {label}", "", head, "",
              f"- Yield of the n-th contact per tutor group of 20 (model): 1st {y5.loc[1, 'precision']:.1%}, "
              f"5th {y5.loc[5, 'precision']:.1%}, 7th {y5.loc[7, 'precision']:.1%}; base rate {y5.loc[1, 'base_rate']:.1%}.",
              f"- Lists of 5 per 20: {reach['listed_non_completers']:,} non-completers among {reach['listed']:,} listed; "
              f"{reach['withdrew_days_28_34']} withdraw in days 28–34; {reach['listed_fail']:,} fail at the end."]
    if scope == "2014":
        lines4.append("- Rule FR1 (confirmatory, test only): aq4_fairness_confirmatory.csv; reasons per name: aq4_reasons.csv.")
    (out / "aq4_summary.md").write_text("\n".join(lines4) + "\n")
    print("\n".join(lines + [""] + lines4))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", choices=["2013", "2014", "all"], required=True)
    main(ap.parse_args().scope)
