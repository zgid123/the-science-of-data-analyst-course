"""Steps 3-4 (Table 7.1), Appendix III steps 2-3: candidates M1-M4 on the 9 leave-one-run-out folds of 2013, with
nested leave-one-run-out tuning inside each training set, at day 13 and day 27 and k = 3 and 5 per 20.

Run: venv/bin/python reports/milestone-4/package/src/03_dev_folds.py [--jobs N]
Reads results/dev_folds_baselines.csv (step 02); writes results/dev_folds.csv (B1-B3 and M1-M4) and
results/dev_tuning.csv (every inner-loop grid result and the chosen setting per outer fold).
"""
import argparse
from pathlib import Path

import pandas as pd

import common as C


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m3", type=Path, default=C.M3_DEFAULT)
    ap.add_argument("--jobs", type=int, default=-1)
    a = ap.parse_args()

    models, tuning = C.run_folds(["M1", "M2", "M3", "M4"], a.jobs, a.m3)
    base = pd.read_csv(C.RESULTS / "dev_folds_baselines.csv")
    dev = pd.concat([base, models], ignore_index=True)
    assert len(dev) == 7 * 2 * 2 * 9, len(dev)
    C.write_dev(dev, C.RESULTS / "dev_folds.csv")
    tb = pd.read_csv(C.RESULTS / "dev_tuning_baselines.csv")
    pd.concat([tb, tuning.sort_values(["config", "cutoff", "validation_run", "grid_index"])], ignore_index=True) \
        .to_csv(C.RESULTS / "dev_tuning.csv", index=False, float_format="%.6f")

    dev = pd.read_csv(C.RESULTS / "dev_folds.csv")
    for (cfg, cutoff, k), g in dev.groupby(["config", "cutoff", "k"]):
        print(f"{cfg} day {cutoff} k={k}/20: pooled normalised recall "
              f"{C.pooled_normalised_recall(g['noncompleters_on_list'], g['max_attainable']):.4f}")


if __name__ == "__main__":
    main()
