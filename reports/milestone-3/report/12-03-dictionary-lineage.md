## Appendix III – Prepared Data Dictionary and Lineage

Table A.11 links each analytics level to its prepared view, population and grain, with the check the brief sets before Milestone 4 and its result.

**Table A.11. Prepared views by analytics level**

| Level | Prepared view | Population | Grain | Check before Milestone 4 | Result |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Descriptive | enrolment, assessment_due, student_week | 32,593 enrolments; KPI on 28,061 | enrolment; enrolment × task; enrolment × week | No double counting, no join bias | Keys unique; joins kept rows; clicks reconcile |
| Diagnostic | features_d27 + enrolment | 27,535 enrolled at day 27 | enrolment | Associations from real data with comparison groups | Signs up to day 27; seven modules for within-module comparison |
| Predictive | features_d13, features_d27, model_ready | 28,069 and 27,535 | enrolment | Target, prediction point, pre-point features, split, enough of each class | Smaller class ≥ 92 per run; 9 training and 13 test runs; train-only transforms |
| Prescriptive | capacity_by_run | 44 run × cut-off rows | run × cut-off | Action, constraint, cost and outcome data | Assumed capacities only; no contact or outcome data |

The data dictionary (`data/metadata/data_dictionary.md`) lists every column of every view with its type, role, source, transformation and sensitivity. Table A.12 is the lineage table of brief section 13.1, one row per prepared variable other than the keys; the six sensitive variables are marked in the purpose column.

**Table A.12. Data lineage**

