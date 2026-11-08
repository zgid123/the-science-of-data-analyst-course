# Frozen Milestone 1 baseline

Frozen 2026-11-05T18:00:42Z from `reports/milestone-1/report/` by `code/freeze_baseline.py`. Text below is copied verbatim; any later change to Milestone 1 goes into the Controlled Change Log.

## Source files (SHA-256)

| File | SHA-256 |
| :---- | :---- |
| 03-01-business-goal.md | 39cd541f2c1ce4c21df2e194cd857df03d09003ddfbeecbb7f7f05354d6ece34 |
| 03-02-smart-goal.md | 4402d67f291aff3a4c29fa776b45ffe4315c3408cdd621a2d15013b366bf78d0 |
| 03-03-kpis.md | 13c18d601d8aa87a8d89c8eb0f6a57dad67a40625edd445890a977f6968f9e29 |
| 04-01-four-level-questions.md | 404bcc2ae5cfae66d3866fa10ebd78b617146db7e5ecbcf70bb21eefbe9a34e2 |
| 05-00-analytic-approach.md | 67e8b7510dcb23675f5d79116ce6aa59d6b550b9d31208f788118bca72e1f584 |
| 06-01-data-requirements.md | a1022c224669eb4f81a460bf396573bb2738c4d503bc8c2dc68f3a03a784582f |
| 07-00-decision-value.md | 49ff783b35dbba1d3f6d7863fd349188b419193eefc3d3c7cd50de5bb6440945 |
| 09-00-traceability-matrix.md | da18b3430886d9be3332405c95442112e4326dc49c065dc61c936a5a5777a8a9 |

## Business Goal

improve successful course completion in the program's online and blended courses by identifying students who stop taking part early enough to support them within the semester

## SMART Goal

> **SMART Goal.** Raise the course completion rate of students enrolled after the add-drop period in the pilot
> courses (the program's online and blended courses chosen for the pilot in Semester 2 of 2026–2027) from their
> recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by the end of the 2027–2028
> academic year.

## KPIs

**Table 3.2. Primary and secondary KPIs**

| KPI | Definition | Why it tracks the SMART Goal |
| :---- | :---- | :---- |
| Primary: course completion rate | Passed ÷ enrolled after add-drop, pooled over pilot courses; fail or course withdrawal = non-completion; leave and transfers excluded, as under Circular 83/2026 | The SMART Goal's measure and the program's reported outcome |
| Secondary 1: early-sign contact rate | Students meeting the early-sign rule (two or more tasks missed or late by week 4) contacted by end of week 5 ÷ students meeting the rule | Shows that disengaging students are reached in time (PM3, CL6); readable within the semester |
| Secondary 2: follow-up rate | Listed students contacted within seven days of the list being sent ÷ listed students | Shows that the list fits capacity and is used (AD10, CL11) |

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
rule such as "two or more assessed tasks missed"? Accuracy is measured on a list as long as staff can follow up each week,
as recall (the share of later non-completers who appear on the list) and precision (the share of listed students who
later fail or withdraw), and is compared between first-year and later-year students and across courses.

**AQ4 – Prescriptive.** At each review point (weeks 3 and 5), which students should be listed, in what order, and with
which contact (a message from the lecturer or lecturer-advisor, a call from the support office, or a referral to
the student affairs office for financial or personal support), so that the list reaches as many as possible of the students most likely not to complete? The list
must fit weekly capacity (three to five contacts per lecturer-advisor, about 30–40 for the support office), reach a
precision of at least 50%, and keep first-year recall within ten points of later-year recall; the last two limits are
assumptions.

## Analytics types and technique families

**Table 5.1. Analytics type, candidate technique family and expected output per question**

| AQ | Analytics type | Candidate technique family | Expected output | Main user |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Rates, distributions, segmentation, trends; repeated after the pilot for pilot and comparison courses | Course and group profile; timeline of first missed tasks | Program Manager |
| AQ2 | Diagnostic | Group comparison, association measures and tests, explanatory regression, cohort comparison | Early signs ranked by association, with consistency across groups | Program Manager, lecturers |
| AQ3 | Predictive | Classification with time-based validation; a simple rule as comparison; survival analysis | Likelihood of not completing per enrolment at weeks 3 and 5, with recall and precision by group | Data Analytics Team |
| AQ4 | Prescriptive | Decision rules, prioritisation under capacity, routing, what-if analysis | Ordered list per review point with a factual reason and a suggested contact | Lecturer-advisors, support office |

## Preliminary data requirements

**Table 6.1. Preliminary data requirements**

| AQ | Data / variables needed | Possible source | Granularity / time | Availability | Privacy / ethics note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment, final result, student status, course, delivery mode, year of study; task due and submission dates | Academic management system; LMS | Enrolment per semester; 2024–2026 | Held; status may mix leave and transfers with withdrawal (DO3) | Groups, not names, for the program |
| AQ2 | AQ1 data plus missed and late tasks, LMS activity within course, tasks missed across courses, attendance (blended) in weeks 1–4 | LMS; attendance lists | Enrolment by week | Held in separate systems, matched by hand (DO1) | No sensitive personal categories |
| AQ3 | AQ2 data recorded by the end of weeks 2 and 4; outcome at semester end | Same as AQ2 | Enrolment at each cut-off | About one week of delay (DO4) | Seen only by staff who act; no automated decision |
| AQ4 | AQ3 output; weekly capacity; contact record (who, when, how, result) | AQ3; staff rosters; a new shared contact record | Student per review point | Contact record does not exist (AD7, VCL4) | Support only; family and employers never told (VST2) |

## Decisions supported

**Table 7.1. Decisions supported and their classification**

| Decision | Who decides, using what | Level | Programmed? | Door | Evidence needed |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1. Whom to contact at each review point, by whom, with which offer | Lecturer-advisors and support office; AQ4 list | Operational control | Programmed | Two-way | A list with higher recall than the simple rule (AQ3); staff check each name |
| D2. Where to place advisors' and tutors' time each semester | Program Manager; AQ1–AQ2 and KPIs | Management control | Semi-programmed | Two-way | A pattern repeated over semesters, correct records, staff agreement (PM7) |
| D3. Whether to extend to all courses and link data routinely | Leadership, legal, data office | Strategic planning | Non-programmed | Close to one-way | Pilot results, legal approval, AQ1 and KPIs for pilot and comparison courses (VAD4, VPM9) |
