---
id: S105
url: reports/milestone-3/package/README.md
requested: reports/milestone-3/package/README.md reports/milestone-3/package/data/metadata/ai_decision_log.md reports/milestone-3/package/data/metadata/change_log.md reports/milestone-3/package/data/metadata/data_dictionary.md reports/milestone-3/package/data/metadata/decision_matrix.md reports/milestone-3/package/data/metadata/feature_spec.md reports/milestone-3/package/data/metadata/lineage.md reports/milestone-3/package/data/metadata/predictor_sets.json reports/milestone-3/package/data/metadata/quality_issue_log.md reports/milestone-3/package/data/metadata/split_spec.md reports/milestone-3/package/data/metadata/traceability.md reports/milestone-3/package/data/metadata/transform_params.json reports/milestone-3/package/data/metadata/transformation_log.md reports/milestone-3/package/data/metadata/understanding_map.md reports/milestone-3/package/data/metadata/validation_summary.json reports/milestone-3/package/data/metadata/validation_summary.md reports/milestone-3/package/data/metadata/version_manifest.json
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 17 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T06
part: 1
raw: raw.txt (110 KB)
conversion: verbatim copy of 17 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-3/package/README.md @ 19d35a4 =====
# Prepared Data Package – Milestone 3 (team N04)

The pipeline, prepared data and metadata that turn the raw Open University Learning Analytics Dataset (OULAD) into
analytic-ready views for Milestone 4 (brief section 16, deliverables C and D, with B, E and F in `data/metadata/`).
Prepared dataset version: `OULAD-N04-prepared-1.0` (`data/metadata/version_manifest.json`).

```
package/
  README.md
  requirements.txt
  data/
    raw/         the seven OULAD CSV tables, read-only, checked against the SHA-256 in metadata/raw_pins.csv
    interim/     clicks by enrolment and day, resources by enrolment and day (rebuilt)
    processed/   analytic-ready views (rebuilt): enrolment, assessment_due, student_week, features_d13,
                 features_d27, capacity_by_run, model_ready_d13, model_ready_d27 (Parquet)
    metadata/    understanding map, profile, quality issue log, decision matrix, feature and split specifications,
                 transformation log, transform parameters, predictor sets, data dictionary, lineage, validation
                 summary, version manifest, traceability (B), change log (E), AI decision log (F)
  notebooks/     02_data_understanding.ipynb, 03_data_preparation.ipynb (executed)
  src/           link_raw, 01_understand, 02_profile, prepare_data, fit_transforms, validate_prepared,
                 build_notebooks, common, dictionary; run_all.sh
  tests/         formula tests on labelled synthetic fixtures (brief section 8.3, level A)
  logs/          one log per step of the last run_all.sh (UTC time, command, output, exit status)
```

## Rebuild from raw

Run from this folder, with Python 3.12 or later:

```bash
python -m pip install -r requirements.txt
bash src/run_all.sh          # steps 00-07, about 15 seconds once the raw files are in place
```

Step 00 uses the raw files in `data/raw/` when they are present. Otherwise it downloads the OULAD archive from the
figshare deposit cited by the data descriptor (DOI 10.6084/m9.figshare.5081998.v1, 46.8 MB) and extracts the seven
tables. Every table is checked against the SHA-256 in `data/metadata/raw_pins.csv` before any step reads it.
`run_all.sh` uses `python3`, or the interpreter named in the `PYTHON` environment variable, and stops at the first
failing step. Two runs from raw write identical files: the SHA-256 of all eight views is equal across runs. The
hashes, row counts and code hashes of the prepared files are in `data/metadata/version_manifest.json`.

## Steps

| Step | Script | Brief | Output |
| :---- | :---- | :---- | :---- |
| 00 | `link_raw.py` | section 3 (raw immutable) | `metadata/raw_check.csv` |
| 01 | `01_understand.py` | Task 1 | `metadata/understanding_map.md`, `understanding.json` |
| 02 | `02_profile.py` | Task 2 | `metadata/profile.json`, `profile_crosscheck.csv`, figure data |
| 03 | `python -m unittest` on `tests/` | Task 8 (formula check) | `logs/03_tests.log` |
| 04 | `prepare_data.py` | Tasks 5–6 | `processed/*.parquet`, `metadata/transformation_log.md` |
| 05 | `fit_transforms.py` | Task 6 | `processed/model_ready_*.parquet`, `metadata/transform_params.json`, `predictor_sets.json` |
| 06 | `validate_prepared.py` | Task 8 | `metadata/validation_summary.md`, `data_dictionary.md`, `lineage.md`, `version_manifest.json` |
| 07 | `build_notebooks.py` | section 10.1 | `notebooks/*.ipynb` |

## Using the views in Milestone 4

- Model inputs are only the columns listed in `metadata/predictor_sets.json`; identifier, split, evaluation, target,
  rule and audit columns are never inputs.
- Train on `split = train` (2013 runs), test on `split = test` (2014 runs); tune with leave-one-run-out folds inside
  2013 that keep each student in one fold. Report test results for paired and unpaired runs separately, and with
  and without `eval_withdrawal_day_unknown` and `student_in_training_runs`.
- `early_sign_rule` is the comparison rule (C10); `capacity_by_run` gives the list sizes of the AQ4 scenarios.

License of the data: CC BY 4.0; cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171.

===== reports/milestone-3/package/data/metadata/ai_decision_log.md @ 19d35a4 =====
# AI Decision Log (deliverable F, brief section 14.1)

Generative AI agents worked for the team in all seven roles the brief allows; team members verify every decision.
No AI answer served as evidence about the data: every accepted suggestion was checked by code, a recount on the raw
files, documentation or a test. Full prompts, outputs and per-item decisions: `preparation-critic-prompt.md`,
`preparation-critic.md`, `preparation-critic-decisions.md`, `leakage-auditor-prompt.md`, `leakage-auditor.md`,
`leakage-auditor-decisions.md`; research prompts in `PROGRESS.md` (T05, T06) and the research trail.

| # | Role (brief 14) | AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A1 | Data dictionary interpreter | A CMA score appears within 7 days and a CMA cannot be submitted late (OU TMA and iCMA policy, The Open University, 2025) | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day (profile.json) | `cma_score_mean_c` uses marks submitted ≤ c − 7; late counts split by TMA and CMA |
| A2 | Data dictionary interpreter | The English IMD covers England only; other UK nations use their own indices (DCLG, 2015; Abel et al., 2016) | Keep imd_band as recorded, "Missing" as its own group, no pooling claims across nations | Accepted | imd_band missing for 40.1% of North Region, 22.5% of Ireland (profile.json) | imd_band is an audit column; fairness rows keep "Missing" apart |
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

===== reports/milestone-3/package/data/metadata/change_log.md @ 19d35a4 =====
# Controlled Change Log (deliverable E)

C01–C08 come from Milestone 2 (copied verbatim, `research/baseline/m3-baseline.md`); C09–C13 are caused by the data understanding of Milestone 3 (`research/fit/aq-data-fit.md`, evidence in `quality_issue_log.md` and `profile.json`). None changes the Business Goal or the decisions D1–D3.

| ID | Milestone | Old content | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C01 | 2 | The program's online and blended courses at a Vietnamese university | OULAD module runs (UK Open University, distance learning, 2013–2014) as an open stand-in for the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses was found; OULAD is the only candidate passing the gates | All AQs answered on stand-in data; results describe OULAD and must be re-checked on the university's data before D1–D3 |
| C02 | 2 | Course and semester; weeks 1–5 of a semester (length not fixed in Milestone 1) | Module run (`code_presentation`), eight to nine months; days counted from day 0 of the run; week n = days 7(n−1) to 7n−1 | Dates in OULAD are days from the run start; runs last 234–269 days | Cut-offs become day 13 (week-3 list) and day 27 (week-5 list); the semester-length difference is a stated limit |
| C03 | 2 | Denominator: students enrolled after the add-drop period; withdrawal as in Circular 83/2026 | Enrolments still registered at day 14 (registration closes two weeks after the start); leave and transfer cannot be told apart | `date_registration`, `date_unregistration` exist; no status field for leave or transfer | Primary KPI computed as a proxy on 28,119 enrolments; deviation from the Circular 83 rule recorded |
| C04 | 2 | Comparisons by delivery mode and year of study; AQ4 limit on first-year against later-year recall | Comparisons by module and run; the fairness limit is checked across IMD band and disability | No delivery-mode or year-of-study field; all modules are distance learning | AQ1–AQ3 narrowed; AQ4 limit re-expressed on available groups |
| C05 | 2 | AQ2 sign: attendance at in-class sessions (blended courses) | Dropped | No in-class sessions or attendance in OULAD | AQ2 uses missed and late tasks, activity and concurrent runs |
| C06 | 2 | AQ3 week-3 list from assessment and activity signs | Week-3 list (day-13 cut-off) from activity only; assessment signs start with the week-5 list | A non-exam task is due by day 13 in 1 of 22 runs, by day 27 in 16 | Secondary KPI 1: two tasks fall due by day 27 in only 1 of 22 runs, so on OULAD its sign part counts one missed or late task in the 16 runs with a task due by day 27; the two-task rule stays for the university |
| C07 | 2 | AQ3 tested on a later semester of the same pilot courses | Train on 2013 runs, test on 2014 runs of the same module and start month (9 pairs); CCC, EEE-B and GGG-B only as later runs | B and J runs should be analysed separately; each module has at most two runs of one start month | Time-based validation feasible but with one earlier run per pair |
| C08 | 2 | AQ4 action and outcome; secondary KPI 2 and the contact part of secondary KPI 1 measured from a contact record | Kept as a future decision requirement; AQ4 limited to ranking under assumed capacity | No contact, capacity or intervention data in any candidate | No prescriptive or causal claim; secondary KPI 1 (contact part) and secondary KPI 2 measured only in the pilot |
| C09 | 3 | KPI denominator: enrolments still registered at day 14 (28,119; C03) | Enrolled at day d = registered by day d (or registration day unknown) and not unregistered by day d; day 14 for the KPI (28,061), days 13 and 27 for the lists (28,069; 27,535) | 58 enrolments registered after day 14, up to day 167 (DQ05) | Primary KPI recomputed on 28,061 enrolments; same rule for every population |
| C10 | 3 | AQ3 comparison rule and secondary KPI 1 early-sign rule: two or more assessed tasks missed or late by week 4 (Milestone 1); on OULAD one missed or late task, in the 16 runs with a task due by day 27 (C06) | Early-sign rule: at least one TMA or CMA due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; CMA lateness only in a sensitivity variant | Two or more tasks are due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1 (DQ18), so a rule on tasks alone cannot fire in 6 runs at day 27 or in 21 at day 13; the meaning of a late CMA in 2013–2014 is undocumented (DQ10) | The rule can fire in every run; secondary KPI 1 (sign part) uses the same rule |
| C11 | 3 | AQ4: whom to list, in what order and with which contact, within capacity | AQ4 (rewritten): ranking under an assumed capacity with recall and precision overall and by deprivation band and disability; the choice of contact and its effect deferred to the pilot | No contact, capacity or outcome-after-contact data (C08; AQ4 RED) | No prescriptive claim; D1 receives an ordered list and its measured quality, not a contact plan |
| C12 | 3 | AQ2 sign "tasks missed in several modules at once", all runs | Described for 2014 runs only; not a predictor in AQ3 | Of 1,382 concurrent enrolments at day 14, 12 fall in 2013 runs (training runs) | AQ2 narrowed; AQ3 feature set excludes it |
| C13 | 3 | AQ4 list limit: precision of at least 50% | List quality measured as lift over the run's base rate and as recall against the most a list of the same size can reach, with a random list and the early-sign rule as baselines | Non-completion is 45.3% at day 13 and 44.2% at day 27, and 24.9–58.3% by run, so a random list already reaches about 45% precision; lists of 3 or 5 per 20 students cap recall | AQ4 limit re-expressed; D1 judges a list by its gain over chance |

===== reports/milestone-3/package/data/metadata/data_dictionary.md @ 19d35a4 =====
# Prepared data dictionary
Written by `src/validate_prepared.py` at 2026-11-06T15:24:17Z from the prepared files and `src/dictionary.py`. Roles: id, split, target, target_derived, predictor, predictor_extended, rule, audit, descriptive. Day fields are offsets from the start of the module run (day 0); week n = days 7(n−1) to 7n−1.

