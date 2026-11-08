# AI leakage auditor – findings (T14)

Instruction: `reports/milestone-3/research/review/leakage-auditor-prompt.md`. Files read: `package/src/prepare_data.py`,
`fit_transforms.py`, `validate_prepared.py`, `dictionary.py`, `common.py`, and `package/data/metadata/feature_spec.md`,
`split_spec.md`, `decision_matrix.md` (plus `validation_summary.md` and `transform_params.json` for the stored check
results and fitted values). All paths below are relative to `reports/milestone-3/package/`. No project file was
modified and no pipeline script was run. Queries were read-only polars scripts kept outside the repository
(session scratchpad `T14/q.py`, `q2.py`, `q3.py`), run as
`venv/bin/python <script> reports/milestone-3/package` from the repository root on 2026-11-06; their inputs were
`data/processed/*.parquet`, `data/raw/studentAssessment.csv`, `data/raw/assessments.csv` and
`data/metadata/transform_params.json`.

Summary: 0 high, 2 medium, 6 low. The feature windows themselves hold: no feature reads an event after its cut-off,
and every fitted parameter comes from training rows (see "Checked without a finding").

## Queries run and results

| ID | Query | Result |
| :---- | :---- | :---- |
| Q1 | `features_d13/d27`: count, non-completion rate and Withdrawn count by `registration_missing` × `split` | d13: 5 train rows (non-completion 1.0), 2 test rows (0.5); d27 identical; base rate 0.453 (d13), 0.441 (d27) |
| Q2 | `model_ready_d13` joined to `features_d13` on the enrolment key: `registration_lead_missing > 0` vs `registration_missing`; is the indicator in `transform_params.json` `primary` / `columns` | Equal on all 28,069 rows; scaled values −0.0203 and 49.14; not listed in `primary`, listed in `columns` |
| Q3 | Enrolments with `withdrawal_day_missing` (enrolment view) inside each feature view: count, split, zero `clicks_0c` | d13: 92 (train 3, test 89), 38 with 0 clicks (41%) vs 9.5% of all other rows; d27: 93 (train 3, test 90), 38 with 0 clicks vs 4.3% |
| Q3b | Same flag by run (enrolment view) | 2014J runs hold 87 of 93: CCC 28, FFF 24, DDD 16, BBB 13, EEE 4, GGG 2; every other run ≤ 1 |
| Q4 | `assessment_due` rows due ≤ c with `due_day < date_registration`, for enrolments in each feature view | d13: 0; d27: 10 task rows in 10 enrolments, 6 of them not submitted by day 27 |
| Q5 | TMA/CMA rows with null `due_day` | 0 |
| Q6 | Banked studentAssessment rows by assessment type | TMA 1,338; CMA 571; no exam |
| Q7 | Rank AUC of `id_student` for `non_completion` | d13 train 0.4664, test 0.4658; d27 train 0.4692, test 0.4657; per 2013 run 0.4625–0.5318 |
| Q7c | Spearman of `id_student` with `num_of_prev_attempts`, `registration_lead`, `studied_credits` (d13); AUC of `id_student` for `student_in_training_runs` (d13 test) | −0.187, −0.085, −0.077; AUC 0.33 |
| Q8 | Null count per feature-view column by split | Only `registration_lead` (train 5 / test 2), `cma_score_mean_c` (11,913 / 15,849 at d13; 11,191 / 13,859 at d27), `days_since_last_click` (1,299 / 1,404; 607 / 624) |
| Q9 | CMAs due ≤ 27 (raw `assessments.csv`) | CCC 2014B and 2014J (day 18), DDD 2013B (day 23) |
| Q10 | Non-null `cma_score_mean_c` | 307 rows at d13, 2,485 at d27 |
| Q11 | Enrolment view: `banked_results > 0` × `num_of_prev_attempts > 0`; date of banked rows | Banked results only with prior attempts (526 rows); every banked `date_submitted` = −1 |
| Q12 | Tasks due ≤ 27 by run (`assessment_due`) | 17 tasks; earliest BBB 2014B TMA day 12 (the only task due ≤ 13) |
| Q13 | Details of the Q4 rows | 3 late TMAs submitted on days 30, 34, 32 by students registered on days 20, 27, 27; 4 banked TMAs; 3 CCC 2014J CMAs (due 18) not submitted by students registered on days 19, 23, 23 |
| Q14 | d27 rows due ≤ 27, not `due_while_enrolled`, not banked, not submitted by 27 | 6 rows in 6 enrolments |
| Q15 | `fill_median` in `transform_params.json`; training non-completion by `days_since_last_click` null vs equal to the filled value | d13 `days_since_last_click` 1.0, `cma_score_mean_c` 89.0, `registration_lead` 53.0; d27 1.0, 87.0, 54.0. Non-completion: null 0.734 vs value 1 → 0.412 (d13); 0.811 vs 0.393 (d27) |
| Q17 | Column list of `features_d13.parquet` | Holds `id_student`, `code_presentation`, `year`, `split`, `final_result`, `non_completion`, rule columns and the five audit columns next to the predictors |

