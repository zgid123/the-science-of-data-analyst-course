# AQ3 – working notes

## Brief

- **Question (Level 1, Table 2.3).** How well can non-completion be estimated from the data up to the end of week 2 (day 13) and of week 4 (day 27), compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs?
- **Level and task.** Predictive; binary classification used as a ranking within each run.
- **Reader and decision.** Lecturer-advisors and the support office: D1, who is listed for contact.
- **Population.** Enrolments registered at the cut-off. Development: 9 runs of 2013 (12,080 at day 13; 11,811 at day 27). Test: 13 runs of 2014 (15,989; 15,724).
- **Baselines.** Random list; early-sign rule ranked by its number of signs; background-only logistic model.
- **Primary approach.** Penalised logistic regression on the primary predictors (M1). **Challengers.** Extended predictor set (M2), gradient-boosted trees (M3, M4).
- **Gate S1 (Table 4.5).** Pooled normalised recall of the model above the rule's, 95% paired two-level bootstrap interval above 0, one-sided sign-flip p < 0.05; all 13 test runs, day 27, 5 per 20. **Result: met.**
- **Status of the run.** Rerun of 12 November 2026: a reproduction of the first run of 11 November (commit `11f4aca`) with no AQ3 design choice changed (`../PROTOCOL.md` P01–P15, P19). The 2014 outcomes and the first run's results were known when the rerun started. First run: frozen 2026-11-11T23:18:16Z, first test access 2026-11-11T23:19:02Z. Rerun: frozen 2026-11-12T15:58:51Z, first test access 2026-11-12T15:58:53Z.
- **Playbook used.** `playbooks/early-warning.md` of the data-analyst skill (cut-off, eligibility, baselines first, temporal holdout, workload view, who is missed, calibration, stress tests).

## Decisions taken while working

| Decision | Reason |
| :---- | :---- |
| Implementation choices P01–P15 and P19 are those written in `../PROTOCOL.md` before the first run's first result (11 November 2026); none was changed for the rerun | Level 1 leaves penalty type, grids, tuning criterion and tie-breaking open; changing one after the 2014 outcomes were seen would let those outcomes shape the model |
| Test rows extracted without outcome columns before the freeze (`aq3_test_features_blind_d*.csv`) | A script cannot use what it does not hold |
| Scores of the test rows saved before the outcomes are joined | The order "score, then open" is visible in `05_test.py` and its log |
| All five fitted configurations frozen, not only the chosen one | Trade-offs on the test can be shown without any refit after the test |
| Ties at the list edge broken by a fixed pseudo-random number per enrolment | Outcome-independent and reproducible; the expected-tie value is reported beside it and is the same to four decimals |
| Every AQ3 and AQ4 result table compared with the first run by `../common/compare_first_run.py` | A reproduction must show that it reproduces |
| Earlier team run (`reports/milestone-4/package/`) compared again | In the first run it was opened only after every result existed; in the rerun its numbers were already known, so the comparison is a consistency check of two implementations |

## Methods checklist

- [x] Input check: hashes, counts against Level 1 Table A.6, capacity rule against `capacity_by_run.parquet` – `results/input_check.csv`
- [x] Baselines before candidates on the development folds – `results/dev_folds.csv` (rankings `B2_rule`, `B3`; random analytic)
- [x] Leave-one-run-out folds with removal of repeat students; nested tuning – `results/dev_fold_design.csv`, `dev_tuning.csv`
- [x] Model choice by the Level 1 margin – `results/model_choice.csv`
- [x] Second freeze with SHA-256 and time – `results/freeze.json`, `frozen_models.csv`, `results/models/`
- [x] Single test: list metrics per run and pooled – `results/test_runs.csv`, `test_pooled.csv`
- [x] Gate S1: bootstrap interval, sign-flip test, wins / ties / losses – `results/s1_gate.csv`, `s1_gate_per_run.csv`, `s1_bootstrap.csv`
- [x] S2 and secondary metrics: precision against base rate and ceiling, lift, ROC-AUC and PR-AUC within run – `results/secondary.csv`
- [x] S3: calibration-in-the-large, slope, Brier, bins, per run – `results/calibration.csv`, `calibration_bins.csv`, `calibration_by_run.csv`
- [x] Net benefit as context – `results/net_benefit.csv`
- [x] Error analysis by run, activity, attempts, registration, kind, reach – `results/errors_by_run.csv`, `errors_by_slice.csv`
- [x] List overlap and stability near rank k – `results/list_overlap.csv`, `list_stability.csv`
- [x] Sensitivity: paired / unpaired, CCC, repeat students, missing withdrawal day, rule with CMAs, labels-available, day 13, 3 per 20 – `results/sensitivity.csv`
- [x] Verification V1–V7 – `results/verification.csv`
- [x] Determinism: development folds rerun inside the pipeline, 5 output files byte-identical – `../logs/determinism_before.sha256`, `determinism_after.sha256`, `../logs/determinism_after.md`
- [x] Reproduction of the first run: every result table compared with commit `11f4aca` – `../logs/compare_first_run.md`, `../logs/compare_first_run.csv`
- [x] Comparison with the earlier team run – `results/crosscheck_earlier_run.csv`, `crosscheck_per_run.csv`
- [x] Figures – `figures/fig-aq3-1` to `fig-aq3-5`
- [ ] Discrete-time survival model (Level 1 extension, not part of the prototype)
- [ ] Recalibration inside development (Level 1 lists it as optional; not fitted, and never on 2014 rows)
- [ ] Decision curves as a figure (net benefit table only)

