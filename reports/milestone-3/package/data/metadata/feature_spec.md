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
