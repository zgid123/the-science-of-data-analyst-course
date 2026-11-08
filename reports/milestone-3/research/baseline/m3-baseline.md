# Frozen baseline for Milestone 3

Frozen 2026-11-07T17:58:22Z by `code/freeze_baseline.py`. The Milestone 1 elements, the Milestone 2 Controlled Change Log, the traceability matrix and the prediction-point table are copied verbatim; any later change goes into the Milestone 3 Change Log (C09 onwards).

## Inputs required by the brief (section 3)

| Input | File | Content | Status |
| :---- | :---- | :---- | :---- |
| Milestone 1 baseline | reports/milestone-2/research/baseline/m1-baseline.md | Business Goal, SMART Goal, KPIs, AQ1–AQ4, analytics types, decisions (frozen with SHA-256) | present |
| Updated Traceability Matrix | reports/milestone-2/report/11-05-change-log.md | Table A.10: KPI → AQ → requirement → file → actual variables → coverage → decision | present |
| Raw Data Package | reports/milestone-2/package/metadata/raw_manifest.csv | archive and seven CSVs, SHA-256 pinned; re-created by package/src/collect.py | present |
| Metadata / Data Dictionary | reports/milestone-2/package/metadata/data_dictionary.md | column definitions from the data descriptor; source.md holds license and citation | present |
| Collection Evidence | reports/milestone-2/package/metadata/source.md | DOI 10.6084/m9.figshare.5081998.v1, access date, version, checksums, collection log | present |
| Controlled Change Log | reports/milestone-2/report/11-05-change-log.md | C01–C08 with old and new content and data evidence | present |

## Milestone 1 files re-checked against the hashes pinned in Milestone 2 (Table A.8)

| File | SHA-256 now | State |
| :---- | :---- | :---- |
| 03-01-business-goal.md | f99753ab586754e3c6f416c34b669db647d93dc20920db59fb964c3aef0bab23 | unchanged |
| 03-02-smart-goal.md | d7b32a609f5b39a24630713b3ca631dca9328404e18a42e0737fa8311caa6087 | unchanged |
| 03-03-kpis.md | 7698548222c8f9431f16f36bb0a7f6ec5de11221e15b645f8f4d3f5391b8710a | unchanged |
| 04-01-four-level-questions.md | 300389d938bb7457192bf10790fffa432849c67460df2df379add184c9a05993 | unchanged |
| 05-00-analytic-approach.md | 98a36dc7d86271d00cd5e5432164e547e7d945f28880e3811c80d35e13439753 | unchanged |
| 06-01-data-requirements.md | 07d212a4cbaa800221a699bf91db387e7f27e59cac53522108bca7ad06293cf1 | unchanged |
| 07-00-decision-value.md | 19086def5d5cabde135c1ecd68e6d6223170d6908b3a0d9f068dd8fe65870e68 | unchanged |
| 09-00-traceability-matrix.md | d74c013921ccb95da9511facaf04b781499012a061d5cb71ae4724e5ec1cdd2d | unchanged |

## Milestone 2 files this baseline is copied from (SHA-256)

| File | SHA-256 |
| :---- | :---- |
| report/01-01-frozen-baseline.md | 88338348f8c78de123e54943c9fe2a2f1e263f0de01507e3545e0b444a7cade3 |
| report/02-03-prediction-point-leakage.md | 7f6bffe4d4f0ca39cef25def0a9682d3406e1d9504df8364c9df4bc609d338f4 |
| report/07-01-traceability.md | 11097857ace2a35a63a6117ce31a889cdc3b7f5e6f9eb42053a76dbdfe611f2b |
| report/07-02-gaps-revisions.md | fad557a2be80f6e00ccc1a33a973f41e901e4d8c3278a6ea2330c9af7129cfdd |
| report/11-05-change-log.md | 0882b4660838ca62afd52f2a337ae823e9cf0cae43aa519a91d72646f26950a2 |
| research/baseline/m1-baseline.md | 2783c8567130771dcdd10fe03798e356476d2c5878f536192b3ff47bf846f7c4 |
| research/requirements/data-requirements.md | 20b972f970fa69b46b6c84878342961adb5c96a8116d887c5d5d43e3f816117d |
| package/metadata/source.md | 88cfa7d4f048cd228696766b2d4ed3ac9917a15a4fd515ef5a8003c08add1be0 |
| package/metadata/data_dictionary.md | e101a04776e041279f246cbf9308b6c2afb19c706bf715778e0ae47e596c0f69 |
| package/metadata/raw_manifest.csv | 6097f6670b30ef3b186416dd68180a31af75729ca5f5a1e92ddd21642774f492 |
| package/metadata/structure_report.md | 5662d3c7c16ba606d4e2d41581d56e61b474974f4b1f1293e1aacfc962c9ac01 |

