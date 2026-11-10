## Appendix IV – Data Requirements and Dataset Selection

This appendix supports Section 4. It gives the sources of the requirements, the full AQ–Data Requirement Matrix, the six must-have gates with their reasons, the search procedure, the ten scores of each candidate dataset, the reasons for each rejection, and the provenance record of our copy of OULAD.

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

**The requirement matrix.** Table A.9 is the AQ–Data Requirement Matrix. For each question it states the analytics
level, the unit, what must be measured, the variables the question cannot do without, the time window and grain, and
the decision point at which the answer is used.

**Table A.9. AQ–Data Requirement Matrix**

| AQ | Level | Unit of analysis | Outcome or measure | Required variables (source) | Time and grain | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass, fail or withdrawal; week of the first missed task, for students who pass and for those who do not | Persistent student, course and semester identifiers; course start date; enrolment start and end dates; final result; dated withdrawal (academic management system); task due and submission dates (LMS) | Four semesters; week | D2, end of semester |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in later non-completion between students with and without each sign | AQ1 variables, plus dated activity (LMS); missed and late tasks, counting only tasks due before a student's withdrawal; courses taken in the same semester (academic management system) | Weeks 1–4; day or week | D2; reasons in D1 |
| AQ3 | Predictive | Student–course–semester at each data cut-off | Non-completion by the end of the semester | Timestamped activity and submissions (LMS); dated withdrawal, enrolment start date and background known at enrolment (academic management system) | Cut-offs at the end of weeks 2 and 4; at least three semesters in time order | D1, weeks 3 and 5 |
| AQ4 | Prescriptive | Student–course–semester at each review point | Recall within capacity; outcome after contact | AQ3 output, one entry per enrolment; weekly capacity (an assumption; staff rosters); contact record (to be created) | Each review point and week | D1, whom to contact |

**Must-have gates.** From the required variables we derived six must-have gates, conditions that any candidate dataset
must meet whatever its score, numbered G1 to G5 with G2 in two parts:

(1) G1 Outcome: a final result for each enrolment that separates pass, fail and withdrawal, with the date of each
   withdrawal, because the primary KPI and the target of AQ3 depend on it.
(2) G2a Dated assessed tasks: due dates and dated submissions counted from the course start, because missed and late
   tasks are the main early signs of AQ2 and the basis of secondary KPI 1.
(3) G2b Dated activity: platform activity for each student by day or week, because AQ2 and AQ3 compare activity in the
   first weeks.
(4) G3 History: at least three runs (separate offerings) of the same courses, ordered in time, with a later run
   available for testing, because AQ3 must be tested on a later semester than the one it learns from.
(5) G4 Access: an open licence for academic use, official documentation and verifiable provenance, because data of
   unclear origin or without a right of use cannot support a submitted analysis.
(6) G5 Privacy and linkage: anonymised data with a student identifier that persists across tables and runs, because the
   questions join results, tasks and activity for the same student.

**Optional variables and declared gaps.** Some variables enrich the questions without deciding whether a dataset can
serve: delivery mode, year of study, attendance, a status that separates leave and transfer from withdrawal, and the
assignment of students to lecturer-advisors. A dataset without them can still answer the core of each question, and
the clauses that rely on them are then covered only in part. One gap was declared before the search began: the
scenario holds no contact record, and weekly staff capacity is an assumption rather than data, so the action part of
AQ4 was expected to find no data. Finally, sensitive attributes such as disability and deprivation may be used only
to check that associations and accuracy hold across groups, never as reasons to put a student on a list. Section 4.1
applies these requirements to the open datasets found.

**How the search worked.** The search was therefore led by the requirements: its keywords came from the requirement matrix (student completion, dropout and withdrawal; interaction with an LMS or virtual learning environment; assessment submission; clickstream; higher education; learning analytics; and dropout from MOOCs), not from datasets already known to us. Milestone 2 searched the UCI Machine Learning
Repository, data repositories that assign a digital object identifier (DOI) such as figshare, Harvard Dataverse and
Zenodo, the pages of research groups that publish datasets, and general web search. Three rules applied to every hit:
the documentation and the licence were read before the data were judged; a dataset found on Kaggle, a blog or another
copy was traced back to the provider that published it; and re-uploads without a known origin were rejected. The
search log holds 16 entries from 11 searches, and seven candidates remained, more than the three the course brief
requires: A, OULAD; B, the UCI dataset 697 on dropout and academic
success; C, the UCI dataset 320 on student performance; D, the UCI dataset 856 on higher-education students'
performance; E, the XuetangX dropout data from MOOCs; F, the HarvardX Person-Course 2013 data; and G, the xAPI-Edu-Data set.

**How the candidates were judged.** Each candidate was scored from 0 to 2 on the brief's ten criteria, where 0 means
not met or not stated, 1 partly met or uncertain and 2 well met, for a total out of 20. The six must-have gates came
first: gates decide, scores inform, so a candidate that fails a gate is rejected whatever its total. Table A.10 is the
Dataset Selection Matrix; three of its columns pair two criteria each, so the table shows all ten scores, the total and
the decision with the gates each rejected candidate fails.

**Table A.10. Dataset Selection Matrix**

