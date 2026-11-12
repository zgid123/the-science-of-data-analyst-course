# Draft A – Storytelling with Data: full speech script, Milestone 5 final presentation

## Method

**Method used.** Storytelling with Data (Cole Nussbaumer Knaflic): understand the context, choose the right visual,
remove clutter, focus attention, think like a designer, tell a story. The narrative arc follows Brent Dykes' data
storytelling arc (setting and hook, rising points, aha moment, solution and next steps), which the method recommends
for data insight talks.

**Context (who / what / how).**

- **Who.** Our lecturers and classmates. They read rates, intervals, logistic regression and recall without help, but
  they have not seen OULAD or our five reports, so every term is defined where it first appears and on every slide
  that uses it.
- **What they should know or do.** Know what the data answer and what they do not; accept that the early-sign list
  must include inactivity because missed tasks come too late; agree that the next step is one held-out model test
  and a randomised pilot, not a deployment.
- **How.** A live group talk with slides, read again later as the deck. Slides stay sparse (lead sentence plus one
  visual or one short table); the speaker notes carry the explanation. Detail slides carry the evidence the course
  brief requires and can move to an appendix section.

**Big Idea (one sentence).** Students who drift away from an online course leave traces in the records weeks before
staff notice, but missed tasks show up too late for most of them, so the university should start from an
interpretable early-sign list that includes inactivity, test a model against it once, and run a randomised pilot
before claiming that early contact helps.

**3-minute story.** A Vietnamese university notices disengaging students only at week 5 or 6 or at the end of the
semester, while the window for help is two to four weeks. Staff need a short list at weeks 3 and 5 with a reason
beside each name. No open dataset of Vietnamese courses exists, so we used OULAD, 22 runs of seven UK
distance-learning modules from 2013 and 2014, as a stand-in, and dated every sign by its cut-off. Four questions
climb the analytics levels. Two are answered: 45.3% of the enrolments still registered at day 14 did not complete,
and all five early signs go with later non-completion within module in both years, a missed task most strongly. But
fewer than one in five non-completers had missed a task by week 4: a task-only list would be too late, so the list
needs inactivity. The model test and the effect of contact are designed, not run; they are the next steps, and every
result must be re-checked on the university's own records.

**Arc (storyboard).** Setting (slides 1–13: context, stakeholders, goal, decisions) → hook (slide 3: noticed at week
5 or 6, while help works in weeks 2 to 4) → rising points (slides 14–45: questions, data, preparation, method,
evaluation, status) → aha moment (slides 49 and 54: the strongest sign, a missed task, reaches under one in five
non-completers by week 4, so the list must count inactivity) → solution (slides 55–64: expected outputs, decision
support, pilot) → conclusions (slides 65–70). The executive summary (slide 2) gives a one-line preview of the answer,
the bottom-line-up-front exception the method allows for an academic audience, and keeps the tension for the
timing finding.

**Visual principles.** Grey for context, one accent colour for the number the lead sentence names; horizontal bars for
comparisons, a dot-and-interval chart for the signs, a cumulative line for timing, tables only where the reader looks
things up (matrices the course brief requires). No pie charts, no 3D, no dual axes; direct labels instead of legends
where possible; every chart carries its key on the slide. Horizontal logic: the slide titles read in order tell the
story; vertical logic: each slide stands alone with its lead sentence and its own key.

**Sources.** Every number comes from the Milestone 5 report (M5), cited as section, appendix and table; earlier reports
(M1–M4) are named only for how a step was reached.

## Coverage table

| Brief part | Slides |
| :---- | :---- |
| Abstract / executive summary | 2 |
| 1 Introduction and educational context (context, motivation, stakeholders, scope, objective) | 3, 4, 5, 6, 7, 8, 9 |
| 2 Business understanding and success criteria (Business Goal, SMART Goal, primary and secondary KPIs, D1–D3) | 10, 11, 12, 13, 17 |
| 3 Analytical questions and analytics levels (final AQ1–AQ4, levels, scope, decision, quality check, revision status) | 14, 15, 16, 17, 18 |
| 4 Data requirements and dataset selection (unit, outcome, concepts, time, population, candidates, rationale, provenance, licence; Data Requirement Matrix) | 19, 20, 21 |
| 5 Dataset description and requirement–data fit (tables, keys, coverage, gaps, keep/modify/defer; data dictionary, AQ–Data Fit Matrix) | 22, 23, 24, 25 |
| 6 Data understanding and quality (distribution, missingness, duplicates, invalids, outliers, imbalance, temporal coverage, representativeness, sensitive fields) | 26, 27, 28, 29, 30, 31 |
| 7 Data preparation (cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control, final versioned dataset; Preparation Decision Matrix) | 32, 33, 34, 35 |
| 8 Modeling and analysis strategy (AQ → type → task → baseline → candidates → primary proposal → rationale; Method Selection Matrix) | 36, 37, 38 |
| 9 Evaluation design (metric, baseline, split and validation, success criterion, leakage, fairness, interpretability) | 39, 40, 41, 42 |
| 10 Experimental status (Level 2 not run, and why) | 43, 44 |
| 11 Findings, discussion and decision support (AQ-by-AQ answers, Final Project Traceability Matrix, D1–D3) | 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61 |
| 12 Limitations and future work (limitation log, deferred AQs, next data, pilot) | 62, 63, 64, 68 |
| 13 Generative AI use and reflection (AI Decision Log) | 65, 66 |
| 14 Conclusion | 67, 68, 69, 70 |

**Line counts.** 70 slides: 46 marked `Line: main`, 24 marked `Line: detail`.

---

## Slide 1 – Early Identification of Disengaging Students in Online Courses   [Title]   [Line: main]
**Lead:** A final project on finding, early enough to help, the students who stop taking part in an online course.
**On the slide:** MTH045 – The Science of Data Analytics, University of Science, VNU-HCM · Milestone 5: Final
Integration and Project Report · Team N04: 25C12002 – Lê Ngọc Trúc Huỳnh; 25C12003 – Phan Trần Khanh; 25C12031 –
Dương Tấn Huỳnh Phong · Lecturers: Dr. Nguyễn Trần Minh Thư, MSc. Phạm Minh Tú · 14 November 2026.
**Visual:** none; a clean title slide with the project title large and the team block small.
**Speaker notes:** Good morning, and thank you for having us. We are team N04, and over five milestones we have
followed one question from a stakeholder's worry to the evidence and back to a decision. The worry is simple: in an
online course, a student can stop taking part and nobody notices until it is too late to help. Our project asks
whether the records a university already holds could show that drift early, and what a member of staff could
responsibly do with such a signal. We will show you what our data could answer, what they could not, and what we
propose to do next. Before the details, here is the whole answer on one slide, so you know where the story is going.
**Sources:** [M5 Title page]

## Slide 2 – Executive Summary   [Abstract]   [Line: main]
**Lead:** Early signs are visible in the records, but missed tasks come too late for most students, so an early list must count inactivity, and its value must still be tested.
**On the slide:** Three cards.
- **Problem.** Disengaging students are noticed at week 5 or 6 or after the semester; help works best within two to
  four weeks.
- **What the data show.** On OULAD (Open University Learning Analytics Dataset, 22 UK module runs of 2013 and 2014,
  our stand-in data): 45.3% (44.7–45.8) of the 28,061 enrolments still registered at day 14 did not complete; under
  one in five non-completers had missed a task by week 4; all five early signs go with later non-completion in both
  years, a missed task by 40.8 and 39.3 percentage points.
- **What stays open.** The model test (AQ3, predictive) and the ranked list (AQ4, prescriptive) are designed, not run;
  the effect of contacting a student needs a randomised pilot.
**Visual:** none; three text cards left to right (problem, evidence, open), with the two key numbers in the accent
colour.
**Speaker notes:** Here is the story in thirty seconds. Students who drift away are noticed late. We could not get
Vietnamese course data, so we used an open UK dataset, OULAD, as a stand-in. On it, almost half of the enrolments
still registered after the add-drop period did not complete. Five early signs, from missed tasks to days without a
click, all go with later non-completion, and they do so in both years. But the surprise is timing: fewer than one in
five of the students who later failed or withdrew had missed a task by week 4. Two of our four questions are
answered; the predictive and prescriptive ones are fully designed but not run. Let us start where the problem starts,
with how late students are noticed today.
**Sources:** [M5 Abstract], [M5 §11.2], [M5 §11.3], [M5 §10]

## Slide 3 – Noticed Too Late   [1 Introduction]   [Line: main]
**Lead:** Each group of staff notices a disengaging student only after the moment when help would be easiest.
**On the slide:** A timeline of a semester, weeks 1 to 15.
- Window for effective support of a student at risk: two to four weeks (published evidence).
- Lecturers become sure a student has gone quiet: around week 5 or 6.
- Program manager sees pass and withdrawal counts: after the semester.
- Support office meets most of these students: on the academic warning list at the end of the semester.
- Footnote: staff timings come from simulated interviews in which AI played both sides; they motivate the design and
  are not evidence.
**Visual:** timeline (sequence): one horizontal week axis, the support window shaded in the accent colour, the three
moments of notice as grey markers to the right of it. The gap between them is the message.
**Speaker notes:** After that summary, let us go back to the start. The project is set in a Vietnamese university
expanding online and blended learning on its learning management system, one undergraduate program of about 1,200
students, which is a scenario assumption. Look at the timeline. Published work puts the window for helping a student
at risk at two to four weeks. In our simulated interviews, lecturers become sure only around week 5 or 6, the
program manager sees counts after the semester, and the support office meets these students on the warning list at
its end. Every moment of notice falls after the window. One caution we will repeat: those interviews were AI on both
sides, so they shape the design, never the evidence. Why does this matter beyond good teaching? Because withdrawal is
now regulated.
**Sources:** [M5 §1], [M5 App I]

## Slide 4 – Withdrawal Is a Regulated Measure   [1 Introduction]   [Line: detail]
**Lead:** Vietnamese regulation caps withdrawal rates, so a university needs exact status records and an early view of who is drifting away.
**On the slide:**
- Circular 01/2024: annual withdrawal rate capped at 10%, first-year rate at 15%; above 15% in the first year, the
  enrolment quota may not rise.
- Circular 83/2026, from 15 November 2026: keeps these thresholds; approved leave and transfers do not count as
  withdrawal.
- Online classes: up to 30% of a full-time or work-study program's volume (2021 training regulation).
**Visual:** none; three short statements with the two thresholds (10%, 15%) in the accent colour.
**Speaker notes:** The timeline showed that students are noticed late; this slide shows why the university cannot
shrug that off. Circular 01/2024 caps the annual withdrawal rate at 10% and the first-year rate at 15%, and a
university over the first-year cap may not raise its enrolment quota. Circular 83/2026, in force from 15 November
2026, keeps these thresholds and excludes approved leave and transfers from withdrawal. At the same time, a program
may now teach up to 30% of its volume online. Together these rules make withdrawal a measured quality indicator, and
they require a correct record of each student's status. That is also why our completion measure later follows the
Circular's definition. Next, what published research says about when disengagement starts.
**Sources:** [M5 §1], [M5 App I]

## Slide 5 – What Published Studies Report   [1 Introduction]   [Line: detail]
**Lead:** Published studies agree that non-completion online is common and that the useful moment for support lies in the first weeks.
**On the slide:**
- A 2024 systematic review of 110 articles (2013 to June 2023): dropout in online higher education is a significant
  concern, with several contributors acting at once.
- A review of 40 studies (2010–2018): completion online about 8 to 14 points below face-to-face courses.
- Vietnam: dropout among university students about 20–30% (2024 review).
- Massive open online courses: about half of enrolled students never show up; the first two weeks are critical.
- A blended first-year statistics course: weeks 5–6 were the best point for an early warning.
**Visual:** none; five short evidence lines, the timing statements in the accent colour.
**Speaker notes:** Regulation raises the stakes; research tells us where to look. A systematic review of 110 articles
treats online dropout as a significant concern with several causes acting at once. Another review of 40 studies puts
online completion about 8 to 14 points below face-to-face courses, and a Vietnamese review puts university dropout at
about 20 to 30 percent. On timing, half of the students in massive open courses never show up, the first two weeks
are critical, and in one blended statistics course weeks 5 to 6 were the best moment for a warning, still early
enough for students to change course. So the first weeks matter, well before any final grade. Now, who in the
university could act on an early signal?
**Sources:** [M5 App I]

## Slide 6 – Who Decides and What They Need   [1 Introduction]   [Line: main]
**Lead:** Five stakeholder groups each see part of the problem, and three decisions, D1 to D3, depend on the answer.
**On the slide:** A table, one row per stakeholder.
| Stakeholder | Need | Decision |
| :---- | :---- | :---- |
| Course lecturer | A short weekly list with a factual reason for each name | D1: whom to contact at each review point |
| Support office and lecturer-advisors | Reach students before the warning list, within a fixed weekly capacity | D1 |
| Program manager | Which courses and groups lose students, and when | D2: where to place support time each semester |
| Leadership, legal staff, data office | A lawful purpose before data are linked | D3: whether to extend the approach |
| Student | Contact from someone known, data used for support only | Whether to accept help |
- Capacity voiced: about 30–40 contacts a week for the support office, three to five per lecturer-advisor.
**Visual:** table (structure): five rows; the decision column in the accent colour.
**Speaker notes:** If research says the first weeks matter, who would act in them? The course lecturer sees first who
stops submitting work and wants a short list with a reason beside each name. The support office and the
lecturer-advisors, lecturers who advise student classes, do the contacting with little time: about 30 to 40 contacts a
week for the office and three to five for each advisor. These two groups share decision D1, whom to contact. The
program manager decides D2, where support time goes each semester. Leadership, with legal staff and the data office,
decides D3, whether to extend the approach. And students are the subject of every data use. These needs set the shape
of everything that follows. Where did they come from? From interviews that we have to describe honestly.
**Sources:** [M5 §1.1], [M5 App I Table A.1]

## Slide 7 – Needs from Simulated Interviews   [1 Introduction]   [Line: detail]
**Lead:** The stakeholder needs come from interviews in which generative AI took both sides, so they motivate the design and are never used as evidence.
**On the slide:**
- How: an isolated AI persona answered for each stakeholder; an AI interviewer asked our questions and follow-ups;
  a validation round followed (Milestone 1).
- What we kept: 51 key statements, each labelled as opinion, assumption or scenario information; each quote checked
  against its transcript.
- What they set: lists at weeks 3 and 5, a factual reason per name, list length within capacity, support only, no
  automated step.
