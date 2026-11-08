---
id: S102
url: reports/milestone-2/report/00-1-abbreviations.md
requested: reports/milestone-2/report/00-1-abbreviations.md reports/milestone-2/report/00-2-glossary.md reports/milestone-2/report/01-00-baseline-scope.md reports/milestone-2/report/01-01-frozen-baseline.md reports/milestone-2/report/01-02-scope-change-log.md reports/milestone-2/report/02-00-data-requirements.md reports/milestone-2/report/02-01-aq-data-matrix.md reports/milestone-2/report/02-02-requirements-by-level.md reports/milestone-2/report/02-03-prediction-point-leakage.md reports/milestone-2/report/03-00-search-strategy.md reports/milestone-2/report/04-00-evaluation-selection.md reports/milestone-2/report/04-01-criteria-gates.md reports/milestone-2/report/04-02-selection-matrix.md reports/milestone-2/report/05-00-acquisition-provenance.md reports/milestone-2/report/06-00-structural-verification.md reports/milestone-2/report/07-00-coverage-gaps.md reports/milestone-2/report/07-01-traceability.md reports/milestone-2/report/07-02-gaps-revisions.md reports/milestone-2/report/08-00-risks-ethics.md reports/milestone-2/report/09-00-genai-reflection.md reports/milestone-2/report/10-references.md reports/milestone-2/report/11-00-appendices.md reports/milestone-2/report/11-01-search-log.md reports/milestone-2/report/11-02-scoring-details.md reports/milestone-2/report/11-03-acquisition-package.md reports/milestone-2/report/11-04-structure-details.md reports/milestone-2/report/11-05-change-log.md reports/milestone-2/report/11-06-ai-evidence.md
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 28 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T05
part: 1
raw: raw.txt (91 KB)
conversion: verbatim copy of 28 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-2/report/00-1-abbreviations.md @ 19d35a4 =====
# List of Abbreviations

The abbreviations below are listed in alphabetical order, each with its full form and its role in this report.

| Abbreviation | Full form | Role in this report |
| :---- | :---- | :---- |
| AI | Artificial intelligence | Generative AI acted as search strategist, metadata interpreter, requirement critic and selection reviewer (Section 9) |
| AQ | Analytical question | The four frozen questions AQ1 to AQ4 of Milestone 1 (Section 1.1) |
| CSV | Comma-separated values | The format of the OULAD tables (Section 5) |
| DOI | Digital object identifier | Persistent identifier of each dataset and descriptor (Sections 3 and 5) |
| KPI | Key performance indicator | The primary and secondary measures of the frozen SMART Goal (Section 1.1) |
| MD5 | Message Digest 5 | Checksum offered by the provider and recorded in the manifest (Section 5) |
| MOOC | Massive open online course | The setting of two rejected candidates (Section 3) |
| OULAD | Open University Learning Analytics Dataset | The selected dataset (Sections 1.2 and 4.2) |
| SHA-256 | Secure Hash Algorithm, 256-bit | Checksum used to verify every collected file (Section 5) |
| SMART | Specific, measurable, achievable, relevant and time-bound | The criteria of the frozen goal (Section 1.1) |
| UCI | University of California, Irvine | Host of the UCI Machine Learning Repository, where three candidates and a copy of OULAD are held (Section 3) |
| UK | United Kingdom | Country of the OULAD population (Sections 1.2 and 8) |
| VLE | Virtual learning environment | The online platform whose daily clicks OULAD records (Sections 3 and 6) |

===== reports/milestone-2/report/00-2-glossary.md @ 19d35a4 =====
# List of Terms

The terms below are listed in alphabetical order with their meaning in this report and the section that defines them.

| Term | Meaning in this report |
| :---- | :---- |
| Checksum | A short fingerprint computed from a file's exact bytes, which changes if any byte changes; SHA-256 and MD5 are the two used here (Section 5) |
| Contact record | A shared log of who contacted which student, when and with what result; the university does not keep it yet (Section 1.1) |
| Controlled Change Log | The record of every change to the frozen Milestone 1 baseline, with its data evidence and effect (Section 1.1; Appendix V) |
| Coverage (Full, Partial, None) | How far the collected data answer a question: fully, in its core with stated limits, or not at all (Section 7.1) |
| Data Collection Package | The raw files, metadata and scripts that re-create the collected data (Section 5; Appendix III) |
| Data cut-off | The last day whose data a contact list may use: the end of week 2 (day 13) for the week-3 list and the end of week 4 (day 27) for the week-5 list (Sections 2.1 and 7.1) |
| Day 0 | The start of an OULAD module run; OULAD counts time in days from it, so negative days fall before the run begins (Section 6) |
| Deprivation band (IMD band) | A ranking of a student's home area by the United Kingdom's Index of Multiple Deprivation, recorded in OULAD as imd_band (Section 8) |
| Frozen baseline | The Milestone 1 goal, measures, questions, data needs and decisions, copied word for word and checksummed before the search (Section 1.1) |
| k-anonymity | A guarantee that every combination of identifying attributes is shared by at least k people; OULAD meets it with k = 5 (Section 8) |
| Leakage | Use of information that is not yet known at the prediction point, which makes a method look more accurate than it can be in practice (Section 2.3) |
| Module | An Open University course; OULAD covers seven, coded AAA to GGG (Section 6) |
| Module run (presentation) | One offering of a module, named by its year and starting month: B for February, J for October, as in 2013J (Section 6) |
| Must-have gate | A condition that a candidate dataset must meet whatever its score; the gates are G1 to G5, with G2 in two parts (Section 2.1) |
| Prediction point | The moment at which a prediction is made; here, the data cut-off of each list (Section 2.3) |
| Review point | A moment in the semester when a contact list reaches staff: week 3 and week 5 (Section 1.1) |
| Structural verification | The check that collected files can be read and match their documentation, without cleaning or analysis (Section 6) |

===== reports/milestone-2/report/01-00-baseline-scope.md @ 19d35a4 =====
# 1. Milestone 1 Baseline and Scope

This part restates what the Milestone 1 proposal committed the project to answer (Section 1.1) and sets out what this
milestone does with it: the scope of the work and the changes that the collected data made necessary (Section 1.2).

===== reports/milestone-2/report/01-01-frozen-baseline.md @ 19d35a4 =====
## 1.1. Frozen Baseline

