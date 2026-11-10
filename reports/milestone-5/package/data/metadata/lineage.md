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