## enrolment.parquet
one row per enrolment (all 32,593); descriptive and diagnostic base. Rows: 32,593; columns: 39.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| id_student | Int64 | id | studentInfo.id_student | as recorded (randomised by the provider) | quasi-identifier |
| gender | String | audit | studentInfo.gender | as recorded | sensitive |
| region | String | audit | studentInfo.region | as recorded | sensitive |
| highest_education | String | predictor | studentInfo.highest_education | ordered; ordinal code in model_ready | sensitive |
| imd_band | String | audit | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | sensitive |
| age_band | String | audit | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | sensitive |
| num_of_prev_attempts | Int64 | predictor | studentInfo.num_of_prev_attempts | as recorded | none |
| studied_credits | Int64 | predictor | studentInfo.studied_credits | as recorded; outliers kept | none |
| disability | String | audit | studentInfo.disability | as recorded (Y/N) | sensitive |
| final_result | String | target | studentInfo.final_result | as recorded | none |
| date_registration | Int64 | descriptive | studentRegistration.date_registration | as recorded | none |
| date_unregistration | Int64 | descriptive | studentRegistration.date_unregistration | as recorded | none |
| enrolled_d13 | Boolean | descriptive | registration days | enrolled_at(13) | none |
| enrolled_d14 | Boolean | descriptive | registration days | enrolled_at(14) | none |
| enrolled_d27 | Boolean | descriptive | registration days | enrolled_at(27) | none |
| year | Int64 | split | code_presentation | first four characters | none |
| start_month | String | predictor | code_presentation | last character: B = February, J = October | none |
| run_length | Int64 | descriptive | courses.module_presentation_length | renamed | none |
| completed | Boolean | target | studentInfo.final_result | Pass or Distinction | none |
| non_completion | Boolean | target | studentInfo.final_result | Fail or Withdrawn | none |
| split | String | split | code_presentation | train if 2013, test if 2014 | none |
| registration_missing | Boolean | predictor_extended | studentRegistration.date_registration | registration day missing | none |
| withdrawal_day_missing | Boolean | target_derived | final_result, date_unregistration | Withdrawn without a day | none |
| unregistered_not_withdrawn | Boolean | target_derived | final_result, date_unregistration | not Withdrawn but a day recorded | none |
| unregistered_after_run_end | Boolean | descriptive | date_unregistration, courses | day after run length | none |
| registration_lead | Int64 | predictor | studentRegistration.date_registration | −date_registration | none |
| banked_results | UInt32 | predictor | studentAssessment.is_banked | count of banked results | none |
| concurrent_runs | UInt32 | descriptive | studentInfo | other enrolments of the student in the same presentation | none |
| student_in_training_runs | Boolean | split | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | none |
| paired_run | Boolean | split | courses | module and start month ran in both years | none |
| first_missed_week | Int64 | descriptive | assessment_due | week of earliest TMA/CMA not submitted and due while enrolled | none |
| tasks_due_while_enrolled | UInt32 | descriptive | assessment_due | count, banked excluded | none |
| tasks_missed_while_enrolled | UInt32 | descriptive | assessment_due | count not submitted | none |
| tasks_late_while_enrolled | UInt32 | descriptive | assessment_due | count submitted after the due day | none |
| total_clicks | Int64 | descriptive | studentVle.sum_click | sum of all rows | none |
| total_clicks_dedup | Int64 | descriptive | studentVle.sum_click | sum with exact duplicate rows once | none |
| active_days | UInt32 | descriptive | studentVle.date | distinct days with a click | none |

## assessment_due.parquet
one row per enrolment and TMA/CMA of its run. Rows: 286,898; columns: 14.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| id_student | Int64 | id | studentInfo.id_student | as recorded (randomised by the provider) | quasi-identifier |
| id_assessment | Int64 | id | assessments.id_assessment | as recorded | none |
| assessment_type | String | descriptive | assessments.assessment_type | TMA or CMA (exams excluded) | none |
| due_day | Int64 | descriptive | assessments.date | renamed | none |
| weight | Float64 | descriptive | assessments.weight | as recorded; not used for grades | none |
| date_submitted | Int64 | descriptive | studentAssessment.date_submitted | as recorded; null if not submitted | none |
| is_banked | Int64 | descriptive | studentAssessment.is_banked | as recorded | none |
| score | Float64 | descriptive | studentAssessment.score | as recorded; not a feature except via cma_score_mean_c | none |
| status | String | descriptive | date_submitted, due day, is_banked | banked / not_submitted / on_time / late | none |
| lateness_days | Int64 | descriptive | date_submitted, due day | submitted − due (non-banked) | none |
| due_while_enrolled | Boolean | descriptive | due day, registration days | registered by due day and unregistered after it | none |
| due_week | Int64 | descriptive | assessments.date | floor(due / 7) + 1 | none |

## student_week.parquet
one row per enrolment and week, weeks −3 to the run end, cut after the withdrawal week. Rows: 1,052,344; columns: 10.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| id_student | Int64 | id | studentInfo.id_student | as recorded (randomised by the provider) | quasi-identifier |
| week | Int64 | id | studentVle.date | floor(date / 7) + 1; week 1 = days 0–6 | none |
| clicks | Int64 | descriptive | studentVle.sum_click | sum per week | none |
| clicks_dedup | Int64 | descriptive | studentVle.sum_click | weekly sum, exact duplicates once | none |
| records | UInt32 | descriptive | studentVle | number of log rows | none |
| active_days | UInt32 | descriptive | studentVle.date | distinct days with a click | none |
| sites | UInt32 | descriptive | studentVle.id_site | distinct resources | none |
| logging_gap | Boolean | descriptive | studentVle.date | week holds a day with no click in the whole run | none |

## features_d13.parquet
one row per enrolment enrolled at day 13; pre-cut-off features only. Rows: 28,069; columns: 50.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| id_student | Int64 | id | studentInfo.id_student | as recorded (randomised by the provider) | quasi-identifier |
| year | Int64 | split | code_presentation | first four characters | none |
| split | String | split | code_presentation | train if 2013, test if 2014 | none |
| paired_run | Boolean | split | courses | module and start month ran in both years | none |
| student_in_training_runs | Boolean | split | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | none |
| eval_withdrawal_day_unknown | Boolean | evaluation | final_result, date_unregistration | Withdrawn without a withdrawal day | none |
| final_result | String | target | studentInfo.final_result | as recorded | none |
| non_completion | Boolean | target | studentInfo.final_result | Fail or Withdrawn | none |
| early_sign_rule | Boolean | rule | derived | rule_missed or rule_tma_late or inactive_last7 | none |
| early_sign_rule_cma | Boolean | rule | derived | early_sign_rule or cma_late_c ≥ 1 | none |
| rule_missed | Boolean | rule | derived | tasks_missed_c ≥ 1 | none |
| rule_tma_late | Boolean | rule | derived | tma_late_c ≥ 1 | none |
| start_month | String | predictor | code_presentation | last character: B = February, J = October | none |
| highest_education | String | predictor | studentInfo.highest_education | ordered; ordinal code in model_ready | sensitive |
| num_of_prev_attempts | Int64 | predictor | studentInfo.num_of_prev_attempts | as recorded | none |
| studied_credits | Int64 | predictor | studentInfo.studied_credits | as recorded; outliers kept | none |
| registration_lead | Int64 | predictor | studentRegistration.date_registration | −date_registration | none |
| banked_results | UInt32 | predictor | studentAssessment.is_banked | count of banked results | none |
| clicks_pre | Int64 | predictor | studentVle.sum_click, date | sum | none |
| clicks_0c | Int64 | predictor | studentVle.sum_click, date | sum (= sum of clicks_w*) | none |
| active_days_0c | UInt32 | predictor | studentVle.date | distinct days with a click | none |
| sites_0c | UInt32 | predictor | studentVle.id_site | distinct resources | none |
| inactive_last7 | Boolean | predictor | studentVle | no click in days c−6 to c | none |
| activity_ratio_run | Float64 | predictor | studentVle | (clicks_0c + 1) ÷ (run median of clicks_0c + 1) | none |
| tasks_due_c | UInt32 | predictor | assessments.date | TMA/CMA due by c and on or after the registration day | none |
| tasks_missed_c | UInt32 | predictor | studentAssessment | due ≤ c, no non-banked submission by c | none |
| tasks_late_c | UInt32 | predictor | studentAssessment | due ≤ c, submitted after due and by c | none |
| tma_late_c | UInt32 | predictor | studentAssessment | late TMA by c | none |
| cma_late_c | UInt32 | predictor | studentAssessment | late CMA by c | none |
| cma_marked_c | UInt32 | predictor | studentAssessment | CMA marks known by c | none |
| cma_score_mean_c | Float64 | predictor | studentAssessment.score | mean of known CMA marks; null if none | none |
| registration_missing | Boolean | predictor_extended | studentRegistration.date_registration | registration day missing | none |
| clicks_0c_dedup | Int64 | predictor_extended | studentVle | sum, exact duplicate rows once | none |
| clicks_pre14 | Int64 | predictor_extended | studentVle.sum_click, date | sum | none |
| days_since_last_click | Int64 | predictor_extended | studentVle.date | c − last active day; c + 1 if no click in 0…c | none |
| trend_last_week | Int64 | predictor_extended | studentVle | last week's clicks − previous week's | none |
| tasks_submitted_early_c | UInt32 | predictor_extended | studentAssessment | tasks due after c submitted by c | none |
| clicks_oucontent_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on content pages | none |
| clicks_forumng_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on forums | none |
| clicks_quiz_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on quizzes | none |
| clicks_homepage_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on the homepage | none |
| gender | String | audit | studentInfo.gender | as recorded | sensitive |
| age_band | String | audit | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | sensitive |
| disability | String | audit | studentInfo.disability | as recorded (Y/N) | sensitive |
| imd_band | String | audit | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | sensitive |
| region | String | audit | studentInfo.region | as recorded | sensitive |
| clicks_w1 | Int64 | predictor_extended | studentVle | sum per week | none |
| clicks_w2 | Int64 | predictor_extended | studentVle | sum per week | none |

## features_d27.parquet
one row per enrolment enrolled at day 27; pre-cut-off features only. Rows: 27,535; columns: 52.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| id_student | Int64 | id | studentInfo.id_student | as recorded (randomised by the provider) | quasi-identifier |
| year | Int64 | split | code_presentation | first four characters | none |
| split | String | split | code_presentation | train if 2013, test if 2014 | none |
| paired_run | Boolean | split | courses | module and start month ran in both years | none |
| student_in_training_runs | Boolean | split | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | none |
| eval_withdrawal_day_unknown | Boolean | evaluation | final_result, date_unregistration | Withdrawn without a withdrawal day | none |
| final_result | String | target | studentInfo.final_result | as recorded | none |
| non_completion | Boolean | target | studentInfo.final_result | Fail or Withdrawn | none |
| early_sign_rule | Boolean | rule | derived | rule_missed or rule_tma_late or inactive_last7 | none |
| early_sign_rule_cma | Boolean | rule | derived | early_sign_rule or cma_late_c ≥ 1 | none |
| rule_missed | Boolean | rule | derived | tasks_missed_c ≥ 1 | none |
| rule_tma_late | Boolean | rule | derived | tma_late_c ≥ 1 | none |
| start_month | String | predictor | code_presentation | last character: B = February, J = October | none |
| highest_education | String | predictor | studentInfo.highest_education | ordered; ordinal code in model_ready | sensitive |
| num_of_prev_attempts | Int64 | predictor | studentInfo.num_of_prev_attempts | as recorded | none |
| studied_credits | Int64 | predictor | studentInfo.studied_credits | as recorded; outliers kept | none |
| registration_lead | Int64 | predictor | studentRegistration.date_registration | −date_registration | none |
| banked_results | UInt32 | predictor | studentAssessment.is_banked | count of banked results | none |
| clicks_pre | Int64 | predictor | studentVle.sum_click, date | sum | none |
| clicks_0c | Int64 | predictor | studentVle.sum_click, date | sum (= sum of clicks_w*) | none |
| active_days_0c | UInt32 | predictor | studentVle.date | distinct days with a click | none |
| sites_0c | UInt32 | predictor | studentVle.id_site | distinct resources | none |
| inactive_last7 | Boolean | predictor | studentVle | no click in days c−6 to c | none |
| activity_ratio_run | Float64 | predictor | studentVle | (clicks_0c + 1) ÷ (run median of clicks_0c + 1) | none |
| tasks_due_c | UInt32 | predictor | assessments.date | TMA/CMA due by c and on or after the registration day | none |
| tasks_missed_c | UInt32 | predictor | studentAssessment | due ≤ c, no non-banked submission by c | none |
| tasks_late_c | UInt32 | predictor | studentAssessment | due ≤ c, submitted after due and by c | none |
| tma_late_c | UInt32 | predictor | studentAssessment | late TMA by c | none |
| cma_late_c | UInt32 | predictor | studentAssessment | late CMA by c | none |
| cma_marked_c | UInt32 | predictor | studentAssessment | CMA marks known by c | none |
| cma_score_mean_c | Float64 | predictor | studentAssessment.score | mean of known CMA marks; null if none | none |
| registration_missing | Boolean | predictor_extended | studentRegistration.date_registration | registration day missing | none |
| clicks_0c_dedup | Int64 | predictor_extended | studentVle | sum, exact duplicate rows once | none |
| clicks_pre14 | Int64 | predictor_extended | studentVle.sum_click, date | sum | none |
| days_since_last_click | Int64 | predictor_extended | studentVle.date | c − last active day; c + 1 if no click in 0…c | none |
| trend_last_week | Int64 | predictor_extended | studentVle | last week's clicks − previous week's | none |
| tasks_submitted_early_c | UInt32 | predictor_extended | studentAssessment | tasks due after c submitted by c | none |
| clicks_oucontent_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on content pages | none |
| clicks_forumng_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on forums | none |
| clicks_quiz_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on quizzes | none |
| clicks_homepage_0c | Int64 | predictor_extended | studentVle, vle.activity_type | sum on the homepage | none |
| gender | String | audit | studentInfo.gender | as recorded | sensitive |
| age_band | String | audit | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | sensitive |
| disability | String | audit | studentInfo.disability | as recorded (Y/N) | sensitive |
| imd_band | String | audit | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | sensitive |
| region | String | audit | studentInfo.region | as recorded | sensitive |
| clicks_w1 | Int64 | predictor_extended | studentVle | sum per week | none |
| clicks_w2 | Int64 | predictor_extended | studentVle | sum per week | none |
| clicks_w3 | Int64 | predictor_extended | studentVle | sum per week | none |
| clicks_w4 | Int64 | predictor_extended | studentVle | sum per week | none |

