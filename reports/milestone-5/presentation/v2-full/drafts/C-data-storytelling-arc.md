# Draft C – Narrative arc (full deck, Milestone 5 final presentation, team N04)

**Method.** Data-storytelling narrative arc: setup → conflict → resolution, carried through the six steps of the arc
(hook with a surprising insight, context and baseline, rising action through data points, climax, resolution with
recommendations, call to action). Every slide passes the "So what?" test: its lead sentence states the message, its
title only names the topic, and every chart or table carries its key and its one annotated takeaway. Spoken register
follows the talk-script craft: one idea per sentence, signposts at each part boundary, numbers said with their
population, every transition written out as the last sentence of the notes.

**Big idea (core message).** Nearly half of the students still enrolled after add-drop do not complete, and most of
them have not missed a single task by week 4, so a list built on missed tasks comes too late; their platform activity
already signals the risk, so the early-sign rule that also counts inactivity is the right candidate for the week-3 and
week-5 lists. It is an association to be measured once on unseen runs, re-checked on the university's records and
tested for effect only in a randomised pilot.

**The arc.**

| Step of the arc | What carries it | Slides |
| :---- | :---- | :---- |
| Hook (surprising insight) | 45.3% of enrolments still registered at day 14 did not complete, yet only 19.6% (2013) and 14.7% (2014) of non-completers had missed a task by week 4 | 1–3 |
| Context and baseline (setup) | Vietnamese university, regulated withdrawal, students noticed in week 5–6 against a 2–4-week window; goal, KPIs, decisions, questions | 4–19 |
| Rising action (conflict) | No open data on Vietnamese courses; OULAD as stand-in and what it lacks; what quality, preparation, method and evaluation had to change; AQ1 shows the size and the late timing of missed tasks | 20–63 |
| Climax (key insight) | Missed tasks come too late for most non-completers (AQ1 timing), while all five early signs, activity signs included, go with later non-completion within module in both years (AQ2) | 63–69 |
| Resolution (recommendations) | Expected outputs of AQ3 and AQ4; answers by question; decision options for D1, D2 and D3; limits stated as conditions; generative AI use | 70–84 |
| Call to action | Run the single AQ3 test, recount on the university's records, classify the list's risk, then a randomised pilot with contacts logged (roadmap 78–81); conclusions firmest first, take-home and thanks | 85–89 |

- **Hook:** "Nearly one in two students still enrolled after add-drop did not complete. Fewer than one in five of
  them had missed a single task by week 4. So the signal everyone watches arrives too late." [M5 Abstract; §11.2]
- **Climax:** all five early signs go with later non-completion within module in both years, a missed task by 40.8
  (37.7–43.9) and 39.3 (36.4–42.1) points, and the activity signs carry information where tasks have not yet fallen
  due: the early-sign rule needs its activity part. [M5 §11.3; App XIII Table A.33]
- **Call to action:** "Measure the rule's list once on the 13 unseen runs, recount on the university's own records,
  classify the list's risk, then let a randomised pilot answer the only question no open dataset can: whether early
  contact helps." [M5 §12.1; §14]

**Coverage table.**

| Brief part | Slides |
| :---- | :---- |
| Abstract / executive summary | 2, 3 |
| 1 Introduction and educational context (context, motivation, stakeholders, scope, objective) | 4, 5, 6, 7, 8 |
| 2 Business understanding and success criteria (Business Goal, SMART Goal, KPIs, D1–D3) | 9, 10, 11, 12, 13 |
| 3 Analytical questions and analytics levels (final AQs, levels, scope, decision, quality check, revision status) | 14, 15, 16, 17, 18, 19 |
| 4 Data requirements and dataset selection (unit, outcome, concepts, time, population, candidates, rationale, provenance, licence; Data Requirement Matrix) | 20, 21, 22, 23, 24 |
| 5 Dataset description and requirement–data fit (tables, keys, coverage, gaps, keep/modify/defer; data dictionary, AQ–Data Fit Matrix) | 25, 26, 27, 28, 29, 30 |
| 6 Data understanding and quality (distribution, missingness, duplicates, invalids, outliers, imbalance, temporal coverage, representativeness, sensitive fields) | 31, 32, 33, 34, 35, 36, 37 |
| 7 Data preparation (cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control, final versioned dataset; Preparation Decision Matrix) | 38, 39, 40, 41, 42 |
| 8 Modeling and analysis strategy (AQ → type → task → baseline → candidates → primary proposal → rationale; Method Selection Matrix) | 43, 44, 45 |
| 9 Evaluation design (metric, baseline, split and validation, success criterion, leakage, fairness, interpretability) | 46, 47, 48, 49, 50, 51, 52 |
| 10 Experimental status (Level 2 not run, and why) | 53, 54 |
| 11 Findings, discussion and decision support (AQ-by-AQ answers, Final Project Traceability Matrix, D1–D3) | 55–75 |
| 12 Limitations and future work (limitation log, deferred AQs, next data, pilot) | 76, 77, 78, 79, 80, 81 |
| 13 Generative AI use and reflection (AI decision log) | 82, 83, 84 |
| 14 Conclusion | 85, 86, 87, 88, 89 |

**Counts.** 89 slides: 49 marked `Line: main`, 40 marked `Line: detail`.

---

## Slide 1 – Early identification of disengaging students   [Title]   [Line: main]
**Lead:** We look for students who stop taking part in an online course early enough to support them within the semester.
**On the slide:** Final Project Report: Early Identification of Disengaging Students in Online Courses · MTH045 – The
Science of Data Analytics · University of Science, VNU-HCM, Faculty of Information Technology · Group 4 (N04):
25C12002 – Lê Ngọc Trúc Huỳnh; 25C12003 – Phan Trần Khanh; 25C12031 – Dương Tấn Huỳnh Phong · Lecturers: Dr. Nguyễn
Trần Minh Thư, MSc. Phạm Minh Tú · 14 November 2026
**Visual:** none (title layout with the university logo).
**Speaker notes:** Good morning. Picture a student in week 5 of an online course. She has not failed anything. She has
not withdrawn. On paper she is fine. But she has stopped opening the course, and by the time her name reaches anyone,
the weeks in which help still works are gone. Our project is about that student. We are team N04, and over five
milestones we traced one chain of evidence: from the people who need to act, to the data, to how we prepared it, to the
methods and how we judge them, and finally to what the results let a university decide. We will be honest about what
we answered and what is still a design. And we start with the number that surprised us most. [click]
**Sources:** [M5 Title page]

## Slide 2 – The surprising number   [Abstract / hook]   [Line: main]
**Lead:** Nearly half of the enrolments still registered after add-drop did not complete, yet fewer than one in five of those non-completers had missed a task by week 4.
**On the slide:** Card 1: 45.3% (44.7–45.8) did not complete, of 28,061 enrolments still registered at day 14, 22
module runs, 2013–2014 [M5 §11.2] · Card 2: only 19.6% (2013) and 14.7% (2014) of non-completers had missed an
assessed task by week 4 [M5 §11.2; App XII Table A.31] · Takeaway line: a list built on missed tasks alone comes too
late for most students. · Key: module run = one offering of a course, the counterpart of a semester; day 14 = end of
the add-drop window; non-completion = Fail or Withdrawn.
**Visual:** two large number cards side by side (comparison): the size of the problem against the share visible by
week 4; the second card in the accent colour.
**Speaker notes:** Here it is. Of the 28,061 enrolments still registered at day 14, the end of the add-drop window,
45.3 percent did not complete. That is nearly one in two. Now the surprise. The obvious early warning is a missed
assignment. But by the end of week 4, only 19.6 percent of the non-completers of 2013, and 14.7 percent of those of
2014, had missed a single assessed task. So if a lecturer waits for missed work, most of the students who will not
finish are still invisible in week 4. That gap, between how many students we lose and how few show it in the obvious
place, is the thread of this whole talk. Let me give you the full answer in one slide before we build it up. [click]
**Sources:** [M5 Abstract; §11.2; App XII Table A.29, Table A.31]

## Slide 3 – Executive summary   [Abstract]   [Line: main]
**Lead:** On an open UK dataset, we answered how many students are lost and which early signs go with it, and we designed, but did not yet run, the test of a ranked contact list.
**On the slide:** Problem: students who stop taking part are noticed late; three decisions need evidence: D1 whom to
contact at each review point, D2 where to place support time, D3 whether to extend the approach. · Data: OULAD (Open
University Learning Analytics Dataset) as a stand-in, 22 module runs of 2013 and 2014. · Four analytical questions
(AQ1–AQ4), one per analytics level. · Answered: AQ1 (descriptive), 45.3% (44.7–45.8) of 28,061 did not complete
[M5 Abstract]; AQ2 (diagnostic), all five early signs go with later non-completion within module in both years, a
missed task by 40.8 (37.7–43.9) and 39.3 (36.4–42.1) percentage points [M5 Abstract]. · Designed, not run: AQ3
(predictive) and AQ4 (prescriptive, ranking under staff capacity). · Read as: associations, not causes; re-check on the
university's records; the effect of contact awaits a pilot.
**Visual:** a three-row summary table (Answered / Designed / Still open) so the audience holds the whole result before
the build-up (structure).
**Speaker notes:** So, the whole story in one slide. Three people need to decide things: who to contact, where to put
support time, and whether to extend the approach. We call those D1, D2 and D3. No open data on Vietnamese courses
exist, so we used OULAD, the Open University Learning Analytics Dataset, as a stand-in. We asked four questions, AQ1 to
AQ4, one per analytics level. Two are answered: how many students are lost, and which early signs go with it. Two are
designs: a predictive model and a ranked list, specified in full but not yet run. Everything we found is an
association on UK data, which must be re-checked here. With that map in hand, let us go back to the beginning: the
university and its problem. [click]
**Sources:** [M5 Abstract; §1.2; §3 Table 3.1; §10]

## Slide 4 – The educational setting   [1 Introduction and context]   [Line: main]
**Lead:** A Vietnamese university is expanding online learning, withdrawal is a regulated quality measure, and students who disengage are noticed after the window for help has closed.
**On the slide:** Setting: one undergraduate program of about 1,200 students in online and blended courses on the
university's LMS (learning management system); the size is a scenario assumption [M5 §1]. · Regulation: Circular
01/2024 caps the annual withdrawal rate at 10% and the first-year rate at 15%; Circular 83/2026 keeps these thresholds
from 15 November 2026 [M5 §1]. · The problem: lecturers become sure around week 5 or 6; the program manager sees
counts after the semester; the support office meets most of these students on the academic warning list at its end
[M5 §1, simulated interviews]. · The window for effective support of a student at risk: two to four weeks [M5 §1].
**Visual:** a semester timeline from week 1 to the end of term: a shaded band for the 2–4-week support window, and
markers where each role notices the student (week 5–6, semester end); sequence shows the gap.
**Speaker notes:** Let us set the scene. The project sits in a Vietnamese university that is moving more teaching onto
its learning management system, the LMS. We take one undergraduate program of about 1,200 students; like every figure
about the university, that is a scenario assumption. Withdrawal here is not only a pastoral worry. Circular 01/2024
caps the annual withdrawal rate at 10 percent and the first-year rate at 15, and Circular 83/2026 keeps those caps. Now
look at the timeline. Published work puts the window for effective support at two to four weeks. Lecturers in our
interviews only become sure around week 5 or 6, and the support office meets most of these students at the end of the
semester. The help arrives after the window. So who exactly could act earlier? [click]
**Sources:** [M5 §1; App I]

## Slide 5 – Who decides what   [1 Motivation and stakeholders]   [Line: main]
**Lead:** The records that could show the drift already exist, but each person who could act sees only part of it.
**On the slide:** Table (stakeholder – decision supported): Course lecturers, lecturer-advisors (lecturers who advise
student classes) and the student support office – D1: whom to contact at each review point · Program manager – D2:
where to place support time each semester · University leadership, with legal staff and the data office – D3: whether
to extend the approach and link data routinely · Students – the subject of every data use; whether to accept help
[M5 §1.1; App I Table A.1]
**Visual:** a stakeholder map: three decision owners around the student in the centre, each arrow labelled D1, D2 or D3
in words (structure).
**Speaker notes:** Why is this worth analysing? Because the data that could show the drift already sit in the LMS and
the academic records, but nobody sees all of it. Three groups decide. The course lecturers, the lecturer-advisors, who
are lecturers advising a student class, and the support office decide whom to contact at each review point; we call
that D1. The program manager decides where support time goes each semester; that is D2. And leadership, with legal
staff and the data office, decides whether to extend the approach and link data routinely; that is D3. In the middle
is the student, who is the subject of every data use and decides whether to accept help. So what did these people ask
us for? [click]
**Sources:** [M5 §1.1; App I Table A.1]

## Slide 6 – What the stakeholders asked for   [1 Motivation]   [Line: detail]
**Lead:** Simulated interviews shaped the design, a short list at weeks 3 and 5 with a reason for each name, but they are never evidence.
**On the slide:** Requests: a short list at weeks 3 and 5 · a factual reason beside each name · within about 30–40
contacts a week for the support office and three to five for each lecturer-advisor · for support only, no automated
step [M5 §1.1]. · How we got them: interviews in which generative AI took both sides; 51 key statements, each labelled
opinion, assumption or scenario information [M5 App I]. · Status: simulated views; they motivate timing and list length;
every finding rests on the data or on published work. · Precedent: the Open University's tool, OU Analyse, informs
teachers so that the teachers act [M5 §1.1].
**Visual:** a callout box "Simulated, not evidence" beside four request cards (structure).
**Speaker notes:** Following on from who decides: what did they want? One honest point first. We could not interview
real staff, so in Milestone 1 generative AI took both sides of every interview: one AI played the stakeholder, another
asked our questions. We checked every transcript and drew 51 statements from them. These shaped our design, and nothing
more. They asked for a short list at weeks 3 and 5, a factual reason beside each name, and a length staff can follow
up: about 30 to 40 contacts a week for the support office, three to five for each lecturer-advisor. Support only, no
automated step. The Open University, which published our dataset, works the same way: its tool informs teachers, and
teachers act. So what is in scope? [click]
**Sources:** [M5 §1.1; App I]

## Slide 7 – Scope and objective   [1 Scope and objective]   [Line: main]
**Lead:** We turn records the university already holds into a short, timely contact list with a reason for each name, and into patterns that show where students are lost.
**On the slide:** In scope: students enrolled after the add-drop period in the program's online and blended courses,
one semester at a time; decisions staff can take within a semester; completion = passing the course; withdrawal as in
Circular 83/2026, excluding approved leave and transfers. · Out of scope: assessment rules, admissions and financial
aid, students' circumstances outside the course, evaluation of lecturers, any automated decision. · Objective: a short
list per review point with an observed reason per name, plus patterns of where and when students are lost. · Condition:
analysed on OULAD (Open University Learning Analytics Dataset) as a stand-in; every result re-checked on the
university's records before it supports a decision [M5 §1.2].
**Visual:** two-column in / out table (comparison).
**Speaker notes:** Given those needs, here is where we drew the line. We cover students enrolled after the add-drop
period, one semester at a time, and only decisions staff can take within that semester. Completion means passing the
course, and withdrawal follows Circular 83/2026, so approved leave and transfers do not count. We leave out assessment
rules, admissions, students' lives outside the course, the evaluation of lecturers, and any automated decision. Our
objective is concrete: a short list at each review point with an observed reason beside every name, and patterns that
show the program where and when it loses students. One condition runs through everything: we work on OULAD as a
stand-in, so every result must be re-checked on the university's own records. Here is the route we took. [click]
**Sources:** [M5 §1.2; App I]

## Slide 8 – The chain we followed   [1 Objective / roadmap]   [Line: main]
**Lead:** One logic chain of eleven links runs from the stakeholder problem to the decisions, and this talk follows it in order.
**On the slide:** Figure: the eleven-link project chain across Milestones 1–5 [M5 §1.2 Figure 1.1]: stakeholder
problem → goal and KPIs (key performance indicators) → analytical questions → data requirements → dataset → data
understanding → preparation → method → evaluation design → findings → decisions. · Talk order: problem → data →
preparation → method → evidence → assessment → use → conclusions.
**Visual:** the project-chain diagram (sequence), with the current part highlighted on later section dividers.
**Speaker notes:** Before we go into each step, here is the map. The report follows one chain of eleven links, from the
stakeholders' problem, to the goal and its key performance indicators, the KPIs, to the questions, the data we needed,
the dataset we found, what we learned about it, how we prepared it, the method, how we would judge it, what we found,
and finally the decisions it supports. Milestones 1 to 4 each built part of this chain; Milestone 5 joins it up. We
will walk it in the same order today: problem, data, preparation, method, evidence, assessment, use, and conclusions.
At each step we will tell you the final choice, and where the data forced a change, why. First link: what exactly are
we trying to improve? [click]
**Sources:** [M5 §1.2 Figure 1.1]

## Slide 9 – Business Goal   [2 Business understanding]   [Line: main]
**Lead:** Our goal is an outcome for the university, more students passing their courses, not a model or a dashboard.
**On the slide:** Business Goal: improve successful course completion in the program's online and blended courses by
identifying students who stop taking part early enough to support them within the semester [M5 §2]. · Why this form:
it names the outcome the program already reports; early identification is the means, support within the semester the
mechanism.
**Visual:** the goal as a single quote block, with "completion" (outcome) and "early enough" (means) underlined
(structure).
**Speaker notes:** So, the first link: the goal. We wrote it as an outcome for the organisation. Improve successful
course completion in the program's online and blended courses, by identifying students who stop taking part early
enough to support them within the semester. Notice what it does not say. It does not say "build a model" or "launch a
dashboard". A model is only useful if, in the end, more students pass. The words "early enough" carry the timing
problem from the last slides: the support window is two to four weeks, and the list has to land inside it. A goal like
this is a direction, though, not a target. To make it something we can check, we need numbers and a deadline. [click]
**Sources:** [M5 §2]

