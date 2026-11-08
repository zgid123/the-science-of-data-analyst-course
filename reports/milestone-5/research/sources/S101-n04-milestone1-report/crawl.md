---
id: S101
url: reports/milestone-1/report/00-1-abbreviations.md
requested: reports/milestone-1/report/00-1-abbreviations.md reports/milestone-1/report/00-2-glossary.md reports/milestone-1/report/01-00-project-context.md reports/milestone-1/report/01-01-situation-background.md reports/milestone-1/report/01-02-problem-statement-scope.md reports/milestone-1/report/02-00-stakeholder-analysis.md reports/milestone-1/report/02-01-stakeholder-map.md reports/milestone-1/report/02-02-interview-approach.md reports/milestone-1/report/02-03-requirement-synthesis.md reports/milestone-1/report/02-04-conflicts-validation.md reports/milestone-1/report/03-00-goals-kpis.md reports/milestone-1/report/03-01-business-goal.md reports/milestone-1/report/03-02-smart-goal.md reports/milestone-1/report/03-03-kpis.md reports/milestone-1/report/04-00-question-ladder.md reports/milestone-1/report/04-01-four-level-questions.md reports/milestone-1/report/04-02-quality-check-refinement.md reports/milestone-1/report/05-00-analytic-approach.md reports/milestone-1/report/06-00-data-feasibility.md reports/milestone-1/report/06-01-data-requirements.md reports/milestone-1/report/06-02-feasibility-privacy.md reports/milestone-1/report/07-00-decision-value.md reports/milestone-1/report/08-00-genai-reflection.md reports/milestone-1/report/09-00-traceability-matrix.md reports/milestone-1/report/10-references.md reports/milestone-1/report/11-00-appendices.md reports/milestone-1/report/11-01-interview-questions.md reports/milestone-1/report/11-02-interview-excerpts.md reports/milestone-1/report/11-03-validation-round.md reports/milestone-1/report/11-04-ai-critique-review.md reports/milestone-1/report/11-05-published-evidence.md reports/milestone-1/report/11-06-synthesis-detail.md reports/milestone-1/report/11-07-goal-kpi-detail.md reports/milestone-1/report/11-08-question-specification.md reports/milestone-1/report/11-09-approach-data-decision-detail.md
fetched: 2026-11-08T23:21+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 35 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T05
part: 1
raw: raw.txt (121 KB)
conversion: verbatim copy of 35 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-1/report/00-1-abbreviations.md @ 19d35a4 =====
# List of Abbreviations

The abbreviations below are listed in alphabetical order, each with its full form and its role in this report.

| Abbreviation | Full form | Role in this report |
| :---- | :---- | :---- |
| AI | Artificial intelligence | Generative AI played the stakeholders, acted as interviewer and reviewer, and assisted research (Section 8) |
| AQ | Analytical question | The four questions of the question ladder, AQ1 to AQ4 (Section 4) |
| KPI | Key performance indicator | The primary and secondary measures of progress towards the SMART Goal (Section 3.3) |
| LMS | Learning management system | The university's online learning platform and a main data source (Sections 1.1 and 6.1) |
| SMART | Specific, measurable, achievable, relevant and time-bound | The criteria of the project's goal (Section 3.2) |

===== reports/milestone-1/report/00-2-glossary.md @ 19d35a4 =====
# List of Terms

| Term | Meaning in this report |
| :---- | :---- |
| Academic warning list | The list of students whose results at the end of a semester fall below the university's threshold (Section 1.2) |
| Add-drop period | The first weeks of a semester in which students may still register for or drop a course; the project counts enrolments after it (Section 1.2) |
| Blended course | A course that combines lessons on the LMS with sessions in a classroom (Section 1.1) |
| Contact record | A shared log of who contacted which student, when, how and with what result; a new data requirement (Section 3.3) |
| Course completion | Passing the course; a fail or a withdrawal from the course counts as non-completion (Section 1.2) |
| Data cut-off | The last day whose data may be used for a list, one week before the list reaches staff: the end of week 2 for the week-3 list and the end of week 4 for the week-5 list (Section 3.3) |
| Data office | The office of the Learning Technology and Data Officer, which runs the LMS and the extracts of academic records (Section 2.1) |
| Early-sign rule | Two or more assessed tasks missed or submitted late by the end of week 4; the basis of the first secondary KPI and the simple rule that AQ3 must beat (Section 3.3) |
| Lecturer-advisor | A lecturer who also acts as academic advisor (cố vấn học tập) for one or two classes of students (Section 2.3) |
| Online course | A course taught entirely through the LMS (Section 1.1) |
| Persona | The role description, grounded in published accounts, that an AI followed when it answered as a stakeholder (Section 2.2) |
| Pilot courses | A small number of the program's online and blended courses, fixed before the pilot in Semester 2 of 2026–2027 and compared with similar courses outside the pilot (Section 3.2) |
| Precision | The share of students on a list who later fail or withdraw (Section 4.1) |
| Recall | The share of students who later fail or withdraw who appear on a list (Section 4.1) |
| Review point | A moment in the semester when a contact list reaches staff: week 3 and week 5 (Section 2.4) |
| Support office | The student support office, which advises and supports students across the faculty (Section 2.1) |
| Validation round | The return to each stakeholder with our understanding, to confirm, correct and add (Section 2.4) |

===== reports/milestone-1/report/01-00-project-context.md @ 19d35a4 =====
# 1. Project Context and Problem Statement

This part describes the university's situation and the evidence on non-completion (Section 1.1), then states the
problem, the scope of the project and why analytics is needed (Section 1.2).

===== reports/milestone-1/report/01-01-situation-background.md @ 19d35a4 =====
## 1.1. Situation and Background

**The university's situation.** A university in Vietnam is expanding online and blended learning. An online course
is taught entirely through the university's learning management system (LMS), the web platform on which lecturers
publish materials, quizzes and assignments and on which students submit their work. A blended course combines
lessons on the LMS with sessions in a classroom. The project concerns one undergraduate program of the university, with about 1,200
students in a faculty of about 4,000 (both scenario assumptions), called the program below. In several online and
blended courses, the university has noticed that
students take part less as the semester goes on, and that some of them do not complete the course. The university
holds data that could describe this: activity records from the LMS, enrolment and result records in its academic
management system, assignment and quiz results, grades and student surveys. It has not yet decided which questions
these data should answer, or which decisions analytics should support [1]. This university is the scenario given by
the course brief, so every figure about it in this proposal is an assumption, marked as such. The figures in the
rest of this section come from published sources about real institutions.

**Online learning and withdrawal in Vietnamese regulation.** Online teaching is now part of regular degree programs
in Vietnam: since 2021, a full-time program may deliver up to 30% of its content online [2]. Withdrawal of students
is also a regulated measure of a university's quality. Circular 01/2024 of the Ministry of Education and Training
limits the share of students who withdraw to 10% a year overall and 15% in the first year of study, and a university
whose first-year withdrawal exceeds 15% may not raise its enrolment quota [3]. Circular 83/2026, in force from
15 November 2026, keeps both limits, and in addition no longer counts approved leave or transfers to another program
as withdrawal [4]. As a result, a university now needs exact records of each student's status, and it has a direct
interest in finding students who are drifting away while they can still be helped.

**What published studies report.** Published studies show that non-completion is common, that it starts early and
that institutions respond by contacting students early. Retention is lower in online courses than in face-to-face
ones [5], and a Vietnamese review puts university dropout at about 20–30%, highest in the first year [6]. In massive
open online courses, participation falls most sharply in the first two weeks [7], and in one blended first-year course
the best moment for an early warning was weeks 5–6, while warnings based on midterm grades came too late [8]. Students
who leave online courses most often name health, finances, technology, isolation and workload [9]. The response most
often recommended is early, proactive contact based on data from the first weeks of the semester [5], [10]. Appendix V
sets out these findings in detail.

===== reports/milestone-1/report/01-02-problem-statement-scope.md @ 19d35a4 =====
## 1.2. Problem Statement, Scope and the Need for Analytics