- What they are not: evidence for any finding; every finding rests on the data or on published work.
**Visual:** none; a two-column "used for / not used for" split.
**Speaker notes:** We just listed what each stakeholder needs. Here is the honest part: those needs come from
simulated interviews. In Milestone 1 an AI persona answered for each stakeholder and an AI interviewer asked our
questions, then a validation round checked the synthesis. We verified every transcript and kept 51 key statements,
each marked as an opinion, an assumption or scenario information. These statements decided practical things: a list
at weeks 3 and 5, a reason beside each name, a length staff can follow up, and no automated step. They never support
a finding. Everything we report as a result comes from the data or from published studies. With the needs set, we
can draw the boundary of the project.
**Sources:** [M5 §1.1], [M5 App I], [M5 App XVI Table A.43]

## Slide 8 – Scope and Objective   [1 Introduction]   [Line: main]
**Lead:** We aim to turn records the university already holds into a short, timely contact list with a reason for each name, within one semester and with no automated decision.
**On the slide:**
- In scope: students enrolled after the add-drop period in the program's online and blended courses; one semester at
  a time; decisions staff can take within a semester.
- Completion means passing the course; withdrawal follows Circular 83/2026 (approved leave and transfers excluded).
- Out of scope: assessment rules, admissions and financial aid, students' circumstances outside the course, the
  evaluation of lecturers, any automated decision.
- Objective: a short list at each review point with an observed reason per name, and patterns that show where and
  when students are lost.
- Data: no open dataset of Vietnamese courses exists, so OULAD (Open University Learning Analytics Dataset) stands in;
  every result must be re-checked on the university's records.
**Visual:** none; an in-scope / out-of-scope two-column layout with the objective sentence across the top.
**Speaker notes:** Knowing who needs what, we drew the boundary. We cover students enrolled after the add-drop period,
one semester at a time, and only decisions staff can take inside that semester. Completion means passing the course,
and withdrawal follows Circular 83/2026. We leave out assessment rules, admissions, students' lives outside the
course, the evaluation of lecturers and any automated decision; a person always decides. The objective is two
things: a short, timely list with an observed reason for each name, and patterns that show the program where students
are lost. One constraint shapes everything after this: no open dataset of Vietnamese courses exists, so we use OULAD,
an open UK dataset, as a stand-in, and every result needs a re-check at the university. Here is the whole project as
one chain.
**Sources:** [M5 §1.2], [M5 App I]

## Slide 9 – The Project as One Chain   [1 Introduction]   [Line: main]
**Lead:** One chain of eleven links runs from the stakeholder problem to the decisions, and this talk follows it in order.
**On the slide:** The eleven-link logic chain across Milestones 1–5: problem → stakeholders → goal and KPIs →
decisions → questions → data requirements → dataset → preparation → method → evaluation → findings and decisions.
Under it, a bar showing which milestone produced each link (Milestone 1: problem to questions; 2: requirements and
dataset; 3: understanding and preparation; 4: method and evaluation; 5: findings and integration). Key: KPI = key
performance indicator.
**Visual:** flow diagram (sequence): the chain as connected boxes, the current section highlighted in the accent colour
as a running roadmap; based on Figure 1.1 of the report.
**Speaker notes:** Before going link by link, here is the map. Our project is one chain of eleven links, from the
stakeholder problem through the goal, the decisions and the questions, to the data, their preparation, the method,
the evaluation and finally the findings and the decisions they support. The first milestone built the front of the
chain, the second found the data, the third understood and prepared them, the fourth chose methods and fixed how to
judge them, and this fifth milestone answers what can be answered and ties it back to the decisions. We will
highlight where we are on this chain as we go, so you never lose the thread. The first link after the problem is the
goal.
**Sources:** [M5 §1.2 Figure 1.1]

## Slide 10 – Business Goal and SMART Goal   [2 Business understanding]   [Line: main]
**Lead:** The goal is more students passing their courses, not a model or a dashboard, and the SMART target makes it measurable with assumed values.
**On the slide:**
- **Business Goal:** improve successful course completion in the program's online and blended courses by identifying
  students who stop taking part early enough to support them within the semester.
- **SMART Goal** (specific, measurable, achievable, relevant, time-bound): raise the completion rate of students
  enrolled after add-drop in the pilot courses from the recounted baseline (assumed 70%) by five percentage points
  (assumed target 75%) by the end of the 2027–2028 academic year.
- Pilot courses: about four courses with about 600 enrolments (assumptions), fixed in advance, compared with similar
  courses outside the pilot.
- The goal measures progress, not the effect of contact.
**Visual:** a simple two-point slope from 70% to 75% labelled "assumed baseline" and "assumed target", in grey with
the five-point gap in the accent colour.
**Speaker notes:** The chain starts with a goal, and we kept it about students, not tools: more students passing
their courses, by finding the ones drifting away in time. The SMART version raises completion in the pilot
courses by five percentage points, from a recounted baseline we assume is 70% to 75%, by the end of 2027 to 2028.
Both values are assumptions, since the scenario gives no real rate; the university's records replace them before any
target is committed. The pilot courses, about four with about 600 enrolments, are fixed in advance and compared with
similar courses, so the target cannot be met by picking easy ones. And note the limit: this goal measures progress,
not whether contact caused it. Is five points realistic?
**Sources:** [M5 §2], [M5 App II]

## Slide 11 – Is the Target Achievable?   [2 Business understanding]   [Line: detail]
**Lead:** At the assumed baseline, five more points means about one in six non-completers passing after support, which fits capacity but remains an assumption.
**On the slide:**
- At 70% completion, about 180 of 600 enrolments end without a pass.
- Five more passes per 100 enrolments: about 30 of them, one in six, would have to pass after support.
- Reaching them fits the weekly capacity staff reported; that one in six would then pass is an assumption, not an
  estimate.
- Time-bound: contact from Semester 2 of 2026–2027; target read on the pilot courses over 2027–2028.
**Visual:** a worked example (simple arithmetic): 600 → 180 non-completers → about 30 extra passes, as three stacked
numbers.
**Speaker notes:** Is five points realistic? Here is the arithmetic. At the assumed 70% baseline, about 180 of 600
enrolments end without a pass. Five more points means about 30 of them, roughly one in six, passing after support.
Reaching 30 students over a year fits the weekly capacity staff described. But whether one in six of them would then
pass is an assumption: no data in this project measure what contact achieves, which is exactly why the pilot exists.
The horizon is a full academic year because, in the validation round, the simulated program manager doubted that five
points could be gained in one semester. With the goal fixed, how do we watch it during the semester?
**Sources:** [M5 App II Table A.2]

## Slide 12 – Primary and Secondary KPIs   [2 Business understanding]   [Line: main]
**Lead:** One primary KPI measures the goal and two secondary KPIs show during the semester whether contact happens; on OULAD only parts of them can be computed.
**On the slide:** Key: KPI = key performance indicator; OULAD = Open University Learning Analytics Dataset (stand-in
data); TMA = tutor-marked assignment; CMA = computer-marked assessment.
| KPI | Definition | On OULAD |
| :---- | :---- | :---- |
| Primary: completion rate | Passes over enrolments after add-drop | Proxy at day 14: 28,061 enrolments (22 runs) |
| Secondary 1: early-sign contact rate | Students meeting the early-sign rule at the end of week 4 contacted by the end of week 5 | Sign part only: the rule flags 28.8% of 27,535 at day 27 |
| Secondary 2: follow-up rate | Listed students contacted within seven days | Only in the pilot |
- Early-sign rule: by the data cut-off, a TMA or CMA due but not submitted, a TMA submitted late, or no platform
  activity in the previous seven days.
**Visual:** table (lookup): three rows; the "On OULAD" column in grey except the two numbers in the accent colour.
**Speaker notes:** A goal read once a year needs indicators staff can watch. The primary KPI is the completion rate
over students enrolled after add-drop. On OULAD it becomes a proxy: enrolments still registered at day 14, 28,061 of
them over 22 runs. The two secondary KPIs track contact. The first is the share of students meeting the early-sign
rule at week 4 who are contacted by week 5; the rule flags a missed task, a late tutor-marked assignment, or a week
without any click. On OULAD we can compute only its sign part: the rule flags 28.8% of 27,535 enrolments at day 27.
The second, follow-up within seven days, needs a contact record, so it lives only in the pilot. These indicators
serve three decisions.
**Sources:** [M5 §2.1 Table 2.1]

## Slide 13 – Three Decisions   [2 Business understanding]   [Line: main]
**Lead:** The three decisions differ in how reversible they are, and that sets how much evidence each one needs.
**On the slide:**
| Decision | Owner | Reversible? | Evidence needed |
| :---- | :---- | :---- | :---- |
| D1: whom to contact at each review point | Lecturers, lecturer-advisors, support office | Yes: a contact that does not help can be followed by another | A list that beats the early-sign rule on the same length, each name checked by staff |
| D2: where to place support time each semester | Program manager | Yes: staff can be moved next semester | A pattern that repeats over semesters |
| D3: whether to extend the approach and link data routinely | Leadership, legal staff, data office | Close to irreversible | Pilot results and legal approval |
**Visual:** table (structure) with a reversibility scale from left (easy to undo) to right (hard to undo) drawn above
it; D3 in the accent colour.
**Speaker notes:** The KPIs feed three decisions, and they are not equal. D1, whom to contact at each review point, is
frequent and reversible: if a contact does not help, another can follow. So it can start with a simple rule checked by
staff, and a model replaces the rule only if it reaches more later non-completers on a list of the same length. D2,
where the program manager places support time, moves scarce staff between courses, so it needs a pattern that repeats.
D3, whether to extend the approach and link data routinely, is close to irreversible: it changes the university's data
practice and students' trust, so it needs pilot results and legal approval. To serve these decisions we asked four
questions.
**Sources:** [M5 §2.1], [M5 App II Table A.3]

## Slide 14 – Four Questions, Four Levels   [3 Analytical questions]   [Line: main]
**Lead:** Four analytical questions climb the analytics levels, and each answer is read only at its own level.
**On the slide:** Key: AQ = analytical question (AQ1–AQ4, one per level in the table); D1 contact, D2 support time, D3 extension; unit = one student's
enrolment in one module run; day 13 and day 27 = data cut-offs for the week-3 and week-5 lists.
| AQ | Level | Final question (short) | Decision | Status |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Share ending in pass, fail or withdrawal, by module, run, start month and year; week of the first missed task | D2, D3 | Answered |
| AQ2 | Diagnostic (association only) | Which signs by the end of week 4 go with later non-completion, within module | D2; reasons in D1 | Answered |
| AQ3 | Predictive | How well a model built on 2013 estimates non-completion in 2014 at weeks 2 and 4, against the early-sign rule | D1 | Deferred |
| AQ4 | Prescriptive (ranking under capacity) | Which enrolments rank first on a list of assumed capacity, with what gain and recall, by group | D1 | Deferred |
**Visual:** table (structure) with a staircase of levels on the left; Answered rows in the accent colour, Deferred rows
in grey.
**Speaker notes:** The three decisions need evidence, and we organised it as four questions, one per analytics level,
all on one unit, a student's enrolment in one module run. AQ1 is descriptive: what share ends in pass, fail or
withdrawal, and when non-completers first miss a task. AQ2 is diagnostic: which early signs go with later
non-completion, read as association only. AQ3 is predictive: can a model built on 2013 runs do better than the
early-sign rule on 2014 runs. AQ4 is prescriptive: who should rank first on a list of fixed capacity. The status
column is the honest summary: AQ1 and AQ2 are answered; AQ3 and AQ4 are deferred, designed but not run. Are these
questions well formed?
**Sources:** [M5 §3 Table 3.1]

## Slide 15 – Quality Check of the Questions   [3 Analytical questions]   [Line: detail]
**Lead:** All four questions are clear, specific, scoped and data-oriented; they differ only in how far the data can answer them.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking.
| Criterion | Test | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Clear | Asks one thing a reader can restate | Met | Met | Met | Met |
| Specific | Names its measure and groups | Met | Met | Met | Met |
| Scoped | Fixes population and period | Met | Met | Met | Met |
| Data-oriented | Names its data | Met | Met | Met | Met |
| Answerable | Data can settle it | Answered | Answered (association) | By a design not yet run | Ranking only; contact has no data |
- Status scale: Answered, Partial, Deferred, Dropped; no question is dropped.
**Visual:** table (lookup): a check grid; the answerable row in the accent colour, since that is where they differ.
**Speaker notes:** Before answering questions, we checked that they were worth answering. The course asks that every
question be clear, specific, scoped, data-oriented and answerable. In their final wording all four pass the first
four tests. The difference lies in answerability. AQ1 and AQ2 are answered on the 2013 and 2014 runs. AQ3 is
answerable by a design that has not been run yet. For AQ4, only the ranking part is answerable, because no data record
any contact with a student, so we deferred the contact part rather than fill it with assumptions. No question was
dropped. But none of them is worded as in Milestone 1; let us see how the data changed them.
**Sources:** [M5 §3.1], [M5 App III Table A.4], [M5 §3 Table 3.1]

## Slide 16 – How the Questions Changed   [3 Analytical questions]   [Line: main]
**Lead:** Every question was narrowed by what the data lack, and each change is recorded with its reason.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; OULAD = Open
University Learning Analytics Dataset (stand-in data); YELLOW = narrow the question; RED = a key concept or intervention missing.
| AQ | Milestone 1 wording | Data finding | Final form | Action |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | By course, delivery mode, year of study | No mode or year of study (YELLOW) | By module, run, start month, year | Modify |
| AQ2 | Signs incl. attendance, across modes and years | No attendance (YELLOW) | Signs by week 4, within module | Modify |
| AQ3 | Against a two-task rule | Few tasks due by the cut-offs (YELLOW) | Against the early-sign rule, 2013 to 2014 | Modify |
| AQ4 | List, order and contact; precision of at least 50% | No contact data; base rate about 45% (RED) | Ranking under capacity, by group | Modify + Defer |
**Visual:** table (comparison, before → after) with an arrow between the Milestone 1 and final columns.
**Speaker notes:** None of our questions survived Milestone 1 unchanged, and that is the data talking. AQ1 asked by
delivery mode and year of study, but OULAD records neither, so it compares modules, runs and start months. AQ2 wanted
attendance at class sessions; there are none. AQ3 was to beat a rule of two missed tasks, but too few tasks fall due
in the first weeks, so the rule changed. AQ4 asked for a list, an order and a type of contact with at least 50%
precision; there are no contact data, and with a base rate near 45% even a random list reaches about that precision.
So AQ4 became a ranking, with contact deferred. Two of these changes deserve their own slide; first, the add-drop
rule.
**Sources:** [M5 §3.2 Table 3.2], [M5 App III Table A.8]

## Slide 17 – The Add-Drop Rule on OULAD   [2 Business understanding / 3 Analytical questions]   [Line: main]
**Lead:** On OULAD, "enrolled after add-drop" becomes "still registered at day 14", because registration closes two weeks after a run starts.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset (stand-in data); run = one offering of a
module; day 0 = the start of the run; KPI = key performance indicator.
- Milestone 1: students enrolled after the add-drop period, withdrawal as in Circular 83/2026.
- On OULAD: enrolled at day d = registered by day d (or registration day unknown) and not unregistered by day d.
- Why: registration closes two weeks after the start; 58 enrolments registered after day 14, up to day 167.
- Result: the primary KPI (completion rate) is counted on 28,061 enrolments; the same rule gives the list
  populations at day 13 and day 27.