## capacity_by_run.parquet
one row per run and cut-off; list sizes under assumed capacities. Rows: 44; columns: 9.

| Column | Type | Role | Source | Transformation | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| code_module | String | id | studentInfo.code_module | as recorded | none |
| code_presentation | String | id | studentInfo.code_presentation | as recorded | none |
| cutoff_day | Int64 | id | – | 13 or 27 | none |
| enrolled | Int64 | descriptive | features views | count enrolled at the cut-off | none |
| tutor_groups_est | Int64 | descriptive | enrolled | ceil(enrolled / 20) | none |
| list_tutor_3 | Int64 | descriptive | tutor_groups_est | 3 × groups (≤ enrolled) | none |
| list_tutor_5 | Int64 | descriptive | tutor_groups_est | 5 × groups (≤ enrolled) | none |
| list_office_30 | Int64 | descriptive | enrolled | min(30, enrolled) | none |
| list_office_40 | Int64 | descriptive | enrolled | min(40, enrolled) | none |

## model_ready_d13.parquet, model_ready_d27.parquet
Linear-model matrices from `src/fit_transforms.py`: the identifier, split, target, rule and audit columns of the feature view unchanged, then every predictor and extended predictor encoded with training-run parameters (`transform_params.json`): `code_module=…`, `start_month=…` one-hot; highest_education ordinal 0–4; counts log1p; `<column>_missing` indicators where a training median fills a gap; all standardised with training mean and standard deviation.

===== reports/milestone-3/package/data/metadata/decision_matrix.md @ 19d35a4 =====
# Preparation Decision Matrix (Task 4, brief section 9)

Written before any data is changed. Each row names the issue (DQnn of `package/data/metadata/quality_issue_log.md`),
the decision, its rationale against the analytical questions, the implementation (function of
`package/src/prepare_data.py` unless named otherwise) and the check that validates it
(`package/src/validate_prepared.py`, check ID Vnn). Brief section 9.1 rules apply: no blanket imputation, no blanket
de-duplication, no IQR deletion, no arbitrary merging of categories, no future data in past features, sensitive
attributes kept for audit.

| Issue / need | Decision | Rationale | Implementation | Validation |
| :---- | :---- | :---- | :---- | :---- |
| Population (in-scope records) | Keep all 32,593 enrolments in the enrolment view with flags `enrolled_d13`, `enrolled_d14`, `enrolled_d27`; feature views hold only enrolments enrolled at their cut-off | The KPI counts students enrolled after the add-drop period (C03, C09); a list can only name students enrolled on the day it is drawn | `step2_population`: `enrolled_at(day)` = registered by day (or unknown) and not unregistered by day | V01 row counts 32,593 / 28,061 / 28,069 / 27,535 equal profile.json |
| Missing values (DQ04, DQ11–DQ14) | imd_band → category "Missing"; date_registration → null + `registration_missing`; withdrawal day of 93 Withdrawn → null + `withdrawal_day_missing`; TMA score → null; week_from/week_to not used | Missingness is informative (imd_band missing goes with 65.7% success, concentrated in two regions), small (45, 93, 173) or unused; imputing would invent values the data do not hold | `step5_missing`; filling of registration lead only in `fit_transforms.py`, median of training runs | V02 missing counts after = before for every kept column; V12 transform parameters computed from training rows only |
| Duplicate / key issue (DQ01, DQ02) | Keep every click row; aggregate clicks by enrolment × day (and × week) before any join; build a de-duplicated twin of each click feature (`*_dedup`, exact duplicate rows counted once) | Cause of exact duplicates undecidable: 31.5% equal two-row groups against 24.0% by chance, below chance for quizzes; the grain is the record, not the day; the twin lets Milestone 4 test sensitivity | `step4_keys`: daily aggregation with `records`, `clicks`, `clicks_dedup` | V03 key uniqueness of every view; V04 total clicks = 39,605,099 raw and 38,343,063 de-duplicated |
| Invalid category / type (DQ12, DQ07) | Normalise "10-20" to "10-20%"; ordered categories for imd_band, age_band, highest_education; banked results separated (`status = banked`), never treated as day −1 submissions | Labels must sort and match; day −1 is a placeholder for a carried-over result, not a submission time | `step3_standardise` | V05 every category in its expected set; V06 no banked row in lateness or missed counts |
| Outliers (DQ10, DQ16) | Keep all values: 6,977-click row, 655 credits, submissions up to day 608 | Heavy users, multi-module students and very late submissions are real; capping would change real totals; post-run submissions fall after both cut-offs | No deletion; log1p of counts applied in `fit_transforms.py` for scale-sensitive models | V07 ranges after = before |
| Activity after withdrawal (DQ03) | Truncate engagement measures at the unregistration day in the enrolment, assessment and week views | Activity after leaving is not engagement while enrolled; it would blur AQ1–AQ2 measures | `step6_truncate` | V08 no click or submission counted after the unregistration day |
| Table integration (DQ17, DQ02) | Left joins from the enrolment table; aggregate studentVle and studentAssessment to the target grain first; zero-fill counts | Absence of a row records no activity; inner joins would drop 3,365 enrolments; a naive submissions × clicks join returns 89,347,197 rows | `step7_integrate` with a row-count assertion after every join | V09 rows equal the left table after each join; V10 enrolments without activity kept with 0 |
| Derived features (DQ08, DQ09, DQ18) | Task counts over TMA and CMA only, unweighted; lateness = submission day − due day; missed by the cut-off = due by the cut-off and not submitted by it; score features use CMA marks known by the cut-off (submitted ≤ c − 7), with their count; early-sign rule of C10 (task missed, TMA late or inactive), CMA lateness only in a variant; activity relative to the run's median up to the cut-off, (clicks + 1) ÷ (median + 1); target-derived flags kept out of feature views | Exam scores are missing for 5 modules; weights differ by module; TMA marks have no release day; the rule must fire in every run | `step8_features` (formulas in `feature_spec.md`) | V11 hand-recomputed features for 5 sampled enrolments from raw rows; fixture tests in `package/tests/` |
| Temporal aggregation | Week n = days 7(n−1) to 7n−1 (week 1 = days 0–6, C02); cut-off d13 = end of week 2, d27 = end of week 4; activity before day 0 kept as its own window | The prediction points are fixed in Milestone 2 (C02); pre-start activity is known before teaching and separates outcomes | `step8_features`, `step9_views` (student_week) | V13 no feature uses an event dated after its cut-off |
| Encoding / scaling | Prepared views keep original scales and labels (tree models use them as they are); `fit_transforms.py` builds model-ready matrices for linear models: ordered categories as ordinal codes with a missing indicator, nominal categories one-hot with levels from training runs, counts log1p, median filling and standardisation fitted on training runs (2013) only | Brief section 11: split before any fitted transform; test runs never inform a parameter | `fit_transforms.py` → `metadata/transform_params.json`, `processed/model_ready_d13/d27.parquet` | V12 parameters recomputed with test rows altered give identical values |
| Sensitive attributes (brief 9.1) | Keep gender, age_band, disability, imd_band, region in every view as audit columns; they are not in the primary predictor set; highest_education, prior attempts and credits are predictors | Fairness checks of AQ3–AQ4 need them; using them as predictors is a policy choice left to Milestone 4 as a comparison | `feature_set` role in the dictionary: id, target, predictor, audit, descriptive | V14 every column has a role; no audit column in the primary predictor list |
| Split | Time split by run: training = 2013B and 2013J runs, test = 2014B and 2014J runs; `paired_run` flag for the 9 module/start-month pairs; `student_in_training_runs` flag for test enrolments of students seen in 2013; tuning in Milestone 4 by run-grouped folds inside 2013 | The claim is prediction for a later run (C07); random splits would mix years whose withdrawal rates differ | `step9_views`: `split`, `paired_run`, `student_in_training_runs` | V15 no run in both partitions; flags recomputed independently |

===== reports/milestone-3/package/data/metadata/feature_spec.md @ 19d35a4 =====
# Prepared views and derived variables (Task 4 specification for Tasks 5–6)

Day 0 is the start of the module run; every day field is an offset from it. Week n covers days 7(n−1) to 7n−1, so
week 1 = days 0–6 and weeks 0, −1, … fall before the start (C02). The cut-offs are c = 13 (end of week 2; the list
reaches staff in week 3) and c = 27 (end of week 4; list in week 5), as fixed in Milestone 2. "Enrolled at day d" = registered by day d (or registration day unknown) and not
unregistered by day d (C09). Tasks = TMA and CMA of the run (exams excluded, DQ08). Banked results are not
submissions (DQ07).

## Views (package/data/processed/)

| View | Grain (key) | Rows (expected) | Analytics level | Role |
| :---- | :---- | :---- | :---- | :---- |
| `enrolment.parquet` | enrolment (code_module, code_presentation, id_student) | 32,593 | Descriptive, diagnostic | Outcome, populations, background, whole-run measures truncated at withdrawal, split flags |
| `assessment_due.parquet` | enrolment × task (+ id_assessment) | enrolments × tasks of their run | Descriptive, diagnostic | Task status (on time, late, not submitted, banked), lateness, first missed task |
| `student_week.parquet` | enrolment × week | weeks −3 (days −28 to −22) to the run's last week, cut after the withdrawal week | Descriptive, diagnostic | Weekly clicks (raw, de-duplicated), active days, sites; logging-gap flag |
| `features_d13.parquet`, `features_d27.parquet` | enrolment enrolled at the cut-off | 28,069; 27,535 | Predictive | Pre-cut-off features, target, split, audit columns |
| `capacity_by_run.parquet` | run × cut-off | 44 | Prescriptive (requirement) | Enrolled count and list sizes under assumed capacities |
| `model_ready_d13.parquet`, `model_ready_d27.parquet` | as the feature views | as above | Predictive | Encoded and scaled matrices from training-run parameters |

## Derived variables