**The problem.** Building on this background and on interviews with five simulated stakeholders (Section 2), the
problem is that, in the program's online and blended courses, students who stop taking part are noticed late and
only some of them are noticed at all. Each group of staff sees the problem at a different moment. (A code in
parentheses, such as CL5, points to a stakeholder's quoted statement; Section 2 explains the codes.) Lecturers notice
some silent students, but usually only around week 5 or 6, when they are sure that a student has gone quiet (CL5).
The program manager sees pass and withdrawal counts only after the semester has closed (PM1). The student support
office, which advises and supports students across the faculty, meets most of these students only when they appear
on the academic warning list, the list of students whose results at the end of a semester fall below the
university's threshold (AD1). In every case, the moment of notice comes after the moment at which help would have
been easiest.

The stakeholders place the start of disengagement in the first weeks of the semester, which matches the published
studies of Section 1.1 [7], [8]. They also estimate that staff can follow up only a few dozen students a week (AD3,
CL10; Section 2.3). Both points are the stakeholders' own estimates, which the data audit of Milestone 2 will check. Finally, staff have no shared,
timely and trusted information on whom to contact first and why, so each lecturer or officer decides alone, from
whatever they happen to see (AD7).

**The scope.** The project covers students enrolled in the program's online and blended courses after the add-drop
period, the first weeks of a semester in which students may still register for or drop a course. Students who leave
during the add-drop period are not counted, because their enrolment was never settled. The project works one semester
at a time, and it covers the decisions that staff can take within a semester: whom to contact, when, by whom and with
which offer of support. Because institutions define retention in different ways, the measures are fixed before any
analysis [5]: course completion means passing the course, and withdrawal follows the definition of Circular 83/2026,
which excludes approved leave and transfers [4].

Outside the scope are assessment rules, which a lecturer cannot change during a semester (CL7); admissions and
financial aid, which are university policy; students' circumstances outside the course, which the university cannot
control, so the project addresses its response to them; the evaluation of lecturers, which would stop lecturers using
the results (CL9); and any automated decision about a student (AD9, DO9). Appendix VI gives each reason in full.

**Why analytics is needed.** The information needed to act earlier already exists but is not used for this purpose.
Published early-warning work draws on three kinds of data that universities already hold: student background
records, continuous-assessment results such as quizzes and assignments during the semester, and LMS activity [8]. In
addition, the new withdrawal rules require student-level status records [4]. Analytics can turn these records into
two things that staff do not have today: a short, timely list of students to contact, with an observed reason for
each name, and patterns by course and student group that show the program where students are lost. Data never give
a complete picture of a student's situation [11], so these results support the judgement of the staff who know the
students rather than replace it.

===== reports/milestone-1/report/02-00-stakeholder-analysis.md @ 19d35a4 =====
# 2. Stakeholder Analysis and Requirement Findings

This part maps the stakeholders (Section 2.1), describes how generative artificial intelligence (AI) was used
to carry out the interviews (Section 2.2), synthesises the answers into themes and priorities (Section 2.3), and
records the conflicts and the validation round (Section 2.4).

Throughout the proposal, a short code in parentheses, such as (PM1) or (VAD5), points to the stakeholder's own words.
The letters name the stakeholder (PM program manager, CL course lecturer, AD support officer, ST student, DO data
officer), a leading V marks a statement from the validation round, and the number orders the statements of one
stakeholder. Appendix II quotes every interview statement word for word, and Appendix III quotes every validation
statement.

===== reports/milestone-1/report/02-01-stakeholder-map.md @ 19d35a4 =====
## 2.1. Stakeholder Map

The brief requires at least three stakeholders: the Academic Program Manager, the Course Lecturer, and the Academic
Advisor or Student Support Officer [1]. In this proposal the third role is an officer of the student support office,
the faculty office that advises and supports students (the support officer and the support office below). The
academic advisors of student classes (cố vấn học tập) are lecturers, called lecturer-advisors below. We added two more
stakeholders, because the proposal would be incomplete without their views. The Student is the person on whom every
decision of the project acts, and the source of the privacy and trust concerns that the brief asks us to
consider. The Learning Technology and Data Officer runs the LMS and the extracts of academic records; this officer's
office (the data office below) decides whether the data needs of Section 6 can be met at all, so the feasibility of
the proposal rests on its view.

Table 2.1 lists each stakeholder's role in the problem, the goal we assumed for that stakeholder before any
interview, and the decision that analytics might support. These goals and decisions were hypotheses, written down
so that the interviews could test them.

**Table 2.1. Stakeholders, initial assumed goals and decisions possibly supported**

| Stakeholder | Role in the problem | Initial assumed goal | Decision possibly supported |
| :---- | :---- | :---- | :---- |
| Program Manager (PM) | Owns the program's quality and completion figures; assigns teaching and support staff | Raise the share of students who complete their online and blended courses | Where to put support staff each semester; which courses to review |
| Course Lecturer (CL) | Runs a course; the first to see who stops attending or submitting work | Keep students taking part until the end of the course, and passing it | Whom to contact or remind, and when |
| Academic Advisor / Student Support Officer (AD) | Contacts and supports students, with little time for each | Reach students who need help early enough for the help to work | Which students to contact first, and with what kind of support |
| Student (ST) | Takes the course; the subject of any data use and any contact | Finish the course while balancing work, family and other courses | Whether to accept help, reduce the study load or pause in time |
| Learning Technology and Data Officer (DO) | Holds and links LMS and academic-record data; applies privacy rules | Make data usable for staff without breaching privacy | Which data may be shared, with whom, how often and under which safeguards |

The interviews confirmed these hypotheses and made two of them more precise. The program manager's main decision is
not which courses to redesign but where to place the time of the support office and the lecturer-advisors within the semester, because support is spread
evenly today for lack of information about where it is needed (PM6). The data officer's first decision is not which
data to share but the purpose for which data may be used at all, a decision that university leadership and legal
staff must take before the data office can act (DO7).

===== reports/milestone-1/report/02-02-interview-approach.md @ 19d35a4 =====
## 2.2. Interview Approach

The interviews followed the procedure of the brief: questions prepared in advance, asked one at a time in a separate
conversation for each stakeholder, with follow-up questions where an answer was general or contradictory, and with
the key statements labelled afterwards [1]. Generative AI took both sides of each conversation. An isolated AI persona,
a conversation that knew only its role and the scenario, answered as the stakeholder; an AI interviewer acting for the
Data Analytics Team asked our questions and follow-ups. We verified every transcript.

Each persona trait was taken from a published account of people in that role: studies and reports of students [12],
[13], [14], of tutors [15] and of academic advisors [16], [17], and the Vietnamese rules on withdrawal [3] and on
personal data [18]. Figures that the personas gave, such as three officers for about 4,000 students, are their own
estimates, not published figures. We wrote seven or eight open questions for each stakeholder, covering the brief's five
information groups, with no question naming a cause, a data source or a tool (Appendix I). We then drew 51 key
statements from the interviews and labelled each one as an opinion (the stakeholder's own view), an assumption (a
figure or fact given as an estimate) or scenario information (a fact given in the brief) (Appendix II). Appendix VI
describes the method step by step.

===== reports/milestone-1/report/02-03-requirement-synthesis.md @ 19d35a4 =====
## 2.3. Synthesised Themes and Priorities

The brief asks us not to turn the AI's answers directly into a Business Goal, but to synthesise them in five
steps: organise, identify themes, prioritise, refine and validate [1]. We first organised each stakeholder's
answers under the brief's five headings: goal or need, challenge, decision needed, success indicator, and risk or
constraint (Appendix VI, Table A.14). Reading across the stakeholders then gave six recurring themes. Table 2.2 states
each theme, what the stakeholders said about it, who raised it and the priority we gave it.

**Table 2.2. Themes across the stakeholders and their priority**

| Theme | What the stakeholders said | Raised by | Priority |
| :---- | :---- | :---- | :---- |
| T1. Late detection | Non-completion becomes visible to the program only after the semester, to the support office only on the warning list, and to the lecturer only around week 5 or 6 (PM1, PM5, AD1, CL5, ST4, DO5) | All five | Core |
| T2. Early start of disengagement | Students begin to drift in the first weeks, and the first sign is usually a missed quiz or assignment (PM3, CL1, CL2, ST3, ST10) | Program manager, lecturer, student | Core |
| T3. Small, fixed capacity | Staff can follow up only a few dozen students a week, so they need a short list with a reason for each name (PM8, CL10, CL11, AD3, AD4, AD10) | Program manager, lecturer, support officer | Core |
| T4. Who contacts, and how | Contact helps when it comes from someone the student knows and offers something practical; generic emails are ignored (AD5, AD8, ST5, ST6, ST9) | Support officer, student | Supporting: defines the actions of AQ4 |
| T5. Trust in the data | Records must be linked, student status must be correct, meanings must be agreed, and the purpose must be lawful (DO1–DO9, PM9, CL3) | Data officer, program manager, lecturer | Constraint: data rules (Section 6) |
| T6. Use for support only | Results must never label students, affect grades or records, or evaluate lecturers (PM10, CL9, ST8, AD9, DO10) | All five | Constraint: use rules (Sections 6 and 7) |

The priorities follow the brief's three criteria: the link to the organisation's goal, the effect on decisions and
feasibility [1]. Themes T1–T3 form the core of the project: completion is the outcome the program reports, the early
signs set when staff can still act, and capacity sets how long a list of students can be. Theme T4 supplies the
actions among which staff choose, and themes T5 and T6 limit how the project may work rather than what it measures. Appendix VI (Table A.15) scores each theme against the three criteria.

Theme T3 rests on two capacity figures that recur in the rest of the proposal, both of them the support officer's
own estimates. The three officers of the support office can follow up about 30–40 students a week between them (AD3,
VAD7). Each lecturer-advisor can contact three to five students a week from their own classes (VAD6). The lecturer's
own account fits the second figure: the lecturer can give one to one and a half hours a week to this work and would act
on a list of five names with a reason for each (CL10, CL11).

Refining the core themes gave the problem statement of Section 1.2 and removed the requests that lie outside the
project, which Section 1.2 lists with their reasons.

===== reports/milestone-1/report/02-04-conflicts-validation.md @ 19d35a4 =====
## 2.4. Conflicts, Constraints and Validation

**Conflicts.** The stakeholders agree on the problem but pull in different directions on three points: early contact
against the risk of false alarms (PM3, CL6 against CL8, ST7, AD9); who should make contact, where the program manager
would have the lecturer-advisor or homeroom teacher call first (PM4), the student prefers the course lecturer (ST6) and
the support officer finds that students answer their own lecturer-advisor (AD5); and figures for the program against
names for staff (PM6 against AD4, CL6). One constraint adds to them: the data officer judges the data not yet clean
enough for anything automated (DO9). We resolved them in four ways. Contact lists reach staff at two review points: week 3, before the
second or third assignment deadline, and week 5, when more of the semester's record is available; a review point that
falls in a registration or examination week moves to the week before, with its data cut-off (VAD2); each name carries a factual reason and is checked by a member of staff, and students are told
about the process at the start of the course. Contact comes from the lecturer or the student's lecturer-advisor, and
the support office takes the harder cases. The project produces both course patterns for the program and short lists
for staff. No step is automated, and the data audit of Milestone 2 checks data quality first. Appendix VI (Table A.16)
sets out each conflict and the constraint with the statements behind them.

**Validation.** In the validation round, the AI interviewer returned to each stakeholder with a written summary of
our understanding and the draft goal, and asked what we had right, what we should correct and what was
missing (Appendix III). The stakeholders confirmed the core of the proposal: a short list in order of urgency with a
factual reason for each name, contact by someone who knows the student, and use for support only, with a person taking
the final decision. They corrected the timing of the review points, which now come in weeks 3 and 5 and avoid registration and examination
weeks (VCL2, VAD2), the definition of completion, which must mean passing (VPM6), and the horizon of the target, which
the program manager would accept over a full academic year rather than one semester (VPM5, VPM7). They added six
requirements, among them a program-level view of courses and groups (VPM3), a shared record of each contact (VCL4) and
a small pilot with comparison courses (VDO4, VPM9). Appendix VI (Table A.17) gives the full results under the
brief's four headings.

We did not adopt three suggestions, and each decision has a reason. First, the support officer suggested measuring the
project without a completion target, because students who answer the support office may have finished anyway (VAD4).
We keep the target, because the brief asks for an organisational outcome as the goal, and report any rise in
completion as progress rather than as the effect of contact. Second, the lecturer suggested defining completion as
having done all the work (CL2). We keep passing, the outcome the program reports, and describe the trail of
submitted work in the descriptive question AQ1 instead. Third, the student persona reported that some classmates
would rather receive a general email than a personal message (VST5). We keep personal contact as the default,
because the support officer reports that generic emails are mostly ignored (AD8), and add a general notice of the support
available, sent to every student at the start of the course.

===== reports/milestone-1/report/03-00-goals-kpis.md @ 19d35a4 =====
# 3. Business Goal, SMART Goal and KPIs

This part states the outcome the university wants (Section 3.1), turns it into a goal that is
SMART (specific, measurable, achievable, relevant and time-bound) (Section 3.2), and sets the
key performance indicator (KPI) measures that show progress towards it (Section 3.3).

===== reports/milestone-1/report/03-01-business-goal.md @ 19d35a4 =====
## 3.1. Business Goal

The project's Business Goal is to **improve successful course completion in the program's online and blended courses
by identifying students who stop taking part early enough to support them within the semester**.

The goal names an outcome for the organisation, more students passing their courses, rather than an activity such as
analysing LMS data or a technical solution such as a prediction model. The brief marks this difference as the test of
a suitable Business Goal, and its own example of a suitable goal also names early identification of students for
timely support [1]. The second half of the goal states when the outcome must be pursued, within the semester, because
every stakeholder placed the useful moment for support in the first weeks (Section 2.3).

The goal comes from three stakeholders. The program manager wants to know early how many students really complete,
and wants students supported to meet the standard rather than a better-looking rate (PM1, PM2). The support office
wants to reach students before they reach the academic warning list (AD1). The lecturer wants students who start the
course to finish it (CL2). The goal matters to students, for whom a failed course costs a semester's time and fees,
and to the university, whose withdrawal rate is tied to its enrolment quota [3].

If the goal is pursued, it supports two decisions in every semester, which Section 7 classifies: whom lecturers and
the support office contact first at each review point, and where the program manager places the time of the support office and the lecturer-advisors across
courses and groups. A third decision, whether to extend the approach beyond a pilot, depends on the results.

===== reports/milestone-1/report/03-02-smart-goal.md @ 19d35a4 =====
## 3.2. SMART Goal

The SMART Goal fixes what is measured, for whom and by when. Its figures need one assumption, stated first. The
scenario gives no real completion rate for the university, and the brief asks that any baseline not taken from real
data be marked as an assumption rather than presented as a fact [1]. The proposal therefore assumes a baseline
completion rate of 70%. Before any target is committed, this assumed figure is replaced by the real rate, recounted
from the university's records for the same courses, as the program manager asked (VPM8).

> **SMART Goal.** Raise the course completion rate of students enrolled after the add-drop period in the pilot
> courses from their recounted baseline (assumed 70%) by five percentage points (assumed target 75%) by the end of
> the 2027–2028 academic year.

The pilot courses are about four of the program's online and blended courses, with about 600 enrolments in total
(both assumptions), chosen before the pilot begins in Semester 2 of 2026–2027. The data office can support only a few courses with a consistent setup at first (VDO4), and
fixing the courses in advance prevents the target from being met by changing which courses are counted. Their
completion rate is compared with that of similar courses outside the pilot, so that a good result cannot come simply
from choosing easy courses (VPM9).

The baseline is the completion rate of the same courses in 2024–2025 and 2025–2026, recounted under Circular
83/2026 so that approved leave and transfers do not count as non-completion (VPM8). The contact process runs in the
pilot courses from Semester 2 of 2026–2027 through the 2027–2028 academic year, and the target is the completion rate
pooled over the pilot courses in 2027–2028, because the program manager doubted that five points could be gained in one semester
(VPM5) and accepted the goal in this longer form (VPM7).

The target is demanding but achievable. At a baseline of 70%, 30 of every 100 enrolments end without a pass, so five
more passes per 100 enrolments means helping five of those 30 students to pass, about one in six. The pilot is small
enough for weekly capacity: at the assumed baseline, about 180 of 600 enrolments end without a pass, while the support
office (about 30–40 contacts a week) and the lecturer-advisors of the pilot classes (three to five each) can reach well
over 100 students across the two review points (VAD6, VAD7). Published gains from
early-warning programs are contested [19], so the target remains an assumption, to be reviewed after the pilot. The
goal is relevant because it measures the Business Goal directly and answers the needs of the program manager and the
support office for real completion and earlier contact (PM2, AD1). Appendix VII (Table A.18) checks the goal against
each of the five SMART criteria.

The SMART Goal measures progress, not the effect of contact. Students who are contacted may have passed anyway, as the
support officer warned (VAD4), so a rise in completion shows that the situation has improved but not why. Whether contact
itself raised completion needs a comparison design, which Section 7 discusses.

===== reports/milestone-1/report/03-03-kpis.md @ 19d35a4 =====
## 3.3. Key Performance Indicators

The brief allows one primary KPI and at most two secondary KPIs, each with a reason why it measures progress towards
the SMART Goal [1]. The primary KPI measures the SMART Goal itself. The two secondary KPIs measure whether the support
process behind the goal works, which matters because completion moves slowly and is known only at the end of a
semester.

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

Both secondary KPIs depend on a contact record, a shared log of who contacted which student, when, how and with what
result. The university has no such record today: the lecturer asked for one (VCL4), and the support officer
described today's alerts from lecturers as unrecorded (VAD1). Section 6 therefore adds it to the data requirements. Differences between student groups, such as first-year and later-year students, are
not a separate KPI; they are handled as a fairness limit in the prescriptive question AQ4 (Section 4.1).

===== reports/milestone-1/report/04-00-question-ladder.md @ 19d35a4 =====
# 4. Analytical Question Ladder

This part states four analytical questions (AQ), one at each of the four levels of analytics that the brief requires
[1] (Section 4.1), and checks them against the brief's five quality criteria (Section 4.2).

===== reports/milestone-1/report/04-01-four-level-questions.md @ 19d35a4 =====
## 4.1. Questions at Four Levels

The four questions form one path from understanding the situation to supporting action, in which each question hands
its result to the next. Appendix VIII shows how each question meets the requirements the brief sets for its level.

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

**How the questions connect.** AQ1 shows which courses and groups lose most students and in which weeks
non-completers begin to fall behind, which tells AQ2 where to look. AQ2 compares the signs named in its wording, each
taken from the interviews, and asks which differ most rather than which cause non-completion, because records of what
students did cannot show why they did it. AQ3 tests whether those signs identify students in time. Its unit is one
student's enrolment in one course, because a student may struggle in one course and not in another, and it may use
only data up to the data cut-offs at the end of weeks 2 and 4. Recall is the share of students who later fail or
withdraw who appear on the list, and precision is the share of listed students who later fail or withdraw; an estimate
that does no better than counting missed tasks adds complexity without value. AQ4 turns the AQ3 ordering into a list
for each review point. Its precision limit keeps staff from spending most of their time on students who are fine
(CL8), and its fairness limit keeps the list from missing first-year students (VPM4); both limits are assumptions, to
be reviewed once the data audit of Milestone 2 shows what is achievable. Each level prepares the next without proving
a cause, and the audit may show that only part of this path can be answered with the university's data.

===== reports/milestone-1/report/04-02-quality-check-refinement.md @ 19d35a4 =====
## 4.2. Quality Check and Refinement

The brief requires every AQ to meet five criteria: clear, specific, scoped, data-oriented and
answerable [1]. In this proposal, a question is clear when it asks one thing that a reader can restate; specific when
it names its metric or target and the groups it compares; scoped when it fixes its population, courses and period;
data-oriented when it names the data it needs; and answerable when those data can settle it. Table 4.1 records, for
each question, how it meets each criterion in its final form, and its last row records what changed during
refinement. The refinements came from the validation round (codes beginning with V) and from an AI reviewer's
critiques, R1 to R12, which Appendix IV lists with our decision on each.

**Table 4.1. Five-criteria check of AQ1 to AQ4**

| Criterion | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- |
| Clear | Yes: asks how enrolments ended and when the first task was missed | Yes: asks which early signs differ most | Yes: asks how well non-completion can be estimated early | Yes: asks whom to list, in what order, with which contact |
| Specific | Yes: pass, fail and withdrawal shares; week of the first missed task | Yes: four named signs; difference in later non-completion rates | Yes: one target; recall and precision against a simple rule | Yes: three contact options; capacity, precision and fairness limits with values |
| Scoped | Yes: enrolments after add-drop, online and blended courses, four semesters of 2024–2025 and 2025–2026 | Yes: signs from weeks 1–4; same population as AQ1 | Yes: pilot courses; cut-offs at the end of weeks 2 and 4; horizon to semester end | Yes: review points in weeks 3 and 5 |
| Data-oriented | Yes: results, status and task dates | Yes: task, LMS activity and attendance records | Yes: AQ2 data up to each cut-off; final outcome | Yes: AQ3 ordering, staff capacity, contact record |
| Answerable | Yes: counts from records the university holds | Yes: comparisons of rates need only counts | Yes: earlier semesters provide known outcomes to test on | Yes: once AQ3 and the contact record exist |
| Refinement made | Year of study and delivery mode added (VPM3, VPM4); timing compared for both groups (R9) | Causal wording removed; activity measured within each course (DO2); attendance for blended courses only (R10) | Week-3 list added (VCL2); recall, precision and the two cut-offs defined (R1, R7) | Capacity and routing between offices added (VAD5); precision and fairness limits given values (R6) |

Two questions show how refinement worked. Table 4.2 gives each one before and after, with the reason for the change.

**Table 4.2. Before → After examples**

| Question | Before | After | Reason for the change |
| :---- | :---- | :---- | :---- |
| AQ2 | "What causes students to stop taking part in online courses?" | The AQ2 of Section 4.1 | "Causes" claims an effect that records of observed behaviour cannot show, and the factors to compare were not named. The final question names four signs and asks only which ones differ most between students who later complete and students who do not |
| AQ3 | "Can we predict which students will drop out?" | The AQ3 of Section 4.1 | The question had no target, no unit, no horizon and no data cut-off, and "drop out" mixed leaving the program with not completing one course. The final question fixes all four and adds a simple rule as the standard to beat |

===== reports/milestone-1/report/05-00-analytic-approach.md @ 19d35a4 =====
# 5. Proposed Analytic Approach

The four questions of Section 4 call for different kinds of analysis. At this milestone the proposal names the family
of techniques likely to fit each question, not a final algorithm; the specific methods are chosen in later milestones,
once the data have been audited [1]. Table 5.1 matches each question to its analytics type, its candidate technique
family, the expected output and the person who uses it.

**Table 5.1. Analytics type, candidate technique family and expected output per question**

| AQ | Analytics type | Candidate technique family | Expected output | Main user |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Rates, distributions, segmentation by course and group, trends over semesters; repeated after the pilot for pilot and comparison courses | A profile of completion by course and student group; a timeline of when non-completers first miss a task | Program manager |
| AQ2 | Diagnostic | Group comparison, association measures and statistical tests, explanatory regression, comparison of cohorts | Early signs ranked by their association with non-completion, with a check of whether the ranking holds across courses and groups | Program manager, lecturers |
| AQ3 | Predictive | Classification with time-based validation, compared against a simple rule; survival analysis of the time to withdrawal | An estimated likelihood of not completing for each enrolment at weeks 3 and 5, with recall and precision by group | Data Analytics Team |
| AQ4 | Prescriptive | Decision rules, prioritisation under capacity, routing between offices, what-if analysis of list length and limits | An ordered list for each review point, with a factual reason and a suggested contact for each name | Lecturer-advisors, support office |

Three choices shape the approach. AQ2 reports differences, not causes, because the records are observational and the
brief warns against causal language without a causal design [1]. AQ3 is
judged against a simple rule that counts missed tasks, because continuous-assessment results were the strongest early
predictor in the blended course described in Section 1.1 [8]; a classification method earns its place only if it
reaches more later non-completers than the rule on a list of the same length, tested on a later semester than the one
it learned from. Courses with no earlier semesters can use methods that learn from the current course's own submitted
assessments [20]. AQ4 shows each reason as an observed fact, such as two quizzes missed since week 2, because staff said
that a score without a reason would be ignored (VCL3, PM9). Appendix IX explains the choice of each technique family
in more detail.

===== reports/milestone-1/report/06-00-data-feasibility.md @ 19d35a4 =====
# 6. Preliminary Data Requirements and Feasibility

This part lists the data each question needs (Section 6.1) and assesses feasibility, quality risks, privacy and
ethics (Section 6.2).

===== reports/milestone-1/report/06-01-data-requirements.md @ 19d35a4 =====
## 6.1. Data Requirements per Question

At this milestone the data needs are stated as concepts, and no data are processed [1]. The needs draw on four sources that the university already holds:
the academic management system, the LMS, attendance lists of blended courses and staff rosters. The LMS and the academic records share a student
identifier, but nothing links them automatically, so records are matched by hand (DO1); attendance lists are kept by
lecturers and must also be matched by hand. Appendix IX describes what each source holds.

One source does not exist yet: the contact record defined in Section 3.3, which AQ4 and both secondary KPIs need.

Table 6.1 lists, for each question, the data it needs, their possible source, their granularity and time window,
their availability and a note on privacy. Availability reflects the data officer's account and remains an assumption
until the data audit of Milestone 2.

**Table 6.1. Preliminary data requirements**

| AQ | Data and variables needed | Possible source | Granularity and time | Availability | Privacy and ethics note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment, final result, student status, course, delivery mode, year of study; due and submission dates of assessed tasks | Academic management system; LMS | One row per enrolment per semester; 2024–2025 and 2025–2026 | Held; status may mix leave and transfers with withdrawal (DO3) | The program sees groups, not names |
| AQ2 | AQ1 data, plus missed and late tasks, LMS activity relative to the course average, tasks missed across courses, and attendance in blended courses, for weeks 1–4 | LMS; attendance lists | One row per enrolment per week | Held in separate systems and matched by hand (DO1) | No sensitive personal categories, such as health or ethnicity, are used |
| AQ3 | AQ2 data recorded by the end of week 2 and by the end of week 4; outcome at the end of the semester | Same as AQ2 | One row per enrolment at each data cut-off | Available with about one week of delay (DO4) | Seen only by the staff who act on it; no automated decision |
| AQ4 | AQ3 output; weekly capacity of each office; contact record (who, when, how, result) | AQ3; staff rosters; a new shared contact record | One row per student per review point | The contact record does not exist yet (VCL4, VAD1) | Used for support only; family and employers are never told (VST2) |

Where the university's own records cannot be used in time, Milestone 2 may test the approach on an open dataset. The
Open University Learning Analytics Dataset is one possible source: it covers 22 course presentations and 32,593
student records of a distance-learning university in the United Kingdom, with their assessment results and daily summaries of
their activity in the virtual learning environment [21]. Its assessment dates, activity records, final results and
withdrawal dates could support AQ1–AQ3, whereas the routing of AQ4 and both secondary KPIs need the university's own
contact record. Its fit, and the limits of transferring results from it to a Vietnamese university, are assessed in
Milestone 2.

===== reports/milestone-1/report/06-02-feasibility-privacy.md @ 19d35a4 =====
## 6.2. Feasibility, Quality Risks and Privacy

**Feasibility.** The data needs of Table 6.1 are feasible for a small pilot. The data office can support a few courses
with a consistent setup once legal approval for linking the records has been given, while routine linking across the
whole program and any automated step must wait (VDO2, VDO4, VDO5). Exports done by hand take about a week, so a list
built from the data of week 4 can reach staff in week 5 (VDO3).

**Quality risks.** Five risks could make the data mislead the analysis, and the project handles each one. Student
status may mix approved leave and transfers with real withdrawal (DO3, VPM2), so the baseline years are recounted under
the definitions of Circular 83/2026 [4], as the program manager asked (VPM8). The same LMS measure means different things in courses built
differently (DO2), so activity is compared within each course and quiz and assignment records are the main source
(VDO1). Activity is not learning, because a student can keep logging in while falling behind (CL3, VST1) [22], so
missed and late tasks are the main signs and a member of staff checks each name. Records are matched by hand with
about one week of delay (DO1, DO4), which the data cut-offs absorb. Small groups give unstable rates and can identify
individual students, so group results are reported only above an agreed minimum size. Appendix IX (Table A.20) sets
out these risks with their source and handling.

**Privacy and ethics.** Privacy and ethics set firm limits on the project. Vietnam's Personal Data Protection Law, in
force since 1 January 2026, ties consent to a stated purpose and does not treat silence as consent [18]. The Ministry
of Education and Training requires universities to secure their education databases and to report data breaches
within 72 hours [23]. Codes of practice for learning analytics add rules that the project adopts. The purpose, the
data, who has access and how results are used are explained to staff and students [11]. Students are told at the start
of the course and consulted on how their data are used [22]. Consent is sought before any personal intervention [11].
Access is limited to staff with a legitimate need [11]. The data have an agreed lifespan [22]. Results are never used for grading, for profiling students or for judging lecturers [11].

Two further rules come from the interviews and from published work. Once a university knows that a student is
struggling, it has an obligation to act [22], and the data officer warned that flagging students whom nobody has time
to follow up is worse than not knowing (DO10); a list therefore never exceeds the capacity to follow it up. The
student's family and employer are never told about a contact, as the student asked (VST2). Finally, no real student
data are entered into public AI tools, as the brief requires [1].

===== reports/milestone-1/report/07-00-decision-value.md @ 19d35a4 =====
# 7. Decision Supported and Expected Value

The analysis of Sections 4–6 serves three decisions, made by different people at different levels of the university.
This section classifies each decision, explains how its level sets the evidence the project must provide, and states
the value the project is expected to bring to each group of people involved.

**Three ways of classifying a decision.** The brief asks for three classifications [1]. The level of a decision is
strategic planning, management control (the brief's tactical level) or operational control, following Anthony's
levels as presented by Gorry and Scott Morton [24]. A decision is programmed, in Simon's sense, when it is routine and
has a worked-out procedure [24]. It is a one-way door when it is nearly irreversible and needs careful deliberation,
and a two-way door when it can be reversed and taken quickly [25]. Appendix IX gives the full definitions.

Table 7.1 applies the three classifications to the three decisions and states the evidence each decision needs.

**Table 7.1. Decisions supported and their classification**

| Decision | Who decides, using what | Level | Programmed? | Door | Evidence needed |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1. Whom to contact at each review point, by whom and with which offer | Lecturer-advisors and the support office, using the AQ4 list | Operational control (operational) | Programmed: repeated at every review point, with a fixed procedure | Two-way: a contact that does not help can be followed by another | A list that reaches more later non-completers than the simple rule (AQ3); a member of staff checks each name |
| D2. Where to place the time of the support office and the lecturer-advisors each semester | The program manager, using AQ1, AQ2 and the KPIs | Management control (tactical) | Semi-programmed: repeated each semester, but with judgement about courses and staff | Two-way: staff can be moved again next semester | A pattern repeated over several semesters, correct records and agreement with staff (PM7) |
| D3. Whether to extend the approach to all courses and link data routinely | University leadership, legal staff and the data office | Strategic planning (strategic) | Non-programmed: taken once, with no earlier case to follow | Close to one-way: it changes the university's data practice and students' trust | Pilot results, legal approval, and AQ1 and the KPIs for pilot and comparison courses (VAD4, VPM9) |

**How the level of a decision sets the evidence needed.** D1 is frequent and reversible, so it can start with the simple
missed-task rule checked by staff, and the AQ3 ordering replaces the rule only if it reaches more later non-completers
on a list of the same length; if a contact does not help, the next review point corrects it. D2 moves
scarce staff time between courses, and the program manager will move staff only for a pattern that repeats rather
than one bad semester or one difficult lecturer (PM7), so it needs results from several semesters. D3 commits the
university's data practice and the trust of its students, and it would be hard to reverse once records are linked
routinely and staff rely on the lists. It therefore needs the strongest evidence: AQ1 and the KPIs measured for pilot
and comparison courses before and after the pilot, legal approval, and an honest account of what the pilot did not
show. Whether contact itself caused any change in completion needs a design that compares contacted and similar
uncontacted students, which the evaluation plan of Milestone 4 sets out.

**Expected value.** Each group of people involved stands to gain something specific. Students who fall behind are
contacted while catching up is still possible, by someone they know and with a practical offer such as an extension
or a short pause (ST5, ST6). Lecturers and the support office spend their limited time on the students who most need
it, with a reason for each name and a record of what happened (VCL3, VCL4). The program manager sees which courses and
groups lose students during the semester, and can place support time where it is needed instead of spreading it
evenly (PM6, VPM3). The university gains the student-level status records that Circular 83/2026 calls for [4]. Even a
negative pilot result has value: it shows, at small scale and before any one-way commitment, which part of the path
from description to action does not work.

===== reports/milestone-1/report/08-00-genai-reflection.md @ 19d35a4 =====
# 8. Generative AI Usage and Team Reflection

Generative AI was used in the three roles that the brief allows, simulated stakeholder, sparring partner and reviewer,
and in a fourth role as a research assistant. It was never used as a source of facts about the university or its
students [1]. Table 8.1 sets out what AI did in each role and the control that kept its output in check.

**Table 8.1. Roles of generative AI and their controls**

| Role | How AI was used | Control |
| :---- | :---- | :---- |
| Simulated stakeholder | Five isolated AI personas answered the prepared questions, asked one at a time by an AI interviewer acting for us (Section 2.2) | Every persona trait cites a published account; key statements were labelled as opinion, assumption or scenario information, and we checked each quote against its transcript |
| Sparring partner | In the validation round, the personas challenged our understanding, for example the program manager's doubt that five points could be gained in one semester (VPM5) | Each challenge received a recorded decision, including the three suggestions not adopted (Section 2.4) |
| Reviewer | An isolated AI reviewer read the brief and Sections 1–7 with the prompt in Appendix IV and returned twelve critiques | Each critique received a decision and a reason (Appendix IV) |
| Research assistant | AI agents searched for and summarised published sources on non-completion, early warning, advising and data protection | Every fact in the report is tied to a saved source and a quoted passage; no AI summary is cited as a source |

**What we accepted and rejected.** Of the reviewer's twelve critiques, we accepted nine, partly accepted
two and rejected one. Three decisions show the reasoning. We accepted the critique that the data cut-off of AQ3
contradicted the one-week data delay of Section 6.2, because the cut-off decides what is known at the time of prediction; the
cut-offs are the end of weeks 2 and 4, for lists delivered in weeks 3 and 5 (R1). We accepted the critique
that the SMART Goal's population and pooling rule were unclear, because a target that depends on which courses are
counted could be met simply by changing the courses; the pilot courses are now fixed in advance and compared with
similar courses (R4). We rejected the critique that the Business Goal should not mention early identification,
because the brief's own example of a suitable goal names it, and the stakeholders asked for that timing (R11; PM1,
AD1). Appendix IV gives all twelve critiques, our decisions and the reviewer's prompt.

**What still needs real evidence.** Several points rest on assumptions or simulated views, and real data must replace
them. The baseline completion rate, the capacity figures, the one-week data delay and the precision and fairness
limits of AQ4 are assumptions or stakeholder estimates, which the university's records must replace in Milestone 2.
The early start of disengagement is supported by studies elsewhere [7], [8], not yet by the university's own data,
and AQ1 will measure it. Students' acceptance of contact based on their study activity rests on one simulated student
and on studies abroad [12], so it needs confirmation from real students in Vietnam before the pilot.

**Team reflection.** Using AI on both sides of the interviews made it possible to hear five perspectives with
consistent questions, and the personas raised points we had not planned for, such as the contact record and the
risk of review points falling in examination weeks. The same method sets its main limit. Because the personas speak
from published accounts, the interviews show plausible needs rather than verified ones, and the stakeholders' figures
are informed estimates rather than measurements. We therefore treat every requirement in this proposal as a
hypothesis about the real university, to be tested with its data in the milestones that follow.

===== reports/milestone-1/report/09-00-traceability-matrix.md @ 19d35a4 =====
# 9. Traceability Matrix

Table 9.1 traces the whole proposal in one place, as the brief requires [1]: from the Business Goal (Section 3.1),
through the SMART Goal and the KPIs (Sections 3.2 and 3.3), the four AQs and their analytics types and
technique families (Sections 4 and 5), and the data each question needs (Section 6), to the decisions supported
(Section 7). The decisions are D1, whom to contact at each review point; D2, where to place support time each
semester; and D3, whether to extend the approach to all courses.

**Table 9.1. Traceability from Business Goal to decision supported**

| Business Goal | SMART Goal / KPI | AQ | Analytics type | Candidate technique family | Data needed | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Improve successful course completion in the program's online and blended courses by identifying students who stop taking part early enough to support them within the semester | SMART Goal: completion in the pilot courses from the recounted baseline (assumed 70%) up five points by the end of 2027–2028; primary KPI: course completion rate | AQ1: how enrolments ended, and when non-completers first missed a task | Descriptive | Rates, distributions, segmentation, trends | Enrolment, final result, status, year of study, task dates | D2: where to place support time; D3: whether to extend |
| (same) | Primary KPI; secondary KPI 1: early-sign contact rate | AQ2: which early signs differ most between completers and non-completers | Diagnostic | Group comparison, association measures, explanatory regression | AQ1 data plus missed and late tasks, LMS activity and attendance in weeks 1–4 | D2; the reasons shown with each name in D1 |
| (same) | Secondary KPI 1: early-sign contact rate | AQ3: how well non-completion can be estimated from data up to the end of weeks 2 and 4 | Predictive | Classification with time-based validation; survival analysis | AQ2 data up to each data cut-off; outcome at semester end | D1: whom to contact |
| (same) | Secondary KPI 2: follow-up rate; primary KPI | AQ4: whom to list, in what order and with which contact | Prescriptive | Decision rules, prioritisation under capacity, what-if analysis | AQ3 output, weekly capacity, contact record | D1: whom to contact, by whom, with which offer |

===== reports/milestone-1/report/10-references.md @ 19d35a4 =====
# References

The references are formatted in APA style (American Psychological Association, 7th edition) and numbered for in-text citation in the form [n], in order of first citation.

[1] MTH045 – The Science of Data Analytics. (2026). *Milestone P1: Requirement analysis & analytics project proposal* [Course brief]. University of Science, VNU-HCM.

[2] Yên Chi. (2021, April 8). Sinh viên được học trực tuyến 30% tổng khối lượng chương trình đào tạo [Students may study online for 30% of the programme]. *Luật sư Việt Nam*. https://lsvn.vn/sinh-vien-duoc-hoc-truc-tuyen-30-tong-khoi-luong-chuong-trinh-dao-tao1617849652-a102715.html

[3] Đại biểu Nhân dân. (2024, November 13). Toa thuốc trị tuyển sinh kiểu "vơ bèo vạt tép" [A remedy for indiscriminate enrolment]. *Đại biểu Nhân dân*. https://daibieunhandan.vn/toa-thuoc-tri-tuyen-sinh-kieu-vo-beo-vat-tep-10351821.html

[4] Giáo dục Việt Nam. (2026, October 15). Quy định mới về tỷ lệ thôi học trong Thông tư 83 giúp thống kê thực chất hơn [New rule on the withdrawal rate in Circular 83 makes statistics more accurate]. *Tạp chí điện tử Giáo dục Việt Nam*. https://giaoduc.net.vn/ban-in/post263350.gd

[5] Muljana, P. S., & Luo, T. (2019). Factors contributing to student retention in online learning and recommended strategies for improvement: A systematic literature review. *Journal of Information Technology Education: Research*, *18*, 19–57. https://doi.org/10.28945/4182

[6] Lê, T. M. L., Trần, T. A. T., & Trần, A. T. (2024). Tổng quan thực trạng và các yếu tố ảnh hưởng đến bỏ học ở sinh viên đại học [A review of the situation of and factors influencing university student dropout]. *Tạp chí Phát triển Khoa học và Công nghệ – Khoa học Xã hội và Nhân văn*, *8*(3), 2683–2706. https://doi.org/10.32508/stdjssh.v8i3.1033

[7] Jordan, K. (2015). Massive open online course completion rates revisited: Assessment, length and attrition. *International Review of Research in Open and Distributed Learning*, *16*(3), 341–358. https://doi.org/10.19173/irrodl.v16i3.2112

[8] Howard, E., Meehan, M., & Parnell, A. (2018). Contrasting prediction methods for early warning systems at undergraduate level. *The Internet and Higher Education*, *37*, 66–75. https://doi.org/10.1016/j.iheduc.2018.02.001

[9] Rahmani, A. M., Groot, W., & Rahmani, H. (2024). Dropout in online higher education: A systematic literature review. *International Journal of Educational Technology in Higher Education*, *21*, Article 19. https://doi.org/10.1186/s41239-024-00450-9

[10] Simpson, O. (2013). Student retention in distance education: Are we failing our students? *Open Learning: The Journal of Open, Distance and e-Learning*, *28*(2), 105–119. https://doi.org/10.1080/02680513.2013.847363

[11] Sclater, N., & Bailey, P. (2015). *Code of practice for learning analytics* (updated September 9, 2026). Jisc. Retrieved November 2, 2026, from https://www.jisc.ac.uk/guides/code-of-practice-for-learning-analytics

[12] Roberts, L. D., Howell, J. A., Seaman, K., & Gibson, D. C. (2016). Student attitudes toward learning analytics in higher education: “The Fitbit version of the learning world”. *Frontiers in Psychology*, *7*, 1959. https://doi.org/10.3389/fpsyg.2016.01959

[13] Greenland, S. (2022, January 24). How unis can save millions by tackling the biggest causes of online students’ high dropout rates. *The Conversation*. https://theconversation.com/how-unis-can-save-millions-by-tackling-the-biggest-causes-of-online-students-high-dropout-rates-173139

[14] Sinh viên Việt Nam Online. (2026). Sự im lặng phía sau lớp học ‘qua loa’ [The silence behind the ‘loudspeaker’ class]. *Tiền Phong*. https://tienphong.vn/su-im-lang-phia-sau-lop-hoc-qua-loa-post1865907.tpo

[15] Herodotou, C., Rienties, B., Boroowa, A., Zdrahal, Z., & Hlosta, M. (2019). A large-scale implementation of predictive learning analytics in higher education: The teachers’ role and perspective. *Educational Technology Research and Development*, *67*(5), 1273–1306. https://doi.org/10.1007/s11423-019-09685-0

[16] Robbins, R. (2013). *Advisor load*. NACADA Clearinghouse of Academic Advising Resources. https://nacada.ksu.edu/Resources/Clearinghouse/View-Articles/Advisor-Load.aspx

[17] Dial, M., & McKeown, P. (2020). Academic early alert and intervention: Why academic advisors are best suited to intervene with at-risk students. *Academic Advising Today, 43*(4). https://nacada.ksu.edu/Resources/Academic-Advising-Today/View-Articles/Academic-Early-Alert-and-Intervention-Why-Academic-Advisors-Are-Best-Suited-to-Intervene-with-At-Risk-Students.aspx

[18] Tài liệu quán triệt nội dung cơ bản của Luật Bảo vệ dữ liệu cá nhân [Briefing document on Law No. 91/2025/QH15]. (n.d.). Trường Đại học Tiền Giang. https://www.tgu.edu.vn/upload/files/Tailieu-gioithieu-LuatBaovedulieucanhan.pdf

[19] Caulfield, M. (2013, September 26). Why the Course Signals math does not add up. *Hapgood*. https://hapgood.us/2013/09/26/why-the-course-signals-math-does-not-add-up/

[20] Hlosta, M., Zdrahal, Z., & Zendulka, J. (2017). Ouroboros: Early identification of at-risk students without models based on legacy data. In *Proceedings of the Seventh International Learning Analytics & Knowledge Conference* (pp. 6–15). ACM. https://doi.org/10.1145/3027385.3027449

[21] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, *4*, Article 170171. https://doi.org/10.1038/sdata.2017.171

[22] Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and dilemmas. *American Behavioral Scientist*, *57*(10), 1510–1529. https://doi.org/10.1177/0002764213479366

[23] Lê, P. (2024, August 23). Bộ Giáo dục và Đào tạo tăng cường công tác bảo vệ dữ liệu cá nhân và an toàn thông tin mạng. *Báo Thanh tra*. https://thanhtra.com.vn/giao-duc-A6BAEB6CD/bo-giao-duc-va-dao-tao-tang-cuong-cong-tac-bao-ve-du-lieu-ca-nhan-va-an-toan-thong-tin-mang-6547C321.html

[24] Gorry, G. A., & Scott Morton, M. S. (1971). *A framework for management information systems* (Working Paper No. 510-71). Sloan School of Management, Massachusetts Institute of Technology. https://dspace.mit.edu/handle/1721.1/47936

[25] Bezos, J. P. (2016, April 5). *2015 letter to shareholders* [Exhibit 99.1 to Form 8-K]. Amazon.com, Inc. https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm

===== reports/milestone-1/report/11-00-appendices.md @ 19d35a4 =====
# Appendices

Appendices I–IV hold the evidence of how generative AI was used in requirement gathering: the interview questions
(Appendix I), word-for-word excerpts from the five interviews (Appendix II), the validation round (Appendix III), and
the AI reviewer's critiques with our decisions and the reviewer prompt (Appendix IV). Appendices V–IX hold the
detail behind the main text, in the order of its parts: the published evidence on non-completion (Appendix V), the
interview method and the requirement synthesis (Appendix VI), the SMART Goal and KPIs (Appendix VII), the
specification of the four AQs (Appendix VIII), and the technique families, data sources and decision
classifications (Appendix IX).

===== reports/milestone-1/report/11-01-interview-questions.md @ 19d35a4 =====
## Appendix I – Interview Questions

The questions below were written before the interviews and cover the five information groups of the brief (business goals, success vision, challenges, decision making and risk anticipation). They are listed by stakeholder: Table A.1 for the Program Manager, Table A.2 for the Course Lecturer, Table A.3 for the Academic Advisor, Table A.4 for the Student and Table A.5 for the Learning Technology and Data Officer. Each question was asked in order, and a question was dropped when an earlier answer had already covered it in full. Table A.6 shows two drafts that were rewritten because they led the stakeholder towards an answer.

**Table A.1. Program Manager: interview questions**

| Code | Group | Question |
| :---- | :---- | :---- |
| PM-Q1 | Business goals | Looking at the online and blended courses in your program, what would you most like to improve over the next year, and why does it matter to the program? |
| PM-Q2 | Success vision | If things went well, what would you see at the end of the next semester that tells you the situation has really improved? |
| PM-Q3 | Success vision | How do you currently judge whether a course or a cohort is doing well or badly? What figures or reports do you look at, and how often? |
| PM-Q4 | Challenges | What makes it hardest today to deal with students who do not complete their courses? |
| PM-Q5 | Decision making | Which decisions about courses, staff or student support are yours to make, and which would you make differently if you had better information? |
| PM-Q6 | Decision making | What resources could you realistically move or add to support students during a semester, and what limits them? |
| PM-Q7 | Risk anticipation | What would make you distrust or ignore the results of an analysis like this? |
| PM-Q8 | Risk anticipation | What could go wrong for students or staff if the university acts on such results? |

**Table A.2. Course Lecturer: interview questions**

| Code | Group | Question |
| :---- | :---- | :---- |
| CL-Q1 | Business goals | In your online or blended courses, what outcome for your students matters most to you over a semester? |
| CL-Q2 | Challenges | How do you usually find out that a student is struggling or has stopped taking part, and at what point in the semester? |
| CL-Q3 | Challenges | What happens next, once you notice? What do you do, and what gets in the way? |
| CL-Q4 | Success vision | What would a good semester look like for you, in terms of how many students finish and how they finish? |
| CL-Q5 | Decision making | If you had better information about how your students are doing during the semester, what would you do differently, and when? |
| CL-Q6 | Decision making | Which parts of the course are you free to change during a semester, and which are fixed? |
| CL-Q7 | Risk anticipation | What would make you stop trusting or using information about your students that came from an analysis? |
| CL-Q8 | Risk anticipation | How much extra time could you give to follow-up work in a typical week, and what would have to give way? |

**Table A.3. Academic Advisor / Student Support Officer: interview questions**

| Code | Group | Question |
| :---- | :---- | :---- |
| AD-Q1 | Business goals | What do you most want to achieve for the students you support during a semester? |
| AD-Q2 | Challenges | How do students who need help usually come to your attention today, and how early or late is that? |
| AD-Q3 | Challenges | What is the hardest part of reaching and helping a student who has stopped taking part in a course? |
| AD-Q4 | Success vision | How would you know that your support work had made a difference by the end of a semester? |
| AD-Q5 | Decision making | When you have more students to contact than time allows, how do you decide whom to contact first? |
| AD-Q6 | Decision making | What kinds of support can you actually offer, and which work best for which students? |
| AD-Q7 | Risk anticipation | What could go wrong when a student is contacted because of information about their study activity? |
| AD-Q8 | Risk anticipation | What would make you or your colleagues stop using a list of students to contact? |

**Table A.4. Student: interview questions**

| Code | Group | Question |
| :---- | :---- | :---- |
| ST-Q1 | Business goals | What matters most to you when you take an online or blended course? |
| ST-Q2 | Challenges | Can you tell me about a time you, or a classmate, started to fall behind or stopped attending a course? What was going on? |
| ST-Q3 | Challenges | Looking back, when did it start, and who noticed – you, a friend, a lecturer, anyone at the university? |
| ST-Q4 | Success vision | What would have helped you, or your classmate, finish that course? |
| ST-Q5 | Decision making | If the university noticed you were falling behind, how would you want them to contact you, and who should it be? |
| ST-Q6 | Risk anticipation | What would you think if you learned the university used your study activity in the online system to decide whom to contact? |
| ST-Q7 | Risk anticipation | What would make such contact feel helpful, and what would make it feel unwelcome? |

**Table A.5. Learning Technology and Data Officer: interview questions**

| Code | Group | Question |
| :---- | :---- | :---- |
| DO-Q1 | Business goals | From where you sit, what would you like the university to be able to do better with the information its systems already collect about teaching and learning? |
| DO-Q2 | Challenges | What information about students' courses and study activity exists today, who owns it, and how easy is it to bring together? |
| DO-Q3 | Challenges | What problems do you see in the quality or consistency of that information across courses and semesters? |
| DO-Q4 | Success vision | What would make you confident that information prepared for staff during a semester is correct and on time? |
| DO-Q5 | Decision making | What would need to be decided, and by whom, before staff could use student activity information in their work? |
| DO-Q6 | Risk anticipation | What rules or concerns about privacy, consent and access would apply, and how are they handled today? |
| DO-Q7 | Risk anticipation | What could go wrong technically or ethically if such information were used to act on individual students? |

**Table A.6. Leading drafts and their final form**

| Draft | Problem | Final question |
| :---- | :---- | :---- |
| CL: "Would an early-warning dashboard of LMS activity help you spot students who are falling behind?" | Proposes a solution and a data source; yes/no | CL-Q5: "If you had better information about how your students are doing during the semester, what would you do differently, and when?" |
| ST: "Did low online activity cause you to fall behind?" | Names a cause; yes/no | ST-Q2: "Can you tell me about a time you, or a classmate, started to fall behind or stopped attending a course? What was going on?" |

===== reports/milestone-1/report/11-02-interview-excerpts.md @ 19d35a4 =====
## Appendix II – Interview Excerpts

The key statements of each interview are quoted word for word from the transcripts: Table A.7 for the Program Manager, Table A.8 for the Course Lecturer, Table A.9 for the Academic Advisor, Table A.10 for the Student and Table A.11 for the Learning Technology and Data Officer. The code in the first column is the one used in the main text (for example PM1). The label marks each statement as the stakeholder's opinion, an assumption (an estimate or impression the stakeholder gives as a figure or fact) or information from the scenario; Q1 to Q8 refer to the questions of Appendix I, and "follow-up" marks a question added during the interview.

**Table A.7. Program Manager: key statements**

| Code | Question | Excerpt | Label | Meaning for the project |
| :---- | :---- | :---- | :---- | :---- |
| PM1 | Q1 | "what I most want to fix is that we find out too late" | Opinion | The program learns of non-completion only after the semester closes |
| PM2 | Q1 | "I don't want a lower rate on paper. I want students supported to meet the standard, not the standard lowered." | Opinion | The goal is real completion, not a better-looking indicator |
| PM3 | Q1 follow-up | "the first four or five weeks of a semester are when it still makes a difference" | Opinion | Window for action: weeks 1–5 |
| PM4 | Q1 follow-up | "first the advisor or homeroom teacher, because they can actually call the student" | Opinion | Advisors act on individual students; the PM acts at program level |
| PM5 | Q3 | "my rhythm is once per semester for courses and once per year for cohorts, and both are looking backwards" | Scenario and opinion | Only end-of-semester data exists today (scenario: data held but unused for this purpose) |
| PM6 | Q5 | "Today I spread support more or less evenly, because I can't see where it is needed." | Opinion | Decision: where to put advisors' time within the semester |
| PM7 | Q5 follow-up | "I'd want to see that the problem repeats, not one bad semester or one difficult lecturer" | Opinion | Evidence bar for moving staff: repeated pattern, correct records, agreement with staff |
| PM8 | Q6 | "not much new money appears mid-semester, so it is mostly about moving what I have" | Opinion | Constraint: fixed resources within a semester |
| PM9 | Q7 | "If the results come only as one score or a list of names without saying why, I can't defend them" | Opinion | Results need reasons |
| PM10 | Q8 | "If a student is called 'at risk' and a lecturer starts treating them that way, it can become a self-fulfilling thing" | Opinion | Labelling risk |

**Table A.8. Course Lecturer: key statements**

| Code | Question | Excerpt | Label | Meaning for the project |
| :---- | :---- | :---- | :---- | :---- |
| CL1 | Q1 | "we lose them somewhere between the second and third assignment, or the third and fourth" | Opinion | Disengagement shows between early assignments |
| CL2 | Q1 follow-up | "Did they submit the assignments, all of them, not just the big final one?" | Opinion | Success = complete trail of work, not only a pass |
| CL3 | Q1 follow-up | "So clicks alone wouldn't convince me." | Opinion | LMS time is a weak signal |
| CL4 | Q3 | "I contacted them, no reply, left a voice message, and that's where it stops." | Opinion | Manual outreach often fails |
| CL5 | Q3 | "by the time I'm sure someone's gone quiet, it's often already week five or six" | Assumption | Detection comes late |
| CL6 | Q5 | "I'd want to reach out in the first two or three weeks, not week six." | Opinion | Earlier contact, timed before assignment deadlines |
| CL7 | Q6 | "I can change how I support students fairly freely, but not what they're assessed on." | Opinion | Actions available mid-semester: support, not assessment |
| CL8 | Q7 | "The quickest way to lose me is to flag students I know are fine." | Opinion | False alarms destroy trust |
| CL9 | Q7 | "if I suspected it would be used to judge my teaching rather than to help students" | Opinion | Results must not evaluate lecturers |
| CL10 | Q8 | "Maybe an hour, an hour and a half a week on top of what I already do" | Assumption | Lecturer capacity: about 1–1.5 hours a week |
| CL11 | Q8 | "If I can open a list, see five names and the reason for each, and send a message in ten minutes, I'll do that every week." | Opinion | Short list with reasons fits the workload |

**Table A.9. Academic Advisor / Student Support Officer: key statements**

| Code | Question | Excerpt | Label | Meaning for the project |
| :---- | :---- | :---- | :---- | :---- |
| AD1 | Q1 | "reach the students who are slipping before they land on the academic warning list" | Opinion | Goal: earlier contact than the warning list |
| AD2 | Q1 | "our office is three people for about four thousand students" | Assumption | Capacity constraint (persona's figure) |
| AD3 | Q1 follow-up | "each of us three officers could manage perhaps ten to fifteen of those in a normal week" | Assumption | Weekly follow-up capacity: about 30–45 for the office in this first estimate, given as 30–40 in the validation round (VAD5), plus 3–5 per lecturer-advisor |
| AD4 | Q1 follow-up | "I'd rather get a shorter list we can actually act on, with some sense of who is most urgent." | Opinion | Prioritised short list |
| AD5 | Q3 | "They reply far more often when it comes from their own cố vấn học tập, someone they already know" | Opinion | The contact person matters |
| AD6 | Q4 | "The students who answer my calls and come to a meeting are often the ones who were going to pull through anyway" | Opinion | Self-selection: outcomes of contacted students are not proof of effect |
| AD7 | Q5 | "it isn't written down anywhere, and two officers in our office might well pick differently from the same list" | Opinion | Prioritisation today is undocumented and inconsistent |
| AD8 | Q6 | "What works least, I think, is a generic reminder email" | Opinion | Action alternatives differ in value |
| AD9 | Q7 | "the judgement about whether and how to contact someone should stay with a person" | Opinion | Human judgement before contact |
| AD10 | Q8 | "The quickest way to lose us is a list that's too long." | Opinion | List length must fit capacity |

**Table A.10. Student: key statements**

| Code | Question | Excerpt | Label | Meaning for the project |
| :---- | :---- | :---- | :---- | :---- |
| ST1 | Q1 | "what matters most to me is that the course fits around my life" | Opinion | Students' constraints come from outside the course |
| ST2 | Q1 follow-up | "I was too embarrassed" | Opinion | Students rarely ask for help early |
| ST3 | Q3 | "I think it started around week four or five" | Assumption | Disengagement started early |
| ST4 | Q3 | "no lecturer or anyone from the university noticed" | Opinion | Nobody noticed |
| ST5 | Q4 | "A clear, simple way to get an extension, or to pause a couple of weeks and pick up again" | Opinion | Practical flexibility helps more than encouragement |
| ST6 | Q5 | "the lecturer of that course, or a tutor who actually knows the course, not an office I've never heard of" | Opinion | Preferred contact person |
| ST7 | Q6 | "I'd want to be told at the start of the course that they look at it" | Opinion | Transparency about data use |
| ST8 | Q6 | "And it should never count against my grade or end up on some record." | Opinion | Support-only use |
| ST9 | Q7 | "Unwelcome is anything that sounds like a label, 'you are at risk' or 'you are failing'." | Opinion | Wording of contact |
| ST10 | Q7 follow-up | "I think the quiz that week was the first one I missed completely." | Assumption | Observable early sign: first fully missed quiz (week 5) |

**Table A.11. Learning Technology and Data Officer: key statements**

| Code | Question | Excerpt | Label | Meaning for the project |
| :---- | :---- | :---- | :---- | :---- |
| DO1 | Q1 | "the LMS logs, the academic affairs records and the quality assurance surveys share a student ID, but nothing links them automatically" | Assumption | Data exist, linkable by ID, not linked |
| DO2 | Q1 | "'activity' in one course isn't the same as in another, and in any case clicks are not learning" | Opinion | Course setups differ; activity is a weak proxy |
| DO3 | Q2 | "The status records have to separate approved leave and transfers from real dropout, and I'm not confident they always do." | Assumption | Outcome label quality risk |
| DO4 | Q2 follow-up | "LMS activity could reach staff with a lag of about a week if I do the exports by hand" | Assumption | Data freshness: about one week |
| DO5 | Q1 follow-up | "Advisors don't get anything from me on a regular basis" | Assumption | The people who act get no data today |
| DO6 | Q4 | "I'd want to be able to check a sample by hand" | Opinion | Trust needs traceable data |
| DO7 | Q5 | "the first decision is the purpose, and that has to come from leadership with legal" | Opinion | Governance decision precedes use |
| DO8 | Q6 | "consent has to be given for each purpose, silence isn't consent" | Opinion | Persona's reading of Law No. 91/2025/QH15, consistent with the law (Section 6.2) |
| DO9 | Q7 | "I don't think our data is clean enough to feed anything automated yet" | Opinion | Feasibility caution |
| DO10 | Q7 | "if we flag students but nobody has time to follow up, I think that's worse than not knowing" | Opinion | Duty to act once flagged |

===== reports/milestone-1/report/11-03-validation-round.md @ 19d35a4 =====
## Appendix III – Validation Round

After the synthesis, each stakeholder was shown the summary below in the same conversation as the interview, followed by one question for that role, and asked what was right, what should be corrected and what was missing. The program manager's answer led to a revised SMART Goal, which was presented again and confirmed.

> Thank you for the interview. We have spoken with five colleagues: the program manager, a course lecturer, the student
> support office, a student and the learning technology and data office. Here is how we understand what we heard. Please
> tell us (1) what we have right, (2) what we should correct, and (3) what is missing.
>
> 1. The main problem: students who stop taking part in online and blended courses are noticed only after the semester
>    ends, although it usually starts within the first four or five weeks, and shows first in missed quizzes and
>    assignments.
> 2. Staff can follow up only a small number of students each week. They need a short list, in order of urgency, with
>    the reason for each name, delivered before the second or third assignment deadline, around week 5.
> 3. Contact works best when it comes from someone who knows the student (the lecturer or the student's own academic
>    advisor), sounds supportive, never says "at risk", and offers something practical such as an extension or a
>    meeting.
> 4. Before any of this is used, the university must agree on the purpose and who may see what, tell students at the
>    start of the course, keep the student-status records correct, and keep the final judgement with a person. Results
>    are for support only: never for grades, records or judging lecturers.
> 5. Our proposed goal: improve successful course completion in the program's online and blended courses by identifying
>    students who stop taking part early enough to support them within the semester. We would measure it by the course
>    completion rate (an assumed baseline of 70%, target 75% by the end of next semester), plus two supporting measures:
>    the share of students who later fail or withdraw who were contacted by week 6, and the share of listed students
>    contacted within a week of being listed.

Table A.12 gives the key statements of the validation round, quoted word for word, with their effect on the proposal; Section 2.4 summarises the result, and Table A.17 in Appendix VI gives it in full.

**Table A.12. Validation statements and their effect on the proposal**

| Code | Excerpt | Effect on the proposal |
| :---- | :---- | :---- |
| VPM1 | "the four or five weeks was my own judgement, not something we have measured, so don't write it as a fact about our students" | Timing of disengagement is a stakeholder view backed by published studies, measured in AQ1 |
| VPM2 | "the student-status records have to follow the new definitions, not only be 'correct'" | Completion and withdrawal counted under Circular 83/2026 |
| VPM3 | "I need a program-level view, which courses and which groups keep producing these cases, not only names for advisors" | AQ1–AQ2 produce course and group patterns for the PM |
| VPM4 | "First-year students deserve explicit attention." | Student year is a segment in AQ1–AQ3 |
| VPM5 | "honestly, I doubt five points in one semester" | SMART horizon moved to the 2027–2028 academic year after a one-semester pilot |
| VPM6 | "Completion is acceptable as the main measure only if it means passing the course, not just staying enrolled" | Completion defined as passing the course |
| VPM7 | "Yes, this version I can take to the dean." | Revised SMART Goal confirmed |
| VPM8 | "please recount them under the new definitions rather than mixing the two" | Baseline years recounted under Circular 83 |
| VPM9 | "tell me how they differ from the others, so a good result isn't simply because we picked the easy courses" | Pilot courses compared with non-pilot courses |
| VCL1 | "The problem is that it's late and patchy, not that nobody sees it." | Problem restated: detection is late and patchy |
| VCL2 | "I'd rather have a first look around week 2 or 3, and then a refresh a few days before each assignment deadline, not one list once" | Two review points: week 3 and week 5 |
| VCL3 | "Not a score, the actual facts, so I know what to say when I write." | Reasons listed as observed facts (missed or late tasks, since when) |
| VCL4 | "a simple record of who was contacted, by whom, and what happened" | Contact record becomes a data requirement and the source of the follow-up KPI |
| VAD1 | "Lecturers do email me sometimes during the semester; it's just scattered, late and unrecorded." | Same as VCL1 |
| VAD2 | "week 5 can collide with registration or exams; a list that lands then gets ignored" | Review dates set outside registration and exam weeks |
| VAD3 | "a student drifting in several courses at once is a different case from one course" | Multi-course disengagement is a priority signal in AQ4 |
| VAD4 | "The students who answer us may have finished anyway, so I'd be careful claiming the five points as our doing." | KPIs report progress, not effect; effect needs a comparison design |
| VAD5 | "My office should take the harder cases: students missing across several courses, repeat warnings, and anyone whose advisor couldn't reach them after two tries." | Routing rule for AQ4 action alternatives |
| VAD6 | "the lecturer-advisors should take students from their own classes, because students answer people they know, but only a handful each, three to five a week" | Weekly capacity of each lecturer-advisor: three to five contacts (advisor's estimate) |
| VAD7 | "Three of us can manage maybe thirty to forty a week between us, at a guess." | Weekly capacity of the support office: about 30–40 contacts (advisor's estimate) |
| VST1 | "I kept logging in and clicking through, so on the system I probably looked fine for a while" | Activity counts can hide disengagement; reasons combine assessment facts with staff knowledge |
| VST2 | "please add that my family or employer never get told" | Privacy rule added |
| VST3 | "I should be able to reply simply, or say 'I'm fine, thanks', and not get chased every week" | One contact per review point; a reply closes the case |
| VST4 | "yes, I'd accept it if I'm told at the start and it's really for support" | Notice at course start confirmed |
| VST5 | "some classmates would rather get a general email" | A general notice of support options goes to every student at course start; personal contact stays the default (Section 2.4) |
| VDO1 | "Missed quizzes and assignments are a better early sign than clicks, and the LMS does record them." | Missed and late assessed tasks are the main signs (Sections 4.1 and 6.2) |
| VDO2 | "legal has to approve linking LMS data to status records first" | Governance gate before Milestone 2 data use at the university |
| VDO3 | "With exports done by hand, a week-5 list could already be a week old." | Data cut-off one week before each review point |
| VDO4 | "I think my office could support a small pilot" | Pilot scope: a few courses with a consistent setup |
| VDO5 | "Routine linking across the whole programme, and anything automated, would have to wait." | No automated action in scope |

===== reports/milestone-1/report/11-04-ai-critique-review.md @ 19d35a4 =====
## Appendix IV – AI Critique, Team Decisions and Reviewer Prompt

An isolated AI reviewer read the brief and Sections 1–7 with the prompt below and returned twelve critiques. Table A.13 gives each critique in short form, our decision and the reason or change; Section 8 discusses three of them.

**Table A.13. AI critique, team decision and reason**

| No. | AI critique | Team decision | Reason or change |
| :---- | :---- | :---- | :---- |
| R1 | AQ3 data cut-off contradicts the one-week data delay (Section 6.2) | Accepted | Cut-offs end of week 2 and week 4; lists delivered in weeks 3 and 5 (Sections 4.1, 4.2, 6.1 and 6.2) |
| R2 | Secondary KPI 1 uses an end-of-semester denominator that falls when contact works; week 6 matches no review point | Accepted | Replaced by the early-sign contact rate (Section 3.3) |
| R3 | D3 has no analytic path; no traceability matrix | Partly accepted | D3 rests on AQ1 and the KPIs repeated for pilot and comparison courses; causal effect left to the Milestone 4 evaluation plan (Sections 5 and 7). The matrix is Section 9, which the reviewer did not receive |
| R4 | SMART population and aggregation unclear | Accepted | Pilot courses fixed before the pilot, pooled rate, comparison courses (Section 3.2) |
| R5 | Achievable criterion acknowledged, not argued | Accepted | Added the reasoning that five more passes per 100 enrolments means helping one in six of the 30 non-completers to finish, and that pilot size fits weekly capacity (Section 3.2) |
| R6 | AQ4 objective counterfactual, limits without values, capacity figures differ | Accepted | Objective on likelihood of non-completion; precision of at least 50% and first-year recall within ten points of later-year recall, both as assumptions; referral destination; 30–40 everywhere (Sections 2.3 and 4.1) |
| R7 | AQ3 metric and threshold undefined; training data unclear | Accepted | Recall and precision at capacity length; D1 threshold = higher recall than the simple rule; training on earlier semesters of the course, or on the current course's submitted assessments when no earlier semester exists (Sections 4.1, 4.2 and 7) |
| R8 | Primary KPI counting rule unclear | Accepted | Course withdrawal and fail count as non-completion; leave and transfers leave the denominator (Section 3.3) |
| R9 | AQ1 compound and one-sided; period unclear | Partly accepted | Timing compared for both groups; period named as 2024–2025 and 2025–2026; one question kept, because timing and outcome describe the same enrolments |
| R10 | AQ2 "differ most" undefined; attendance absent in online courses | Accepted | Difference in later non-completion rates; attendance for blended courses only; weeks 1–4 (Sections 4.1 and 6.1) |
| R11 | Business Goal contains the means | Not accepted | The brief's own "better" example is "Nhận diện sớm sinh viên có nguy cơ không hoàn thành để hỗ trợ kịp thời" (identify early the students at risk of not completing, to support them in time); the goal leads with the outcome and names the timing that stakeholders asked for (PM1, AD1) |
| R12 | Persona caseload (300) and scenario capacity (4,000 for 3) unexplained | Accepted | Section 2.2 states that published figures shape the persona and the persona's own estimates drive capacity |

The reviewer prompt, with documents named by their place in this report:

```text
You are a reviewer of a student team's analytics project proposal for the course MTH045 – The Science of Data
Analytics. Read the instructor brief and Sections 1–7 of the proposal (English). Do not read any other
document.

Review the proposal as the brief's reviewer would. Check in particular:
1. SMART: is the SMART Goal specific, measurable, achievable, relevant and time-bound; are baselines and targets
   labelled as assumptions?
2. KPIs: one primary and at most two secondary; does each have a rationale and track the SMART Goal?
3. Analytical questions: are AQ1–AQ4 clear, specific, scoped, data-oriented and answerable; does the diagnostic
   question avoid causal language; does the predictive question state target, unit, horizon and data cut-off; does the
   prescriptive question state the decision, the action alternatives, the objective and the constraints?
4. Traceability: does each step follow from the previous one (stakeholder needs → Business Goal → SMART → KPI → AQ →
   analytics type → technique family → data → decision)?
5. Scope: does the proposal stay within Milestone 1 (no dataset analysis, no fixed algorithm)?
6. Anything vague, contradictory, unsupported or likely to confuse a reader.

Do not rewrite the proposal and do not propose new analytical questions of your own. Return a numbered list of at
most 12 critiques. For each: the section and sentence concerned (quote a few words), the problem, and why it matters.
Order them from most to least important.
```

===== reports/milestone-1/report/11-05-published-evidence.md @ 19d35a4 =====
## Appendix V – Published Evidence on Non-completion

This appendix sets out in detail the published findings that Section 1.1 summarises: how common non-completion is,
when it starts, why students leave and how institutions respond. The figures come from studies of real institutions,
not from the scenario university.

**How common non-completion is.** Published studies show that non-completion is common and that it starts early.
A systematic review of online learning found that retention, the share of students who stay and finish, is
significantly lower in online courses than in face-to-face ones, and that blended courses are completed more often
than fully online courses [5]. A 2024 Vietnamese review puts university dropout at about 20–30%, highest in the
first year [6]. These figures count students who leave a whole program; no published Vietnamese source gives a
figure for the completion of single courses taught online or in blended form, which is the level this project works
at.

**When non-completion starts.** In massive open online courses, the sharpest fall in participation comes in the
first two weeks [7]. In a blended first-year statistics course at an Irish university, weeks 5–6, halfway through the
semester, were the best point for an early warning, because students still had time to change how they studied,
while warnings based on midterm grades came too late, when some students had already dropped out [8]. Both findings point to the first weeks of a semester
as the period in which support can still change the outcome.

**Why students leave, and what institutions do.** Students who leave online courses report health, finances,
technology, isolation and workload as their reasons [9]. Vietnamese studies add family circumstances and weak
coordination between the offices that manage students [6]. The response most often recommended is early, proactive
contact: the institution reaches out to a student who shows signs of difficulty, rather than waiting for the student
to ask for help, and it bases that contact on data from the first weeks of the semester [5], [10].

===== reports/milestone-1/report/11-06-synthesis-detail.md @ 19d35a4 =====
## Appendix VI – Interview Method and Requirement Synthesis in Detail

This appendix gives the detail behind Sections 2.2–2.4: how the interviews were prepared and carried out, how the
stakeholders' answers were organised, how the themes were ranked, the requests left outside the scope, the conflicts
between stakeholders, and the full results of the validation round.

### 1. Interview Method

The interviews were prepared and carried out in four steps.

**Step 1: personas grounded in published accounts.** A persona is the role description that the AI follows when it
answers as a stakeholder. To keep the answers close to what real people in these roles report, each persona trait was
taken from a published source. The student persona draws on students who said that a "you are at risk" message could
make them give up [12], on withdrawal surveys in which work, family and health lead the reasons [13], and on
Vietnamese students who keep silent in online classes for fear of losing face [14]. The lecturer persona draws on
tutors who lose students between the second and the fourth assignment [15]. The advisor persona draws on advisor
caseloads of about 300 students each in the United States [16] and on evidence that students answer an advisor they
already know more readily [17]. The program manager persona draws on the regulated withdrawal limits [3], and the data
officer persona on Vietnam's personal data protection law, under which consent is given separately for each purpose
[18]. Details of identity, such as each persona's office, years of service and workload, are scenario
assumptions. So are the capacity figures
that the personas gave, such as three officers for about 4,000 students (AD2, AD3): they are the persona's own
estimates, not published figures.

**Step 2: open questions, written before the interviews.** We wrote seven or eight open questions for each
stakeholder. Every list covers the five information groups of the brief: business goals (what the stakeholder wants
to improve), success vision (how improvement would be recognised), challenges (what makes the problem hard), decision
making (what the stakeholder would decide with better information) and risk anticipation (what would stop the
stakeholder from trusting or using the results) [1]. To avoid leading the stakeholder, no question names a cause, a
data source or a tool, and none can be answered with a simple yes or no. The words "at risk", "dashboard",
"prediction" and "AI" appear only after the stakeholder has used them. Two draft questions broke these rules and were
rewritten: a lecturer question that proposed "an early-warning dashboard of LMS activity" and a student question that
asked whether "low online activity" caused the student to fall behind. Appendix I lists every question and both
rewrites.

**Step 3: one conversation per stakeholder.** Each conversation began with the role prompt of the brief, which tells
the AI to answer from the stakeholder's perspective, not to write AQs or technical solutions for the
team, and to state clearly when something is an assumption or the stakeholder's own view rather than a verified fact
[1]. The interviewer then asked the prepared questions in order. Where an earlier answer had already covered a
question in full, the interviewer asked a follow-up on the point that answer opened instead. Each interview has one or
two follow-ups, for example the question to the program manager about which staff should act first (PM4) and the
question to the support officer about how many students the office could follow up each week (AD3).

**Step 4: labelled key statements.** After each interview, we drew out its key statements, 51 in all across the
five interviews, and labelled each one in the three categories of the brief [1]. An opinion is the stakeholder's own
view or preference. An assumption is a figure or fact that the stakeholder gives as an estimate or impression, such as
the size of the support office. Scenario information is a fact given in the brief's scenario, such as the data that
the university holds. We checked every quoted statement against its transcript. Appendix II quotes the
statements with their labels.

### 2. Stakeholder Input Organised by Heading

Table A.14 sorts each stakeholder's answers under the five headings of the brief: the goal or need the stakeholder
expressed, the main challenge, the decision the stakeholder needs to take, how the stakeholder would recognise
success, and the risks and constraints the stakeholder raised. The six themes of Section 2.3 were read across its rows.

**Table A.14. Stakeholder input organised by the brief's synthesis headings**

| Stakeholder | Goal or need | Challenge | Decision needed | Success indicator | Risk or constraint |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Program Manager | Know within the semester which courses and groups lose students; real completion, not a better-looking rate (PM1, PM2) | Only end-of-semester and yearly figures; no new resources during a semester (PM5, PM8) | Where to put advisors' and tutors' time during the semester (PM6) | Students supported to complete; a pattern confirmed over several semesters (PM2, PM7) | Students labelled; results without reasons that cannot be defended (PM9, PM10) |
| Course Lecturer | Students who start the course finish it, having done the work (CL2) | Silence noticed only in week 5 or 6; messages to silent students go unanswered; one to one and a half hours a week for this work (CL4, CL5, CL10) | Whom to message before the second or third assignment deadline (CL6) | Every assignment submitted, not only the final one (CL2) | False alarms about students who are fine; results used to judge teaching (CL8, CL9) |
| Support Officer | Reach students before they reach the academic warning list (AD1) | Three officers for about 4,000 students; about 30–40 follow-ups a week (AD2, AD3, VAD7) | Whom to contact first, and with which kind of support (AD4, AD7, AD8) | Contacted students finish their courses, judged with care because those who answer may have finished anyway (AD6) | Lists too long to act on; students feeling watched; judgement must stay with a person (AD9, AD10) |
| Student | The course fits around work and family; some flexibility (ST1, ST5) | Too embarrassed to ask for help; nobody noticed when the student fell behind (ST2, ST4) | Whether to accept help, or pause in time | A practical option, such as an extension, offered early (ST5) | Labels such as "at risk"; effects on grades or records; contact in front of others (ST8, ST9) |
| Data Officer | Link the data the university already holds; agree what each number means (DO1, DO2) | Records matched by hand; about one week of delay; status records that may mix leave with withdrawal (DO3, DO4) | The purpose of data use and the rules of access, agreed by leadership and legal staff (DO7) | Data that staff can check by hand, delivered on an agreed schedule (DO6) | Consent for each purpose; data not clean enough for automated use (DO8, DO9) |

### 3. Priority of the Themes

Table A.15 scores each theme of Table 2.2 against the three criteria of the brief: its link to the organisation's
goal, its effect on decisions and its feasibility.

**Table A.15. Priority of the themes against the brief's three criteria**

| Theme | Link to the organisational goal | Effect on decisions | Feasibility | Priority |
| :---- | :---- | :---- | :---- | :---- |
| T1. Late detection | Direct: completion is the outcome the program reports | Makes decisions within the semester possible | Data already held (DO1) | Core |
| T2. Early start | Direct | Sets when staff can act | Quiz and assignment records are the most reliable LMS data (CL2, DO2) | Core |
| T3. Capacity | Indirect | Sets the length and order of a list | A known limit, with no new budget (PM8) | Core |
| T4. Contact | Indirect | Sets the action for each student | Depends on staff, not on data | Defines the actions of AQ4 |
| T5. Data trust | Enabling condition | A gate before any use | Needs governance decisions (DO7) | Constraint for Section 6 |
| T6. Support only | Enabling condition | Limits how results may be used | A matter of policy | Constraint for Sections 6 and 7 |

### 4. Requests Outside the Scope

Refining the core themes into the problem statement of Section 1.2 also removed the requests that lie outside the
project. Several related matters are outside the scope, each for a stated reason. Assessment rules and course content are
excluded, because a lecturer can change how students are supported during a semester but not what they are assessed
on (CL7). Admissions, enrolment quotas and financial aid are university policies that the program cannot change
within a semester. Students' circumstances outside the course, such as work and family, are outside the university's
control, so the project addresses the university's response to them, such as an extension or a short pause, rather
than the circumstances themselves (ST1, ST5). The evaluation of lecturers is excluded, because lecturers would stop using any result that might
be used to judge their teaching (CL9). Any automated decision about a student is excluded, because the stakeholders
want a person to decide whether and how to contact each student (AD9) and the data office judges that the data are not
yet clean enough for automation (DO9).

### 5. Conflicts between Stakeholders

Table A.16 sets out the three conflicts and the data constraint of Section 2.4, the statements on each side and the resolution we
adopted.

**Table A.16. Conflicts between stakeholders and our resolution**

| Conflict | One side | Other side | Resolution |
| :---- | :---- | :---- | :---- |
| Early contact against false alarms | The program manager and the lecturer want contact in the first weeks, while it can still help (PM3, CL6) | The lecturer, the student and the advisor warn that early lists are less certain, that flagging students who are fine destroys trust, and that students may feel watched (CL8, ST7, AD9) | Two review points, in weeks 3 and 5; a factual reason for each name; a member of staff checks each name before any contact; students are told about the process at the start of the course |
| Who makes contact | The program manager would have the lecturer-advisor or homeroom teacher call first (PM4) | The student prefers the course lecturer or a tutor who knows the course, and the support officer finds that students answer their own lecturer-advisor (ST6, AD5) | Contact comes from someone who knows the student, the lecturer or the student's lecturer-advisor; the support office takes the harder cases |
| Program figures against student-level action | The program manager needs figures by course and group to place staff (PM6) | The advisor and the lecturer need names to contact (AD4, CL6) | Two outputs: course and group patterns for the program manager, and a short contact list for lecturers and advisors |
| Constraint: automation against unready data | An automated list would save staff time, the usual reason for building an early-warning system | The data officer judges that the data are not yet clean enough for anything automated (DO9) | No automated action; data quality is checked in the data audit of Milestone 2 before any model is built |

### 6. Validation Results

Table A.17 gives the full results of the validation round of Section 2.4 under the four headings of the brief.

**Table A.17. Validation results under the brief's four headings**

| Validation content | Result |
| :---- | :---- |
| Points the stakeholders confirmed | A short list in order of urgency, with a factual reason for each name (all five stakeholders); contact by someone who knows the student, in supportive words that never say "at risk"; use for support only, with a person taking the final decision; missed quizzes and assignments as a better early sign than LMS activity (VDO1); the revised SMART Goal (VPM7) |
| Points the stakeholders asked to adjust | Detection is late and patchy rather than absent, because lecturers do sometimes alert the support office (VCL1, VAD1); two review points, in week 3 and week 5, kept away from registration and examination weeks (VCL2, VAD2); completion means passing the course, not merely staying enrolled (VPM6); the target is assessed over the 2027–2028 academic year rather than one semester, against a baseline recounted under Circular 83/2026 (VPM5, VPM8); consent for each purpose, and legal approval before any linking of records (VDO2); the student's family and employer are never told (VST2) |
| Points the stakeholders added | A program-level view of the courses and groups that lose students (VPM3); first-year students as a group of their own (VPM4); a shared record of each contact (VCL4); students who drift in several courses at once as a separate, more urgent case (VAD3); a simple "I'm fine, thanks" reply that closes the contact (VST3); a small pilot with comparison courses, so that a good result cannot come from choosing easy courses (VDO4, VPM9) |
| Points we did not adopt, with the reason | The advisor's suggestion to drop the completion target (VAD4); the lecturer's definition of completion as having done all the work (CL2); a general email instead of personal contact (VST5). Section 2.4 gives the reason for each |

===== reports/milestone-1/report/11-07-goal-kpi-detail.md @ 19d35a4 =====
## Appendix VII – SMART Goal and KPIs in Detail

This appendix gives the detail behind Sections 3.2 and 3.3. Table A.18 checks the SMART Goal against each of the five
criteria, and Table A.19 summarises the three KPIs, when each can be read and where its data come from.

**Table A.18. The SMART Goal against the five criteria**

| Criterion | How the goal meets it |
| :---- | :---- |
| Specific | It concerns one outcome, passing the course, for one population: students enrolled after the add-drop period in the pilot courses (about four courses with about 600 enrolments) of one program of about 1,200 students, in a faculty of about 4,000 students (both figures are scenario assumptions). Completion means passing the course (VPM6). |
| Measurable | It is measured by the primary KPI, the completion rate pooled over the pilot courses (Section 3.3), against a baseline recounted for 2024–2025 and 2025–2026 under Circular 83/2026 (VPM8). The assumed values are 70% before and 75% after. |
| Achievable | At a baseline of 70%, 30 of every 100 enrolments end without a pass; five more passes per 100 enrolments means helping five of those 30 students to pass, about one in six. The pilot is small enough for the weekly follow-up capacity of the support office and the lecturer-advisors (VAD6, VAD7). The program manager accepts the target over a full academic year rather than one semester (VPM5, VPM7). Published gains from early-warning programs are contested [19], so the target remains an assumption to be reviewed after the pilot. |
| Relevant | It measures the Business Goal directly, and it answers the needs of the program manager and the support office for real completion and earlier contact (PM2, AD1). |
| Time-bound | The contact process runs from Semester 2 of 2026–2027 through 2027–2028, and the target is the completion rate pooled over the pilot courses in 2027–2028, compared with the same courses' rate in 2024–2025 and 2025–2026. |

**Table A.19. Primary and secondary KPIs: what each measures, when it is read and where its data come from**

| KPI | Measures | Read | Data source |
| :---- | :---- | :---- | :---- |
| Primary: course completion rate | The SMART Goal: the share of enrolments that end in a pass | At the end of each semester | Academic management system: enrolment, final result, student status |
| Secondary 1: early-sign contact rate | Whether students with early signs are reached by the end of week 5 | In week 6 of each semester | LMS quiz and assignment records; contact record |
| Secondary 2: follow-up rate | Whether each list is used within seven days | One week after each review point | Contact lists; contact record |

===== reports/milestone-1/report/11-08-question-specification.md @ 19d35a4 =====
## Appendix VIII – Specification of the Analytical Questions

The brief sets requirements for each level of AQ: a descriptive question needs a metric, a
population, a period and segments; a diagnostic question must name the factors it compares; a predictive question
needs a target, a unit, a horizon and the data available at the time of prediction; and a prescriptive question must
state the decision, the alternatives, the objective and the constraints [1]. This appendix shows how each question of
Section 4.1 meets the requirements of its level and where each element comes from.

### 1. AQ1 – Descriptive

A descriptive question needs a clear metric, population, period and segment [1]. The metric is the share of
enrolments that ended in a pass, a fail or a withdrawal, and the week in which a student first missed an assessed
task. The population is students enrolled after the add-drop period, the period is the four semesters of 2024–2025 and
2025–2026, and the segments are course, delivery mode (online or blended) and year of study. Year of study was added
because the program manager asked for first-year students to be seen as a group of their own (VPM4). AQ1 gives the
program manager the view of courses and groups that the validation round asked for (VPM3), and it shows the next
question when non-completers begin to fall behind.

### 2. AQ2 – Diagnostic

A diagnostic question must name the factors it compares and must not claim a cause when the design cannot support one
[1]. AQ2 names four kinds of sign, each taken from the interviews: missed and late tasks, which the lecturer and the
data officer consider the most reliable early sign (CL2, VDO1); LMS activity, measured against the course's own
average because the same measure means different things in differently built courses (DO2); missed tasks in several
courses at once, which the support officer treats as a more urgent case (VAD3); and attendance, which exists only in blended
courses. The question asks which signs show the largest difference, not which signs cause non-completion, because
records of what students did cannot show why they did it. AQ2 hands to AQ3 the signs worth testing as predictors.

### 3. AQ3 – Predictive

A predictive question needs a target, a unit of prediction, a horizon and the data available at the time of
prediction [1]. The target is failing or withdrawing by the end of the semester. The unit is one student's enrolment in
one course, because a student may struggle in one course and not in another. The horizon is the rest of the semester.
Only data recorded by the end of week 2 and by the end of week 4 may be used, because exports from the LMS take about
a week (DO4), so these two data cut-offs feed the lists of week 3 and week 5. Accuracy is measured in two ways that
staff can read. Recall is the share of students who later fail or withdraw who appear on the list; precision is the
share of students on the list who later fail or withdraw. Both are measured on a list of the length staff can follow
up, because a longer list cannot be acted on (AD10). The comparison with a simple rule matters: an estimate that does
no better than counting missed tasks adds complexity without value. AQ3 hands to AQ4 an ordering of students by their
estimated likelihood of not completing.

### 4. AQ4 – Prescriptive

A prescriptive question must state the decision, the alternatives, the objective and the constraints, rather than ask
for a recommendation in general [1]. The decision is which students to list and in what order. The alternatives are
three kinds of contact, taken from the interviews and the validation round: a message from the lecturer or
lecturer-advisor who knows the student; a call from the support office, which takes the harder cases, such as students
missing in several courses, repeated warnings, or students whom their advisor could not reach after two tries
(VAD5); and a referral to the student affairs office for financial or personal support. The objective is to reach as
many as possible of the students most likely not to complete. The constraints are three. The list must fit weekly
capacity: three to five contacts per lecturer-advisor and about 30–40 for the support office (VAD6, VAD7). At least half of
the students on a list must be students who later fail or withdraw, a precision of at least 50%, so that staff do not
spend most of their time on students who are fine (CL8). First-year recall must stay within ten points of later-year
recall, so that the list does not miss the group the program manager most wants to protect (VPM4). The last two limits
are assumptions, to be reviewed with staff once the data audit of Milestone 2 shows what is achievable.

===== reports/milestone-1/report/11-09-approach-data-decision-detail.md @ 19d35a4 =====
## Appendix IX – Technique Families, Data Sources and Decision Classification in Detail

This appendix explains the choice of each candidate technique family of Section 5, describes the data sources and the quality risks of
Section 6, and gives the full definitions of the three decision classifications used in Section 7.

### 1. Choice of the Technique Families

The descriptive and diagnostic questions use the simplest families that answer them. AQ1 needs counts and rates broken
down by course, mode and year of study, and a comparison of timing between two groups. AQ2 compares the later
non-completion rate of students with and without each sign. Explanatory regression lets us see whether a sign
still differs once other signs are taken into account, for example whether missed tasks matter beyond low LMS
activity. AQ2 reports differences, not causes, because the records are observational: they show what students did,
not why they did it, and the brief warns against causal language without a causal design [1].

The predictive question is judged against a simple rule. In the blended course described in Section 1.1,
continuous-assessment results such as quizzes and assignments were the strongest early predictor [8], so a rule that
simply counts missed tasks is a demanding standard. A classification method earns its place only if it reaches more
of the students who later fail or withdraw than the rule does on a list of the same length. Validation is
time-based: the method learns from earlier semesters and is tested on a later one, as it would be used in practice.
Courses that have no earlier semesters can use methods that learn from the current course's own submitted
assessments [20]. Survival analysis, which models the time until an event such as withdrawal, is a candidate for the
withdrawal part of the target.

The prescriptive question turns the AQ3 ordering into a list that staff can act on. Decision rules cut the ordering at
the length that capacity allows, apply the precision and fairness limits, and route each student to the lecturer,
the lecturer-advisor or the support office. What-if analysis shows how the limits change the list, for example how
many more non-completers a list of 40 names would reach than a list of 30. Each name carries its reason as an observed
fact, such as two quizzes missed since week 2, because staff said that a score without a reason would be ignored
(VCL3, PM9).

### 2. Data Sources

The data needs of Table 6.1 draw on four sources. The academic management system, run by the academic affairs office, holds each student's enrolments, final
results, status (enrolled, on leave, transferred, withdrawn) and year of study. The LMS holds course pages, quiz and
assignment records with their due and submission dates, and activity logs of what each student opened and when.
Attendance lists of in-class sessions exist only for blended courses and are kept by lecturers. Staff rosters give the
weekly capacity of lecturer-advisors and the support office. According to the data officer, these sources share a
student identifier, but nothing links them automatically, so records are matched by hand (DO1).

Table A.20 sets out the five data quality and feasibility risks of Section 6.2, where each was raised and how the
project handles it.

**Table A.20. Data quality and feasibility risks**

| Risk | Raised by | Handling |
| :---- | :---- | :---- |
| Student status mixes approved leave and transfers with real withdrawal, which distorts the outcome | Data officer and program manager (DO3, VPM2); Circular 83/2026 [4] | Recount the baseline years under the definitions of Circular 83/2026 (VPM8) |
| The same LMS measure means different things in courses built differently | Data officer (DO2) | Compare activity within each course; rely mainly on quiz and assignment records (VDO1) |
| Activity is not learning: a student can keep logging in while falling behind | Lecturer and student (CL3, VST1); published work [22] | Use missed and late tasks as the main signs; a member of staff checks each name |
| Records are matched by hand, with about one week of delay | Data officer (DO1, DO4) | Data of weeks 2 and 4 feed the lists of weeks 3 and 5 (VDO3) |
| Small groups give unstable rates and can identify individual students | Group comparisons in AQ2 and AQ3 | Report group results only above an agreed minimum group size |

### 3. Decision Classifications

The brief asks for three classifications [1], each from an established
framework. The first is the level of the decision. Gorry and Scott Morton [24] draw on Anthony's three levels of
managerial activity: strategic planning decides on the organisation's objectives and the resources used to attain
them; management control ensures that resources are used effectively and efficiently towards those objectives; and
operational control ensures that specific tasks are carried out. These correspond to the brief's strategic, tactical
and operational levels. The second is whether a decision is programmed. Gorry and Scott Morton also draw on Simon, for
whom a decision is programmed to the extent that it is repetitive and routine, with a definite procedure worked out
for it, and non-programmed to the extent that it is novel, unstructured and consequential; the two are ends of a
continuum, not sharp categories [24]. The third is reversibility. Bezos separates one-way doors, decisions that are
consequential and nearly irreversible and must be made slowly, with great deliberation and consultation, from two-way
doors, decisions that can be reversed and can therefore be made quickly [25].
