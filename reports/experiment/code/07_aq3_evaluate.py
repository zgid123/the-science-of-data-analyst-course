"""AQ3 evaluation on the saved 2014 scores (no refit): gate S1, report S2, condition S3 and the deeper views.

Reads scores/test_scores_d{13,27}.csv written once by 06_aq3_score.py.
"""

import itertools
import json
import math

import _tools  # noqa: F401
import numpy as np
import pandas as pd
from holdout_guard import open_holdout
from sklearn.metrics import average_precision_score, roc_auc_score

import common as c

open_holdout(c.FREEZE, c.ACCESS, who="07_aq3_evaluate.py", why="AQ3 metrics from the saved 2014 scores")
CHOSEN = json.loads((c.RESULTS / "aq3_choices.json").read_text())["chosen_configuration"]
METHODS = ["RULE", "B3", "M1", "M2", "M3", "M4"]
NAMES = {"RULE": "Early-sign rule (ranked)", "B3": "Background-only model", "M1": "Logistic, primary predictors",
         "M2": "Logistic, extended predictors", "M3": "Boosted trees, primary", "M4": "Boosted trees, extended",
         "RANDOM": "Random list (expected)"}
B = 2000
rng = np.random.default_rng(c.SEED)


def load(cut: int) -> pd.DataFrame:
    s = pd.read_csv(c.SCORES / f"test_scores_d{cut}.csv")
    f = c.features(cut)
    f = f[f["year"] == 2014][c.KEY + ["paired_run", "student_in_training_runs", "eval_withdrawal_day_unknown",
                                      "final_result", "clicks_0c", "activity_ratio_run", "num_of_prev_attempts",
                                      "registration_lead", "rule_missed", "rule_tma_late", "inactive_last7",
                                      "early_sign_rule", "tasks_due_c"]]
    e = c.enrolment()[c.KEY + ["date_unregistration"]]
    out = s.merge(f, on=c.KEY, how="left", validate="1:1").merge(e, on=c.KEY, how="left", validate="1:1")
    out["RULE"] = out["rule"]
    assert len(out) == len(s)
    return out.reset_index(drop=True)


def metrics(frame: pd.DataFrame, per20: int) -> pd.DataFrame:
    rows = []
    for meth in METHODS:
        m = c.list_metrics(frame, meth, per20).assign(method=meth)
        rows.append(m)
    r = c.list_metrics(frame, "RULE", per20)               # same n, k, positives; expected tp of a random list
    r["tp"] = r["k"] * r["positives"] / r["n"]
    r["recall"], r["precision"] = r["tp"] / r["positives"], r["tp"] / r["k"]
    r["lift"], r["norm_recall"] = 1.0, r["tp"] / r["attainable"]
    rows.append(r.assign(method="RANDOM"))
    return pd.concat(rows, ignore_index=True)


def pooled_table(frame: pd.DataFrame, per20: int, label: dict) -> list[dict]:
    m = metrics(frame, per20)
    out = []
    for meth, g in m.groupby("method", sort=False):
        out.append({**label, "method": meth, "name": NAMES[meth], **c.pooled(g)})
    return out


# ------------------------------------------------------------------ S1 machinery
def arrays(frame: pd.DataFrame, a: str, b: str):
    return [(g["y"].to_numpy(), g[a].to_numpy(), g[b].to_numpy(), g["tiebreak_u"].to_numpy())
            for _, g in frame.groupby("run", sort=True)]


def tp_at(y, s, u, k):
    order = np.lexsort((u, -s))
    return y[order[:k]].sum()


def run_diff(y, sa, sb, u, per20):
    n, pos = len(y), int(y.sum())
    k = c.list_size(n, per20)
    return tp_at(y, sa, u, k), tp_at(y, sb, u, k), min(k, pos)