| Variable | View | Formula | Source fields | Window / timing rule | AQ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `non_completion` (target) | all | final_result ∈ {Fail, Withdrawn} | studentInfo.final_result | Observed at run end; never a feature | AQ1–AQ3 |
| `completed` | enrolment | final_result ∈ {Pass, Distinction} | final_result | Run end | AQ1, KPI |
| `enrolled_d13/d14/d27` | enrolment | enrolled_at(d) | date_registration, date_unregistration | Day d | KPI, AQ3 |
| `registration_lead` | enrolment, features | −date_registration (days registered before the start) | date_registration | Known at registration | AQ2, AQ3 |
| `banked_results` | enrolment, features | count of the enrolment's banked results | studentAssessment.is_banked | Known at registration (carried over) | AQ3 |
| `concurrent_runs` | enrolment | other enrolments of the student with the same code_presentation | studentInfo | Known at registration | AQ2 (2014 only, C12) |
| `imd_band` | all | label normalised, missing → "Missing" | studentInfo.imd_band | Audit only | AQ3–AQ4 fairness |
| `status` | assessment_due | banked; not_submitted; on_time (submitted ≤ due); late (submitted > due) | date_submitted, assessments.date, is_banked | Whole run (descriptive) | AQ1, AQ2 |
| `lateness_days` | assessment_due | date_submitted − due day (submitted rows) | date_submitted, date | Whole run | AQ2 |
| `due_while_enrolled` | assessment_due | due day ≤ unregistration day − 1 (or never unregistered) and registration ≤ due day | due, registration days | Whole run | AQ1, AQ2 (a task counts as missed only if due while enrolled) |
| `first_missed_week` | enrolment | week of the earliest due task with status not_submitted and due_while_enrolled | assessment_due | Whole run | AQ1 |
| `total_clicks`, `active_days` | enrolment | clicks and distinct active days from the first record to the unregistration day (or run end) | studentVle | Truncated at withdrawal (DQ03) | AQ1, AQ2 descriptive only |
| `clicks_pre` | features | clicks on days < 0 | studentVle.date, sum_click | Before day 0 | AQ2, AQ3 |
| `clicks_0c`, `clicks_0c_dedup` | features | clicks on days 0…c (exact duplicate rows once in `_dedup`) | studentVle | Days 0 to c | AQ2, AQ3 |
| `active_days_0c` | features | distinct days with ≥ 1 click in 0…c | studentVle.date | Days 0 to c | AQ2, AQ3 |
| `sites_0c` | features | distinct resources clicked in 0…c | id_site | Days 0 to c | AQ3 |
| `clicks_w1 … clicks_w2` (d13), `clicks_w1 … clicks_w4` (d27) | features | clicks per week up to the cut-off | studentVle | Weeks fully before the cut-off | AQ3 |
| `clicks_last7`, `inactive_last7` | features | clicks on days c−6…c (equal to the last week's clicks at both cut-offs; source of the flag, not a predictor); inactive = 0 clicks | studentVle | Seven days ending at c | AQ2, AQ3, rule |
| `activity_ratio_run` | features | (clicks_0c + 1) ÷ (median clicks_0c of the enrolments of the same run enrolled at c + 1) | studentVle | Same run, days 0 to c only; no outcome used | AQ2 sign "activity against the course average" |
| `tasks_due_c` | features | tasks with due day ≤ c | assessments.date | Due by c | AQ2, AQ3 |
| `tasks_missed_c` | features | tasks due ≤ c with no non-banked submission on or before c | studentAssessment | Submissions ≤ c | AQ2, AQ3, rule |
| `tasks_late_c` (`tma_late_c`, `cma_late_c`) | features | tasks due ≤ c submitted after the due day and on or before c, in total and by type | studentAssessment | Submissions ≤ c | AQ2, AQ3, rule |
| `cma_score_mean_c` | features | mean score of CMAs submitted on or before c − 7 (null if none) | score, assessment_type | CMA marks appear within 7 days (computer marked); TMA marks excluded (returned up to ten working days after the cut-off, no release day in the data) | AQ3 |
| `early_sign_rule` | features | tasks_missed_c ≥ 1 or tma_late_c ≥ 1 or inactive_last7; components stored as `rule_missed`, `rule_tma_late`, `inactive_last7` | derived | At c; at day 13 it acts as an activity rule (a task is due in 1 run of 22) | AQ3 comparison rule, secondary KPI 1 (C10) |
| `early_sign_rule_cma` | features | early_sign_rule or cma_late_c ≥ 1 | derived | At c | Sensitivity variant (CMA lateness undocumented) |
| `cma_marked_c` | features | number of CMA marks known at c (submitted ≤ c − 7, scored) | studentAssessment | At c | AQ3 (coverage of the CMA score) |
| `clicks_pre14` | features (extended) | clicks on days −14 to −1 | studentVle | Fixed pre-start window | AQ3 |
| `days_since_last_click` | features (extended) | c − last day 0…c with a click (null if none) | studentVle | At c | AQ3 |
| `trend_last_week` | features (extended) | clicks in the last week minus the week before | studentVle | Weeks up to c | AQ3 |
| `clicks_oucontent_0c`, `clicks_forumng_0c`, `clicks_quiz_0c`, `clicks_homepage_0c` | features (extended) | clicks on days 0…c on resources of that type | studentVle, vle.activity_type | Days 0 to c | AQ2, AQ3 |
| `tasks_submitted_early_c` | features (extended) | tasks due after c already submitted by c (non-banked) | studentAssessment | Submissions ≤ c | AQ3 |
| `split` | enrolment, features | train if year 2013, test if 2014 | code_presentation | Run level | AQ3 |
| `paired_run` | enrolment, features | the run's module and start month have runs in both years | courses | Run level | AQ3 evaluation subsets |
| `student_in_training_runs` | features (test rows) | id_student appears in any 2013 enrolment | studentInfo | Known before the 2014 run | AQ3 strict check |
| `list_size_*` | capacity_by_run | tutor groups = ceil(enrolled_c / 20); list = 3 or 5 per group; office scenario 30 or 40 per run | features views | At c | AQ4 (assumed capacity) |

Capacity assumptions: Milestone 1 sets three to five contacts per lecturer-advisor a week and about 30–40 for the
support office; the OU splits a module into tutor groups of a few tens of students (Hlosta et al., 2018); a group of
20 is assumed to stand in for one advisor's caseload.

===== reports/milestone-3/package/data/metadata/lineage.md @ 19d35a4 =====
# Data lineage (brief section 13.1)

One row per prepared variable, from `src/dictionary.py`; the formulas are implemented in `src/prepare_data.py`.

| Prepared variable | Source file / field | Transformation | Window / filter | Purpose / AQ | Sensitivity |
| :---- | :---- | :---- | :---- | :---- | :---- |
| year | code_presentation | first four characters | – | time split | none |
| split | code_presentation | train if 2013, test if 2014 | run level | AQ3 time split (C07) | none |
| paired_run | courses | module and start month ran in both years | run level | AQ3 evaluation subsets | none |
| student_in_training_runs | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | – | AQ3 strict unseen-student check | none |
| eval_withdrawal_day_unknown | final_result, date_unregistration | Withdrawn without a withdrawal day | – | AQ3: report test metrics with and without these rows (audit F1) | none |
| final_result | studentInfo.final_result | as recorded | observed at run end | AQ1 outcome | none |
| non_completion | studentInfo.final_result | Fail or Withdrawn | observed at run end | AQ1–AQ3 target | none |
| completed | studentInfo.final_result | Pass or Distinction | observed at run end | primary KPI | none |
| withdrawal_day_missing | final_result, date_unregistration | Withdrawn without a day | – | DQ04 flag | none |
| unregistered_not_withdrawn | final_result, date_unregistration | not Withdrawn but a day recorded | – | DQ04 flag | none |
| unregistered_after_run_end | date_unregistration, courses | day after run length | – | DQ06 flag | none |
| date_registration | studentRegistration.date_registration | as recorded | day offset | populations | none |
| date_unregistration | studentRegistration.date_unregistration | as recorded | day offset; after the cut-offs for feature rows | populations, withdrawal timing (AQ1) | none |
| enrolled_d13 | registration days | enrolled_at(13) | day 13 | AQ3 population (C09) | none |
| enrolled_d14 | registration days | enrolled_at(14) | day 14 | primary KPI denominator (C09) | none |
| enrolled_d27 | registration days | enrolled_at(27) | day 27 | AQ3 population (C09) | none |
| start_month | code_presentation | last character: B = February, J = October | – | AQ1 dimension; AQ3 predictor | none |
| run_length | courses.module_presentation_length | renamed | – | run end | none |
| gender | studentInfo.gender | as recorded | – | AQ3–AQ4 fairness audit | sensitive |
| region | studentInfo.region | as recorded | – | fairness audit; explains imd_band Missing | sensitive |
| age_band | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | – | fairness audit | sensitive |
| disability | studentInfo.disability | as recorded (Y/N) | – | AQ4 fairness limit (C04) | sensitive |
| imd_band | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | – | AQ4 fairness limit (C04) | sensitive |
| highest_education | studentInfo.highest_education | ordered; ordinal code in model_ready | known at enrolment | AQ2–AQ3 | sensitive |
| num_of_prev_attempts | studentInfo.num_of_prev_attempts | as recorded | known at enrolment | AQ3 | none |
| studied_credits | studentInfo.studied_credits | as recorded; outliers kept | known at enrolment | AQ3 (study load) | none |
| registration_lead | studentRegistration.date_registration | −date_registration | known at registration | AQ2–AQ3 | none |
| registration_missing | studentRegistration.date_registration | registration day missing | known at registration | AQ3 extended (39 of 45 are Withdrawn) | none |
| banked_results | studentAssessment.is_banked | count of banked results | known at registration | AQ3 | none |
| concurrent_runs | studentInfo | other enrolments of the student in the same presentation | – | AQ2 (2014 only, C12) | none |
| first_missed_week | assessment_due | week of earliest TMA/CMA not submitted and due while enrolled | whole run | AQ1 | none |
| tasks_due_while_enrolled | assessment_due | count, banked excluded | whole run | AQ1–AQ2 | none |
| tasks_missed_while_enrolled | assessment_due | count not submitted | whole run | AQ1–AQ2 | none |
| tasks_late_while_enrolled | assessment_due | count submitted after the due day | whole run | AQ2 | none |
| total_clicks | studentVle.sum_click | sum of all rows | whole run, up to the unregistration day | AQ1–AQ2 | none |
| total_clicks_dedup | studentVle.sum_click | sum with exact duplicate rows once | as total_clicks | DQ01 sensitivity | none |
| active_days | studentVle.date | distinct days with a click | whole run (student_week: within the week), up to the unregistration day | AQ1–AQ2 | none |
| assessment_type | assessments.assessment_type | TMA or CMA (exams excluded) | – | AQ1–AQ2 | none |
| due_day | assessments.date | renamed | day offset | AQ1–AQ2 | none |
| due_week | assessments.date | floor(due / 7) + 1 | – | AQ1 | none |
| weight | assessments.weight | as recorded; not used for grades | – | DQ09 | none |
| date_submitted | studentAssessment.date_submitted | as recorded; null if not submitted | whole run | AQ1–AQ2 | none |
| is_banked | studentAssessment.is_banked | as recorded | – | DQ07 | none |
| score | studentAssessment.score | as recorded; not a feature except via cma_score_mean_c | whole run | AQ2 | none |
| status | date_submitted, due day, is_banked | banked / not_submitted / on_time / late | whole run | AQ1–AQ2 | none |
| lateness_days | date_submitted, due day | submitted − due (non-banked) | whole run | AQ2 | none |
| due_while_enrolled | due day, registration days | registered by due day and unregistered after it | whole run | AQ1 (missed only if due while enrolled) | none |
| clicks | studentVle.sum_click | sum per week | week, up to the unregistration day | AQ1–AQ2 | none |
| clicks_dedup | studentVle.sum_click | weekly sum, exact duplicates once | week | DQ01 sensitivity | none |
| records | studentVle | number of log rows | week | DQ02 | none |
| sites | studentVle.id_site | distinct resources | week | AQ2 | none |
| logging_gap | studentVle.date | week holds a day with no click in the whole run | week | DQ15 | none |
| clicks_pre | studentVle.sum_click, date | sum | days before 0 | AQ2–AQ3 | none |
| clicks_pre14 | studentVle.sum_click, date | sum | days −14 to −1 | AQ3 | none |
| clicks_0c | studentVle.sum_click, date | sum (= sum of clicks_w*) | days 0 to c | AQ2–AQ3 | none |
| clicks_0c_dedup | studentVle | sum, exact duplicate rows once | days 0 to c | DQ01 sensitivity | none |
| active_days_0c | studentVle.date | distinct days with a click | days 0 to c | AQ2–AQ3 | none |
| sites_0c | studentVle.id_site | distinct resources | days 0 to c | AQ3 | none |
| inactive_last7 | studentVle | no click in days c−6 to c | last seven days | AQ2–AQ3; rule part | none |
| activity_ratio_run | studentVle | (clicks_0c + 1) ÷ (run median of clicks_0c + 1) | same run, days 0 to c, enrolled at c | AQ2 sign against the course average | none |
| tasks_due_c | assessments.date | TMA/CMA due by c and on or after the registration day | due ≤ c | AQ2–AQ3 | none |
| tasks_missed_c | studentAssessment | due ≤ c, no non-banked submission by c | submissions ≤ c | AQ2–AQ3; rule part | none |
| tasks_late_c | studentAssessment | due ≤ c, submitted after due and by c | submissions ≤ c | AQ2–AQ3 | none |
| tma_late_c | studentAssessment | late TMA by c | submissions ≤ c | AQ2–AQ3; rule part | none |
| cma_late_c | studentAssessment | late CMA by c | submissions ≤ c | AQ2–AQ3; rule variant | none |
| cma_marked_c | studentAssessment | CMA marks known by c | submitted ≤ c − 7 | AQ3 (coverage of the CMA score) | none |
| cma_score_mean_c | studentAssessment.score | mean of known CMA marks; null if none | submitted ≤ c − 7 | AQ3 | none |
| days_since_last_click | studentVle.date | c − last active day; c + 1 if no click in 0…c | days 0 to c | AQ3 | none |
| trend_last_week | studentVle | last week's clicks − previous week's | weeks up to c | AQ3 | none |
| tasks_submitted_early_c | studentAssessment | tasks due after c submitted by c | submissions ≤ c | AQ3 | none |
| clicks_oucontent_0c | studentVle, vle.activity_type | sum on content pages | days 0 to c | AQ2–AQ3 | none |
| clicks_forumng_0c | studentVle, vle.activity_type | sum on forums | days 0 to c | AQ2–AQ3 | none |
| clicks_quiz_0c | studentVle, vle.activity_type | sum on quizzes | days 0 to c | AQ2–AQ3 | none |
| clicks_homepage_0c | studentVle, vle.activity_type | sum on the homepage | days 0 to c | AQ2–AQ3 | none |
| early_sign_rule | derived | rule_missed or rule_tma_late or inactive_last7 | at c | AQ3 comparison rule; secondary KPI 1 (C10) | none |
| early_sign_rule_cma | derived | early_sign_rule or cma_late_c ≥ 1 | at c | sensitivity variant | none |
| rule_missed | derived | tasks_missed_c ≥ 1 | at c | rule part | none |
| rule_tma_late | derived | tma_late_c ≥ 1 | at c | rule part | none |
| enrolled | features views | count enrolled at the cut-off | run, cut-off | AQ4 | none |
| tutor_groups_est | enrolled | ceil(enrolled / 20) | run, cut-off | AQ4 (assumed group of 20) | none |
| list_tutor_3 | tutor_groups_est | 3 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity | none |
| list_tutor_5 | tutor_groups_est | 5 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity | none |
| list_office_30 | enrolled | min(30, enrolled) | run, cut-off | AQ4 assumed capacity | none |
| list_office_40 | enrolled | min(40, enrolled) | run, cut-off | AQ4 assumed capacity | none |
| clicks_w1 | studentVle | sum per week | week 1 (days 0–6) | AQ3 weekly trajectory | none |
| clicks_w2 | studentVle | sum per week | week 2 (days 7–13) | AQ3 weekly trajectory | none |
| clicks_w3 | studentVle | sum per week | week 3 (days 14–20) | AQ3 weekly trajectory | none |
| clicks_w4 | studentVle | sum per week | week 4 (days 21–27) | AQ3 weekly trajectory | none |

===== reports/milestone-3/package/data/metadata/predictor_sets.json @ 19d35a4 =====
{
  "rule": "the only columns a model may use; everything else in a feature view is id, split, evaluation, target, rule or audit (data_dictionary.md)",
  "primary": [
    "code_module",
    "start_month",
    "highest_education",
    "num_of_prev_attempts",
    "studied_credits",
    "registration_lead",
    "banked_results",
    "clicks_pre",
    "clicks_0c",
    "active_days_0c",
    "sites_0c",
    "inactive_last7",
    "activity_ratio_run",
    "tasks_due_c",
    "tasks_missed_c",
    "tasks_late_c",
    "tma_late_c",
    "cma_late_c",
    "cma_marked_c",
    "cma_score_mean_c"
  ],
  "extended": [
    "registration_missing",
    "clicks_0c_dedup",
    "clicks_pre14",
    "days_since_last_click",
    "trend_last_week",
    "tasks_submitted_early_c",
    "clicks_oucontent_0c",
    "clicks_forumng_0c",
    "clicks_quiz_0c",
    "clicks_homepage_0c"
  ],
  "weekly_clicks": {
    "d13": [
      "clicks_w1",
      "clicks_w2"
    ],
    "d27": [
      "clicks_w1",
      "clicks_w2",
      "clicks_w3",
      "clicks_w4"
    ]
  },
  "not_used_in_milestone4": {
    "cma_score_mean_c": "known for fewer than 10% of training rows at both cut-offs"
  }
}

===== reports/milestone-3/package/data/metadata/quality_issue_log.md @ 19d35a4 =====
# Data Quality Issue Log (Task 2, brief section 7.1)

Every row rests on a computed result: `P.` = `data/metadata/profile.json` (written by `src/02_profile.py`),
`U.` = `data/metadata/understanding.json` (written by `src/01_understand.py`). Severity is judged against the
analytical questions (AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive): High = it would change a
reported rate, the target or a feature at a cut-off; Medium = it would change a measure if ignored, with a known
size; Low = it affects a few records or fields that no AQ relies on. The decision column states what the pipeline
does; the Preparation Decision Matrix (`decision_matrix.md`) gives the rationale, implementation and validation.

| Issue ID | Variable / table | Evidence | Impact on AQ | Severity | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- |
| DQ01 | studentVle: exact duplicate rows | 787,170 rows (7.39%) repeat another row in every column; 3.82–11.73% per run; 69.8% of duplicated groups are single-click; collapsing them removes 3.19% of clicks (P.duplicates). In two-row student-site-day groups, 31.5% have equal counts against 24.0% expected by chance from each site's own counts; quizzes, wikis and questionnaires fall below chance, forums and content pages above it (P.duplicates.chance_test_two_row_groups) | Click measures of AQ2 and AQ3 | Medium | Cause not decidable from the data: keep every row in the primary click measures (the table's record grain) and build a de-duplicated variant of each click feature for sensitivity |
| DQ02 | studentVle: grain differs from the documentation | 1,614,505 student-site-day groups hold several rows (3,810,465 rows), 1,179,074 of them with different click counts; up to 10 rows in one group (P.shape.studentVle_grain) | Any join or count at row level would mistake records for days | Medium | Aggregate clicks to enrolment × day and enrolment × week before any join; count active days, not rows |
| DQ03 | studentVle, studentAssessment: activity after unregistration | 29,440 click rows (98,745 clicks) by 1,279 enrolments, up to 423 days after unregistering; 588 non-banked submissions by 411 enrolments (P.validity) | Engagement up to withdrawal (AQ1, AQ2); none at a cut-off for students still registered | Medium | Truncate engagement measures at the unregistration day; feature views contain only students still registered at the cut-off, so no post-withdrawal event enters them |
| DQ04 | final_result × date_unregistration | 93 Withdrawn enrolments without an unregistration day, 87 of them in October 2014 runs; 9 Fail enrolments with one, 8 of them on or before day 0 (U.outcome, P.validity.withdrawn_without_day_by_presentation) | Populations at day 14, 13 and 27; time to withdrawal | Low | Keep final_result as the outcome; keep the recorded day; flag both groups (`withdrawal_day_missing`, `unregistered_not_withdrawn`); the 93 stay in every population because no record shows them leaving before a cut-off, and an evaluation flag lets test metrics be reported with and without them |
| DQ05 | studentRegistration: registration after day 14 | 58 enrolments registered on days 16–167, after the two-week sign-up window of the descriptor; 16 of them later unregistered (P.validity) | KPI denominator and populations at cut-offs | Low | Define "enrolled at day d" as registered by day d (or registration day unknown) and not unregistered by day d; late registrants enter only the populations of later days |
| DQ06 | studentRegistration: departures before teaching | 3,097 enrolments unregistered on or before day 0; one unregistration on day 444 of a 268-day run (U.outcome) | KPI denominator | Low | Not an error: these students left before the run began and are outside the day-14 KPI population; the day-444 record is kept with a flag |
| DQ07 | studentAssessment: banked results | All 1,909 banked results carry date_submitted = −1, a placeholder for a result carried over from an earlier run (P.validity.banked_day_values) | Timeliness and missed-task measures (AQ1–AQ3) | Medium | Exclude banked rows from submission timing, lateness and missed-task counts; keep a per-enrolment count of banked results, known at registration |
| DQ08 | assessments, studentAssessment: exams | 18 of 24 exams have no result rows (scores only for CCC 2 and DDD 4); 11 exams have no due day (P.missing, U.time) | "First missed assessed task" (AQ1); task signs (AQ2, AQ3) | High for exams, none for coursework | Count missed and late tasks over TMA and CMA only; the outcome stays final_result; exam scores are not used |
| DQ09 | assessments: weights | Coursework weights sum to 0 in the three GGG runs and to 100 elsewhere; FFF CMAs weigh 0; CCC 2014 runs hold two exams (total 200) (P.validity, U.measurement) | Weighted score features | Medium | Build no weighted grade; count tasks unweighted (formative tasks are still due) and keep weight as a column |
| DQ10 | studentAssessment: late and post-run submissions | 49,318 of 169,138 non-banked submissions with a due day are late (29.2%; median 3, 99th percentile 29 days): 16,320 of 97,088 TMA and 32,991 of 69,956 CMA, although the OU's current (2025) policy accepts no CMA after its cut-off day; 85 fall after the run ended, up to day 608 (P.validity) | Late-task signs (AQ1, AQ2, early-sign rule) | Medium | Keep every submission; lateness = date_submitted − due day, counted separately for TMA and CMA because the meaning of a late CMA in 2013–2014 is not documented; post-run submissions fall after both cut-offs |
| DQ11 | studentAssessment.score | 173 missing scores, all TMA (P.missing.score_missing_by_type); 45.8% of CMA scores are multiples of 10 against 17.4% of TMA (P.distribution) | Score features | Low | Keep the submission, leave the score missing; scores enter features only where the mark is known at the cut-off (decision matrix, row "Derived feature") |
| DQ12 | studentInfo.imd_band | 1,111 missing (3.41%), 40.1% of North Region and 22.5% of Ireland; success 65.7% when missing against 46.6% when present, so not missing at random; one label "10-20" lacks the % sign (P.missing, P.validity) | AQ4 fairness check by deprivation; background features | Medium | Normalise the label to "10-20%"; keep missing as its own category "Missing"; no imputation |
| DQ13 | studentRegistration.date_registration | 45 missing, 39 of them Withdrawn (P.missing) | Registration-lead feature | Low | Keep null with an indicator; any filling is fitted on the training runs only |
| DQ14 | vle.week_from, week_to | 82.4% missing; filled for 1,121 of 6,364 sites (P.missing, U.time) | None | Low | Not used |
| DQ15 | studentVle: days without any click | In all six February 2014 runs two consecutive days carry no click (days 218–219; days 211–212 in BBB) (P.temporal) | Daily activity series after week 30 | Low | Treat the two days as missing, not as zero activity, in daily series; both lie after the cut-offs |
| DQ16 | Outliers: clicks and credits | One row of 6,977 clicks; clicks per enrolment skewness 3.03, 2,503 enrolments beyond the upper interquartile-range fence; studied_credits up to 655 against a 99th percentile of 240 (P.distribution) | Scale-sensitive methods | Low | Keep every value (heavy users and students on several modules are real); log or rank transforms are applied in modelling, fitted on training runs |
| DQ17 | Enrolments without any activity or submission row | 3,365 enrolments without a click row (2,988 Withdrawn; 2,390 left by day 0); 6,750 without a submission (P.missing) | Counts would drop these students under an inner join | Medium | Absence of a row records no activity (descriptor: no submission, no result row): fill counts with 0 after left joins from the enrolment table |
| DQ18 | assessments: tasks due by the cut-offs | A non-exam task is due by day 13 in 1 of 22 runs and by day 27 in 16; two or more are due by day 27 in 1 run only (P.temporal.tasks_due_by_cutoff) | AQ3 comparison rule and secondary KPI 1: the Milestone 1 rule ("two or more tasks missed or late by week 4") can fire in 1 run of 22, and its OULAD form of one task (C06) in 16 runs at day 27 and 1 at day 13 | High | Task 3 decision (AQ–Data fit): rule restated on the tasks actually due (Change Log C10) |
| DQ19 | Population and module mix | Seven UK distance-learning modules of 2013–2014, selected partly for many failing students; women 11.5% of EEE and 88.4% of BBB; completion in the day-14 population from 45.7% (CCC) to 73.8% (AAA) (P.representativeness) | Generalisation of every AQ; group comparisons | High for claims | State the scope; compare groups within module; results describe OULAD and are re-checked on the university's data before decisions D1–D3 |

