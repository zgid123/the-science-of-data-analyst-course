# Requirement coverage, traceability and Change Log (T12, Task 7)

Inputs: requirements (`requirements/data-requirements.md`), structural results (`package/metadata/structure_results.json`,
`logs/T11_structure.log`), selection (`selection/selection.md`). Every variable below exists in the collected files.

## 1. Facts from the structural verification that decide coverage

| Fact | Value | Source |
| :---- | :---- | :---- |
| Result values | Pass 12,361; Withdrawn 10,156; Fail 7,052; Distinction 3,024 | structure_results.json `final_result_values` |
| Dated withdrawal | 10,063 of 10,156 Withdrawn carry `date_unregistration`; 93 do not; 9 non-Withdrawn carry one | `withdrawn_with_date`, `withdrawn_without_date`, `date_but_not_withdrawn` |
| Identifier across runs | 3,538 of 28,785 students in more than one run; 1,309 of 1,309 same-module repeats raise `num_of_prev_attempts` | `students_in_more_than_one_run`, `repeats_with_higher_attempt_counter` |
| Runs per module | BBB, DDD, FFF 4; EEE, GGG 3; AAA, CCC 2 | `runs_per_module_all` |
| Earlier and later run of the same module and start month (B or J) | 9 pairs: AAA-J, BBB-B, BBB-J, DDD-B, DDD-J, EEE-J, FFF-B, FFF-J, GGG-J; CCC, EEE-B and GGG-B have only a 2014 run | `runs_per_module` |
| First non-exam task due day | 12–61 (median 21.5); due by day 13 in 1 of 22 runs; by day 27 in 16 of 22 | `first_task_due_day` |
| Denominator | 28,119 enrolments still registered at day 14; 3,097 unregistered on or before day 0; 58 registered after day 14; 45 without a registration day | `still_registered_at_day_14` etc. |
| Links | 0 assessment, submission, click or site rows without a parent | `*_without_*` |

## 2. Updated traceability matrix (brief section 11)

| AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Gap / action |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Pass / fail / withdrawal per enrolment by course, mode, year of study, four semesters; week of first missed task for both groups | OULAD: studentInfo.csv, studentRegistration.csv, courses.csv, assessments.csv, studentAssessment.csv | `code_module`, `code_presentation`, `id_student`, `final_result`, `date_registration`, `date_unregistration`, `module_presentation_length`, `id_assessment`, `assessment_type`, `date`, `date_submitted` | Partial | Course (module), run and timing covered; four runs for BBB, DDD, FFF only; delivery mode and year of study absent – comparisons by them dropped (C04) |
| AQ2 | Diagnostic | Weeks 1–4 signs: missed and late tasks, activity relative to course, tasks missed in several courses, attendance | OULAD: AQ1 files + studentVle.csv, vle.csv | AQ1 variables + `sum_click`, `date` (studentVle), `id_site`, `activity_type`; concurrent runs via `id_student` | Partial | Missed and late tasks only in runs with a task due by day 27 (16 of 22); attendance, delivery mode and year of study absent (C04, C05) |
| AQ3 | Predictive | Target fail or withdrawal; features recorded by day 13 and day 27; time-ordered runs; group comparison | OULAD: as AQ2 | Target from `final_result`; population from `date_registration`, `date_unregistration`; features from `studentVle.date` ≤ cut-off, `date_submitted` ≤ cut-off, `num_of_prev_attempts`, `studied_credits`; groups from `imd_band`, `disability` | Partial | Week-3 list (day-13 cut-off) uses activity only (C06); time-based test on the 9 module-start pairs, 2013 → 2014 (C07); first-year comparison replaced by groups the data hold (C04) |
| AQ4 | Prescriptive | Ranking under weekly capacity; contacts and their outcomes | OULAD: AQ3 outputs only | AQ3 estimates; capacity is a baseline assumption | Partial (ranking) / None (action and outcome) | List length and order can be simulated under assumed capacity; no contact record, so no claim about the effect of contact; contact data stay a future decision requirement for the pilot (C08) |

