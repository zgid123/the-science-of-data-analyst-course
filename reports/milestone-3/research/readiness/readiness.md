# Analytics and model readiness (Task 7, brief section 12)

Evidence: `V.` = `package/data/metadata/validation_summary.json`, `P.` = `profile.json`, views in
`package/data/processed/`, roles in `data_dictionary.md`.

## 1. Prepared views by analytics level (Table 8.1)

| Level | Prepared view | Population and denominator | Grain | Check before Milestone 4 (brief section 12) | Result |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Descriptive | `enrolment`, `assessment_due`, `student_week` | All 32,593 enrolments; KPI on the 28,061 enrolled at day 14 | enrolment; enrolment × task; enrolment × week | Summaries without double counting or join bias | Keys unique (V03), every join kept its rows (V09), clicks reconcile with the raw log (V04) |
| Diagnostic | `features_d27` + `enrolment` | 27,535 enrolled at day 27 | enrolment | Associations from real data, comparison groups, module as context | Signs built only from events up to day 27 (V13); audit columns kept; within-module comparisons possible (7 modules) |
| Predictive | `features_d13`, `features_d27`, `model_ready_d13/d27` | 28,069 and 27,535 enrolled at the cut-off; 45.3% and 44.2% non-completion | enrolment | Target and prediction point, pre-point features, time split, leakage-safe transforms, enough of each class | Smallest class in a run 92 (P.outcome); 9 training and 13 test runs (V15); parameters from training rows only (V12); features recomputed from raw with 0 mismatches (V11) |
| Prescriptive | `capacity_by_run` | 44 run × cut-off rows | run × cut-off | Action, constraint, cost and outcome data | List sizes under assumed capacities only; no contact, cost or outcome-after-contact data: decision requirement (C08, C11) |

## 2. Model Readiness Matrix (Table 8.2)

| AQ | Analytics type | Prepared view / table | Target / measure | Feature set / dimensions | Split / time rule | Readiness |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | `enrolment`, `assessment_due` | completion and non-completion rates; first missed task week | module, run, start month, year | All 22 runs; KPI population enrolled at day 14 | Ready |
| AQ2 | Diagnostic | `features_d27`, `enrolment` | non_completion | missed tasks, late TMA and CMA, inactivity in the last 7 days, activity against the run median; concurrent runs for 2014 only | Signs up to day 27; task signs in the 16 runs with a task due | Ready (association, not cause) |
| AQ3 | Predictive | `features_d13`, `features_d27`, `model_ready_*` | non_completion at run end | 20 primary predictors, of which the CMA score falls below the 10% coverage rule (known for 1.4% and 5.3% of training rows) and is left out; 10 extended predictors plus the weekly click counts (2 at day 13, 4 at day 27); comparison rule `early_sign_rule` (fires for 20.2% of enrolments at day 13, 28.8% at day 27) | Train 2013 runs, test 2014 runs; tuning by leave-one-run-out folds in 2013 grouped by student; fitted transforms from training rows | Ready (week-3 list on activity only) |
| AQ4 | Prescriptive | `capacity_by_run` + AQ3 scores | lift over the run base rate; recall against the most a list of that size reaches | lists of 3 or 5 per tutor group of 20, 30 or 40 per run; audit groups imd_band (with "Missing" apart) and disability | Per run and cut-off, test runs only | Revise: ranking ready; choice of contact and its effect deferred to the pilot |

## 3. Questions not yet feasible

- AQ4: which contact (lecturer message, support-office call, referral) works best, and its effect on completion; needs
  a contact record and outcomes after contact from the pilot (C08, C11).
- AQ1–AQ3 comparisons by year of study and delivery mode (C04) and the attendance sign (C05).
- Secondary KPI 2 (follow-up rate) and the contact part of secondary KPI 1: measured only in the pilot (C08).

## 4. Milestone 4 entry conditions (brief section 19)

| Condition | State |
| :---- | :---- |
| Core AQs have a prepared view with traceability | AQ1–AQ3 views ready; AQ4 ranking view ready, action part deferred (Table A.7) |
| Target, features and dimensions stable | Defined in `feature_spec.md` and `data_dictionary.md`; tests 9/9 |
| Leakage and split defined for predictive tasks | `split_spec.md`; V11–V13, V15 PASS |
| Important quality issues handled or kept on purpose | DQ01–DQ19 each with a decision; residual risks listed (Section 7.3) |
| No synthetic data as evidence | Only labelled level A fixtures in `package/tests/` |
| Prepared data reproducible from raw | Two runs from raw, 8 of 8 output files identical (logs/T12_prepare_rerun.log) |
