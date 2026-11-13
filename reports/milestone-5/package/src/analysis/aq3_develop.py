"""AQ3 development on the 9 runs of 2013 only, then the freeze (Milestone 4 report, Appendix III steps 2-5).

1. Leave-one-run-out outer folds; rows of students who also appear in the validation run leave the training rows.
2. Inside every outer fold the penalty (logistic) or depth, trees and learning rate (boosted trees) are tuned by an
   inner leave-one-run-out loop on pooled log loss; equal values go to the stronger penalty or smaller model (C18).
3. Choice rule: M1 stays unless a challenger gains >= 0.03 pooled normalised recall at day 27, 5 per 20, and gains
   in >= 7 of 9 folds; several qualifiers -> largest gain, ties -> the simpler configuration.
4. Final models: every configuration tuned on all 9 runs and refitted on all 2013 rows, at day 13 and day 27.
5. Freeze: data/interim/aq3/freeze.json records the choices and the SHA-256 of every fitted model before any 2014
   outcome is read; aq3_test.py refuses to run without it or when a model file changed.

Only 2013 rows are read (filter pushed to the reader, then asserted in aq34_common.features).

Usage (from the package folder): python src/analysis/aq3_develop.py   (run_all.sh step 19)
Writes results/aq3/dev_folds.csv, dev_choice.csv, final_tuning.csv, choice.json; data/interim/aq3/*.pkl, freeze.json.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")

import hashlib  # noqa: E402
import json  # noqa: E402
import pickle  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from joblib import Parallel, delayed  # noqa: E402
from sklearn.metrics import log_loss  # noqa: E402

import aq34_common as c  # noqa: E402

SETS = c.predictor_sets()
JOBS = int(os.environ.get("JOBS", str(max(1, (os.cpu_count() or 2) - 1))))


def train_rows(f: pd.DataFrame, held: str) -> pd.DataFrame:
    """Rows of the other runs, without the students who also appear in the held-out run."""
    students = set(f.loc[f["run"] == held, "id_student"])
    return f[(f["run"] != held) & ~f["id_student"].isin(students)]


def tune(config: str, cutoff: int, f: pd.DataFrame) -> tuple[dict, list[dict]]:
    losses = []
    for params in c.grid(config):
        ys, ps = [], []
        for run in sorted(f["run"].unique()):
            tr, va = train_rows(f, run), f[f["run"] == run]
            ps.append(c.Model(config, cutoff, SETS, params).fit(tr, tr["y"].to_numpy()).predict(va))
            ys.append(va["y"].to_numpy())
        losses.append({"params": json.dumps(params, sort_keys=True),
                       "log_loss": log_loss(np.concatenate(ys), np.concatenate(ps))})
    best = min(range(len(losses)), key=lambda i: (round(losses[i]["log_loss"], 10), i))
    return c.grid(config)[best], losses


def outer_fold(config: str, f: pd.DataFrame, held: str) -> dict:
    tr, va = train_rows(f, held), f[f["run"] == held].copy()
    params, _ = tune(config, 27, tr)
    va["score"] = c.Model(config, 27, SETS, params).fit(tr, tr["y"].to_numpy()).predict(va)
    met = c.list_metrics(va, "score", 5).iloc[0].to_dict()
    return {"config": config, "fold": held, "params": json.dumps(params, sort_keys=True), "n_train": len(tr), **met}


def final(config: str, cutoff: int, f: pd.DataFrame) -> dict:
    params, losses = tune(config, cutoff, f)
    model = c.Model(config, cutoff, SETS, params).fit(f, f["y"].to_numpy())
    with open(c.WORK / f"{config}_d{cutoff}.pkl", "wb") as fh:
        pickle.dump(model, fh)
    return {"config": config, "cutoff": cutoff, "params": params, "losses": losses}


if __name__ == "__main__":
    c.WORK.mkdir(parents=True, exist_ok=True)
    (c.WORK / "freeze.json").unlink(missing_ok=True)          # a new development run needs a new freeze
    f27, f13 = c.features(27, year=2013), c.features(13, year=2013)
    runs = sorted(f27["run"].unique())
    assert len(runs) == 9 and len(f27) == 11811 and len(f13) == 12080, "2013 training populations differ from the plan"

    folds = pd.DataFrame(Parallel(n_jobs=JOBS)(delayed(outer_fold)(cfg, f27, r) for cfg in c.CONFIGS for r in runs))
    f27["rule"] = c.rule_score(f27)
    rule = c.list_metrics(f27, "rule", 5).assign(config="RULE", fold=lambda d: d["run"], params="", n_train=0)
    folds = pd.concat([folds, rule[folds.columns]], ignore_index=True)
    c.write(folds, c.RES3, "dev_folds.csv")

    m1 = folds[folds["config"] == "M1"].set_index("fold")["norm_recall"]
    m1_pooled = c.pooled(folds[folds["config"] == "M1"])["norm_recall"]
    choice = []
    for cfg, g in folds.groupby("config"):
        p = c.pooled(g)
        choice.append({"config": cfg, **p, "gain_over_M1": p["norm_recall"] - m1_pooled,
                       "folds_better_than_M1": int((g.set_index("fold")["norm_recall"] > m1).sum())})
    choice = pd.DataFrame(choice)
    qual = choice[choice["config"].isin(["M2", "M3", "M4"]) & (choice["gain_over_M1"] >= 0.03)
                  & (choice["folds_better_than_M1"] >= 7)]
    chosen = "M1" if qual.empty else qual.sort_values(["gain_over_M1", "config"], ascending=[False, True]).iloc[0]["config"]
    choice["chosen"] = choice["config"] == chosen
    c.write(choice, c.RES3, "dev_choice.csv")
    print(choice[["config", "norm_recall", "gain_over_M1", "folds_better_than_M1", "chosen"]].round(4).to_string(index=False))

    jobs = [(cfg, 27, f27) for cfg in c.CONFIGS] + [(cfg, 13, f13) for cfg in c.CONFIGS]
    finals = Parallel(n_jobs=JOBS)(delayed(final)(cfg, cut, f) for cfg, cut, f in jobs)
    c.write(pd.DataFrame([{"config": r["config"], "cutoff": r["cutoff"], **loss} for r in finals for loss in r["losses"]]),
            c.RES3, "final_tuning.csv")

    choices = {"chosen_configuration": chosen,
               "final_hyperparameters": {f"{r['config']}_d{r['cutoff']}": r["params"] for r in finals},
               "tuning_criterion": "pooled log loss of an inner leave-one-run-out loop (Change Log C18)",
               "operating_point": {"cutoff_day": 27, "contacts_per_20": 5}, "seed": c.SEED}
    (c.RES3 / "choice.json").write_text(json.dumps(choices, indent=2, sort_keys=True) + "\n")
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(c.WORK.glob("*.pkl"))}
    freeze = {"frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "choices": choices,
              "models": hashes}
    (c.WORK / "freeze.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(f"frozen {len(hashes)} models at {freeze['frozen_utc']}; chosen configuration {chosen}")