## Slide 10 – SMART Goal   [2 Business understanding]   [Line: main]
**Lead:** The SMART Goal makes completion measurable: five percentage points more in the pilot courses by the end of 2027–2028, from a baseline we must recount.
**On the slide:** SMART (specific, measurable, achievable, relevant, time-bound) Goal: raise the course completion rate
of students enrolled after the add-drop period in the pilot courses from their recounted baseline (assumed 70%) by five
percentage points (assumed target 75%) by the end of the 2027–2028 academic year [M5 §2]. · Pilot: about four courses
with about 600 enrolments (both assumptions), compared with similar courses outside the pilot. · Baseline recounted
under Circular 83/2026. · Limit: it measures progress, not the effect of contact; only a randomised pilot tests that.
**Visual:** a simple bar pair, baseline (assumed 70%) and target (assumed 75%), both labelled "assumed" (comparison).
**Speaker notes:** Here is that measurable version. SMART stands for specific, measurable, achievable, relevant and
time-bound. We want the completion rate of students enrolled after add-drop in the pilot courses to rise by five
percentage points by the end of 2027–2028. The scenario gives us no real completion rate, so 70 percent as baseline and
75 as target are assumptions, replaced by the real recount before anyone commits to them. The pilot is about four
courses and about 600 enrolments, again assumed, compared with similar courses outside it. One honest limit: this goal
measures progress. It cannot say whether contacting students caused the gain; only a randomised pilot can. Now, how do
we track the goal during the semester, not only at the end? [click]
**Sources:** [M5 §2; App II Table A.2]

## Slide 11 – Key performance indicators   [2 Success criteria]   [Line: main]
**Lead:** One primary KPI measures the goal and two secondary KPIs show during the semester whether contact works; on OULAD only their non-contact parts can be measured.
**On the slide:** Table [M5 §2.1 Table 2.1] (KPI – definition – status on OULAD): Primary KPI (key performance
indicator), completion rate – passes over enrolments after add-drop – proxy at day 14: 28,061 enrolments (22 runs) ·
Secondary KPI 1, early-sign contact rate – students meeting the early-sign rule at the end of week 4 contacted by the
end of week 5, over those meeting it – sign part only: the rule flags 28.8% of 27,535 enrolments (22 runs) at day 27 ·
Secondary KPI 2, follow-up rate – listed students contacted within seven days, over students listed – measured only in
the pilot. · Key: OULAD = Open University Learning Analytics Dataset; run = one offering of a module.
**Visual:** a three-row KPI table with a status column coloured measured / partly / pilot only (table).
**Speaker notes:** From the goal to its indicators. The primary KPI is the completion rate: passes over enrolments after
add-drop. On OULAD we can only compute a proxy, counting an enrolment if it is still registered at day 14, because
registration there closes two weeks after the start. That gives 28,061 enrolments over 22 runs. Two secondary KPIs show
progress inside the semester. The first: of the students who meet the early-sign rule by week 4, how many were
contacted by week 5? The second: of the students on a list, how many were contacted within seven days? Both need a
contact record, which OULAD does not have. We can measure only the sign part: the rule flags 28.8 percent of 27,535
enrolments at day 27. So what is this early-sign rule? [click]
**Sources:** [M5 §2.1 Table 2.1]

## Slide 12 – The early-sign rule   [2 Success criteria]   [Line: main]
**Lead:** One simple rule flags a student at the data cut-off if any of three things holds, and it is the single rule of the project on OULAD and in the pilot.
**On the slide:** A student is flagged at the cut-off if: (1) a TMA (tutor-marked assignment) or CMA (computer-marked
assessment) was due and not submitted; or (2) a TMA was submitted late; or (3) there was no platform activity in the
previous seven days [M5 §2.1]. · Cut-offs: day 13 (end of week 2, for the week-3 list) and day 27 (end of week 4, for
the week-5 list) [M5 §3]. · Why the activity part: at Milestone 1 the rule was "two or more tasks missed or late by
week 4"; on OULAD two tasks fall due by day 27 in only 1 of 22 runs, so a task-only rule could not fire in most runs
[M5 App III Table A.8]. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** a three-part flowchart joined by "or", with a note box "why activity was added" (worked example).
**Speaker notes:** We keep mentioning this rule, so here it is. At the cut-off, flag a student if any one of three
things holds. A tutor-marked assignment, a TMA, or a computer-marked assessment, a CMA, was due and not submitted. Or a
TMA came in late. Or the student had no activity on the platform in the last seven days. The cut-offs are day 13 for
the week-3 list and day 27 for the week-5 list, one week before each list, because data exports take time. Why the
third part? In Milestone 1 our rule was purely about tasks: two or more missed or late by week 4. On OULAD, two tasks
fall due by day 27 in only one of the 22 runs. A task-only rule would be silent almost everywhere. Which decisions does
all this feed? [click]
**Sources:** [M5 §2.1; §3; App III Table A.8]

## Slide 13 – Three decisions, three levels of evidence   [2 Decision needs D1–D3]   [Line: main]
**Lead:** The more a decision is reversible, the less evidence it needs: D1 can start with the checked rule, D3 needs a pilot and legal approval.
**On the slide:** Table [M5 §2.1; App II Table A.3] (decision – owner – kind – evidence needed): D1, whom to contact at
each review point – lecturers, lecturer-advisors, support office – operational, repeated, reversible – a list that
reaches more later non-completers than the early-sign rule on a list of the same length; every name checked by staff ·
D2, where to place support time each semester – program manager – management, reversible next semester – a pattern
that repeats over semesters · D3, whether to extend the approach and link data routinely – leadership, legal staff,
data office – strategic, close to irreversible – pilot results and legal approval.
**Visual:** a ladder or gradient from "reversible, frequent" (D1) to "near one-way" (D3), each rung naming its evidence
(comparison).
**Speaker notes:** Now the goal serves three decisions, and they need very different amounts of evidence. D1, whom to
contact at each review point, happens every few weeks and is easy to reverse: if a contact does not help, you try
another. So D1 can start with the simple early-sign rule, checked by a person. D2, where the program manager puts
support time, moves scarce staff, so it needs a pattern that repeats over semesters, not one bad term. D3, whether to
extend the approach and link data routinely, changes the university's data practice and students' trust. That is close
to a one-way door, so it needs pilot results and legal approval. Keep this ladder in mind; it decides how strongly we
can phrase every finding later. Next: the questions that feed these decisions. [click]
**Sources:** [M5 §2.1; App II Table A.3]

## Slide 14 – Four analytical questions   [3 Analytical questions and levels]   [Line: main]
**Lead:** Four questions, one per analytics level, all on one unit, a student's enrolment in one module run, supply the evidence D1–D3 need.
**On the slide:** Table [M5 §3 Table 3.1] (question – level – decision): AQ1, descriptive: what share of enrolments
end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss a
task – D2, D3 · AQ2, diagnostic (association only): which signs by the end of week 4 go with later non-completion,
within module – D2; reasons in D1 · AQ3, predictive: how well non-completion is estimated at weeks 2 and 4 against
the early-sign rule, built on 2013, applied to 2014 – D1 · AQ4, prescriptive (ranking under capacity): who ranks first
on a list of assumed capacity, with what gain over a random list, overall and by deprivation band and disability – D1.
· Key: D1 whom to contact; D2 where support time goes; D3 whether to extend.
**Visual:** a four-step ladder, descriptive → diagnostic → predictive → prescriptive, each step labelled with its
decision (sequence).
**Speaker notes:** From decisions to questions. We ask four, one per analytics level, and all on the same unit: one
student's enrolment in one module run. AQ1 is descriptive: what share of enrolments end in pass, fail or withdrawal,
and in which week non-completers first miss a task. That serves the program manager and leadership. AQ2 is diagnostic:
which signs by the end of week 4 go with later non-completion, compared within each module. It gives reasons for the
contact list. AQ3 is predictive: can a model built on 2013 estimate non-completion in 2014 better than the early-sign
rule? AQ4 is prescriptive: who goes first on a list of fixed length, and is the list fair across groups? Each answer
can only be read at its own level. Let me say exactly what that means. [click]
**Sources:** [M5 §3 Table 3.1]

## Slide 15 – How each level may be read   [3 Analytics levels]   [Line: detail]
**Lead:** Each answer is read by its level, so a diagnostic answer is an association and a prescriptive answer on observational data is only an option to test.
**On the slide:** Descriptive (AQ1): states what happened. · Diagnostic (AQ2): states an association, never a cause. ·
Predictive (AQ3): states how well an outcome is foreseen on proper validation, on unseen runs. · Prescriptive (AQ4): on
observational data, an option to test [M5 §3; §11]. · Cut-offs on OULAD: day 13 (week-3 list) and day 27 (week-5
list); a semester becomes a module run [M5 §3]. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** four boxes in a row, each with "may claim" and "may not claim" (comparison).
**Speaker notes:** Building on those four questions, here is the reading rule we hold ourselves to. A descriptive
answer says what happened. A diagnostic answer, AQ2, says that a sign and an outcome move together; it never says the
sign causes the outcome. A predictive answer, AQ3, is only as good as its test on data the model has never seen. And a
prescriptive answer from observational data, AQ4, is an option for someone to try, not a proven remedy. On OULAD a
semester becomes a module run, and the two review points become cut-offs at day 13 and day 27. We repeat this rule
whenever we show a result, because the strongest temptation in this project is to read an association as a cause.
Were the questions themselves good enough? [click]
**Sources:** [M5 §3; §11]

## Slide 16 – Quality check of the questions   [3 AQ quality check]   [Line: detail]
**Lead:** All four questions are clear, specific, scoped and data-oriented; they differ only in how far the data can answer them.
**On the slide:** Five criteria [M5 §3.1]: clear (asks one thing) · specific (names its measure and groups) · scoped
(fixes population and period) · data-oriented (names its data) · answerable (the data can settle it). · Result: AQ1
(descriptive) all five met; AQ2 (diagnostic) all five met, association only; AQ3 (predictive) answerable by design, not
yet run; AQ4 (prescriptive ranking) ranking answerable, contact has no data [M5 §3 Table 3.1].
**Visual:** a 4 × 5 check grid, with the "answerable" column shaded differently for AQ3 and AQ4 (table).
**Speaker notes:** The course brief asks every question to pass five checks: clear, specific, scoped, data-oriented and
answerable. Clear means it asks one thing. Specific means it names its measure and groups. Scoped means a fixed
population and period. Data-oriented means it names its data, and answerable means those data can settle it. In their
final wording all four questions pass the first four checks. The difference is in the last one. AQ1 and AQ2 are
answered. AQ3 is answerable by a design that has not yet run. And for AQ4, only the ranking is answerable, because no
dataset records a contact, so we deferred the contact part rather than fill it with assumptions. These wordings were
not where we started. [click]
**Sources:** [M5 §3.1; §3 Table 3.1; App III Table A.4]

## Slide 17 – From Milestone 1 to the final questions   [3 AQ revision status]   [Line: main]
**Lead:** Every question kept its core, and each change traces to something the data lacked.
**On the slide:** Table [M5 §3.2 Table 3.2] (at Milestone 1 → final, action, status): AQ1 (descriptive): by course,
delivery mode and year of study → by module, run, start month, year; modify (no mode or year field); answered · AQ2
(diagnostic): signs incl. attendance, across modes and years → signs by week 4, within module; modify (no attendance);
answered · AQ3 (predictive): against a two-task rule → against the early-sign rule, 2013 to 2014; modify (rule needs
activity); deferred · AQ4 (prescriptive): list, order and contact, precision of at least 50% → ranking under capacity,
by group; modify and defer (no contact data); deferred. · No question dropped.
**Visual:** before → after arrows per question, with the reason on each arrow (comparison).
**Speaker notes:** So where did the questions start? In Milestone 1, AQ1 compared delivery modes and years of study.
OULAD has neither, so AQ1 now compares modules, runs, start months and years. AQ2 included attendance at in-class
sessions; OULAD has no classes, so attendance went, and signs are compared within module. AQ3 used to beat a two-task
rule; as we saw, tasks fall due too rarely, so it now beats the early-sign rule, with 2013 for building and 2014 for
testing. AQ4 wanted to choose the contact and reach a precision of at least 50 percent. No data record contacts, so it
became a ranking under capacity, and the contact part waits for the pilot. Nothing was dropped. The precision limit
deserves its own slide. [click]
**Sources:** [M5 §3.2 Table 3.2; App III Tables A.5, A.6]

## Slide 18 – What the data forced us to change   [3 AQ revision status]   [Line: detail]
**Lead:** Four changes recorded in the change log came straight from the data: the day-14 population, the activity part of the rule, gain over chance instead of a precision floor, and one rule for OULAD and the pilot.
**On the slide:** [M5 App III Table A.8] · Population: "enrolled after add-drop" → still registered at day 14, since
OULAD registration closes two weeks after the start; 58 enrolments registered after day 14, so one rule for every
population. · Early-sign rule: tasks only → tasks or no activity in the last seven days; two or more tasks fall due by
day 27 in 1 of 22 runs. · List quality: precision of at least 50% → lift over the run's base rate and normalised
recall; non-completion is 45.3% at day 13 and 44.2% at day 27, so a random list already reaches about 45% precision. ·
One rule: the same early-sign rule for secondary KPI 1 (key performance indicator) and the AQ3 comparison, on OULAD and
in the pilot. · Key: lift = share of non-completers on the list ÷ run's base rate (1 = chance); normalised recall =
recall at capacity ÷ the most a list of that length can reach. · Key: OULAD = Open University Learning Analytics Dataset; AQ3 = predictive question (model against the early-sign rule).
**Visual:** four before/after cards, each with its data reason in small type (comparison).
**Speaker notes:** Following from the revision log, four changes matter most. First, the population. "Enrolled after
add-drop" becomes "still registered at day 14", because OULAD's registration closes two weeks in; and since 58
enrolments registered later, one dated rule now defines every population. Second, the rule gained its activity part,
as you saw. Third, the precision floor. Milestone 1 asked for at least 50 percent precision. But about 45 percent of
students do not complete anyway, so even a random list is nearly there. A floor like that rewards nothing. We judge a
list by lift, its gain over chance, and by normalised recall, the share of non-completers it reaches out of the most a
list that long could reach. Fourth, one rule everywhere. Now, where do the questions point? [click]
**Sources:** [M5 App III Table A.8; §3]

## Slide 19 – Questions mapped to decisions   [3 Decision supported]   [Line: detail]
**Lead:** Each decision draws on a different question: D1 on the list and its reasons, D2 on patterns, D3 on a measurement method.
**On the slide:** D1 (whom to contact): AQ3 and AQ4 give the list and its order; AQ2 gives the reason beside each name.
· D2 (where to place support time): AQ1 and AQ2, with the primary KPI (key performance indicator). · D3 (whether to
extend): AQ1 and the KPIs for pilot and comparison courses [M5 App II Table A.3]. · Key: AQ1 descriptive, AQ2
diagnostic, AQ3 predictive, AQ4 prescriptive ranking.
**Visual:** a bipartite diagram, questions on the left, decisions on the right, lines between them (structure).
**Speaker notes:** To close the question part, here is how the four questions plug into the three decisions. D1, whom
to contact, needs the list and its order, which come from AQ3 and AQ4, and a reason beside each name, which comes from
AQ2. D2, where the program manager places support time, draws on AQ1 and AQ2 and on the completion KPI. And D3, whether
to extend, needs AQ1's way of counting completion and the KPIs, measured in pilot and comparison courses. So the two
questions we could answer serve D2 and the reasons part of D1, while the ordering part of D1 waits on the questions we
designed. Quick checkpoint: problem, goal, questions. Now the data. What did we need before we looked? [click]
**Sources:** [M5 App II Table A.3; §3 Table 3.1]

## Slide 20 – Data requirements, stated first   [4 Data requirements]   [Line: main]
**Lead:** We wrote the requirements in the university's terms before searching, so that the data would fit the questions and not the reverse.
**On the slide:** Unit: one student's enrolment in one course and semester. · Population: enrolled after add-drop. ·
Outcome: final result with a dated withdrawal. · Time: each list uses only data recorded up to its cut-off, one week
before the list; every event needs a timestamp. · AQ–Data Requirement Matrix [M5 §4 Table 4.1]: AQ1 (descriptive) –
identifiers, enrolment dates, final result, dated withdrawal, task dates – four semesters, week · AQ2 (diagnostic) –
plus dated activity, missed and late tasks – weeks 1–4, day · AQ3 (predictive) – timestamped activity and
submissions, background at enrolment – weeks 2 and 4, runs in time order · AQ4 (prescriptive ranking) – AQ3 output,
capacity (assumed), contact record (to create) – each review point. · Contact record declared a gap before the search.
**Visual:** the requirement matrix as a four-row table, with the time column highlighted (table).
**Speaker notes:** Second part, the data. We did something on purpose here: we wrote the requirements before we
searched, in the terms of the university's own records. The unit is one student in one course and semester. The
population is everyone enrolled after add-drop. The outcome is the final result, with a dated withdrawal. And the
strict one: each list may only use data recorded up to its cut-off, so every event needs a timestamp. The matrix shows
what each question adds. AQ1 needs results and task dates; AQ2 adds dated activity; AQ3 needs timestamped activity and
submissions in runs ordered by time; AQ4 needs a capacity and a contact record. We declared that contact record a gap
before searching. Those needs became pass-or-fail gates. [click]
**Sources:** [M5 §4 Table 4.1; App IV Table A.9]

## Slide 21 – Six must-have gates   [4 Data requirements]   [Line: detail]
**Lead:** Six gates decided first and scores only informed, so a dataset that failed any gate was out whatever its total.
**On the slide:** Gates [M5 §4]: a dated outcome · dated tasks · dated activity · at least three time-ordered runs · an
open licence with provenance · a persistent anonymised identifier. · Rule: gates decide, scores inform. · Scoring: each
candidate scored 0 to 2 on the brief's ten criteria, total out of 20 [M5 §4.1].
**Visual:** six gate icons in a row, each with a one-line test (structure).
**Speaker notes:** From the requirement matrix came six must-have gates. A dated outcome, so we know when a student
withdrew. Dated tasks and dated activity, so we can build signs before a cut-off. At least three runs in time order, so
a model can be tested on a later run. An open licence with known provenance. And a persistent anonymised identifier,
so the same student can be followed. The rule was simple: gates decide, scores inform. Each candidate also got a score
from 0 to 2 on the brief's ten criteria, out of 20, but a high score could not rescue a dataset that failed a gate.
Let us see what happened to the seven candidates. [click]
**Sources:** [M5 §4; §4.1; App IV]