## Findings

### F1 (medium) – Withdrawn enrolments without a withdrawal day stay in every cut-off population, almost all in the test runs

- **Evidence.** `common.py` lines 60–61: `enrolled_at` keeps a row when `date_unregistration` is null. For the 93
  Withdrawn enrolments without a day (`prepare_data.py` line 133, `withdrawal_day_missing`), the null hides when they
  left, so they enter both feature views (Q3: 92 at d13, 93 at d27) as positives. They are concentrated in the 2014J
  runs (Q3b: 87 of 93), so 89 of 92 (d13) sit in the test partition, and 41% of them have no click in days 0–13
  against 9.5% of all other rows (Q3).
- **Risk.** Population rule using an unknowable state: some of these students had probably already left before the
  cut-off and would not be on any real list. They are easy positives that exist almost only in the test runs, so
  test recall and precision on 2014J are inflated relative to training, and the train–test populations differ.
- **Fix.** Keep `withdrawal_day_missing` out of the predictors (it is target-derived, as now), but carry it in the
  feature views as an evaluation flag and report Milestone 4 test metrics with and without these 92/93 rows; state
  the 2014J concentration as a scope limit.

### F2 (medium) – Identifiers and target columns travel inside the feature views that tree models use "as they are"

- **Evidence.** `fit_transforms.py` lines 7–8: "Tree models use the prepared views as they are." `prepare_data.py`
  lines 345–348 put `id_student`, `code_presentation`, `year`, `split`, `final_result`, `non_completion` and the
  audit columns in the same table as the predictors (Q17). `id_student` carries signal: rank AUC 0.466 for
  non-completion in both train and test (Q7), Spearman −0.187 with `num_of_prev_attempts` and AUC 0.33 for
  `student_in_training_runs` (Q7c), i.e. lower ids belong to students with a longer history.
- **Risk.** A tree model fitted on `df.drop("non_completion")` would learn from `final_result` (direct leak) or from
  `id_student` (a proxy for prior attempts and student cohort); `year`/`split` are constant within a partition. The
  roles exist in `dictionary.py`, but no code enforces them for tree models.
- **Fix.** Export one predictor whitelist (`PREDICTORS`, `EXTENDED`, `clicks_w*`) for all model families and assert
  in Milestone 4 that the model input holds no `id`, `split`, `target` or `audit` column; optionally write a
  `tree_ready_d13/d27` view with only those columns plus the key and target in separate files.

### F3 (low) – A target-proxy indicator enters the primary model matrix through median filling

- **Evidence.** `fit_transforms.py` lines 42–43 and 66–68 create `registration_lead_missing` because
  `registration_lead` (a primary predictor) has nulls. It equals `registration_missing` on every row (Q2), which
  `dictionary.py` line 45 declares an extended predictor ("39 of 45 are Withdrawn"). In the feature views it marks 5
  training rows, all non-completers (Q1), and after scaling takes the value 49.14 (Q2). `transform_params.json`
  lists it under `columns` but not under `primary` (Q2).
- **Risk.** The primary linear model silently receives an extended, outcome-laden flag with an extreme scaled value;
  with weak regularisation it fits those 5 rows exactly. Impact on metrics is small (7 rows) but the primary/extended
  separation is broken.
- **Fix.** For `registration_lead`, fill with the training median without an indicator in the primary matrix (the
  indicator is already available as `registration_missing` in the extended set), or list the indicator explicitly
  as extended in `transform_params.json`.

### F4 (low) – Whether a missing indicator exists is decided on train and test rows together

- **Evidence.** `fit_transforms.py` line 42: `if df[x].null_count():` reads the full frame, not `tr`. The V12
  self-check in the same file (lines 86–92) alters test values with `x * 3 + 7`, which keeps nulls null, so it cannot
  detect this. Today every column with nulls also has nulls in training rows (Q8), so the parameters are unaffected,
  and `validate_prepared.py` V12 (fit on all rows vs on training rows only) passes.
- **Risk.** A future column with nulls only in test rows would add a model column whose existence depends on test
  data, and `float(tr[x].median())` would then be computed on training values only, possibly `None`.
- **Fix.** Use `tr[x].null_count()` (or a fixed list of nullable columns from the spec), and make the self-check
  also null out some test values.

### F5 (low) – Tasks due before the student registered count as missed at day 27

