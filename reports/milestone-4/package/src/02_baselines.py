"""Step 2 (Table 7.1): baselines B1-B3 on the 9 development folds of 2013, before any candidate.

B1 random list (mean of B1_DRAWS seeded draws per run); B2 early-sign rule (C10) ranked by number of signs, ties by
lower activity ratio (then ascending id_student); B3 background-only penalised logistic model, nested leave-one-run-out.

Run: venv/bin/python reports/milestone-4/package/src/02_baselines.py [--jobs N]
Writes results/dev_folds_baselines.csv and results/dev_tuning_baselines.csv.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

import common as C


def b1_b2_rows(cutoff: int, m3: Path) -> list[dict]:
    df = C.load_view(cutoff, m3)
    C.assert_2013(df)
    rows = []
    for ri, (run, _, valid) in enumerate(C.loro_folds(df)):   # B1, B2 fit nothing; the validation run only
        y = valid["y"].to_numpy()
        n = len(valid)
        # B1: seeded random lists; one seed stream per (cutoff, run)
        rng = np.random.default_rng([C.SEED, cutoff, ri])
        draws = [rng.permutation(n) for _ in range(C.B1_DRAWS)]
        aucs = []
        for d in draws:
            score = np.empty(n)
            score[d] = np.arange(n, 0, -1)          # first in the permutation = highest score
            aucs.append(C.within_run_auc(y, score))
        for per20 in C.PER20:
            k = C.list_length(n, per20)
            listed_mean = np.mean([C.on_list(d, k) for d in draws], axis=0)
            rows.append({"config": "B1", "cutoff": cutoff, "k": per20, "validation_run": run,
                         **C.run_metrics(y, listed_mean, k, float(np.mean(aucs)))})
        # B2: early-sign rule ranking
        order = C.b2_order(valid)
        auc = C.within_run_auc(y, C.rule_score(valid))
        for per20 in C.PER20:
            k = C.list_length(n, per20)
            rows.append({"config": "B2", "cutoff": cutoff, "k": per20, "validation_run": run,
                         **C.run_metrics(y, C.on_list(order, k), k, auc)})
        flagged = int(valid["early_sign_rule"].sum())
        assert flagged == int((C.rule_signs(valid) > 0).sum()), "rule signs disagree with early_sign_rule"
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m3", type=Path, default=C.M3_DEFAULT)
    ap.add_argument("--jobs", type=int, default=-1)
    a = ap.parse_args()
    C.RESULTS.mkdir(parents=True, exist_ok=True)

    rows = [r for c in C.CUTOFFS for r in b1_b2_rows(c, a.m3)]
    b3, tuning = C.run_folds(["B3"], a.jobs, a.m3)
    dev = pd.concat([pd.DataFrame(rows), b3], ignore_index=True)
    C.write_dev(dev, C.RESULTS / "dev_folds_baselines.csv")
    tuning.sort_values(["config", "cutoff", "validation_run", "grid_index"]) \
        .to_csv(C.RESULTS / "dev_tuning_baselines.csv", index=False, float_format="%.6f")

    for (cfg, cutoff, k), g in dev.groupby(["config", "cutoff", "k"]):
        print(f"{cfg} day {cutoff} k={k}/20: pooled normalised recall "
              f"{C.pooled_normalised_recall(g['noncompleters_on_list'], g['max_attainable']):.4f}")


if __name__ == "__main__":
    main()