- Limit: approved leave and transfers cannot be told apart from withdrawal on OULAD.
**Visual:** a small timeline (sequence) of days −30 to 30 with day 0 and day 14 marked; the population counted from
day 14 in the accent colour.
**Speaker notes:** The first change looks technical but moves every rate. Our KPI counts students enrolled after the
add-drop period. OULAD has no add-drop flag, but it has registration and unregistration days counted from the start
of each run, and registration closes two weeks after the start. So an enrolment counts if it is registered by day 14
and not unregistered by then. A few records registered later, 58 of them, some as late as day 167, which is why the
rule is stated for every day, not only day 14. The result is 28,061 enrolments in the KPI population, and the same
rule defines who is on a list at day 13 and day 27. You will see later that this choice moves a rate by more than ten
points. The second change concerns the rule itself.
**Sources:** [M5 §2.1], [M5 App III Table A.8], [M5 App VII Table A.18]

## Slide 18 – One Early-Sign Rule   [3 Analytical questions]   [Line: main]
**Lead:** A rule based on tasks alone cannot fire in the first weeks of most runs, so the early-sign rule adds a week without platform activity.
**On the slide:** Key: TMA = tutor-marked assignment; CMA = computer-marked assessment; cut-off = the last day of data
for a list (day 13 for week 3, day 27 for week 5); KPI = key performance indicator.
- Milestone 1 rule: two or more assessed tasks missed or late by week 4.
- Finding: two or more tasks fall due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1.
- Final rule: by the cut-off, a TMA or CMA due but not submitted, or a TMA submitted late, or no platform activity in
  the previous seven days.
- One rule for the project, on OULAD (Open University Learning Analytics Dataset) and in the pilot.
- At day 27 it flags 28.8% of 27,535 enrolments.
**Visual:** a three-part rule diagram (structure): three boxes joined by "or", the inactivity box in the accent colour
as the part the data forced.
**Speaker notes:** The second change is the heart of our design. Milestone 1 imagined a rule of two missed or late
tasks by week 4. The data said no: two tasks fall due by day 27 in only 1 of 22 runs, and any task by day 13 in only
1. A task-only rule would stay silent in most runs exactly when a list is needed. So the final early-sign rule flags a
student with a tutor-marked or computer-marked task due but not submitted, a tutor-marked assignment submitted late,
or no click at all in the last seven days. It is one rule, on OULAD and later in the pilot, so the pilot's KPI and the
model's benchmark count the same students. At day 27 it flags 28.8% of enrolments. Now we turn from questions to data.
**Sources:** [M5 §2.1], [M5 App III Table A.8], [M5 §6.1]

## Slide 19 – Data Requirements Before the Search   [4 Data requirements]   [Line: main]
**Lead:** We wrote what the questions need in the university's own terms before looking at any dataset, so that data fit questions and not the reverse.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; D1 contact, D2
support time.
| AQ | Outcome or measure | Required variables | Time and grain | Decision point |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Pass, fail or withdrawal; first missed week | Identifiers, enrolment dates, final result, dated withdrawal, task dates | Four semesters; week | D2, semester end |
| AQ2 | Non-completion with and without each sign | AQ1 variables, dated activity, missed and late tasks | Weeks 1–4; day | D2; reasons in D1 |
| AQ3 | Non-completion by semester end | Timestamped activity and submissions, background at enrolment | Weeks 2 and 4; runs in time order | D1, weeks 3 and 5 |
| AQ4 | Recall within capacity; outcome after contact | AQ3 output, capacity (assumed), contact record (to create) | Each review point | D1 |
- Shared: unit = one student's enrolment in one course and semester; population = enrolled after add-drop; every event
  timestamped, each list using data up to one week before it.
- Six must-have gates: dated outcome (G1); dated tasks (G2a) and activity (G2b); at least three time-ordered runs
  (G3); open licence with provenance (G4); persistent anonymised identifier (G5). Contact record declared a gap
  before the search.
**Visual:** table (lookup) – the AQ–Data Requirement Matrix – with the six gates as a row of badges beneath it.
**Speaker notes:** Questions in hand, we resisted the usual temptation to start from a convenient dataset. We wrote
what each question needs in the university's own terms first. Every question uses one student's enrolment in one
course and semester, the population enrolled after add-drop, and a final result with a dated withdrawal. Because each
list may use only data recorded up to its cut-off, every event needs a timestamp. From this matrix came six must-have
gates: a dated outcome, dated tasks, dated activity, at least three runs in time order, an open licence with
provenance, and an identifier that persists. We also declared, before searching, that no dataset would have a contact
record. Then we searched.
**Sources:** [M5 §4 Table 4.1], [M5 App IV]

## Slide 20 – Seven Candidates, One Fit   [4 Data requirements]   [Line: main]
**Lead:** Of seven candidate datasets, only OULAD passes every gate, and it was chosen for fit with the questions, not for ease of access.
**On the slide:** Key: G1 dated outcome; G2a dated tasks; G2b dated activity; G3 at least three time-ordered runs; G4
open licence; OULAD = Open University Learning Analytics Dataset; UCI = University of California, Irvine repository.
| Candidate | Score (of 20) | Gates failed | Decision |
| :---- | :---- | :---- | :---- |
| OULAD | 12 | None | Selected, conditional on three facts |
| UCI 697 | 10 | G1, G2a, G2b | Rejected |
| UCI 856 | 7 | G1, G2a, G2b, G3 | Rejected |
| UCI 320 | 6 | G1, G2a, G2b, G3 | Rejected |
| XuetangX | 8 | G1, G2a, G4 | Rejected |
| HarvardX | 8 | G1, G2a, G2b, G3, G4 | Rejected |
| xAPI-Edu-Data | 4 | G1, G2a, G2b, G3 | Rejected |
- Gates decide, scores inform: each candidate scored 0–2 on the brief's ten criteria.
**Visual:** horizontal bar chart (comparison) of the scores, OULAD in the accent colour, the rest grey, with the failed
gates written at the end of each bar.
**Speaker notes:** In Milestone 2 we screened seven candidates from data repositories, including three from the
University of California, Irvine repository, scoring each from 0 to 2 on the brief's ten criteria. But gates decided
first. OULAD scores only 12 of 20, because we counted only what its documentation states, yet it is the only one that
records a dated withdrawal, dated submissions and daily clicks. Every other candidate fails at least the outcome gate.
Some scored higher on quality or documentation, but none could show when a student stopped taking part. We made the
choice conditional on three facts the files had to confirm; the check confirmed two and met the history gate for five
of seven modules. Where exactly does our copy come from?
**Sources:** [M5 §4.1 Table 4.2], [M5 App IV Table A.10]

## Slide 21 – Provenance and Licence   [4 Data requirements]   [Line: detail]
**Lead:** Our copy of OULAD is a pinned public release under an open licence, so anyone can rebuild every number.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; SHA-256 = a checksum that proves a file is
unchanged.
- Authors: J. Kuzilek, M. Hlosta and Z. Zdrahal, Knowledge Media Institute, The Open University.
- Copy: figshare deposit, doi:10.6084/m9.figshare.5081998.v1, version 1, accessed 6 November 2026.
- Integrity: size and SHA-256 checksum of the archive and of each of the seven tables pinned; all matched.
- Licence: Creative Commons Attribution 4.0 (CC BY 4.0), use with attribution.
- Privacy: anonymised by the publisher (k-anonymity, k = 5); we make no attempt at re-identification and never link it
  to another source.
**Visual:** none; a provenance card in the form of a short record.
**Speaker notes:** Having chosen OULAD, we made sure anyone could get exactly the same data. Our copy is version 1 of
the figshare deposit by Kuzilek, Hlosta and Zdrahal, accessed on 6 November 2026. We pinned the checksum of the
archive and of each of its seven tables, and all matched. The licence is Creative Commons Attribution 4.0, so the data
and our prepared views can be shared with attribution. The publisher anonymised it so that every combination of
identifying attributes is shared by at least five students. We never try to re-identify anyone and never link OULAD
to another source, which Vietnam's personal data law also forbids for de-identified data. So what is inside OULAD?
**Sources:** [M5 §4.1], [M5 App IV Table A.11], [M5 App VI]

## Slide 22 – OULAD at a Glance   [5 Dataset description]   [Line: main]
**Lead:** OULAD records 32,593 enrolments in 22 runs of seven UK distance-learning modules, with a dated result, dated tasks and daily clicks for each.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; run = one offering of a module, named by
year and start month (B = February, J = October).
- 22 runs of seven modules, coded AAA to GGG, 2013 and 2014; 32,593 enrolments of 28,785 students.
- 2013: 9 runs, six modules, 13,529 enrolments · 2014: 13 runs, all seven modules, 19,064 enrolments.
- Final results: Pass 12,361 · Withdrawn 10,156 · Fail 7,052 · Distinction 3,024; completion = Pass or Distinction.
- Seven tables keyed by module, run and student; every link between them holds; the click table holds 10,655,280
  rows.
- A task other than the exam falls due by day 27 in only 16 of the 22 runs.
**Visual:** horizontal stacked bar (part-to-whole) of the four final results, the two non-completion outcomes (Fail,
Withdrawn) in the accent colour and the completion outcomes in grey.
**Speaker notes:** So what does OULAD hold? It covers 22 runs of seven Open University modules, coded AAA to GGG, in
2013 and 2014: 32,593 enrolments of 28,785 students. A run is one offering of a module, named by its year and start
month, B for February and J for October. Every enrolment has a final result: 12,361 passes, 10,156 withdrawals, 7,052
fails and 3,024 distinctions; completion means pass or distinction. The 2013 runs cover six modules, the 2014 runs all
seven. Seven tables link cleanly by module, run and student, including more than ten million daily click rows. One
fact matters later: a task other than the exam falls due by day 27 in only 16 of the 22 runs. Which variables do we
use?
**Sources:** [M5 §5], [M5 App V Table A.12]

## Slide 23 – Key Variables   [5 Dataset description]   [Line: detail]
**Lead:** Seven groups of variables carry every question, and two of them serve only the fairness checks.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; TMA = tutor-marked
assignment; CMA = computer-marked assessment.
| Variable | Meaning | Used by |
| :---- | :---- | :---- |
| final_result | Pass, Distinction, Fail or Withdrawn | Target of all four |
| code_module, code_presentation | Module (AAA–GGG) and run | All four |
| date_registration, date_unregistration | Registration and unregistration day from day 0 | Populations; withdrawal timing |
| assessment_type, date; date_submitted | Kind of task (TMA, CMA, exam), due day, submission day | AQ1–AQ3 |
| sum_click, date | Clicks on one page in one day | AQ2, AQ3 |
| num_of_prev_attempts, studied_credits | Earlier attempts; credits studied | AQ2, AQ3 |
| imd_band, disability | Deprivation band of the home area; declared disability | Group checks only |
- The full data dictionary travels with the Final Project Package.
**Visual:** table (lookup): the short data dictionary; the last row shaded to mark "audit only".
**Speaker notes:** Behind those tables, a short list of variables carries the whole analysis. The final result is
the target of every question. Module and run codes key everything. Registration and unregistration days define who
is enrolled at each cut-off and when a withdrawal happened. Task type, due day and submission day give missed and
late tasks. Daily clicks give activity. Earlier attempts and credits studied adjust the association model and enter
the predictive design. And two sensitive variables, the deprivation band of the student's home area and declared
disability, are used only to check fairness, never to predict. The full dictionary travels with our final package.
Now, how well do these data fit our four questions?
**Sources:** [M5 §5 Table 5.1], [M5 App V]

## Slide 24 – Requirement–Data Fit   [5 Dataset description]   [Line: main]
**Lead:** No question fits OULAD perfectly: three must be narrowed and one lacks its key concept, yet every question keeps a core the data can answer.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; GREEN = data enough;
YELLOW = narrow the question; RED = key concept missing; TMA/CMA = tutor-/computer-marked tasks; OULAD = Open University
Learning Analytics Dataset.
| AQ | Fit | Missing or weak in OULAD | Handling | Action | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | YELLOW | Year of study, delivery mode; exam results in 2 of 7 modules | TMA and CMA only; day-14 rule; both years | Modify | Answered |
| AQ2 | YELLOW | Attendance; several-modules sign in 2013 | Signs up to day 27; several-modules sign on 2014 only | Modify | Answered |
| AQ3 | YELLOW | A task-only rule fires in 1 of 22 runs at day 13 | Rule with inactivity; test on 2014 | Modify | Deferred |
| AQ4 | RED | Contacts, capacity, outcomes after contact | Ranking part only; contact to the pilot | Modify + Defer | Deferred |
**Visual:** table (lookup) – the AQ–Data Fit Matrix – with the fit column as coloured chips (yellow, red) and status in
plain text.
**Speaker notes:** With the variables known, we rated each question against them in Milestone 3. Green would mean the
data are enough; none is. AQ1, AQ2 and AQ3 are yellow: they must be narrowed. AQ1 loses year of study and delivery
mode, and since exam results exist in only two of seven modules, a task means a tutor-marked or computer-marked
assignment. AQ2 loses attendance. AQ3 needs the rule with inactivity, because a task-only rule fires in one of 22 runs
at day 13. AQ4 is red: there is no contact, no capacity and no outcome after contact, so only its ranking survives.
Keep, modify or defer: three modified, one modified and partly deferred, none dropped. What exactly is missing?
**Sources:** [M5 §5.1 Table 5.2], [M5 App V Table A.13]

## Slide 25 – Gaps No Dataset Fills   [5 Dataset description]   [Line: detail]
**Lead:** We never impute a missing value or simulate a missing variable, and three parts of the proposal need the university's own records.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; KPI = key performance indicator; AQ4 =
prescriptive ranking question; TMA = tutor-marked assignment.
| Class of gap | Cases in OULAD | Handling |
| :---- | :---- | :---- |
| Missing value | Deprivation band (1,111 enrolments); registration day (45); TMA score (173) | "Missing" category or indicator; no imputation |
| Recorded absence | No click row; no submission row | Zero counts after joins |
| Missing variable | Year of study, delivery mode, attendance, leave or transfer, contacts, staff capacity | Not imputed or simulated; questions narrowed or part deferred |
| Missing target | None: every enrolment has a final result | Supervised target available |
- Needs the university: the contact part of AQ4; comparisons by year of study, mode or attendance; the contact parts of
  the secondary KPIs.