**Why the baseline is frozen.** The brief requires us to start this milestone from our proposal, not from a
dataset: the questions decide what data are needed, and the data may not quietly change the questions [1]. Before any
dataset was examined, we therefore froze the Milestone 1 baseline. Its goal, measures, questions, data needs and
decisions were copied word for word into a baseline record, and a checksum (a fingerprint of a file's exact content)
was recorded for every source file, so that any later difference between the proposal and this report is visible and
must be explained (Appendix V). Every change that the data made necessary is recorded in a Controlled Change Log, the
brief's term for a list of changes with their reasons [1].

**Goal and measures.** The Business Goal is to improve successful course completion in a university program's online
and blended courses by identifying students who stop taking part early enough to support them within the semester.
The SMART (specific, measurable, achievable, relevant and time-bound) Goal raises the course completion rate of
students enrolled after the add-drop period, the first weeks in which students may still register for or drop a
course, in the pilot courses from their recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by
the end of the 2027–2028 academic year. Completion means passing the course; a fail or a withdrawal from the course counts as non-completion, and
approved leave and transfers are left out of the count, as Vietnam's Circular 83/2026 does when it counts students
who leave a program.

Three key performance indicators (KPI) track the goal. The primary KPI is the course completion rate itself. The first
secondary KPI, the early-sign contact rate, rests on the early-sign rule: two or more assessed tasks missed or
submitted late by the end of week 4. It is the number of students meeting the rule who are contacted by the end of
week 5, divided by the number of students meeting the rule. The second secondary KPI, the
follow-up rate, is the share of students on a contact list who are contacted within seven days of receiving the list.
Both secondary KPIs rely on a contact record, a shared log of who contacted which student, when and with what result,
which the university does not keep yet.

**Questions and decisions.** The proposal climbs the four levels of analytics with four analytical questions (AQ),
each serving one or more of three decisions. D1 is whom lecturer-advisors (lecturers who also advise one or two classes
of students) and the support office contact at each review point, by whom and with which offer; a review point is a
moment in weeks 3 and 5 when a contact list reaches staff. D2 is where the program manager places the time of the
support office and the lecturer-advisors each semester. D3 is whether to extend the approach to all courses and link
data routinely after the pilot. Table 1.1 restates the four questions in short with their analytics type and the decision each supports.

**Table 1.1. The frozen questions AQ1–AQ4 with analytics types and decisions**

| AQ | Analytics type | Question in short | Decision supported |
| :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | What share of students passed, failed or withdrew, by course, delivery mode and year of study over four semesters, and in which week students who passed and students who did not first missed an assessed task | D2: where to place support time; D3: whether to extend after the pilot |
| AQ2 | Diagnostic | Which signs in weeks 1–4 (missed or late tasks, activity on the learning platform, tasks missed in several courses at once, and attendance in blended courses) differ most between students who later complete and students who do not | D2, and the reasons shown with each name in D1 |
| AQ3 | Predictive | How well failing or withdrawing by the end of the semester can be estimated from the data recorded by the end of week 2 and by the end of week 4, compared with a simple rule that counts missed assessed tasks | D1: who is listed in weeks 3 and 5 |
| AQ4 | Prescriptive | Which students to list at each review point, in what order and with which contact, within weekly staff capacity, with at least 50% of listed students later failing or withdrawing, and first-year recall within ten points of later-year recall | D1: whom to contact, by whom and with which offer |

The proposal also gave a first list of data needs for each question, at the level of concepts: enrolments, results
and student status from the academic management system; dated quizzes, assignments and activity from the learning
platform; attendance lists of blended courses; staff capacity; and the contact record. Those needs are the starting
hypotheses that Section 2 turns into testable requirements.

===== reports/milestone-2/report/01-02-scope-change-log.md @ 19d35a4 =====
## 1.2. Scope of Milestone 2 and Change Log Summary

**What this milestone does.** Building on the frozen baseline, this milestone answers the two questions that the brief
sets: which data the four questions need, and whether the open dataset that we collect actually provides them
[1]. Its work follows the brief's steps. Section 2 turns each question into a data requirement. Section 3 describes
the search for candidate open datasets, and Section 4 scores the candidates and selects one. Section 5 records how the
selected dataset was collected so that anyone can collect it again, and Section 6 checks that the collected files can
be read and match their documentation. Section 7 then maps every question to the real files and variables and states
how far each question can be answered. Sections 8 and 9 cover the risks and the use of generative
artificial intelligence (AI). Cleaning the data, filling in missing values, building features and training models are left to
later milestones, as the brief requires [1].

**What the data changed.** The selected dataset, the Open University Learning Analytics Dataset (OULAD), describes
distance-learning modules of a university in the United Kingdom (UK), not the courses of a Vietnamese program, so the
questions cannot be answered on it exactly as the proposal framed them. We recorded eight controlled revisions,
C01 to C08, each with the old and the new content, the data evidence behind it and its effect on the questions, KPIs
and decisions. Four of them matter most. OULAD stands in for the university's courses in the analysis, while the
university's own records remain the target for the pilot (C01). A semester becomes a module run, one offering of a
module lasting eight to nine months, with time counted in days from the run's start (C02). Comparisons by delivery mode and year of study are dropped,
because OULAD holds neither (C04). The action part of AQ4, the record of contacts and their outcomes, stays a
requirement for the pilot, because no open dataset records it (C08). The other four adjust the KPI denominator to
OULAD's registration window (C03), drop the attendance sign (C05), build the week-3 list from activity alone and adapt the early-sign rule to OULAD's calendar (C06) and
test AQ3 on the 2014 runs of each module (C07). Section 7.2 explains every revision, and Appendix V (Table A.9) gives
the full Change Log.

None of the revisions alters the Business Goal, the SMART Goal or the decisions. They narrow how far each question can
be answered on open data, and they keep the full questions as the target for the university's own records.

===== reports/milestone-2/report/02-00-data-requirements.md @ 19d35a4 =====
# 2. Data Requirement Specification

This part turns each frozen question into a data requirement before any dataset is examined, using concepts rather
than the column names of a dataset at hand, as the brief requires [1]. Section 2.1 gives the requirement matrix and
the must-have gates that follow from it, Section 2.2 the requirements of each analytics level, and Section 2.3 the
prediction points of AQ3 and the risk of leakage.

===== reports/milestone-2/report/02-01-aq-data-matrix.md @ 19d35a4 =====
## 2.1. AQ–Data Requirement Matrix

**What every question shares.** AQ1–AQ3 share one unit of analysis: one student's enrolment in one course in one
semester, so that a student who struggles in one course and not in another is seen correctly. AQ3 takes this unit at
each data cut-off, and AQ4 lists students, one entry per student across courses. The population
is the students still enrolled after the add-drop period, which is also the denominator of the primary KPI. The
outcome is the final result in three classes: any passing grade counts as completion, while a fail and a withdrawal
from the course count as non-completion. A withdrawal must carry its date, because AQ3 must know whether a student was
still enrolled at each data cut-off, the last day whose data a contact list may use.

**What each question needs.** AQ4 is judged by recall, the share of students who later fail or withdraw who appear on
a list, and precision, the share of listed students who later fail or withdraw. Table 2.1 is the brief's requirement
matrix. For each question it states the unit, what
must be measured, the variables the question cannot do without, the time window and grain, and the decision point at
which the answer is used.

**Table 2.1. AQ–Data Requirement Matrix**

| AQ | Analytics type | Unit of analysis | Outcome / measure | Required variables | Time / granularity | Decision point |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Student–course–semester | Pass, fail or withdrawal; week of the first missed task, for students who pass and for those who do not | Persistent student, course and semester identifiers; course start date; enrolment start and end dates; final result; dated withdrawal (academic management system); task due and submission dates (learning platform) | Four semesters; week | D2, end of semester |
| AQ2 | Diagnostic | Student–course–semester with weekly signs | Difference in later non-completion between students with and without each sign | AQ1 variables, plus dated activity (learning platform); missed and late tasks (only tasks due before a student's withdrawal); courses taken in the same semester (academic management system) | Weeks 1–4; day or week | D2; reasons in D1 |
| AQ3 | Predictive | Student–course–semester at each data cut-off | Non-completion by the end of the semester | Timestamped activity and submissions (learning platform); dated withdrawal, enrolment start date and background known at enrolment (academic management system) | Cut-offs at the end of weeks 2 and 4; at least three semesters in time order | D1, weeks 3 and 5 |
| AQ4 | Prescriptive | Student at each review point | Recall and precision within capacity; outcome after contact | AQ3 output, one entry per student; weekly capacity (an assumption; staff rosters); contact record (to be created) | Each review point and week | D1, whom to contact |

**Optional variables.** Some variables enrich the questions without deciding whether a dataset can serve: delivery
mode, year of study, attendance, a status that separates leave and transfer from withdrawal, and the assignment of
students to lecturer-advisors. A dataset without them can still answer the core of each question; the clauses that
rely on them are then covered only in part (Partial coverage, Section 7), rather than the dataset being rejected.

**Must-have gates.** From the required variables, we derived six must-have gates, conditions that any candidate
dataset must meet whatever its score, numbered G1 to G5 with G2 in two parts:

(1) G1 Outcome: a final result for each enrolment that separates pass, fail and withdrawal, with the date of each withdrawal, because the primary KPI and AQ3's target depend on it.
(2) G2a Dated assessed tasks: due dates and dated submissions, counted from the course start, because missed and late tasks are the main early signs of AQ2 and the basis of the first secondary KPI.
(3) G2b Dated activity: activity on the learning platform for each student by day or week, because AQ2 and AQ3 compare activity in the first weeks.
(4) G3 History: at least three runs (separate offerings) of the same courses, ordered in time, with a later run available for testing, because AQ3 must be tested on a later semester than the one it learns from.
(5) G4 Access: an open license for academic use, official documentation and verifiable provenance, because the brief forbids data of unclear origin or without a right of use [1].
(6) G5 Privacy and linkage: anonymised data with a student identifier that persists across tables and runs, because the questions join results, tasks and activity for the same student.

===== reports/milestone-2/report/02-02-requirements-by-level.md @ 19d35a4 =====
## 2.2. Requirements by Analytics Level

The four questions climb the analytics levels, and the brief stresses that each level needs a different kind of
evidence rather than simply more data [1]. Table 2.2 sets out the minimum data for each level and what that data can,
and cannot, show.

**Table 2.2. Data requirements by analytics level**

| Level | AQ | Minimum data | What the data can show |
| :---- | :---- | :---- | :---- |
| Descriptive | AQ1 | Outcome; course and semester dimensions; dated tasks; the denominator of students enrolled after add-drop | Rates and the timing of first missed tasks |
| Diagnostic | AQ2 | AQ1 data, plus dated signs and comparison groups, with background attributes to check consistency across groups | Associations, not causes |
| Predictive | AQ3 | A labelled outcome; predictors timestamped before the prediction point; enough semesters to test on a later one | Accuracy on a later semester, for a list of fixed length |
| Prescriptive | AQ4 | Actions (contacts), constraints (capacity) and outcomes after the action | A ranking under constraints; without action and outcome data, no claim that a contact helps |

**The prescriptive gap.** The prescriptive level is the hardest to supply from open data. It needs records of actions
and of what followed them, and the brief warns that a recommendation without such evidence must not be presented as
prescriptive analytics; the missing data must be recorded as a gap instead [1]. In the scenario of the course brief, the university keeps
no contact record yet, so the action part of AQ4 was declared a gap before the search began, and weekly staff
capacity is treated as an assumption of the baseline, not as data to be found.

**Ethics conditions.** The requirements also carry conditions on the use of sensitive data. AQ1 needs no sensitive
attribute, and its results go to the program manager by group, never by name. AQ2 and AQ3 may use background
attributes such as disability or the deprivation of a student's home area only to check that associations and
accuracy hold across groups, never as reasons to put a student on a list. For AQ4, the contact record and any
referral for financial or personal support are personal data, used only for support under a stated purpose and never
for grading.

===== reports/milestone-2/report/02-03-prediction-point-leakage.md @ 19d35a4 =====
## 2.3. Prediction Point and Leakage Risk

**Prediction points.** A predictive question must name its prediction point, the moment at which a prediction is
made, and may use only information known before it [1]. The baseline assumes about one week of delay before data reach
staff, so the data cut-offs fall at the end of week 2 and the end of week 4, and the lists reach staff in weeks 3
and 5. Leakage is the use of information that is not yet known at the prediction point; it makes a method look more
accurate on past data than it can be in practice. Table 2.3 sets out, for each list, the target, the features it may
use and the fields that would leak information from after the cut-off.

**Table 2.3. Prediction points, allowed features and leakage risks**

| AQ predictive | Prediction point | Target | Features allowed before the point | Fields unavailable / leakage risk |
| :---- | :---- | :---- | :---- | :---- |
| AQ3, week-3 list | End of week 2 | Fail or withdrawal by the end of the semester | Activity to the end of week 2; submissions and their timeliness for tasks due by then; enrolment start date; background at enrolment | Final result; a withdrawal dated after the cut-off; scores and submissions of later tasks; later activity; exam results |
| AQ3, week-5 list | End of week 4 | Same | As above, to the end of week 4 | As above, after week 4; activity logged after a student's own withdrawal |
| Both lists | – | – | Course averages, scaling and encodings fitted on training semesters only, up to the cut-off; scores whose marks were known by the cut-off; study load and background as recorded at enrolment | Averages or scaling computed with test-semester students or with days after the cut-off; marks released after the cut-off; study load at the end of the semester; background fields updated later |

**Two further rules.** Two rules prevent counting a student's departure as a sign of it. In AQ1 and AQ2, a task counts
as missed only if it was due before the student's withdrawal date; otherwise every student who withdrew early would
appear to have missed every later task. In AQ3, students who had already left by a cut-off are not counted as found by
a list, because staff could no longer contact them.

===== reports/milestone-2/report/03-00-search-strategy.md @ 19d35a4 =====
# 3. Open Dataset Search Strategy

**Where the search started.** The search started from the requirements of Section 2, not from datasets already known
to us, so that the questions decided what was looked for [1]. Its keywords came from the requirement matrix:
student completion, dropout and withdrawal; interaction with a learning management system or
virtual learning environment (VLE), the online platform on which students open materials and submit work; assessment submission;
clickstream, the record of each click a student makes on such a platform; higher education; learning analytics; and
massive open online course (MOOC) dropout.

**Where we searched.** The search covered the sources the brief suggests [1]; the
University of California, Irvine (UCI) Machine Learning Repository; data repositories that assign a digital object identifier (DOI), a permanent
reference to a dataset, such as figshare, Harvard Dataverse and Zenodo; the pages of the research groups that publish
datasets; and general web search.

**Three rules for every hit.** Three rules applied to every dataset found, as the brief asks [1]. First, we read
the documentation and the license before judging the data. Second, a dataset found on Kaggle, a blog or another
copy was traced back to the provider that published it. Third, re-uploads without a known origin were rejected.

**What the search found.** The search log in Appendix I records 16 entries, from 11 searches and the further hits they
produced, including the rejected ones: copies of a data descriptor already held, superseded web addresses, third-party re-uploads of the KDD
Cup 2015 data and secondary descriptions of datasets. Seven candidates remained, more than the three the brief
requires, each documented from its official page or descriptor. Table 3.1 summarises them: who provides each, which
population it describes, its unit of analysis, its outcome and how it records time within a course.

**Table 3.1. Candidate open datasets**

| Candidate | Provider and source | Population | Unit | Outcome | Timing within the course |
| :---- | :---- | :---- | :---- | :---- | :---- |
| A. OULAD | The Open University (UK); provider page and data descriptor [2], [3] | Students of seven distance-learning modules, 2013–2014 [3] | Student–module–run [3] | Final result, including Withdrawal with a dated unregistration [3] | Assessment due and submission days; daily clicks [3] |
| B. UCI 697 Dropout and Academic Success | Polytechnic Institute of Portalegre; UCI page and descriptor [4], [5] | Undergraduates of one institution, 2008–2019 [5] | Student [4] | Degree dropout, still enrolled, or graduate [4] | Semester totals only [5] |
| C. UCI 320 Student Performance | Two Portuguese secondary schools; UCI page [6] | Secondary-school pupils [6] | Student–subject [6] | Grade from 0 to 20 [6] | Three grades per school year [6] |
| D. UCI 856 Higher Education Students Performance Evaluation | One collection in 2019; UCI page [7] | Students of two faculties [7] | Questionnaire answer [7] | Letter grade [7] | None [7] |
| E. XuetangX MOOC dropout data | Tsinghua University, MOOCData [8], [9] | Users of a Chinese MOOC platform, 2015–2017 [8] | User–course [8] | Dropout, yes or no [8] | Timestamped actions [8] |
| F. HarvardX Person-Course 2013 | HarvardX, Harvard Dataverse [10] | HarvardX learners, 2012–2013 [10] | Person–course summary [10] | Certification | Only the first and last activity [10] |
| G. xAPI-Edu-Data | Data from the Kalboard 360 platform; the authors' Kaggle listing [11] | Students of several countries [11] | Student [11] | Grade band [11] | None documented |

The table already shows the main difference between the candidates. Only OULAD and the XuetangX data record when
students did things within a course, which AQ2 and AQ3 need, and only OULAD combines that timing with an outcome that
includes withdrawal and with dated assessments. Section 4 tests this impression against the gates and the brief's
criteria.

===== reports/milestone-2/report/04-00-evaluation-selection.md @ 19d35a4 =====
# 4. Dataset Evaluation and Selection

The seven candidates of Section 3 were judged in two steps: the must-have gates of Section 2.1 first, then the brief's
ten criteria on a common scale. Section 4.1 explains the criteria, the scale and the role of the gates, and Section 4.2
gives the selection matrix and the reasons for the choice.

===== reports/milestone-2/report/04-01-criteria-gates.md @ 19d35a4 =====
## 4.1. Criteria and Must-Have Gates

**Ten criteria on one scale.** Every candidate was scored on the ten criteria of the brief [1]: AQ coverage;
population fit; unit and granularity; outcome availability; feature availability and timing; temporal coverage;
documentation and provenance; license and access; quality feasibility; and ethics and representativeness. Appendix II
explains each criterion. Each
criterion takes 0 when it is not met or not stated, 1 when it is partly met or uncertain, and 2 when it is well met.

**Scores rest on documented facts.** A score of 2 requires a fact recorded from the candidate's own documentation, not
an expectation. A criterion scores 1 when the documentation states only part of what is needed. OULAD's outcome is an
example: its documentation describes the Withdrawal value and its date, but not the other result values, so whether
pass and fail are separated could not be scored as met from the documentation alone. Appendix II gives every score
with the fact behind it.

**Gates decide, scores inform.** The scores support the discussion, but the gates decide. A candidate that misses a
must-have gate is rejected whatever its total, because the brief warns that a high score cannot make up for a missing
target, missing timing for a predictive question or a missing right of use [1]. The gates of Section 2.1 apply these
warnings to this project: G1 secures the outcome and the date of each withdrawal, G2a and G2b the timing of tasks and
activity, G3 a later run on which to test AQ3, G4 the right of use, and G5 privacy and the links between tables.
A gate that a candidate misses outright rejects it. A gate met for only part of a dataset, such as enough runs for
some of its courses but not all, does not reject it; it narrows the questions on the part that fails, which is then
recorded as Partial coverage (Section 7). Facts that a candidate's documentation does not settle, but its files can,
were not counted as met; they became conditions to be checked in the structural verification of Section 6.

===== reports/milestone-2/report/04-02-selection-matrix.md @ 19d35a4 =====
## 4.2. Selection Matrix and Rationale

**The matrix.** Table 4.1 applies the brief's selection matrix to the seven candidates, with scores from 0 to 2. The
brief's matrix has six criterion columns; two of them each pair two criteria (target and timing; documentation and
license), and we added one column that pairs the remaining two (unit and granularity; temporal coverage), so the
table shows all ten scores and their total out of 20. The last column gives the decision and, for each rejected
candidate, the gates it fails.

**Table 4.1. Dataset Selection Matrix**

| Candidate | AQ coverage | Population fit | Unit / temporal | Target / timing | Docs / license | Quality feasibility | Ethics / representativeness | Total (of 20) | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A OULAD | 1 | 1 | 2 / 1 | 1 / 1 | 1 / 2 | 1 | 1 | 12 | Selected, on condition that Section 6 confirms three facts |
| B UCI 697 | 0 | 1 | 0 / 1 | 1 / 0 | 2 / 2 | 2 | 1 | 10 | Rejected: fails G1, G2a, G2b |
| C UCI 320 | 0 | 0 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 6 | Rejected: fails G1–G3 |
| D UCI 856 | 0 | 1 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 7 | Rejected: fails G1–G3 |
| E XuetangX | 1 | 1 | 1 / 1 | 1 / 1 | 1 / 0 | 1 | 0 | 8 | Rejected: fails G1, G2a, G4 |
| F HarvardX | 0 | 1 | 1 / 0 | 1 / 0 | 2 / 0 | 2 | 1 | 8 | Rejected: fails G1–G4 |
| G xAPI-Edu-Data | 0 | 0 | 0 / 0 | 1 / 0 | 0 / 1 | 2 | 0 | 4 | Rejected: fails G1–G3 |

**Why OULAD.** OULAD is selected because it is the only candidate whose documentation meets the timing and license
gates and records a dated withdrawal. It records a final result for each enrolment, including Withdrawal with the day
of unregistration [3]; dated assessments and the day of each submission; and the daily number of clicks of each
student on each page of the learning platform [3]. It is published under the Creative Commons Attribution 4.0 license
(CC BY 4.0), which allows academic use with attribution [2].

**Why not the others.** Every other candidate fails at least the outcome gate (G1) and the dated-task gate (G2a). UCI
697 labels students by their degree after three or four years, not by course, and holds only semester totals, so it
cannot show when within a course a student stopped [4], [5]. UCI 320 and UCI 856 describe secondary-school pupils or a
single questionnaire, with grades but no withdrawal and no dated tasks or activity [6], [7]. The XuetangX data record dated activity,
but their outcome is a yes-or-no dropout label without pass or fail, and they state no license [8]. HarvardX records
only the first and last activity of each learner and is not openly licensed [10], and xAPI-Edu-Data has no dated
records and is known only from a Kaggle listing [11].

**A modest total, made conditional.** OULAD's total of 12 out of 20 is modest because its documentation leaves several
facts open, and the scores count only what is documented. Documentation scores 1, for example, because the provider
page gives no version number and its download link was broken; only the figshare deposit carries a version. The selection was therefore made conditional on the files
confirming three facts: that the result values separate pass from fail (G1), that each module has enough runs for
testing (G3), and that a student's identifier stays the same across runs (G5). Section 6 confirms the first and the
third. It shows the second met for five of the seven modules, which keeps OULAD under the rule of Section 4.1 and
narrows AQ3 to those runs; the rejected candidates have a single period or no dates, so they miss the history gate
outright.

**Limits that come with the choice.** OULAD describes UK distance-learning modules from 2013–2014, and its modules were
selected by the publisher partly because many students failed them [3], so its failure and withdrawal rates are likely
to exceed those of a typical program. It holds no delivery mode, year of study, attendance, leave or transfer status.
Its authors also advise analysing module runs that start in February and in October separately [3], which limits how
many comparable runs each module has.

**No supplementary dataset.** The brief allows at most one supplementary dataset when it is really needed [1]. None is
selected: no candidate holds the missing contact, capacity or attendance data, and the only other source of dated
activity, the XuetangX data, lacks a license and a pass or fail outcome [8].

===== reports/milestone-2/report/05-00-acquisition-provenance.md @ 19d35a4 =====
# 5. Data Acquisition and Provenance

**Principle.** The brief requires the raw data to stay exactly as published and the collection to be repeatable by
anyone [1]. The selected dataset was therefore collected by a script that downloads the published files, checks them
and stores them unchanged, and that records everything needed to obtain them again. Two kinds of evidence make the copy
checkable. A checksum is a short fingerprint computed from a file's exact bytes; if a single byte changes, the
checksum changes. We recorded two of them for every file: SHA-256 (Secure Hash Algorithm, 256-bit), the
standard used for verification, and MD5 (Message Digest 5), the checksum that the provider itself publishes. The files
are stored as comma-separated values (CSV), plain-text tables that any tool can read. Table 5.1 is the brief's
acquisition plan for OULAD.

**Table 5.1. Data acquisition plan for OULAD**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (official title) |
| Provider / authors | J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University [3] |
| Official URL / DOI | Provider page [2]; data descriptor doi:10.1038/sdata.2017.171 [3]; files deposited on figshare, doi:10.6084/m9.figshare.5081998.v1 [3] |
| Access date | 6 November 2026 (Vietnam time, UTC+7) |
| Version / release | figshare version 1; the provider page offers the latest version without a number [2] |
| License / terms | CC BY 4.0 [2], [12] |
| Acquisition method | Direct download of one zip archive from the figshare deposit; size and SHA-256 checked against reference values written in the collection script; the seven tables extracted unchanged |
| Raw files | anonymisedData.zip (46,750,706 bytes) containing courses, assessments, vle, studentInfo, studentRegistration, studentAssessment and studentVle (CSV, 453.8 MB for studentVle) |
| Integrity evidence | SHA-256 and MD5 of the archive and of each table in the manifest, the list of files with their checksums; all seven tables matched their pinned SHA-256 |
| Citation | Kuzilek, Hlosta and Zdrahal (2017), *Scientific Data*, 4, 170171 [3] |

**Which copy, and why.** OULAD is published in three places: the provider's own server, whose link was broken
when the data were collected [2]; a figshare deposit with a DOI and a version number, which the data descriptor cites
[3]; and the UCI repository [12]. We collected and cite the figshare deposit, and a row-by-row comparison found
the UCI copy identical apart from how missing values are written (Appendix III).

**Reproducible in two commands.** Anyone with the Data Collection Package can re-create our copy with two
commands. The first, `src/collect.py`, downloads the archive, checks its size and checksum and extracts the seven
tables. The second, `src/verify_structure.py`, runs the structural checks of Section 6. The package also holds the
manifest of checksums, the data dictionary copied from the descriptor, the source and license sheet, the citation and
the collection log. The raw files stay as published: nothing is cleaned, filtered or converted. Appendix III shows the
package's layout and its source, license and manifest tables.

===== reports/milestone-2/report/06-00-structural-verification.md @ 19d35a4 =====
# 6. Initial Structural Verification

**What the check does.** With the files collected, a structural check confirmed that they can be read and that they
match their documentation, without cleaning or exploring them, as the brief limits this step [1]. Every table was read
as text, so that no value was converted on reading, and its rows, columns, keys, types, missing values and time fields
were compared with the data dictionary copied from the descriptor. Every header matches the dictionary except the one
column name noted below; Appendix IV gives the headers, the types inferred from the values and the missing cells of
every table (Table A.6).

**How OULAD is organised.** OULAD describes seven modules, the Open University's equivalent of courses, coded AAA to
GGG. Each module is offered in several runs, which the dataset calls presentations. A run is named by its year and its
starting month: B for February and J for October, so that 2013J is the run that started in October 2013 [3]. Time is
counted in days from the start of each run, day 0, so a negative day falls before the run begins. The seven tables
divide the data as follows: courses lists the module runs; assessments lists their assessed tasks with due days; vle
lists the pages of the VLE; studentInfo holds one row per enrolment of a student in a module
run, with background attributes and the final result; studentRegistration holds the days on which each enrolment was
registered and, where it happened, unregistered; studentAssessment holds each submitted task with its day and score;
and studentVle holds each student's daily number of clicks on each page. Table 6.1 summarises the structure found in
the files.

**Table 6.1. Structure of the collected OULAD files**

| File / table | Rows | Columns | Key(s) | Target / outcome | Time field | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| courses | 22 | 3 | module, module run; unique | – | run length 234–269 days | Column named module_presentation_length, documented as length |
| assessments | 206 | 6 | id_assessment; unique | – | due day (date) 12–261 | 11 exams without a due day |
| vle | 6,364 | 6 | id_site; unique | – | planned weeks 0–29 | Planned weeks missing for 5,243 sites |
| studentInfo | 32,593 | 12 | module, module run, student; unique | final_result: Pass 12,361; Withdrawn 10,156; Fail 7,052; Distinction 3,024 | – | imd_band missing for 1,111 |
| studentRegistration | 32,593 | 5 | module, module run, student; unique, 1:1 with studentInfo | – | registration day −322 to 167; unregistration day −365 to 444 | Unregistration empty for 22,521; registration missing for 45 |
| studentAssessment | 173,912 | 5 | assessment, student; unique | score 0–100 | submission day −11 to 608 | score missing for 173 |
| studentVle | 10,655,280 | 6 | none documented | – | interaction day −25 to 269 | 787,170 rows are exact duplicates |

Several column names appear in this table and in Section 7. In studentInfo, final_result is the outcome, in which
Distinction is a pass with honours, so completion means Pass or Distinction; imd_band is the deprivation band of the
student's home area; num_of_prev_attempts counts earlier attempts at the same module; and studied_credits is the
credits the student was taking in that run. In studentVle, sum_click is the number of clicks on one page in one day,
and id_site and activity_type identify the page and its kind. code_module and code_presentation name the module and
the run, and assessment_type separates tutor-marked, computer-marked and exam tasks.

**Links between tables.** All links between tables hold: every submission, assessment, click record and page has its
parent row, so the tables can be joined for the same student, module run and task without losing records.

**Differences from the documentation.** The brief asks for every difference between the documentation and the files
to be recorded [1]; the check found three. The run-length column is named module_presentation_length, not length as
documented [3]. The outcome value for withdrawn students is "Withdrawn" in the file, while the descriptor calls it
Withdrawal [3]. The descriptor's rule that only withdrawn students carry an unregistration day [3] has exceptions: 93
Withdrawn enrolments lack the day, and 9 enrolments with another result carry one. One further issue is not a
difference, because the documentation gives the click table no key: its 787,170 identical rows cannot be told apart
from repeated visits on the same day.

**The three conditions of the selection.** The check settled the conditions on which OULAD was selected (Section
4.2). First, the result values separate pass and distinction from fail and withdrawal, and 10,063 of the 10,156
withdrawals are dated, so the outcome gate G1 holds. Second, the student identifier persists across runs, so the
linkage gate G5 holds. OULAD holds 32,593 enrolments of 28,785 students; 3,538 students appear in more than one module run, and in all 1,309 cases in which a
student repeats the same module, the recorded count of previous attempts rises. That count can only rise if the same
identifier marks the same student in each run. Third, the history gate G3 holds only in part. Modules BBB, DDD and FFF
have four runs, EEE and GGG three, and AAA and CCC two. With February and October runs kept apart, as the authors
advise, each module has at most one earlier and one later run of the same start month.

**Timing and the denominator.** Two further counts shape the questions. A task other than the final exam falls due by
the end of week 2 in only 1 of the 22 module runs, and by the end of week 4 in 16, so task-based signs are available
for the week-5 list but hardly for the week-3 list. Two such tasks fall due by the end of week 4 in only 1 run, which
matters for the early-sign rule of the first secondary KPI (Section 7.2). Of the 32,593 enrolments, 3,097 ended on or
before day 0, before the run began, and 1,377 ended between days 1 and 14; the remaining 28,119 enrolments, still
registered on day 14, form the KPI denominator (Section 7.1).

===== reports/milestone-2/report/07-00-coverage-gaps.md @ 19d35a4 =====
# 7. Requirement Coverage and Data Gaps

The requirements of Section 2 and the structure found in Section 6 together show how far OULAD can answer each
question. Section 7.1 maps every question to the real files and variables, and Section 7.2 records the gaps and the
controlled revisions they caused.

===== reports/milestone-2/report/07-01-traceability.md @ 19d35a4 =====
## 7.1. Updated Traceability Matrix

**Coverage levels.** The brief rates each question's coverage as Full, Partial or None [1]. Full means that the
collected data answer the question as stated. Partial means that they answer its core but not every clause, so the
question is kept or narrowed with its limits stated. None means that they cannot answer it, so the question must be
revised or kept as a requirement for future data.

**From questions to variables.** Table 7.1 is the brief's updated traceability matrix. It links each question to the
OULAD files and the variables that serve it; every variable named exists in the collected files.

**Table 7.1. Updated traceability from AQ to actual variables**

| AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Gap / action |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Outcome by module, module run and time; first missed task for students who passed and for those who did not | OULAD: studentInfo, studentRegistration, courses, assessments, studentAssessment | final_result, code_module, code_presentation, date_registration, date_unregistration, module_presentation_length, assessment_type, assessments.date, date_submitted | Partial | Only BBB, DDD and FFF have all four module runs; no delivery mode or year of study, so those comparisons are dropped (C04) |
| AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | AQ1 files, plus studentVle and vle | AQ1 variables, plus sum_click, studentVle.date, id_site, activity_type; concurrent module runs through id_student | Partial | Task signs only where a task is due by week 4 (16 of 22 module runs); no attendance (C05) |
| AQ3 | Predictive | Fail or withdrawal; features by the cut-off; a later run for testing | As AQ2 | final_result; date_unregistration for who is still enrolled; sum_click by studentVle.date and date_submitted up to day 13 or 27; num_of_prev_attempts, studied_credits; imd_band, disability for group checks | Partial | Week-3 list from activity only (C06); testing on the 2014 runs of the 9 module and start-month pairs that have both a 2013 and a 2014 run (C07); groups by deprivation and disability (C04) |
| AQ4 | Prescriptive | Ranking within capacity; contacts and outcomes | AQ3 outputs | None for contacts or capacity | Partial (ranking) / None (action) | Ranking simulated under assumed capacity; no claim on the effect of contact; contact record kept as a pilot requirement (C08) |

**Mapping the proposal's time onto OULAD.** The questions speak of semester weeks; OULAD counts days from the start of
each module run. Week n therefore spans days 7(n−1) to 7n−1, and the data cut-offs of the week-3 and week-5 lists
fall on day 13 and day 27 (C02). The add-drop period corresponds to the Open University's registration window, which
closes two weeks after the start [3]. The KPI denominator is therefore the 28,119 enrolments still registered on day
14 (C03).

**The full chain.** The brief's deliverable B asks for a matrix that runs from the Business Goal, the SMART Goal and
the KPIs through the questions and data to the decisions [1]. Table 7.1 covers the questions and data; Appendix V
(Table A.10) extends the same rows to the goal, the KPIs and the decisions.

===== reports/milestone-2/report/07-02-gaps-revisions.md @ 19d35a4 =====
## 7.2. Data Gaps and Controlled Revisions

**The rules applied.** No question is fully covered, but each keeps its core, so the brief's gap rules lead to
narrowing rather than dropping a question [1]. Partial coverage allows a question to be kept or narrowed with its
limits stated, and a prescriptive question without evidence of actions stays a future decision requirement with a
lower claim [1]. We applied these rules to each question as follows.

**AQ1 and AQ2.** Both keep their outcome, module, module-run and timing parts, and lose the comparisons and the
attendance sign that OULAD does not hold (Table 7.1; C04, C05).

**AQ3.** The predictive question keeps its target, its two cut-offs and its test on a later module run, with three
limits. First, before the end of week 2 almost no module run has a task due, so the week-3 list rests on activity alone
(C06). Second, each module and start month has at most one earlier run to learn from, so the method trains on the 2013
runs and is tested on the 2014 runs of the 9 module and start-month pairs that have both (C07). Module CCC and the
February runs of EEE and GGG have no earlier run of the same start month, so they can test a method trained on other
runs but cannot train one of their own. Third, the comparison between first-year and later-year students cannot be
made, so it is replaced by a check across deprivation band and disability, which OULAD records (C04). In addition, OULAD records no date on which marks were released, so task scores are not
used as features for either list; only whether and when tasks were submitted is used, as Table 2.3 requires.

**The first secondary KPI.** The early-sign rule needs two or more missed or late tasks by the end of week 4, but two
tasks fall due by then in only 1 of the 22 module runs. On OULAD, the sign part of this KPI is therefore measured with
one missed or late task in the 16 runs that have a task due by the end of week 4, a stated deviation recorded with C06;
the rule as defined stays the measure for the university's courses, whose assessment calendars the pilot will check.

**AQ4.** The prescriptive question keeps its ranking under an assumed weekly capacity: the AQ3 ordering can be cut at a
list length and judged by recall and precision. The contact record, the outcome after contact and the follow-up KPI
remain requirements for the pilot, and no claim about the effect of a contact will be drawn from OULAD (C08).

**What does not change.** The Business Goal, the SMART Goal and the decisions are unchanged. The eight controlled
revisions, C01 to C08, are summarised in Section 1.2 and given in full in Appendix V, with the old and new content, the
data evidence and the effect of each.

===== reports/milestone-2/report/08-00-risks-ethics.md @ 19d35a4 =====
# 8. Risks, Ethics and Limitations

The collected data are open and anonymised, but they still describe real students, and the gaps of Section 7 limit
what the later milestones may claim. This part sets out how the data are protected, how far they represent the
project's setting, and which claims they cannot support.

**Privacy.** OULAD was anonymised before release: student identifiers were replaced by random numbers, dates are
given as days relative to the start of each run, and the data meet k-anonymity with k = 5 [3], meaning that every
combination of the identifying attributes is shared by at least five students. The data still hold sensitive
attributes, among them the deprivation band of the student's home area, a ranking of local areas by the United
Kingdom's Index of Multiple Deprivation, and declared disability [3]. We use these attributes only to check
that associations and list accuracy hold across groups, never as reasons to list a student, and we make no attempt
to re-identify anyone. The data stay on our machines under their CC BY 4.0 license [2], with the descriptor
cited, and no record is entered into public AI tools.

**Representativeness.** Representativeness is the largest limit. The data come from UK distance learners in
2013–2014, while the proposal concerns a Vietnamese program's online and blended courses. The modules were also chosen
by the publisher partly because many students failed them [3], so their failure and withdrawal rates are likely to be
higher than a typical program's. Any rate, association or accuracy measured on OULAD therefore describes OULAD, and it
has to be checked again on the university's own records before it informs a decision (C01). The module runs last eight to nine months rather than one semester (C02), and runs that start in February and in October differ in structure [3],
so findings may not carry over between them.

**Claims the data cannot support.** Several claims cannot be supported by these data. No causal statement about
engagement and completion follows from observational records, which show what students did but not why. Nothing can
be learned about the effect of contacting students, because no contact or intervention is recorded (C08). Comparisons
by delivery mode and year of study are impossible (C04).

**Data issues for the next milestone.** Three data issues need decisions in the next milestone, made openly rather
than fixed silently: the 787,170 identical click rows, the 93 withdrawals without a date and, as the descriptor states,
the exam results that are missing for most modules [3]. Each will be handled in the open, with its effect on the
counts reported.

===== reports/milestone-2/report/09-00-genai-reflection.md @ 19d35a4 =====
# 9. Generative AI Usage and Reflection

Generative AI supported this milestone in the roles the brief allows, and no fact about a dataset was accepted from
it without checking the official source, because the brief does not accept AI output as evidence about a dataset [1].
Table 9.1 lists the four uses whose output entered the evidence, each with its control; Appendix VI holds the prompts,
the critiques and our decisions.

**Table 9.1. Roles of generative AI and their controls**

| Role (brief) | How AI was used | Verification |
| :---- | :---- | :---- |
| Search strategist | An AI agent working for us turned the requirement keywords into queries and opened repositories and provider pages, using the prompt in Appendix VI | Every query and hit logged (Appendix I); every fact saved with a quoted passage from the official page and checked by us against that page |
| Metadata interpreter | The same agent summarised units of analysis, outcomes and licenses from data descriptors and repository pages | Facts kept only with a word-for-word quotation; facts the pages left open were checked in the files (Section 6) |
| Requirement critic | An isolated AI critic reviewed the data requirements before any dataset was scored | 12 critiques: 10 accepted, 2 accepted in part (Appendix VI) |
| Selection reviewer | An isolated AI reviewer challenged the scoring and the decision after the scoring | 10 critiques, all accepted (Appendix VI) |

**What the critics changed.** The two critics changed the work in ways we could check. The requirement critic
showed that the gates must require a dated withdrawal and dated tasks, because AQ3 and the first secondary KPI need
both; the gates were revised to require them before any candidate was scored. Its demand that year of study and
delivery mode be must-have requirements was accepted only in part. No open dataset holds them, and a gate that no
dataset can pass would leave only synthetic data, which the brief forbids [1]; the clauses that depend on them were
declared Partial instead. The selection reviewer found that OULAD's first scores rested partly on facts that its
documentation does not state, such as its outcome values and the number of runs per module. The scores were lowered to
what was documented, and the choice was made conditional on the structural check, which confirmed two of the three
conditions.

**How dataset facts were verified.** AI was not used to create data, statistics or license information. Every number
in Sections 5 to 7 comes from the collection and verification scripts, which read the files themselves, and every
dataset fact in Sections 3 and 4 comes from a saved official page with a quoted passage.

**Reflection.** The AI agent made a wide search fast, and the critics found weaknesses that we had not seen, such
as gates that did not yet require the dates on which AQ3 depends. The same speed carries a risk: the first scores
credited OULAD with facts that only seemed obvious. Requiring a quoted source for every score, and a check in the files
for every fact the documentation left open, is what turned AI assistance into evidence we can stand behind.

===== reports/milestone-2/report/10-references.md @ 19d35a4 =====
# References

The references are formatted in APA style (American Psychological Association, 7th edition) and numbered for in-text citation in the form [n], in order of first citation.

[1] MTH045 – The Science of Data Analytics. (2026). *Milestone P2: From requirements to collection* [Course brief]. University of Science, VNU-HCM.

[2] OU Analyse. (n.d.). *Open University Learning Analytics dataset*. The Open University. Retrieved November 6, 2026, from https://research.stem.open.ac.uk/ouanalyse/dataset/

[3] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, *4*, Article 170171. https://doi.org/10.1038/sdata.2017.171

[4] Realinho, V., Vieira Martins, M., Machado, J., & Baptista, L. (2021). *Predict students' dropout and academic success* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5MC89

[5] Realinho, V., Machado, J., Baptista, L., & Martins, M. V. (2022). Predicting student dropout and academic success. *Data*, *7*(11), Article 146. https://doi.org/10.3390/data7110146

[6] Cortez, P. (2008). *Student performance* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T

[7] Yilmaz, N., & Şekeroğlu, B. (2019). *Higher education students performance evaluation* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51G82

[8] MOOCData. (2020). *User activity* [Dataset collection]. Tsinghua University. Retrieved November 6, 2026, from http://moocdata.cn/data/user-activity

[9] Feng, W., Tang, J., & Liu, T. X. (2019). Understanding dropouts in MOOCs. *Proceedings of the AAAI Conference on Artificial Intelligence*, *33*(01), 517–524. https://doi.org/10.1609/aaai.v33i01.3301517

[10] HarvardX. (2014). *HarvardX person-course academic year 2013 de-identified dataset, version 3.0* (Version 11) [Dataset]. Harvard Dataverse. https://doi.org/10.7910/DVN/26147

[11] Amrieh, E. A., Hamtini, T., & Aljarah, I. (2016). *Students' academic performance dataset (xAPI-Edu-Data)* [Dataset]. Kaggle. https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data

[12] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2015). *Open University Learning Analytics dataset* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5KK69