## Milestone 1 baseline (verbatim from Milestone 2)

### Business Goal

improve successful course completion in the program's online and blended courses
by identifying students who stop taking part early enough to support them within the semester

### SMART Goal

> **SMART Goal.** Raise the course completion rate of students enrolled after the add-drop period in the pilot
> courses from their recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by the end of
> the 2027–2028 academic year.

### KPIs

**Primary KPI: course completion rate.** The number of enrolments in the pilot courses that end in a pass, divided by
the number of enrolments after the add-drop period, pooled over the pilot courses. A fail and a withdrawal from the
course both count as non-completion. Approved leave and transfers to another program leave the denominator, as under
Circular 83/2026 [4]. This KPI is the SMART Goal's own measure and the outcome that the program already reports, so it
tracks the goal directly. It is read at the end of each semester from the academic management system.

**Secondary KPI 1: early-sign contact rate.** This KPI uses the early-sign rule, a simple and transparent definition
of a student who shows early signs of disengagement: a student who has missed two or more assessed tasks, or submitted
them late, by the end of week 4. The end of week 4 is the data cut-off of the week-5 review point: the last day whose
data may be used for that list, one week before it reaches staff, because exports from the LMS take about a week
(DO4). The KPI is the number of students meeting the rule who were contacted by
the end of week 5, divided by the number of students meeting the rule. It shows whether students who begin to
disengage are reached while support can still help, which is what the program manager and the lecturer asked for
(PM3, CL6), and it can be read in week 6, within the semester rather than after it. Students who meet the rule but are not on a
list, because capacity is full, count as not contacted, so a low value signals that capacity is too small rather than
that staff failed; the KPI is monitored without a target until the pilot shows what is achievable.

**Secondary KPI 2: follow-up rate.** The number of students on a contact list who were contacted within seven days of
the list being sent, divided by the number of students on the list. It shows whether the lists fit staff capacity and
are actually used. A list that staff cannot follow up is worse than no list, as the data officer warned (DO10), and a
list that is too long loses the support office's trust (AD10). The lecturer's wish to act on a short list every week
(CL11) is met only if this rate stays high. It is read one week after each review point. Appendix VII (Table A.19)
summarises the three KPIs with their timing and data sources.

### Analytical questions

**AQ1 – Descriptive.** In the program's online and blended courses over the four semesters of 2024–2025 and
2025–2026, what share of students enrolled after the add-drop period passed, failed or withdrew, by course, delivery
mode and year of study, and how does the week of the first missed assessed task compare between students who passed
and students who did not?

**AQ2 – Diagnostic.** Which signs observable in weeks 1–4 (missed or late quizzes and assignments, LMS activity
compared with the course's own average, missed tasks in several courses at once, and, in blended courses only,
attendance at in-class sessions) show the largest difference in later non-completion rates between students who have
the sign and students who do not, and are these differences similar across courses, delivery modes and years of
study?

**AQ3 – Predictive.** For each student enrolled in a pilot course, how well can failing or withdrawing by the end of
the semester be estimated from the data recorded by the end of week 2 and by the end of week 4, compared with a simple
rule such as "two or more assessed tasks missed"? Accuracy is measured on a list as long as staff can follow up each
week, as recall and precision, and is compared between first-year and later-year students and across courses.

**AQ4 – Prescriptive.** At each review point (weeks 3 and 5), which students should be listed, in what order, and with
which contact (a message from the lecturer or lecturer-advisor, a call from the support office, or a referral to the
student affairs office, which handles financial and personal matters, separate from the support office), so that the list reaches as many as possible of the
students most likely not to complete? The list must fit weekly capacity (three to five contacts per lecturer-advisor,
about 30–40 for the support office), reach a precision of at least 50%, and keep first-year recall within ten points
of later-year recall.