**Visual:** table (structure): four classes of gap; the "missing variable" row in the accent colour.
**Speaker notes:** The fit ratings point to gaps of four kinds, and we handle each differently. A missing value, like
1,111 enrolments without a deprivation band, keeps its own category; we never impute it. A recorded absence, like no
click on a day, is real information and becomes a zero. A missing variable, like year of study, attendance or any
contact, is something OULAD never collected, and we never simulate it, because invented values would turn assumptions
into apparent evidence. There is no missing target. So three parts of the proposal wait for the university: the
contact part of AQ4, comparisons by year, mode or attendance, and the contact parts of the secondary KPIs. Next, what
the data look like inside.
**Sources:** [M5 §5.1], [M5 App V Table A.14]

## Slide 26 – Close Classes, Skewed Activity   [6 Data understanding]   [Line: main]
**Lead:** Completers and non-completers are close in number, so no resampling is needed, while activity is so skewed that counts enter models as logarithms.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; run = one offering of a module.
- Profile on all 10.9 million rows of the seven raw tables; 13 figures recounted independently, all 13 in agreement.
- Outcome balance: 54.7% of the 28,061 enrolments registered at day 14 completed; non-completion 45.3% at day 13 and
  44.2% at day 27; 24.9–58.3% between runs.
- Mix differs by module: withdrawal highest in the CCC runs (43–46%); GGG has the fewest withdrawals but the most
  failures.
- Activity: median 602 clicks per enrolment; 3,365 enrolments without any click; one record reaches 6,977 clicks in a
  day.
- Decision: no resampling; counts as logarithms; no value removed.
**Visual:** a histogram of clicks per enrolment on a log scale (distribution), with the median marked in the accent
colour and the zero-click bar labelled.
**Speaker notes:** Before answering anything, we needed to know which features of the data could change a conclusion.
In Milestone 3 we profiled all 10.9 million rows, not a sample, and recounted thirteen figures with separate code; all
thirteen agreed. Two shapes matter. First, balance: 54.7% of the day-14 population completed, so the two classes are
close in size and no resampling is needed, although runs range from 24.9 to 58.3 percent non-completion and modules
lose students in different ways. Second, skew: the median enrolment has 602 clicks, 3,365 have none, and one record
reaches 6,977 in a day. So counts enter models as logarithms, and we remove nothing. Every later number refers to a
defined population, shown next.
**Sources:** [M5 §6], [M5 App VI]

## Slide 27 – Populations Behind Every Number   [6 Data understanding]   [Line: detail]
**Lead:** Each later number refers to one of seven populations, set by year and by the day a student is counted as enrolled.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; day 13 and day 27 =
cut-offs of the week-3 and week-5 lists.
| Population | Enrolments | Non-completers | Used by |
| :---- | :---- | :---- | :---- |
| All 2013 enrolments (9 runs) | 13,529 | 6,959 (51.4%) | AQ1, second denominator |
| 2013, registered at day 14 | 12,076 | 5,515 (45.7%) | AQ1, primary denominator |
| 2013, registered at day 13 | 12,080 | 5,519 | AQ3 development, day 13 |
| 2013, registered at day 27 | 11,811 | 5,245 (44.4%) | AQ2; AQ3 development, day 27 |
| 2013, day 27, 7 runs with a task due | 9,960 | – | AQ2 task signs |
| 2014, registered at day 14 | 15,985 | 7,185 (44.9%) | AQ1, primary denominator |
| 2014 test (13 runs), day 13 and day 27 | 15,989 and 15,724 | day 27: 6,911 (44.0%) | AQ2 replication; AQ3 and AQ4 test |
**Visual:** table (lookup); the two primary AQ1 rows and the AQ3/AQ4 test row in the accent colour.
**Speaker notes:** We just said every number has a population; here they are, so you can check any figure later.
Model development uses the nine runs of 2013, and the thirteen runs of 2014 are kept for a single test, while the
descriptive and diagnostic questions describe both years. Each year has a primary population, students still
registered at day 14, and the week-5 list population at day 27. In 2013, 45.7% of the 12,076 enrolments registered at
day 14 did not complete; in 2014, 44.9% of 15,985. Over all enrolments of 2013 the rate is higher, 51.4%, because many
who left early were withdrawals. Keep this table in mind; it explains a surprise later. Now, the quality problems.
**Sources:** [M5 §6 Table 6.1]

## Slide 28 – Three Issues That Change the Method   [6 Data understanding]   [Line: main]
**Lead:** Of nineteen logged quality issues, three are severe enough to change the method itself.
**On the slide:** Key: TMA = tutor-marked assignment; CMA = computer-marked assessment; severity High = ignoring it
would change a rate, the target or a feature.
- Nineteen issues logged, each rated High, Medium or Low against the questions, each with a decision.
- High 1 – Exam results missing: 18 of 24 exams have no result rows → a task means a TMA or CMA only.
- High 2 – Few tasks due early: no 2013 run has a task due by day 13, and 7 of 9 have one by day 27 → the early-sign
  rule needs an activity part.
- High 3 – Narrow population: seven UK modules of 2013–2014 → scope stated; comparisons within module.
- Other issues: duplicate click rows, activity after unregistration, missing values, outliers – handled with flags,
  truncation or "Missing" groups; nothing deleted or imputed.
**Visual:** three issue cards (structure), each with "issue → decision"; the activity-part card in the accent colour,
because it returns at the climax.
**Speaker notes:** The profile turned into a log of nineteen quality issues, each rated by whether ignoring it would
change a rate, the target or a feature. Three are High. Exam results are missing for 18 of 24 exams, so a task means a
tutor-marked or computer-marked assignment only. No 2013 run has any task due by day 13, and only 7 of 9 have one by
day 27, which is the data reason behind the activity part of the early-sign rule. And the population is narrow, seven
UK modules from two years, so we state the scope and compare within module. The others, from duplicate click rows to
missing bands, are handled with flags or a "Missing" group, never by deleting or imputing. Two Medium issues have a
known size.
**Sources:** [M5 §6.1 Table 6.2], [M5 App VI Table A.15]

## Slide 29 – Two Issues with a Known Effect   [6 Data understanding]   [Line: detail]
**Lead:** Two medium issues would move a measure by a known amount, so each becomes a sensitivity run instead of a silent choice.
**On the slide:** Key: TMA = tutor-marked assignment; CMA = computer-marked assessment; OULAD = Open University
Learning Analytics Dataset.
- Late CMAs: counting them would raise the share the early-sign rule flags at day 27 from 28.8% to 41.2% → the rule
  uses TMA lateness; late CMAs become a sensitivity run.
- Duplicate click rows: 7.39% of click rows; removing them would drop 3.19% of all clicks → rows kept, clicks summed by
  day, and a de-duplicated twin of each click feature tests the choice.
**Visual:** two before/after pairs (comparison): 28.8% → 41.2% as two bars, and the 3.19% of clicks that de-duplication
would remove as the accent-coloured end of a single bar.
**Speaker notes:** Beyond the three severe issues, two medium ones could move a result by a known amount, and we made
each visible rather than deciding quietly. If late computer-marked assessments counted as a sign, the rule would flag
41.2% of enrolments at day 27 instead of 28.8%, and what a late computer-marked task meant in those years is
undocumented. So the rule counts lateness only for tutor-marked assignments, and the wider version is a sensitivity
run. Duplicate click rows make up 7.39% of rows; dropping them would remove 3.19% of clicks. We keep them, sum by day,
and test a de-duplicated twin of each feature. Next, time and how far OULAD represents our setting.
**Sources:** [M5 §6.1]

## Slide 30 – Time Coverage and Representativeness   [6 Data understanding]   [Line: main]
**Lead:** The only honest test of a model on a later run is to train on 2013 and test on 2014, and the narrow, high-failure sample means every result needs a re-check at the university.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; run = one offering of a module.
- Weekly clicks peak in week 3: the cut-offs at day 13 and day 27 fall in the weeks of highest activity.
- Each module has at most one earlier run of the same start month → train on 2013, test on 2014.
- Module CCC and the February runs of EEE and GGG appear only in 2014 → the test also covers transfer to unseen runs.
- OULAD modules were chosen partly because many students failed them → rates are likely higher than a typical
  program's; groups are compared within module.
**Visual:** a module × year grid (structure): seven modules by 2013/2014 with filled cells for runs that exist;
2014-only cells outlined in the accent colour.
**Speaker notes:** Quality is one question; coverage in time is another. Weekly clicks peak in week 3, so our cut-offs
at day 13 and day 27 fall in the busiest weeks, which is good for early signals. But each module has at most one
earlier run of the same start month, so the only way to test a model on a later run, as the university would use it,
is to train on 2013 and test on 2014. Look at the grid: module CCC and two February runs exist only in 2014, so the
test also checks transfer. And OULAD's modules were partly chosen because many students failed them, so its rates
probably exceed a typical program's. Results describe OULAD; the university must recount. What about sensitive data?
**Sources:** [M5 §6.2], [M5 App VI]

## Slide 31 – Sensitive Fields and Privacy   [6 Data understanding]   [Line: detail]
**Lead:** We keep six sensitive attributes out of every predictor set except one, because bias cannot be audited without knowing group membership.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset.
| Attribute | Role |
| :---- | :---- |
| Gender, age band, region | Audit only |
| Declared disability (3,164 enrolments) | Audit only; fairness group |
| Deprivation band (1,111 missing) | Audit only; fairness group; "Missing" its own group |
| Highest education | Predictor, also audited |
- Why keep them: bias can arise through proxies, and a fairness study on OULAD reproduced a disparity of five to six
  percentage points in favour of male students.
- Privacy: under Vietnam's Personal Data Protection Law, re-identifying de-identified data is prohibited, so OULAD is
  never linked to another source.
**Visual:** table (lookup); the "audit only" label in grey, "predictor" in the accent colour.
**Speaker notes:** Coverage leads to fairness. OULAD holds six sensitive attributes: gender, age band, disability,
deprivation band, region and highest education. Five serve only the fairness audit, and highest education is a
predictor that is also audited. Why not delete them? Because leaving them out does not make a model blind: activity or
credits can carry the same information, and bias cannot be audited without knowing who belongs to which group. The
need is concrete: a published study on OULAD reproduced a disparity of five to six points in favour of male students.
On privacy, Vietnam's law prohibits re-identifying de-identified data, so OULAD is never linked to anything. Now the
preparation.
**Sources:** [M5 §6.2], [M5 App VI Table A.16]

## Slide 32 – Preparation Decisions   [7 Data preparation]   [Line: main]
**Lead:** Every preparation decision was fixed with a check that fails if it is not carried out, under three rules: delete nothing, date everything, learn only from training runs.
**On the slide:**
| Need | Decision |
| :---- | :---- |
| Population | Flags for days 13, 14 and 27; views hold those enrolled at the cut-off |
| Missing values | "Missing" category or indicator; no imputation |
| Duplicates, keys, joins | Every row kept; clicks summed by day; left joins from the enrolments |
| Invalid values, outliers | Labels corrected; banked results untimed; every value kept |
| Activity after withdrawal | Truncated at the unregistration day |
| Derived features | Tutor- and computer-marked tasks; early-sign rule; activity against the run median |
| Time, encoding | Cut-offs at days 13 and 27; transforms learned on training rows |
| Sensitive attributes, split | Audit columns outside the predictors; train 2013, test 2014 |
- 22 validation checks under 15 identifiers; ten scripted steps, no manual step.
**Visual:** table (lookup) – the Preparation Decision Matrix – with the three governing rules as a banner above it.
**Speaker notes:** Knowing the data's flaws, we built the pipeline that every analysis reads. Each issue received a
decision before any record changed, and each decision has a validation check that fails if it is not carried out.
Three rules govern the whole thing. Nothing recorded is deleted or imputed. Every feature uses only events dated on or
before its cut-off. And every learned parameter comes from the training runs alone. The matrix shows how each need
was met: populations by flags, missing values as their own category, all rows kept and clicks summed by day, activity
after a withdrawal cut off. Ten scripted steps, no manual edit, 22 checks under fifteen names. What did the pipeline derive?
**Sources:** [M5 §7 Table 7.1], [M5 App VII Table A.17]

## Slide 33 – Derived Variables and Predictors   [7 Data preparation]   [Line: detail]
**Lead:** The pipeline derives the early signs and a compact predictor set of 19 usable predictors, all dated at the cut-off.
**On the slide:** Key: TMA = tutor-marked assignment; CMA = computer-marked assessment; c = cut-off day (13 or 27).
- Derived: clicks before day 0; clicks and active days from day 0 to c; activity against the median of the same run;
  no click in the last seven days; missed and late tasks; the early-sign rule.
- A task counts as missed only if it fell due on or after the student's registration day.
- TMA marks have no release day, so they are never used.
- Primary set: 19 usable predictors, 23 parameters once module and start month are coded.
- Encoding: counts as log(1 + count); transforms refitted inside each development fold; module terms deviation-coded,
  so an unseen module receives the average effect.
- Volume: 10,655,280 click rows summed into 1,808,119 enrolment-day records; 98,745 clicks after withdrawal left out.
**Visual:** none; a short list grouped into "signs" and "encoding", the timing rule in the accent colour.
**Speaker notes:** From the raw tables the pipeline derives the variables our questions use. Activity is counted
before the start, up to the cut-off, and against the median of the same run, so a student is compared with their own
cohort. It records a week without clicks, missed tasks and late tasks, and the early-sign rule itself. Two timing
details protect fairness and validity: a late registrant is never charged with tasks set before they joined, and
tutor-marked marks are never used, because we cannot know when a student saw them. The primary set has 19 usable
predictors, 23 parameters after coding. Since these features look backwards from a cut-off, leakage is the next risk.
**Sources:** [M5 §7.1], [M5 App VII Table A.18]

## Slide 34 – Leakage Control   [7 Data preparation]   [Line: main]
**Lead:** Leakage is blocked four ways, and the date-filter check is built so that it can fail.
**On the slide:** Leakage = using information that would not exist at the moment of prediction.
| Form | Control |
| :---- | :---- |
| Target leakage (result, withdrawal day, later activity) | Features only from events dated up to the cut-off |
| Train–test contamination | Medians, scales and levels learned on 2013 only, refitted per fold |
| Student leakage | 1,586 test enrolments at day 27 of students seen in 2013 flagged; kept in the main test, removed in a sensitivity check |
| Temporal leakage | Train on the 9 runs of 2013, test on the 13 runs of 2014 |
- The check can fail: without the date filter, click features change only for the 26,755 (day 13) and 25,663 (day
  27) enrolments that clicked after the cut-off.