def s1(frame: pd.DataFrame, a: str, b: str, per20: int = 5, boot: int = B) -> dict:
    runs = arrays(frame, a, b)
    per = np.array([run_diff(*r, per20) for r in runs], dtype=float)
    ta, tb, best = per[:, 0], per[:, 1], per[:, 2]
    diff = ta.sum() / best.sum() - tb.sum() / best.sum()
    d_run = ta / best - tb / best
    reps = np.empty(boot)
    for i in range(boot):
        tot = np.zeros(3)
        for j in rng.integers(0, len(runs), len(runs)):
            y, sa, sb, u = runs[j]
            idx = rng.integers(0, len(y), len(y))
            tot += run_diff(y[idx], sa[idx], sb[idx], u[idx], per20)
        reps[i] = (tot[0] - tot[1]) / tot[2]
    signs = np.array(list(itertools.product([1, -1], repeat=len(d_run))))
    flips = (signs * d_run).mean(axis=1)
    return {"a": a, "b": b, "per20": per20, "runs": len(runs), "norm_recall_a": ta.sum() / best.sum(),
            "norm_recall_b": tb.sum() / best.sum(), "difference": diff, "low": np.quantile(reps, 0.025),
            "high": np.quantile(reps, 0.975), "extra_listed_noncompleters": int(ta.sum() - tb.sum()),
            "list_places": int(sum(c.list_size(len(r[0]), per20) for r in runs)),
            "mean_run_difference": d_run.mean(), "signflip_p": float((flips >= d_run.mean() - 1e-12).mean()),
            "wins": int((d_run > 0).sum()), "ties": int((d_run == 0).sum()), "losses": int((d_run < 0).sum())}


# ------------------------------------------------------------------ main operating point
d27, d13 = load(27), load(13)
by_run = metrics(d27, 5)
c.write(by_run, "aq3_test_by_run.csv")

pooled = []
for cut, frame in [(27, d27), (13, d13)]:
    for per20 in (5, 3):
        pooled += pooled_table(frame, per20, {"cutoff": cut, "per20": per20})
pooled = pd.DataFrame(pooled)
c.write(pooled, "aq3_test_pooled.csv")

gate = s1(d27, CHOSEN, "RULE")
gate["met"] = bool(gate["difference"] > 0 and gate["low"] > 0 and gate["signflip_p"] < 0.05)
others = [s1(d27, CHOSEN, "B3", boot=500), *[s1(d27, cfg, CHOSEN, boot=500) for cfg in ["M2", "M3", "M4"] if cfg != CHOSEN]]
c.write(pd.DataFrame([gate] + others), "aq3_s1.csv")
print("S1:", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in gate.items()})

# ------------------------------------------------------------------ sensitivity views (cannot change the verdict)
sens = []
variants = [("Main: all 13 runs, day 27, 5 per 20", d27, 5),
            ("Day 13, 5 per 20", d13, 5), ("Day 27, 3 per 20", d27, 3),
            ("9 runs also run in 2013", d27[d27["paired_run"]], 5),
            ("4 runs not run in 2013", d27[~d27["paired_run"]], 5),
            ("Without module CCC", d27[d27["code_module"] != "CCC"], 5),
            ("Module CCC only", d27[d27["code_module"] == "CCC"], 5),
            ("Without students seen in 2013", d27[~d27["student_in_training_runs"]], 5),
            ("Without Withdrawn lacking a withdrawal day", d27[~d27["eval_withdrawal_day_unknown"]], 5)]
for label, frame, per20 in variants:
    r = s1(frame.reset_index(drop=True), CHOSEN, "RULE", per20, boot=500)
    sens.append({"variant": label, **{k: r[k] for k in ["runs", "norm_recall_a", "norm_recall_b", "difference", "low",
                                                        "high", "wins", "losses", "extra_listed_noncompleters"]}})
c.write(pd.DataFrame(sens), "aq3_sensitivity.csv")

# ------------------------------------------------------------------ discrimination and calibration
disc = []
for cut, frame in [(27, d27), (13, d13)]:
    for meth in METHODS:
        aucs = [roc_auc_score(g["y"], g[meth]) for _, g in frame.groupby("run")]
        aps = [average_precision_score(g["y"], g[meth]) for _, g in frame.groupby("run")]
        row = {"cutoff": cut, "method": meth, "name": NAMES[meth], "roc_auc_within_run": np.mean(aucs),
               "pr_auc_within_run": np.mean(aps), "base_rate_mean": frame.groupby("run")["y"].mean().mean()}
        if meth != "RULE":
            row.update(c.calibration(frame["y"].to_numpy(), frame[meth].to_numpy()))
            runs_ok = 0
            for _, g in frame.groupby("run"):
                cal = c.calibration(g["y"].to_numpy(), g[meth].to_numpy())
                runs_ok += int(-0.2 <= cal["citl"] <= 0.2 and 0.8 <= cal["slope"] <= 1.2)
            row["runs_within_s3_bounds"] = runs_ok
            row["s3_met_pooled"] = bool(-0.2 <= row["citl"] <= 0.2 and 0.8 <= row["slope"] <= 1.2)
        disc.append(row)
