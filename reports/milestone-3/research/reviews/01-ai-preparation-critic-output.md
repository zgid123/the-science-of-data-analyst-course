# AI preparation critic – critiques (T11)

Files read (only these): `reports/milestone-3/package/data/metadata/quality_issue_log.md` (DQnn),
`reports/milestone-3/research/preparation/decision-matrix.md` (DM), `feature-spec.md` (FS), `split-spec.md` (SS),
`reports/milestone-3/research/fit/aq-data-fit.md` (FIT) and `reports/milestone-3/package/data/metadata/profile.json`
(`P.` + key path). No file was modified and no data script was run. Derived ratios are computed by hand from the
cited counts and marked "derived".

## 1. The AQ4 precision target of 50% sits barely above the base rate

- **Issue.** AQ4 requires "precision ≥ 50%" on a capacity-length list (FIT, AQ4 row). The non-completion base rate
  in the day-13 population is 45.27% (`P.outcome.population_at_cutoff.d13.rate` = 0.4527) and 44.15% at day 27
  (`P.outcome.population_at_cutoff.d27.rate` = 0.4415). Across runs the day-14 rate ranges from 24.86% to 58.33%
  (`P.outcome.kpi_non_completion_by_run_range`). A random list therefore reaches about 45% precision overall and
  more than 50% in the highest-rate runs. The list holds 3 or 5 students per tutor group of 20 (FS, `list_size_*`),
  i.e. 15% or 25% of the enrolled (derived), so recall is capped at about 0.15/0.45 ≈ 33% and 0.25/0.45 ≈ 55%
  (derived) even for a perfect ranking.
- **Why it matters.** AQ4 (and AQ3 evaluation): the threshold cannot separate a useful ranking from chance, and
  recall targets above the cap are unreachable by construction.
- **Recommendation.** Express the AQ4 target as lift over each run's base rate (precision@k ÷ run rate) and as
  recall against the maximum attainable recall at that k; report a random-list and early-sign-rule baseline per run
  and per cut-off. State the tutor-group size of 20 as an assumption (not verifiable from these files).
- **Severity.** High.

## 2. Target-derived flags and the registration-missing indicator need explicit exclusion from predictors

- **Issue.** `withdrawal_day_missing` is defined only for Withdrawn enrolments and `unregistered_not_withdrawn`
  only for Fail enrolments (DQ04): both are functions of the target. `registration_missing` (DM, "Missing values")
  is near-diagnostic of the outcome: 39 of 45 missing registration days belong to Withdrawn enrolments
  (`P.missing.date_registration_missing_by_outcome`; 87% derived). DM's role list (id, target, predictor, audit,
  descriptive) and V14 check only that no *audit* column is a predictor; they do not name these flags or test for
  target-derived columns.
- **Why it matters.** AQ3 (target leakage), AQ2 (spurious association). A missing registration day may be an
  artefact of how withdrawals were recorded rather than something known at the cut-off; the cause is not verifiable
  from these files.
- **Recommendation.** Add a role `target_derived` and assign both DQ04 flags to it; extend V14 to fail if any
  `target_derived` column reaches a feature view. Keep `registration_missing` out of the primary predictor set, or
  include it only in a pre-declared ablation, and report its univariate association with the target on 2013 runs.
- **Severity.** High.

## 3. The early-sign rule collapses to "inactive in the last 7 days" at day 13 and fires unevenly at day 27

- **Issue.** A non-exam task is due by day 13 in 1 of 22 runs and by day 27 in 16; 6 runs have no task due by day 27
  (`P.temporal.tasks_due_by_cutoff.d13.runs_with_task_due` = 1; `.d27.runs_with_task_due` = 16;
  `.d27.tasks_due_per_run_values` [0, 6]). The restated rule (C10, FS `early_sign_rule`) is therefore an inactivity
  rule at day 13 in 21 runs and in 6 runs at day 27. FIT says the rule "can fire in every run", which is true only
  through its inactivity part.
- **Why it matters.** AQ3 comparison baseline and secondary KPI 1: the comparison "model vs rule" compares against a
  different rule in different runs, and the secondary KPI mixes task-based and activity-based signals by run.
- **Recommendation.** Report the rule's firing rate and each component (missed, late, inactive) per run and cut-off;
  label the day-13 rule as an activity rule; evaluate the task component only in the runs with a task due (as AQ2
  already does in FIT).
- **Severity.** High.

## 4. Students seen in both years and students with several enrolments are not handled as dependent units