===== reports/milestone-3/package/data/metadata/split_spec.md @ 19d35a4 =====
# Split and leakage specification (Task 6, brief section 11)

| Risk (brief 11) | Case in this project | Control | Where | Check |
| :---- | :---- | :---- | :---- | :---- |
| Target leakage | final_result, withdrawal day, activity or submissions after the cut-off, TMA marks (release day unknown), whole-run measures | Feature views computed only from events dated ≤ c; target and whole-run measures kept out of the predictor list; CMA marks only | `prepare_data.py` step 8; dictionary role | V13 (max event day per feature ≤ c), V14 (roles) |
| Train–test contamination | Imputation values, scaling, category levels, log transforms fitted on all runs | Fitted on training runs (2013) only and applied to test runs | `fit_transforms.py` | V12 (parameters unchanged when test rows are altered) |
| Student leakage | 2014 enrolments of students already seen in 2013 runs | Main test keeps them (the claim is a later run of the same modules, where repeaters exist); `student_in_training_runs` marks them for a strict unseen-student check | `prepare_data.py` step 9 | V15 flag recomputed independently |
| Temporal leakage | Random split across years; tuning on 2014 | Split by run year: training 2013B, 2013J (9 runs); test 2014B, 2014J (13 runs); tuning only inside 2013 by leave-one-run-out folds that also keep each student in one fold; intervals by bootstrap clustered by student; 2014 outcomes are not looked at while preparing | `prepare_data.py` step 9; Milestone 4 protocol | V15 (no run in both partitions); validation reports test outcome rates only as counts |
| Cohort statistic | `activity_ratio_run` uses the same run's median up to c | Uses only pre-cut-off activity of students enrolled at c, no outcome; the same value is known to staff on day c | step 8 | V13 |
| Augmentation leakage | None: no synthetic augmentation | – | – | – |

Paired subset: the 9 test runs whose module and start month also ran in 2013 (BBB-B, DDD-B, FFF-B, AAA-J, BBB-J,
DDD-J, EEE-J, FFF-J, GGG-J); the other 4 test runs (CCC-B, CCC-J, EEE-B, GGG-B) test a model trained on other
modules or start months and are reported separately.

===== reports/milestone-3/package/data/metadata/traceability.md @ 19d35a4 =====
# Updated traceability (deliverable B, brief section 16)

Every row serves the Business Goal: improve successful course completion in the program's online and blended courses
by identifying students who stop taking part early enough to support them within the semester. Columns follow brief
section 16: Business Goal / SMART / KPI → AQ → analytics type → raw variables → preparation → prepared variables /
view → decision supported. Raw variables are OULAD columns; prepared variables are columns of `data/processed/`.