c.write(pd.DataFrame(disc), "aq3_discrimination_calibration.csv")

from stats_helpers import calibration_table  # noqa: E402
cal = calibration_table(d27["y"], d27[CHOSEN], bins=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
c.write(cal, "aq3_calibration_bins.csv")

# ------------------------------------------------------------------ capacity curve: contacts per 20 from 1 to 10
curve = []
for per20 in range(1, 11):
    for meth, g in metrics(d27, per20).groupby("method", sort=False):
        if meth in (CHOSEN, "RULE", "B3", "RANDOM"):
            curve.append({"per20": per20, "method": meth, "name": NAMES[meth], **c.pooled(g)})
c.write(pd.DataFrame(curve), "aq3_capacity_curve.csv")

# ------------------------------------------------------------------ who is listed: model against rule
d27["rank_model"] = c.rank_in_run(d27, CHOSEN)
d27["rank_rule"] = c.rank_in_run(d27, "RULE")
d27["k"] = d27.groupby("run")["run"].transform(lambda s: c.list_size(len(s), 5))
d27["on_model"], d27["on_rule"] = d27["rank_model"] <= d27["k"], d27["rank_rule"] <= d27["k"]
d27["n_rule_signs"] = d27[["rule_missed", "rule_tma_late", "inactive_last7"]].astype(int).sum(axis=1)
d27["withdrew_after"] = d27["final_result"].eq("Withdrawn") & d27["date_unregistration"].gt(27)
d27["withdrew_7d"] = d27["final_result"].eq("Withdrawn") & d27["date_unregistration"].between(28, 34)
groups = {"On both lists": d27["on_model"] & d27["on_rule"], "Model list only": d27["on_model"] & ~d27["on_rule"],
          "Rule list only": ~d27["on_model"] & d27["on_rule"], "On neither list": ~d27["on_model"] & ~d27["on_rule"]}
who = []
for label, mask in groups.items():
    g = d27[mask]
    who.append({"group": label, "enrolments": len(g), "non_completers": int(g["y"].sum()), "rate": g["y"].mean(),
                "fail": int((g["final_result"] == "Fail").sum()), "withdrawn": int((g["final_result"] == "Withdrawn").sum()),
                "share_with_rule_sign": (g["n_rule_signs"] > 0).mean(), "share_no_click": (g["clicks_0c"] == 0).mean(),
                "median_activity_ratio": g["activity_ratio_run"].median(),
                "share_previous_attempt": (g["num_of_prev_attempts"] > 0).mean()})
c.write(pd.DataFrame(who), "aq3_model_vs_rule.csv")

# ------------------------------------------------------------------ errors by slice (model and rule, day 27, 5 per 20)
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
c.write(pd.DataFrame(err), "aq3_errors_by_slice.csv")

# ------------------------------------------------------------------ timing: when listed non-completers leave
lt = []
listed = d27[d27["on_model"] & (d27["y"] == 1)]
bands = [("withdrew days 28–34 (before the list can act)", listed["withdrew_7d"]),
         ("withdrew days 35–90", listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].between(35, 90)),
         ("withdrew after day 90", listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].gt(90)),
         ("withdrawn, day unknown", listed["final_result"].eq("Withdrawn") & listed["date_unregistration"].isna()),
         ("failed at the end", listed["final_result"].eq("Fail"))]
for label, mask in bands:
    lt.append({"band": label, "listed_non_completers": int(mask.sum()), "share": mask.mean()})
c.write(pd.DataFrame(lt), "aq3_lead_time.csv")
print(pd.DataFrame(lt).to_string(index=False))