- **Issue.** The main test keeps 2014 enrolments of students seen in 2013 and only flags them
  (`student_in_training_runs`, SS "Student leakage"); the size of this group is not verifiable from these files.
  In addition, 1,370 day-14 enrolments in 2014 runs are concurrent enrolments of the same student
  (`P.temporal.concurrent_enrolments_day14.by_presentation`: 2014B 642 + 2014J 728, derived sum), so test rows are
  not independent. Tuning uses "run-grouped folds inside 2013" (DM, "Split"), which do not group a student enrolled
  in both 2013B and 2013J.
- **Why it matters.** AQ3 (optimistic validation and too-narrow confidence intervals), AQ4 (one student may occupy
  two list places).
- **Recommendation.** Report the count and outcome rate of `student_in_training_runs` before modelling; use folds
  grouped by run *and* student inside 2013 (or check overlap and drop cross-fold repeats); compute test intervals
  with a bootstrap clustered by `id_student`; decide whether a student appears once or per module on the AQ4 list.
- **Severity.** Medium.

## 5. The time split leaves a whole module unseen in training and few folds for tuning

- **Issue.** Training has 9 runs and test 13 (SS); CCC appears only in the test runs (SS, "Paired subset": CCC-B,
  CCC-J among the 4 unpaired test runs), and CCC has the lowest day-14 completion, 45.7%
  (`P.representativeness.kpi_completion_by_module` CCC = 0.457). The training population is smaller than the test
  population: 12,076 against 15,985 at day 14 (`P.outcome.kpi_non_completion_by_year`). Run-grouped tuning inside
  2013 has at most 9 groups.
- **Why it matters.** AQ3 (generalisation claim "later run of the same modules" does not hold for CCC; unstable
  tuning), AQ4 (list quality in CCC is an extrapolation).
- **Recommendation.** Keep the paired/unpaired split of results (already planned) and state that CCC is a new-module
  test; use leave-one-run-out folds in 2013 and report fold variance; keep the hyperparameter grid small given 9
  groups.
- **Severity.** Medium.

## 6. Duplicate-row share varies threefold by run, so raw click features may shift between years

- **Issue.** Exact duplicates make up 3.82% to 11.73% of rows per run (`P.duplicates.studentVle_extra_share_by_run_range`);
  the primary click features keep every row and a `_dedup` twin is built (DQ01, DM "Duplicate / key issue"). Whether
  the share differs between 2013 and 2014 is not verifiable from these files. If it does, raw-click features carry a
  logging artefact across the time split; offering both variants also invites choosing after seeing test results.
- **Why it matters.** AQ3 (distribution shift between training and test), AQ2 (activity-against-average sign).
- **Recommendation.** Tabulate the duplicate share by run and year; pre-declare that the choice between raw and
  `_dedup` is made on 2013 folds only and recorded before any 2014 evaluation; consider `activity_ratio_run` on the
  de-duplicated counts, which normalises run-level artefacts.
- **Severity.** Medium.

## 7. `cma_score_mean_c` will be almost empty at day 13 and its filling rule is unspecified

- **Issue.** The feature uses CMAs submitted on or before c − 7 (FS), i.e. by day 6 at day 13; the earliest non-exam
  due day ranges from 12 to 61 across runs (`P.temporal.first_non_exam_due_day_range`), so few CMA marks exist at
  day 13. The "marks appear within 7 days" assumption is not verifiable from these files. FS says "null if none",
  while DM fits median filling only for registration lead; how this null is encoded is not stated.
- **Why it matters.** AQ3: a median-filled score would treat "no CMA yet" as "average mark", and a mostly-null
  feature adds noise.
- **Recommendation.** Report the feature's coverage per cut-off; pair it with `cma_submitted_c` (count) and a
  missing indicator rather than filling; drop it from the day-13 set if coverage is below a pre-set level.
- **Severity.** Medium.

## 8. Features computable at the cut-off are missing

- **Issue.** The feature set (FS) counts clicks, days, sites and due tasks but omits signals available from the same
  fields before c:
  - recency: days since the last click before c, and day of the first click (studentVle.date);
  - activity by resource type: `vle.activity_type` exists (`P.duplicates.chance_test_two_row_groups.observed_by_activity_type_top6`
    lists forumng, oucontent, quiz, ouwiki, questionnaire, oucollaborate), e.g. forum and quiz clicks to c;
  - submissions of tasks not yet due by c and days submitted before the due day (studentAssessment.date_submitted);
  - trend: change between the last two weeks before c;
  - a fixed pre-start window (e.g. days −14 to −1) instead of `clicks_pre`, whose open window grows with
    `registration_lead`.
