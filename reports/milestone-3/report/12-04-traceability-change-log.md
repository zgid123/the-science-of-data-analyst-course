## Appendix IV – Updated Traceability and Controlled Change Log

Table A.14 is the updated traceability of deliverable B: each row runs from the goal and KPI through the question and its analytics type to the raw variables, the preparation, the prepared variables and the decision supported.

**Table A.14. Updated traceability**

| Business Goal / SMART / KPI | AQ | Analytics type | Raw variables | Preparation | Prepared variables / view | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Primary KPI: completion rate of students enrolled after the add-drop period (day 14; SMART assumed 70% → 75%) | AQ1 | Descriptive | studentInfo.final_result; studentRegistration.date_registration, date_unregistration; assessments.date; studentAssessment.date_submitted, is_banked | Enrolled-at-day rule (C09); tasks = TMA and CMA; banked results separated; missed only if due while enrolled | `enrolment`: completed, non_completion, enrolled_d14, first_missed_week, code_module, code_presentation, start_month, year; `assessment_due`: status, due_week | D2 where advisors' time goes; D3 extend after the pilot |
| Primary KPI; secondary KPI 1, sign part (early-sign rule, C10) | AQ2 | Diagnostic | + studentVle.date, sum_click, id_site; vle.activity_type | Clicks aggregated by enrolment × day (DQ02), truncated at withdrawal (DQ03), all rows kept with a de-duplicated twin (DQ01); signs up to day 27 | `features_d27`: tasks_missed_c, tasks_late_c, tma_late_c, cma_late_c, inactive_last7, activity_ratio_run, clicks_*_0c; `enrolment`: concurrent_runs (2014) | D2; the reasons shown with D1 lists |
| Secondary KPI 1, sign part | AQ3 | Predictive | as AQ2 + num_of_prev_attempts, studied_credits, highest_education, date_registration, is_banked, score (CMA) | Populations at days 13 and 27; events ≤ cut-off only; CMA marks known at c − 7; time split; transforms fitted on 2013 runs | `features_d13`, `features_d27` (20 primary, 10 extended predictors, weekly clicks), `early_sign_rule`, `split`, `paired_run`, `student_in_training_runs`; `model_ready_d13/d27` | D1 who is listed in weeks 3 and 5 |
| Secondary KPI 2 (follow-up rate) and secondary KPI 1, contact part: pilot only (C08) | AQ4 | Prescriptive (ranking; AQ4 rewritten, C11) | AQ3 inputs; gender, age_band, disability, imd_band, region as audit columns | Capacity scenarios from tutor groups of about 20; list quality as lift and attainable recall (C13); fairness by imd_band ("Missing" apart) and disability | `capacity_by_run`: enrolled, list_tutor_3, list_tutor_5, list_office_30, list_office_40; audit columns in the feature views | D1 ordered list within capacity; contact choice deferred |

Table A.15 is the Controlled Change Log of deliverable E: C01–C08 from Milestone 2 and C09–C13 from the data understanding of Milestone 3 (column M), each with its evidence and effect.

**Table A.15. Controlled Change Log**

| ID | M | Old content | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
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

**Reasoning behind each fit rating.** The paragraphs below explain, question by question, the ratings of the AQ–Data
Fit Decision Log (Table 4.1) and the changes C09 to C13 that follow from them.

**AQ1, descriptive.** OULAD records the final result of every enrolment and the due day of every task, so completion
rates by module, run, start month and year can be computed, and the week of the first missed task can be derived
from due days and submissions. The question is YELLOW rather than GREEN because two of its comparisons, by year of
study and by delivery mode, have no field in OULAD, and because exam results are missing in five modules, so the
first missed task is taken over TMA and CMA only. In addition, the population of the rates is restated: an enrolment
counts as enrolled on a given day when the student registered by that day, or the registration day is unknown, and
did not unregister by it. This rule (C09) adds the registration condition to the Milestone 2 definition, which counted
every enrolment still registered on day 14 (28,119); it removes the 58 students who registered after day 14 and leaves
28,061 enrolments in the KPI population, and the same rule gives the populations at both cut-offs.

**AQ2, diagnostic.** Each sign of AQ2 can be derived from the click and submission records with a stated formula and
window. Two parts of the question narrow. Task signs exist only in the 16 runs where a task falls due by day 27.
The sign "tasks missed in several modules at once" needs students enrolled in two runs at the same time, and of the
1,382 such enrolments at day 14, only 12 fall in the 2013 runs; the sign is therefore described for the 2014 runs
only and does not enter the predictive features, which are learned on 2013 (C12). AQ2 measures association, not
cause, and the attendance sign of Milestone 1 has no counterpart in distance learning.

**AQ3, predictive.** The target exists for every enrolment, the populations at both cut-offs are large, and nine
module and start-month pairs ran in both years, so a model built on 2013 can be tested on 2014. The comparison rule is
the weak part. In Milestone 1, the early-sign rule reads "two or more assessed tasks missed or late by the end of week
4"; two tasks fall due by day 27 in only one run, so Milestone 2 counted one missed or late task (C06), but even that
form cannot fire in the 6 runs without a task due by day 27 or in 21 runs at day 13. The meaning of a late CMA in
2013–2014 is also undocumented (DQ10). The rule is therefore restated (C10): a student shows early signs when a task
due by the cut-off has not been submitted, or a TMA has been submitted late, or the student has had no platform
activity in the seven days before the cut-off. The rule can now fire in every run, and the CMA-lateness version is kept
only as a sensitivity variant. Scores, in turn, enter only where the mark is known by the cut-off, which holds for CMA
marks submitted at least seven days earlier and never for TMA marks.