===== reports/milestone-2/report/11-00-appendices.md @ 19d35a4 =====
# Appendices

The appendices hold the evidence behind the main text: the dataset search log (Appendix I), the scoring of every
candidate (Appendix II), the acquisition plan and Data Collection Package (Appendix III), the details of the
structural verification (Appendix IV), the Controlled Change Log and full traceability matrix (Appendix V) and the evidence of generative AI use
(Appendix VI).

===== reports/milestone-2/report/11-01-search-log.md @ 19d35a4 =====
## Appendix I – Dataset Search Log

Table A.1 lists every query and hit examined, including the rejected ones, in the format of the brief (section 7.1). Keywords came from the data requirements of Section 2.

**Table A.1. Dataset search log**

| Date | Query / source | Candidate dataset | URL/DOI | Reason considered | Result |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06 | Brief section 13; web search "Open University Learning Analytics Dataset OU Analyse official dataset page" | OULAD (provider page) | https://research.stem.open.ac.uk/ouanalyse/dataset/ | Higher education, course-level outcome with withdrawal, dated assessments and daily VLE clicks | Kept: candidate A; documentation meets G2a, G2b and G4; G1, G3 and G5 to be checked in the files |
| 2026-11-06 | Data descriptor and UCI record of OULAD | OULAD (documentation) | doi:10.1038/sdata.2017.171; doi:10.24432/C5KK69 | Data dictionary, license, anonymisation of candidate A | Kept: documentation of candidate A |
| 2026-11-06 | Same search | OULAD copies on PMC, CORE, author page; old address analyse.kmi.open.ac.uk | PMC5704676; core.ac.uk/download/153444254.pdf | Copies of the descriptor or superseded address | Rejected: duplicates of the descriptor / redirected address |
| 2026-11-06 | Brief section 13; web search "UCI … Predict Students' Dropout and Academic Success dataset 697" | UCI 697 Predict Students' Dropout and Academic Success | doi:10.24432/C5MC89 | Higher education dropout, CC BY 4.0 | Kept: candidate B; fails G1, G2a, G2b (degree-level label, semester aggregates) |
| 2026-11-06 | Title search "Predicting Student Dropout and Academic Success" | UCI 697 data descriptor | doi:10.3390/data7110146 | Period, target definition, anonymisation of candidate B | Kept: documentation of candidate B |
| 2026-11-06 | Same find | Zenodo, Mendeley Data (2026) and Kaggle (2026) copies of UCI 697 | doi:10.5281/zenodo.5777339; doi:10.17632/k7hrxk9xjg; doi:10.34740/kaggle/dsv/15256262 | Other copies of candidate B | Rejected: Zenodo is the authors' copy of the same data (UCI record used); Mendeley and Kaggle re-uploads have unclear provenance |
| 2026-11-06 | Brief section 13 | UCI 320 Student Performance | doi:10.24432/C5TG7T | Suggested source; grades and student attributes | Kept: candidate C; fails G1, G2a, G2b, G3 (secondary school, grades only) |
| 2026-11-06 | Brief section 13 | UCI 856 Higher Education Students Performance Evaluation | doi:10.24432/C51G82 | Suggested source; higher education performance | Kept: candidate D; fails G1, G2a, G2b, G3 (145-student survey, 2019) |
| 2026-11-06 | Web search "KDD Cup 2015 XuetangX MOOC dropout prediction dataset official download license" | XuetangX dropout data and KDD Cup 2015 data (MOOCData, Tsinghua) | http://moocdata.cn/data/user-activity | MOOC dropout with timestamped activity | Kept: candidate E; G2b met; fails G1, G2a, G4 (no license stated) |
| 2026-11-06 | Same search | KDD Cup 2015 copies on Zenodo, a data-mining blog and Azure ML (per R-bloggers) | zenodo.org/record/5914059; data-mining.philippe-fournier-viger.com | Third-party copies of the KDD Cup 2015 data | Rejected: re-uploads without provenance; official KDD Cup page reported offline |
| 2026-11-06 | Title search "Understanding Dropouts in MOOCs" | XuetangX source paper | doi:10.1609/aaai.v33i01.3301517 | Provenance of candidate E | Kept: documentation of candidate E (abstract only; full text behind captcha) |
| 2026-11-06 | Web search "HarvardX-MITx Person-Course Academic Year 2013 De-Identified dataset Harvard Dataverse" | HarvardX Person-Course AY2013 | doi:10.7910/DVN/26147 | MOOC completion (certification) with de-identified person-course records | Kept: candidate F; fails G1, G2a, G2b, G3 and G4 (no named license) |
| 2026-11-06 | Same search | Release news, blogs, de-identification scripts, ICAR metadata mirror | openlearning.mit.edu; github.com/harvard/de_id; krishi.icar.gov.in | Secondary descriptions of candidate F | Rejected: secondary or not the data |
| 2026-11-06 | Web search "xAPI-Edu-Data students academic performance dataset Amrieh Hamtini Aljarah original source" | xAPI-Edu-Data (University of Jordan group page) | https://research.ju.edu.jo/research/groups/EVO-ML/Pages/Resources.aspx | LMS-based student performance data | Blocked: connection refused; replaced by the authors' Kaggle listing |
| 2026-11-06 | Replacement for the blocked University of Jordan page | xAPI-Edu-Data, Kaggle listing by co-author I. Aljarah | https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data | Found via Kaggle; traced to the authors' own listing | Kept: candidate G; fails G1, G2a, G2b, G3; G4 unclear |
| 2026-11-06 | Same search | MaRDI portal, ISC index, derivative papers | portal.mardi4nfdi.de/wiki/Item:Q6036517 | Secondary metadata about candidate G | Rejected: secondary |