## Slide 22 – Seven candidates screened   [4 Candidate datasets]   [Line: main]
**Lead:** Of seven candidate datasets, only OULAD passed every gate, because it alone records a dated withdrawal, dated submissions and daily clicks.
**On the slide:** Dataset Selection Matrix [M5 §4.1 Table 4.2] (candidate – total of 20 – decision): OULAD (Open
University Learning Analytics Dataset) – 12 – selected, conditional on three facts · UCI 697; UCI 320; UCI 856 (UCI =
University of California, Irvine repository) – 10; 6; 7 – rejected, no dated outcome, tasks or activity (320 and 856
also too few runs) · XuetangX; HarvardX (MOOC data) – 8; 8 – rejected, no dated outcome or tasks, no open licence ·
xAPI-Edu-Data – 4 – rejected, fails four gates. · Key: MOOC = massive open online course.
**Visual:** a horizontal bar chart of totals out of 20, bars of rejected candidates greyed with the failed gate named;
the OULAD bar in the accent colour (comparison). Key on the slide: bar = total score; grey = failed at least one gate.
**Speaker notes:** In Milestone 2 we searched repositories, among them the UCI repository of the University of
California, Irvine, with keywords taken from the requirements, and kept seven candidates. Look at the bars. OULAD
scored 12 out of 20. That is modest, and one UCI dataset scored 10, close behind. But the grey bars all fail the first
gate: none of them records when a student withdrew. The UCI sets hold semester totals or school pupils; the MOOC sets
from XuetangX and HarvardX lack a dated pass or fail and an open licence; xAPI-Edu-Data has no dated records at all.
So OULAD was not chosen because it was easy. It was the only one that could show when a student stopped taking part.
Why only conditionally? [click]
**Sources:** [M5 §4.1 Table 4.2; App IV Table A.10]

## Slide 23 – Why OULAD, and on what condition   [4 Selection rationale]   [Line: detail]
**Lead:** OULAD was chosen for fit with the questions, not ease of access, and only after its files confirmed three facts.
**On the slide:** Why: the only candidate with a final result for each enrolment including dated withdrawal, dated
submissions and daily clicks per page [M5 App IV]. · Not for ease: five candidates scored higher on quality
feasibility [M5 App IV]. · Three conditions checked in the files: results separate pass from fail (confirmed); a
student identifier persists across runs (confirmed); enough runs per module for testing (met for five of seven
modules, those with three or four runs) [M5 §4.1; App IV]. · Consequence: the predictive test covers all 13 runs of
2014. · Limits that come with it: UK distance learning, 2013–2014; modules chosen partly because many students failed
them. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** a three-item checklist with ticks and one partial tick (structure).
**Speaker notes:** Why do we trust a dataset that scored only 12? Because the score counted only what the documentation
stated, and OULAD's documentation leaves facts open. So we made the choice conditional on three facts, and checked them
in the files. Do the results separate pass from fail? Yes. Does a student keep the same identifier across runs? Yes. Is
there enough history per module to test a model on a later run? Partly: five of the seven modules have three or four
runs. That is why the predictive test uses all 13 runs of 2014. The choice brings limits too: these are UK
distance-learning modules from 2013 and 2014, picked partly because many students failed them. Where exactly does our
copy come from? [click]
**Sources:** [M5 §4.1; App IV]

## Slide 24 – Provenance and licence   [4 Provenance and licence]   [Line: detail]
**Lead:** Our copy is a pinned, checksummed version under an open licence, so anyone can rebuild exactly what we analysed.
**On the slide:** Source: OULAD (Open University Learning Analytics Dataset), J. Kuzilek, M. Hlosta and Z. Zdrahal,
Knowledge Media Institute, The Open University. · Version: figshare deposit, doi:10.6084/m9.figshare.5081998.v1,
version 1; accessed 6 November 2026. · Integrity: SHA-256 (Secure Hash Algorithm, 256-bit) checksums of the archive and
each of the seven tables pinned; all matched. · Licence: CC BY 4.0, academic use with attribution. · Privacy:
anonymised by the publisher with k-anonymity, k = 5; we make no attempt at re-identification [M5 §4.1; App IV Table
A.11].
**Visual:** a provenance card (title, version, checksum, licence, privacy) (structure).
**Speaker notes:** A quick word on provenance, because a result is only as reproducible as its input. We use version 1
of the figshare deposit of OULAD, by Kuzilek, Hlosta and Zdrahal at the Open University, accessed on 6 November 2026.
Every file is pinned with a SHA-256 checksum, so a rebuild either matches byte for byte or stops. The licence is CC BY
4.0, which allows academic use with attribution. The data are anonymised by the publisher with k-anonymity at k equals
5, meaning every combination of identifying attributes is shared by at least five students, and we never try to
re-identify anyone. With the source settled, the next part asks what the dataset actually contains. [click]
**Sources:** [M5 §4.1; App IV Table A.11]

## Slide 25 – OULAD at a glance   [5 Dataset description]   [Line: main]
**Lead:** OULAD holds 32,593 enrolments of 28,785 students in 22 runs of seven UK distance-learning modules, each with a final result.
**On the slide:** 22 module runs of seven Open University modules, coded AAA to GGG, 2013 and 2014 · run named by year
and start month: B = February, J = October · days counted from day 0, the start of the run · 32,593 enrolments of
28,785 students · final results: Pass 12,361; Withdrawn 10,156; Fail 7,052; Distinction 3,024 · completion = Pass or
Distinction; non-completion = Fail or Withdrawn [M5 §5]. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** a single stacked bar of the four outcomes with counts labelled; legend on the slide (structure).
**Speaker notes:** Third part: what OULAD contains. It covers 22 runs of seven distance-learning modules of the UK's
Open University, coded AAA to GGG, in 2013 and 2014. A run is one offering of a module, named by year and start month:
B for February, J for October. Time counts in days from day 0, the start of the run. Altogether there are 32,593
enrolments of 28,785 students, and every enrolment has a final result: 12,361 passes, 10,156 withdrawals, 7,052 fails
and 3,024 distinctions. A distinction is a pass with honours, so completion means Pass or Distinction, and
non-completion means Fail or Withdrawn. How are those records organised? [click]
**Sources:** [M5 §5; App V Table A.12]

## Slide 26 – Seven tables and their keys   [5 Tables and keys]   [Line: detail]
**Lead:** Seven tables keyed by module, run and student join without losing a record, from 22 run rows to 10.7 million click rows.
**On the slide:** Table [M5 App V Table A.12] (table – rows – content): courses – 22 – one row per run · assessments –
206 – tasks with type (TMA tutor-marked assignment, CMA computer-marked assessment, exam) and due day · vle – 6,364 –
platform pages · studentInfo – 32,593 – background and final result · studentRegistration – 32,593 – registration and
unregistration day · studentAssessment – 173,912 – each submission with day and score · studentVle – 10,655,280 – daily
clicks per student per page. · Every link between tables holds [M5 §5].
**Visual:** an entity diagram, enrolment table in the centre, arrows to the other six labelled with keys (structure).
**Speaker notes:** Seven tables. In the centre, one row per enrolment, with background attributes and the final
result, and a matching table of registration and unregistration days. Around them: 206 assessed tasks, each a TMA, a
tutor-marked assignment, a CMA, a computer-marked assessment, or an exam, with its due day; 173,912 submissions with
their day and score; 6,364 platform pages; and the big one, 10,655,280 rows of daily clicks per student per page. The
important fact for us: every link between the tables holds. No submission, click or page lacks its parent row, so we
can join for the same student, run and task without losing records. But how is that spread over time? [click]
**Sources:** [M5 §5; App V Table A.12]

## Slide 27 – Coverage over years and runs   [5 Coverage]   [Line: detail]
**Lead:** 2013 holds 9 runs of six modules and 2014 holds 13 runs of all seven, and a task falls due by day 27 in only 16 of the 22 runs.
**On the slide:** 2013: 9 runs, six modules, 13,529 enrolments · 2014: 13 runs, all seven modules, 19,064 enrolments ·
module CCC runs only in 2014 · a task other than the exam falls due by day 27 in only 16 of 22 runs [M5 §5]. · Key:
run = one offering of a module; day 27 = end of week 4.
**Visual:** a module × run grid (7 modules × 4 run slots), cells filled where a run exists, a dot where a task falls
due by day 27 (structure).
**Speaker notes:** Now the coverage, because it shapes everything later. The 9 runs of 2013 cover six modules and
13,529 enrolments. The 13 runs of 2014 cover all seven modules and 19,064 enrolments. Module CCC appears only in 2014,
so anything built on 2013 has never seen it. And look at the dots: a task other than the exam falls due by day 27, the
end of week 4, in only 16 of the 22 runs. In the other six runs, a sign based on tasks cannot fire at all by the
week-5 cut-off. That single fact is half the reason our early-sign rule counts inactivity. Which variables carry the
analysis? [click]
**Sources:** [M5 §5]

## Slide 28 – Key variables   [5 Data dictionary]   [Line: detail]
**Lead:** A short data dictionary names the variables every question rests on, and keeps deprivation band and disability for group checks only.
**On the slide:** Table [M5 §5 Table 5.1] (variable – meaning – questions): final_result – Pass, Distinction, Fail or
Withdrawn – target of all four · code_module, code_presentation – module (AAA–GGG) and run – all four ·
date_registration, date_unregistration – registration and unregistration day from day 0 – populations; withdrawal
timing · assessment_type, date; date_submitted – kind of task (TMA, CMA, exam), due day, submission day – AQ1–AQ3 ·
sum_click, date – clicks on one page in one day – AQ2, AQ3 · num_of_prev_attempts, studied_credits – earlier attempts;
credits studied – AQ2, AQ3 · imd_band, disability – deprivation band of the home area; declared disability – group
checks only. · Key: TMA tutor-marked assignment; CMA computer-marked assessment. · Key: AQ1 = descriptive question (outcome shares and timing); AQ2 = diagnostic question (early signs, association only); AQ3 = predictive question (model against the early-sign rule); AQ4 = prescriptive question (ranking under capacity).
**Visual:** the dictionary table, group-check row shaded (table).
**Speaker notes:** Here are the variables that carry the analysis. The final result is the target of all four
questions. Module and run codes key every table. Registration and unregistration days define who is enrolled at each
cut-off and when someone withdrew. Task type, due day and submission day give missed and late tasks. Daily clicks give
the activity signs. Earlier attempts and credits studied enter the AQ2 model as background. And the last row matters
ethically: deprivation band of the home area and declared disability are used only to check whether results differ
between groups. They are never predictors. The full dictionary goes with the final project package. So how well do
these data fit our questions? [click]
**Sources:** [M5 §5 Table 5.1]

## Slide 29 – AQ–Data Fit Matrix   [5 Requirement–data fit]   [Line: main]
**Lead:** Three questions fit with narrowing and AQ4 lacks its key part, so we modified all four, deferred the contact part, and dropped none.
**On the slide:** Ratings: GREEN data enough · YELLOW narrow the question or its claim · RED key concept, variable or
intervention missing. · Table [M5 §5.1 Table 5.2] (question – fit – missing – action – status): AQ1 (descriptive) –
YELLOW – year of study, delivery mode; exam results in 2 of 7 modules – modify – answered · AQ2 (diagnostic) – YELLOW –
attendance; several-modules sign in 2013 – modify – answered · AQ3 (predictive) – YELLOW – a task-only rule fires in 1
of 22 runs at day 13 – modify – deferred · AQ4 (prescriptive ranking) – RED – contacts, capacity, outcomes after
contact – modify and defer – deferred.
**Visual:** the fit matrix with coloured fit cells; key of the three colours on the slide (table).
**Speaker notes:** In Milestone 3 we rated each question against the data: green if the data are enough, yellow if the
question must be narrowed, red if a key concept is missing. No question is green. AQ1 is yellow: no year of study or
delivery mode, and exam results exist in only 2 of 7 modules, so it uses TMAs and CMAs. AQ2 is yellow: no attendance.
AQ3 is yellow: a task-only rule fires in just one of the 22 runs at day 13, hence the activity part. AQ4 is red: no
contacts, no capacity, no outcome after contact. So we modified all four, deferred AQ4's contact part, and dropped
none. Missing values keep a category and are never imputed; missing variables are never simulated. Which gaps need
the university itself? [click]
**Sources:** [M5 §5.1 Table 5.2; App V Table A.13]

## Slide 30 – Gaps only the university can fill   [5 Gaps; keep / modify / defer]   [Line: detail]
**Lead:** Three parts of the proposal need the university's own records, and we neither impute nor simulate them.
**On the slide:** Needs the university's records [M5 §5.1]: (1) the contact part of AQ4 (prescriptive ranking); (2)
comparisons by year of study, delivery mode or attendance; (3) the contact parts of the secondary KPIs (key performance
indicators). · Handling: missing values keep a category or an indicator and are never imputed; missing variables are
never simulated [M5 §5.1]. · Status: keep the core of every question; modify all four; defer only the contact part;
drop none.
**Visual:** three gap cards with a padlock icon labelled "pilot records" (structure).
**Speaker notes:** Following the fit matrix, three things simply are not in OULAD or any dataset we screened. First,
the contact part of AQ4: who was contacted, by whom, and what happened next. Second, comparisons by year of study,
delivery mode or attendance. Third, the contact parts of the two secondary KPIs. We made one firm decision about these:
we do not invent them. A missing value keeps its own category or indicator, and a missing variable is never simulated,
because invented values would turn assumptions into apparent evidence. Every question keeps its core, and only the
contact part is deferred. That closes the data-fit step. Now: what do these data look like up close, and can we trust
them? [click]
**Sources:** [M5 §5.1; App V Table A.14]

## Slide 31 – Profile of the raw data   [6 Data understanding: distributions, outliers]   [Line: detail]
**Lead:** We profiled all 10.9 million raw rows, and the skew of activity, not errors, decided how counts enter a model.
**On the slide:** Profile of all 10.9 million rows of the seven tables, not a sample; thirteen figures recounted
independently, all thirteen agree [M5 §6]. · Keys: six keyed tables, no duplicate key; no child row without its
parent; only the click table has no key [M5 App VI]. · Activity strongly skewed: median 602 clicks per enrolment;
3,365 enrolments with none; 2,503 beyond the upper fence; one record of 6,977 clicks [M5 §6; App VI]. · Scores: median
80; 45.8% of CMA (computer-marked assessment) scores against 17.4% of TMA (tutor-marked assignment) scores on a multiple
of ten [M5 App VI]. · Decision: counts enter models as logarithms; no value is removed.
**Visual:** a histogram of clicks per enrolment on a log axis, median line labelled 602 and a bar for zero clicks
(distribution).
**Speaker notes:** Fourth part: understanding the data before answering anything. In Milestone 3 we profiled all 10.9
million rows, not a sample, and recounted thirteen of the figures with separate code. All thirteen agreed. The keys are
clean: no duplicate key, and no orphan rows. The real feature of these data is skew. The median enrolment has 602
clicks, but 3,365 have none, 2,503 lie beyond the upper fence, and a single day on one page reaches 6,977 clicks. We
could call those outliers and remove them. We did not. They are real behaviour. Instead, counts enter models as
logarithms, and no value is removed. Now the outcome itself: are the two classes balanced? [click]
**Sources:** [M5 §6; App VI]

## Slide 32 – Outcome balance and its mix   [6 Imbalance]   [Line: detail]
**Lead:** The two outcome classes are close in size, so no resampling is needed, but the mix of fail and withdrawal differs sharply by module.
**On the slide:** Of 28,061 enrolments still registered at day 14: 54.7% completed [M5 §6]. · Non-completion: 45.3%
at day 13 and 44.2% at day 27; 24.9–58.3% between the 22 runs; the smaller class holds at least 92 enrolments in every
run [M5 §6; App VI]. · Mix by module: withdrawal highest in the CCC runs, at 43–46%; GGG has the fewest withdrawals but
the most failures [M5 §6]. · Decision: no resampling or reweighting; AQ1 (descriptive question) reports Fail and
Withdrawn apart. · Key: non-completion = Fail or Withdrawn; run = one offering of a module.
**Visual:** a 100% stacked bar per module (Pass + Distinction, Fail, Withdrawn) with a legend on the slide
(comparison).
**Speaker notes:** Following the profile, the outcome. Among the 28,061 enrolments still registered at day 14, 54.7
percent completed. Non-completion sits at 45.3 percent at day 13 and 44.2 at day 27. That is close to an even split,
and even the smaller class has at least 92 enrolments in every run, so we need no resampling and no reweighting.
Imbalance is not our problem. Mixing is. Non-completion joins two different things, failing and withdrawing, and the
modules differ: in CCC, 43 to 46 percent withdraw, while GGG has the fewest withdrawals and the most failures. That is
why AQ1 reports the two apart. Every number from here on refers to a fixed population, so let us pin those down. [click]
**Sources:** [M5 §6; App VI]

## Slide 33 – The populations behind every number   [6 Data understanding]   [Line: detail]
**Lead:** Each number in this talk refers to one of a few fixed populations, defined by year and by who was still registered at a given day.
**On the slide:** Table [M5 §6 Table 6.1] (population – enrolments – non-completers – used by): all 2013 (9 runs) –
13,529 – 6,959 (51.4%) – AQ1 second denominator · 2013, registered at day 14 – 12,076 – 5,515 (45.7%) – AQ1 primary ·
2013, registered at day 27 – 11,811 – 5,245 (44.4%) – AQ2; AQ3 development · 2013, day 27, 7 runs with a task due –
9,960 – AQ2 task signs · 2014, registered at day 14 – 15,985 – 7,185 (44.9%) – AQ1 primary · 2014 test (13 runs), day
27 – 15,724 – 6,911 (44.0%) – AQ2 replication; AQ3 and AQ4 test. · Key: AQ1 descriptive, AQ2 diagnostic, AQ3
predictive, AQ4 ranking.
**Visual:** the population table, rows grouped by year (table).
**Speaker notes:** This table is a reference for the rest of the talk. A rate is meaningless without its denominator,
so every number we quote belongs to one of these rows. For 2013, the 9 runs hold 13,529 enrolments; 12,076 were still
registered at day 14, the primary denominator of AQ1, with 45.7 percent non-completion. At day 27, 11,811 remain, the
population of AQ2. For 2014, 15,985 enrolments at day 14 with 44.9 percent non-completion, and 15,724 at day 27, which
is both the AQ2 replication and the future test set for AQ3 and AQ4. Note the year split: 2013 develops, 2014 tests.
Now, what can go wrong in these records? [click]
**Sources:** [M5 §6 Table 6.1]

