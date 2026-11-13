"""AQ3 single test on the 13 runs of 2014 with the frozen models (Milestone 4 report, Appendix III steps 6-7).

Refuses to run unless data/interim/aq3/freeze.json exists and every model file still has its frozen SHA-256, so no
2014 outcome can be read before the freeze. Scores each 2014 enrolment once (data/interim/aq3/scores_d13.csv,
scores_d27.csv; not shipped) and computes from those scores, without refitting or recalibrating:

- gate S1 (Table 4.5): pooled normalised recall of the chosen model against the rule-ranked list, day 27, 5 per 20,
  paired two-level bootstrap (2,000 replicates) and exact one-sided sign-flip test on the 13 run differences;
- S2 precision, the other configurations and the background-only baseline as context;
- sensitivity views that cannot change the verdict (day 13, 3 per 20, paired and unpaired runs, CCC, repeat
  students, Withdrawn without a day);
- discrimination within run and calibration S3, pooled and per run;
- capacity curve, the students on the model list only or the rule list only, recall by slice, and when listed
  non-completers leave.

Usage (from the package folder): python src/analysis/aq3_test.py   (run_all.sh step 20)
Writes results/aq3/test_*.csv, s1_gate.csv, sensitivity.csv, discrimination_calibration.csv, calibration_bins.csv,
capacity_curve.csv, model_vs_rule.csv, errors_by_slice.csv, lead_time.csv, aq3_summary.md.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import pickle
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

import aq34_common as c

# ---------------------------------------------------------------- freeze guard and single scoring
freeze_path = c.WORK / "freeze.json"
if not freeze_path.exists():
    sys.exit("no freeze record: run src/analysis/aq3_develop.py first")
freeze = json.loads(freeze_path.read_text())
for name, digest in freeze["models"].items():
    assert hashlib.sha256((c.WORK / name).read_bytes()).hexdigest() == digest, f"{name} changed after the freeze"
CHOSEN = freeze["choices"]["chosen_configuration"]
print(f"freeze of {freeze['frozen_utc']} verified ({len(freeze['models'])} models); chosen {CHOSEN}")

METHODS = ["RULE", "B3", "M1", "M2", "M3", "M4"]
NAMES = {"RULE": "Early-sign rule (ranked)", "B3": "Background-only model", "M1": "Logistic, primary predictors",
         "M2": "Logistic, extended predictors", "M3": "Boosted trees, primary", "M4": "Boosted trees, extended",
         "RANDOM": "Random list (expected)"}
rng = np.random.default_rng(c.SEED)
enrol = c.enrolment()[c.KEY + ["date_unregistration"]]


def score(cut: int) -> pd.DataFrame:
    test = c.features(cut, year=2014)
    assert test["run"].nunique() == 13, "the test must hold the 13 runs of 2014"
    out = test[c.KEY + ["run", "y", "tiebreak_u"]].copy()
    out["rule"] = c.rule_score(test)
    for cfg in c.CONFIGS:
        with open(c.WORK / f"{cfg}_d{cut}.pkl", "rb") as fh:
            out[cfg] = pickle.load(fh).predict(test)
    out.to_csv(c.WORK / f"scores_d{cut}.csv", index=False)
    cols = ["paired_run", "student_in_training_runs", "eval_withdrawal_day_unknown", "final_result", "clicks_0c",
            "activity_ratio_run", "num_of_prev_attempts", "registration_lead", "rule_missed", "rule_tma_late",
            "inactive_last7"]
    frame = out.merge(test[c.KEY + cols], on=c.KEY, validate="1:1").merge(enrol, on=c.KEY, how="left", validate="1:1")
    frame["RULE"] = frame["rule"]
    return frame.reset_index(drop=True)


d27, d13 = score(27), score(13)
print(f"scored {len(d27)} enrolments at day 27 and {len(d13)} at day 13 in 13 runs of 2014")


def metrics(frame: pd.DataFrame, per20: int) -> pd.DataFrame:
    rows = [c.list_metrics(frame, m, per20).assign(method=m) for m in METHODS]
    r = c.list_metrics(frame, "RULE", per20)                  # expected values of a random list of the same length
    r["tp"] = r["k"] * r["positives"] / r["n"]
    r["recall"], r["precision"] = r["tp"] / r["positives"], r["tp"] / r["k"]
    r["lift"], r["norm_recall"] = 1.0, r["tp"] / r["attainable"]
    rows.append(r.assign(method="RANDOM"))
    return pd.concat(rows, ignore_index=True)


def tp_at(y, s, u, k):
    return y[np.lexsort((u, -s))[:k]].sum()


def run_diff(y, sa, sb, u, per20):
    k = c.list_size(len(y), per20)
    return tp_at(y, sa, u, k), tp_at(y, sb, u, k), min(k, int(y.sum()))


def s1(frame: pd.DataFrame, a: str, b: str, per20: int = 5, boot: int = 2000) -> dict:
    runs = [(g["y"].to_numpy(), g[a].to_numpy(), g[b].to_numpy(), g["tiebreak_u"].to_numpy())
            for _, g in frame.groupby("run", sort=True)]
    per = np.array([run_diff(*r, per20) for r in runs], dtype=float)
    ta, tb, best = per[:, 0], per[:, 1], per[:, 2]
    d_run = ta / best - tb / best
    reps = np.empty(boot)
    for i in range(boot):
        tot = np.zeros(3)
        for j in rng.integers(0, len(runs), len(runs)):
            y, sa, sb, u = runs[j]
            idx = rng.integers(0, len(y), len(y))
            tot += run_diff(y[idx], sa[idx], sb[idx], u[idx], per20)
        reps[i] = (tot[0] - tot[1]) / tot[2]
    flips = (np.array(list(itertools.product([1, -1], repeat=len(d_run)))) * d_run).mean(axis=1)
    return {"a": a, "b": b, "per20": per20, "runs": len(runs), "norm_recall_a": ta.sum() / best.sum(),
            "norm_recall_b": tb.sum() / best.sum(), "difference": (ta.sum() - tb.sum()) / best.sum(),
            "low": np.quantile(reps, 0.025), "high": np.quantile(reps, 0.975),
            "extra_listed_noncompleters": int(ta.sum() - tb.sum()),
            "list_places": int(sum(c.list_size(len(r[0]), per20) for r in runs)),
            "mean_run_difference": d_run.mean(), "signflip_p": float((flips >= d_run.mean() - 1e-12).mean()),
            "wins": int((d_run > 0).sum()), "ties": int((d_run == 0).sum()), "losses": int((d_run < 0).sum())}


# ---------------------------------------------------------------- list quality, gate S1 and context
c.write(metrics(d27, 5), c.RES3, "test_by_run.csv")
pooled = []
for cut, frame in [(27, d27), (13, d13)]:
    for per20 in (5, 3):
        for meth, g in metrics(frame, per20).groupby("method", sort=False):
            pooled.append({"cutoff": cut, "per20": per20, "method": meth, "name": NAMES[meth], **c.pooled(g)})
c.write(pd.DataFrame(pooled), c.RES3, "test_pooled.csv")

gate = s1(d27, CHOSEN, "RULE")
gate["met"] = bool(gate["difference"] > 0 and gate["low"] > 0 and gate["signflip_p"] < 0.05)
others = [s1(d27, CHOSEN, "B3", boot=500)] + [s1(d27, cfg, CHOSEN, boot=500) for cfg in ["M2", "M3", "M4"] if cfg != CHOSEN]
c.write(pd.DataFrame([gate] + others), c.RES3, "s1_gate.csv")

sens = []
for label, frame, per20 in [("Main: all 13 runs, day 27, 5 per 20", d27, 5), ("Day 13, 5 per 20", d13, 5),
                            ("Day 27, 3 per 20", d27, 3), ("9 runs also run in 2013", d27[d27["paired_run"]], 5),
                            ("4 runs not run in 2013", d27[~d27["paired_run"]], 5),
                            ("Without module CCC", d27[d27["code_module"] != "CCC"], 5),
                            ("Module CCC only", d27[d27["code_module"] == "CCC"], 5),
                            ("Without students seen in 2013", d27[~d27["student_in_training_runs"]], 5),
                            ("Without Withdrawn lacking a withdrawal day", d27[~d27["eval_withdrawal_day_unknown"]], 5)]:
    r = s1(frame.reset_index(drop=True), CHOSEN, "RULE", per20, boot=500)
    sens.append({"variant": label, **{k: r[k] for k in ["runs", "norm_recall_a", "norm_recall_b", "difference", "low",
                                                        "high", "wins", "losses", "extra_listed_noncompleters"]}})
c.write(pd.DataFrame(sens), c.RES3, "sensitivity.csv")

# ---------------------------------------------------------------- discrimination and calibration (S3)
disc = []
for cut, frame in [(27, d27), (13, d13)]:
    for meth in METHODS:
        row = {"cutoff": cut, "method": meth, "name": NAMES[meth],
               "roc_auc_within_run": np.mean([roc_auc_score(g["y"], g[meth]) for _, g in frame.groupby("run")]),
               "pr_auc_within_run": np.mean([average_precision_score(g["y"], g[meth]) for _, g in frame.groupby("run")]),
               "base_rate_mean": frame.groupby("run")["y"].mean().mean()}
        if meth != "RULE":
            row.update(c.calibration(frame["y"].to_numpy(), frame[meth].to_numpy()))
            ok = 0
            for _, g in frame.groupby("run"):
                cal = c.calibration(g["y"].to_numpy(), g[meth].to_numpy())
                ok += int(-0.2 <= cal["citl"] <= 0.2 and 0.8 <= cal["slope"] <= 1.2)
            row["runs_within_s3_bounds"] = ok
            row["s3_met_pooled"] = bool(-0.2 <= row["citl"] <= 0.2 and 0.8 <= row["slope"] <= 1.2)
        disc.append(row)
c.write(pd.DataFrame(disc), c.RES3, "discrimination_calibration.csv")

bins = []
cut_bins = pd.cut(d27[CHOSEN], bins=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0], include_lowest=True)
for b, g in d27.groupby(cut_bins, observed=True):
    bins.append({"bin": str(b), "n": len(g), "mean_predicted": g[CHOSEN].mean(), "observed": g["y"].mean()})
c.write(pd.DataFrame(bins), c.RES3, "calibration_bins.csv")

# ---------------------------------------------------------------- capacity curve, 1 to 10 contacts per 20
curve = []
for per20 in range(1, 11):
    for meth, g in metrics(d27, per20).groupby("method", sort=False):
        if meth in (CHOSEN, "RULE", "B3", "RANDOM"):
            curve.append({"per20": per20, "method": meth, "name": NAMES[meth], **c.pooled(g)})
c.write(pd.DataFrame(curve), c.RES3, "capacity_curve.csv")

# ---------------------------------------------------------------- who is listed: model against rule; recall by slice
d27["k"] = d27.groupby("run")["run"].transform(lambda s: c.list_size(len(s), 5))
d27["on_model"] = c.rank_in_run(d27, CHOSEN) <= d27["k"]
d27["on_rule"] = c.rank_in_run(d27, "RULE") <= d27["k"]
d27["n_rule_signs"] = d27[["rule_missed", "rule_tma_late", "inactive_last7"]].astype(int).sum(axis=1)
d27["withdrew_7d"] = d27["final_result"].eq("Withdrawn") & d27["date_unregistration"].between(28, 34)
who = []
for label, mask in {"On both lists": d27["on_model"] & d27["on_rule"], "Model list only": d27["on_model"] & ~d27["on_rule"],
                    "Rule list only": ~d27["on_model"] & d27["on_rule"], "On neither list": ~d27["on_model"] & ~d27["on_rule"]}.items():
    g = d27[mask]
    who.append({"group": label, "enrolments": len(g), "non_completers": int(g["y"].sum()), "rate": g["y"].mean(),
                "fail": int((g["final_result"] == "Fail").sum()), "withdrawn": int((g["final_result"] == "Withdrawn").sum()),
                "share_with_rule_sign": (g["n_rule_signs"] > 0).mean(), "share_no_click": (g["clicks_0c"] == 0).mean(),
                "median_activity_ratio": g["activity_ratio_run"].median(),
                "share_previous_attempt": (g["num_of_prev_attempts"] > 0).mean()})
c.write(pd.DataFrame(who), c.RES3, "model_vs_rule.csv")

d27["activity"] = np.select([d27["clicks_0c"] == 0, d27["activity_ratio_run"] < 0.5], ["none", "low"], "normal")
d27["history"] = np.where(d27["num_of_prev_attempts"] > 0, "previous attempt", "first attempt")
d27["registration"] = np.where(d27["registration_lead"] < 0, "registered after the start", "registered by the start")
d27["kind"] = d27["final_result"]
d27["reach"] = np.where(d27["withdrew_7d"], "withdrew within 7 days", "still reachable")
err = []
for by in ["activity", "history", "registration", "kind", "reach"]:
    for lev, g in d27.groupby(by):
        pos = g[g["y"] == 1]
        err.append({"slice": by, "level": lev, "enrolments": len(g), "non_completers": len(pos),
                    "recall_model": pos["on_model"].mean() if len(pos) else np.nan,
                    "recall_rule": pos["on_rule"].mean() if len(pos) else np.nan,
                    "listed_model": int(g["on_model"].sum()),
                    "listed_completers_model": int((g["on_model"] & (g["y"] == 0)).sum())})
c.write(pd.DataFrame(err), c.RES3, "errors_by_slice.csv")

listed = d27[d27["on_model"] & (d27["y"] == 1)]
w = listed["final_result"].eq("Withdrawn")
u = listed["date_unregistration"]
lt = [{"band": b, "listed_non_completers": int(m.sum()), "share": m.mean()} for b, m in
      [("withdrew days 28–34 (before the list can act)", listed["withdrew_7d"]), ("withdrew days 35–90", w & u.between(35, 90)),
       ("withdrew after day 90", w & (u > 90)), ("withdrawn, day unknown", w & u.isna()),
       ("failed at the end", listed["final_result"].eq("Fail"))]]
c.write(pd.DataFrame(lt), c.RES3, "lead_time.csv")

# ---------------------------------------------------------------- summary
p = pd.DataFrame(pooled).query("cutoff == 27 and per20 == 5").set_index("method")
cal = pd.DataFrame(disc).query("cutoff == 27 and method == @CHOSEN").iloc[0]
lines = [
    "# AQ3: early-warning model, 2013 -> 2014", "",
    f"Chosen configuration: {CHOSEN} (development on the 9 runs of 2013, results/aq3/dev_choice.csv).", "",
    f"- Gate S1 (day 27, 5 per 20, 13 runs of 2014): pooled normalised recall {gate['norm_recall_a']:.3f} against "
    f"{gate['norm_recall_b']:.3f} for the rule-ranked list; difference {gate['difference']:+.3f} "
    f"(95% bootstrap interval {gate['low']:+.3f} to {gate['high']:+.3f}), sign-flip p = {gate['signflip_p']:.4f}, "
    f"{gate['wins']} of 13 runs won: {'met' if gate['met'] else 'not met'}.",
    f"- Lists of 5 per 20: {int(p.loc[CHOSEN, 'tp']):,} of {int(p.loc[CHOSEN, 'positives']):,} non-completers listed "
    f"(recall {p.loc[CHOSEN, 'recall']:.1%}, precision {p.loc[CHOSEN, 'precision']:.1%}); rule "
    f"{int(p.loc['RULE', 'tp']):,}; random list {p.loc['RANDOM', 'tp']:.1f}.",
    f"- Calibration S3 (pooled): calibration-in-the-large {cal['citl']:.3f}, slope {cal['slope']:.3f}: "
    f"{'met' if cal['s3_met_pooled'] else 'not met'} pooled; {int(cal['runs_within_s3_bounds'])} of 13 runs within the bounds.",
]
(c.RES3 / "aq3_summary.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