## Check ledger

| Check | Condition evaluated | Result | Evidence |
| :---- | :---- | :---- | :---- |
| Input | Three prepared files equal the Milestone 3 manifest; counts equal Level 1 Table A.6; list-length rule reproduces the capacity table in 22 runs | PASS | `logs/01_extract.md` |
| Ceiling | Most non-completers the 9 development lists can hold = 2,976 (day 27) and 3,032 (day 13), as in Level 1 Table A.6 | PASS | `results/dev_pooled.csv` |
| Parameters | Frozen M1 has 23 parameters besides the intercept, as Level 1 states | PASS | `logs/04_freeze.md` |
| Freeze | 12 model files unchanged between freeze and test (SHA-256) | PASS | `logs/05_test.md` |
| V1 | Refit of M1 with the frozen hyperparameters reproduces the saved test scores (6 decimals) | PASS, largest difference 5e-07 | `logs/09_verify.md` |
| V1b | Lists from unrounded scores hold the same number of non-completers | PASS, 2,870 = 2,870 | `logs/09_verify.md` |
| V2 | S1 counts recomputed by a second code path | PASS, 2,870 / 2,786 / 3,955 | `logs/09_verify.md` |
| V3 | AQ4 and error-analysis counts equal the S1 counts | PASS | `logs/09_verify.md` |
| V4 | No audit or outcome column among the 33 model inputs | PASS | `logs/09_verify.md` |
| V5 | Every input has the role predictor or predictor_extended in the Milestone 3 dictionary | PASS | `logs/09_verify.md` |
| V6 | First test access of the rerun (2026-11-12T15:58:53Z) after its freeze (2026-11-12T15:58:51Z). This shows the order of the scripts, not a blind test | PASS | `logs/test-access.md` |
| V7 | Prepared files still equal the manifest after all runs | PASS | `logs/09_verify.md` |
| Unit tests | 17 of 17 code-path tests of the metric functions on labelled synthetic inputs | PASS | `../logs/tests_lib.md` |
| Determinism | Development outputs byte-identical after a full rerun of the folds inside the pipeline | PASS, 5 of 5 files | `../logs/determinism_after.md` |
| Reproduction | Every AQ3 result table equals the first run (commit `11f4aca`) | PASS: 28 of 30 byte-identical; 2 differ only in a column that records run time; 12 of 12 model files with the same SHA-256; 16 of 16 AQ3 headline numbers equal | `../logs/compare_first_run.md` |
| Comparison with the earlier team run | Rule list identical in 13 of 13 runs; model lists differ by 1 non-completer in total | Agree on S1; differ on S3 | `logs/10_crosscheck_earlier_run.md` |

8 of 8 verification checks pass (`results/verification.csv`). No step of the final pass failed. In the first run two checks failed on their first execution and were corrected in the checking code (a tolerance of 1e-9 against scores stored with 6 decimals; an unsigned-integer overflow in a displayed difference); the corrected code is what ran here. In the rerun one checking step failed in the first pass, the comparison with the first run, because it counted the freeze time quoted in the detail text of V6 as a changed value; `../logs/process-log.md`, section 6, has the record.

## Open issues

- **S3 is not robust.** Met here (slope 0.873), not met in the earlier team run (slope 1.311); the difference is the tuning criterion. Proposed Change Log entries C15 and C16 in the report, Section 7, are for the team to decide.
- **Frozen penalty differs between cut-offs** (C = 10 at day 27, C = 0.01 at day 13). At day 27 the leave-one-run-out log loss falls slowly from 0.5899 at C = 0.003 to 0.5871 at C = 10 (`results/freeze_tuning.csv`), a difference of 0.003, so the choice of C there is weakly determined; the ranking does not depend on it (report, Section 6).
- **Two coefficients share one signal:** `tasks_late_c` (−0.16) and `tma_late_c` (+0.29) are nearly collinear; reasons shown to tutors should name "TMA late" once.
- **Unpaired runs:** the gain is positive but its interval includes 0; more runs are needed to show transfer to a new module.