## Slide 34 – Three quality issues that changed the method   [6 Quality: invalids, missingness]   [Line: main]
**Lead:** Of nineteen logged quality issues, three were rated High because ignoring them would change a rate, the target or a feature, and each one changed the method.
**On the slide:** Data Quality Issue Log: nineteen issues; High = would change a rate, the target or a feature; Medium
= would change a measure by a known amount; Low otherwise [M5 §6.1]. · High 1: exam results missing in five modules
(18 of 24 exams without result rows) → tasks mean TMAs (tutor-marked assignments) and CMAs (computer-marked
assessments) only. · High 2: no 2013 run has a task due by day 13, and 7 of 9 have one by day 27 → the early-sign rule
has an activity part. · High 3: seven UK modules of 2013–2014 → scope stated, comparisons within module [M5 §6.1 Table
6.2].
**Visual:** three issue → decision arrows, severity tag "High" on each (structure).
**Speaker notes:** From the profile we built a log of nineteen quality issues, each rated against our questions. High
means ignoring it would change a rate, the target or a feature. Three were High, and each changed the method. First,
exam results are missing in five modules; 18 of 24 exams have no result rows. So a "task" means a TMA or CMA, never an
exam. Second, no 2013 run has a task due by day 13, and only 7 of 9 have one by day 27. A rule on tasks alone would be
blind early on, so the rule counts inactivity. Third, the population is narrow: seven UK modules in two years. So we
state the scope and compare only within module. Two Medium issues could move numbers by a known amount. [click]
**Sources:** [M5 §6.1 Table 6.2; App VI Table A.15]

## Slide 35 – Duplicates, lateness and missing values   [6 Quality: duplicates, missingness, invalids]   [Line: detail]
**Lead:** Medium and Low issues were handled by stated rules, and two of them were turned into sensitivity checks because their size is known.
**On the slide:** Late CMAs (computer-marked assessments): counting them would raise the share the early-sign rule
flags at day 27 from 28.8% to 41.2% → the rule uses TMA (tutor-marked assignment) lateness; late CMAs a sensitivity
run [M5 §6.1]. · Duplicate click rows: 7.39% of click rows; removal would drop 3.19% of all clicks → rows kept, clicks
summed by day, a de-duplicated twin of each click feature [M5 §6.1]. · Activity after unregistration → truncated at
the unregistration day. · Banked results dated −1 → never timed. · Missing deprivation band (1,111), registration day
(45), TMA score (173) → "Missing" group or indicator, no imputation [M5 §6.1 Table 6.2; App VII Table A.20].
**Visual:** a two-column issue → rule table, the two sensitivity checks marked with a flag icon (table).
**Speaker notes:** Below the High issues, every other issue got a stated rule. Two of them could move a number by a
known amount. If a late CMA counted as an early sign, the rule would flag 41.2 percent at day 27 instead of 28.8,
because late CMAs are common and their meaning in 2013 is undocumented. So the rule counts late TMAs, and late CMAs
become a sensitivity run. Duplicate click rows make up 7.39 percent of click rows; dropping them would remove 3.19
percent of all clicks, so we keep them and test a de-duplicated twin. Activity after withdrawal is truncated. Missing
values, such as 1,111 missing deprivation bands, keep their own "Missing" group. Nothing is imputed. Now, time and
representativeness. [click]
**Sources:** [M5 §6.1 Table 6.2; App VI Table A.15; App VII Table A.20]

## Slide 36 – Time coverage and who OULAD represents   [6 Temporal coverage, representativeness]   [Line: detail]
**Lead:** The cut-offs fall in the busiest weeks, the run structure forces a train-2013, test-2014 split, and OULAD represents modules chosen partly because many students failed.
**On the slide:** Weekly clicks peak in week 3, so day 13 and day 27 fall in the weeks of highest activity [M5 §6.2]. ·
Each module has at most one earlier run of the same start month → the only test on a later run is train on 2013, test
on 2014 [M5 §6.2]. · OULAD (Open University Learning Analytics Dataset) represents Open University modules chosen partly
because many students failed them [M5 §6.2]. · Students learn at a distance: 70.4% under 35; 63.1% study 60 credits or
fewer [M5 App VI]. · Consequences: check every result on the university's records before D1–D3 (the three decisions);
compare groups within module; module CCC appears only in the test year. · Key: D1 = whom to contact; D3 = whether to extend the approach.
**Visual:** a weekly click line over the run with day 13 and day 27 marked (trend).
**Speaker notes:** Two time facts shape the design. Weekly activity peaks in week 3, so our two cut-offs, day 13 and day
27, sit in the busiest weeks, when signs are most visible. And each module has at most one earlier run with the same
start month. The only honest way to test a model on a later run, the way the university would use it next semester, is
to build on 2013 and test on 2014. Then representativeness. OULAD students learn at a distance; 70.4 percent are under
35. And the modules were chosen partly because many students failed them. So results describe OULAD, not the
university, groups are compared within module, and every result is re-checked before any of the three decisions. Which
fields need extra care? [click]
**Sources:** [M5 §6.2; App VI]

## Slide 37 – Sensitive fields and privacy   [6 Sensitive fields]   [Line: main]
**Lead:** We keep six sensitive attributes for the fairness audit and out of the predictors, because bias cannot be audited without knowing group membership.
**On the slide:** Six attributes: gender, age band, disability, deprivation band, region, highest education; audit only,
except highest education (a predictor, also audited) [M5 §6.2; App VI Table A.16]. · Why kept: bias cannot be audited
without group membership; a fairness study on OULAD (Open University Learning Analytics Dataset) reproduced a
disparity of five to six percentage points in favour of male students [M5 §6.2]. · Group sizes: declared disability
3,164 enrolments; missing deprivation band 1,111; aged 55 or over 216 [M5 App VI Table A.16]. · Privacy: Vietnam's
Personal Data Protection Law prohibits re-identifying de-identified data, so OULAD is never linked to another source
[M5 §6.2].
**Visual:** a table of the six attributes with a role column (audit / predictor) (table).
**Speaker notes:** Last step of data understanding: the sensitive fields. OULAD holds six: gender, age band,
disability, deprivation band, region and highest education. You might think the safe move is to delete them. It is the
opposite. A model can learn group membership through other fields, so bias cannot be audited unless we keep the
groups. And the risk is real here: a published fairness study on OULAD reproduced a gap of five to six percentage
points in favour of male students. So five of the six stay out of the predictors and serve only the audit; highest
education is a predictor that is audited too. Under Vietnam's data protection law, re-identifying de-identified data is
prohibited, so we never link OULAD to anything. Quick checkpoint: problem, data, understanding. Now preparation. [click]
**Sources:** [M5 §6.2; App VI Table A.16]

## Slide 38 – Three rules that govern preparation   [7 Data preparation]   [Line: main]
**Lead:** Preparation follows three rules: delete or impute nothing, date every feature on or before its cut-off, and learn every parameter from the training runs alone.
**On the slide:** Before any record changed: each issue got a decision, its reason and a validation check that fails
if the decision is not carried out [M5 §7]. · Rule 1: nothing recorded is deleted or imputed in the views. · Rule 2:
every feature uses only events dated on or before its cut-off. · Rule 3: every learned parameter comes from the
training runs alone [M5 §7]. · Pipeline: ten scripted steps, no manual step; 10,655,280 click rows summed into
1,808,119 enrolment-day records; 98,745 clicks after withdrawal left out; 25 joins, each keeping its input rows [M5 App
VII].
**Visual:** a ten-step pipeline strip from raw tables to prepared views, three rule badges above it (sequence).
**Speaker notes:** Fifth part: preparation. In Milestone 3 we built a pipeline that turns the seven raw tables into
views every analysis reads. Before any record changed, each issue received a decision, its reason, and a check that
fails if the decision is not carried out. Three rules govern everything. First, nothing recorded is deleted or
imputed. Second, every feature uses only events dated on or before its cut-off, so nothing from the future leaks in.
Third, every learned parameter comes from the training runs alone. The pipeline has ten scripted steps and no manual
step. For example, 10,655,280 click rows become 1,808,119 enrolment-day records, and all 25 joins keep their input
rows. Here is the decision matrix. [click]
**Sources:** [M5 §7; App VII]

## Slide 39 – Preparation Decision Matrix   [7 Preparation Decision Matrix]   [Line: detail]
**Lead:** Every preparation need has one decision and one check, from the population rule to the train–test split.
**On the slide:** Table [M5 §7 Table 7.1] (need – decision): Population – flags for days 13, 14 and 27; views hold those
enrolled at the cut-off · Missing values – "Missing" category or indicator; no imputation · Duplicates, keys,
integration – every row kept; clicks summed by day; left joins from the enrolments · Invalid values, outliers – labels
corrected; banked results untimed; every value kept · Activity after withdrawal – truncated at the unregistration day ·
Derived features – TMA and CMA tasks; early-sign rule; activity against the run median · Time, encoding – cut-offs at
days 13 and 27; transforms learned on training rows · Sensitive attributes, split – audit columns outside the
predictors; train 2013, test 2014. · Key: TMA tutor-marked assignment; CMA computer-marked assessment.
**Visual:** the decision matrix as an eight-row table (table).
**Speaker notes:** Building on those three rules, this is the decision matrix in full. Each row is one need and its one
decision, and in the report each also has a check. Population: flags for who is enrolled at day 13, 14 and 27.
Missing values: a "Missing" category, never imputed. Duplicates and joins: every row kept, clicks summed by day, left
joins from the enrolment table so nobody drops out. Outliers: kept. Activity after withdrawal: cut. Derived features:
the tasks, the rule and activity against the run's median. Time and encoding: two cut-offs, transforms learned only on
training rows. And the split: 2013 to train, 2014 to test, sensitive columns outside the predictors. Which variables
come out of this? [click]
**Sources:** [M5 §7 Table 7.1; App VII Table A.17]

## Slide 40 – Derived variables and encoding   [7 Derived variables, encoding]   [Line: detail]
**Lead:** We derive activity, task and rule variables dated to each cut-off, giving 19 usable predictors encoded so that a model can handle an unseen module.
**On the slide:** Derived [M5 §7.1; App VII Table A.18]: clicks before and after day 0 · activity against the median of
the same run · no click in the last seven days · missed and late tasks (a task counts as missed only if due on or after
the student's registration day) · the early-sign rule. · Primary set: 19 usable predictors, 23 parameters once module
and start month are coded [M5 §7.1]. · Set aside: mean CMA (computer-marked assessment) mark, known for only 1.4% of
training rows at day 13 and 5.2% at day 27, below the 10% coverage required [M5 App VII]. · Encoding: counts as
log(1 + count); every transform refitted inside each development fold; module terms deviation-coded so an unseen
module gets the average effect [M5 §7.1].
**Visual:** a worked example: one enrolment's raw rows → its derived variables at day 27 (worked example).
**Speaker notes:** From those decisions come the variables. Clicks before and after the start. Activity compared with
the median student of the same run up to the same day. No click in the last seven days. Missed and late tasks, where a
task only counts as missed if it fell due after the student registered, so late joiners are not punished. And the rule
itself. The primary set holds 19 usable predictors, 23 parameters once module and start month are coded. We set aside
the mean CMA mark: it was known for only 1.4 percent of training rows at day 13. Module terms are coded so that a module
never seen in training, like CCC, receives the average effect. The biggest risk in all this is leakage. [click]
**Sources:** [M5 §7.1; App VII Table A.18]

## Slide 41 – Leakage control   [7 Leakage control]   [Line: main]
**Lead:** Leakage, using information that would not exist at the moment of prediction, is blocked four ways, and our main check is built so that it can fail.
**On the slide:** Definition: leakage = use of information that would not exist at the moment of prediction [M5 §7.1].
· Controls: (1) timing rule: activity after the cut-off, the withdrawal day, the final result and TMA (tutor-marked
assignment) marks never enter a feature; (2) parameters learned on 2013 alone; (3) split by year; (4) 1,586 test
enrolments at day 27 of students seen in 2013 flagged [M5 §7.1]. · The check can fail: recounting click features
without the date filter changes them only for the enrolments that clicked after the cut-off, 26,755 at day 13 and
25,663 at day 27 [M5 App VII].
**Visual:** a timeline with the cut-off line; everything right of it greyed "never used" (sequence).
**Speaker notes:** Following the variables, leakage. Leakage means using information that would not exist when the
prediction is made; it makes a model look better on paper than it can ever be in use. We block it four ways. A timing
rule: nothing after the cut-off, no withdrawal day, no final result, and no TMA marks, because the data never say when
a mark was released. Parameters learned on 2013 only. A split by year. And 1,586 test enrolments of students already
seen in 2013 are flagged. Most important, our check can fail. Remove the date filter, and the click features change for
exactly the 25,663 enrolments that clicked after day 27, and no others. So, what did the pipeline deliver? [click]
**Sources:** [M5 §7.1; App VII Table A.19, Table A.20]

## Slide 42 – Final versioned dataset   [7 Final versioned dataset]   [Line: main]
**Lead:** The result is one versioned dataset that passes every validation check and rebuilds byte for byte from the pinned download.
**On the slide:** Name: OULAD-N04-prepared-1.0 [M5 §7.2]. · All 22 validation checks pass; the 32,593 enrolments and
their outcome mix unchanged [M5 §7.2]. · Six features recomputed from raw by separate code: 0 differences in 55,604
feature rows [M5 §7.2]. · A data dictionary documents each of the 88 prepared variables with source, transformation,
role and sensitivity [M5 §7.2]. · One command rebuilds the views from the pinned figshare download, byte-identical; CC
BY 4.0 allows sharing with attribution [M5 §7.2]. · Synthetic data only in unit tests, never in a view, statistic or
finding. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** a before → after check table: enrolments 32,593 → 32,593; outcome mix identical; features 0 differences
(comparison).
**Speaker notes:** Here is what preparation delivered: one versioned dataset, OULAD-N04-prepared-1.0. All 22 validation
checks pass. The 32,593 enrolments and their outcomes are exactly as in the raw data; nothing was dropped. Six features
were recomputed from the raw files by separate code, and in 55,604 feature rows, there were zero differences. A data
dictionary documents all 88 prepared variables: where each comes from, how it was transformed, its role, and how
sensitive it is. One command rebuilds the views from the pinned download, byte for byte. And synthetic data appear
only in unit tests, never in a finding. Quick checkpoint: problem, data, preparation. Now the method: what do we do
with each question? [click]
**Sources:** [M5 §7.2; App VII Table A.20]

## Slide 43 – Purpose decides the method   [8 Modeling and analysis strategy]   [Line: main]
**Lead:** Each question's purpose fixes how its result may be read, and a ranked list is needed because the rule flags more students than staff can contact.
**On the slide:** Designed at Level 1 in Milestone 4, without training any model [M5 §8]. · Explanatory power does not
imply predictive power, so AQ2 (diagnostic) is never read as cause and AQ3 (predictive) and AQ4 (prescriptive ranking)
must be judged on unseen runs [M5 §8]. · Why a ranking: the early-sign rule names 28.8% of enrolments at day 27, more
than a list of 15% or 25% of a run can hold (3 or 5 contacts per 20 students); no data record a contact [M5 §8]. ·
Four tasks: AQ1 (descriptive) aggregation · AQ2 association within module run · AQ3 binary classification at days 13
and 27 · AQ4 ranking under a fixed capacity [M5 §8].
**Visual:** a bar comparing the rule's 28.8% flagged share with list capacities of 15% and 25% (comparison).
**Speaker notes:** Sixth part, the method. We designed it in Milestone 4 at Level 1, the compulsory level, without
training a model. The first principle: purpose decides reading. A regression used to describe associations explains;
it does not predict, and explaining well does not mean predicting well. So AQ2 is never read as a cause, and AQ3 and
AQ4 must prove themselves on runs they have never seen. Second, why rank at all? Look at the bars. At day 27 the rule
flags 28.8 percent of students. Staff can contact 3 or 5 per 20, that is 15 or 25 percent. The rule names more people
than staff can reach, so someone must decide the order. That gives four tasks. Here are the methods for the first two.
[click]
**Sources:** [M5 §8; App VIII Table A.22]

## Slide 44 – Method selection: AQ1 and AQ2   [8 Method Selection Matrix]   [Line: detail]
**Lead:** AQ1 needs no model, only grouped rates with intervals, and AQ2 needs a within-module association model with no causal claim.
**On the slide:** Model and Method Selection Matrix, part 1 [M5 §8.1 Table 8.1]: AQ1 (descriptive) – aggregation and
rate comparison – baselines: pooled rate; rate over all enrolments; rate without flagged enrolments – primary: grouped
rates with Wilson intervals, cumulative first missed week by outcome, year difference with Newcombe interval –
rationale: no model needed; the denominator decides the rate · AQ2 (diagnostic) – association within module run –
baseline: unadjusted rate difference per sign – candidates: logistic regression with run fixed effects and sign ×
module terms; mixed-effects logistic regression – primary: the fixed-effects logistic, robust standard errors, effects
as average risk differences with odds ratios beside them – rationale: every run is observed; 6 modules are too few for
a random effect; no causal claim. · Key: fixed effects = students compared only within the same run.
**Visual:** the two matrix rows written out, primary proposal column highlighted (table).
**Speaker notes:** Building on those tasks, the selection matrix, first half. Each candidate was judged on the course's
eight criteria, and ties went to the simpler, more interpretable method. AQ1 is descriptive, so it needs no model:
grouped rates with Wilson intervals, the week of the first missed task, and a year difference with a Newcombe interval.
The baselines are other denominators, because the denominator decides the rate. AQ2 compares students within each run,
so we chose logistic regression with a fixed effect per run and sign-by-module terms. We rejected a random effect,
since six modules are too few. Effects are reported as average risk differences in percentage points, with odds ratios
beside them. And no causal claim. Now the two designed questions. [click]
**Sources:** [M5 §8.1 Table 8.1; App VIII]

## Slide 45 – Method selection: AQ3 and AQ4   [8 Method Selection Matrix]   [Line: detail]
**Lead:** AQ3 proposes an interpretable penalised logistic model that must beat the early-sign rule, and AQ4 a top-k list per run with the signs behind each name.
**On the slide:** Model and Method Selection Matrix, part 2 [M5 §8.1 Table 8.1]: AQ3 (predictive) – binary
classification at day 13 and day 27 – baselines: early-sign rule ranked by its number of signs; background-only
logistic model; random list – candidates: penalised logistic regression; gradient-boosted trees; discrete-time
survival as an extension – primary: penalised logistic on the 19 primary predictors (23 parameters), unless a
challenger wins by a margin fixed in advance – rationale: interpretable reasons for staff; about 230 non-completers per
parameter; transfer to a later run · AQ4 (prescriptive ranking) – ranking under a fixed capacity – baselines: random
list; rule-ranked list of the same length – primary: top-k per run from the AQ3 scores, with the signs behind each name
– rationale: capacity is fixed; no contact data, so no ranking by expected benefit; staff decide. · Status: proposals,
no model metric.
**Visual:** the two matrix rows, with a "designed, not run" stamp (table).
**Speaker notes:** Now the second half, the two designed questions. For AQ3 the baselines matter most: the early-sign
rule ranked by its number of signs, a model using background only, and a random list. The primary proposal is a
penalised logistic regression on 19 predictors. Why not boosted trees first? Because staff need a reason beside each
name, and with about 230 non-completers per parameter a simple model is well supported. Trees can still win, but only
by a margin fixed in advance. AQ4 takes the AQ3 scores and lists the top k in each run, with the signs behind each
name. It cannot rank by expected benefit, because nobody recorded a contact. Both are proposals; no model metric
exists. So how would we judge them? [click]
**Sources:** [M5 §8.1 Table 8.1; App VIII]

## Slide 46 – Capacity and the list metrics   [9 Evaluation design: metric]   [Line: main]
**Lead:** A list is judged by how many later non-completers it reaches at a fixed length, scaled by the most that length could reach.
**On the slide:** Capacity k: 3 or 5 contacts per 20 students; main operating point 5 per 20 at day 27 [M5 §9]. ·
Recall at capacity: share of a run's non-completers on the list. · Normalised recall: recall at capacity ÷ the most a
list of length k can reach; the ceiling ranges from 46% to 100% between training runs [M5 §9]. · Lift: share of
non-completers on the list ÷ the run's base rate; 1 means chance [M5 §9; Glossary]. · Framework: TRIPOD+AI (reporting
guideline for prediction models, updated for AI): discrimination, calibration, usefulness for the decision [M5 §9].
**Visual:** a worked example in symbols, no data: a run with N students and m non-completers, a list of length k; the
ceiling is min(k, m) ÷ m; normalised recall = non-completers on the list ÷ min(k, m) (worked example).
**Speaker notes:** Seventh part, evaluation. It was fixed in Milestone 4, before any code ran. Staff capacity sets the
list length: 3 or 5 contacts per 20 students, and the main point is 5 per 20 at day 27. Recall at capacity is the share
of a run's non-completers who make it onto the list. But a short list cannot reach everyone. In some training runs a
perfect list would reach only 46 percent, in others 100. So we divide by that ceiling: normalised recall. The diagram
shows the idea in symbols: listed non-completers over the most the list could hold. Lift adds the view against chance. The frame is TRIPOD+AI, a
reporting guideline for prediction models: discrimination, calibration, and usefulness for the decision. Here is the
full plan. [click]
**Sources:** [M5 §9; Glossary]

