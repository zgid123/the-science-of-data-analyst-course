## 2.1. AQ–Data Requirement Matrix

All four questions share one unit of analysis: one student's enrolment in one course in one semester. The population
is the students still enrolled after the add-drop period, which is also the denominator of the primary KPI. The
outcome is the final result in three classes: any passing grade counts as completion, and a fail or a course
withdrawal does not.
Table 2.1 states, for each question, what must be measured, the variables it cannot do without, the time grain and the
decision it serves.

**Table 2.1. AQ–Data Requirement Matrix**

| AQ | Analytics type | Unit of analysis | Outcome / measure | Required variables | Time / granularity | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass, fail or withdrawal; week of the first missed task, for students who pass and for those who do not | Persistent student, course and semester identifiers; course start date; enrolment start and end dates; final result; dated withdrawal; task due and submission dates | Four semesters; week | D2, end of semester |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in later non-completion between students with and without each sign | AQ1 variables + dated learning-platform activity; missed and late tasks (only tasks due before a student's withdrawal); courses taken in the same semester | Weeks 1–4; day or week | D2; reasons in D1 |
| AQ3 | Predictive | Student–course–semester at each cut-off | Non-completion by the end of the semester | Timestamped activity and submissions; dated withdrawal; enrolment start date; background known at enrolment | Cut-offs at the end of weeks 2 and 4; at least three semesters in time order | D1, weeks 3 and 5 |
| AQ4 | Prescriptive | Student per review point | Recall and precision within capacity; outcome after contact | AQ3 output, one entry per student; weekly capacity (an assumption); contact record | Per review point and week | D1, whom to contact |

Delivery mode, year of study, attendance, the distinction between leave, transfer and withdrawal, and the assignment
of students to advisors are optional: they enrich AQ1–AQ4 but do not decide whether a dataset can serve. Their absence
turns the clauses that rely on them into Partial coverage instead (Appendix V). From these requirements, six must-have gates follow
for any candidate dataset, G1 to G5 with G2 in two parts:

(1) G1 Outcome: a final result per enrolment that separates pass, fail and withdrawal, with a dated withdrawal.
(2) G2a Dated assessed tasks: due dates and dated submissions, counted from the course start.
(3) G2b Dated activity: learning-platform activity per student at day or week level.
(4) G3 History: at least three runs of the same courses, ordered in time, with a later run available for testing.
(5) G4 Access: an open license for academic use, official documentation and verifiable provenance.
(6) G5 Privacy and linkage: anonymised data with a persistent student identifier across tables and runs.
