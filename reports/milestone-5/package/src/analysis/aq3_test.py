"""AQ3 single test on the 13 runs of 2014 with the frozen models (Milestone 4 report, Appendix III steps 6-7).

Refuses to run unless data/interim/aq3/freeze.json exists and every model file still has its frozen SHA-256, so no
2014 outcome can be read before the freeze. Scores each 2014 enrolment once (data/interim/aq3/scores_d13.csv,
scores_d27.csv; not shipped) and computes from those scores, without refitting or recalibrating, the parts that
exist only for the test:

- gate S1 (Table 4.5): pooled normalised recall of the chosen model against the rule-ranked list, day 27, 5 per 20,
  paired two-level bootstrap (2,000 replicates) and exact one-sided sign-flip test on the 13 run differences; the
  background-only model and the challengers as context;
- sensitivity views that cannot change the verdict (day 13, 3 per 20, paired and unpaired runs, CCC, repeat
  students, Withdrawn without a day);
- calibration by bins of predicted risk, and when listed non-completers leave.

The views shared with the other scopes (lists by run and pooled, discrimination and calibration, capacity curve,
model against rule, recall by slice, AQ4 yield and fairness rates) are written by aq34_scopes.py --scope 2014.

Usage (from the package folder): python src/analysis/aq3_test.py   (run_all.sh step 20)
Writes results/2014/aq3_s1_gate.csv, aq3_sensitivity.csv, aq3_calibration_bins.csv, aq3_lead_time.csv.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import pickle
import sys

import numpy as np
import pandas as pd

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
    cols = ["paired_run", "student_in_training_runs", "eval_withdrawal_day_unknown", "final_result"]
    frame = out.merge(test[c.KEY + cols], on=c.KEY, validate="1:1").merge(enrol, on=c.KEY, how="left", validate="1:1")
    frame["RULE"] = frame["rule"]
    return frame.reset_index(drop=True)


d27, d13 = score(27), score(13)
print(f"scored {len(d27)} enrolments at day 27 and {len(d13)} at day 13 in 13 runs of 2014")


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


# ---------------------------------------------------------------- gate S1 and context
gate = s1(d27, CHOSEN, "RULE")
gate["met"] = bool(gate["difference"] > 0 and gate["low"] > 0 and gate["signflip_p"] < 0.05)
others = [s1(d27, CHOSEN, "B3", boot=500)] + [s1(d27, cfg, CHOSEN, boot=500) for cfg in ["M2", "M3", "M4"] if cfg != CHOSEN]
c.write(pd.DataFrame([gate] + others), c.R2014, "aq3_s1_gate.csv")

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
c.write(pd.DataFrame(sens), c.R2014, "aq3_sensitivity.csv")

# ---------------------------------------------------------------- calibration bins and timing of listed non-completers
bins = []
for b, g in d27.groupby(pd.cut(d27[CHOSEN], bins=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0], include_lowest=True),
                        observed=True):
    bins.append({"bin": str(b), "n": len(g), "mean_predicted": g[CHOSEN].mean(), "observed": g["y"].mean()})
c.write(pd.DataFrame(bins), c.R2014, "aq3_calibration_bins.csv")

d27["k"] = d27.groupby("run")["run"].transform(lambda s: c.list_size(len(s), 5))
listed = d27[(c.rank_in_run(d27, CHOSEN) <= d27["k"]) & (d27["y"] == 1)]
w, u = listed["final_result"].eq("Withdrawn"), listed["date_unregistration"]
lt = [{"band": b, "listed_non_completers": int(m.sum()), "share": m.mean()} for b, m in
      [("withdrew days 28–34 (before the list can act)", w & u.between(28, 34)), ("withdrew days 35–90", w & u.between(35, 90)),
       ("withdrew after day 90", w & (u > 90)), ("withdrawn, day unknown", w & u.isna()),
       ("failed at the end", listed["final_result"].eq("Fail"))]]
c.write(pd.DataFrame(lt), c.R2014, "aq3_lead_time.csv")
print(f"gate S1: {gate['norm_recall_a']:.3f} against {gate['norm_recall_b']:.3f}, difference {gate['difference']:+.3f} "
      f"({gate['low']:+.3f} to {gate['high']:+.3f}), sign-flip p = {gate['signflip_p']:.4f}: {'met' if gate['met'] else 'not met'}")