**Visual:** table (structure) with a small timeline showing the cut-off as a vertical wall, data to its right greyed out.
**Speaker notes:** Features that look backwards from a cut-off invite one danger: leakage, using information that
would not exist when the list is made. We block it four ways. The final result, the withdrawal day and later activity
never enter a feature. Medians and scales are learned on 2013 alone. Students who appear in both years are flagged:
1,586 test enrolments at day 27, kept in the test as they would be in real use and removed in a sensitivity check. And
the split is by year. Most important, our date-filter check can fail: without the filter, features change exactly for
the enrolments that clicked after the cut-off, and nothing else. The result is one versioned dataset.
**Sources:** [M5 §7.1], [M5 App VII Table A.19]

## Slide 35 – The Final Prepared Dataset   [7 Data preparation]   [Line: detail]
**Lead:** The prepared dataset is versioned, fully checked and rebuilt byte for byte by one command from the public download.
**On the slide:**
- Name: OULAD-N04-prepared-1.0 (OULAD = Open University Learning Analytics Dataset).
- All 22 validation checks pass: 32,593 enrolments and their outcome mix unchanged; six features recomputed from raw by
  separate code differ in none of the 55,604 feature rows.
- Data dictionary: 88 prepared variables, each with source, transformation, role and sensitivity.
- Rebuild: one command from the pinned figshare download; byte-identical output on a rerun.
- Synthetic data only in unit tests, never in a view, a statistic or a finding.
**Visual:** none; four check-marked statements in a vertical list.
**Speaker notes:** All that preparation ends in one named dataset, version 1.0. All 22 validation checks pass. The
32,593 enrolments and their outcomes are unchanged, and six features recomputed from the raw files by separate code
match in all 55,604 feature rows. Every one of the 88 prepared variables is documented with its source, its
transformation, its role and its sensitivity. One command rebuilds the whole thing from the pinned public download,
and running it twice gives byte-identical files. Synthetic records exist only to test code, never in a result. So the
data side of the chain is closed. We now move from data to method: what analysis does each question need?
**Sources:** [M5 §7.2], [M5 App VII Table A.20]

## Slide 36 – From Question to Task   [8 Modeling strategy]   [Line: main]
**Lead:** Each question maps to one technical task, and the purpose of the task fixes how its result may be read.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking.
- AQ1 → aggregation and rate comparison → states what happened.
- AQ2 → association within module run → states an association, never a cause.
- AQ3 → binary classification at day 13 and day 27 → must be judged on unseen runs.
- AQ4 → ranking under a fixed capacity → a decision option, untested.
- Level 1 (compulsory): strategy and evaluation designed in Milestone 4 without training any model; AQ1 and AQ2 then
  run as specified.
**Visual:** a four-row flow (sequence): question → task → "how to read it", with the reading column in the accent
colour.
**Speaker notes:** With clean data, the method follows from each question's purpose. AQ1 is aggregation: rates and
comparisons that state what happened. AQ2 is association within module run; a regression used this way describes how
a sign and an outcome move together and says nothing about cause. AQ3 is binary classification at day 13 and day 27,
and a predictive claim needs evaluation on runs the model has never seen, because explaining the data is not
predicting new cases. AQ4 is ranking under fixed capacity, which can only produce an option to test. We designed all
this in Milestone 4 without training a model, then ran AQ1 and AQ2 exactly as planned. Here is the full selection.
**Sources:** [M5 §8], [M5 App VIII Table A.22]

## Slide 37 – Method Selection   [8 Modeling strategy]   [Line: main]
**Lead:** For each question we chose the simplest method that answers it, with interpretability breaking ties, because decisions about people call for reasons staff can check.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; top-k = the k
highest-ranked students of a run.
| AQ | Baseline | Candidates | Primary proposal | Rationale |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Pooled rate; rate over all enrolments | Grouped rates with 95% intervals | Wilson intervals; cumulative first missed week; Newcombe interval for the year difference | No model needed; the denominator decides the rate |
| AQ2 | Unadjusted rate difference per sign | Logistic regression with run fixed effects; mixed-effects logistic | Fixed-effects logistic, robust errors; average risk differences | Every run observed; 6 modules too few for a random effect; no causal claim |
| AQ3 | Early-sign rule ranked by number of signs; background-only model; random list | Penalised logistic regression; gradient-boosted trees | Penalised logistic on 19 predictors (23 parameters) | Interpretable reasons; about 230 non-completers per parameter |
| AQ4 | Random list; rule-ranked list | Top-k per run; risk tiers | Top-k with the signs behind each name | Capacity fixed; no contact data; staff decide |
- Judged on the course's eight criteria; ties go to the simpler, more interpretable method.
**Visual:** table (lookup) – the Model and Method Selection Matrix – with the primary-proposal column in the accent
colour.
**Speaker notes:** Here is the Method Selection Matrix. Each candidate was judged on the course's eight criteria, from
fit to fairness and actionability, and ties went to the simpler method. AQ1 needs no model: grouped rates with Wilson
intervals and a Newcombe interval for the year difference. AQ2 uses logistic regression with a fixed effect for each
run, because every run of these modules is observed and six modules are too few for a random effect. For AQ3 we
propose penalised logistic regression on 19 predictors, because staff must see reasons and the 2013 runs give about
230 non-completers per parameter. Trees can challenge it. AQ4 takes the top of the AQ3 ranking, with signs beside each
name. Why a ranking at all?
**Sources:** [M5 §8.1 Table 8.1], [M5 App VIII]

## Slide 38 – Why a Ranking, Not a Threshold   [8 Modeling strategy]   [Line: detail]
**Lead:** The early-sign rule flags more students than staff can contact, so the list must be ranked to fit capacity.
**On the slide:**
- The early-sign rule flags 28.8% of enrolments at day 27.
- Capacity: 3 or 5 contacts per 20 students, that is 15% or 25% of a run (scenario values).
- No data record a contact or its outcome → no ranking by expected benefit; the list orders by risk, and a member of
  staff decides.
**Visual:** a single horizontal bar (part-to-whole) of 100 students: 28.8 flagged by the rule against markers at 15
and 25, the overflow in the accent colour.
**Speaker notes:** Why rank instead of simply flagging? Because the rule flags 28.8% of enrolments at day 27, and staff
capacity, in our scenario, is three or five contacts per twenty students, 15 or 25 percent of a run. The rule flags
more students than can be reached, so someone must decide who comes first. A ranking does that. But a ranking by risk
is not a ranking by benefit: since no data record a contact or what happened after it, we cannot say who would gain
most from being contacted. So the list orders by risk, shows its reasons, and a person decides. How would we know if a
list is good? That is the evaluation design.
**Sources:** [M5 §8], [M5 App IX]

## Slide 39 – Evaluation Plan   [9 Evaluation design]   [Line: main]
**Lead:** Each question has a primary metric, a baseline and a success criterion fixed before any code ran.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; S1 = the single
gate for AQ3 (model's list must beat the rule's list); capacity = 5 contacts per 20 students at day 27.
| AQ | Primary metric | Baseline | Validation | Success criterion |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Rates and shares with 95% intervals | Pooled rate; all enrolments; without flagged enrolments | Two independent aggregation paths | Paths agree to the enrolment; every rate with denominator and interval |
| AQ2 | Average risk difference within module run, with 95% interval | Unadjusted difference | 2013; sensitivity runs; replication on 2014 | At least 5 points, interval excluding 0, same direction in at least two-thirds of modules |
| AQ3 | Normalised recall at capacity, pooled | Rule list; background-only model; random list | Leave-one-run-out on 2013; one test on 13 runs of 2014 | Gate S1: beat the rule list, bootstrap interval above 0, sign-flip p below 0.05 |
| AQ4 | Normalised recall at capacity | Random list; rule list | As AQ3, per test run | S1 met; fairness check passed or reviewed; no claim about contact |
**Visual:** table (lookup) – the Evaluation Plan – with the success-criterion column in the accent colour.
**Speaker notes:** A good method needs a fixed way to judge it, and ours was fixed in Milestone 4 before any code ran,
so no threshold could bend to a result. AQ1 succeeds when two independent ways of counting agree to the enrolment and
every rate carries its denominator and interval. AQ2 calls a sign a consistent association at five points or more,
with an interval excluding zero and the same direction in two-thirds of modules; p-values take no part. AQ3 has one
gate, S1: the model's list must beat the rule's list on all thirteen 2014 runs. AQ4 must pass the same gate plus a
fairness check. The metric for lists needs one minute of explanation.
**Sources:** [M5 §9 Table 9.1], [M5 §9.1]

## Slide 40 – Measuring a List: Normalised Recall and Lift   [9 Evaluation design]   [Line: detail]
**Lead:** Normalised recall compares a list with the best list of the same length, because the ceiling differs from run to run.
**On the slide:**
- Recall at capacity = share of a run's non-completers who are on the list.
- Attainable recall = the most a list of length k can reach (below 1 when non-completers outnumber places).
- Normalised recall = recall ÷ attainable recall; 1 means the best list possible.
- Lift = share of non-completers on the list ÷ the run's base rate; 1 means no better than a random list.
- Why: in the 2013 runs a list of 5 per 20 at day 27 can hold between 46% and 100% of a run's non-completers.
- Main operating point: 5 per 20 at day 27; also 3 per 20 and day 13.
**Visual:** worked example (diagram): two runs side by side, each with 20 seats and its non-completers as dots; the
ceiling marked per run to show why raw recall compares unlike things.
**Speaker notes:** Why not just recall? Because the ceiling moves. In a run where more students fail than the list has
places, even a perfect list cannot reach them all. In the 2013 runs, a list of five per twenty at day 27 could hold
anywhere from 46% to all of a run's non-completers. So we divide recall by what a list of that length could possibly
reach: one means the best list possible. Lift is the share of non-completers on the list over the run's base rate,
where one means no better than random. Milestone 1's precision target is gone for the same reason: at a 45% base rate
precision says little. Next, how the single test is protected.
**Sources:** [M5 §9], [M5 App IX], [M5 App III Table A.8]

## Slide 41 – Validation and the Single Gate   [9 Evaluation design]   [Line: detail]
**Lead:** Development happens only inside 2013, and the 2014 runs are opened once, for one verdict.
**On the slide:** Key: S1 = the single gate for the predictive question; S3 = the calibration condition; the rule =
the early-sign rule.
- Development: leave-one-run-out folds on the 9 runs of 2013; every learned step refitted inside each fold.
- A challenger replaces the primary model only with a gain of at least 0.03 in pooled normalised recall (about 89 more
  non-completers listed) and a gain in 7 of 9 folds, fixed before any fold result.
- Test: the frozen model scored once on all 13 runs of 2014 (15,724 enrolments at day 27); 9 paired runs (10,801)
  and 4 unpaired runs (4,923) also reported apart.
- Gate S1: pooled normalised recall above the rule's, with a paired two-level bootstrap interval above 0 and a one-sided
  sign-flip test p below 0.05.
- S3: probabilities shown only if calibration-in-the-large lies between −0.2 and 0.2 and the slope between 0.8 and
  1.2; otherwise ranks and reasons only.
**Visual:** a split diagram (structure): 2013 folds on the left, a locked 2014 box on the right with "opened once".
**Speaker notes:** With the metric defined, the gate itself. All development happens inside 2013, one run held out at a
time. A challenger like gradient-boosted trees replaces the simple model only if it gains at least 0.03 in normalised
recall, about 89 more non-completers listed, and wins in seven of nine folds, a margin fixed in advance. Then the
model is frozen and scored once on all thirteen 2014 runs, with paired and unpaired runs also reported apart. To pass,
it must beat the rule with a bootstrap interval above zero and a sign-flip test below 0.05. Probabilities appear only
if calibration holds. A good list must also be fair.
**Sources:** [M5 §9.1], [M5 App IX Table A.23]

## Slide 42 – Fairness and Interpretability   [9 Evaluation design]   [Line: main]
**Lead:** A list is checked for equal recall across groups, and a gap triggers human review, not an automatic verdict.
**On the slide:** Key: FR1 = the fairness review rule; recall at capacity = share of a group's non-completers who make
the list.
- One criterion: equal recall at capacity across groups.
- FR1: flag a group for human review when its recall is more than 10 points below the other students' and the
  Holm-adjusted one-sided interval of the gap lies below 0.
- Confirmatory groups (test enrolments at day 27): declared disability 1,488; most deprived band 1,486; missing band 610.
  Aged 55 or over (118): too few, reported as "insufficient data, not cleared".
- No flag means no evidence of a gap at that group's precision, not that the list is fair.
- Interpretability: each name's reasons come from the same model that ranks it; no coefficient read as a cause; model
  card and datasheet.
**Visual:** a simple illustrative bar pair (comparison) "group recall vs others' recall" with the 10-point band drawn
as a grey zone; explicitly labelled as a schematic, not a result.
**Speaker notes:** A list can be accurate overall and still miss one group, so the design audits fairness with one
criterion: equal recall at capacity. The main harm of a list is missing a student who struggles, so a struggling
student should have the same chance of being listed whatever their group. Rule FR1 flags a group for human review when
its recall falls more than ten points below others' and the adjusted interval agrees. The groups are declared
disability, the most deprived band and the missing band; students over 55 are too few to clear. A flag asks for
judgement, not rejection. Reasons shown to staff come from the ranking model itself. So, did we run this?
**Sources:** [M5 §9.2], [M5 App IX Table A.24]

## Slide 43 – Level 2 Was Not Run   [10 Experimental status]   [Line: main]
**Lead:** We completed the compulsory Level 1 design and chose not to run the optional Level 2 prototype, to keep the 2014 runs for one complete, untouched test.
**On the slide:** Key: Level 1 = modeling strategy and evaluation design (compulsory); Level 2 = optional prototype
run; AQ3 predictive, AQ4 prescriptive ranking; AQ1 descriptive, AQ2 diagnostic.
- Level 1: complete.
- Level 2 for AQ3 and AQ4: specified in full in Milestone 4, not run → no model metric, chart or confusion matrix
  exists.
- Why: Level 2 is optional, and the 13 runs of 2014 are the only independent test; a partial early run would spend it.
- AQ1 and AQ2 are descriptive and diagnostic analyses, not the prototype: they train no predictive model and change
  nothing in the AQ3 design fixed on 2013.
**Visual:** none; a two-state status bar: "Level 1 – done" in the accent colour, "Level 2 – specified, not run" in grey.
**Speaker notes:** So, did we run the predictive test? No, and this was a deliberate choice of scope. Level 1, the
compulsory part, is complete: the strategy and the evaluation design you just saw. The optional Level 2 prototype for
AQ3 and AQ4 is specified in full, and it has not been run, so we have no model metric of any kind. The reason is that
the thirteen 2014 runs are our only independent test, and they can be used once. Running part of the protocol early
would spend that test. AQ1 and AQ2 are a different matter: they train no predictive model, so answering them changed
nothing in the AQ3 design. Here is what the prototype would compare.
**Sources:** [M5 §10], [M5 App X]