### Analytics types and technique families

**Table 5.1. Analytics type, candidate technique family and expected output per question**

| AQ | Analytics type | Candidate technique family | Expected output | Main user |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Rates, distributions, segmentation by course and group, trends over semesters; repeated after the pilot for pilot and comparison courses | A profile of completion by course and student group; a timeline of when non-completers first miss a task | Program manager |
| AQ2 | Diagnostic | Group comparison, association measures and statistical tests, explanatory regression, comparison of cohorts | Early signs ranked by their association with non-completion, with a check of whether the ranking holds across courses and groups | Program manager, lecturers |
| AQ3 | Predictive | Classification with time-based validation, compared against a simple rule; survival analysis of the time to withdrawal | An estimated likelihood of not completing for each enrolment at weeks 3 and 5, with recall and precision by group | Data Analytics Team |
| AQ4 | Prescriptive | Decision rules, prioritisation under capacity, routing between offices, what-if analysis of list length and limits | An ordered list for each review point, with a factual reason and a suggested contact for each name | Lecturer-advisors, support office |

### Preliminary data requirements

**Table 6.1. Preliminary data requirements**

| AQ | Data and variables needed | Possible source | Granularity and time | Availability | Privacy and ethics note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment, final result, student status, course, delivery mode, year of study; due and submission dates of assessed tasks | Academic management system; LMS | One row per enrolment per semester; 2024–2025 and 2025–2026 | Held; status may mix leave and transfers with withdrawal (DO3) | The program sees groups, not names |
| AQ2 | AQ1 data, plus missed and late tasks, LMS activity relative to the course average, tasks missed across courses, and attendance in blended courses, for weeks 1–4 | LMS; attendance lists | One row per enrolment per week | Held in separate systems and matched by hand (DO1) | No sensitive personal categories, such as health or ethnicity, are used |
| AQ3 | AQ2 data recorded by the end of week 2 and by the end of week 4; outcome at the end of the semester | Same as AQ2 | One row per enrolment at each data cut-off | Available with about one week of delay (DO4) | Seen only by the staff who act on it; no automated decision |
| AQ4 | AQ3 output; weekly capacity of each office; contact record (who, when, how, result) | AQ3; staff rosters; a new shared contact record | One row per student per review point | The contact record does not exist yet (VCL4, VAD1) | Used for support only; family and employers are never told (VST2) |

### Decisions supported

**Table 7.1. Decisions supported and their classification**

| Decision | Who decides, using what | Level | Programmed? | Door | Evidence needed |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1. Whom to contact at each review point, by whom and with which offer | Lecturer-advisors and the support office, using the AQ4 list | Operational control (operational) | Programmed: repeated at every review point, with a fixed procedure | Two-way: a contact that does not help can be followed by another | A list that reaches more later non-completers than the simple rule (AQ3); a member of staff checks each name |
| D2. Where to place the time of the support office and the lecturer-advisors each semester | The program manager, using AQ1, AQ2 and the KPIs | Management control (tactical) | Semi-programmed: repeated each semester, but with judgement about courses and staff | Two-way: staff can be moved again next semester | A pattern repeated over several semesters, correct records and agreement with staff (PM7) |
| D3. Whether to extend the approach to all courses and link data routinely | University leadership, legal staff and the data office | Strategic planning (strategic) | Non-programmed: taken once, with no earlier case to follow | Close to one-way: it changes the university's data practice and students' trust | Pilot results, legal approval, and AQ1 and the KPIs for pilot and comparison courses (VAD4, VPM9) |

## Controlled Change Log C01–C08 (verbatim)

**Table A.9. Controlled Change Log**

