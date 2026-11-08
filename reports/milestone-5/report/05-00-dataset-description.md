# 5. Dataset Description and Requirement–Data Fit

The dataset selected in Section 4.1 must now be described as it really is, because the questions can be answered only
as far as its tables allow. Section 5 describes the files, keys, sample, variables and coverage of OULAD, and Section
5.1 sets each question against these data.

**Population and unit.** OULAD covers 22 runs of seven modules of the Open University, four in science, technology,
engineering and mathematics and three in the social sciences, all taught by distance learning in the United Kingdom in
2013 and 2014. A module is the Open University's equivalent of a course; the modules carry anonymised codes, AAA to
GGG, and each offering of a module, a module run (called a presentation in the data), is named by its year and its
start month, B for February and J for October, so that 2013J is the run that started in October 2013. Time is counted
in days from the start of each run, day 0, so a negative day falls before the run begins. The unit of analysis is the
enrolment, one student in one module run, which matches the student–course–semester unit of Section 4.

**Files, keys and links.** OULAD consists of seven tables, which Table 5.1 lists with their size, key and content.
Every link between the tables holds: each submission, assessment, click record and page has its parent row, so the
tables can be joined for the same student, module run and task without losing records.

**Table 5.1. Tables of OULAD**

| Table | Rows | Key | Content | Used for |
| :---- | :---- | :---- | :---- | :---- |
| courses | 22 | module, module run | One row per module run, with its length in days | Run calendar |
| assessments | 206 | id_assessment | Assessed tasks of each run with type (TMA, CMA or exam) and due day | Missed and late tasks; first missed week |
| vle | 6,364 | id_site | Pages of the virtual learning environment with their activity type | Activity by kind of page |
| studentInfo | 32,593 | module, module run, student | One row per enrolment: background attributes and the final result | Outcome; group checks |
| studentRegistration | 32,593 | module, module run, student | Registration and unregistration day of each enrolment | Population at each day; dated withdrawal |
| studentAssessment | 173,912 | assessment, student | Each submitted task with its submission day and score | Missed and late tasks |
| studentVle | 10,655,280 | none documented | Daily number of clicks of each student on each page | Activity signs and features |

**Sample and outcome.** The 22 runs hold 32,593 enrolments of 28,785 students, and 3,538 students appear in more than
one module run. The final result is recorded for every enrolment: Pass 12,361, Withdrawn 10,156, Fail 7,052 and
Distinction 3,024. Distinction is a pass with honours, so completion means Pass or Distinction, and non-completion
means Fail or Withdrawn. Of the 10,156 withdrawals, 10,063 carry their date, which meets the outcome gate (G1); the
student identifier persists across runs, which meets the linkage gate (G5).

**Key variables.** Table 5.2 is a short data dictionary of the variables on which the questions rest; the full data
dictionary of the prepared data accompanies the Final Project Package.

**Table 5.2. Key variables of OULAD**

| Variable | Table | Meaning | Questions |
| :---- | :---- | :---- | :---- |
| final_result | studentInfo | The student's final result in the module run: Pass, Distinction, Fail or Withdrawn | Target of all four |
| code_module, code_presentation | all student tables | Module code (AAA–GGG) and run code (year and start month) | All four |
| date_registration, date_unregistration | studentRegistration | Days of registration and unregistration relative to day 0; unregistration empty for students who did not withdraw | Population at each day; withdrawal timing |
| assessment_type, date | assessments | Kind of task (TMA, CMA, exam) and its due day | AQ1–AQ3 |
| date_submitted, score | studentAssessment | Submission day and score from 0 to 100, below 40 read as a fail | AQ1–AQ3 |
| sum_click, date | studentVle | Number of clicks on one page in one day | AQ2, AQ3 |
| num_of_prev_attempts, studied_credits | studentInfo | Earlier attempts at the same module; credits studied in the run | AQ2 adjustment; AQ3 predictors |
| imd_band, disability | studentInfo | Deprivation band of the home area; declared disability | Group checks of AQ2–AQ4, never predictors |

**Coverage.** The runs are unevenly spread over modules and years. Modules BBB, DDD and FFF have four runs, EEE and
GGG three, and AAA and CCC two, so the history gate (G3) holds only in part, and with February and October runs kept
apart each module has at most one earlier and one later run of the same start month. The 9 runs of 2013 cover six
modules and 13,529 enrolments, and the 13 runs of 2014 cover all seven modules and 19,064 enrolments; module CCC has no
2013 run. Assessed tasks fall due late: a task other than the exam falls due by the end of week 2 in only 1 of the 22
runs and by the end of week 4 in 16, so task-based signs exist for the week-5 list but hardly for the week-3 list. The
population shrinks in the first days: 3,097 enrolments ended on or before day 0 and 1,377 between days 1 and 14,
leaving 28,119 still registered on day 14. Under the population rule of Section 2.1, which also removes 58 late
registrants, 28,069 enrolments count at day 13, 28,061 at day 14 and 27,535 at day 27.

**Gaps visible in the raw files.** Some values are missing: the deprivation band for 1,111 enrolments, the
registration day for 45, the score of 173 submissions, the withdrawal day of 93 Withdrawn enrolments, the due day of
11 exams and the planned weeks of 5,243 pages. The click table has no documented key, and 787,170 of its rows are exact
duplicates that cannot be told apart from repeated visits on the same day. The files differ from the documentation in
three ways: the run-length column has another name, the withdrawn outcome is written "Withdrawn" rather than
"Withdrawal", and 9 enrolments with another result carry an unregistration day. Several requirements have no variable
at all: year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity
and the day a TMA mark was released. Section 6 examines the quality issues that could change a conclusion, and
Section 5.1 shows which parts of each question these gaps affect.