===== reports/milestone-2/report/11-02-scoring-details.md @ 19d35a4 =====
## Appendix II – Candidate Scoring Details

Table A.2 gives each candidate's score on the brief's ten criteria (0 = not met or not stated, 1 = partly met or uncertain, 2 = well met) with the fact behind it, and the must-have gates it fails. Every fact comes from the candidate's official page or descriptor.

The ten criteria ask whether the dataset can answer the questions (AQ coverage), whether its population resembles the project's (population fit), whether its unit and time grain match (unit and granularity), whether it holds the outcome (outcome availability), whether its predictors exist before the prediction point (feature availability and timing), whether it covers enough time (temporal coverage), whether it is documented and traceable (documentation and provenance), whether it may be used (license and access), whether it can be handled (quality feasibility) and whether it is anonymised and representative (ethics and representativeness). Each criterion takes 0 when it is not met or not stated, 1 when it is partly met or uncertain, and 2 when it is well met.

**Table A.2. Scores on the ten criteria and failed gates**

| Criterion | A OULAD | B UCI 697 | C UCI 320 | D UCI 856 | E XuetangX | F HarvardX | G xAPI-Edu |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ coverage | 1 – data for AQ1–AQ3 with partial clauses (no delivery mode, year of study, attendance); AQ4 ranking only | 0 – degree-level, no course timing | 0 – one grade per subject | 0 – questionnaire | 1 – activity and dropout, no assessments | 0 – aggregates | 0 – one grade band |
| Population fit | 1 – higher education, distance learning, UK; modules chosen partly for high failure | 1 – higher education, Portugal | 0 – secondary school | 1 – higher education, one 2019 collection | 1 – MOOC learners, China | 1 – MOOC learners | 0 – users of a school learning platform |
| Unit and granularity | 2 – student–module–run; daily activity | 0 – student | 0 – student–subject | 0 – student questionnaire | 1 – user–course, timestamped | 1 – user–course aggregates | 0 – student record |
| Outcome / target | 1 – Withdrawal recorded with a date; the other result values not stated in the documentation read | 1 – degree dropout / graduate | 1 – grade 0–20 | 1 – letter grade | 1 – binary dropout | 1 – certification only | 1 – grade band |
| Feature availability and timing | 1 – dated assessments, submissions and clicks; mark release dates not recorded, unsubmitted tasks leave no row, tasks in weeks 1–4 not stated | 0 – semester aggregates | 0 – period grades | 0 – none | 1 – dated actions, no assessments | 0 – first and last event only | 0 – none dated |
| Temporal coverage | 1 – 22 runs over 2013–2014, ordered by code; runs per module not stated | 1 – 11 entry cohorts, no cohort field documented | 0 – one year | 0 – one collection | 1 – two years; runs of a course not stated | 0 – one year | 0 – two undated semesters |
| Documentation and provenance | 1 – descriptor and DOI, but no version number and two distribution points | 2 – UCI page, descriptor, DOI | 1 – variable list | 1 – question list | 1 – column list, paper blocked | 2 – versioned deposit with checksum | 0 – Kaggle listing only |
| License and access | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 2 – CC BY 4.0 | 0 – no license stated | 0 – community norms, no open license | 1 – CC BY-SA on a Kaggle listing |
| Quality feasibility | 1 – CSV, 10.7 million click rows; unsubmitted tasks leave no row, exam results mostly missing | 2 – one clean CSV | 2 – small CSV | 2 – small CSV | 1 – large logs | 2 – one table | 2 – small CSV |
| Ethics and representativeness | 1 – anonymised (k = 5); deprivation (IMD) band and disability present; high-failure module selection | 1 – anonymised under the EU General Data Protection Regulation | 0 – anonymisation not stated | 0 – not stated | 0 – not stated | 1 – de-identified | 0 – not stated |
| **Total (of 20)** | **12** | **10** | **6** | **7** | **8** | **8** | **4** |
| Gates failed (documented evidence) | none; G1 pass/fail values, G3 per module and G5 linkage across runs to confirm in the structural verification (Section 6) | G1, G2a, G2b | G1, G2a, G2b, G3 | G1, G2a, G2b, G3 | G1, G2a, G4 | G1, G2a, G2b, G3, G4 | G1, G2a, G2b, G3; G4 unclear |

