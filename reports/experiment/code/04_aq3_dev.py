"""AQ3 development on the 9 runs of 2013 only (no 2014 outcome is read here).

1. Leave-one-run-out outer folds; rows of students who also appear in the validation run are removed from training.
2. Inside every outer fold, hyperparameters are tuned by an inner leave-one-run-out loop on pooled log loss
   (equal values go to the stronger penalty or the smaller tree model).
3. Choice rule (design, Appendix III step 4): M1 stays unless a challenger gains >= 0.03 pooled normalised recall
   at day 27, 5 per 20, and gains in >= 7 of 9 folds; several qualifiers -> largest gain, ties -> simpler.
4. Final models: every configuration tuned by leave-one-run-out on all 9 runs and refitted on all 2013 rows, at
   day 13 and day 27. Saved to models/ and skipped when they exist, so the frozen files never change.
"""

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")

import json  # noqa: E402
import pickle  # noqa: E402

import _tools  # noqa: E402,F401
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from joblib import Parallel, delayed  # noqa: E402
from sklearn.metrics import log_loss  # noqa: E402

import common as c  # noqa: E402
import models as m  # noqa: E402

SETS = c.predictor_sets()
JOBS = int(os.environ.get("JOBS", "10"))


def train_rows(f: pd.DataFrame, held: str) -> pd.DataFrame:
    """Rows of the other runs, without the students who also appear in the held-out run."""
    students = set(f.loc[f["run"] == held, "id_student"])
    return f[(f["run"] != held) & ~f["id_student"].isin(students)]


def tune(config: str, cutoff: int, f: pd.DataFrame) -> tuple[dict, list[dict]]:
    """Leave-one-run-out over the runs of f; pooled log loss per grid point; first best in grid order wins."""
    losses = []
    for params in m.grid(config):
        ys, ps = [], []
        for run in sorted(f["run"].unique()):
            tr, va = train_rows(f, run), f[f["run"] == run]
            ps.append(m.Model(config, cutoff, SETS, params).fit(tr, tr["y"].to_numpy()).predict(va))
            ys.append(va["y"].to_numpy())
        losses.append({"params": m.describe(params), "log_loss": log_loss(np.concatenate(ys), np.concatenate(ps))})
    best = min(range(len(losses)), key=lambda i: (round(losses[i]["log_loss"], 10), i))
    return m.grid(config)[best], losses


def outer_fold(config: str, f: pd.DataFrame, held: str) -> dict:
    tr, va = train_rows(f, held), f[f["run"] == held].copy()
    params, _ = tune(config, 27, tr)
    va["score"] = m.Model(config, 27, SETS, params).fit(tr, tr["y"].to_numpy()).predict(va)
    met = c.list_metrics(va, "score", 5).iloc[0].to_dict()
    return {"config": config, "fold": held, "params": m.describe(params), "n_train": len(tr), **met}


def final(config: str, cutoff: int, f: pd.DataFrame) -> dict:
    path = c.MODELS / f"{config}_d{cutoff}.pkl"
    if path.exists():                                    # frozen: never refit
        with open(path, "rb") as fh:
            return {"config": config, "cutoff": cutoff, "params": m.describe(pickle.load(fh).params), "refit": False}
    params, losses = tune(config, cutoff, f)
    model = m.Model(config, cutoff, SETS, params).fit(f, f["y"].to_numpy())
    with open(path, "wb") as fh:
        pickle.dump(model, fh)
    return {"config": config, "cutoff": cutoff, "params": m.describe(params), "refit": True, "losses": losses}


if __name__ == "__main__":
    c.MODELS.mkdir(exist_ok=True)
    f27 = c.features(27)
    f27 = f27[f27["year"] == 2013].reset_index(drop=True)
    f13 = c.features(13)
    f13 = f13[f13["year"] == 2013].reset_index(drop=True)
    runs = sorted(f27["run"].unique())
    assert len(runs) == 9

    # ---- outer folds at the main operating point (day 27, 5 per 20)
    if not (c.RESULTS / "aq3_dev_folds.csv").exists():
        folds = Parallel(n_jobs=JOBS)(delayed(outer_fold)(cfg, f27, r) for cfg in m.CONFIGS for r in runs)
        folds = pd.DataFrame(folds)
        f27["rule"] = c.rule_score(f27)
        rule = c.list_metrics(f27, "rule", 5).assign(config="RULE", fold=lambda d: d["run"], params="", n_train=0)
        folds = pd.concat([folds, rule[folds.columns]], ignore_index=True)
        c.write(folds, "aq3_dev_folds.csv")
    folds = pd.read_csv(c.RESULTS / "aq3_dev_folds.csv")

    summary = []
    m1 = folds[folds["config"] == "M1"].set_index("fold")["norm_recall"]
    for cfg, g in folds.groupby("config"):
        p = c.pooled(g)
        wins = int((g.set_index("fold")["norm_recall"] > m1).sum())
        summary.append({"config": cfg, **p, "gain_over_M1": p["norm_recall"] - c.pooled(folds[folds["config"] == "M1"])["norm_recall"],
                        "folds_better_than_M1": wins})
    summary = pd.DataFrame(summary)
    qual = summary[summary["config"].isin(["M2", "M3", "M4"]) & (summary["gain_over_M1"] >= 0.03)
                   & (summary["folds_better_than_M1"] >= 7)]
    chosen = "M1" if qual.empty else qual.sort_values(["gain_over_M1", "config"], ascending=[False, True]).iloc[0]["config"]
    summary["chosen"] = summary["config"] == chosen
    c.write(summary, "aq3_dev_summary.csv")
    print(summary[["config", "norm_recall", "gain_over_M1", "folds_better_than_M1", "chosen"]].round(4).to_string(index=False))

    # ---- final models on all 2013 rows, both cut-offs, every configuration
    jobs = [(cfg, 27, f27) for cfg in m.CONFIGS] + [(cfg, 13, f13) for cfg in m.CONFIGS]
    finals = Parallel(n_jobs=JOBS)(delayed(final)(cfg, cut, f) for cfg, cut, f in jobs)
    tuning = [{"config": r["config"], "cutoff": r["cutoff"], **loss} for r in finals if r.get("losses") for loss in r["losses"]]
    if tuning:
        c.write(pd.DataFrame(tuning), "aq3_final_tuning.csv")

    choices = {
        "chosen_configuration": chosen,
        "final_hyperparameters": {f"{r['config']}_d{r['cutoff']}": json.loads(r["params"]) for r in finals},
        "operating_point": {"cutoff_day": 27, "contacts_per_20": 5},
        "sensitivity": {"cutoff_day": 13, "contacts_per_20": 3},
        "gate_S1": "pooled normalised recall of chosen model > rule-ranked list; paired two-level bootstrap 95% interval "
                   "of the difference > 0 (2,000 replicates, seed 20261112); exact one-sided sign-flip p < 0.05 on the 13 "
                   "per-run differences",
        "condition_S3": "calibration-in-the-large in [-0.2, 0.2] and slope in [0.8, 1.2], pooled, no recalibration",
        "fairness_FR1": "groups disability=Y, imd 0-10%, imd Missing; flag if recall gap < -10 points and Holm-adjusted "
                        "one-sided bootstrap p < 0.05 (5,000 replicates)",
        "tie_breaker": "uniform draw per enrolment, seed 20261112, key order",
        "seed": c.SEED,
    }
    (c.RESULTS / "aq3_choices.json").write_text(json.dumps(choices, indent=2) + "\n")
    print(json.dumps(choices["final_hyperparameters"], indent=1))
