## 2.1. AQ–Data Requirement Matrix

**What every question shares.** All four questions share one unit of analysis: one student's enrolment in one course
in one semester, so that a student who struggles in one course and not in another is seen correctly. The population
is the students still enrolled after the add-drop period, which is also the denominator of the primary KPI. The
outcome is the final result in three classes: any passing grade counts as completion, while a fail and a withdrawal
from the course count as non-completion. A withdrawal must carry its date, because AQ3 must know whether a student was
still enrolled at each data cut-off, the last day whose data a contact list may use.

**What each question needs.** Table 2.1 is the brief's requirement matrix. For each question it states the unit, what
must be measured, the variables the question cannot do without, the time window and grain, and the decision point at
which the answer is used.

**Table 2.1. AQ–Data Requirement Matrix**

| AQ | Analytics type | Unit of analysis | Outcome / measure | Required variables | Time / granularity | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass, fail or withdrawal; week of the first missed task, for students who pass and for those who do not | Persistent student, course and semester identifiers; course start date; enrolment start and end dates; final result; dated withdrawal; task due and submission dates | Four semesters; week | D2, end of semester |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in later non-completion between students with and without each sign | AQ1 variables, plus dated learning-platform activity; missed and late tasks (only tasks due before a student's withdrawal); courses taken in the same semester | Weeks 1–4; day or week | D2; reasons in D1 |
| AQ3 | Predictive | Student–course–semester at each data cut-off | Non-completion by the end of the semester | Timestamped activity and submissions; dated withdrawal; enrolment start date; background known at enrolment | Cut-offs at the end of weeks 2 and 4; at least three semesters in time order | D1, weeks 3 and 5 |
| AQ4 | Prescriptive | Student at each review point | Recall and precision within capacity; outcome after contact | AQ3 output, one entry per student; weekly capacity (an assumption); contact record | Each review point and week | D1, whom to contact |

**Optional variables.** Some variables enrich the questions without deciding whether a dataset can serve: delivery
mode, year of study, attendance, a status that separates leave and transfer from withdrawal, and the assignment of
students to lecturer-advisors. A dataset without them can still answer the core of each question; the clauses that
rely on them are then covered only in part (Partial coverage, Section 7), rather than the dataset being rejected.

**Must-have gates.** From the required variables, the team derived six must-have gates, conditions that any candidate
dataset must meet whatever its score, numbered G1 to G5 with G2 in two parts:

1. G1 Outcome: a final result for each enrolment that separates pass, fail and withdrawal, with the date of each
   withdrawal, because the primary KPI and AQ3's target depend on it.
2. G2a Dated assessed tasks: due dates and dated submissions, counted from the course start, because missed and late
   tasks are the main early signs of AQ2 and the basis of the first secondary KPI.
3. G2b Dated activity: activity on the learning platform for each student by day or week, because AQ2 and AQ3 compare
   activity in the first weeks.
4. G3 History: at least three runs of the same courses, ordered in time, with a later run available for testing,
   because AQ3 must be tested on a later semester than the one it learns from.
5. G4 Access: an open license for academic use, official documentation and verifiable provenance, because the brief
   forbids data of unclear origin or without a right of use [1].
6. G5 Privacy and linkage: anonymised data with a student identifier that persists across tables and runs, because
   the questions join results, tasks and activity for the same student.