| Business Goal / SMART / KPI | AQ | Analytics type | Raw variables | Preparation | Prepared variables / view | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Primary KPI: completion rate of students enrolled after the add-drop period (day 14; SMART assumed 70% → 75%) | AQ1 | Descriptive | studentInfo.final_result; studentRegistration.date_registration, date_unregistration; assessments.date; studentAssessment.date_submitted, is_banked | Enrolled-at-day rule (C09); tasks = TMA and CMA; banked results separated; missed only if due while enrolled | `enrolment`: completed, non_completion, enrolled_d14, first_missed_week, code_module, code_presentation, start_month, year; `assessment_due`: status, due_week | D2 where advisors' time goes; D3 extend after the pilot |
| Primary KPI; secondary KPI 1, sign part (early-sign rule, C10) | AQ2 | Diagnostic | + studentVle.date, sum_click, id_site; vle.activity_type | Clicks aggregated by enrolment × day (DQ02), truncated at withdrawal (DQ03), all rows kept with a de-duplicated twin (DQ01); signs up to day 27 | `features_d27`: tasks_missed_c, tasks_late_c, tma_late_c, cma_late_c, inactive_last7, activity_ratio_run, clicks_*_0c; `enrolment`: concurrent_runs (2014) | D2; the reasons shown with D1 lists |
| Secondary KPI 1, sign part | AQ3 | Predictive | as AQ2 + num_of_prev_attempts, studied_credits, highest_education, date_registration, is_banked, score (CMA) | Populations at days 13 and 27; events ≤ cut-off only; CMA marks known at c − 7; time split; transforms fitted on 2013 runs | `features_d13`, `features_d27` (20 primary, 10 extended predictors, weekly clicks), `early_sign_rule`, `split`, `paired_run`, `student_in_training_runs`; `model_ready_d13/d27` | D1 who is listed in weeks 3 and 5 |
| Secondary KPI 2 (follow-up rate) and secondary KPI 1, contact part: pilot only (C08) | AQ4 (rewritten, C11) | Prescriptive (ranking requirement) | AQ3 inputs; gender, age_band, disability, imd_band, region as audit columns | Capacity scenarios from tutor groups of about 20; list quality as lift and attainable recall (C13); fairness by imd_band ("Missing" apart) and disability | `capacity_by_run`: enrolled, list_tutor_3, list_tutor_5, list_office_30, list_office_40; audit columns in the feature views | D1 ordered list within capacity; contact choice deferred |

===== reports/milestone-3/package/data/metadata/transform_params.json @ 19d35a4 =====
{
  "generated": "2026-11-06T15:24:14Z",
  "fitted_on": "split = train (2013B, 2013J runs)",
  "cutoffs": {
    "d13": {
      "cutoff": 13,
      "nominal_levels": {
        "code_module": [
          "AAA",
          "BBB",
          "DDD",
          "EEE",
          "FFF",
          "GGG"
        ],
        "start_month": [
          "B",
          "J"
        ]
      },
      "ordinal_codes": {
        "highest_education": {
          "No Formal quals": 0,
          "Lower Than A Level": 1,
          "A Level or Equivalent": 2,
          "HE Qualification": 3,
          "Post Graduate Qualification": 4
        }
      },
      "fill_median": {
        "num_of_prev_attempts": 0.0,
        "studied_credits": 60.0,
        "registration_lead": 53.0,
        "banked_results": 0.0,
        "clicks_pre": 30.0,
        "clicks_0c": 79.0,
        "active_days_0c": 5.0,
        "sites_0c": 13.0,
        "activity_ratio_run": 1.0,
        "tasks_due_c": 0.0,
        "tasks_missed_c": 0.0,
        "tasks_late_c": 0.0,
        "tma_late_c": 0.0,
        "cma_late_c": 0.0,
        "cma_marked_c": 0.0,
        "cma_score_mean_c": 89.0,
        "clicks_0c_dedup": 75.0,
        "clicks_pre14": 25.0,
        "days_since_last_click": 1.0,
        "trend_last_week": 0.0,
        "tasks_submitted_early_c": 0.0,
        "clicks_oucontent_0c": 4.0,
        "clicks_forumng_0c": 23.0,
        "clicks_quiz_0c": 0.0,
        "clicks_homepage_0c": 16.0,
        "clicks_w1": 37.0,
        "clicks_w2": 32.0
      },
      "log1p": [
        "num_of_prev_attempts",
        "studied_credits",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "clicks_0c_dedup",
        "clicks_pre14",
        "tasks_submitted_early_c",
        "clicks_oucontent_0c",
        "clicks_forumng_0c",
        "clicks_quiz_0c",
        "clicks_homepage_0c",
        "clicks_w1",
        "clicks_w2"
      ],
      "mean": {
        "code_module=AAA": 0.030629139072847682,
        "code_module=BBB": 0.286341059602649,
        "code_module=DDD": 0.23774834437086093,
        "code_module=EEE": 0.07731788079470199,
        "code_module=FFF": 0.2912251655629139,
        "code_module=GGG": 0.07673841059602649,
        "start_month=B": 0.3579470198675497,
        "start_month=J": 0.6420529801324504,
        "highest_education": 1.7191225165562913,
        "num_of_prev_attempts": 0.10848955211137096,
        "studied_credits": 4.294299452473678,
        "registration_lead": 67.64801324503311,
        "banked_results": 0.021314632690826146,
        "clicks_pre": 3.0498609262823897,
        "clicks_0c": 3.918296568315061,
        "active_days_0c": 1.5774497153684999,
        "sites_0c": 2.3807083300706675,
        "inactive_last7": 0.20513245033112582,
        "activity_ratio_run": 1.5446907077834702,
        "tasks_due_c": 0.0,
        "tasks_missed_c": 0.0,
        "tasks_late_c": 0.0,
        "tma_late_c": 0.0,
        "cma_late_c": 0.0,
        "cma_marked_c": 0.010925015188562702,
        "cma_score_mean_c_missing": 0.9861754966887417,
        "cma_score_mean_c": 88.96556291390729,
        "registration_missing": 0.0004139072847682119,
        "clicks_0c_dedup": 3.8848470504261035,
        "clicks_pre14": 2.8670872751660244,
        "days_since_last_click": 3.535430463576159,
        "trend_last_week": -6.9552980132450335,
        "tasks_submitted_early_c": 0.05402280391103048,
        "clicks_oucontent_0c": 1.7849851635234943,
        "clicks_forumng_0c": 2.6779079637739573,
        "clicks_quiz_0c": 0.6818779171702043,
        "clicks_homepage_0c": 2.599087390241448,
        "clicks_w1": 3.1197883734755023,
        "clicks_w2": 3.0113315632393136
      },
      "std": {
        "code_module=AAA": 0.17231788351707286,
        "code_module=BBB": 0.45206943600255256,
        "code_module=DDD": 0.42572182508563255,
        "code_module=EEE": 0.2671062189612549,
        "code_module=FFF": 0.4543458562537252,
        "code_module=GGG": 0.266186950198767,
        "start_month=B": 0.4794162881293028,
        "start_month=J": 0.4794162881293028,
        "highest_education": 0.7361595253847911,
        "num_of_prev_attempts": 0.2823967634081644,
        "studied_credits": 0.4387682452544203,
        "registration_lead": 46.20218308003275,
        "banked_results": 0.18423985379114685,
        "clicks_pre": 1.9584800766181099,
        "clicks_0c": 1.8256373329060847,
        "active_days_0c": 0.7853488392618905,
        "sites_0c": 1.091063051047533,
        "inactive_last7": 0.40381509016533956,
        "activity_ratio_run": 2.175741802757847,
        "tasks_due_c": 1.0,
        "tasks_missed_c": 1.0,
        "tasks_late_c": 1.0,
        "tma_late_c": 1.0,
        "cma_late_c": 1.0,
        "cma_marked_c": 0.09449350877541224,
        "cma_score_mean_c_missing": 0.11676692641531888,
        "cma_score_mean_c": 1.4217502605858399,
        "registration_missing": 0.02034134258177961,
        "clicks_0c_dedup": 1.8169299479610268,
        "clicks_pre14": 1.921857873925571,
        "days_since_last_click": 4.609719120531676,
        "trend_last_week": 95.4201353162464,
        "tasks_submitted_early_c": 0.20111040734360106,
        "clicks_oucontent_0c": 1.6909152772448306,
        "clicks_forumng_0c": 1.8564163404545424,
        "clicks_quiz_0c": 1.427704095178636,
        "clicks_homepage_0c": 1.352074281947396,
        "clicks_w1": 1.8912161370319942,
        "clicks_w2": 1.8807694189740156
      },
      "indicator": [
        "cma_score_mean_c"
      ],
      "columns": [
        "code_module=AAA",
        "code_module=BBB",
        "code_module=DDD",
        "code_module=EEE",
        "code_module=FFF",
        "code_module=GGG",
        "start_month=B",
        "start_month=J",
        "highest_education",
        "num_of_prev_attempts",
        "studied_credits",
        "registration_lead",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "inactive_last7",
        "activity_ratio_run",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "cma_score_mean_c_missing",
        "cma_score_mean_c",
        "registration_missing",
        "clicks_0c_dedup",
        "clicks_pre14",
        "days_since_last_click",
        "trend_last_week",
        "tasks_submitted_early_c",
        "clicks_oucontent_0c",
        "clicks_forumng_0c",
        "clicks_quiz_0c",
        "clicks_homepage_0c",
        "clicks_w1",
        "clicks_w2"
      ],
      "primary": [
        "code_module",
        "start_month",
        "highest_education",
        "num_of_prev_attempts",
        "studied_credits",
        "registration_lead",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "inactive_last7",
        "activity_ratio_run",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "cma_score_mean_c"
      ]
    },
    "d27": {
      "cutoff": 27,
      "nominal_levels": {
        "code_module": [
          "AAA",
          "BBB",
          "DDD",
          "EEE",
          "FFF",
          "GGG"
        ],
        "start_month": [
          "B",
          "J"
        ]
      },
      "ordinal_codes": {
        "highest_education": {
          "No Formal quals": 0,
          "Lower Than A Level": 1,
          "A Level or Equivalent": 2,
          "HE Qualification": 3,
          "Post Graduate Qualification": 4
        }
      },
      "fill_median": {
        "num_of_prev_attempts": 0.0,
        "studied_credits": 60.0,
        "registration_lead": 54.0,
        "banked_results": 0.0,
        "clicks_pre": 31.0,
        "clicks_0c": 187.0,
        "active_days_0c": 10.0,
        "sites_0c": 21.0,
        "activity_ratio_run": 1.0,
        "tasks_due_c": 1.0,
        "tasks_missed_c": 0.0,
        "tasks_late_c": 0.0,
        "tma_late_c": 0.0,
        "cma_late_c": 0.0,
        "cma_marked_c": 0.0,
        "cma_score_mean_c": 87.0,
        "clicks_0c_dedup": 180.0,
        "clicks_pre14": 25.0,
        "days_since_last_click": 1.0,
        "trend_last_week": -7.0,
        "tasks_submitted_early_c": 0.0,
        "clicks_oucontent_0c": 18.0,
        "clicks_forumng_0c": 46.0,
        "clicks_quiz_0c": 0.0,
        "clicks_homepage_0c": 37.0,
        "clicks_w1": 38.0,
        "clicks_w2": 32.0,
        "clicks_w3": 48.0,
        "clicks_w4": 29.0
      },
      "log1p": [
        "num_of_prev_attempts",
        "studied_credits",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "clicks_0c_dedup",
        "clicks_pre14",
        "tasks_submitted_early_c",
        "clicks_oucontent_0c",
        "clicks_forumng_0c",
        "clicks_quiz_0c",
        "clicks_homepage_0c",
        "clicks_w1",
        "clicks_w2",
        "clicks_w3",
        "clicks_w4"
      ],
      "mean": {
        "code_module=AAA": 0.031242062484124967,
        "code_module=BBB": 0.2848192363051393,
        "code_module=DDD": 0.23622047244094488,
        "code_module=EEE": 0.07848615697231394,
        "code_module=FFF": 0.290999915333164,
        "code_module=GGG": 0.07823215646431293,
        "start_month=B": 0.3494200321733977,
        "start_month=J": 0.6505799678266023,
        "highest_education": 1.7235627804588942,
        "num_of_prev_attempts": 0.10781016482880862,
        "studied_credits": 4.291173307329321,
        "registration_lead": 67.71636609939887,
        "banked_results": 0.022010470709928693,
        "clicks_pre": 3.0747026364414887,
        "clicks_0c": 4.85662900176513,
        "active_days_0c": 2.2306347832029845,
        "sites_0c": 2.9166046968910146,
        "inactive_last7": 0.2069257471848277,
        "activity_ratio_run": 1.4107962258698357,
        "tasks_due_c": 0.623580822572433,
        "tasks_missed_c": 0.07966910510752197,
        "tasks_late_c": 0.09075610238632494,
        "tma_late_c": 0.03386215588714659,
        "cma_late_c": 0.05745416050869413,
        "cma_marked_c": 0.04071118919386968,
        "cma_score_mean_c_missing": 0.94750656167979,
        "cma_score_mean_c": 86.91287782575566,
        "registration_missing": 0.00042333418000169333,
        "clicks_0c_dedup": 4.823869615745247,
        "clicks_pre14": 2.891467579117067,
        "days_since_last_click": 4.39734146134959,
        "trend_last_week": -22.633307933282534,
        "tasks_submitted_early_c": 0.059757058545026956,
        "clicks_oucontent_0c": 2.6520960616036646,
        "clicks_forumng_0c": 3.354688627348792,
        "clicks_quiz_0c": 1.242818194272894,
        "clicks_homepage_0c": 3.4001772972086957,
        "clicks_w1": 3.147416130082543,
        "clicks_w2": 3.046785144423705,
        "clicks_w3": 3.407876476049485,
        "clicks_w4": 2.9606164710900766
      },
      "std": {
        "code_module=AAA": 0.17397861580942472,
        "code_module=BBB": 0.45134741252913047,
        "code_module=DDD": 0.42477716246906694,
        "code_module=EEE": 0.2689464710214806,
        "code_module=FFF": 0.4542427043578278,
        "code_module=GGG": 0.2685479327074986,
        "start_month=B": 0.47680700693735034,
        "start_month=J": 0.47680700693735034,
        "highest_education": 0.7361727054000148,
        "num_of_prev_attempts": 0.2818022868617644,
        "studied_credits": 0.4389042628905747,
        "registration_lead": 46.25381859553144,
        "banked_results": 0.1876713190713036,
        "clicks_pre": 1.95106644354487,
        "clicks_0c": 1.6854842626551185,
        "active_days_0c": 0.8412064063823547,
        "sites_0c": 1.0179220168722123,
        "inactive_last7": 0.40511896768063277,
        "activity_ratio_run": 1.8515982315468598,
        "tasks_due_c": 0.2941012291400018,
        "tasks_missed_c": 0.2314225856023693,
        "tasks_late_c": 0.2356752178856658,
        "tma_late_c": 0.1494212254360135,
        "cma_late_c": 0.1911185531931667,
        "cma_marked_c": 0.17696371217882104,
        "cma_score_mean_c_missing": 0.2230293450620423,
        "cma_score_mean_c": 2.6450127416095937,
        "registration_missing": 0.020571601746088238,
        "clicks_0c_dedup": 1.6807912555564155,
        "clicks_pre14": 1.9155833342202082,
        "days_since_last_click": 7.188476740079644,
        "trend_last_week": 93.46398367965982,
        "tasks_submitted_early_c": 0.21781861644583844,
        "clicks_oucontent_0c": 1.9659137789219832,
        "clicks_forumng_0c": 1.8803012220216435,
        "clicks_quiz_0c": 1.9199236790333327,
        "clicks_homepage_0c": 1.3132440298223664,
        "clicks_w1": 1.8815913812374223,
        "clicks_w2": 1.86726908653896,
        "clicks_w3": 1.8663008679565447,
        "clicks_w4": 1.9059331509564952
      },
      "indicator": [
        "cma_score_mean_c"
      ],
      "columns": [
        "code_module=AAA",
        "code_module=BBB",
        "code_module=DDD",
        "code_module=EEE",
        "code_module=FFF",
        "code_module=GGG",
        "start_month=B",
        "start_month=J",
        "highest_education",
        "num_of_prev_attempts",
        "studied_credits",
        "registration_lead",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "inactive_last7",
        "activity_ratio_run",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "cma_score_mean_c_missing",
        "cma_score_mean_c",
        "registration_missing",
        "clicks_0c_dedup",
        "clicks_pre14",
        "days_since_last_click",
        "trend_last_week",
        "tasks_submitted_early_c",
        "clicks_oucontent_0c",
        "clicks_forumng_0c",
        "clicks_quiz_0c",
        "clicks_homepage_0c",
        "clicks_w1",
        "clicks_w2",
        "clicks_w3",
        "clicks_w4"
      ],
      "primary": [
        "code_module",
        "start_month",
        "highest_education",
        "num_of_prev_attempts",
        "studied_credits",
        "registration_lead",
        "banked_results",
        "clicks_pre",
        "clicks_0c",
        "active_days_0c",
        "sites_0c",
        "inactive_last7",
        "activity_ratio_run",
        "tasks_due_c",
        "tasks_missed_c",
        "tasks_late_c",
        "tma_late_c",
        "cma_late_c",
        "cma_marked_c",
        "cma_score_mean_c"
      ]
    }
  }
}

