## Appendix V – AI Decision Log and Prompts

Table A.16 is the AI Decision Log of deliverable F, one row per significant AI suggestion with our decision and the evidence used to verify it.

**Table A.16. AI Decision Log**

| # | Role (brief 14) | AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A1 | Data dictionary interpreter | A CMA score appears within 7 days and a CMA cannot be submitted late [3] | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day (profile.json) | `cma_score_mean_c` uses marks submitted ≤ c − 7; late counts split by TMA and CMA |
| A2 | Data dictionary interpreter | The English IMD covers England only; other UK nations use their own indices [5], [6] | Keep imd_band as recorded, "Missing" as its own group, no pooling claims across nations | Accepted | imd_band missing for 40.1% of North Region, 22.5% of Ireland (profile.json) | imd_band is an audit column; fairness rows keep "Missing" apart |
| A3 | EDA / quality checklist partner | Test whether exact duplicate click rows are copies or separate records | Run a chance test on two-row groups | Accepted | 31.5% equal against 24.0% expected; below chance for quizzes (profile.json) | All rows kept, de-duplicated twin built |
| A4 | Preparation critic | Precision ≥ 50% is near the base rate; measure lift and attainable recall | Re-express the AQ4 limit (C13) | Accepted | 45.3% and 44.2% non-completion at the cut-offs | Capacity view; Milestone 4 metric plan |
| A5 | Preparation critic | Target-derived flags could reach the predictors | Role `target_derived`, kept out of feature views | Accepted | Flags defined from final_result | V14 and V13 forbid them |
| A6 | Preparation critic | CMA lateness of unclear meaning drives the rule | Rule uses TMA lateness; CMA variant kept | Accepted | 47.2% of CMA vs 16.8% of TMA submissions late | `early_sign_rule`, `early_sign_rule_cma` (C10) |
| A7 | Feature engineering ideator | Recency, trend, pre-start window, clicks by resource type, early submissions; first-click day | Add all but first-click day as an extended set | Accepted in part | Pre-start clicks already carried by `clicks_pre`, `clicks_pre14` | 10 extended predictors |
| A8 | Preparation critic | Report the outcome rate of test enrolments of students seen in 2013 before modelling | Report only their count now | Accepted in part | Looking at test outcomes while preparing breaks the independent test (brief section 11) | 1,962 flagged, outcome left to Milestone 4 |
| A9 | Preparation critic (leakage audit) | 93 Withdrawn without a day sit in the test views as easy positives | Evaluation flag; metrics with and without | Accepted | 89 of 92 at day 13 are test rows; 41% have no early click | `eval_withdrawal_day_unknown` |
| A10 | Preparation critic (leakage audit) | Tasks due before registration counted as missed; V13 could not fail; a V14 line commented out | Fix the formula and both checks | Accepted | 6 tasks at day 27; code reading | Pipeline rerun: 22 of 22 checks PASS |
| A11 | Code assistant | Draft every script of the package (understanding, profile, preparation, transforms, validation, notebooks) | Keep after review, tests and independent recounts | Accepted | 13 of 13 numbers equal a separate recount by the exploration code; 9 fixture tests; 6 features recomputed from raw for every row, 0 mismatches; one row recounted by hand from the raw files | Package `src/`, `tests/` |
| A12 | Documentation assistant | Draft the dictionary, lineage, README and transformation log | Generated from code and checked | Accepted | V14: every prepared column documented with role and source | `data_dictionary.md`, `lineage.md` |
| A13 | Synthetic-data assistant | Small invented enrolments to test the formulas | Level A fixtures only, labelled, never in a view or a finding | Accepted | Brief section 8.3, level A | `tests/test_features.py` |

The preparation critic received the following instruction and read only the issue log, the matrix, the specifications, the fit log and the profile. In both instructions, files are named by their place in the Prepared Data Package.

> You are a critical reviewer of a data preparation plan for an education analytics project (course completion and
> early warning on the Open University Learning Analytics Dataset, OULAD). Read only these files:
> `data/metadata/quality_issue_log.md`,
> `data/metadata/decision_matrix.md`, `feature_spec.md`, `split_spec.md`,
> the AQ–Data Fit Decision Log (Section 4) and, for numbers, `data/metadata/profile.json`.
> Challenge the plan as a sceptical senior analyst would: (1) imputation, de-duplication, outlier and encoding
> choices; (2) any feature that could leak information from after its cut-off or from the test runs; (3) the split
> and the handling of students seen in both years; (4) the population rules and denominators; (5) whether any
> decision is cleaning by habit rather than tied to an analytical question; (6) features that are missing but
> computable from the real fields at the cut-off. Do not invent facts about the data: cite the file and key for
> every number you use, and say "not verifiable from these files" otherwise. Return at most 12 numbered critiques,
> each with: the issue, why it matters (which AQ), a concrete recommendation, and severity (high / medium / low).

Table A.17 records the decision on each of its 12 critiques.

**Table A.17. Decisions on the preparation critic's critiques**