## Slide 47 – Evaluation Plan   [9 Evaluation design]   [Line: main]
**Lead:** Each question has a primary metric, a baseline, a validation and a success criterion fixed before any result existed.
**On the slide:** Table [M5 §9 Table 9.1] (question – metric – baseline – validation – success criterion): AQ1
(descriptive) – rates with 95% intervals – pooled rate; other denominators – two independent aggregation paths – both
agree to the enrolment, every rate with denominator and interval · AQ2 (diagnostic) – average risk difference within
module run, 95% interval – unadjusted difference – 2013, sensitivity runs, replication on 2014 – at least 5 points,
interval excluding 0, same direction in at least two-thirds of modules · AQ3 (predictive) – normalised recall at
capacity, day 27, 5 per 20 – rule-ranked list; background-only model; random list – leave-one-run-out folds in 2013;
one logged test on 13 runs of 2014 – gate S1 · AQ4 (prescriptive ranking) – normalised recall at capacity – random;
rule-ranked – as AQ3 – gate S1 and fairness rule FR1. · Key: S1 = the model must beat the rule list; FR1 = fairness
review rule (both defined on the next slides).
**Visual:** the four-row plan table, success column bold (table).
**Speaker notes:** Following the metrics, here is the whole plan on one table. AQ1 succeeds if two independent ways of
counting agree to the single enrolment and every rate carries its denominator and interval. AQ2 succeeds for a sign if
its adjusted risk difference is at least 5 points, its interval excludes zero, and it points the same way in at least
two-thirds of the modules. AQ3 has one gate, which we call S1: the model must beat the rule's list. It is developed on
2013 with each run held out in turn, and tested once on 2014. AQ4 must pass the same gate plus a fairness review rule,
FR1. Let me unpack the AQ2 threshold first, because we have results for it. [click]
**Sources:** [M5 §9 Table 9.1]

## Slide 48 – The AQ2 success criterion   [9 Success criterion]   [Line: detail]
**Lead:** A sign counts as a consistent association when its adjusted difference is at least 5 points, its interval excludes 0 and its direction holds in two-thirds of modules; p-values play no part.
**On the slide:** Criterion for AQ2 (diagnostic question): mutually adjusted risk difference ≥ 5 percentage points ·
95% interval excludes 0 · same direction in at least two-thirds of the modules where the sign is defined [M5 §9; App
XIII]. · Why 5 points: the smallest gap worth staff attention, a convention fixed in Milestone 4, lenient at a base rate
near 44%, so the size of each estimate distinguishes the signs [M5 §9.1]. · Why no p-values: a p-value does not measure
the size of an effect [M5 §9.1]. · Key: risk difference = difference in later non-completion between enrolments with
and without a sign, averaged within module run.
**Visual:** a number line from 0 to 45 points with the 5-point threshold marked (structure).
**Speaker notes:** Zooming in on AQ2's criterion. A sign counts as a consistent association if three things hold. Its
risk difference, adjusted for the other signs, is at least 5 percentage points. Its 95 percent interval excludes zero.
And it points the same way in at least two-thirds of the modules where it is defined. We chose 5 points in Milestone 4
as the smallest gap worth a lecturer's attention. We admit it is lenient when the base rate is near 44 percent, so the
size of each estimate, not the pass, is what tells the signs apart. And p-values take no part, because a p-value does
not measure how big an effect is. Now the stricter design, for AQ3. [click]
**Sources:** [M5 §9; §9.1; App XIII]

## Slide 49 – Validation design for AQ3   [9 Split and validation]   [Line: detail]
**Lead:** Development uses leave-one-run-out folds on 2013, a challenger must win by a margin fixed in advance, and the frozen model meets 2014 only once.
**On the slide:** Development: leave-one-run-out folds on the 9 runs of 2013; every learned step refitted inside each
fold [M5 §9.1]. · Challenger rule: replaces the primary only with a gain of at least 0.03 in pooled normalised recall
(about 89 more non-completers listed over the 9 runs) and a gain in 7 of 9 folds [M5 §9.1; App IX]. · Two freezes, one
test: question, splits, metrics, baselines fixed before training; final model fixed before testing; scored once on the
13 runs of 2014 [M5 App IX]. · Test reported apart: 9 paired runs (10,801 enrolments at day 27) and 4 unpaired runs
(4,923) [M5 App IX]. · Fold results choose between candidates only; never reported as performance. · Key: AQ3 = predictive question (model against the early-sign rule).
**Visual:** a timeline: 2013 folds → freeze 1 → model choice → freeze 2 → single 2014 test (sequence).
**Speaker notes:** Following the AQ2 criterion, the AQ3 design is stricter, because a predictive claim lives or dies on
unseen data. On 2013 each run is held out in turn, and every step that learns, filling, scaling, tuning, is redone
inside each fold. A challenger like boosted trees replaces the simple model only if it gains at least 0.03 in
normalised recall, about 89 more non-completers over the 9 runs, and wins in 7 of 9 folds. That margin was fixed before
any fold result existed. Then two freezes and one test: the model is frozen, and only then scored, once, on the 13 runs
of 2014. Nine of those runs have a 2013 twin; four test transfer to something new. So what must the model achieve?
[click]
**Sources:** [M5 §9.1; App IX]

## Slide 50 – Gate S1 and the calibration condition   [9 Success criterion]   [Line: main]
**Lead:** One gate decides: the model must reach more non-completers than the rule's list of the same length on all 13 test runs, and probabilities are shown only if calibration holds.
**On the slide:** Gate S1 (single success criterion of AQ3): on all 13 test runs, day 27, 5 per 20, the model's pooled
normalised recall would have to exceed the rule-ranked list's, with the 95% paired two-level bootstrap interval of the
difference above 0 and a one-sided sign-flip test on the 13 per-run differences with p below 0.05 [M5 App IX Table
A.23]. · No minimum gain size; a pass would be reported with the number of extra non-completers listed. · S2,
precision at capacity: reported, not a gate. · S3, calibration: calibration-in-the-large between −0.2 and 0.2 and slope
between 0.8 and 1.2; otherwise staff see ranks and reasons only [M5 App IX Table A.23]. · Key: AQ3 = predictive question (model against the early-sign rule).
**Visual:** a decision diagram: model list vs rule list → S1 pass → model order; fail → rule order (structure).
**Speaker notes:** Here is the gate. We call it S1, the single success criterion of AQ3. On all 13 test runs, at day
27, with 5 per 20, the model's normalised recall must beat the rule's list. Beat means the bootstrap interval of the
difference sits above zero and a sign-flip test across the 13 runs gives p below 0.05. If the model fails, the rule's
order stays. That is an acceptable outcome, not a failure of the project. There is a second condition, S3, for showing
probabilities: calibration-in-the-large between minus 0.2 and 0.2 and a slope between 0.8 and 1.2. Otherwise staff see
ranks and reasons only. Precision, S2, is reported but decides nothing. Next, the fairness rule. [click]
**Sources:** [M5 §9; App IX Table A.23]

## Slide 51 – Fairness audit and rule FR1   [9 Fairness check]   [Line: main]
**Lead:** The audit asks one thing, equal recall at capacity across groups, and rule FR1 sends a group for human review when its recall falls clearly more than 10 points behind.
**On the slide:** Criterion: separation, measured as equal recall at capacity across groups [M5 §9.2; App IX]. · Rule
FR1 (fairness review rule): flag a group for human review when its recall at capacity is more than 10 points below the
other students' and the Holm-adjusted one-sided interval of the gap lies below 0 [M5 §9.2]. · Confirmatory groups (test
enrolments at day 27): declared disability 1,488 · most deprived band, 0–10% 1,486 · missing deprivation band 610 [M5
§9.2; App IX Table A.24]. · Aged 55 or over: 118, gap reported, "insufficient data, not cleared". · No flag means no
evidence of a gap at that precision, not that the list is fair. · Origin: the ten-point gap carries Milestone 1's limit
on first-year against later-year recall, moved to groups OULAD records. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** the three groups as bars of test enrolments, with a dashed "10-point" review line on a gap axis (structure).
**Speaker notes:** From accuracy to fairness. With different base rates across groups, not every fairness criterion can
hold at once, so we chose one: equal recall at capacity. A struggling student should have the same chance of being
listed, whatever the group. Rule FR1 flags a group when its recall is more than 10 points below everyone else's and the
adjusted interval confirms the gap. A flag triggers human review, not automatic rejection. Three groups are large
enough: declared disability, 1,488 test enrolments; the most deprived band, 1,486; and the missing band, 610. Students
aged 55 or over, 118, are too few, so they are marked "not cleared". And no flag only means no evidence of a gap. What
else protects the evaluation? [click]
**Sources:** [M5 §9.2; App IX Table A.24]

## Slide 52 – Leakage and interpretability in the evaluation   [9 Leakage, interpretability]   [Line: detail]
**Lead:** No 2014 outcome enters any AQ3 choice, and each listed student's reasons come from the same model that ranks them, never read as causes.
**On the slide:** Leakage in evaluation [M5 §9.2; App IX]: predictors, candidates, selection rule and gate fixed in
Milestone 4 on 2013 alone · every learned step refitted inside each fold · fold results used only to choose, never
reported as performance. · Interpretability: each listed student's reasons come from the same model that ranks the
student; no coefficient read as a cause; the model would carry a model card and its data a datasheet [M5 §9.2]. · Key:
AQ3 = the predictive question; fold = one 2013 run held out in development.
**Visual:** a mock list row: rank, name placeholder, three sign chips as reasons (worked example).
**Speaker notes:** Two last protections. On leakage: the predictors, the candidates, the rule for choosing between them
and the gate were all fixed in Milestone 4, on 2013 alone. No 2014 outcome touches any of those choices. Fold results
are used to choose, never reported as performance, because a score that guided a choice flatters the chosen model. On
interpretability: the mock row shows what a lecturer would see, a name and the signs behind it. Those reasons come from
the same model that ranks the student, and no coefficient is read as a cause. The model would ship with a model card
and its data with a datasheet. That is the design. So what did we actually run? [click]
**Sources:** [M5 §9.2; App IX]

## Slide 53 – Experimental status   [10 Experimental status]   [Line: main]
**Lead:** We completed Level 1, the compulsory level, and specified Level 2 in full but did not run it, to keep the 2014 runs as one clean test.
**On the slide:** Done: Level 1, the modeling strategy and the evaluation design [M5 §10]. · Not run: the optional
Level 2 prototype for AQ3 (predictive) and AQ4 (prescriptive ranking); no model metric, chart or confusion matrix
exists [M5 §10]. · Why: Level 2 is optional, and the 13 runs of 2014 are the only independent test, which we keep for
one complete run of the frozen protocol [M5 §10]. · AQ1 and AQ2 are not the prototype: they train no predictive model,
and describing 2014 changes nothing in the AQ3 design fixed on 2013 [M5 §10]. · Key: AQ1 = descriptive question (outcome shares and timing); AQ2 = diagnostic question (early signs, association only).
**Visual:** a status bar: Level 1 complete; Level 2 specified, not run (structure).
**Speaker notes:** Eighth part, and an honest one. We completed Level 1, the compulsory level: the strategy and the
evaluation design you just saw. The optional Level 2 prototype for AQ3 and AQ4 is specified in full, and we did not
run it. So there is no model metric, no chart and no confusion matrix. That is a choice of scope, not a gap. The 13
runs of 2014 are the only independent test we have. A test can be used once; a partial early run would spend it. So we
keep it for one complete run of the frozen protocol. And AQ1 and AQ2 are not that prototype: they train no predictive
model and do not change the AQ3 design. What exactly is frozen? [click]
**Sources:** [M5 §10]

## Slide 54 – What the frozen protocol fixes   [10 Experimental status]   [Line: detail]
**Lead:** The protocol leaves no modeling choice open: three baselines and four candidate configurations are fixed, and the 2014 outcomes are opened once.
**On the slide:** Baselines [M5 App X Table A.25]: random list · early-sign rule ranked by its number of signs, ties by
lower activity ratio · background-only logistic model. · Candidates: penalised logistic regression on the primary set
(primary) · penalised logistic on the extended set · gradient-boosted trees on the primary set · gradient-boosted
trees on the extended set. · Ties go to the simpler configuration. · Eight steps, from checking the data hashes to an
experiment log. · One logged test: the 2014 outcomes opened once, after the second freeze, with the access time and the
frozen model's hash recorded first [M5 App X].
**Visual:** a 3 + 4 grid of configurations, primary highlighted (structure).
**Speaker notes:** Here is what the protocol fixes, so that whoever runs it has no modeling choice left. Three
baselines: a random list, the early-sign rule ranked by how many signs a student shows, and a model with background
only. Four candidates: penalised logistic regression and boosted trees, each on the primary and on an extended
predictor set. The penalised logistic on the primary set is the proposal, and ties go to the simpler option. It runs in
eight steps, and the 2014 outcomes are opened exactly once, after the second freeze, with the time and the frozen
model's fingerprint recorded first. A baseline matching the model would be an acceptable result. Checkpoint: method and
assessment are designed. Now the evidence we do have. [click]
**Sources:** [M5 App X Table A.25]