## Slide 44 – What the Specified Prototype Would Compare   [10 Experimental status]   [Line: detail]
**Lead:** The protocol fixes three baselines and four candidate configurations in advance, leaving no modeling choice to whoever runs it.
**On the slide:** Key: B = baseline; M = model configuration; D1 = whom to contact; primary set = 19 predictors; extended set = primary plus
10 further predictors.
| ID | Role | Method | Predictors |
| :---- | :---- | :---- | :---- |
| B1 | Baseline | Random list | – |
| B2 | Baseline | Early-sign rule, ranked by number of signs | Rule columns |
| B3 | Baseline | Background-only logistic model | Module, start month, attempts, credits, education, registration lead |
| M1 | Primary | Penalised logistic regression | Primary set |
| M2 | Challenger | Penalised logistic regression | Extended set |
| M3 | Challenger | Gradient-boosted trees | Primary set |
| M4 | Challenger | Gradient-boosted trees | Extended set |
- Eight steps, two freezes, one logged test; unfavourable results reported as they come.
**Visual:** table (lookup); B2 in the accent colour, because it is the benchmark D1 needs either way.
**Speaker notes:** For completeness, this is what the unrun prototype would compare. Three baselines: a random list,
the early-sign rule ranked by its number of signs, and a model on background variables only. Then the primary model,
penalised logistic regression on the primary set, and three challengers mixing trees and an extended set of
predictors. Every choice is fixed, so the prototype can confirm or refute Level 1 but not reshape it. Notice baseline
B2, the rule's own list: even if no model wins, measuring B2 tells the contact decision how good the simple rule is.
The protocol has eight steps, two freezes and one logged test. Now to what we did run: the findings.
**Sources:** [M5 §10], [M5 App X Table A.25]

## Slide 45 – How to Read Each Answer   [11 Findings]   [Line: detail]
**Lead:** The same number means different things at different analytics levels, so every finding carries its level, interval, population and confidence.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking.
| AQ | States | Does not state |
| :---- | :---- | :---- |
| AQ1 | Outcome shares and the week of the first missed task, with denominator and 95% interval | Why rates differ; any rate for the university |
| AQ2 | Which signs go with later non-completion within module runs, by how many points | That a sign causes non-completion |
| AQ3 | The expected output and the gate | Any model metric |
| AQ4 | The expected list and its conditions | Whom contact helps |
- Confidence High: two independent computations verify the counts on the stated population. Moderate: direction holds
  under checks, but observational or with a known weakness. Not applicable: no result yet.
**Visual:** table (structure), the "does not state" column in the accent colour.
**Speaker notes:** Before the numbers, a reading guide, because a number means different things at different levels.
AQ1 states what happened on a population, with its interval; it does not say why. AQ2 states associations within
module runs; it never says a sign causes non-completion. AQ3 and AQ4 state only their expected outputs, no metric.
Confidence follows the same logic. High means two independent computations agree on the stated population, which
says nothing about the university. Moderate means the direction holds under checks but rests on observational data or
a known weakness. And not applicable means no result exists yet. With that guide, the first answer: how many students
did not complete?
**Sources:** [M5 §11], [M5 App XI Table A.26]

## Slide 46 – Nearly Half Did Not Complete   [11 Findings]   [Line: main]
**Lead:** Of the 28,061 enrolments still registered at day 14, 45.3% did not complete, and the two years lie close together.
**On the slide:** Key: AQ1 = the descriptive question on completion and timing; day 14 = end of the add-drop period on
OULAD (Open University Learning Analytics Dataset); intervals are 95% Wilson intervals.
- 22 runs: 45.3% (44.7–45.8), 12,700 of 28,061 – 25.0% failed, 20.2% withdrew.
- 2013: 45.7% (44.8–46.6) of 12,076 · 2014: 44.9% (44.2–45.7) of 15,985.
- Success criterion met: prepared views and raw tables agree in all 176 outcome cells; the first missed week agrees for
  all 32,593 enrolments.
- Confidence: high for OULAD 2013–2014; validity for the university's courses open.
**Visual:** one large number (single important number): 45.3%, with a thin stacked bar beneath it split into failed
(25.0%) and withdrew (20.2%), both in the accent colour, completers in grey.
**Speaker notes:** Here is the first answer. Of the 28,061 enrolments still registered at day 14, 45.3% did not
complete: a quarter failed and a fifth withdrew. The two years are almost the same, 45.7% in 2013 and 44.9% in 2014.
We trust these counts because two independent ways of counting, from the prepared views and straight from the raw
tables, agree in all 176 outcome cells, and the first missed week agrees for every one of the 32,593 enrolments. So
confidence is high for OULAD. It says nothing yet about the university, whose own rate must be recounted. But a
pooled rate hides how different the runs are.
**Sources:** [M5 §11.2], [M5 App XII Table A.29]

## Slide 47 – Runs and Modules Differ Widely   [11 Findings]   [Line: main]
**Lead:** Non-completion ranges from a quarter to well over half between runs, and February runs lose more students than October runs in both years.
**On the slide:** Key: AQ1 = descriptive question; run = one offering of a module, named by year and start month (B =
February, J = October); population = enrolments registered at day 14; 95% Wilson intervals.
- Runs: from 24.9% (AAA 2013J) to 58.3% (CCC 2014B).
- Modules over 22 runs: lowest AAA, 26.3%; highest CCC, 54.3% (ran only in 2014).
- Start month: February 51.6% vs October 42.4% in 2013; 49.6% vs 41.6% in 2014.
- How students leave differs: in GGG 2013, 4.3% withdrew and 31.7% failed; in CCC, 33.1% withdrew and 21.3% failed.
**Visual:** dot-and-interval chart (comparison) of non-completion per module, 2013 and 2014 side by side, with a
dashed line at the pooled 45.3%; based on Figure 11.1 of the report. Grey dots, the two extremes labelled in the
accent colour.
**Speaker notes:** That 45.3% is an average over very different courses. Runs range from 24.9% non-completion in AAA's
October 2013 run to 58.3% in CCC's February 2014 run. Over both years, module AAA has the lowest rate, 26.3%, and CCC the
highest, 54.3%. February runs lose more students than October runs in both years. And students leave differently: in GGG most
non-completers stay and fail, while in CCC 33.1% withdraw. A list aimed at students who stop taking part would meet
different kinds of non-completion in different modules. For the program manager, this is a hypothesis about where
support time would go first, to be checked on the university's records. But there is a subtler trap in these rates.
**Sources:** [M5 §11.2], [M5 App XII Table A.30], [M5 §11.2 Figure 11.1]

## Slide 48 – The Denominator Decides   [11 Findings]   [Line: main]
**Lead:** Changing only who is counted moves a run's rate by up to 13.6 points and even reverses the year-on-year comparison.
**On the slide:** Key: day 14 = registered at the end of the add-drop period; "all" = every enrolment, including those
who left before day 14; KPI = key performance indicator (here the completion rate); differences are 2014 minus 2013, in percentage points, 95% Newcombe intervals.
- Same students, two denominators: BBB 2014J – 36.2% of 1,791 at day 14, 49.7% of all 2,292 → 13.6 points apart.
- Year comparison, all enrolments: +2.3 (1.2 to 3.4) – "non-completion rose".
- Year comparison, day 14: −0.7 (−1.9 to 0.5); in the six modules run in both years −3.5 (−4.8 to −2.3).
- Why: 16.2% of 2014 enrolments against 10.7% of 2013 were not registered at day 14.
**Visual:** slopegraph (two-point comparison): 2013 to 2014 under each denominator, the "all enrolments" line rising in
grey and the "day 14" line falling in the accent colour.
**Speaker notes:** Here is the trap, and it is our first surprise. Take BBB's October 2014 run. Counting students
registered at day 14, 36.2% did not complete; counting everyone who ever enrolled, 49.7%. Same students, 13.6 points
apart. Now the year comparison. Over all enrolments, non-completion rose by 2.3 points in 2014. Over students
registered at day 14, it fell slightly, and in the six modules that ran in both years it fell by 3.5 points. The
reason: more 2014 students left before day 14, where the KPI does not count them. So a completion figure without its
add-drop rule can tell the opposite story. That is why our KPI fixes the rule. Next: when do students start to slip?
**Sources:** [M5 §11.2], [M5 App XII Table A.32]

## Slide 49 – Missed Tasks Come Too Late   [11 Findings]   [Line: main]
**Lead:** Most non-completers miss a task at some point, but fewer than one in five has missed one by week 4, when the list is made.
**On the slide:** Key: AQ1 = descriptive question; missed task = a tutor-marked assignment (TMA) or computer-marked
assessment (CMA) that fell due with no submission; non-completer = Fail or Withdrawn; population = registered at day 14.
| | 2013 | 2014 |
| :---- | :---- | :---- |
| Non-completers who missed a task during the run | 78.1% | 72.7% |
| Non-completers who missed a task by week 4 | 19.6% | 14.7% |
| Completers who missed a task by week 4 | under 1% | under 1% |
| Median week of the first missed task, non-completers | 9 | 9 |
- Six of 22 runs had no task due by day 27 at all.
**Visual:** cumulative line chart (trend over weeks): share of non-completers with a first missed task by week, 2013
and 2014; week 4 marked with a vertical accent line labelled "list made here: 19.6% / 14.7%"; the completers' line in
grey near zero.
**Speaker notes:** Now the question that turned our design. When do non-completers first miss a task? Over the whole
run, most do: 78.1% in 2013 and 72.7% in 2014, against about one in five completers. Missing a task is a sharp
separator. But look at the timing. By the end of week 4, when the week-5 list is drawn, only 19.6% of 2013
non-completers and 14.7% of 2014 non-completers had missed one. Their median first missed week is week 9. And in six of
the 22 runs no task was even due by day 27. So a list built on missed tasks alone would arrive too late for most of
the students it should reach. Does anything else show earlier?
**Sources:** [M5 §11.2], [M5 App XII Table A.31]

## Slide 50 – Non-completion by Group of Students   [11 Findings]   [Line: detail]
**Lead:** Non-completion is higher for students with a declared disability and rises with deprivation, which is why these groups anchor the fairness audit.
**On the slide:** Key: deprivation band = Index of Multiple Deprivation band of the student's home area (0–10% = most
deprived); population = registered at day 14; 95% Wilson intervals; described without adjustment.
| Group | 2013 | 2014 |
| :---- | :---- | :---- |
| Declared disability | 55.0% of 1,157 | 54.9% of 1,519 |
| No declared disability | 44.7% | 43.9% |
| Most deprived band (0–10%) | 61.2% of 1,196 | 53.8% of 1,512 |
| Least deprived band (90–100%) | 35.2% of 969 | 36.0% of 1,299 |
**Visual:** paired horizontal bars (comparison) per group, 2013 and 2014; the disability and most-deprived bars in the
accent colour.
**Speaker notes:** Before moving to the signs, one more descriptive pattern. Students with a declared disability did
not complete in 55.0% of enrolments in 2013 and 54.9% in 2014, against 44.7% and 43.9% of other students. Non-completion
falls steadily from the most deprived home areas to the least deprived, from 61.2% to 35.2% in 2013. These are
descriptions, not adjusted comparisons, and they explain nothing about why. But they tell us where a list could fail
students most, which is why disability and the deprivation bands are the groups the fairness audit checks. Now,
which early signs go with non-completion?
**Sources:** [M5 App XII]

## Slide 51 – Five Early Signs, Two Years   [11 Findings]   [Line: main]
**Lead:** All five signs recorded by week 4 go with later non-completion within module in both years, and a missed task goes with 40.8 and 39.3 more percentage points.
**On the slide:** Key: AQ2 = the diagnostic question; risk difference = extra percentage points of later
non-completion with the sign than without it, mutually adjusted, within module run; TMA = tutor-marked assignment.
| Sign at day 27 | 2013 | 2014 |
| :---- | :---- | :---- |
| Task due, not submitted | 40.8 (37.7–43.9) | 39.3 (36.4–42.1) |
| TMA submitted late | 20.2 | 20.3 |
| No click in the last seven days | 14.5 | 15.8 |
| Clicks below the run's median | 13.4 | 14.6 |
| No click before the start | 10.6 | 8.7 |
- Populations: 11,811 enrolments in 2013 (44.4% non-completion), 15,724 in 2014 (44.0%); task signs in runs with a task
  due (9,960 and 12,585).
- No sign moves by more than two points between years. These are associations, not causes.
**Visual:** dot-and-interval chart (comparison), one row per sign, 2013 and 2014 dots side by side, a dashed line at
the 5-point criterion; based on Figure 11.2 of the report. The missed-task row in the accent colour; the inactivity row
outlined, because it returns on slide 54.
**Speaker notes:** Missed tasks come late; what else shows by week 4? We fitted a logistic regression with a fixed
effect for each run, so each sign is compared within its own module run, on 11,811 enrolments of 2013 and then the
same model on 15,724 of 2014. All five signs pass our criterion in both years. A missed task goes with 40.8 more
points of non-completion in 2013 and 39.3 in 2014. A late tutor-marked assignment, 20.2 and 20.3. No click in the last
seven days, 14.5 and 15.8. Below the run's median, 13.4 and 14.6, and no click before the start, 10.6 and 8.7. Between years no sign moves more than two points.
And remember: these are associations. A student who stops clicking may already have decided to leave. Are they
stable?
**Sources:** [M5 §11.3], [M5 App XIII Table A.33], [M5 §11.3 Figure 11.2]

## Slide 52 – Consistent Across Modules and Checks   [11 Findings]   [Line: detail]
**Lead:** Each sign keeps its direction in every module and under six sensitivity runs, with one wide exception.
**On the slide:** Key: AQ2 = diagnostic question; TMA = tutor-marked assignment; CMA = computer-marked assessment;
sensitivity run = the same model with one analysis choice changed.
- Modules: 2013 – every sign in the same direction in every module where it is defined (4 of 4 task, 6 of 6 click);
  2014 – 29 of 30 module estimates.
- Exception: late TMA in AAA 2014, −1.2 points on 348 enrolments, interval −14.4 to 12.1 (includes 0).
- Six sensitivity runs (de-duplicated clicks, late CMAs counted, flagged enrolments removed, runs without a task due
  removed, half-median cut, one sign effect for all modules): no verdict changes.
- Largest shift: counting late CMAs lowers the late sign from 20.2 to 15.2 points in 2013.
- Sizes vary: no click in the last seven days ranges from 3.8 (GGG) to 27.5 points (EEE) in 2013.
**Visual:** small multiples (comparison): one mini dot-plot per sign across modules, grey dots and one accent dot for
the AAA 2014 exception.
**Speaker notes:** Two years agreeing is encouraging; here are the harder tests. Within modules, every sign points the
same way in every module of 2013, and in 29 of 30 module estimates of 2014. The exception is a late tutor-marked
assignment in AAA 2014, minus 1.2 points on 348 enrolments, with an interval so wide it includes the 2013 value. Six
sensitivity runs, from de-duplicated clicks to one common effect for all modules, change no verdict; the biggest
shift is the late sign falling to 15.2 when late computer-marked tasks count. But sizes do vary, inactivity from 3.8
points in GGG to 27.5 in EEE. One model check found a real weakness.
**Sources:** [M5 §11.3], [M5 App XIII Tables A.34, A.35]

