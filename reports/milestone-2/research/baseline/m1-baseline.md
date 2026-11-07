# Frozen Milestone 1 baseline

Frozen 2026-11-07T17:48:28Z from `reports/milestone-1/report/` by `code/freeze_baseline.py`. Text below is copied verbatim; any later change to Milestone 1 goes into the Controlled Change Log.

## Source files (SHA-256)

| File | SHA-256 |
| :---- | :---- |
| 03-01-business-goal.md | f99753ab586754e3c6f416c34b669db647d93dc20920db59fb964c3aef0bab23 |
| 03-02-smart-goal.md | d7b32a609f5b39a24630713b3ca631dca9328404e18a42e0737fa8311caa6087 |
| 03-03-kpis.md | 7698548222c8f9431f16f36bb0a7f6ec5de11221e15b645f8f4d3f5391b8710a |
| 04-01-four-level-questions.md | 300389d938bb7457192bf10790fffa432849c67460df2df379add184c9a05993 |
| 05-00-analytic-approach.md | 98a36dc7d86271d00cd5e5432164e547e7d945f28880e3811c80d35e13439753 |
| 06-01-data-requirements.md | 07d212a4cbaa800221a699bf91db387e7f27e59cac53522108bca7ad06293cf1 |
| 07-00-decision-value.md | 19086def5d5cabde135c1ecd68e6d6223170d6908b3a0d9f068dd8fe65870e68 |
| 09-00-traceability-matrix.md | d74c013921ccb95da9511facaf04b781499012a061d5cb71ae4724e5ec1cdd2d |

## Business Goal

improve successful course completion in the program's online and blended courses
by identifying students who stop taking part early enough to support them within the semester

## SMART Goal

> **SMART Goal.** Raise the course completion rate of students enrolled after the add-drop period in the pilot
> courses from their recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by the end of
> the 2027–2028 academic year.

## KPIs

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

## Analytical questions

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

## Analytics types and technique families

**Table 5.1. Analytics type, candidate technique family and expected output per question**

| AQ | Analytics type | Candidate technique family | Expected output | Main user |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Rates, distributions, segmentation by course and group, trends over semesters; repeated after the pilot for pilot and comparison courses | A profile of completion by course and student group; a timeline of when non-completers first miss a task | Program manager |
| AQ2 | Diagnostic | Group comparison, association measures and statistical tests, explanatory regression, comparison of cohorts | Early signs ranked by their association with non-completion, with a check of whether the ranking holds across courses and groups | Program manager, lecturers |
| AQ3 | Predictive | Classification with time-based validation, compared against a simple rule; survival analysis of the time to withdrawal | An estimated likelihood of not completing for each enrolment at weeks 3 and 5, with recall and precision by group | Data Analytics Team |
| AQ4 | Prescriptive | Decision rules, prioritisation under capacity, routing between offices, what-if analysis of list length and limits | An ordered list for each review point, with a factual reason and a suggested contact for each name | Lecturer-advisors, support office |

## Preliminary data requirements

**Table 6.1. Preliminary data requirements**

| AQ | Data and variables needed | Possible source | Granularity and time | Availability | Privacy and ethics note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment, final result, student status, course, delivery mode, year of study; due and submission dates of assessed tasks | Academic management system; LMS | One row per enrolment per semester; 2024–2025 and 2025–2026 | Held; status may mix leave and transfers with withdrawal (DO3) | The program sees groups, not names |
| AQ2 | AQ1 data, plus missed and late tasks, LMS activity relative to the course average, tasks missed across courses, and attendance in blended courses, for weeks 1–4 | LMS; attendance lists | One row per enrolment per week | Held in separate systems and matched by hand (DO1) | No sensitive personal categories, such as health or ethnicity, are used |
| AQ3 | AQ2 data recorded by the end of week 2 and by the end of week 4; outcome at the end of the semester | Same as AQ2 | One row per enrolment at each data cut-off | Available with about one week of delay (DO4) | Seen only by the staff who act on it; no automated decision |
| AQ4 | AQ3 output; weekly capacity of each office; contact record (who, when, how, result) | AQ3; staff rosters; a new shared contact record | One row per student per review point | The contact record does not exist yet (VCL4, VAD1) | Used for support only; family and employers are never told (VST2) |

## Decisions supported

**Table 7.1. Decisions supported and their classification**

| Decision | Who decides, using what | Level | Programmed? | Door | Evidence needed |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1. Whom to contact at each review point, by whom and with which offer | Lecturer-advisors and the support office, using the AQ4 list | Operational control (operational) | Programmed: repeated at every review point, with a fixed procedure | Two-way: a contact that does not help can be followed by another | A list that reaches more later non-completers than the simple rule (AQ3); a member of staff checks each name |
| D2. Where to place the time of the support office and the lecturer-advisors each semester | The program manager, using AQ1, AQ2 and the KPIs | Management control (tactical) | Semi-programmed: repeated each semester, but with judgement about courses and staff | Two-way: staff can be moved again next semester | A pattern repeated over several semesters, correct records and agreement with staff (PM7) |
| D3. Whether to extend the approach to all courses and link data routinely | University leadership, legal staff and the data office | Strategic planning (strategic) | Non-programmed: taken once, with no earlier case to follow | Close to one-way: it changes the university's data practice and students' trust | Pilot results, legal approval, and AQ1 and the KPIs for pilot and comparison courses (VAD4, VPM9) |