| Candidate | AQ coverage | Population fit | Unit / temporal | Target / timing | Docs / licence | Quality feasibility | Ethics / representativeness | Total (of 20) | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A OULAD | 1 | 1 | 2 / 1 | 1 / 1 | 1 / 2 | 1 | 1 | 12 | Selected, on condition that the files confirm three facts |
| B UCI 697 | 0 | 1 | 0 / 1 | 1 / 0 | 2 / 2 | 2 | 1 | 10 | Rejected: fails G1, G2a, G2b |
| C UCI 320 | 0 | 0 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 6 | Rejected: fails G1, G2a, G2b, G3 |
| D UCI 856 | 0 | 1 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 7 | Rejected: fails G1, G2a, G2b, G3 |
| E XuetangX | 1 | 1 | 1 / 1 | 1 / 1 | 1 / 0 | 1 | 0 | 8 | Rejected: fails G1, G2a, G4 |
| F HarvardX | 0 | 1 | 1 / 0 | 1 / 0 | 2 / 0 | 2 | 1 | 8 | Rejected: fails G1, G2a, G2b, G3, G4 |
| G xAPI-Edu-Data | 0 | 0 | 0 / 0 | 1 / 0 | 0 / 1 | 2 | 0 | 4 | Rejected: fails G1, G2a, G2b, G3; G4 unclear |

**Why OULAD, and why not the others.** OULAD is selected because it is the only candidate whose documentation meets
the timing and licence gates and records a dated withdrawal: a final result for each enrolment, including withdrawal
with the day of unregistration, dated assessments with the day of each submission, and the daily number of clicks of
each student on each page of the learning platform. Every other candidate fails at least the outcome gate (G1).
UCI 697 labels students by their degree after several years and holds only semester totals, so it cannot show when
within a course a student stopped; UCI 320 and UCI 856 describe secondary-school pupils or a single questionnaire, with
grades but no withdrawal and no dated tasks or activity; the XuetangX data record dated activity but have a yes-or-no
dropout label without pass or fail and state no licence; HarvardX records only the first and last activity of each
learner and is not openly licensed; and xAPI-Edu-Data has no dated records and is known only from a Kaggle listing.
OULAD was therefore chosen for its fit with the questions, not for ease of access: five candidates scored higher on
quality feasibility, and UCI 697 and HarvardX also on documentation, but none of them could show when a student stopped taking part.

**A modest total, made conditional.** OULAD's total of 12 out of 20 is modest because the scores count only what the
documentation states, and its documentation leaves several facts open. The selection was therefore made conditional
on the files confirming three facts: that the result values separate pass from fail (G1), that each module has enough
runs for testing (G3), and that a student's identifier stays the same across runs (G5). The structural check of
Milestone 2 confirmed the first and third, and showed the second met for five of the seven modules, the five with three or four runs. AQ3 is therefore tested on all 13 runs of 2014, with the 9 runs that have an earlier run of the same module and start month reported apart from the 4 that have none (Sections 5 and 9.1).

**Limits that come with the choice.** OULAD describes UK distance-learning modules from 2013–2014, and its modules
were selected by the publisher partly because many students failed them, so its failure and withdrawal rates are
likely to exceed those of a typical program. It holds no delivery mode, year of study, attendance, leave or transfer
status, and its authors advise analysing runs that start in February and in October separately. No supplementary
dataset is added, because no candidate holds the missing contact, capacity or attendance data.

**Provenance, version and licence.** Table A.11 records where our copy of OULAD comes from, which version it is, under
which licence it may be used and how its integrity was checked. The dataset is described in the data descriptor of
Kuzilek, Hlosta and Zdrahal, which reports 22 courses and 32,593 students with their assessment results and daily
summaries of their clicks, released anonymised under a CC BY 4.0 licence [5].

**Table A.11. Provenance, version and licence of OULAD**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (OULAD) |
| Provider and authors | J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University |
| Copy used and version | figshare deposit, doi:10.6084/m9.figshare.5081998.v1, version 1; the provider page offers the latest version without a number |
| Access date | 6 November 2026 (Vietnam time, UTC+7, seven hours ahead of Coordinated Universal Time) |
| Licence | Creative Commons Attribution 4.0 (CC BY 4.0): academic use with attribution |
| Raw files | One archive, anonymisedData.zip (46,750,706 bytes), holding seven tables in comma-separated values (CSV) format |
| Integrity | Size and SHA-256 checksum of the archive and of each table pinned at collection; all seven tables matched; Milestone 3 re-confirmed every pinned checksum before preparation |
| Other copies | The UCI repository copy is identical apart from how missing values are written ("?"); the provider page's own download link returned HTTP 404 on 5 November 2026 |

**Reproducible collection and privacy.** The collection procedure re-creates the raw copy with two commands, one that
downloads the archive and checks its size and checksum, and one that verifies the structure of the seven tables;
nothing in it cleans, filters, imputes or transforms the data, so the raw files stay as published. OULAD is anonymised
by its publisher with random identifiers, days counted relative to each run and k-anonymity with k = 5, so that every
combination of identifying attributes is shared by at least five students. We make no attempt at re-identification,
and no record of the data is entered into public AI tools. Section 5 describes the tables of this copy and how far they
fit the requirements.