- **Why it matters.** AQ3, especially at day 13, where a task is due in 1 of 22 runs (`P.temporal.tasks_due_by_cutoff.d13`)
  and early submissions are the only assessment signal; AQ2 "activity against the course average" by resource type.
- **Recommendation.** Add these to `feature-spec.md` with window rules, include them in V13 (max event day ≤ c), and
  test them in Milestone 4 as a pre-declared extended set.
- **Severity.** Medium.

## 9. Several click features are exact linear copies of each other

- **Issue.** At c = 13, `clicks_last7` (days 7–13) equals `clicks_w2` (week 2 = days 7–13), and `clicks_0c` equals
  `clicks_w1 + clicks_w2`; at c = 27, `clicks_last7` equals `clicks_w4` and `clicks_0c` equals the sum of weeks 1–4;
  `inactive_last7` is the indicator of the last week being zero (FS definitions).
- **Why it matters.** AQ3 (perfect collinearity in logistic models; split importance across copies in SHAP), AQ2
  (association of a "sign" that is the same variable twice).
- **Recommendation.** Keep the weekly series or the totals, not both, in linear models; define `clicks_last7` only
  where it differs from a week boundary or drop it; document which column the early-sign rule uses.
- **Severity.** Low.

## 10. CMA lateness has an undocumented meaning but drives the late-task sign and the rule

- **Issue.** 32,991 of 69,956 CMA submissions are late (47.2%, derived) against 16,320 of 97,088 TMA (16.8%, derived)
  (`P.validity.late_by_type`). DQ10 states that the meaning of a late CMA in 2013–2014 is not documented, yet
  `tasks_late_c` and the early-sign rule (FS) count CMA and TMA lateness together.
- **Why it matters.** AQ2 (a sign half of all CMA submitters show is weak and may reflect a submission window, not
  disengagement), AQ3 rule baseline (rule may fire for a large share of the list population).
- **Recommendation.** Use TMA lateness in the rule by default and run CMA lateness as a sensitivity; report the
  share of enrolments the rule flags per run under both versions on 2013 runs.
- **Severity.** Medium.

## 11. Small population groups and the "Missing" deprivation group need explicit treatment

- **Issue.** The 93 Withdrawn without an unregistration day (`P.validity.withdrawn_without_day`) and the 45 with an
  unknown registration day (`P.missing.date_registration`) stay in every cut-off population (DQ04, DQ05), although
  some may have left before c; they add up to 138 at most (derived), so the effect on rates is small but one-directional.
  Separately, imd_band "Missing" (1,111, 3.41%; `P.missing.by_column.studentInfo.imd_band`) is concentrated in North
  Region (40.1%) and Ireland (22.5%) (`P.missing.imd_band_by_region_top3`) with 65.7% success against 46.6%
  (`P.missing.imd_band_success_missing_vs_present`).
- **Why it matters.** KPI and AQ3 denominators (small upward bias in non-completion); AQ4 fairness check by
  deprivation band, where "Missing" is a regional group, not a deprivation level.
- **Recommendation.** Report KPI and list metrics with and without the 138; in the fairness audit, show "Missing"
  as its own row with its region mix and never pool it with a band.
- **Severity.** Low.

## 12. Some preparation steps follow habit rather than an AQ or the chosen models

- **Issue.** imd_band, age_band and highest_education are stored as ordered categories (DM "Invalid category"), then
  one-hot encoded in `fit_transforms.py` (DM "Encoding / scaling"), which discards the order; log1p and
  standardisation are applied to all model-ready matrices, which tree models do not need; `activity_ratio_run`
  divides by a run median whose value can be zero (not verifiable from these files); DQ15 logging-gap handling
  concerns days after both cut-offs and no AQ (DQ15).
- **Why it matters.** AQ3: transforms not tied to a model choice add parameters to validate (V12) without benefit;
  a zero median makes the AQ2 sign undefined.
- **Recommendation.** Tie each transform to a model family (ordinal or one-hot for linear models, raw for trees);
  add a guard for a zero run median (e.g. ratio to the mean, or to median + 1); keep DQ15 handling only in the
  descriptive `student_week` view.
- **Severity.** Low.

## Summary by severity

| Severity | Critiques |
| :---- | :---- |
| High | 1, 2, 3 |
| Medium | 4, 5, 6, 7, 8, 10 |
| Low | 9, 11, 12 |