## Slide 53 – Activity Is Graded, Not a Step   [11 Findings]   [Line: detail]
**Lead:** Yes-or-no click signs miss part of a smooth activity gradient, and once activity enters as a continuous measure, the below-median sign weakens below the criterion in 2014.
**On the slide:** Key: AQ2 = diagnostic question; residual = observed minus predicted non-completion; continuous
adjustment = log(1 + clicks on days 0–27) added to the model; criterion = at least 5 points, interval excluding 0,
same direction in two-thirds of modules.
- 2013 residuals by activity level: no click +5.6 points; half the median to the median −3.7 points – outside the
  ±2 standard-error bands.
- With the continuous adjustment: below-median sign 13.4 → 5.8 points (2013) and 14.6 → 5.9 (2014); in 2014 same
  direction in only 4 of 7 modules → no longer meets the criterion.
- The other four signs still meet it; a missed task 37.3 (2013) and 35.6 (2014).
- Design consequence: the predictive model uses continuous click measures, not only the binary signs.
**Visual:** a line of observed against predicted non-completion across five activity levels (trend), predicted in grey,
observed in the accent colour, showing the gap at both ends.
**Speaker notes:** The model check that matters looked at errors by activity level. Students with no click at all
failed to complete 5.6 points more often than the model predicted, and students just below the median 3.7 points less
often. The yes-or-no signs treat everyone under the median alike, yet non-completion keeps falling as activity rises.
When we added clicks as a continuous measure, the misfit vanished in 2013 and shrank in 2014, and the below-median sign
dropped to 5.8 points in 2013 and 5.9 in 2014; in 2014 it no longer meets the criterion. The other four survive. This is why the
predictive design uses continuous click measures. Now let us put timing and signs together.
**Sources:** [M5 §11.3], [M5 App XIII Table A.36]

## Slide 54 – The Turning Point: The List Needs Inactivity   [11 Findings]   [Line: main]
**Lead:** The strongest sign, a missed task, reaches under one in five non-completers by week 4, while a week without clicks is an independent warning available in every run, so an early list must count inactivity.
**On the slide:** Key: non-completer = Fail or Withdrawn; early-sign rule = a task due but not submitted, a tutor-marked
assignment submitted late, or no click in the last seven days.
- Missed task by week 4: strongest association (40.8 and 39.3 points) – but only 19.6% (2013) and 14.7% (2014) of
  non-completers show it.
- In 6 of 22 runs no task is due by day 27 at all.
- No click in the last seven days: 14.5 and 15.8 points, mutually adjusted, defined in every run; adjusted alone, 33.3
  points in 2013.
- So: the early-sign rule keeps its activity part; the signs become the reasons beside each name.
**Visual:** a two-panel contrast (comparison): left, "how strong" – the 40.8-point bar for a missed task; right, "how
many by week 4" – 19.6% of non-completers; arrow to a third box, "add inactivity", in the accent colour. Everything
else grey.
**Speaker notes:** Let us slow down here, because this is the point of the whole project. The missed task is our
strongest sign, 40.8 points in 2013 and 39.3 in 2014. Yet by week 4 it has appeared for fewer than one in five of the students who will fail or
withdraw, and in six runs it cannot appear at all because nothing is due yet. Waiting for missed tasks means waiting
until it is too late. A week with no clicks is different: it goes with 14.5 and 15.8 extra points even after the
other signs, and it can be measured in every run, at both cut-offs. So the early-sign rule must count inactivity, and the
signs become the factual reasons staff see beside each name. What about the model questions?
**Sources:** [M5 §11.2], [M5 §11.3], [M5 App XII Table A.31], [M5 App XIII Table A.33]

## Slide 55 – AQ3 and AQ4: Expected Outputs   [11 Findings]   [Line: main]
**Lead:** The predictive and ranking questions have expected outputs and a decision rule, but no result, because no model has been trained.
**On the slide:** Key: AQ3 = predictive question (model vs early-sign rule); AQ4 = prescriptive ranking under capacity;
S1 = the single gate (model list beats rule list on the 13 runs of 2014); FR1 = fairness review rule (recall gap over
10 points); D1 = whom to contact.
- AQ3 would give: a risk rank per enrolment at days 13 and 27; a probability only if calibration holds; answered by S1.
- If the model does not beat the rule: the rule's order stays on the D1 lists, with its own list performance measured.
- AQ4 would give: a list of 3 or 5 per 20 students per run with the signs behind each name; answered when S1 is met,
  FR1 passes or its flags are reviewed, and the risk order is stated as untested for need.
- Neither says who should make contact or whether contact helps.
**Visual:** none; two output cards ("AQ3 would give" / "AQ4 would give") with a grey "not yet run" stamp.
**Speaker notes:** Those were the answers we have. For the predictive and ranking questions we have expected outputs,
not results, because no model was trained. AQ3 would give each enrolment a risk rank at day 13 and day 27, shown as a
probability only if calibration holds, and gate S1 alone would decide whether it beats the rule. If it does not, the
rule's order simply stays, with its own list performance measured. AQ4 would turn that ranking into a list of three or
five per twenty students, with the signs beside each name, used only after the fairness review. Neither output says
who should call a student or whether calling helps. Here is the whole chain in one matrix.
**Sources:** [M5 §11.4], [M5 App XIV Table A.37]

## Slide 56 – Traceability: From Goal to Data   [11 Findings]   [Line: main]
**Lead:** Each question traces from the goal it serves to the data that meet it, with GAP where OULAD lacks a variable.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; KPI = key performance
indicator (primary: completion rate; KPI 1: early-sign contact rate; KPI 2: follow-up rate); GAP = no data in OULAD
(Open University Learning Analytics Dataset). All rows share the Business Goal and SMART Goal.
| AQ | Goal + KPI | Level | Required data | Actual dataset and variables |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Descriptive | Dated result, tasks | 22 runs, day 14: 28,061; GAP: mode, year |
| AQ2 | Primary KPI; KPI 1 | Diagnostic | Signs, weeks 1–4 | Day 27: 11,811 and 15,724; GAP: attendance |
| AQ3 | KPI 1 (rule to beat) | Predictive | Enrolment at cut-off | 19 predictors; 2014 test |
| AQ4 | KPIs 1–2: GAP | Prescriptive | Capacity; contacts | GAP: contacts |
**Visual:** table (structure) – the first half of the Final Project Traceability Matrix; GAP cells in the accent
colour.
**Speaker notes:** The course asks us to show the whole chain for each question, and this matrix does it in two
halves. The first half runs from the goal to the data. Every row serves the same Business Goal. AQ1 feeds the primary
KPI and is met by 28,061 enrolments, with a gap where OULAD has no delivery mode or year of study. AQ2 feeds the
primary KPI and the early-sign KPI, met by 11,811 and 15,724 enrolments, with attendance missing. AQ3 is tied to the
rule it must beat. AQ4's link to the contact KPIs is a gap, because no contact is recorded anywhere. The second half
continues from method to decision.
**Sources:** [M5 §11.1 Table 11.1], [M5 App XI Table A.27]

## Slide 57 – Traceability: From Method to Decision   [11 Findings]   [Line: main]
**Lead:** For AQ1 and AQ2 every link holds evidence and both meet their criteria; for AQ3 and AQ4 the chain ends at the evaluation design.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; S1 = single gate;
FR1 = fairness review rule; D1 contact, D2 support time, D3 extension; N.A. = no result yet.
| AQ | Preparation | Method | Evaluation / result | Decision | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Day-14 rule; tutor- and computer-marked tasks | Grouped rates | Paths agree; 45.3% | D2, D3 | Answered |
| AQ2 | Dated by day 27 | Logistic, run effects | 5 of 5 signs, both years | D2; D1 | Answered |
| AQ3 | Refit per fold | Penalised logistic; reasons | S1 planned; N.A. | D1 | Deferred |
| AQ4 | 3 or 5 per 20 | Top-k with signs | S1, FR1; N.A. | D1 | Deferred |
**Visual:** table (structure) – the second half of the matrix; Answered rows in the accent colour, Deferred rows grey.
**Speaker notes:** The second half follows each question from preparation to decision. AQ1 rests on the day-14 rule
and the tutor- and computer-marked tasks, uses grouped rates, passes its check and gives 45.3%; it informs where
support time goes and how the university would measure an extension. AQ2 rests on signs dated by day 27, uses the
fixed-effects logistic model, and all five signs pass in both years; it informs support time and gives the reasons on
the contact list. AQ3 and AQ4 stop at the evaluation design: gate S1 and the fairness rule are planned, and their
results read "not applicable". Here are the four answers side by side.
**Sources:** [M5 §11.1 Table 11.2], [M5 App XI Table A.28]

## Slide 58 – The Four Answers Side by Side   [11 Findings]   [Line: detail]
**Lead:** Two answers are measured, two are expected, and each carries its confidence and its implication for a decision.
**On the slide:** Key: AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive ranking; D1 contact, D2
support time; S1 = single gate; FR1 = fairness review rule.
| AQ | Main finding or expected output | Confidence | Implication |
| :---- | :---- | :---- | :---- |
| AQ1 | 45.3% did not complete; runs 24.9–58.3%; under 20% missed a task by week 4 | High for OULAD 2013–2014; KPI proxy | D2 hypothesis; tasks alone too late |
| AQ2 | Five signs consistent in both years; missed task 40.8 and 39.3 points | Moderate; association | D1 reasons; contact to test |
| AQ3 | Expected: risk rank; gate S1 | Not applicable | D1 order only if S1 is met |
| AQ4 | Expected: 3 or 5 per 20 with signs | Not applicable; no contact data | D1 list, not a contact plan |
- OULAD = Open University Learning Analytics Dataset; KPI = key performance indicator.
**Visual:** table (lookup) – the final answers by question; the confidence column as plain text, no colour coding
beyond Answered/Deferred.
**Speaker notes:** Side by side, the four answers. AQ1: 45.3% did not complete, runs ranged from 24.9 to 58.3 percent,
and fewer than one in five non-completers had missed a task by week 4; high confidence for OULAD, and a hypothesis for
where support time goes. AQ2: five signs consistent in both years, a missed task at 40.8 and 39.3 points; moderate
confidence because these are associations with a known misfit; they give reasons for the contact list. AQ3 and AQ4:
expected outputs only, with no confidence to report. The last column is what matters to the staff, so let us take the
decisions one by one, starting with whom to contact.
**Sources:** [M5 §11.5 Table 11.3], [M5 App XIV Tables A.38, A.39]

## Slide 59 – Decision D1: Whom to Contact   [11 Decision support]   [Line: main]
**Lead:** For whom to contact, the early-sign rule is the candidate list, with its signs shown as reasons, once its own list performance has been measured.
**On the slide:** Key: D1 = whom to contact at each review point (lecturers, lecturer-advisors, support office); B2 =
the rule-ranked list measured as a baseline in the predictive test; S1 = the gate a model must pass to replace the
rule's order.
- Evidence now: a missed task goes with 40.8 more points (37.7–43.9) in 2013; each part of the early-sign rule carries
  information on its own; only 19.6% of non-completers had missed a task by week 4.
- Option: build the week-3 and week-5 lists from the early-sign rule, ordered by number of signs, with the signs beside
  each name, once its list performance (B2) is measured; use a model's order only if S1 is met.
- Still to test: that contacting flagged students raises completion – in a randomised pilot with contacts and outcomes
  logged; the offer and the contact person stay open choices for that pilot.
**Visual:** none; a three-step card "evidence → option → test", the option in the accent colour.
**Speaker notes:** Starting with D1, whom to contact. The evidence supports a clear candidate: the early-sign rule. It
is interpretable, it can be computed from records the university already holds, and each of its parts goes with later
non-completion in both years. So the option is to build the week-3 and week-5 lists from it, ordered by the number of
signs, with the signs shown beside each name. Two conditions remain. First, how well its list reaches non-completers
has not been measured; that is baseline B2 of the predictive test. Second, a model replaces its order only by passing
gate S1. What it cannot tell us is whether contact helps. That is for the pilot. Next, where to place support time.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40]

## Slide 60 – Decision D2: Where to Place Support Time   [11 Decision support]   [Line: main]
**Lead:** The rates and signs suggest placing early support where non-completion and early signs are highest, as a hypothesis for the university's own records.
**On the slide:** Key: D2 = where the program manager places the time of the support office and lecturer-advisors each
semester; D3 = whether to extend the approach; run = one offering of a module (B = February, J = October); OULAD =
Open University Learning Analytics Dataset.
- Evidence now: non-completion from 24.9% to 57.5% between runs in 2013; February runs 51.6% vs October runs 42.4%
  (2013); no click on days 21–27 in 54.8% of GGG 2013J but 7.6% of DDD 2013B.
- Option, as a hypothesis: place early support time first in the courses and intakes with the highest non-completion
  and the highest share of early signs, measured on the university's own records.
- Caution: high risk marks where non-completion concentrates, not where support helps most.
- Check before adoption: the pattern repeats in the university's courses over several semesters; the baseline is
  recounted under the add-drop rule.
**Visual:** horizontal bar chart (comparison) of 2013 run rates sorted from lowest to highest, the top runs in the
accent colour, labelled "where support time would go first, if the pattern repeats".
**Speaker notes:** D2 belongs to the program manager: where should support time go each semester? In 2013, runs ranged
from 24.9 to 57.5 percent non-completion, February intakes lost more than October ones, and the share of students
without clicks in the last week before day 27 ranged from 7.6% in one run to 54.8% in another. The option is to place
early support first where both non-completion and early signs are highest. But it is a hypothesis: OULAD is not the
university, and a high-risk course shows where losses concentrate, not where support would help most. The pattern
must repeat in the university's records over several semesters. Finally, the biggest decision, D3.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40]

## Slide 61 – Decision D3: Whether to Extend   [11 Decision support]   [Line: main]
**Lead:** For extending the approach, the project offers a measurement method, a gate and a fairness audit, not a verdict; extension waits for a pilot result.
**On the slide:** Key: D3 = whether to extend the approach to all courses and link data routinely (leadership, legal
staff, data office); S1 = model gate; FR1 = fairness review rule.
- Evidence now: the denominator alone can move a completion rate by up to 13.6 points; no model result yet; no evidence
  on the effect of contact.
- Option: decide only after the pilot, with completion of pilot and comparison courses computed by one rule, and the
  S1 gate and FR1 audit run.
- Conditions: a completion gain against comparison courses; legal approval under Vietnam's rules on high-risk AI use;
  staff capacity confirmed.