| # | Critique (short) | Decision | Evidence used to verify | Effect on the pipeline |
| :---- | :---- | :---- | :---- | :---- |
| 1 | AQ4 precision ≥ 50% sits near the base rate (45.3% at day 13, 44.2% at day 27; 24.9–58.3% by run) | Accepted | P.outcome; capacity lists of 3 or 5 per group of 20 cap recall | AQ4 and AQ3 list quality measured as lift over the run's base rate and as recall against the most a list of that size can reach, with a random list and the early-sign rule as baselines (Change Log C13); `capacity_by_run` carries the list sizes |
| 2 | Target-derived flags and `registration_missing` could reach the predictors | Accepted | `withdrawal_day_missing` and `unregistered_not_withdrawn` are functions of final_result; 39 of 45 missing registration days are Withdrawn (P.missing) | The two flags exist only in `enrolment` with role `target_derived`; `registration_missing` moved to the extended set; V14 fails if a target-derived column appears in a feature view |
| 3 | The rule is an inactivity rule at day 13 | Accepted | A task is due by day 13 in 1 of 22 runs (P.temporal) | Rule components stored (`rule_missed`, `rule_tma_late`, `inactive_last7`); firing rate of each component per run and cut-off in the validation summary; the day-13 rule is named an activity rule |
| 4 | Repeat and concurrent students are dependent units | Accepted in part | `student_in_training_runs` and `concurrent_runs` exist in the views | Count of flagged test enrolments reported (no test outcome is inspected, so the requested outcome rate of this group is not computed now); Milestone 4 protocol: folds grouped by run and student inside 2013, bootstrap intervals clustered by student; lists are drawn per module run, so a student in two modules can appear on two tutors' lists |
| 5 | CCC unseen in training; 9 tuning groups | Accepted | `paired_run` = false for CCC-B, CCC-J, EEE-B, GGG-B | Reported as a new-module test; leave-one-run-out folds inside 2013 with fold variance (Milestone 4) |
| 6 | Duplicate share may shift between years | Accepted | Extra-row share 6.82% in 2013 runs, 7.87% in 2014 runs (P.duplicates) | Raw clicks are the declared primary measure; the `_dedup` twin is a sensitivity variant chosen, if at all, on 2013 folds before any 2014 evaluation; the run-relative ratio absorbs run-level differences |
| 7 | CMA score almost empty at day 13; filling unspecified | Accepted | Earliest task due on days 12–61 by run (P.temporal) | `cma_marked_c` (count of marks known) added; the score stays null without filling; its coverage per cut-off is reported; Milestone 4 uses it only if at least 10% of training rows carry it |
| 8 | Computable features missing | Accepted in part | Fields exist before the cut-off | Added as an extended set: recency (`days_since_last_click`), trend (`trend_last_week`), fixed pre-start window (`clicks_pre14`), clicks by the four busiest resource types, tasks submitted before their due day; the day of first click was not added, because `clicks_pre` and `clicks_pre14` already carry pre-start engagement |
| 9 | Linear copies among click features | Accepted | At both cut-offs the last seven days are the last calendar week | `clicks_last7` kept only as the source of `inactive_last7`, not as a predictor; the dictionary states that `clicks_0c` = sum of the weekly columns, so linear models use one or the other |
| 10 | CMA lateness has no documented meaning | Accepted | 32,991 of 69,956 CMA submissions after the due day against 16,320 of 97,088 TMA (P.validity) | Early-sign rule = a task missed, or a TMA late, or no activity in the last seven days; `early_sign_rule_cma` adds CMA lateness as a sensitivity variant; Change Log C10 restated |
| 11 | Small groups and imd "Missing" | Accepted in part | 93 + 45 enrolments flagged; imd "Missing" concentrated in two regions | KPI reported with and without the 138 flagged enrolments in the validation summary; "Missing" is its own row in the fairness audit; no exclusion |
| 12 | Habit transforms and zero median | Accepted | Ordered categories would be lost by one-hot encoding | Run-relative ratio is (clicks + 1) ÷ (run median + 1); model-ready matrices are for linear models only: ordered categories as ordinal codes with a missing indicator, nominal ones one-hot, counts log1p then standardised; tree models use the prepared views; the logging-gap flag stays in `student_week` only |

The leakage auditor received the following instruction and could query the prepared and raw files without changing them.

> You are an independent auditor of data leakage in a preparation pipeline for early prediction of course
> non-completion on OULAD (prediction points: end of day 13 and end of day 27 of each module run; training runs 2013,
> test runs 2014). Read `src/prepare_data.py`, `fit_transforms.py`, `validate_prepared.py`,
> `dictionary.py`, `common.py` and `data/metadata/feature_spec.md`, `split_spec.md`,
> `decision_matrix.md`. You may run read-only Python with Python (polars) on
> `data/processed/*.parquet` and `data/raw/*.csv`, writing
> nothing except your report. Look for: (1) any feature that uses information dated after its cut-off or derived from
> the outcome; (2) any population rule that uses future information (who is in a cut-off view); (3) any statistic
> computed across runs or with test rows that a model would learn from; (4) train–test contamination in
> fit_transforms.py; (5) identifiers or columns that could act as a proxy for the target; (6) bugs in the feature
> formulas (off-by-one days or weeks, banked results, exams, duplicates). For every finding give the file and line
> or the query and its result, the risk, and a fix, with severity (high / medium / low). Do not report a finding you
> could not support with code or a query result. At most 10 findings.