===== reports/milestone-2/report/11-03-acquisition-package.md @ 19d35a4 =====
## Appendix III – Acquisition Plan and Data Collection Package

The Data Collection Package re-creates our copy of OULAD exactly. Its layout is shown below; the raw files are produced by the collection script and are not edited.

```text
package/
  README.md
  data/raw/        published files, unchanged
  metadata/        source.md, citation.bib, data_dictionary.md, raw_manifest.csv,
                   collection_log.txt, structure_report.md, structure_results.json
  src/             collect.py (download, verify, extract), verify_structure.py (Section 6)
```

Table A.3 is the source and license sheet of the package.

**Table A.3. Source, license and citation**

| Item | Value |
| :---- | :---- |
| Dataset title | Open University Learning Analytics Dataset (official title) |
| Provider / authors | Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal; Knowledge Media Institute, The Open University (UK) |
| Official pages | Provider page: https://research.stem.open.ac.uk/ouanalyse/dataset/ ; data descriptor: https://doi.org/10.1038/sdata.2017.171 |
| Copy collected | figshare deposit cited by the data descriptor, DOI https://doi.org/10.6084/m9.figshare.5081998.v1 (version 1), file https://ndownloader.figshare.com/files/8606371 |
| Other distributions | UCI Machine Learning Repository, DOI https://doi.org/10.24432/C5KK69 (same data; missing values written "?" instead of empty); the provider page's own link http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip returned HTTP 404 on 2026-11-05 |
| Access date | 6 November 2026 (UTC+7; 2026-11-05 18:24 UTC in `metadata/collection_log.txt`) |
| Version | figshare version 1 (the provider page offers "the latest version" without a number) |
| License | Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ |
| Acquisition method | Direct download of one zip archive, verified against pinned SHA-256 values, extracted unchanged (`src/collect.py`) |
| Integrity evidence | `metadata/raw_manifest.csv` (bytes, SHA-256, MD5, data rows per file); `metadata/collection_log.txt` |
| Citation | Kuzilek, Hlosta and Zdrahal (2017), *Scientific Data*, 4, Article 170171, https://doi.org/10.1038/sdata.2017.171 (full entry in citation.bib) |

