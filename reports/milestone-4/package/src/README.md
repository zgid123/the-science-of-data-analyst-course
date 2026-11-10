# Prototype code – phase 1 (development and freeze) and phase 2 (single test and analyses)

Implements steps 1–5 of report Appendix III, Table A.5, under the contract in `../README.md`. Only rows of
`year == 2013` are read (filter applied while scanning; `assert_2013` on every frame, fold and fit). Phase 2
(`06_test` onwards, the single test on 2014) is not part of this phase.

Setup (shared environment): `venv/bin/pip install -r reports/milestone-4/package/requirements.txt`

| Command (from the repository root) | Does | Writes |
| :---- | :---- | :---- |
| `bash reports/milestone-4/package/src/run_dev.sh` | Tests, then steps 01–05; logs per step; one experiment-log entry | `logs/<step>.log`, `logs/experiment_log.md` |
| `bash reports/milestone-4/package/src/check_determinism.sh` | Runs `run_dev.sh` twice and compares SHA-256 of all results and models | `logs/determinism.log` |
| `venv/bin/python -m unittest discover -s reports/milestone-4/package/tests -v` | Tests on synthetic fixtures (metrics, ties, fold-local preprocessing, 2013 guard) | – |
| `venv/bin/python reports/milestone-4/package/src/01_load_check.py` | Hash check against `version_manifest.json` (stop on mismatch); 2013 populations; folds | `results/input_hashes.csv`, `populations_2013.csv`, `folds_2013.csv` |
| `venv/bin/python reports/milestone-4/package/src/02_baselines.py [--jobs N]` | B1 random list, B2 early-sign rule, B3 background-only logistic (nested) | `results/dev_folds_baselines.csv`, `dev_tuning_baselines.csv` |
| `venv/bin/python reports/milestone-4/package/src/03_dev_folds.py [--jobs N]` | M1–M4, nested leave-one-run-out, day 13 and 27, k = 3 and 5 per 20 | `results/dev_folds.csv`, `dev_tuning.csv` |
| `venv/bin/python reports/milestone-4/package/src/04_choose.py` | Selection rule (gain ≥ 0.03 and gain in ≥ 7 of 9 folds) | `results/model_choice.csv` |
| `venv/bin/python reports/milestone-4/package/src/05_freeze.py` | Refit the chosen configuration on all 9 runs of 2013 per cut-off | `models/frozen_<config>_d<cutoff>.joblib`, `.spec.json`, `results/freeze.csv`, `freeze_tuning.csv` |

Phase 2 (steps 6–8 of Table A.5, after the lead approved the freeze). `06_test.py` records the test access in
`results/freeze.csv` and the experiment log before reading any 2014 row, and refuses a second access; `--reproduce`
recomputes with the same frozen models and checks byte identity. `run_dev.sh` and `05_freeze.py` refuse to redo the
freeze once the access is recorded.

| Command (from the repository root) | Does | Writes |
| :---- | :---- | :---- |
| `bash reports/milestone-4/package/src/run_test.sh` | Tests, 06 (or 06 `--reproduce`), 07–12; logs per step; one experiment-log entry | `logs/<step>.log`, `logs/experiment_log.md` |
| `bash reports/milestone-4/package/src/check_determinism_test.sh` | Runs `run_test.sh` twice; compares SHA-256 of all outputs | `logs/determinism_test.log` |
| `venv/bin/python reports/milestone-4/package/tests/dry_run_phase2.py` | Code-path dry run of 06–12 on a temporary copy with 2013 rows standing in for the test | console (`logs/dry_run_phase2.log`) |
| `venv/bin/python reports/milestone-4/package/src/06_test.py [--reproduce]` | Single test: B3 fit on 2013, access record, scoring of the 13 runs of 2014 | `results/test_runs.csv`, `b3_fit.csv`, `models/fitted_B3_d<cutoff>.joblib` |
| `venv/bin/python reports/milestone-4/package/src/07_gates.py` | S1 (bootstrap, sign-flip), S2/secondary, net benefit, S3 calibration, Brier | `results/s1_gate.csv`, `s1_per_run.csv`, `secondary.csv`, `net_benefit.csv`, `calibration.csv`, `calibration_bins.csv`, `brier.csv` |
| `venv/bin/python reports/milestone-4/package/src/08_fairness.py` | FR1 recall gaps, Holm-adjusted one-sided bounds | `results/fairness.csv` |
| `venv/bin/python reports/milestone-4/package/src/09_sensitivity.py` | S1 statistics per sensitivity variant | `results/sensitivity.csv`, `sensitivity_detail.csv` |
| `venv/bin/python reports/milestone-4/package/src/10_aq4_lists.py` | AQ4 lists with reasons; list quality per run | `results/aq4_lists/lists_d<cutoff>.csv`, `results/aq4_lists_summary.csv` |
| `venv/bin/python reports/milestone-4/package/src/11_aq2_replication.py` | AQ2 re-estimated on 2014 (method copied from Milestone 5) | `results/aq2_replication.csv`, `aq2_replication_detail.csv` |
| `venv/bin/python reports/milestone-4/package/src/12_report.py` | Code-generated report from the CSV files, with figures | `report/prototype_report.md`, `.html`, `report/figures/*.png` |

`gates.py` holds the gate statistics (S1, bootstrap, sign-flip, recall gap, Holm). `common.py` holds the shared code (loading and guard, per-fold preprocessing, metrics of Appendix II, folds and
tuning) and the lists of deviations (`DEVIATIONS`, `TEST_DEVIATIONS`), which every experiment-log entry repeats.