| Prepared variable | Source file / field | Transformation | Window / filter | Purpose / AQ |
| :---- | :---- | :---- | :---- | :---- |
| year | code_presentation | first four characters | – | time split |
| split | code_presentation | train if 2013, test if 2014 | run level | AQ3 time split (C07) |
| paired_run | courses | module and start month ran in both years | run level | AQ3 evaluation subsets |
| student_in_training_runs | studentInfo.id_student | test enrolment of a student with a 2013 enrolment | – | AQ3 strict unseen-student check |
| eval_withdrawal_day_unknown | final_result, date_unregistration | Withdrawn without a withdrawal day | – | AQ3: report test metrics with and without these rows (audit F1) |
| final_result | studentInfo.final_result | as recorded | observed at run end | AQ1 outcome |
| non_completion | studentInfo.final_result | Fail or Withdrawn | observed at run end | AQ1–AQ3 target |
| completed | studentInfo.final_result | Pass or Distinction | observed at run end | primary KPI |
| withdrawal_day_missing | final_result, date_unregistration | Withdrawn without a day | – | DQ04 flag |
| unregistered_not_withdrawn | final_result, date_unregistration | not Withdrawn but a day recorded | – | DQ04 flag |
| unregistered_after_run_end | date_unregistration, courses | day after run length | – | DQ06 flag |
| date_registration | studentRegistration.date_registration | as recorded | day offset | populations |
| date_unregistration | studentRegistration.date_unregistration | as recorded | day offset; after the cut-offs for feature rows | populations, withdrawal timing (AQ1) |
| enrolled_d13 | registration days | enrolled_at(13) | day 13 | AQ3 population (C09) |
| enrolled_d14 | registration days | enrolled_at(14) | day 14 | primary KPI denominator (C09) |
| enrolled_d27 | registration days | enrolled_at(27) | day 27 | AQ3 population (C09) |
| start_month | code_presentation | last character: B = February, J = October | – | AQ1 dimension; AQ3 predictor |
| run_length | courses.module_presentation_length | renamed | – | run end |
| gender | studentInfo.gender | as recorded | – | AQ3–AQ4 fairness audit (sensitive) |
| region | studentInfo.region | as recorded | – | fairness audit; explains imd_band Missing (sensitive) |
| age_band | studentInfo.age_band | as recorded (ordered 0-35, 35-55, 55<=) | – | fairness audit (sensitive) |
| disability | studentInfo.disability | as recorded (Y/N) | – | AQ4 fairness limit (C04) (sensitive) |
| imd_band | studentInfo.imd_band | '10-20' → '10-20%'; missing → 'Missing' | – | AQ4 fairness limit (C04) (sensitive) |
| highest_education | studentInfo.highest_education | ordered; ordinal code in model_ready | known at enrolment | AQ2–AQ3 (sensitive) |
| num_of_prev_attempts | studentInfo.num_of_prev_attempts | as recorded | known at enrolment | AQ3 |
| studied_credits | studentInfo.studied_credits | as recorded; outliers kept | known at enrolment | AQ3 (study load) |
| registration_lead | studentRegistration.date_registration | −date_registration | known at registration | AQ2–AQ3 |
| registration_missing | studentRegistration.date_registration | registration day missing | known at registration | AQ3 extended (39 of 45 are Withdrawn) |
| banked_results | studentAssessment.is_banked | count of banked results | known at registration | AQ3 |
| concurrent_runs | studentInfo | other enrolments of the student in the same presentation | – | AQ2 (2014 only, C12) |
| first_missed_week | assessment_due | week of earliest TMA/CMA not submitted and due while enrolled | whole run | AQ1 |
| tasks_due_while_enrolled | assessment_due | count, banked excluded | whole run | AQ1–AQ2 |
| tasks_missed_while_enrolled | assessment_due | count not submitted | whole run | AQ1–AQ2 |
| tasks_late_while_enrolled | assessment_due | count submitted after the due day | whole run | AQ2 |
| total_clicks | studentVle.sum_click | sum of all rows | whole run, up to the unregistration day | AQ1–AQ2 |
| total_clicks_dedup | studentVle.sum_click | sum with exact duplicate rows once | as total_clicks | DQ01 sensitivity |
| active_days | studentVle.date | distinct days with a click | whole run (student_week: within the week), up to the unregistration day | AQ1–AQ2 |
| assessment_type | assessments.assessment_type | TMA or CMA (exams excluded) | – | AQ1–AQ2 |
| due_day | assessments.date | renamed | day offset | AQ1–AQ2 |
| due_week | assessments.date | floor(due / 7) + 1 | – | AQ1 |
| weight | assessments.weight | as recorded; not used for grades | – | DQ09 |
| date_submitted | studentAssessment.date_submitted | as recorded; null if not submitted | whole run | AQ1–AQ2 |
| is_banked | studentAssessment.is_banked | as recorded | – | DQ07 |
| score | studentAssessment.score | as recorded; not a feature except via cma_score_mean_c | whole run | AQ2 |
| status | date_submitted, due day, is_banked | banked / not_submitted / on_time / late | whole run | AQ1–AQ2 |
| lateness_days | date_submitted, due day | submitted − due (non-banked) | whole run | AQ2 |
| due_while_enrolled | due day, registration days | registered by due day and unregistered after it | whole run | AQ1 (missed only if due while enrolled) |
| clicks | studentVle.sum_click | sum per week | week, up to the unregistration day | AQ1–AQ2 |
| clicks_dedup | studentVle.sum_click | weekly sum, exact duplicates once | week | DQ01 sensitivity |
| records | studentVle | number of log rows | week | DQ02 |
| sites | studentVle.id_site | distinct resources | week | AQ2 |
| logging_gap | studentVle.date | week holds a day with no click in the whole run | week | DQ15 |
| clicks_pre | studentVle.sum_click, date | sum | days before 0 | AQ2–AQ3 |
| clicks_pre14 | studentVle.sum_click, date | sum | days −14 to −1 | AQ3 |
| clicks_0c | studentVle.sum_click, date | sum (= sum of clicks_w*) | days 0 to c | AQ2–AQ3 |
| clicks_0c_dedup | studentVle | sum, exact duplicate rows once | days 0 to c | DQ01 sensitivity |
| active_days_0c | studentVle.date | distinct days with a click | days 0 to c | AQ2–AQ3 |
| sites_0c | studentVle.id_site | distinct resources | days 0 to c | AQ3 |
| inactive_last7 | studentVle | no click in days c−6 to c | last seven days | AQ2–AQ3; rule part |
| activity_ratio_run | studentVle | (clicks_0c + 1) ÷ (run median of clicks_0c + 1) | same run, days 0 to c, enrolled at c | AQ2 sign against the course average |
| tasks_due_c | assessments.date | TMA/CMA due by c and on or after the registration day | due ≤ c | AQ2–AQ3 |
| tasks_missed_c | studentAssessment | due ≤ c, no non-banked submission by c | submissions ≤ c | AQ2–AQ3; rule part |
| tasks_late_c | studentAssessment | due ≤ c, submitted after due and by c | submissions ≤ c | AQ2–AQ3 |
| tma_late_c | studentAssessment | late TMA by c | submissions ≤ c | AQ2–AQ3; rule part |
| cma_late_c | studentAssessment | late CMA by c | submissions ≤ c | AQ2–AQ3; rule variant |
| cma_marked_c | studentAssessment | CMA marks known by c | submitted ≤ c − 7 | AQ3 (coverage of the CMA score) |
| cma_score_mean_c | studentAssessment.score | mean of known CMA marks; null if none | submitted ≤ c − 7 | AQ3 |
| days_since_last_click | studentVle.date | c − last active day; c + 1 if no click in 0…c | days 0 to c | AQ3 |
| trend_last_week | studentVle | last week's clicks − previous week's | weeks up to c | AQ3 |
| tasks_submitted_early_c | studentAssessment | tasks due after c submitted by c | submissions ≤ c | AQ3 |
| clicks_oucontent_0c | studentVle, vle.activity_type | sum on content pages | days 0 to c | AQ2–AQ3 |
| clicks_forumng_0c | studentVle, vle.activity_type | sum on forums | days 0 to c | AQ2–AQ3 |
| clicks_quiz_0c | studentVle, vle.activity_type | sum on quizzes | days 0 to c | AQ2–AQ3 |
| clicks_homepage_0c | studentVle, vle.activity_type | sum on the homepage | days 0 to c | AQ2–AQ3 |
| early_sign_rule | derived | rule_missed or rule_tma_late or inactive_last7 | at c | AQ3 comparison rule; secondary KPI 1 (C10) |
| early_sign_rule_cma | derived | early_sign_rule or cma_late_c ≥ 1 | at c | sensitivity variant |
| rule_missed | derived | tasks_missed_c ≥ 1 | at c | rule part |
| rule_tma_late | derived | tma_late_c ≥ 1 | at c | rule part |
| enrolled | features views | count enrolled at the cut-off | run, cut-off | AQ4 |
| tutor_groups_est | enrolled | ceil(enrolled / 20) | run, cut-off | AQ4 (assumed group of 20) |
| list_tutor_3 | tutor_groups_est | 3 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity |
| list_tutor_5 | tutor_groups_est | 5 × groups (≤ enrolled) | run, cut-off | AQ4 assumed capacity |
| list_office_30 | enrolled | min(30, enrolled) | run, cut-off | AQ4 assumed capacity |
| list_office_40 | enrolled | min(40, enrolled) | run, cut-off | AQ4 assumed capacity |
| clicks_w1 | studentVle | sum per week | week 1 (days 0–6) | AQ3 weekly trajectory |
| clicks_w2 | studentVle | sum per week | week 2 (days 7–13) | AQ3 weekly trajectory |
| clicks_w3 | studentVle | sum per week | week 3 (days 14–20) | AQ3 weekly trajectory |
| clicks_w4 | studentVle | sum per week | week 4 (days 21–27) | AQ3 weekly trajectory |