Table A.18 records the evidence and the effect of each of its 8 findings, all of which were accepted.

**Table A.18. Decisions on the leakage auditor's findings**

| # | Finding (severity) | Evidence used to verify | Effect on the pipeline |
| :---- | :---- | :---- | :---- |
| F1 | 93 Withdrawn enrolments without a withdrawal day stay in both cut-off views as positives, 89 of the 92 at day 13 in test runs (medium) | `eval_withdrawal_day_unknown` counts 92 (day 13) and 93 (day 27), 89 and 90 in test runs | Evaluation flag added to the feature views (role evaluation, never a predictor); Milestone 4 reports test metrics with and without these rows |
| F2 | Feature views hold id_student, final_result and non_completion, and tree models were told to use the views as they are (medium) | Columns listed in the view schema | `predictor_sets.json` names the only model inputs for every model family; `fit_transforms.py` docstring corrected |
| F3 | Missing indicator of registration_lead duplicates the extended flag registration_missing in the primary matrix (low) | 5 training rows, all non-completers | No indicator for registration_lead; the flag stays an extended predictor |
| F4 | Existence of a missing indicator was decided with test rows (low) | `fit()` read df instead of the training rows | Indicators decided on training rows; training medians computed for every numeric column |
| F5 | Tasks due before a late registrant's registration counted as missed at day 27 (low) | 6 such tasks at day 27 | A task counts only if due on or after the registration day; validator recount and fixture test changed accordingly |
| F6 | No-click students received the training median (1 day) for days_since_last_click (low) | Median 1.0 in `transform_params.json` | Value c + 1 for students with no click in days 0…c, set in the view |
| F7 | V13 could never fail, because the data were filtered before the check (low) | Code reading | V13 recounts clicks without any cut-off and requires the pipeline to differ exactly where later clicks exist (26,755 and 25,663 rows) |
| F8 | V14 check of extended predictors was commented out by a misplaced comment (low) | `validate_prepared.py` line 170 | Line split; V14 checks both predictor lists |

**Rules shaped by the reviews.** The reviews shaped four rules that the pipeline applies. The AQ4 list is judged by its gain over chance,
because a precision limit of 50% sits close to the base rate (C13). CMA lateness, seen in 47.2% of CMA submissions
against 16.8% of TMA submissions, stays out of the early-sign rule (C10). A task counts as missed only if it falls
due on or after the student's registration day, the auditor having pointed to six tasks at day 27 that fell due before
the student registered. And the leakage check is built so that it can fail, as the auditor required.

The fourth of the critic's twelve critiques was accepted only in part, because of a rule we keep. The critic asked for the outcome rate of the test enrolments of
students seen in 2013 to be reported before modelling. We report their number, 1,962, but not their outcomes, because looking
at test outcomes while preparing the data would make the test set part of the preparation, which the brief rules out
[1].

**Further decisions and reflection.**

The interpreter's suggestion on the OU policy of 2025 was also accepted in part: its reading of the 2025 policy gave a usable rule for
CMA marks, which appear within seven days, but its rule that a CMA cannot be submitted late does not hold in data
where 32,991 CMA submissions are late, so it was not applied.

**Reflection.** The reviews were most useful where the AI critic had to argue from the data rather than from general
advice: the duplicate test, the base-rate argument and the registration-day error each changed the pipeline, and each
was confirmed by a count before it was accepted.

**AI roles and verification.** The table below gives each of the seven roles, what AI did in it and how the result was
verified.

| Role (brief) | What AI did | How the result was verified |
| :---- | :---- | :---- |
| Data dictionary interpreter | Read the data descriptor, the OU's assessment policy and the IMD documentation | Each fact kept only with a verbatim quotation; the 2025 rule that a CMA cannot be late tested on the data and not applied |
| EDA and quality checklist partner | Proposed a test of whether duplicate click rows are copies | Test run on the data: 31.5% equal counts against 24.0% by chance |
| Code assistant | Drafted every script of the package | 13 figures equal to an independent recount; 9 unit tests; 6 features recomputed for every row without a difference; one row recounted by hand |
| Preparation critic | Reviewed the plan in isolation (12 critiques) and audited leakage (8 findings) | Each critique checked on the data or the code before a decision |
| Feature engineering ideator | Proposed recency, trend, a pre-start window, clicks by resource type and early submissions | Each feature computable from real fields before the cut-off; added as the extended set |
| Documentation assistant | Drafted the dictionary, lineage, package guide and transformation log | Generated from the code; V14 fails if a column lacks an entry |
| Synthetic-data assistant | Wrote small labelled test enrolments | Level A of the brief's policy only; never in a view or a finding |
