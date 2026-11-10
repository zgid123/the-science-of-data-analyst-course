## Appendix V – Dataset Tables, Coverage and Gaps

This appendix supports Section 5. It gives the seven tables of OULAD with their keys, the coverage of runs and tasks, the gaps visible in the raw files, the AQ–Data Fit Matrix with every cell written out, and the four classes of gap with their handling.

**Population and unit.** OULAD covers 22 runs of seven modules of the Open University, four in science, technology,
engineering and mathematics and three in the social sciences, all taught by distance learning in the UK in
2013 and 2014. A module is the Open University's equivalent of a course; the modules carry anonymised codes, AAA to
GGG, and each offering of a module, a module run (called a presentation in the data), is named by its year and its
start month, B for February and J for October, so that 2013J is the run that started in October 2013. Time is counted
in days from the start of each run, day 0, so a negative day falls before the run begins. The unit of analysis is the
enrolment, one student in one module run, which matches the student–course–semester unit of Section 4.

**Files, keys and links.** OULAD consists of seven tables, which Table A.12 lists with their size, key and content.
Every link between the tables holds: each submission, assessment, click record and page has its parent row, so the
tables can be joined for the same student, module run and task without losing records.

**Table A.12. Tables of OULAD**

| Table | Rows | Key | Content | Used for |
| :---- | :---- | :---- | :---- | :---- |
| courses | 22 | module, module run | One row per module run, with its length in days | Run calendar |
| assessments | 206 | id_assessment | Assessed tasks of each run with type (TMA, CMA or exam) and due day | Missed and late tasks; first missed week |
| vle | 6,364 | id_site | Pages of the virtual learning environment with their activity type | Activity by kind of page |
| studentInfo | 32,593 | module, module run, student | One row per enrolment: background attributes and the final result | Outcome; group checks |
| studentRegistration | 32,593 | module, module run, student | Registration and unregistration day of each enrolment | Population at each day; dated withdrawal |
| studentAssessment | 173,912 | assessment, student | Each submitted task with its submission day and score | Missed and late tasks |
| studentVle | 10,655,280 | none documented | Daily number of clicks of each student on each page | Activity signs and features |

**Key variables.** The key variables of Table 5.1 (Section 5) come from these tables with the following scales and roles. The final result (final_result) and the background attributes come from studentInfo, and the module and run codes (code_module, code_presentation) key every student table. The registration and unregistration days (date_registration, date_unregistration) come from studentRegistration and count from day 0; the unregistration day is empty for students who did not withdraw. The kind and due day of each task (assessment_type, date) come from assessments, and the submission day and score (date_submitted, score) from studentAssessment, where the score runs from 0 to 100 and a score below 40 is read as a fail. Each row of studentVle gives the clicks of one student on one page in one day (sum_click, date). Earlier attempts at the same module and the credits studied in the run (num_of_prev_attempts, studied_credits) adjust the AQ2 model and enter the AQ3 predictors, while the deprivation band of the home area and declared disability (imd_band, disability) serve only the group checks of AQ2 to AQ4 and are never predictors.

**Sample and outcome.** The 22 runs hold 32,593 enrolments of 28,785 students, and 3,538 students appear in more than
one module run. The final result is recorded for every enrolment: Pass 12,361, Withdrawn 10,156, Fail 7,052 and
Distinction 3,024. Distinction is a pass with honours, so completion means Pass or Distinction, and non-completion
means Fail or Withdrawn. Of the 10,156 withdrawals, 10,063 carry their date, which meets the outcome gate (G1); the
student identifier persists across runs, which meets the linkage gate (G5).

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

The tables of Section 5 meet the core requirements of every question but none in full, so each question had to be set
against the real data before any analysis. The fit was rated twice, in sequence. Milestone 2 rated coverage from the
documentation and the structural check: Full when the data answer the question as stated, Partial when they answer its
core but not every clause, and None when they cannot answer it; all four questions were Partial, and the action part of
AQ4 was None. Milestone 3 then rated each question against the claim it carries after profiling the data: GREEN when
the variables, population, time window and quality are enough to answer it, YELLOW when the question must be narrowed,
its claim changed or data added, and RED when a key concept, variable, target or intervention is missing.

**The fit matrix.** Table A.13 is the AQ–Data Fit Matrix in its final form. For each question it gives what the data
support, what is missing or weak, how the gap is handled, the revision action on the brief's scale and the final
status of Section 3.

**Table A.13. AQ–Data Fit Matrix**