## 3. Full traceability (deliverable B)

| Business Goal / SMART Goal / KPI | AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completion rate in pilot courses, assumed 70% → 75% by end 2027–2028 (primary KPI) | AQ1 | Descriptive | Outcome by course and time; first missed task | studentInfo, studentRegistration, assessments, studentAssessment | final_result, date_unregistration, assessments.date, date_submitted | Partial | D2, D3 |
| Primary KPI; secondary KPI 1, early-sign contact rate (sign part) | AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | + studentVle, vle | sum_click, studentVle.date, date_submitted | Partial | D2; reasons in D1 |
| Secondary KPI 1 (sign part) | AQ3 | Predictive | Target and features by the cut-off; later run for testing | as AQ2 | as AQ2 + num_of_prev_attempts, studied_credits, imd_band, disability | Partial | D1 |
| Secondary KPI 2, follow-up rate; secondary KPI 1 (contact part) | AQ4 | Prescriptive | Ranking within capacity; contact record | AQ3 outputs | none for contacts | Partial / None | D1 |

## 4. Controlled Change Log (brief section 3.1)

| ID | Old content (Milestone 1) | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- |
| C01 | The program's online and blended courses at a Vietnamese university | OULAD module runs (UK Open University, distance learning, 2013–2014) as an open stand-in for the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses was found; OULAD is the only candidate passing the gates (selection.md) | All AQs answered on stand-in data; results describe OULAD and must be re-checked on the university's data before D1–D3 |
| C02 | Course and semester; weeks 1–5 of a semester (length not fixed in Milestone 1) | Module run (`code_presentation`), eight to nine months; days counted from day 0 of the run; week n = days 7(n−1) to 7n−1 | Dates in OULAD are days from the run start (C3-012); runs last 234–269 days | Cut-offs become day 13 (week-3 list) and day 27 (week-5 list); the semester-length difference is a stated limit |
| C03 | Denominator: students enrolled after the add-drop period; withdrawal as in Circular 83/2026 | Enrolments still registered at day 14 (registration closes two weeks after the start, C2-001); leave and transfer cannot be told apart | `date_registration`, `date_unregistration` exist; no status field for leave or transfer | Primary KPI computed as a proxy on 28,119 enrolments; deviation from the Circular 83 rule recorded |
| C04 | Comparisons by delivery mode and year of study; AQ4 limit on first-year against later-year recall | Comparisons by module and run; the fairness limit is checked across IMD band and disability | No delivery-mode or year-of-study field; all modules are distance learning | AQ1–AQ3 narrowed; AQ4 limit re-expressed on available groups |
| C05 | AQ2 sign: attendance at in-class sessions (blended courses) | Dropped | No in-class sessions or attendance in OULAD | AQ2 uses missed and late tasks, activity and concurrent runs |
| C06 | AQ3 week-3 list from assessment and activity signs | Week-3 list (day-13 cut-off) from activity only; assessment signs start with the week-5 list | A non-exam task is due by day 13 in 1 of 22 runs, by day 27 in 16 | Secondary KPI 1: two tasks fall due by day 27 in only 1 of 22 runs, so on OULAD its sign part counts one missed or late task in the 16 runs with a task due by day 27; the two-task rule stays for the university |
| C07 | AQ3 tested on a later semester of the same pilot courses | Train on 2013 runs, test on 2014 runs of the same module and start month (9 pairs); CCC, EEE-B and GGG-B only as later runs | B and J runs should be analysed separately (C4-001); each module has at most two runs of one start month | Time-based validation feasible but with one earlier run per pair |
| C08 | AQ4 action and outcome; secondary KPI 2 and the contact part of secondary KPI 1 measured from a contact record | Kept as a future decision requirement; AQ4 limited to ranking under assumed capacity | No contact, capacity or intervention data in any candidate | No prescriptive or causal claim; secondary KPI 1 (contact part) and secondary KPI 2 measured only in the pilot |