**Main derived variables.** Table A.13 defines the main derived variables of Section 6.2 with their formula, source
fields and timing rule; c stands for the cut-off day, 13 or 27.

**Table A.13. Main derived variables**

| Variable | Formula | Source fields | Window / timing rule |
| :---- | :---- | :---- | :---- |
| non_completion (target) | final_result is Fail or Withdrawn | studentInfo | Observed at the run end; never a feature |
| enrolled_d13, enrolled_d14, enrolled_d27 | Registered by day d, or registration day unknown, and not unregistered by day d | studentRegistration | Day d (C09) |
| clicks_pre | Clicks before day 0 | studentVle | Before the start |
| clicks_0c, active_days_0c | Clicks, and days with at least one click, from day 0 to c | studentVle | Days 0 to c |
| activity_ratio_run | (clicks_0c + 1) ÷ (median clicks_0c of the run's enrolled students + 1) | studentVle | Same run, days 0 to c; no outcome used |
| inactive_last7 | No click on days c − 6 to c | studentVle | Seven days ending at c |
| tasks_missed_c | TMA or CMA due by c, due on or after the registration day, not submitted by c | assessments, studentAssessment | Submissions up to c; banked results excluded |
| tma_late_c, cma_late_c | Tasks due by c submitted after the due day but by c, by type | assessments, studentAssessment | Submissions up to c |
| cma_score_mean_c | Mean score of CMAs submitted by c − 7; empty if none | studentAssessment | Marks known by c; prepared, not a predictor (Section 7.3) |
| early_sign_rule | A task missed, or a TMA late, or inactive in the last seven days | derived | At c (C10) |
| early_sign_rule_cma | early_sign_rule, or a CMA late | derived | At c; sensitivity variant |
| first_missed_week | Week of the earliest task not submitted that fell due while the student was enrolled | assessment_due view | Whole run (AQ1 only) |

**Feature choices and predictor sets.**

Two of these definitions carry a choice. A task counts as missed only if it fell due on or after the student's
registration day, because a student who registers late cannot have missed a task that fell due before they joined.
The activity ratio compares a student with the median of the same run up to the same day, which stands for the "course
average" of the AQ2 sign; it adds one to both counts so that a run or a student with no clicks gives a defined value,
and it uses no outcome, so staff could compute it on the day of the cut-off.

**Predictor sets.** The feature views hold 20 primary predictors and 10 extended predictors, plus the weekly click
counts up to the cut-off, two at day 13 and four at day 27; every other column is an identifier, the target, a flag
for evaluation, the rule or an audit attribute. The primary set covers the module and start month, prior education,
previous attempts, study load, how early the student registered, banked results, activity before and after the start,
the activity ratio, inactivity, and the task counts and lateness. The extended set holds ten predictors for comparison in
Milestone 4: the registration-missing indicator, the de-duplicated clicks, the clicks in the 14 days before the start,
the days since the last click, the trend over the last week, the tasks submitted early, and the clicks on content
pages, forums, quizzes and the home page. The CMA score falls below the coverage that a predictor needs, as Section 7.3 explains.
Demographic attributes serve mainly the fairness audit, because earlier experiments at the OU found that adding them
to activity and assessment data did not significantly improve the prediction of students at risk [9]; Table A.12 gives
every prepared variable with its source and purpose.