Table A.4 lists the size, checksums and data rows of every collected file; each table matched its pinned SHA-256.

**Table A.4. Raw file manifest**

| File | Bytes | SHA-256 | MD5 | Data rows | Check |
| :---- | :---- | :---- | :---- | :---- | :---- |
| anonymisedData.zip | 46,750,706 | 90dda45037939953f979072fa70a809ebe07e90ec783c408762af7698a3825ec | 7412686fd77cf0e0ee1e8c3e9b354308 |  | MATCH |
| courses.csv | 526 | 4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75 | 4c3df8a42a98a0d26b22f507007c31a8 | 22 | MATCH |
| assessments.csv | 8,200 | 8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1 | 6126f9d435767bcc70134b46f21c2a90 | 206 | MATCH |
| vle.csv | 260,126 | d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9 | 0e7ef38c483daca42900ca426b66f8da | 6,364 | MATCH |
| studentInfo.csv | 3,461,652 | 7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6 | ead11d001fe8b7aed1469daa643a812c | 32,593 | MATCH |
| studentRegistration.csv | 1,109,984 | 0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170 | ef06e3d5784dc7dffe06ef911c5b190c | 32,593 | MATCH |
| studentAssessment.csv | 5,690,310 | fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e | 9ceb38acaeb26fbc15c98b563290c1db | 173,912 | MATCH |
| studentVle.csv | 453,836,331 | 52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0 | b8aae6f4ffd1523319aeb56d66b17f72 | 10,655,280 | MATCH |

