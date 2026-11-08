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