- **Evidence.** `prepare_data.py` lines 211–215 count every task with `due_day <= c` and no submission by c as
  missed; they do not use `due_while_enrolled` (line 185–187), which the spec uses for whole-run missed counts. At
  d27, 10 task rows in 10 enrolments were due before the student registered (Q4); 6 of them count as missed (Q14):
  3 TMAs later submitted on days 30–34 by students registered on days 20 and 27, and 3 CCC 2014J CMAs due on day 18
  for students registered on days 19 and 23 (Q13). d13 is unaffected (Q4).
- **Risk.** Feature formula bug: late registrants get `tasks_missed_c` and `rule_missed` for tasks they could not
  submit while enrolled; the early-sign rule fires for them. No future information is used.
- **Fix.** Restrict the cut-off task counts to tasks due on or after `date_registration` (null registration counts
  as registered), matching `due_while_enrolled`, and apply the same filter in the V11 recount.

### F6 (low) – Never-active students receive "last click 1 day ago" in the model matrices

- **Evidence.** `fit_transforms.py` lines 42–43 and 66–68 fill `days_since_last_click` nulls (no click in days 0…c,
  `prepare_data.py` line 252) with the training median 1.0 at both cut-offs (Q15). In training rows these students
  have non-completion 0.734 (d13) and 0.811 (d27), against 0.412 and 0.393 for rows whose real value is 1 (Q15).
- **Risk.** Not leakage, but a formula that maps the riskiest group onto the safest value; a linear model must use
  the `_missing` indicator to undo it, and any model without the indicator (or a SHAP reading of the column) is
  misled.
- **Fix.** Fill with c + 1 (no click since before day 0), or with the days since the last pre-start click, and keep
  the indicator.

### F7 (low) – The V13 "no event after the cut-off" check can never fail

- **Evidence.** `validate_prepared.py` line 124 builds `s = sv.join(pop, ...).filter(pl.col("date") <= c)`, and
  line 151 then counts `s.filter(pl.col("date") > c)`, which is 0 by construction. The real guard is the assertion
  in `prepare_data.py` line 262 (`_last_event_day <= c`, `_last_cma_day <= c - 7`).
- **Risk.** The validation summary reports V13 PASS as independent evidence that no later event entered a feature,
  but the check tests nothing; the CMA-score window and the submission windows are not covered by any independent
  check.
- **Fix.** Recompute in the validator, from unfiltered raw rows, the maximum event day and maximum CMA submission
  day that contribute to each row's features (activity ≤ c, submissions ≤ c, CMA marks ≤ c − 7) and compare.

### F8 (low) – The V14 role check for extended predictors is commented out

- **Evidence.** `validate_prepared.py` line 170: `... and x != "code_module"]  # module: key and predictor + [x for x
  in EXTENDED if C[x][0] != "predictor_extended"]` – the EXTENDED part sits inside the comment, so it never runs.
  Every current EXTENDED column has role `predictor_extended` in `dictionary.py` (lines 45, 71, 73, 85–91), so no
  wrong role exists today.
- **Risk.** An audit, target-derived or descriptive column added to `EXTENDED` would pass V14 unnoticed.
- **Fix.** Move the comment to the end of the line so the EXTENDED clause is part of `roles_bad`.

## Checked without a finding

- Activity windows: `clicks_w{w}` (days 7(w−1) to 7w−1, w ≤ (c+1)//7), `clicks_last7` (c−6…c), `clicks_pre14`,
  `trend_last_week` match the spec (`prepare_data.py` lines 196–206); V11 recount from raw matches on all rows
  (`validation_summary.md`).
- CMA scores use submissions ≤ c − 7 only (line 227, assertion line 262); CMAs due ≤ 27 exist only in 3 runs (Q9) and
  only 307 / 2,485 rows have a known mark (Q10). The 7-day release assumption itself cannot be tested: OULAD holds no
  release day.
- Banked results: carried over from earlier attempts only (Q11), dated −1, excluded from missed/late/early counts
  (`nb`, lines 212–218); no exam is banked or counted (Q6, line 96). No TMA/CMA lacks a due day (Q5).
- `activity_ratio_run` uses the same run's median of pre-cut-off clicks over students enrolled at c (lines 246–251);
  it uses no outcome and no other run, and the value is available to staff on day c.
- `fit_transforms.py`: levels, log1p choice, medians, means and standard deviations come from `split == "train"`
  (lines 34–52); V12 refit without test rows gives identical, stored parameters (`validation_summary.md`).
- `concurrent_runs`, whole-run counts and `logging_gap` (which use post-cut-off information) are only in the
  enrolment and student_week views, not in the feature views (Q17); `student_in_training_runs` uses only 2013
  enrolments.
- Truncation at the unregistration day (`step6_truncate`) cannot change a feature row, because feature rows have
  `date_unregistration > c`.