OULAD is published in three places, so we had to decide which copy to collect and cite. The provider page links an archive on the Open University's own server [2] and asks users to check it against an MD5 checksum [2]; that link returned an HTTP 404 error, meaning that the file was not found, when the data were collected. The data descriptor, the peer-reviewed article that documents the dataset, cites a deposit on figshare [3], which carries a DOI and a version number; this is the copy we collected. The UCI repository holds a third copy under its own DOI [12]. To make sure the copies agree, we compared the UCI copy with the collected files. All seven tables hold the same rows. The only difference is that UCI writes a missing value as "?" where figshare leaves the cell empty, in five tables (Table A.5). The analysis therefore reads empty cells as missing values and cites the figshare deposit and the descriptor.

Table A.5 compares the UCI copy of OULAD with the collected figshare files, table by table.

**Table A.5. Comparison of the UCI copy with the collected files**

| Table | Figshare bytes | UCI bytes | Same SHA-256 | Line endings (figshare / UCI) | Rows (figshare / UCI) | Same rows |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| assessments.csv | 8200 | 8211 | False | CRLF / CRLF | 206 / 206 | only missing values written '?' in UCI, empty in figshare (11 rows) |
| courses.csv | 526 | 526 | True | CRLF / CRLF | 22 / 22 | True |
| studentAssessment.csv | 5690310 | 5690483 | False | CRLF / CRLF | 173912 / 173912 | only missing values written '?' in UCI, empty in figshare (173 rows) |
| studentInfo.csv | 3461652 | 3462763 | False | CRLF / CRLF | 32593 / 32593 | only missing values written '?' in UCI, empty in figshare (1111 rows) |
| studentRegistration.csv | 1109984 | 1132550 | False | CRLF / CRLF | 32593 / 32593 | only missing values written '?' in UCI, empty in figshare (22560 rows) |
| studentVle.csv | 453836331 | 453836331 | True | CRLF / CRLF | 10655280 / 10655280 | True |
| vle.csv | 260126 | 270612 | False | CRLF / CRLF | 6364 / 6364 | only missing values written '?' in UCI, empty in figshare (5243 rows) |

===== reports/milestone-2/report/11-04-structure-details.md @ 19d35a4 =====
## Appendix IV – Structural Verification Details

Table A.6 gives, for each table, the headers found, the types inferred from the text values and the missing cells; Table A.7 lists the counts that settle the selection conditions.

**Table A.6. Headers, inferred types and missing values**

| Table | Headers and inferred types | Missing cells |
| :---- | :---- | :---- |
| courses | code_module (text), code_presentation (text), module_presentation_length (integer) | none |
| assessments | code_module (text), code_presentation (text), id_assessment (integer), assessment_type (text), date (integer), weight (decimal) | date 11 |
| vle | id_site (integer), code_module (text), code_presentation (text), activity_type (text), week_from (integer), week_to (integer) | week_from 5,243, week_to 5,243 |
| studentInfo | code_module (text), code_presentation (text), id_student (integer), gender (text), region (text), highest_education (text), imd_band (text), age_band (text), num_of_prev_attempts (integer), studied_credits (integer), disability (text), final_result (text) | imd_band 1,111 |
| studentRegistration | code_module (text), code_presentation (text), id_student (integer), date_registration (integer), date_unregistration (integer) | date_registration 45, date_unregistration 22,521 |
| studentAssessment | id_assessment (integer), id_student (integer), date_submitted (integer), is_banked (integer), score (integer) | score 173 |
| studentVle | code_module (text), code_presentation (text), id_student (integer), id_site (integer), date (integer), sum_click (integer) | none |

Table A.7 gives the counts that decide the selection conditions G1, G3 and G5, the timing of the first tasks and the KPI denominator.

**Table A.7. Counts behind the selection conditions and the denominator**

| Check | Result |
| :---- | :---- |
| Result values | Pass 12,361, Withdrawn 10,156, Fail 7,052, Distinction 3,024 |
| Withdrawn with / without an unregistration day; other results with one | 10,063 / 93 ; 9 |
| Students; students in more than one run | 28,785; 3,538 |
| Same-module repeats; repeats with a higher attempt count | 1,309; 1,309 |
| Runs per module | AAA: 2013J, 2014J; BBB: 2013B, 2013J, 2014B, 2014J; CCC: 2014B, 2014J; DDD: 2013B, 2013J, 2014B, 2014J; EEE: 2013J, 2014B, 2014J; FFF: 2013B, 2013J, 2014B, 2014J; GGG: 2013J, 2014B, 2014J |
| Runs with a non-exam task due by day 13 / day 27 (of 22) | 1 / 16 |
| First non-exam task due day per run | AAA-2013J 19, AAA-2014J 19, BBB-2013B 19, BBB-2013J 19, BBB-2014B 12, BBB-2014J 19, CCC-2014B 18, CCC-2014J 18, DDD-2013B 23, DDD-2013J 25, DDD-2014B 25, DDD-2014J 20, EEE-2013J 33, EEE-2014B 33, EEE-2014J 33, FFF-2013B 19, FFF-2013J 19, FFF-2014B 24, FFF-2014J 24, GGG-2013J 61, GGG-2014B 61, GGG-2014J 61 |
| Exams without a due day | 11 |
| Unregistered on or before day 0; registered after day 14; registration day missing | 3,097; 58; 45 |
| Still registered on day 14 | 28,119 |
| Rows without a parent (assessment, submission, click enrolment, click site) | 0, 0, 0, 0 |

===== reports/milestone-2/report/11-05-change-log.md @ 19d35a4 =====
## Appendix V – Controlled Change Log and Full Traceability

The Milestone 1 baseline was frozen before the search: Table A.8 lists the proposal files it was copied from, with their SHA-256, so any later edit to them is detectable. Table A.9 records every change to the baseline with its data evidence, in the format of the brief (section 3.1).

**Table A.8. Frozen Milestone 1 files**

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

Table A.9 gives each change with the old and new content, the data evidence and its effect on the questions, KPIs and decisions.

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

Table A.10 is the full traceability matrix of deliverable B: every row serves the Business Goal of improving successful course completion by identifying students who stop taking part early enough to support them within the semester, and links its KPI, question, data requirement, files, actual variables, coverage and decision.