## Slide 55 – How we read the findings   [11 Findings: reading rules]   [Line: detail]
**Lead:** Every finding is an effect size with its 95% interval and population, read by its level and labelled with a confidence that says how well it is verified on OULAD.
**On the slide:** Reading by level: AQ2 (diagnostic) estimates are associations, not causes; a predictive claim needs
unseen data; a recommendation from observational data is an option to test [M5 §11]. · Confidence [M5 §11]: High – two
independent computations verify the counts on the stated population (says nothing about the university's courses) ·
Moderate – estimates keep their direction under the checks but rest on observational data or a model with a known
weakness · Not applicable – no result yet. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** three confidence badges with their definitions (structure).
**Speaker notes:** Ninth part: the evidence. Before the first number, three ground rules for reading it. Every finding
comes as an effect size with its 95 percent interval and its population. Every answer is read at its own level, so
AQ2 gives associations, never causes. And each answer carries a confidence label. High means two independent
computations agree on the stated population. Notice what it does not mean: it says nothing about whether the same is
true at the university. Moderate means the estimates keep their direction under every check but rest on observational
data or a model with a known weakness. And Not applicable means no result exists yet. With those rules, here is the
whole chain, question by question. [click]
**Sources:** [M5 §11; App XI Table A.26]

## Slide 56 – Final Project Traceability Matrix: goal to data   [11 Traceability Matrix]   [Line: main]
**Lead:** Each question traces in one row from the goal and its KPI to the data we actually had, with GAP where OULAD lacks a variable.
**On the slide:** Table [M5 §11.1 Table 11.1] (question – goal and KPI – level – required data – actual dataset and
variables): AQ1 – primary KPI – descriptive – dated result, tasks – 22 runs, day 14: 28,061; GAP: mode, year · AQ2 –
primary KPI; KPI 1 – diagnostic – signs, weeks 1–4 – day 27: 11,811 and 15,724; GAP: attendance · AQ3 – KPI 1 (rule
to beat) – predictive – enrolment at cut-off – 19 predictors; 2014 test · AQ4 – KPIs 1–2: GAP – prescriptive –
capacity; contacts – GAP: contacts. · All rows share the Business Goal and SMART Goal. · Key: KPI = key performance
indicator; KPI 1 = early-sign contact rate; KPI 2 = follow-up rate; GAP = no evidence for this link. · Key: OULAD = Open University Learning Analytics Dataset; SMART = specific, measurable, achievable, relevant, time-bound.
**Visual:** the matrix, GAP cells in a warning colour (table).
**Speaker notes:** Following those rules, here is the Final Project Traceability Matrix, the spine of the whole
project, in two halves. This first half runs from the goal to the data. Every row shares the same Business Goal and
SMART Goal. AQ1 serves the completion KPI and used 28,061 enrolments over 22 runs; it lacks delivery mode and year of
study. AQ2 serves the completion KPI and the early-sign contact rate; it used 11,811 enrolments in 2013 and 15,724 in
2014, and it lacks attendance. AQ3 has the rule to beat and 19 predictors ready, with 2014 as its test. AQ4 has a gap
where its contacts should be. The second half continues the same rows from preparation to decision. [click]
**Sources:** [M5 §11.1 Table 11.1; App XI Table A.27]

## Slide 57 – Final Project Traceability Matrix: method to decision   [11 Traceability Matrix]   [Line: main]
**Lead:** For AQ1 and AQ2 every link holds evidence and both meet their criteria; for AQ3 and AQ4 the chain ends at the evaluation design.
**On the slide:** Table [M5 §11.1 Table 11.2] (question – preparation – method – evaluation / result – decision –
status): AQ1 – day-14 rule; TMA, CMA – grouped rates – paths agree; 45.3% – D2, D3 – Answered · AQ2 – dated by day 27 –
logistic, run effects – 5 of 5 signs, both years – D2; D1 – Answered · AQ3 – refit per fold – penalised logistic;
reasons – S1 planned; N.A. – D1 – Deferred · AQ4 – 3 or 5 per 20 – top-k with signs – S1, FR1; N.A. – D1 – Deferred. ·
Key: TMA tutor-marked assignment; CMA computer-marked assessment; S1 gate (model must beat the rule list); FR1 fairness
review rule; D1 whom to contact; D2 where support time goes; D3 whether to extend; N.A. no result. · Key: AQ1 = descriptive question (outcome shares and timing); AQ2 = diagnostic question (early signs, association only); AQ3 = predictive question (model against the early-sign rule); AQ4 = prescriptive question (ranking under capacity).
**Visual:** the second half of the matrix, status column coloured Answered / Deferred (table).
**Speaker notes:** Here is the second half, from preparation to decision. AQ1 used the day-14 rule and tasks defined as
TMAs and CMAs, grouped rates with no model, both counting paths agree, and the headline is 45.3 percent. It serves D2
and D3, and it is answered. AQ2 used signs dated by day 27 and a logistic model with run effects; all five signs pass in
both years; it serves D2 and the reasons in D1; answered. AQ3 and AQ4 end at the design: the gate S1 and the fairness
rule FR1 are planned, and their result cell says not applicable. Both are deferred, and both serve D1. Now let us open
the AQ1 row. [click]
**Sources:** [M5 §11.1 Table 11.2; App XI Tables A.27, A.28]

## Slide 58 – AQ1: nearly one in two did not complete   [11 AQ1 answer]   [Line: main]
**Lead:** Of the 28,061 enrolments still registered at day 14, 45.3% did not complete, about the same in both years, a quarter by failing and a fifth by withdrawing.
**On the slide:** 45.3% (44.7–45.8) non-completion, 12,700 of 28,061 enrolments, 22 runs [M5 §11.2; App XII Table A.29]
· 2013: 45.7% (44.8–46.6) of 12,076 · 2014: 44.9% (44.2–45.7) of 15,985 [M5 §11.2] · Pooled: Fail 25.0% (24.5–25.6),
Withdrawn 20.2% (19.8–20.7) [M5 App XII Table A.29] · Success criterion met: prepared views and raw tables agree in
all 176 outcome cells; first missed week agrees for all 32,593 enrolments [M5 §11.2] · Confidence: high for OULAD
2013–2014. · Key: AQ1 = descriptive question; day 14 = end of add-drop; OULAD = Open University Learning Analytics
Dataset.
**Visual:** a stacked bar per year (Pass, Distinction, Fail, Withdrawn) with the non-completion share annotated and
95% intervals in the labels; legend on the slide (comparison).
**Speaker notes:** AQ1, the descriptive question: how many students are lost? Of the 28,061 enrolments still registered
at day 14, 45.3 percent did not complete. In 2013 it was 45.7 percent, in 2014 44.9; the intervals overlap. Pooled, a
quarter of students failed and a fifth withdrew. And we can trust the counting: two independent paths, the prepared
views and the raw tables, agree in all 176 outcome cells, and the first missed week agrees for every one of the 32,593
enrolments. So confidence is high, for OULAD. But "45.3 percent of whom?" matters more than you might think. Let me
show you what happens if you change the denominator. [click]
**Sources:** [M5 §11.2; App XII Table A.29]

## Slide 59 – AQ1: the denominator changes the answer   [11 AQ1 answer]   [Line: detail]
**Lead:** Counted over all enrolments rather than those still registered at day 14, non-completion rises above half, almost entirely through early withdrawals.
**On the slide:** Table [M5 App XII Table A.29] (population – non-completion – withdrawn): 2013 day 14 (12,076) –
45.7% – 18.9% · 2013 all (13,529) – 51.4% – 27.5% · 2014 day 14 (15,985) – 44.9% – 21.2% · 2014 all (19,064) – 53.8% –
33.8% · 22 runs all (32,593) – 52.8% – 31.2%. · The failed share barely moves. · Without flagged enrolments (unknown
withdrawal or registration day): 45.6% of 12,068 (2013) and 44.6% of 15,894 (2014), so the answer holds [M5 App XII]. ·
Key: day 14 = the primary KPI (key performance indicator) population. · Key: AQ1 = descriptive question (outcome shares and timing).
**Visual:** paired bars per year, day-14 vs all enrolments, the withdrawn segment highlighted (comparison).
**Speaker notes:** Following the headline, here is why the denominator is not a detail. Count over every enrolment
instead of those still registered at day 14, and non-completion jumps: 51.4 percent in 2013 and 53.8 in 2014. The extra
students are nearly all early withdrawals: the withdrawn share rises from 18.9 to 27.5 percent in 2013, from 21.2 to
33.8 in 2014, while the failed share barely moves. So the same students give two different completion rates, depending only on who
counts as enrolled. We also dropped the enrolments with an unknown withdrawal or registration day: 45.6 and 44.6
percent, so they do not change the answer. Next, where the losses concentrate. [click]
**Sources:** [M5 App XII Table A.29]

## Slide 60 – AQ1: modules and start months   [11 AQ1 answer]   [Line: detail]
**Lead:** Non-completion ranges from about a quarter in module AAA to over half in CCC, February runs lose more than October runs in both years, and modules lose students in different ways.
**On the slide:** Over 22 runs: lowest AAA, 26.3% of 720; highest CCC, 54.3% (52.7–55.9) of 3,670, 2014 only [M5 §11.2;
App XII]. · February (B) vs October (J) starts: 51.6% vs 42.4% in 2013; 49.6% vs 41.6% in 2014 [M5 App XII Table A.30].
· How students leave: GGG 2013, 4.3% withdrew and 31.7% failed; CCC 2014, 33.1% withdrew and 21.3% failed [M5 App XII].
· Among the six modules in both years: AAA lowest and DDD highest in each year. · Key: modules coded AAA–GGG; B =
February start, J = October start. · Key: AQ1 = descriptive question (outcome shares and timing).
**Visual:** a dot plot of non-completion by module, one dot per year with intervals; legend for year on the slide
(comparison).
**Speaker notes:** Now where students are lost. Module AAA loses the fewest, 26.3 percent over its runs. CCC, which ran
only in 2014, loses the most, 54.3 percent. Among the six modules that ran in both years, AAA is lowest and DDD highest
each time. Start month matters too: runs starting in February lose more students than runs starting in October, 51.6
against 42.4 percent in 2013, and 49.6 against 41.6 in 2014. And the way students leave differs. In GGG in 2013, only
4.3 percent withdrew while 31.7 failed. In CCC in 2014, 33.1 percent withdrew. A list aimed at students who stop taking part will
meet different kinds of risk in different modules. Zoom in to single runs. [click]
**Sources:** [M5 §11.2; App XII Table A.30]

## Slide 61 – AQ1: every run is different   [11 AQ1 answer]   [Line: main]
**Lead:** Run rates span from 24.9% to 58.3%, so a single pooled rate hides differences larger than its own interval.
**On the slide:** Figure: non-completion per module in 2013 and 2014, students registered at day 14, with 95% Wilson
intervals; dashed line = pooled rate of the 22 runs, 45.3% (12,700 of 28,061) [M5 §11.2 Figure 11.1]. · Range: 24.9%
(AAA 2013J) to 58.3% (CCC 2014B) [M5 §11.2]. · In 2013, four runs lie wholly above the pooled line and four wholly
below [M5 App XII]. · Takeaway: compare runs only with their intervals. · Key: run = module + year + start month (B
February, J October). · Key: AQ1 = descriptive question (outcome shares and timing).
**Visual:** Figure 11.1 of the report: dots with interval bars per module and year, dashed pooled line; legend for
year colours on the slide (comparison).
**Speaker notes:** Here is the picture. Each dot is a module in one year, with its 95 percent interval, and the dashed
line is the pooled rate, 45.3 percent. Look at the spread. The lowest run, AAA in October 2013, lost 24.9 percent. The
highest, CCC in February 2014, lost 58.3. In 2013 alone, four runs sit entirely above the pooled line and four entirely
below it. So one number for "the program" hides differences bigger than its own uncertainty. For the program manager,
that is the first useful pattern: losses concentrate in particular courses and intakes. But there is a trap in comparing
across years. [click]
**Sources:** [M5 §11.2 Figure 11.1; App XII]

## Slide 62 – AQ1: the year comparison depends on the add-drop rule   [11 AQ1 answer]   [Line: detail]
**Lead:** Over all enrolments 2014 looks worse than 2013, but among students registered at day 14 it looks no worse, because more 2014 students left before day 14.
**On the slide:** 2014 − 2013, all enrolments: +2.3 points (1.2 to 3.4) [M5 §11.2; App XII Table A.32] · day-14
population: −0.7 (−1.9 to 0.5) · six modules run in both years, day 14: −3.5 (−4.8 to −2.3) · not registered at day
14: 16.2% of 2014 enrolments against 10.7% of 2013 [M5 §11.2] · one run, BBB 2014J: 36.2% of 1,791 at day 14 against
49.7% of 2,292 enrolments, a 13.6-point shift from the denominator alone [M5 App XII]. · So the KPI (key performance
indicator) fixes the add-drop rule, and the university's baseline must be recounted under it. · Key: AQ1 = descriptive question (outcome shares and timing).
**Visual:** a slope chart of 2013 → 2014 under the two denominators, lines crossing (comparison).
**Speaker notes:** Following the run picture, the year question. Over all enrolments, 2014 is 2.3 points worse than
2013. Among students still registered at day 14, it is 0.7 points better, and in the six modules that ran in both
years, 3.5 points better. Same data, opposite stories. Why? In 2014, 16.2 percent of enrolments were gone or not yet
registered by day 14, against 10.7 percent in 2013; more of the students who would not complete left before the KPI
counts them. In a single run, BBB in October 2014, the denominator alone moves the rate by 13.6 points. That is why our
KPI fixes the add-drop rule. And now the finding that turned the project. [click]
**Sources:** [M5 §11.2; App XII Table A.32]

## Slide 63 – AQ1: missed tasks come too late   [11 AQ1 answer]   [Line: main]
**Lead:** Most non-completers miss a task at some point, but only 19.6% (2013) and 14.7% (2014) had missed one by week 4, so a rule on tasks alone comes too late.
**On the slide:** Missed any task during the run: non-completers 78.1% (2013) and 72.7% (2014); completers 21.9% and
19.4% [M5 §11.2; App XII Table A.31]. · Missed a task by week 4: non-completers 19.6% (18.6–20.7) and 14.7%
(13.9–15.5); completers under 1% [M5 App XII Table A.31]. · By week 8: 37.4% and 33.4% of non-completers [M5 App XII].
· Median first missed week: 9 for non-completers in both years [M5 App XII]. · Six of 22 runs had no task due by day 27
at all [M5 App XII]. · Takeaway: the early-sign rule must also count inactivity. · Key: task = TMA (tutor-marked
assignment) or CMA (computer-marked assessment); week 4 ends at day 27. · Key: AQ1 = descriptive question (outcome shares and timing).
**Visual:** cumulative curves of "share of non-completers who have missed a task" by week, one line per year, with a
vertical band at week 4 and the 19.6% / 14.7% points annotated; legend on the slide (trend).
**Speaker notes:** This is the result from our opening slide, now with its evidence. Missing a task separates the two
groups sharply: 78.1 percent of non-completers in 2013 and 72.7 in 2014 miss a task at some point, against about one
in five completers.
But look at the timing. By the end of week 4, only 19.6 percent of non-completers in 2013, and 14.7 percent in 2014,
had missed one. By week 8, still only 37.4 and 33.4 percent. The median non-completer first misses a task in week 9. And in six
of the 22 runs no task falls due by day 27 at all. So the signal everyone watches arrives after the support window. The
question becomes: what else is visible by week 4? That is AQ2. [click]
**Sources:** [M5 §11.2; App XII Table A.31]

## Slide 64 – AQ2: five signs, one model   [11 AQ2 answer: setup]   [Line: detail]
**Lead:** We tested five signs visible by day 27 in a within-run model on 2013, then replicated it unchanged on 2014.
**On the slide:** Populations: 2013, 11,811 enrolments registered at day 27 (44.4% non-completion); 2014, 15,724
(44.0%), including module CCC [M5 §11.3]. · Task signs, in runs with a task due by day 27 (9,960 and 12,585
enrolments): a missed task; a late TMA (tutor-marked assignment). · Click signs, all runs: no click in the last seven
days (days 21–27); clicks on days 0–27 below the run median; no click before day 0 [M5 §11.3; App XIII]. · Model:
logistic regression with run fixed effects, background terms and sign × module terms; each effect an average risk
difference in percentage points, an association, never an effect of the sign [M5 §11.3]. · Key: AQ2 = diagnostic
question; fixed effects = comparison within the same run.
**Visual:** five sign cards in two groups (task, click) with the population under each group (structure).
**Speaker notes:** AQ2, the diagnostic question. We measured five signs at day 27. Two are about tasks: a missed task,
and a TMA submitted late; they only exist in runs with a task due by then. Three are about clicks: no click in the last
seven days, total clicks below the median of the same run, and no click before the course even started. The model is
a logistic regression with a fixed effect per run, so each student is compared only with others in the same run,
plus background terms. We built it on 11,811 enrolments of 2013 and ran it unchanged on 15,724 of 2014. Each result is
a risk difference in percentage points, and an association, never an effect. Here is what we found. [click]
**Sources:** [M5 §11.3; App XIII]

## Slide 65 – AQ2: every early sign goes with later non-completion   [11 AQ2 answer: key insight]   [Line: main]
**Lead:** All five signs go with later non-completion within module in both years, and the activity signs carry information that missed tasks cannot yet show.
**On the slide:** Figure: mutually adjusted risk difference between enrolments with and without each sign at day 27,
2013 and 2014, 95% intervals [M5 §11.3 Figure 11.2]. · Missed task: 40.8 (37.7–43.9) and 39.3 (36.4–42.1) points ·
late TMA (tutor-marked assignment): 20.2 and 20.3 · no click in the last seven days: 14.5 and 15.8 · clicks below the
run median: 13.4 and 14.6 · no click before the start: 10.6 and 8.7 [M5 §11.3; App XIII Table A.33]. · No sign moves by
more than two points between years [M5 §11.3]. · Raw view, 2013: 90.0% of enrolments with a missed task did not
complete, against 39.6% without [M5 App XIII Table A.33]. · Association, not cause. · Key: points = percentage points
of later non-completion; dot = 2013, square = 2014. · Key: AQ2 = diagnostic question (early signs, association only).
**Visual:** Figure 11.2 of the report: a forest plot, five signs, two markers per sign (2013, 2014) with intervals, a
vertical line at 5 points; marker key on the slide (comparison).
**Speaker notes:** This is the key insight. Every one of the five signs goes with later non-completion, inside the same
run, in both years. A missed task by day 27 goes with 40.8 more percentage points of non-completion in 2013 and 39.3 in
2014. In raw terms, 90.0 percent of those students in 2013 did not complete. A late TMA goes with 20.2 and 20.3 points. And here is
the part that matters for timing: the click signs. No click in the last seven days, 14.5 and 15.8 points; activity
below the run median, 13.4 and 14.6; no click before the start, 10.6 and 8.7. No sign moves more than two points between years. Activity
is visible when tasks are not. These are associations, not causes. Do they hold module by module? [click]
**Sources:** [M5 §11.3 Figure 11.2; App XIII Table A.33]

## Slide 66 – AQ2: consistent across modules   [11 AQ2 answer]   [Line: detail]
**Lead:** Each sign points the same way in every module in 2013 and in 29 of 30 module estimates in 2014, though its size varies by module.
**On the slide:** 2013: every sign same direction in every module where it is defined (4 of 4 for task signs, 6 of 6
for click signs) [M5 App XIII]. · 2014: same direction in 29 of 30 module estimates; exception: a late TMA (tutor-marked
assignment) in AAA, −1.2 points (−14.4 to 12.1) on 348 enrolments, interval includes 0 [M5 §11.3; App XIII]. · No CCC
student had submitted a TMA late by day 27 [M5 §11.3]. · Size varies: no click in the last seven days goes with 27.5
points in EEE but 3.8 in GGG (2013) [M5 App XIII Table A.34]. · Consistency means same direction, not similar size. · Key: AQ2 = diagnostic question (early signs, association only).
**Visual:** a heatmap of signs × modules × year, colour = risk difference, hatched where the interval includes 0;
colour key on the slide (comparison).
**Speaker notes:** Following the pooled estimates, module by module. In 2013 every sign points the same way in every
module where it exists. In 2014, 29 of 30 module estimates do. The exception is a late TMA in module AAA, minus 1.2
points, on only 348 enrolments, with an interval from minus 14.4 to plus 12.1, so it tells us very little either way. But
consistency means direction, not size. Inactivity in the last seven days goes with 27.5 points in EEE and only 3.8 in
GGG. Remember that GGG has very few withdrawals; most of its non-completers stay and fail. So a sign of stopping may
matter less there, a reading we note but cannot test. Did our analysis choices drive this? [click]
**Sources:** [M5 §11.3; App XIII Table A.34]

## Slide 67 – AQ2: sensitivity runs   [11 AQ2 answer]   [Line: detail]
**Lead:** Six sensitivity runs in each year change no verdict: every sign stays above 5 points with an interval excluding 0.
**On the slide:** Variants (2013, mutually adjusted, points) [M5 App XIII Table A.35]: de-duplicated clicks – missed
task 40.9 · late CMAs (computer-marked assessments) counted as late – late sign 15.2 (from 20.2) · without flagged
enrolments – missed task 40.8 · without the 2 runs with no task due – no click before start 10.4 · below half the run
median – below-median sign 14.7 · one sign effect for all modules – no click in last seven days 11.5. · 2014: smallest
estimate under any variant 6.9 points, lowest interval bound 4.3 [M5 App XIII]. · Pooled over 22 runs (27,535
enrolments at day 27): 39.8, 20.6, 14.7, 14.0 and 9.4 points [M5 App XIII]. · Key: AQ2 = diagnostic question (early signs, association only).
**Visual:** a small-multiples dot chart: one panel per sign, one dot per variant, 5-point line marked (comparison).
**Speaker notes:** Next, were these results an artefact of our choices? We ran six variants in each year: removing
duplicate clicks, counting late CMAs as late, dropping uncertain records, dropping runs with no task due, a different
cut for low activity, and one effect for all modules. No verdict changes. The biggest move is the late sign when late
CMAs count: it drops from 20.2 to 15.2, because in one run nearly everyone had a late CMA. In 2014 the smallest estimate
under any variant is 6.9 points. Pooled over all 22 runs, the five signs go with 39.8, 20.6, 14.7, 14.0 and 9.4 points.
But one check did find a weakness. [click]
**Sources:** [M5 App XIII Table A.35]

## Slide 68 – AQ2: activity works as a gradient   [11 AQ2 answer]   [Line: detail]
**Lead:** The yes/no click signs miss a graded activity effect, and with clicks added as a continuous adjustment the below-median sign weakens below the criterion in 2014 while the other four still meet it.
**On the slide:** Binned residuals by activity level lie outside the band in all five levels in both years; e.g. no
click on days 0–27, 2013: observed 81.1%, predicted 75.4%, residual +5.6 against a band of 3.0 [M5 App XIII Table
A.36]. · Added check, chosen after seeing the residuals: log(1 + clicks on days 0–27) as a continuous adjustment [M5 App
XIII]. · 2013: misfit disappears; below-median sign 13.4 → 5.8; missed task 40.8 → 37.3 [M5 App XIII]. · 2014:
below-median sign 5.9, same direction in only 4 of 7 modules, no longer meets the criterion; other four signs still do
[M5 §11.3]. · It qualifies the verdict; the planned estimates remain the primary result. · Supports continuous click
measures in the AQ3 (predictive) design. · Key: AQ2 = diagnostic question (early signs, association only).
**Visual:** a bar chart of residuals by activity level (five bins), band shown as a shaded zone; key on the slide
(trend).
**Speaker notes:** One check found a real weakness. When we compared observed and predicted non-completion by activity
level, the model was off in every level. Students with no click at all failed to complete 5.6 points more often than
predicted. Risk keeps falling as activity rises; a yes-or-no cut at the median misses that. So, after seeing this, we
added one run with clicks as a continuous adjustment. In 2013 the misfit disappears. The below-median sign shrinks to
5.8 points, and in 2014 to 5.9, where it no longer meets the criterion. The other four signs still do. Because we chose
this run after looking, it qualifies the verdict rather than replacing it. So what does AQ2 mean overall? [click]
**Sources:** [M5 §11.3; App XIII Table A.36]

## Slide 69 – AQ2: what the signs mean for the list   [11 AQ2 answer: discussion]   [Line: main]
**Lead:** The signs give each name on a contact list a factual reason staff can check and show that every part of the early-sign rule carries information, but they do not show that contact would help.
**On the slide:** Confidence: moderate; two years agree, but the click signs rest on a known misfit and on
associations that unrecorded reasons could explain [M5 §11.3]. · For D1 (whom to contact): a factual reason beside each
name; each part of the early-sign rule carries information on its own [M5 §11.3; App XIII]. · For D2 (where support time
goes): a hypothesis to place early support where signs are common, to check on the university's records. · Cannot
show: that a sign causes non-completion; a student who stops clicking may already have decided to leave [M5 App XIII]. ·
Groups (2013): the missed-task sign keeps a positive difference with an interval excluding 0 in every one of 15
groups, a description, not grounds for different treatment [M5 App XIII]. · Key: AQ2 = diagnostic question (early signs, association only).
**Visual:** two columns "The signs can…" / "The signs cannot…" (comparison).
**Speaker notes:** So, the meaning of AQ2. Confidence is moderate, not high: two years agree, but the click signs carry
a known misfit, and these are associations that unrecorded reasons could explain. Here is the plain possibility: a
student who stops clicking may already have decided to leave, for reasons OULAD never sees. Then the sign does not
cause anything. What the signs can do is real, though. They give every name on a list a factual reason a lecturer can
check against the record. And they show that each part of the early-sign rule, including inactivity, carries
information on its own. That is the climax of our story: the rule needs its activity part. Now, the two questions
still waiting. [click]
**Sources:** [M5 §11.3; App XIII]

## Slide 70 – AQ3 and AQ4: expected outputs, not results   [11 Deferred AQs]   [Line: main]
**Lead:** AQ3 and AQ4 have expected outputs and the criteria that would decide them, but no model metric.
**On the slide:** AQ3 (predictive): would give a risk rank per enrolment at days 13 and 27, a probability only if
calibration holds; answered by gate S1 (the model must beat the early-sign rule's list on the 13 runs of 2014); if it
does not, the rule's order stays [M5 §11.4]. · AQ4 (prescriptive ranking): would give a list of 3 or 5 per 20 students
per run with the signs behind each name; answered when it meets S1, rule FR1 (fairness review when a group's recall is
more than 10 points behind) passes or its flags are reviewed, and the risk order is stated as untested for need [M5
§11.4; App XIV Table A.37]. · Neither says who should make contact or whether contact helps.
**Visual:** two "expected output" cards, each with a grey "not yet measured" stamp (structure).
**Speaker notes:** Following AQ2, the two designed questions. We state their answers as expected outputs, because no
model has been trained. AQ3 would give a risk rank for each enrolment at days 13 and 27, and a probability only if the
calibration check holds. It is answered by gate S1 on the 13 runs of 2014. If the model does not beat the rule, the
rule's order stays. AQ4 would give a list of 3 or 5 per 20 students per run, with the signs beside each name, usable
only if it passes S1 and the fairness rule FR1, or if any flag is reviewed by people. And neither says who should call,
or whether calling helps. All four answers side by side. [click]
**Sources:** [M5 §11.4; App XIV Table A.37]

## Slide 71 – Final answers by question   [11 AQ-by-AQ answers]   [Line: main]
**Lead:** Two questions are answered with stated confidence, two await their single test, and every implication is read at the level of its question.
**On the slide:** Table [M5 §11.5 Table 11.3] (question – main finding or expected output – confidence – implication):
AQ1 (descriptive) – 45.3% did not complete; runs 24.9–58.3%; under 20% missed a task by week 4 – high for OULAD
2013–2014; KPI proxy – D2 hypothesis; tasks alone too late · AQ2 (diagnostic) – five signs consistent in both years;
missed task 40.8 and 39.3 points – moderate; association – D1 reasons; contact to test · AQ3 (predictive) – expected:
risk rank; gate S1 – not applicable – D1 order only if S1 is met · AQ4 (prescriptive ranking) – expected: 3 or 5 per 20
with signs – not applicable; no contact data – D1 list, not a contact plan. · Key: D1 whom to contact; D2 where support
time goes; S1 the model-beats-rule gate; KPI key performance indicator. · Key: OULAD = Open University Learning Analytics Dataset.
**Visual:** the four-row answers table, confidence column colour-coded (table).
**Speaker notes:** Here are the four answers side by side. AQ1: 45.3 percent did not complete, runs range from 24.9 to
58.3, and fewer than one in five non-completers had missed a task by week 4. High confidence for OULAD. It gives the
program manager a hypothesis and tells us tasks alone come too late. AQ2: five signs, consistent in both years, a
missed task at 40.8 and 39.3 points. Moderate confidence. It gives reasons for the contact list, while contact itself stays
a thing to test. AQ3 and AQ4: expected outputs only. AQ3 changes the order of the list only if it passes the gate. AQ4
gives a list, not a contact plan. So what can each decision-maker do with this now? Starting with D1. [click]
**Sources:** [M5 §11.5 Table 11.3; App XIV Tables A.38, A.39]

## Slide 72 – Decision support for D1: whom to contact   [11 Decision support D1]   [Line: main]
**Lead:** For D1, the early-sign rule, with its activity part, is the candidate list for the pilot, once its list performance is measured in the AQ3 test.
**On the slide:** Evidence now: a missed task goes with 40.8 more points of non-completion (37.7–43.9); each part of the
early-sign rule carries information on its own (AQ2, diagnostic); by week 4 only 19.6% of non-completers had missed a
task (AQ1, descriptive) [M5 App XIV Table A.40]. · Decision option: build the week-3 and week-5 lists from the rule,
ordered by number of signs, signs shown beside each name; replace the order by the AQ3 ranking only if gate S1 (model
beats the rule's list) is met [M5 App XIV Table A.40]. · Still to test: the rule's list reaches more later
non-completers than a random list of the same length; contact raises completion, in a randomised pilot; the person and
offer stay open choices. · Key: D1 = whom to contact at each review point. · Key: AQ3 = predictive question (model against the early-sign rule).
**Visual:** a three-column card: evidence now → option → test before adoption (sequence).
**Speaker notes:** Resolution, decision by decision. D1: whom should lecturers, lecturer-advisors and the support office
contact? The evidence supports a clear candidate: the early-sign rule, including its activity part. It is simple, staff
can understand it, the university can compute it from records it already holds, and each of its parts goes with later
non-completion in both years. The option is to build the week-3 and week-5 lists from it, with the signs beside each
name. Two things must come first. Its list performance must be measured, which is a baseline of the AQ3 test. And
whether contact helps must be tested in a randomised pilot. Next, D2, the program manager. [click]
**Sources:** [M5 §11.5; App XIV Table A.40]

## Slide 73 – Decision support for D2: where support time goes   [11 Decision support D2]   [Line: detail]
**Lead:** For D2, a hypothesis: place early support time first where non-completion and early signs are highest, once the same pattern shows in the university's records.
**On the slide:** Evidence now: non-completion from 24.9% to 57.5% between runs (2013); February runs 51.6% against
October runs 42.4% (2013); no click on days 21–27 in 54.8% of GGG 2013J against 7.6% of DDD 2013B [M5 App XIV Table
A.40]. · Decision option, as a hypothesis: place early support time first in the courses and intakes with the highest
non-completion and the highest share of early signs, measured on the university's own records [M5 §11.5]. · Caution:
high risk marks where non-completion concentrates, not where support helps most. · Check before adoption: the pattern
repeats over several semesters; baseline recounted under the add-drop rule. · Key: D2 = where the program manager
places support time.
**Visual:** a ranked bar of run non-completion rates with the top intakes highlighted (comparison).
**Speaker notes:** Following D1, the program manager's decision, D2. In OULAD's 2013 runs, non-completion ranges from
24.9 to 57.5 percent, February intakes lose more than October intakes, and the share of students already silent in
week 4 ranges from 7.6 percent in one run to 54.8 in another. So the option is to put early support time first where
both the losses and the early signs are highest. But we phrase it as a hypothesis, for two reasons. The pattern must
repeat in the university's own courses, over several semesters. And high risk shows where losses concentrate, not
where support would help most. Finally, D3, leadership. [click]
**Sources:** [M5 §11.5; App XIV Table A.40]

## Slide 74 – Decision support for D3: whether to extend   [11 Decision support D3]   [Line: detail]
**Lead:** For D3, we offer a measurement method rather than a verdict, and extension should wait for a pilot result.
**On the slide:** Evidence now: the denominator alone can move a completion rate by up to 13.6 points (AQ1,
descriptive); AQ3 and AQ4 have no result; no evidence on the effect of contact exists [M5 App XIV Table A.40]. ·
Offered: a completion rate computed by one rule for pilot and comparison courses; a ranking gate fixed in advance; a
fairness audit [M5 §11.5]. · Decision option: decide on extension only after the pilot. · Conditions: a completion gain
against comparison courses; legal approval under Vietnam's rules on high-risk AI use; staff capacity confirmed [M5 App
XIV Table A.40]. · Key: D3 = whether to extend the approach and link data routinely. · Key: AQ3 = predictive question (model against the early-sign rule).
**Visual:** a gate diagram: pilot result + legal approval + capacity → extension decision (structure).
**Speaker notes:** D3 is close to a one-way door, so here we offer a method, not a verdict. AQ1 shows that the choice
of denominator alone can move a completion rate by up to 13.6 points. So the first thing leadership needs is one rule
for counting completion, the same in pilot and comparison courses. Second, a ranking gate fixed in advance. Third, a
fairness audit. With those, a pilot can produce a result worth trusting, even a negative one. Extension waits for that
result, for legal approval under Vietnam's rules on high-risk AI, and for confirmed staff capacity. Let me put the
three decisions together. [click]
**Sources:** [M5 §11.5; App XIV Table A.40]

## Slide 75 – What the answers support together   [11 Decision support]   [Line: main]
**Lead:** Together, the answers support preparing a pilot, with the rule as the candidate list, the signs as reasons and the AQ1 method as the measure, and leave the effect of contact as the question the pilot must answer.
**On the slide:** Prepare the pilot with [M5 App XIV]: the early-sign rule as the candidate list, once its list
performance is measured in the AQ3 (predictive) test · the AQ2 (diagnostic) signs as the reasons shown to staff · the
AQ1 (descriptive) method as the measure of completion. · Every prescriptive statement is a decision option with a
hypothesis for the pilot: OULAD (Open University Learning Analytics Dataset) records no contact [M5 §11.5]. · Main open
question: whether, and for whom, early contact improves completion.
**Visual:** three building blocks (list, reasons, measure) supporting a "pilot" platform, with the open question above
(structure).
**Speaker notes:** So, all three decisions in one view. The answers support preparing a pilot built from three blocks.
The early-sign rule as the candidate list, once the AQ3 test has measured how well its list performs. The AQ2 signs as
the reasons that staff see beside each name. And the AQ1 method as the way to count completion. Everything prescriptive
stays a decision option, because OULAD records no contact at all, so it cannot even compare contacted and
non-contacted students. The main question is still open: does early contact help, and for whom? Before we say how to
answer it, let us be clear about the limits of what we have. [click]
**Sources:** [M5 §11.5; App XIV]

## Slide 76 – Three kinds of limit   [12 Limitations]   [Line: main]
**Lead:** We keep three situations apart, "no evidence found", "no data to test" and "not yet tested", because each calls for a different next step.
**On the slide:** No evidence found: a comparison was made and showed no clear difference [M5 §12]. · No data to test:
OULAD (Open University Learning Analytics Dataset) and every screened dataset lack the data [M5 §12]. · Not yet tested:
the data exist, but the analysis waits for the single AQ3 (predictive) test [M5 §12]. · Three conditions on every
answer: results describe UK distance-learning modules of 2013–2014, and instructional conditions change what predicts
success; confounding makes the effect of contact unknowable from these data; a flag must not become a label [M5 §12].
**Visual:** three labelled boxes, each with its next step: report as uncertain / collect in the pilot / run the test
(structure).
**Speaker notes:** Tenth part: limitations and future work. We sort every limit into one of three boxes, because each
needs a different next step. "No evidence found" means we compared and saw no clear difference. "No data to test" means
neither OULAD nor any dataset we screened holds the data. "Not yet tested" means the data exist, but we are saving the
single AQ3 test. On top of that, three conditions hang over every answer. These are UK distance-learning modules from
2013 and 2014, and what predicts success changes with teaching conditions. Confounding means OULAD can never tell us
the effect of contact. And a risk flag must never become a label on a student. Here is the log. [click]
**Sources:** [M5 §12; App XV]

## Slide 77 – Limitation log   [12 Limitation log]   [Line: detail]
**Lead:** Each limit is logged with its kind and its handling, so a reader knows where each answer can and cannot be used.
**On the slide:** Table [M5 §12 Table 12.1] (limitation – kind – handling): year difference over all enrolments in
shared modules; small-module click signs, intervals include 0 – no evidence found – no claim, reported as uncertain ·
contact and its outcome; mode, year of study, attendance; capacity – no data to test – randomised pilot ·
several-modules sign before 2014; leave and transfer – no data to test – described on 2014; university recount · AQ3
and AQ4 results – not yet tested – single AQ3 test, design unchanged · binary click signs; below-median sign weak in
2014 once adjusted; KPI proxy and denominator – measurement – continuous measures in AQ3; one add-drop rule · UK
distance learning of 2013–2014; observational design – scope and causal – re-check on the university's records;
options as hypotheses. · Key: AQ3 predictive, AQ4 ranking; KPI key performance indicator.
**Visual:** the log table, kind column colour-coded to the three boxes of the previous slide (table).
**Speaker notes:** Following those three boxes, here is the log. Where we saw no clear difference, such as the year
difference in shared modules over all enrolments, or click signs in the smallest module, we make no claim. Contacts,
delivery mode, year of study, attendance and capacity have no data anywhere, so they go to the pilot. AQ3 and AQ4 are
not yet tested, and their design stays unchanged until the single test. Then the measurement limits: the click signs
are binary, the below-median sign is weak in 2014 once adjusted, and the KPI is a proxy. And the big one: two years of
UK distance learning, observed rather than randomised. So, what comes next? Two steps can run on OULAD today. [click]
**Sources:** [M5 §12 Table 12.1; App XV Table A.41]

## Slide 78 – Next on OULAD: the single test   [12 Future work; deferred AQs]   [Line: main]
**Lead:** Two steps can run on OULAD as it stands: the AQ3 test under the frozen protocol, which also measures the rule's own list, and then the AQ4 list with its fairness audit.
**On the slide:** Step 1, Level 2 prototype of AQ3 (predictive): whether a model at day 27 lists more non-completers than
the early-sign rule (gate S1); the rule's own list performance, which D1 (whom to contact) needs; calibration. Data:
2013 runs for development, 13 runs of 2014 for the single test [M5 App XV Table A.42]. · Step 2, AQ4 (prescriptive
ranking) list and fairness audit: recall at 3 and 5 per 20, gain over a random list, rule FR1 (fairness review rule)
by disability and deprivation band. Depends on step 1 [M5 App XV Table A.42]. · The design stays as Milestone 4 fixed
it [M5 §12.1]. · Key: OULAD = Open University Learning Analytics Dataset; S1 = gate: the model must beat the rule list.
**Visual:** steps 1 and 2 of a five-step roadmap, steps 3–5 greyed (sequence).
**Speaker notes:** Following the log, the first two steps of the roadmap need no new data. Step 1 is the AQ3 test,
exactly as Milestone 4 froze it: baselines first, then the candidates on the 2013 folds, a freeze, and one scoring of
the 13 runs of 2014. It answers whether a model beats the rule, and, just as important for D1, how well the rule's own
list performs. Step 2 takes those scores, forms the AQ4 lists of 3 or 5 per 20, measures the gain over a random list,
and runs the fairness rule by disability and deprivation band. Everything about both steps is already specified. The
remaining steps need something OULAD cannot give: the university itself. [click]
**Sources:** [M5 §12.1; App XV Table A.42]

## Slide 79 – Next at the university: recount and replace assumptions   [12 Next data needed]   [Line: detail]
**Lead:** At the university, the baseline is recounted under the add-drop rule, the early-sign rule is checked on its task calendar, and every assumed value is replaced by its records.
**On the slide:** Step 3, transfer to the university: baseline completion under the add-drop rule; the early-sign rule
on the university's task calendar; the AQ1 (descriptive) and AQ2 (diagnostic) results re-checked. Data: two years of
the university's enrolment, task and platform records; access approved by the legal and data office [M5 App XV Table
A.42]. · Assumptions to replace: the baseline completion rate, the capacity figures, the one-week data delay, the
list-length scenarios and the ten-point fairness gap [M5 App XV]. · Students' acceptance of activity-based contact was
voiced only by simulated students, so it needs confirmation from real students in Vietnam [M5 App XV].
**Visual:** a checklist of five assumed values with an arrow to "university records" (structure).
**Speaker notes:** Step 3 moves to the university. First, recount the baseline completion rate under the same add-drop
rule we used, because, as AQ1 showed, the denominator can move a rate by more than ten points. Second, check the
early-sign rule against the university's own task calendar. Third, re-check the AQ1 and AQ2 patterns on two years of
its records. Along the way, every assumption gets replaced: the baseline rate, the staff capacity, the one-week data
delay, the list lengths and the ten-point fairness gap. And one more honest point: only simulated students said they
would accept being contacted because of their activity. Real students in Vietnam need to be asked. Then come the legal
duties. [click]
**Sources:** [M5 §12.1; App XV Table A.42]

## Slide 80 – Risk classification and human control   [12 Future work]   [Line: detail]
**Lead:** A contact list built from a model is likely a high-risk use of AI in education under Vietnamese law, so it needs a risk classification first and staff keep the final say.
**On the slide:** Vietnam's Law on Artificial Intelligence, No. 134/2025/QH15, applies from 1 March 2026: human control
and the ability to intervene over every decision of an AI system [M5 App XV]. · Decision 33/2026/QĐ-TTg lists among
high-risk uses in education AI systems that rank learners or analyse learner behaviour [M5 App XV]. · Step 4: risk
classification and consent; legal review; consultation with students [M5 App XV Table A.42]. · Ethics: a flag leads to
support and expires with the run [M5 App XV].
**Visual:** a gate icon "risk classification" between step 3 and the pilot (sequence).
**Speaker notes:** Following the transfer step, the law. Vietnam's Law on Artificial Intelligence applies from 1 March
2026 and requires human control, and the ability to intervene, over every decision of an AI system. A government
decision of 2026 lists, among high-risk uses in education, systems that rank learners and systems that analyse learner
behaviour. A contact list built from a model is likely to fall in that class. So step 4 is a risk classification
first, with legal review and consultation with students, and staff keep the final say on every contact. Ethically, we
add one rule: a flag leads to support and expires with the run. It never follows a student. That brings us to the
pilot. [click]
**Sources:** [M5 §12.1; App XV]

## Slide 81 – The randomised pilot   [12 The pilot]   [Line: main]
**Lead:** Only a randomised pilot among flagged students can separate the effect of contact from the reasons students are flagged, and its contacts must be logged before any model is retrained.
**On the slide:** Design: randomised comparison among the flagged students of the pilot courses, time zero at the
eligibility cut-off [M5 §12.1]. · Answers: whether contact raises completion; which contact and offer work; the
contact parts of secondary KPI 1 (early-sign contact rate) and KPI 2 (follow-up rate) [M5 App XV Table A.42]. · Needs: a
contact record with time, person, offer and outcome; year of study, delivery mode, attendance [M5 App XV Table A.42]. ·
Rule: contacts logged with their outcomes before any model is retrained, since a model retrained on outcomes shaped by
contact would learn its own influence [M5 §12.1]. · Timing: steps 3 and 4 complete before contact begins in Semester 2
of 2026–2027 [M5 App XV]. · Key: KPI = key performance indicator.
**Visual:** a randomisation diagram: flagged students → contact / usual support → completion compared (structure).
**Speaker notes:** And step 5, the pilot. Among the flagged students in the pilot courses, some are randomly assigned to
contact and the rest receive usual support, with time zero at the eligibility cut-off. Why randomise? Because flagged
students differ from others in ways we cannot see; only random assignment separates the effect of contact from the
reasons they were flagged. The pilot logs every contact: when, by whom, which offer, and what happened. That also
measures the contact parts of our two secondary KPIs. One subtle rule: log contacts before retraining any model, or the
model learns its own influence. Steps 3 and 4 must be done before contact starts in Semester 2 of 2026–2027. Now, how
did we use AI along the way? [click]
**Sources:** [M5 §12.1; App XV Table A.42]

## Slide 82 – Generative AI: roles and one rule   [13 Generative AI use]   [Line: main]
**Lead:** AI served as simulated stakeholder, research and code assistant, critic and writing partner, under one rule: it was never a source of data, statistics, licence information or results.
**On the slide:** Roles [M5 §13]: simulated stakeholder · research and code assistant · critic · writing partner. ·
Rule: AI was never a source of data, statistics, licence information or results; every fact it offered was checked
against a saved source, the data files or code we ran [M5 §13]. · No AI produced a metric value, threshold or result
[M5 §13.1].
**Visual:** four role icons around a central rule box (structure).
**Speaker notes:** Eleventh part: generative AI. We used it in four roles. As simulated stakeholders in Milestone 1,
which is why we keep calling the interviews simulated. As a research and code assistant. As a critic of our plans. And
as a writing partner. In every role, one rule held. AI was never a source of data, statistics, licence information or
results. Anything it offered was checked against a saved source, the data files, or code we ran ourselves. No AI
produced a metric value, a threshold or a result in this project. Here is what that looked like milestone by
milestone. [click]
**Sources:** [M5 §13; §13.1]

## Slide 83 – AI Decision Log   [13 AI decision log]   [Line: detail]
**Lead:** At each milestone we checked AI output and accepted, modified or rejected it, and the final decisions stayed ours.
**On the slide:** Table [M5 App XVI Table A.43] (stage – AI used for – verification – our decision): Milestone 1 –
simulated stakeholders and a reviewer, 12 critiques – each quote checked against its transcript; 9 accepted, 2 partly,
1 rejected – cut-offs moved to the end of weeks 2 and 4; interviews count as simulated · Milestone 2 – search and
selection critics, 22 critiques – no dataset fact without the official source – gates require a dated withdrawal and
dated tasks · Milestone 3 – code assistant and a leakage auditor, 8 findings – 13 of 13 numbers equal an independent
recount – all eight findings acted on, e.g. tasks due before registration counted as missed · Milestone 4 – three
isolated reviewers, 24 critiques – each critique checked against design facts – switching rule with a margin fixed in
advance; gate S1 (model must beat the rule list) fixed on all 13 test runs · Milestone 5 – evidence extraction, AQ1 and
AQ2 code, drafting – 369 statements checked, 0 errors; 2014 associations re-estimated by separate code, 35 of 35 agree
to 0.01 points; 66 review critiques: 42 accepted, 14 in part, none rejected, 10 handled in finishing steps. · Key: AQ1 = descriptive question (outcome shares and timing); AQ2 = diagnostic question (early signs, association only).
**Visual:** the log table with an accepted / partly / rejected tally per row (table).
**Speaker notes:** Here is the log in brief. In Milestone 1, a reviewer gave twelve critiques: we accepted nine, two in
part, and rejected one. In Milestone 2, critics pushed us to require a dated withdrawal and dated tasks. In Milestone 3,
a separate AI auditor found real errors in our code, such as tasks due before a student registered being counted as
missed. All eight findings were acted on. In Milestone 4, three isolated reviewers led to the switching margin and to
fixing the gate on all 13 test runs. In Milestone 5, AI extracted 369 statements, each checked against its source with
zero errors, and wrote analysis code that separate code re-estimated: 35 of 35 agree. What did we learn from this?
[click]
**Sources:** [M5 §13.1; App XVI Table A.43]

## Slide 84 – Reflection on AI as a partner   [13 Reflection]   [Line: detail]
**Lead:** AI helped most when it had to argue from the data, and its output was always a proposal to verify, never a finding.
**On the slide:** Guidance: UNESCO (United Nations Educational, Scientific and Cultural Organization) holds that
generative AI cannot be trusted to be accurate and that its information should never be accepted at face value [M5
§13.2]. · Verification matched to risk: quotes against transcripts; literature against saved copies with verbatim
quotations; code against fixtures and independent recounts; critics confined to the brief and the data [M5 §13.2]. ·
Decisions that stayed ours: keep the 2014 runs out of every AQ3 (predictive) choice; one early-sign rule; report AQ3 and
AQ4 as designs; state every association as an association [M5 §13.2]. · Key: AQ4 = prescriptive question (ranking under capacity).
**Visual:** a two-column "AI proposed / we decided" list (comparison).
**Speaker notes:** Following the log, our reflection. UNESCO's guidance says generative AI cannot be trusted to be
accurate, and that its information should never be taken at face value. We took that literally and matched each check
to what could go wrong: quotes against transcripts, literature against saved copies, code against fixtures and
independent recounts. AI helped most when it had to argue from our data, as the Milestone 3 auditor did. But the key
decisions were ours: keep 2014 out of every AQ3 choice, keep one early-sign rule, report AQ3 and AQ4 honestly as
designs, and call every association an association. AI challenged our reasoning; the evidence came from the data.
Final checkpoint. Let us conclude, firmest first. [click]
**Sources:** [M5 §13.2; App XVI]

## Slide 85 – What we can conclude, firmest first   [14 Conclusion]   [Line: main]
**Lead:** We can firmly say how many students are lost and when tasks show it, moderately say which early signs go with it, and only propose how a list should be tested.
**On the slide:** 1. Firm (AQ1, descriptive; high confidence on OULAD 2013–2014): 45.3% of enrolments still registered
at day 14 did not complete; rates vary strongly between runs; the year difference depends on the add-drop rule; most
non-completers first missed a task after week 4 [M5 §14; §11.2]. · 2. Moderate (AQ2, diagnostic): all five early signs
go with later non-completion in both years, a missed task by 40.8 and 39.3 points, in the same direction across modules
[M5 §14; §11.3]. · 3. Designed (AQ3 predictive, AQ4 ranking): a penalised logistic model judged once against the
early-sign rule, and a capacity-limited list audited for fairness; outputs expected, not measured [M5 §14]. · Key: OULAD
= Open University Learning Analytics Dataset.
**Visual:** three tiers with decreasing fill, "firm / moderate / designed" (structure).
**Speaker notes:** Conclusions, firmest first. First, with high confidence on OULAD: nearly half of the students still
enrolled at day 14, 45.3 percent, did not complete. Rates vary strongly between runs, any year comparison depends on
the add-drop rule, and most non-completers first missed a task after week 4. Second, with moderate confidence: all
five early signs go with later non-completion in both years, a missed task by 40.8 and 39.3 points, in the same
direction across modules. Third, as a design: a penalised logistic model, judged once against the early-sign rule, and
a list limited to staff capacity and audited for fairness. Those outputs are expected, not measured. Equally important
is what we cannot conclude. [click]
**Sources:** [M5 §14; §11.2; §11.3; §11.4]

## Slide 86 – What we cannot conclude   [14 Conclusion]   [Line: main]
**Lead:** We cannot conclude that the signs cause non-completion, that a model ranks students better than the rule, or that contacting a listed student raises completion.
**On the slide:** Not concluded [M5 §14]: the signs cause non-completion · a model ranks students better than the
early-sign rule · contacting a listed student raises completion. · Why: a regression capturing associations is
descriptive rather than causal; questions of effectiveness need a randomised experiment [M5 §14]. · Bounded: on OULAD
(Open University Learning Analytics Dataset), an early list cannot rest on missed tasks alone, and the signs can serve as
reasons staff check beside each name [M5 §14].
**Visual:** three struck-through claims beside the one supported claim (comparison).
**Speaker notes:** Following what we can say, here is what we cannot. We cannot say the signs cause non-completion; a
regression that captures associations describes, it does not explain causes. We cannot say a model ranks students
better than the rule; that test has not been run. And we cannot say that contacting a listed student raises
completion; that needs a randomised experiment. What we can say, within OULAD, is bounded but useful: an early list
cannot rest on missed tasks alone, and the signs can serve as reasons that staff check beside each name. Let me gather
the limits and open problems in one place. [click]
**Sources:** [M5 §14]

## Slide 87 – Limits and open problems   [14 Conclusion; 12 Limitations]   [Line: main]
**Lead:** The answers hold for two years of UK distance-learning modules, and the open problems are the predictive test, the transfer to Vietnam and the effect of contact.
**On the slide:** Limits [M5 §12; §14]: UK distance learning, 2013–2014; KPI (key performance indicator) proxy at day
14; binary click signs, below-median sign weak in 2014 once adjusted; no delivery mode, year of study, attendance,
capacity or contact record; observational design. · Open problems [M5 §12.1; §14]: (1) does a model beat the rule's
list on 13 unseen runs? (2) do the patterns hold on the university's records? (3) whether, and for whom, early contact
improves completion.
**Visual:** two lists, limits and open problems, the third open problem in the accent colour (structure).
**Speaker notes:** Here are the limits in one place. Our answers describe two years of UK distance-learning modules.
The completion KPI is a proxy at day 14. The click signs are binary, and one of them is weak in 2014 once activity is
adjusted. OULAD has no delivery mode, year of study, attendance, staff capacity or contact record. And the design is
observational. Three problems stay open. Does a model beat the rule's list on 13 unseen runs? Do the patterns hold on
the university's own records? And the one that matters most: whether, and for whom, early contact improves
completion. Which brings us to what we would like you to take away. [click]
**Sources:** [M5 §12; §12.1; §14]

## Slide 88 – Take-home and next steps   [14 Conclusion: call to action]   [Line: main]
**Lead:** Do not wait for missed work: watch activity by week 4, use the early-sign rule as the candidate list with reasons beside each name, and test whether contact helps before anyone scales it.
**On the slide:** Take-home: most students who will not complete have not missed a task by week 4 (19.6% and 14.7% had
[M5 §11.2]); their activity already signals the risk; the early-sign rule with its activity part is the candidate list
[M5 §11.5]. · Next steps, in order [M5 §12.1; §14]: 1. run the single AQ3 (predictive) test under the frozen protocol;
2. recount on the university's own records; 3. classify the list's risk; 4. a randomised pilot with contacts and
outcomes logged.
**Visual:** one take-home sentence in large type above a four-step arrow (sequence).
**Speaker notes:** If you remember one thing, let it be this. Most students who will not complete have not missed a
single task by week 4, but their activity already signals the risk. So a list should not wait for missed work. The
early-sign rule, with its activity part, is the candidate list, with the reasons shown beside every name. And here is
what we ask next, in order. Run the single AQ3 test, exactly as frozen. Recount on the university's own records.
Classify the list's risk under Vietnamese law. Then run a randomised pilot, with every contact and outcome logged. That
pilot answers the question no open dataset can: whether early contact helps, and for whom. [click]
**Sources:** [M5 §11.2; §11.5; §12.1; §14]

## Slide 89 – Thank you   [Closing / questions]   [Line: main]
**Lead:** Thank you; we welcome your questions.
**On the slide:** Thank you – questions welcome · Early Identification of Disengaging Students in Online Courses ·
Team N04 · Take-home repeated: by week 4, activity shows what missed tasks do not; test contact before scaling it.
**Visual:** none (closing layout; the take-home line stays visible during questions).
**Speaker notes:** To close where we began: the student in week 5 who has not failed anything, but has gone quiet. On
the data we have, her silence is visible by week 4, well before a missed task would show it. Whether reaching out to
her changes her outcome is the question we have designed carefully but cannot yet answer, and we have tried to be
precise about that line throughout. Thank you for your attention. We are happy to take your questions. [stay on this
slide] If useful, a natural first question is why we did not simply run the predictive model on 2014 now; the answer is
on slide 53.
**Sources:** [M5 §11.2; §14]