===== reports/milestone-3/package/data/metadata/transformation_log.md @ 19d35a4 =====
# Transformation log
Written by `src/prepare_data.py` at 2026-11-06T15:24:14Z. One row per operation, in the order run; every join is a checked left join (rows in = rows out).

| Step | Operation | Rows in | Rows out | Note |
| :---- | :---- | :---- | :---- | :---- |
| 1 load | courses.csv (SHA-256 pinned, columns as documented) |  | 22 |  |
| 1 load | assessments.csv (SHA-256 pinned, columns as documented) |  | 206 |  |
| 1 load | vle.csv (SHA-256 pinned, columns as documented) |  | 6,364 |  |
| 1 load | studentInfo.csv (SHA-256 pinned, columns as documented) |  | 32,593 |  |
| 1 load | studentRegistration.csv (SHA-256 pinned, columns as documented) |  | 32,593 |  |
| 1 load | studentAssessment.csv (SHA-256 pinned, columns as documented) |  | 173,912 |  |
| 1 load | studentVle.csv (SHA-256 pinned, columns as documented) |  | 10,655,280 |  |
| 2 population | studentInfo + studentRegistration | 32,593 | 32,593 | left join, rows kept |
| 2 population | + courses (run length) | 32,593 | 32,593 | left join, rows kept |
| 2 population | flag enrolled_d13 | 32,593 | 28,069 | enrolled at the day (C09) |
| 2 population | flag enrolled_d14 | 32,593 | 28,061 | enrolled at the day (C09) |
| 2 population | flag enrolled_d27 | 32,593 | 27,535 | enrolled at the day (C09) |
| 3 standardise | imd_band label '10-20' -> '10-20%' | 3,516 | 0 |  |
| 3 standardise | year, start_month, completed, non_completion, split derived | 32,593 | 32,593 |  |
| 3 standardise | tasks = TMA and CMA (exams excluded, DQ08) | 206 | 182 |  |
| 4 keys | studentVle rows -> enrolment x day (records, clicks, clicks_dedup) | 10,655,280 | 1,808,119 | clicks 39,605,099, de-duplicated 38,343,063 |
| 4 keys | studentVle rows -> distinct enrolment x site x day | 10,655,280 | 8,459,320 |  |
| 5 missing | imd_band missing -> category 'Missing' (no imputation) | 1,111 | 1,111 |  |
| 5 missing | flag registration_missing | 32,593 | 45 |  |
| 5 missing | flag withdrawal_day_missing | 32,593 | 93 |  |
| 5 missing | flag unregistered_not_withdrawn | 32,593 | 9 |  |
| 5 missing | flag unregistered_after_run_end | 32,593 | 1 |  |
| 6 truncate | enrolment x day click records up to the unregistration day | 1,808,119 | 1,802,593 | clicks removed 98,745 |
| 6 truncate | enrolment x site x day records up to the unregistration day | 8,459,320 | 8,435,429 |  |
| 7 integrate | enrolment x task grid (TMA, CMA of the run) | 32,593 | 286,898 |  |
| 7 integrate | + submission (if any) | 286,898 | 286,898 | left join, rows kept |
| 7 integrate | TMA/CMA submissions placed in the grid | 168,953 | 168,953 |  |
| 9 views | + banked results | 32,593 | 32,593 | left join, rows kept |
| 9 views | + concurrent runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + student seen in training runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + paired run flag | 32,593 | 32,593 | left join, rows kept |
| 9 views | + first missed task week | 32,593 | 32,593 | left join, rows kept |
| 9 views | + tasks while enrolled | 32,593 | 32,593 | left join, rows kept |
| 9 views | + whole-run activity (truncated at withdrawal) | 32,593 | 32,593 | left join, rows kept |
| 9 views | student_week grid + weekly clicks | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + weekly distinct resources | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + logging-gap flag (DQ15) | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | student_week rows (weeks -3..run end, cut at withdrawal) |  | 1,052,344 | clicks before week -3 not in this view: 0 |
| 8 features d13 | + activity up to the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + distinct resources | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks due by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + CMA marks known by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks submitted before their due day (due after the cut-off) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + run median of clicks up to the cut-off (same run, no outcome) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | features built; max event day <= cut-off | 28,069 | 28,069 | early_sign_rule 5,673 |
| 8 features d27 | + activity up to the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + distinct resources | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks due by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + CMA marks known by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks submitted before their due day (due after the cut-off) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + run median of clicks up to the cut-off (same run, no outcome) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | features built; max event day <= cut-off | 27,535 | 27,535 | early_sign_rule 7,933 |
| 10 persist | processed/enrolment.parquet |  | 32,593 | 39 columns |
| 10 persist | processed/assessment_due.parquet |  | 286,898 | 14 columns |
| 10 persist | processed/student_week.parquet |  | 1,052,344 | 10 columns |
| 10 persist | processed/features_d13.parquet |  | 28,069 | 50 columns |
| 10 persist | processed/features_d27.parquet |  | 27,535 | 52 columns |
| 10 persist | processed/capacity_by_run.parquet |  | 44 | 9 columns |

===== reports/milestone-3/package/data/metadata/understanding_map.md @ 19d35a4 =====
# Dataset Understanding Map (Task 1)

Generated 2026-11-06T15:24:01Z by `src/01_understand.py` from `data/raw/`. Every key and relationship below is a computed check; full results in `understanding.json`.

| File/Table | Rows | Unit of Analysis | Primary Key | Foreign Key | Main Variables | Time Field | Role in AQ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses.csv | 22 | module run (module × presentation) | code_module, code_presentation (unique) | – | module_presentation_length | module_presentation_length (days) | Run length; run end for exam due days (AQ1–AQ3) |
| assessments.csv | 206 | assessment of a module run | id_assessment (unique) | code_module, code_presentation → courses | assessment_type, weight | date (due day) | Due days of tasks: missed and late tasks (AQ1, AQ2), task-based features and baseline rule (AQ3) |
| vle.csv | 6,364 | learning-platform resource (site) of a module run | id_site (unique) | code_module, code_presentation → courses | activity_type | week_from, week_to (planned weeks) | Resource type of clicks (AQ2 activity mix); planned weeks rarely filled |
| studentInfo.csv | 32,593 | enrolment (student × module run) | code_module, code_presentation, id_student (unique) | code_module, code_presentation → courses | final_result, gender, region, highest_education, imd_band, age_band, num_of_prev_attempts, studied_credits, disability | – (final_result observed at run end) | Outcome and target (AQ1–AQ3); background and audit attributes (AQ2, AQ3, AQ4 fairness) |
| studentRegistration.csv | 32,593 | enrolment (student × module run) | code_module, code_presentation, id_student (unique) | code_module, code_presentation, id_student → studentInfo (1–1) | date_registration, date_unregistration | date_registration, date_unregistration (days) | KPI denominator (registered on day 14), withdrawal day, population at each cut-off |
| studentAssessment.csv | 173,912 | submission (student × assessment) | id_assessment, id_student (unique) | id_assessment → assessments; id_student (+ run of the assessment) → studentInfo | score, is_banked | date_submitted (day) | Submission and lateness (AQ1, AQ2, AQ3) |
| studentVle.csv | 10,655,280 | logged interaction record (student × resource × day; several rows per day possible) | none documented (no key) | id_site → vle; code_module, code_presentation, id_student → studentInfo | sum_click | date (day of interaction) | Platform activity by day and week (AQ2, AQ3) |

## Relationships

| Relationship | Result |
| :---- | :---- |
| courses→assessments | orphan_rows=0, parents_without_children=0, children_per_parent_min=5, children_per_parent_max=14 |
| courses→vle | orphan_rows=0, parents_without_children=0, children_per_parent_min=106, children_per_parent_max=529 |
| courses→studentInfo | orphan_rows=0, parents_without_children=0, children_per_parent_min=365, children_per_parent_max=2498 |
| studentInfo↔studentRegistration | info_without_registration=0, registration_without_info=0 |
| assessments→studentAssessment | orphan_rows=0, parents_without_children=18, children_per_parent_min=278, children_per_parent_max=1917 |
| studentInfo→studentAssessment (enrolment) | orphan_rows=0, enrolments_with_submissions=25843 |
| vle→studentVle | orphan_sites=0, sites_never_used=96 |
| studentInfo→studentVle (enrolment) | orphan_enrolments=0, enrolments_with_activity=29228, enrolments_without_activity=3365 |