**AQ4, prescriptive.** AQ4 asks whom to list, in what order and with which contact, within capacity. OULAD records no
contact, no type of contact, no staff capacity and no outcome after a contact, and none of the seven candidate datasets
of Milestone 2 records them either, so the question is RED. Following the brief's order, it is rewritten to the part
the data support: under an assumed weekly capacity, which enrolments rank first at each cut-off, and what recall, the
share of later non-completers who appear on the list, and what precision, the share of listed students who later fail
or withdraw, the list reaches overall and by deprivation band and disability (C11). The choice of contact and its effect
are deferred to the pilot, where the contact record will exist. In addition, the Milestone 1 limit of at least 50%
precision says little when 44–45% of students do not
complete, since a random list already reaches about 45%. List quality is therefore measured as lift, the precision of
the list divided by the run's rate of non-completion, and as recall against the most that a list of the same length
can reach, with a random list and the early-sign rule as baselines (C13).

**Changes C09 to C13 in full.** Five changes follow from these ratings, and each narrows how a question is measured without changing what it asks.
The population rule (C09) counts an enrolment as enrolled on a given day when the student registered by that day, or
the registration day is unknown, and did not unregister by it; it removes the 58 late registrants from the Milestone 2
count of 28,119, which took every enrolment still registered on day 14, and leaves 28,061 enrolments in the KPI population.

The sign "tasks missed in several modules at once" is described for the 2014 runs only, because only 12 of the 1,382 concurrent enrolments fall in the 2013 training
runs (C12).

The early-sign rule counts one missed or late task on OULAD (C06), but no task falls due by day 27 in 6 runs or
by day 13 in 21, so in those runs it can flag no one; it therefore becomes "a task due by the cut-off not submitted, or a TMA submitted late, or no platform
activity in the seven days before the cut-off" (C10), whose inactivity part can flag students in every run.

AQ4 is rated RED because its contact part has no data
at all; it is rewritten to its ranking part, which rests on AQ3, and the choice of contact
is deferred to the pilot, because no dataset records contacts (C11).

Finally, the Milestone 1 limit of 50% precision,
the share of listed students who later fail or withdraw, says little when 44–45% of students do not complete, since a random list already reaches about 45%, so a
list is judged by its lift, its precision divided by the run's rate of non-completion, and by its recall, the share of
later non-completers it reaches, against the most a list of its length can reach (C13).

**Baseline in full.** The paragraphs below give the goal, the measures and the decisions of the baseline that
Section 1.1 summarises.

**Goal and measures.** The Business Goal is to improve successful course completion in a university program's online
and blended courses by identifying students who stop taking part early enough to support them within the semester.
The SMART Goal turns this into a target: the completion
rate of students enrolled after the add-drop period, the first weeks in which students may still register for or
drop a course, rises in the pilot courses from a baseline that the pilot will recount from the university's records,
assumed for now to be 70%, by five percentage points to 75% by the end of the 2027–2028 academic year. Completion means passing the course; a fail or a withdrawal counts as
non-completion.

Three KPIs track the goal. The primary KPI is the course completion rate itself. The
first secondary KPI, the early-sign contact rate, is the share of students showing early signs of disengagement who
are contacted by the end of week 5; the early signs are defined by the early-sign rule, which in Milestone 1 reads
"two or more assessed tasks missed or submitted late by the end of week 4". The second secondary KPI, the follow-up
rate, is the share of students on a contact list who are contacted within seven days of the list reaching staff.
Both secondary KPIs rely on a contact record, a shared log of who contacted which student, when and with what result,
which the university does not keep yet.

**Decisions.** The proposal supports three decisions. D1 is whom the lecturer-advisors and the support office contact
at each review point, a moment in weeks 3 and 5 of the semester when a contact list reaches staff; each list uses the
data up to its data cut-off, the end of week 2 for the week-3 list and the end of week 4 for the week-5 list,
because data exports take about a week. D2 is where the program manager places the time of the support office and
the lecturer-advisors each semester, and D3 is whether to extend the approach to all courses after the pilot.

**Changes from Milestone 2 in full.** Milestone 2 selected OULAD as an open
stand-in for the university's own records, which cannot be used yet, and recorded eight changes, C01 to C08, in the
Controlled Change Log, the list of every change to the baseline with its reason in the data. The population became
the OULAD module runs of 2013–2014, the courses of a distance-learning university in the UK, in place of
the program's courses (C01). Time became a count of days from the start of each run, which places the two data
cut-offs at day 13 and day 27 (C02). The KPI denominator became the enrolments still registered on day 14 (C03).
Comparisons by delivery mode and year of study became comparisons by module and run, since OULAD records neither
(C04), and the attendance sign was dropped because distance learning has no classes to attend (C05). The week-3 list
rests on activity alone, because a task falls due by day 13 in only one run, and on OULAD the early-sign rule counts
one missed or late task rather than two (C06). The predictive question is trained on the 2013 runs and tested on the
2014 runs (C07), and the choice of contact and its outcome remain a requirement for the pilot, because OULAD records
no contact (C08).

**Synthetic-data policy in full.**

The brief allows synthetic data at five levels with different conditions: small test data for
code (level A) and simulation to illustrate a method (level B) are allowed; augmentation of training data (level C)
needs the lecturer's approval; and synthetic data that fill a missing concept, label or intervention (level D) or that
enter descriptive or diagnostic evidence (level E) are not allowed [1]. This project uses level A only: a few
hand-made test enrolments, labelled as synthetic in the `tests/` folder of the Prepared Data Package, check that each
feature formula gives the expected value. They never enter a prepared view, a statistic or a finding, and no
augmentation is planned.