**Table A.10. Full traceability from goal to decision with coverage**

| Business Goal / SMART Goal / KPI | AQ | Analytics type | Data requirement | Dataset / file | Actual variables | Coverage | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Completion rate in pilot courses, assumed 70% → 75% by end 2027–2028 (primary KPI) | AQ1 | Descriptive | Outcome by course and time; first missed task | studentInfo, studentRegistration, assessments, studentAssessment | final_result, date_unregistration, assessments.date, date_submitted | Partial | D2, D3 |
| Primary KPI; secondary KPI 1, early-sign contact rate (sign part) | AQ2 | Diagnostic | Signs in weeks 1–4 against later outcome | + studentVle, vle | sum_click, studentVle.date, date_submitted | Partial | D2; reasons in D1 |
| Secondary KPI 1 (sign part) | AQ3 | Predictive | Target and features by the cut-off; later run for testing | as AQ2 | as AQ2 + num_of_prev_attempts, studied_credits, imd_band, disability | Partial | D1 |
| Secondary KPI 2, follow-up rate; secondary KPI 1 (contact part) | AQ4 | Prescriptive | Ranking within capacity; contact record | AQ3 outputs | none for contacts | Partial / None | D1 |

===== reports/milestone-2/report/11-06-ai-evidence.md @ 19d35a4 =====
## Appendix VI – Generative AI Usage Evidence

An AI agent searched for candidate datasets for us with the prompt below, in which documents are named by the report section that holds them and the agent's file-handling steps are left out; every query it ran is in Appendix I, and every fact it recorded was checked by us against the saved official page.

Prompt of the search strategist and metadata interpreter:

```text
You are the research agent for the dataset search of the MTH045 Milestone 2 report ("From requirements to collection").

1. Record every search, fetch and interpretation before the next step, and anchor every fact in a verbatim quote from its source.
2. Read the team's data requirements and the must-have gates G1–G5 (Section 2) and the brief sections 7–8 and 13. Build search keywords from the requirements (e.g. student completion, dropout, withdrawal, LMS/VLE interaction, assessment submission, clickstream, higher education, learning analytics, MOOC dropout).
3. Find and document at least six candidate open education datasets from official sources (landing page, DOI, repository of the provider, or the original paper), reading the documentation/data dictionary and license page of each before judging it. Include at least: OULAD (official page https://research.stem.open.ac.uk/ouanalyse/dataset/ and the Scientific Data paper), UCI "Predict Students' Dropout and Academic Success" (id 697), UCI "Student Performance" (id 320), UCI "Higher Education Students Performance Evaluation" (id 856), and at least two more found by your own search (for example KDD Cup 2015 / XuetangX MOOC dropout data, MOOCCubeX, EdNet, HarvardX-MITx person-course data, xAPI-Edu-Data). When a dataset is found via Kaggle/blog/GitHub, trace it to the official source or record that provenance is unclear.
4. For each candidate record facts with quote anchors: provider/authors, official URL/DOI, license or terms, version/release date, population and context (level, country, years), unit of analysis, outcome/target available (does it separate pass, fail and withdrawal?), within-semester timing (dated activity or dated assessments? granularity), number of semesters/course runs, size (rows/records), file formats, documentation available, anonymisation, sensitive attributes, citation. Only facts found on the source pages; write "not stated" otherwise.
5. Write one section per candidate with those fields, each fact followed by its source, and a short note per gate G1–G5 (met / partly / not met / unclear, with the evidence). Also write the brief's Search Log table (| Date | Query / source | Candidate dataset | URL/DOI | Reason considered | Result |), one row per query/candidate examined, including rejected ones.
6. Do not download any dataset.

Return at most 6 lines: candidates documented, sources fetched/partial/blocked, facts recorded, gate result per candidate in one line, unresolved questions.

Follow-up message sent during the task: the must-have gates were revised (G1 also requires a dated withdrawal; G2 split into G2a dated assessed tasks and G2b dated activity; G3 at least three course runs ordered in time with a later run for testing; G5 adds a persistent pseudonymous identifier); write the gate notes against the revised gates and note early tasks and enrolment dates per candidate.
```

Two isolated AI agents critiqued the work at fixed points: a requirement critic before any dataset was scored, and a selection reviewer after the scoring. Each received only the brief and our documents named in its prompt. Their prompts are given in English, with documents named by the report section that holds them; Tables A.11 and A.12 give each critique in short form with our decision and the change made.

Prompt of the requirement critic:

```text
You act as the "Requirement critic" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Chỉ ra AQ nào cần timestamp, target, intervention data hoặc có leakage risk"). Read only: the brief, the team's frozen Milestone 1 baseline (Section 1.1) and the team's data requirements (Section 2). Do not read any dataset file or exploration result, and do not search the web.

Critique the data requirements: for each AQ, is anything missing (timestamps, target definition, denominator, prediction point, intervention data), is any requirement written as a dataset's column rather than a concept, is there leakage risk not covered, are the must-have gates G1–G5 right (too strict, too loose, missing one), and are the requirements consistent with the baseline (KPIs, decisions)? Do not propose datasets and do not rewrite the document.

Write at most 12 numbered critiques, most important first, each with: the passage (quote a few words), the problem, why it matters.
```

Table A.11 lists the requirement critic's twelve critiques with our decisions.

**Table A.11. Requirement critic: AI critique, our decision and change**

| # | Critique (short) | Decision | Change |
| :---- | :---- | :---- | :---- |
| Q1 | Withdrawal date only nice-to-have, though AQ3 needs it | Accepted | G1 now requires a dated withdrawal |
| Q2 | G2 accepts dated activity alone; AQ3 rule and secondary KPI 1 need dated tasks | Accepted | G2 split: G2a dated assessed tasks and submissions, G2b dated learning-platform activity; tasks due in weeks 1–4 is a nice-to-have, reported per module run |
| Q3 | KPI denominator (add-drop, leave, transfer) not required | Accepted | Enrolment start and end dates relative to the course start are minimum variables; leave/transfer distinction stays optional and its absence is recorded as a KPI deviation |
| Q4 | Year of study and delivery mode optional though AQs name them | Partly accepted | They stay optional, because a gate no open dataset can meet would leave only synthetic data, which the brief forbids; the clauses that become Partial without them are declared now |
| Q5 | G3 three runs against AQ1 four semesters; no time order | Accepted | G3: at least three course runs ordered in time, a later run available for testing; AQ1 is Partial with fewer than four semesters |
| Q6 | Missing leakage paths (course average, mark release, study load, updated background, normalisation) | Accepted | Leakage table extended with five rows |
| Q7 | Missed tasks counted after withdrawal | Accepted | Rule: a task counts as missed only if due before the student's withdrawal date |
| Q8 | Week numbering and data delay unspecified | Accepted | Course start date is a minimum variable; the cut-offs (ends of weeks 2 and 4) already leave one week for the data delay before the lists in weeks 3 and 5 |
| Q9 | No gate for identifiers that link across tables and courses | Accepted | G5 requires a persistent pseudonymous student identifier across tables, courses and semesters |
| Q10 | No volume or outcome-distribution requirement | Partly accepted | Nice-to-have: at least 100 later non-completers per compared group in the test run (an assumption to confirm in Milestone 3) |
| Q11 | AQ4 mixes data and assumptions; advisor assignment missing; contact record known not to exist | Accepted | Capacity labelled as a baseline assumption; advisor assignment added as optional; one list entry per student across courses; contact record declared a gap now; referral data marked sensitive |
| Q12 | Wording names fields or systems; grade mapping unclear | Accepted | Concept wording ("withdrawal indicator and date", "enrolment start and end dates", "dated learning-platform activity"); any passing grade, including higher grades, counts as completion |

Prompt of the selection reviewer:

```text
You act as the "Selection reviewer" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Phản biện Dataset Selection Matrix và phát hiện criteria bị bỏ sót"; "Không chấp nhận recommendation nếu không có evidence"). Read only: the brief, the requirements and gates (Section 2), the candidate facts with their sources and verbatim quotes, and the team's scoring and decision (Section 4). Check that each score rests on a recorded fact. Do not search the web and do not open any dataset file.

Challenge the selection: scores not backed by a recorded fact, criteria applied inconsistently across candidates, gates that were misread, a candidate rejected or kept for a weak reason, a criterion the brief lists that is missing, a supplementary dataset that should have been considered, and anything about the selected dataset that the team treats as settled without evidence. Do not rescore the matrix yourself and do not propose new datasets unless you name the evidence gap they would close.

Write at most 10 numbered critiques, most important first, each with the passage, the problem and why it matters.
```

Table A.12 lists the selection reviewer's ten critiques with our decisions.

**Table A.12. Selection reviewer: AI critique, our decision and change**

| # | Critique (short) | Decision | Change |
| :---- | :---- | :---- | :---- |
| S1 | G3 treated as passed, uncertain per module | Accepted | Selection conditional on the structural check; fallback named |
| S2 | G5 "Partly" missing from the gate decision | Accepted | Conditional on the structural check; Partial clauses named |
| S3 | Outcome classes claimed without a recorded fact | Accepted | Outcome scored 1; pass/fail values checked in the structural check |
| S4 | Feature timing scored 2 with open conditions | Accepted | Scored 1; mark release, unsubmitted tasks and early tasks noted |
| S5 | High-failure module selection ignored | Accepted | Added to population fit, ethics and rationale |
| S6 | Inconsistent scoring of "not stated" and gate lists | Accepted | "Not stated" scores 0 everywhere; HarvardX fails G4; xAPI G4 unclear; the recorded fact named for every score; unsupported figures removed |
| S7 | AQ coverage 2 despite Partial clauses | Accepted | Scored 1 |
| S8 | No version number, two distribution points | Accepted | Documentation scored 1; the acquisition records which copy and its checksums |
| S9 | Denominator not tested | Accepted | The structural check counts unregistration on or before day 0 |
| S10 | Supplementary dataset reasoning | Accepted | Real blocker for XuetangX (license, outcome) named; external-validity check recorded as an open limitation |