- Even a negative pilot result shows, at small scale, which part of the path does not work.
**Visual:** none; a checklist of three conditions, each unchecked, in grey with the "pilot result" condition in the
accent colour.
**Speaker notes:** D3 is the decision closest to a one-way door: extending the approach to all courses and linking data
routinely. Here the project offers tools rather than a verdict. A way to measure completion by one rule for pilot and
comparison courses, which matters because the denominator alone can move a rate by 13.6 points. A gate a model must
pass. And a fairness audit. What it cannot offer yet is any evidence that contact helps. So extension waits for a pilot
result, legal approval and confirmed staff capacity. Even a negative pilot is valuable: it shows which part of the
path fails before the university commits. That brings us to the limits of everything we have shown.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40]

## Slide 62 – Limitation Log   [12 Limitations]   [Line: main]
**Lead:** We separate what showed no evidence, what has no data to test and what is not yet tested, because each needs a different next step.
**On the slide:** Key: AQ3 predictive, AQ4 prescriptive ranking; KPI = key performance indicator; OULAD = Open
University Learning Analytics Dataset.
| Limitation | Kind | Handling |
| :---- | :---- | :---- |
| Year difference over all enrolments in shared modules; small-module click signs | No evidence found | No claim; reported as uncertain |
| Contact and its outcome; delivery mode, year of study, attendance; capacity | No data to test | Randomised pilot |
| Several-modules sign before 2014; leave and transfer | No data to test | Described on 2014; university recount |
| AQ3 and AQ4 results | Not yet tested | Single predictive test, design unchanged |
| Binary click signs; below-median sign weak in 2014 once adjusted; KPI proxy and denominator | Measurement | Continuous measures in the model; one add-drop rule |
| UK distance learning of 2013–2014; observational design | Scope and causal | Re-check on the university's records; options as hypotheses |
**Visual:** table (structure) grouped by kind of limit, with the three kinds as coloured section labels.
**Speaker notes:** Every answer we gave has a boundary, and we sorted the boundaries by what they need next. "No
evidence found" means we compared and saw no clear difference, like the small-module click signs; we make no claim.
"No data to test" means OULAD and every candidate lack the data, like contacts, year of study or attendance; only the
pilot can create them. "Not yet tested" means the data exist and the analysis waits, which is AQ3 and AQ4. Then
measurement limits, like the binary click signs and our KPI proxy. And the largest: these are UK distance-learning
modules from 2013 and 2014, and the design is observational. So, what comes next?
**Sources:** [M5 §12 Table 12.1], [M5 App XV Table A.41]

## Slide 63 – Next Steps and the Pilot   [12 Future work]   [Line: main]
**Lead:** Two steps can run on OULAD now, and three need the university, ending in a randomised pilot that alone can show whether contact helps.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset; AQ1 descriptive; AQ2 diagnostic; AQ3
predictive; AQ4 prescriptive ranking; S1 = model gate; FR1 = fairness review rule.
1. Level 2 prototype of AQ3: does a model at day 27 list more non-completers than the rule (S1)? Also the rule's own
   list performance and calibration. Data: OULAD as prepared.
2. AQ4 list and fairness audit: recall at 3 and 5 per 20, gain over a random list, FR1 by disability and deprivation
   band. Depends on step 1.
3. Transfer to the university: baseline recounted under the add-drop rule; rule on the university's task calendar;
   AQ1 and AQ2 re-checked. Data: two years of the university's records.
4. Risk classification and consent: legal review; students' acceptance of activity-based contact.
5. Randomised pilot: does contact raise completion, and which contact and offer work? Contacts logged with time,
   person, offer and outcome.
**Visual:** a five-step sequence (process), steps 1–2 under "on OULAD now" in grey, steps 3–5 under "at the university"
with step 5 in the accent colour.
**Speaker notes:** The limits translate directly into steps. Two can run on OULAD as it stands: the single predictive
test under the frozen protocol, which also measures how good the rule's own list is, and then the ranked list with
its fairness audit. Three need the university. First, recount the baseline under the same add-drop rule and re-check
our two answers on its own records. Second, a risk classification and real students' consent, because activity-based
contact was accepted only by simulated students. Third, a randomised pilot among flagged students, with every contact
logged with its outcome, because only random assignment separates the effect of contact from the reasons a student was
flagged. That pilot also has legal conditions.
**Sources:** [M5 §12.1], [M5 App XV Table A.42]

## Slide 64 – Legal and Ethical Conditions   [12 Future work]   [Line: detail]
**Lead:** A contact list built from a model is likely a high-risk use under Vietnamese law, so staff keep the final say and a flag must never become a label.
**On the slide:**
- Law on Artificial Intelligence No. 134/2025/QH15, from 1 March 2026: human control and the ability to intervene over
  every decision of an AI system.
- Decision 33/2026/QĐ-TTg: AI systems that automatically assess or rank learners, or monitor learner behaviour, are
  high-risk uses in education.
- Personal data: a declared disability is health information and needs the student's consent in the pilot.
- Ethics: predictive analysis carries a potential for bias and stereotyping; a flag leads to support and expires with
  the run.
- Retraining: contacts logged with outcomes before any model is retrained, so a model never learns its own influence.
**Visual:** none; five short conditions with the two legal citations set apart.
**Speaker notes:** The pilot cannot start just because the analysis is ready. Vietnam's Law on Artificial Intelligence,
in force since 1 March 2026, requires human control over every decision of an AI system, and Decision 33/2026 lists
systems that rank learners or monitor their behaviour as high-risk uses in education. Our list fits that description,
so it needs a risk classification first, and staff keep the final say on every contact. Declared disability is health
information, so the pilot needs consent. Ethically, a flag must not become a label: it leads to support and expires
with the run. And contacts are logged before any retraining, so the model never learns its own influence. One more
part of our process to account for: AI.
**Sources:** [M5 §12.1], [M5 App XV], [M5 App VI]

## Slide 65 – Generative AI: One Rule Throughout   [13 Generative AI]   [Line: main]
**Lead:** AI played several roles across the five milestones, but under one rule: it was never a source of data, statistics, licence information or results.
**On the slide:**
- Roles: simulated stakeholder; research and code assistant; critic; writing partner.
- Verification matched to the risk: quotes against transcripts; literature against saved copies with verbatim
  quotations; code against fixture tests and independent recounts; critics confined to the brief and the data.
- Most useful: critics forced to argue from the data – a Milestone 3 auditor found tasks due before registration
  counted as missed and a leakage check that could not fail.
- Human decisions: keep the 2014 runs out of every predictive choice; one early-sign rule; report AQ3 and AQ4 as
  designs; state every association as an association.
- Key: AQ3 = predictive question; AQ4 = prescriptive ranking question.
**Visual:** none; four role icons in a row, with the rule written across them in the accent colour.
**Speaker notes:** We used generative AI throughout, and we owe you an account of how. It played a simulated
stakeholder in Milestone 1, then research assistant, code assistant, critic and writing partner. One rule never
changed: AI was never a source of data, statistics or results. Every fact it offered was checked against a saved
source, the data or code we ran. The reviews helped most when the critic had to argue from the data: in Milestone 3 an
AI auditor found that tasks due before a student registered were counted as missed, and that one of our leakage checks
could not fail. The decisions stayed ours, as listed here. The log has the details.
**Sources:** [M5 §13], [M5 §13.2], [M5 App XVI]

## Slide 66 – AI Decision Log   [13 Generative AI]   [Line: detail]
**Lead:** Every AI contribution is logged with what it suggested, how we checked it and what we decided.
**On the slide:**
| Stage | AI used for | Check | Our decision |
| :---- | :---- | :---- | :---- |
| Milestone 1 | Simulated stakeholders; reviewer (12 critiques) | Quotes checked against transcripts | 9 accepted, 2 in part, 1 rejected; interviews count as simulated |
| Milestone 2 | Search and selection critics (22 critiques) | Every dataset fact from the official source | Gates require a dated withdrawal and dated tasks |
| Milestone 3 | Code assistant, critics, leakage auditor (8 findings) | Fixture tests; 13 of 13 numbers equal to a recount | All eight findings acted on |
| Milestone 4 | Three isolated reviewers (24 critiques) | Checked against design facts and arithmetic | Switching rule with a fixed margin; gate on all 13 test runs |
| Milestone 5 | Evidence extraction; analysis code; drafting and review | 369 statements checked against 32 sources, 0 errors; 2014 associations re-estimated by separate code, 35 of 35 agree | 66 critiques: 42 accepted, 14 in part, none rejected, 10 handled in finishing; no AI produced a metric value, threshold or result |
**Visual:** table (lookup) – the AI Decision Log condensed to one row per milestone.
**Speaker notes:** This is the AI Decision Log, one row per milestone. In Milestone 1 a reviewer gave twelve critiques;
we accepted nine, two in part and rejected one. In Milestone 2 critics pushed the gates to require a dated withdrawal
and dated tasks. In Milestone 3 every script was kept only after review, and all eight findings of the leakage auditor
were acted on. In Milestone 4 three isolated reviewers added a switching rule with a fixed margin. In this milestone AI
extracted 369 statements, each checked automatically against its source with zero errors, and wrote analysis code
whose 2014 results were re-estimated by separate code. No AI produced a metric, threshold or result. Now, our
conclusions.
**Sources:** [M5 §13.1], [M5 App XVI Table A.43]

## Slide 67 – Conclusions, Firmest First   [14 Conclusion]   [Line: main]
**Lead:** Our conclusions run from verified counts to associations to designs, and their strength falls in that order.
**On the slide:** Key: OULAD = Open University Learning Analytics Dataset (UK, 2013–2014); AQ3 predictive; AQ4
prescriptive ranking.
1. **Verified count (high confidence, OULAD):** 45.3% of enrolments still registered at day 14 did not complete; runs
   ranged from 24.9% to 58.3%.
2. **Measurement rule:** the denominator alone moves a rate by up to 13.6 points and can reverse a year comparison, so
   completion must be stated with its add-drop rule.
3. **Timing:** under one in five non-completers had missed a task by week 4, so an early list cannot rest on missed
   tasks alone.
4. **Associations (moderate confidence):** all five early signs go with later non-completion within module in both
   years, a missed task by 40.8 and 39.3 points; they can serve as reasons staff check beside each name.
5. **Designs:** for AQ3 and AQ4 a penalised logistic model judged once against the rule and a capacity-limited list
   audited for fairness are the appropriate methods; their outputs remain expected, not measured.
**Visual:** a ranked list with a confidence bar beside each item, fading from the accent colour (firm) to grey
(design).
**Speaker notes:** Let us draw it together, firmest first. One: on OULAD, 45.3% of enrolments still registered at day
14 did not complete, and runs differed widely; two independent counts agree. Two: the denominator alone moves a rate
by up to 13.6 points and can reverse a year comparison, so any completion figure needs its add-drop rule. Three: fewer
than one in five non-completers had missed a task by week 4, so a list cannot wait for missed tasks. Four: five early
signs go with later non-completion in both years, which makes them useful reasons, not causes. Five: the predictive
and ranking questions have a sound design and no result yet. Just as important is what we cannot conclude.
**Sources:** [M5 §14], [M5 §11.2], [M5 §11.3], [M5 §11.4]

## Slide 68 – What We Cannot Conclude, and Open Problems   [14 Conclusion / 12 Limitations]   [Line: main]
**Lead:** Three claims stay out of reach of these data, and each maps to an open problem with a planned answer.
**On the slide:** Key: AQ3 = predictive question; the rule = the early-sign rule.
| We cannot conclude that… | Because | Open problem and planned answer |
| :---- | :---- | :---- |
| the signs cause non-completion | A regression capturing associations is descriptive, not causal | Treat signs as reasons to check, never as causes |
| a model ranks students better than the rule | No model has been trained or tested | The single AQ3 test under the frozen protocol |
| contacting a listed student raises completion | No data record contact; effectiveness needs a randomised experiment | A randomised pilot with contacts and outcomes logged |
- Every result describes UK distance-learning modules of 2013–2014 and must be re-checked on the university's records.
**Visual:** table (structure): three rows; the "planned answer" column in the accent colour.
**Speaker notes:** Equally firm is what we cannot say. We cannot say the signs cause non-completion: a regression that
captures associations describes them, it does not explain them. We cannot say a model ranks students better than the
simple rule, because no model has been tested; that is the single predictive test we kept clean. And we cannot say
that contacting a listed student raises completion, because no data record a contact, and questions of effectiveness
need a randomised experiment. Above all three sits the scope: UK distance-learning modules from 2013 and 2014, to be
re-checked at the university. If you remember one thing, make it this.
**Sources:** [M5 §14], [M5 §12], [M5 §12.1]

## Slide 69 – Take-Home Message   [14 Conclusion]   [Line: main]
**Lead:** Start early with an interpretable list that counts inactivity, test a model against it once, and let a randomised pilot decide whether contact helps.
**On the slide:** Three lines, large:
- **Don't wait for missed tasks:** under one in five non-completers show one by week 4.
- **Start simple, test once:** the early-sign rule is the list to beat; a model replaces it only by passing one gate.
- **Prove it before scaling:** only a randomised pilot can show whether early contact improves completion.
**Visual:** none; three short lines in large type, the first in the accent colour.
**Speaker notes:** So here is what we hope you take away. Do not wait for missed tasks: by week 4, fewer than one in
five of the students who will fail or withdraw have missed one, so an early list has to look at whether students are
still active. Start simple and test once: the early-sign rule is interpretable and computable from records the
university already has, and a model replaces it only by passing one gate fixed in advance. And prove it before
scaling: only a randomised pilot can tell us whether, and for whom, early contact improves completion. That is the
question no open dataset can answer, and it is where this project hands over to the university.
**Sources:** [M5 §11.2], [M5 §11.5], [M5 §14]

## Slide 70 – Thank You and Questions   [Closing]   [Line: main]
**Lead:** Thank you; we welcome your questions on any link of the chain, from the problem to the pilot.
**On the slide:** "Thank you – questions?" Below, the eleven-link chain from slide 9 in grey as a map for questions,
with the two answered questions (AQ1 descriptive, AQ2 diagnostic) and the two designed ones (AQ3 predictive, AQ4
prescriptive ranking) labelled. The full report, its appendices and the Final Project Package hold every table and
check.
**Visual:** the project chain diagram (structure), all grey, as a navigation aid for questions.
**Speaker notes:** Thank you for following the chain with us, from a stakeholder's worry about students noticed too
late, through the data, their preparation, the methods and the evaluation, to the two questions we could answer and
the two we have designed and kept for a single honest test. Our report and its appendices hold every table we showed,
with its population and interval, and the final package lets anyone rebuild the prepared data from the public
download. We are happy to take questions on any link of the chain, whether it is the add-drop rule, the early signs,
the gate, the fairness audit or the pilot.
**Sources:** [M5 §1.2 Figure 1.1], [M5 §7.2]