| AQ | Supported by OULAD | Missing or weak | Handling | Action | Final status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Final result of all 32,593 enrolments in 22 runs; due days of 182 TMA and CMA tasks and their submissions; registration and unregistration days | Year of study and delivery mode (every run is distance learning); exam results in only 2 of 7 modules | First missed task derived over TMA and CMA; comparisons by module, run, start month and year; population rule at day 14 (C09); computed on 2013, 2014 and the 22 runs pooled (C15) | Modify | Answered |
| AQ2 | Daily click records; tasks due by day 27 in 16 of 22 runs; 1,382 enrolments in two runs at once, 1,370 of them in 2014 | Attendance; year of study and delivery mode; the several-modules sign in 2013 | Each sign derived with a formula and a time window; task signs only in runs with a task due; several-modules sign for 2014 only (C12); estimated on 2013 and replicated on 2014 (C14, C15) | Modify | Answered |
| AQ3 | Target for every enrolment; 28,069 enrolled at day 13 and 27,535 at day 27; 9 module and start-month pairs in both years | A task-only rule fires in 1 run at day 13 and 16 at day 27; no day on which a TMA mark was released; one earlier run per module and start month | Early-sign rule restated with an inactivity part (C10); CMA marks used only when known by the cut-off; train on 2013, test once on all 13 runs of 2014 (C16) | Modify | Deferred |
| AQ4 | Ranking from the AQ3 scores; enrolment counts for capacity scenarios | Contacts, contact types, staff capacity and outcomes after contact | No compatible open dataset; rewritten to the ranking part (C11); judged by lift and normalised recall (C13); contact choice deferred to the pilot | Modify + Defer | Deferred |

**Kinds of gap and how each is handled.** Not every empty cell in OULAD is a gap of the same kind, and each kind
needs a different response. Table A.14 sorts the gaps into four classes. A missing value is a variable that exists but
is empty for some records; a recorded absence is a missing row that itself records an event, such as no click or no
submission; a missing variable is something the dataset never collected, which must not be imputed or generated as if
it were real; and a missing target means no outcome for supervised prediction.

**Table A.14. Classes of gap in OULAD and their handling**

| Class | Cases in OULAD | Handling |
| :---- | :---- | :---- |
| Missing value | Deprivation band (1,111 enrolments); registration day (45); TMA score (173); withdrawal day of 93 Withdrawn enrolments; due day of 11 exams | A "Missing" category for the deprivation band; indicators; no imputation in the prepared views; exams left out of task counts |
| Recorded absence | No click row; no submission row; empty unregistration day of students who stayed | Zero counts after joins; an empty unregistration day means the student did not withdraw |
| Missing variable | Year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity, the day a TMA mark was released | Not imputed or simulated; questions narrowed (AQ1–AQ3) or the contact part deferred (AQ4) |
| Missing target | None: the final result is present for every enrolment | Supervised target available |

**Why no other dataset is added.** Adding a compatible open dataset closes none of these gaps. None of the seven
candidates screened in Section 4.1 records contacts, attendance or year of study for the same students, and joining
data of other students only because they share a variable name would create links that do not exist. Synthetic data
are used only as small hand-made test records that check each feature formula in the code; they never enter a prepared
view, a statistic or a finding.

**Status entering the analysis.** After Milestone 3 every question had a prepared view, a fixed target and fixed time
rules: AQ1 and AQ3 were ready, AQ2 was ready for association only, and AQ4 was ready as a ranking with its contact part
deferred, so all the entry conditions for modeling held. The prepared data are split by year: the 9 runs of 2013 are
for development and the 13 runs of 2014 for the single final test. At day 27 the development runs hold 11,811
enrolments, of whom 5,245 (44.4%) did not complete, and the test runs hold 15,724 enrolments, of whom 6,911 (44.0%)
did not complete; AQ1 and AQ2 describe both years, and no 2014 outcome enters any AQ3 choice (C15).

**Which questions the data cannot support.** Three parts of the proposal cannot be answered with OULAD and need the
university's own records. The first is the contact part of AQ4: which contact, a message from a lecturer, a call from
the support office or a referral, works for which student, and whether contact raises completion; it is deferred to a
randomised pilot in which contacts and outcomes are logged. The second is every comparison by year of study, delivery
mode or attendance, which AQ1–AQ3 replace by comparisons by module, run and start month, and which the pilot can
restore. The third is secondary KPI 2 with the contact part of secondary KPI 1, which need the contact record. Within
OULAD, the several-modules sign of AQ2 exists almost only in 2014 (12 of 1,382 such enrolments fall in 2013) and is deferred with the 2014 replication. No question is
dropped, because each keeps a core that the data answer. Section 6 examines the data behind these supported cores in
detail.
