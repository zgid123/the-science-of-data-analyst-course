# Changelog – AQ3 and AQ4 into Milestone 5

This file lists every change made to `reports/milestone-5/` to bring AQ3 and AQ4 from `reports/experiment/` into the Milestone 5 package and report, following the AQ1/AQ2 pattern, so that Khanh can check each one.

## Status

In progress (started 2026-11-13). Part A (package) is written and being run; Part B (report) has not started.

## Decisions taken for this change

| Decision | Choice | Why |
| :---- | :---- | :---- |
| Which AQ3/AQ4 run enters the report | The team's Level 2 experiment (`reports/experiment/`), ported into the package | Independent reviewer, second code path, clean-copy reproduction; same verdicts as the Milestone 4 draft package (`reports/experiment/comparison.md`) |
| Tuning criterion of the penalty and tree settings | Pooled log loss of an inner leave-one-run-out loop (new Change Log entry C18) | The Milestone 4 plan says "tuned by nested cross-validation" without a measure; the Milestone 4 draft tuned on recall at capacity. Log loss is a proper scoring rule and suits the calibration condition S3. Chosen after both results were seen; the draft's result (S3 not met) is reported beside it |
| AQ1 and AQ2 | Unchanged | Khanh's Milestone 5 results stay as they are; nothing from `reports/experiment/` replaces them |
| Existing package steps 00–18 and `results/checksums.csv` | Unchanged | The new work is added after step 18, with its own checksum file |
| Per-enrolment scores and fitted models | Kept in `data/interim/aq3/` (git-ignored, rebuilt by `run_all.sh`), not shipped | Like the raw and interim data; `results/` holds aggregated tables only |

## Part A – package (`package/`)

### A1. New files

| File | What it does |
| :---- | :---- |
| `src/analysis/aq34_common.py` | Shared definitions: loaders with a year filter pushed to the reader and asserted, the fixed tie-breaker, list size k = 3 or 5 × ⌈n/20⌉, rule-ranked list, list metrics, the five candidate configurations (B3, M1–M4) with their preprocessing and grids, calibration |
| `src/analysis/aq3_develop.py` | Step 19: development on the 9 runs of 2013 only (leave-one-run-out, nested tuning on log loss, choice rule of Appendix III), final models at days 13 and 27, freeze record with the SHA-256 of every model |
| `src/analysis/aq3_test.py` | Step 20: refuses to run without the freeze; scores the 13 runs of 2014 once; gate S1 (bootstrap 2,000, exact sign-flip), context models, sensitivity views, discrimination and calibration S3, capacity curve, model-only and rule-only students, recall by slice, timing of listed non-completers; `results/aq3/aq3_summary.md` |
| `src/analysis/aq4_lists.py` | Step 21: yield of each contact per tutor group, list summary at 3 and 5 per 20, reach, the reason shown beside each name, rule FR1 (bootstrap 5,000, Holm) and descriptive fairness rates; `results/aq4/aq4_summary.md` |
| `src/analysis/aq34_checks.py` | Step 22: populations, freeze before scores, second count of the listed non-completers, agreement with the Milestone 4 draft package, no student identifier in the shipped results; writes `data/metadata/aq34_checks.csv` |
| `data/metadata/aq34_reference_m4.csv` | Reference values from the Milestone 4 draft package used by step 22 (chosen configuration; rule list 2,786 exactly; model list 2,871 within 5) |
| `results/aq3/`, `results/aq4/` | Result tables written by steps 19–21 (aggregated; no student identifier) |
| `results/checksums_aq34.csv` | Reference SHA-256 of every file in `results/aq3/` and `results/aq4/`, for step 23 |

### A2. Edited files

| File | Change | Effect on existing steps |
| :---- | :---- | :---- |
| `run_all.sh` | Header comment extended; five steps appended after step 18: `19_aq3_develop`, `20_aq3_test`, `21_aq4_lists`, `22_aq34_checks` (check), `23_check_results_aq34` (check) | Steps 00–18 unchanged, same names and order |
| `requirements.txt` | Added, pinned: `scikit-learn==1.9.1`, `joblib==1.6.0`, `threadpoolctl==3.8.0` | Existing pins unchanged |
| `src/checks/check_rebuild.py` | New mode `results_aq34` (patterns `aq3/*`, `aq4/*`; reference `results/checksums_aq34.csv`; output `data/metadata/rebuild_check_results_aq34.csv`). `result_files()` and `results()` take the patterns and file names as arguments, with the old values as defaults | Mode `results` (step 18) behaves exactly as before |

### A3. Still to edit in the package (not done yet)

`README.md` (steps table, structure, dependencies, run time), `results/README.md` (AQ3/AQ4 methods and deviations), `docs/traceability_matrix.md` (AQ3 and AQ4 status), `docs/ai_decision_log.md`, `data/metadata/change_log.md` (C18), `logs/clean_copy_test.md`.

## Part B – report (`report/`, English and Vietnamese)

Not started.