===== reports/milestone-3/package/data/metadata/validation_summary.json @ 19d35a4 =====
{
  "generated": "2026-11-06T15:24:17Z",
  "checks": [
    {
      "ID": "V01a",
      "Check": "enrolment rows and outcome mix equal raw studentInfo",
      "Expected": "32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)]",
      "Observed": "32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)]",
      "Status": "PASS"
    },
    {
      "ID": "V01b",
      "Check": "students",
      "Expected": "28,785",
      "Observed": "28,785",
      "Status": "PASS"
    },
    {
      "ID": "V01c",
      "Check": "population sizes equal the profile (C09)",
      "Expected": "{'d14': 28061, 'd13': 28069, 'd27': 27535}",
      "Observed": "{'d14': 28061, 'd13': 28069, 'd27': 27535}",
      "Status": "PASS"
    },
    {
      "ID": "V01d",
      "Check": "non-completion count per feature view equals the profile",
      "Expected": "{'d13': 12708, 'd27': 12156}",
      "Observed": "{'d13': 12708, 'd27': 12156}",
      "Status": "PASS"
    },
    {
      "ID": "V02",
      "Check": "missing values after = before (no imputation in views)",
      "Expected": "{'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173}",
      "Observed": "{'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173}",
      "Status": "PASS"
    },
    {
      "ID": "V03",
      "Check": "key unique in every view",
      "Expected": "0 duplicates",
      "Observed": "{'enrolment': 0, 'assessment_due': 0, 'student_week': 0, 'features_d13': 0, 'features_d27': 0, 'capacity_by_run': 0}",
      "Status": "PASS"
    },
    {
      "ID": "V04a",
      "Check": "enrolment clicks + clicks after withdrawal = raw clicks",
      "Expected": "39,605,099",
      "Observed": "39,506,354 + 98,745 = 39,605,099",
      "Status": "PASS"
    },
    {
      "ID": "V04b",
      "Check": "student_week clicks = enrolment clicks",
      "Expected": "39,506,354",
      "Observed": "39,506,354",
      "Status": "PASS"
    },
    {
      "ID": "V04c",
      "Check": "de-duplicated total ≤ raw total",
      "Expected": "dedup ≤ raw",
      "Observed": "38,247,422 ≤ 39,506,354",
      "Status": "PASS"
    },
    {
      "ID": "V05",
      "Check": "every category in its expected set",
      "Expected": "no other label",
      "Observed": "{'imd_band': [], 'age_band': [], 'highest_education': [], 'final_result': [], 'start_month': [], 'split': []}",
      "Status": "PASS"
    },
    {
      "ID": "V06",
      "Check": "banked results carry no lateness and no missed status",
      "Expected": "0",
      "Observed": "0",
      "Status": "PASS"
    },
    {
      "ID": "V07",
      "Check": "ranges after = before (no capping)",
      "Expected": "score [0, 100]; credits [30, 655]",
      "Observed": "{'score': [0.0, 100.0], 'studied_credits': [30, 655]}",
      "Status": "PASS"
    },
    {
      "ID": "V08",
      "Check": "no student_week row after the withdrawal week",
      "Expected": "0",
      "Observed": "0",
      "Status": "PASS"
    },
    {
      "ID": "V09",
      "Check": "every logged join kept its rows",
      "Expected": "25 joins, rows in = rows out",
      "Observed": "25",
      "Status": "PASS"
    },
    {
      "ID": "V10",
      "Check": "enrolments without any click row kept with 0 clicks",
      "Expected": "≥ 3,365",
      "Observed": "3,554",
      "Status": "PASS"
    },
    {
      "ID": "V11-d13",
      "Check": "6 features recomputed from raw for all 28,069 rows (independent code)",
      "Expected": "0 mismatches",
      "Observed": "{'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0}",
      "Status": "PASS"
    },
    {
      "ID": "V13-d13",
      "Check": "pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view",
      "Expected": "26,755 rows with later clicks; no forbidden column",
      "Observed": "26,755 rows differ; forbidden []",
      "Status": "PASS"
    },
    {
      "ID": "V11-d27",
      "Check": "6 features recomputed from raw for all 27,535 rows (independent code)",
      "Expected": "0 mismatches",
      "Observed": "{'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0}",
      "Status": "PASS"
    },
    {
      "ID": "V13-d27",
      "Check": "pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view",
      "Expected": "25,663 rows with later clicks; no forbidden column",
      "Observed": "25,663 rows differ; forbidden []",
      "Status": "PASS"
    },
    {
      "ID": "V12",
      "Check": "transform parameters identical with and without test rows, equal to the stored ones",
      "Expected": "identical",
      "Observed": "d13: identical, d27: identical",
      "Status": "PASS"
    },
    {
      "ID": "V14",
      "Check": "every column documented; predictor lists hold no audit, target or descriptive column",
      "Expected": "none",
      "Observed": "{'undocumented': [], 'wrong role': []}",
      "Status": "PASS"
    },
    {
      "ID": "V15",
      "Check": "no run in both partitions; 2013 = train; student flag recomputed",
      "Expected": "9 train, 13 test runs; 0 flag mismatches",
      "Observed": "{'train runs': 9, 'test runs': 13, 'test enrolments of students seen in 2013': 1962, 'flag mismatches': 0}",
      "Status": "PASS"
    }
  ],
  "extra": {
    "cma_score_coverage_training_rows": {
      "d13": 0.0138,
      "d27": 0.0525
    },
    "kpi_sensitivity": {
      "completion_day14": 0.5474,
      "enrolled_day14": 28061,
      "completion_without_138_flagged": 0.5493,
      "enrolled_without_flagged": 27962
    },
    "rule_rate_overall": {
      "d13": 0.2021,
      "d27": 0.2881
    },
    "rule_rate_cma_variant": {
      "d13": 0.2021,
      "d27": 0.4123
    },
    "runs_where_rule_exceeds_list_of_5_per_20": {
      "13": 7,
      "27": 10
    },
    "runs_where_rule_exceeds_list_of_3_per_20": {
      "13": 15,
      "27": 22
    },
    "rule_rate_by_run_range": {
      "13": [
        0.0838,
        0.4401
      ],
      "27": [
        0.1791,
        0.5476
      ]
    }
  },
  "all_pass": true
}

===== reports/milestone-3/package/data/metadata/validation_summary.md @ 19d35a4 =====
# Validation summary (Task 8)

Written by `src/validate_prepared.py` at 2026-11-06T15:24:17Z. Each check names its expected and observed value.

| ID | Check | Expected | Observed | Status |
| :---- | :---- | :---- | :---- | :---- |
| V01a | enrolment rows and outcome mix equal raw studentInfo | 32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)] | 32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)] | PASS |
| V01b | students | 28,785 | 28,785 | PASS |
| V01c | population sizes equal the profile (C09) | {'d14': 28061, 'd13': 28069, 'd27': 27535} | {'d14': 28061, 'd13': 28069, 'd27': 27535} | PASS |
| V01d | non-completion count per feature view equals the profile | {'d13': 12708, 'd27': 12156} | {'d13': 12708, 'd27': 12156} | PASS |
| V02 | missing values after = before (no imputation in views) | {'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173} | {'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173} | PASS |
| V03 | key unique in every view | 0 duplicates | {'enrolment': 0, 'assessment_due': 0, 'student_week': 0, 'features_d13': 0, 'features_d27': 0, 'capacity_by_run': 0} | PASS |
| V04a | enrolment clicks + clicks after withdrawal = raw clicks | 39,605,099 | 39,506,354 + 98,745 = 39,605,099 | PASS |
| V04b | student_week clicks = enrolment clicks | 39,506,354 | 39,506,354 | PASS |
| V04c | de-duplicated total ≤ raw total | dedup ≤ raw | 38,247,422 ≤ 39,506,354 | PASS |
| V05 | every category in its expected set | no other label | {'imd_band': [], 'age_band': [], 'highest_education': [], 'final_result': [], 'start_month': [], 'split': []} | PASS |
| V06 | banked results carry no lateness and no missed status | 0 | 0 | PASS |
| V07 | ranges after = before (no capping) | score [0, 100]; credits [30, 655] | {'score': [0.0, 100.0], 'studied_credits': [30, 655]} | PASS |
| V08 | no student_week row after the withdrawal week | 0 | 0 | PASS |
| V09 | every logged join kept its rows | 25 joins, rows in = rows out | 25 | PASS |
| V10 | enrolments without any click row kept with 0 clicks | ≥ 3,365 | 3,554 | PASS |
| V11-d13 | 6 features recomputed from raw for all 28,069 rows (independent code) | 0 mismatches | {'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0} | PASS |
| V13-d13 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 26,755 rows with later clicks; no forbidden column | 26,755 rows differ; forbidden [] | PASS |
| V11-d27 | 6 features recomputed from raw for all 27,535 rows (independent code) | 0 mismatches | {'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0} | PASS |
| V13-d27 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 25,663 rows with later clicks; no forbidden column | 25,663 rows differ; forbidden [] | PASS |
| V12 | transform parameters identical with and without test rows, equal to the stored ones | identical | d13: identical, d27: identical | PASS |
| V14 | every column documented; predictor lists hold no audit, target or descriptive column | none | {'undocumented': [], 'wrong role': []} | PASS |
| V15 | no run in both partitions; 2013 = train; student flag recomputed | 9 train, 13 test runs; 0 flag mismatches | {'train runs': 9, 'test runs': 13, 'test enrolments of students seen in 2013': 1962, 'flag mismatches': 0} | PASS |

## Reports for the analysis plan

- cma_score_coverage_training_rows: {"d13": 0.0138, "d27": 0.0525}
- kpi_sensitivity: {"completion_day14": 0.5474, "enrolled_day14": 28061, "completion_without_138_flagged": 0.5493, "enrolled_without_flagged": 27962}
- rule_rate_overall: {"d13": 0.2021, "d27": 0.2881}
- rule_rate_cma_variant: {"d13": 0.2021, "d27": 0.4123}
- runs_where_rule_exceeds_list_of_5_per_20: {"13": 7, "27": 10}
- runs_where_rule_exceeds_list_of_3_per_20: {"13": 15, "27": 22}
- rule_rate_by_run_range: {"13": [0.0838, 0.4401], "27": [0.1791, 0.5476]}

Rule firing rates per run and cut-off (no outcome used): `rule_rates.csv`. Five training-run rows per cut-off (two with a missed task, two with a late task where the cut-off has one, one at random) recomputed from raw rows: `manual_check_d13.csv`, `manual_check_d27.csv`.

===== reports/milestone-3/package/data/metadata/version_manifest.json @ 19d35a4 =====
{
  "prepared_dataset_version": "OULAD-N04-prepared-1.0",
  "created": "2026-11-06T15:24:17Z",
  "raw_input": {
    "assessments.csv": "8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1",
    "courses.csv": "4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75",
    "studentAssessment.csv": "fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e",
    "studentInfo.csv": "7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6",
    "studentRegistration.csv": "0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170",
    "studentVle.csv": "52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0",
    "vle.csv": "d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9"
  },
  "raw_source": "OULAD, figshare DOI 10.6084/m9.figshare.5081998.v1 (Milestone 2 package, SHA-256 pinned)",
  "code": {
    "01_understand.py": "2cab4e60c74ef67124dfac4520631d49dafbfbc1579675a95193cf521cb1bcff",
    "02_profile.py": "754600bced6306212b22308ba78a104fe99523a43713aefce24ac0e0e48d4a87",
    "build_notebooks.py": "bec46a98aa65919781552c949cba41da41077e9aa89385ccd93d3151541328a7",
    "common.py": "e7db87de4e3faaefb35dd4c0951fcc4e9e9cee897053f0d6f6b1ba6f8c5108af",
    "dictionary.py": "39cc3345a6d9b7876ea7ab741337f7ce11bd247542ba8540d2d8a6ad79fe9b68",
    "fit_transforms.py": "60d3ba2aa27e61e7fd733de09d6d1f478c06041dfd0b793672f4e7843644fdf9",
    "link_raw.py": "56898bc7e8afaf35068f583cad42e84bfb7fd959887a1aa22283c835fa5bfa24",
    "prepare_data.py": "61cba9249112695afadc8751dfc3a505efb5d6ca486b0fa0d0c70399569b3bc1",
    "validate_prepared.py": "d7bb8ea556e30eeb6c8d1a322e076545defac119329ed971380409fd340c18a7"
  },
  "git_commit": "41299c12ce9c81775d52e0837e5115710553ba84",
  "package_has_uncommitted_changes": true,
  "python": "3.12.7",
  "polars": "2.1.0",
  "outputs": {
    "assessment_due.parquet": {
      "sha256": "f67d7916dd95c2ab2321140b277a554145163b59e8d99f68b13d2d6c415cb498",
      "rows": 286898
    },
    "capacity_by_run.parquet": {
      "sha256": "38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08",
      "rows": 44
    },
    "enrolment.parquet": {
      "sha256": "1d1e397ac67ce774fec8be5d23bbf988ab70eb11f1bda5efc3d2f05510900a78",
      "rows": 32593
    },
    "features_d13.parquet": {
      "sha256": "c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6",
      "rows": 28069
    },
    "features_d27.parquet": {
      "sha256": "4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347",
      "rows": 27535
    },
    "model_ready_d13.parquet": {
      "sha256": "773d1e2fa077356483cd281a93f6efcb88fd8156b1c7d0874afdb0c0d22cb72f",
      "rows": 28069
    },
    "model_ready_d27.parquet": {
      "sha256": "3560a51594d4ad97102089a790d6aa74cd29fced6b5dc21b9222c3b53bc23c6b",
      "rows": 27535
    },
    "student_week.parquet": {
      "sha256": "7526872e26e95da74441de8a5b5e72e86c485bb0d09b5866af90d0ceda11e079",
      "rows": 1052344
    }
  }
}
