"""Append one entry to logs/experiment_log.md (contract: "Experiment log").

Run (by run_dev.sh): venv/bin/python src/log_entry.py --command "<cmd>" --started <utc> --steps "01_load_check=0 ..."
"""
import argparse
import datetime as dt
import json
import platform
from importlib.metadata import version

import pandas as pd

import common as C

PACKAGES = ("numpy", "pandas", "polars", "scipy", "scikit-learn", "joblib", "threadpoolctl", "statsmodels")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--command", required=True)
    ap.add_argument("--started", required=True)
    ap.add_argument("--steps", required=True, help="space-separated step=exit_status")
    ap.add_argument("--note", default="")
    ap.add_argument("--phase", default="1", choices=["1", "2"])
    a = ap.parse_args()
    steps = dict(s.split("=") for s in a.steps.split())
    overall = 0 if all(v == "0" for v in steps.values()) else 1
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = json.loads((C.M3_DEFAULT / "data/metadata/version_manifest.json").read_text())
    used = ("features_d13.parquet", "features_d27.parquet", "capacity_by_run.parquet")
    title = ("phase 1: development on 2013 and freeze" if a.phase == "1" else
             "phase 2: single test on 2014, gates, fairness, sensitivity, AQ4 lists, AQ2 replication, report")
    lines = [f"## Run {a.started} ({title})", "",
             f"- UTC start / end: {a.started} / {now}",
             f"- Command: `{a.command}`",
             f"- Git commit: {C.git_commit()}",
             f"- Exit status: {overall} (" + ", ".join(f"{k}={v}" for k, v in steps.items()) + ")",
             f"- Python {platform.python_version()}; " + ", ".join(f"{p} {version(p)}" for p in PACKAGES),
             f"- Prepared data: {manifest['prepared_dataset_version']} (hash check in logs/01_load_check.log, "
             "results/input_hashes.csv); files read: "
             + "; ".join(f"{u} {manifest['outputs'][u]['sha256']}" for u in used),
             "- Metadata read (no manifest hash; recorded): "
             + "; ".join(f"{k} {v}" for k, v in C.metadata_hashes().items()),
             f"- Seeds: SEED={C.SEED} (B1 draws: numpy default_rng([SEED, cutoff, fold index]), {C.B1_DRAWS} draws; "
             "HistGradientBoostingClassifier random_state=SEED, early stopping off; logistic lbfgs deterministic)",
             ]
    if a.phase == "1":
        lines.append("- Rows read: year == 2013 only (filter applied while scanning; assert_2013 on every frame, fold "
                     "and fit); no 2014 row read, no metric on 2014")
    else:
        lines.append(f"- Rows read: 2013 (fits) and 2014 (scoring only, after the recorded access at "
                     f"{C.test_access_time()}); no refit or tuning on 2014; bootstrap B={C.BOOT_B}, seed {C.BOOT_SEED}")
    folds = C.RESULTS / "folds_2013.csv"
    if folds.exists():
        fd = pd.read_csv(folds)
        for cutoff, g in fd.groupby("cutoff"):
            lines.append(f"- Folds, day {cutoff}: leave-one-run-out over {len(g)} runs: "
                         + ", ".join(f"{r.validation_run} (valid {r.n_valid}, train {r.n_train}, removed {r.removed_rows})"
                                     for r in g.itertuples()))
    lines.append("- Inner tuning: leave-one-run-out over the 8 training runs of each outer fold (results/dev_tuning.csv)")
    fr = C.RESULTS / "freeze.csv"
    if fr.exists():
        for r in pd.read_csv(fr, keep_default_na=False).itertuples():
            lines.append(f"- Freeze: {r.parameter_file} sha256 {r.model_sha256}; first_test_access_utc "
                         f"'{r.first_test_access_utc}' (empty: test not accessed)")
    lines.append("- Test-access record: none (phase 1; the 2014 outcomes are not opened)" if a.phase == "1" else
                 f"- Test-access record: first_test_access_utc {C.test_access_time()} (results/freeze.csv); this run "
                 "used 06_test.py --reproduce if the access was already recorded")
    lines.append("- Deviations from the contract (implementation details it leaves open):")
    lines += [f"  - {d}" for d in C.DEVIATIONS + (C.TEST_DEVIATIONS if a.phase == "2" else [])]
    if a.note:
        lines.append(f"- Note: {a.note}")
    log = C.LOGS / "experiment_log.md"
    if not log.exists():
        log.write_text("# Experiment log – Milestone 4 Level 2 prototype (team N04)\n\nOne entry per run, newest last.\n\n")
    with open(log, "a") as f:
        f.write("\n".join(lines) + "\n\n")
    print(f"appended entry to {log}")


if __name__ == "__main__":
    main()
