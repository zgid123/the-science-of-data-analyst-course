# 4. Data Requirements and Dataset Selection

The questions of Section 3 decide which data the project needs, and the data were chosen to fit those questions
rather than the other way round. We first stated the requirements as concepts, in the terms of the university's own
records, and only then searched for an open dataset (Section 4.1).

**Where the requirements come from.** In the university, the data needed by the questions would come from four
sources: the academic management system (enrolments, results and withdrawals), the LMS (activity and submissions),
the attendance lists of blended courses and the staff rosters. A fifth source, a record of each contact with a student
and its result, does not exist yet; secondary KPI 1 and secondary KPI 2 depend on it (Section 2.1).

**What every question shares.** All four questions share one unit of analysis: one student's enrolment in one course in one semester, so that a student who struggles in one course and not in another is seen correctly. AQ3 takes this unit at
each data cut-off, and AQ4 lists one entry per enrolment at each review point, so a student enrolled in two courses can appear on the lists of both. The population is the students still
enrolled after the add-drop period, which is also the denominator of the primary KPI. The outcome is the final result
in three classes: any passing grade counts as completion, while a fail and a withdrawal from the course count as
non-completion. A withdrawal must carry its date, because AQ3 must know whether a student was still enrolled at each
data cut-off.

**Time and the prediction point.** The lists reach staff at the review points of weeks 3 and 5, and each list may use
only the data recorded up to its data cut-off, the end of week 2 and the end of week 4, one week before the list,
because LMS exports take about a week. Any variable recorded after a cut-off would leak the future into the list, so
the requirements fix a timestamp for every event. For the same reason a task counts as missed only if it was due
before the student's withdrawal date; otherwise a student who withdrew would appear to miss every later task.

**The requirement matrix.** Table 4.1 is the AQ–Data Requirement Matrix. For each question it states the analytics
level, the unit, what must be measured, the variables the question cannot do without, the time window and grain, and
the decision point at which the answer is used.

**Table 4.1. AQ–Data Requirement Matrix**

| AQ | Level | Unit of analysis | Outcome or measure | Required variables (source) | Time and grain | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass, fail or withdrawal; week of the first missed task, for students who pass and for those who do not | Persistent student, course and semester identifiers; course start date; enrolment start and end dates; final result; dated withdrawal (academic management system); task due and submission dates (LMS) | Four semesters; week | D2, end of semester |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in later non-completion between students with and without each sign | AQ1 variables, plus dated activity (LMS); missed and late tasks, counting only tasks due before a student's withdrawal; courses taken in the same semester (academic management system) | Weeks 1–4; day or week | D2; reasons in D1 |
| AQ3 | Predictive | Student–course–semester at each data cut-off | Non-completion by the end of the semester | Timestamped activity and submissions (LMS); dated withdrawal, enrolment start date and background known at enrolment (academic management system) | Cut-offs at the end of weeks 2 and 4; at least three semesters in time order | D1, weeks 3 and 5 |
| AQ4 | Prescriptive | Student–course–semester at each review point | Recall within capacity; outcome after contact | AQ3 output, one entry per enrolment; weekly capacity (an assumption; staff rosters); contact record (to be created) | Each review point and week | D1, whom to contact |

**Must-have gates.** From the required variables we derived six must-have gates, conditions that any candidate dataset
must meet whatever its score, numbered G1 to G5 with G2 in two parts:

1. G1 Outcome: a final result for each enrolment that separates pass, fail and withdrawal, with the date of each
   withdrawal, because the primary KPI and the target of AQ3 depend on it.
2. G2a Dated assessed tasks: due dates and dated submissions counted from the course start, because missed and late
   tasks are the main early signs of AQ2 and the basis of secondary KPI 1.
3. G2b Dated activity: platform activity for each student by day or week, because AQ2 and AQ3 compare activity in the
   first weeks.
4. G3 History: at least three runs (separate offerings) of the same courses, ordered in time, with a later run
   available for testing, because AQ3 must be tested on a later semester than the one it learns from.
5. G4 Access: an open licence for academic use, official documentation and verifiable provenance, because data of
   unclear origin or without a right of use cannot support a submitted analysis.
6. G5 Privacy and linkage: anonymised data with a student identifier that persists across tables and runs, because the
   questions join results, tasks and activity for the same student.

**Optional variables and declared gaps.** Some variables enrich the questions without deciding whether a dataset can
serve: delivery mode, year of study, attendance, a status that separates leave and transfer from withdrawal, and the
assignment of students to lecturer-advisors. A dataset without them can still answer the core of each question, and
the clauses that rely on them are then covered only in part. One gap was declared before the search began: the
scenario holds no contact record, and weekly staff capacity is an assumption rather than data, so the action part of
AQ4 was expected to find no data. Finally, sensitive attributes such as disability and deprivation may be used only
to check that associations and accuracy hold across groups, never as reasons to put a student on a list. Section 4.1
applies these requirements to the open datasets found.