| ID | Old content (Milestone 1) | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- |
| C01 | The program's online and blended courses at a Vietnamese university | OULAD module runs (UK Open University, distance learning, 2013–2014) as an open stand-in for the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses was found; OULAD is the only candidate passing the gates | All AQs answered on stand-in data; results describe OULAD and must be re-checked on the university's data before D1–D3 |
| C02 | Course and semester; weeks 1–5 of a semester (length not fixed in Milestone 1) | Module run (`code_presentation`), eight to nine months; days counted from day 0 of the run; week n = days 7(n−1) to 7n−1 | Dates in OULAD are days from the run start; runs last 234–269 days | Cut-offs become day 13 (week-3 list) and day 27 (week-5 list); the semester-length difference is a stated limit |
| C03 | Denominator: students enrolled after the add-drop period; withdrawal as in Circular 83/2026 | Enrolments still registered at day 14 (registration closes two weeks after the start); leave and transfer cannot be told apart | `date_registration`, `date_unregistration` exist; no status field for leave or transfer | Primary KPI computed as a proxy on 28,119 enrolments; deviation from the Circular 83 rule recorded |
| C04 | Comparisons by delivery mode and year of study; AQ4 limit on first-year against later-year recall | Comparisons by module and run; the fairness limit is checked across IMD band and disability | No delivery-mode or year-of-study field; all modules are distance learning | AQ1–AQ3 narrowed; AQ4 limit re-expressed on available groups |
| C05 | AQ2 sign: attendance at in-class sessions (blended courses) | Dropped | No in-class sessions or attendance in OULAD | AQ2 uses missed and late tasks, activity and concurrent runs |
| C06 | AQ3 week-3 list from assessment and activity signs | Week-3 list (day-13 cut-off) from activity only; assessment signs start with the week-5 list | A non-exam task is due by day 13 in 1 of 22 runs, by day 27 in 16 | Secondary KPI 1: two tasks fall due by day 27 in only 1 of 22 runs, so on OULAD its sign part counts one missed or late task in the 16 runs with a task due by day 27; the two-task rule stays for the university |
| C07 | AQ3 tested on a later semester of the same pilot courses | Train on 2013 runs, test on 2014 runs of the same module and start month (9 pairs); CCC, EEE-B and GGG-B only as later runs | B and J runs should be analysed separately; each module has at most two runs of one start month | Time-based validation feasible but with one earlier run per pair |
| C08 | AQ4 action and outcome; secondary KPI 2 and the contact part of secondary KPI 1 measured from a contact record | Kept as a future decision requirement; AQ4 limited to ranking under assumed capacity | No contact, capacity or intervention data in any candidate | No prescriptive or causal claim; secondary KPI 1 (contact part) and secondary KPI 2 measured only in the pilot |

## Traceability matrix (verbatim)

**Table A.10. Full traceability from goal to decision with coverage**

| Business Goal / SMART Goal / KPI | AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completion rate in pilot courses, assumed 70% → 75% by end 2027–2028 (primary KPI) | AQ1 | Descriptive | Outcome by course and time; first missed task | studentInfo, studentRegistration, assessments, studentAssessment | final_result, date_unregistration, assessments.date, date_submitted | Partial | D2, D3 |
| Primary KPI; secondary KPI 1, early-sign contact rate (sign part) | AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | + studentVle, vle | sum_click, studentVle.date, date_submitted | Partial | D2; reasons in D1 |
| Secondary KPI 1 (sign part) | AQ3 | Predictive | Target and features by the cut-off; later run for testing | as AQ2 | as AQ2 + num_of_prev_attempts, studied_credits, imd_band, disability | Partial | D1 |
| Secondary KPI 2, follow-up rate; secondary KPI 1 (contact part) | AQ4 | Prescriptive | Ranking within capacity; contact record | AQ3 outputs | none for contacts | Partial / None | D1 |

## Prediction points and leakage rules (verbatim)

**Table 2.3. Prediction points, allowed features and leakage risks**

| AQ predictive | Prediction point | Target | Features allowed before the point | Fields unavailable / leakage risk |
| :---- | :---- | :---- | :---- | :---- |
| AQ3, week-3 list | End of week 2 | Fail or withdrawal by the end of the semester | Activity to the end of week 2; submissions and their timeliness for tasks due by then; enrolment start date; background at enrolment | Final result; a withdrawal dated after the cut-off; scores and submissions of later tasks; later activity; exam results |
| AQ3, week-5 list | End of week 4 | Same | As above, to the end of week 4 | As above, after week 4; activity logged after a student's own withdrawal |
| Both lists | – | – | Course averages, scaling and encodings fitted on training semesters only, up to the cut-off; scores whose marks were known by the cut-off; study load and background as recorded at enrolment | Averages or scaling computed with test-semester students or with days after the cut-off; marks released after the cut-off; study load at the end of the semester; background fields updated later |
