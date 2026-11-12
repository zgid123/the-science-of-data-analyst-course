# Speech script – Early Identification of Disengaging Students in Online Courses

Team N04 · MTH045 – The Science of Data Analytics · Milestone 5 final presentation · 30 slides.

**Big idea (core message).** Staff notice a drifting student only after the window in which help works best, and the
obvious sign, a missed task, comes too late for most non-completers; on two years of open course data, an early-sign
rule that also counts a silent week gives staff a factual reason beside each name now, while a better ranking and the
effect of contact still need one designed test and a randomised pilot.

**SCQA.**

- **Situation.** A Vietnamese university expanding online and blended learning already holds LMS, enrolment and result
  records, and withdrawal is a regulated quality measure [M5 §1].
- **Complication.** Lecturers become sure at week 5 or 6, the program manager sees counts after the semester and the
  support office meets students at its end, while help works best in weeks 2–4; staff can contact only a few students;
  no open dataset of Vietnamese courses exists and no dataset records a contact [M5 §1, §1.1, §1.2, §5.1].
- **Question.** Can records dated by week 4 tell staff, in time and within capacity, whom to contact and why, and how
  much of that can the evidence honestly claim?
- **Answer.** In part, each claim at its own level. On OULAD, 45.3% of the enrolments still registered at day 14 did
  not complete; under one in five non-completers had missed a task by week 4; all five early signs go with later
  non-completion in both years, a missed task by 40.8 and 39.3 points [M5 §11.2, §11.3]. The early-sign rule is the
  candidate list for D1 today; whether a model ranks better is one designed test away, and whether contact helps needs
  a randomised pilot [M5 §11.4, §11.5, §12.1].

**Arc.** Hook and answer first (Slides 1–3) → Part 1, the problem: stakeholders, goal, questions (4–6) → Part 2, the
data: requirements, search, OULAD and its fit (7–9) → Part 3, preparation: quality, the add-drop rule, the early-sign
rule, leakage (10–13; the breadcrumb for the aha is planted on 12) → Part 4, method: methods, judging a list, gate S1,
fairness (14–17) → Part 5, evidence: status, AQ1 size, denominator (the hourglass), the first missed task (**the aha,
Slide 21**), AQ2 signs and robustness (18–23) → Part 6, integration and use: Traceability Matrix, AQ3 and AQ4 expected,
decision support, generative AI (24–27) → conclusions firmest first, limitations and take-home, thank you (28–30).

**Time and pace.** Slot 25 minutes, Q&A outside the slot. Budget at 125 words a minute (non-native presenters), with a
30-second safety buffer: 3,057 scriptable words. Spoken total and verdict: see the timing report beside this file
(`timing-report.txt`); the speaker notes total 3,054 words, about 24:26 at 125 wpm, WITHIN BUDGET (margin 0:34); all three cuts
together bring it to about 21:59. Each slide's
notes open with its start mark and word budget in brackets, e.g. `[7:00 · budget 125]`. Checkpoints: Slide 10 (7:00),
Slide 18 (13:56), Slide 28 (22:00). The timer counts only the speaker notes (a notes-only copy is timed, because the
brief's other fields are not spoken); bracketed directions and comments are not counted.

**How it was ensembled.** Draft A (Storytelling with Data) supplied the hook, the hourglass and the aha and most chart
choices; Draft B (SCQA, pyramid) supplied the answer-first slide, the stakeholder needs, the before/after reasoning of
the data-forced rules and the limitations. Per slide:

| Slide | Source | Slide | Source | Slide | Source |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | A + B, rewritten | 11 | A + B (late registrants) | 21 | A |
| 2 | A | 12 | Rewritten (A12 + B11) | 22 | A |
| 3 | B | 13 | A (cut block added) | 23 | A + B |
| 4 | B + A | 14 | A | 24 | A + B |
| 5 | A + B | 15 | A + B (precision line) | 25 | A |
| 6 | B + A | 16 | A + B, rewritten (cut block) | 26 | A + B |
| 7 | A | 17 | B + A | 27 | A |
| 8 | A (table from B) | 18 | A, rewritten | 28 | A + B |
| 9 | Merged A8 + A9 + B9 | 19 | A notes, B figure | 29 | Rewritten (B24 + B27 + A29) |
| 10 | A + B (cut block) | 20 | A | 30 | B + A, rewritten |

**Cut list (for running long).** Three blocks, marked `<!-- CUT: label -->` … `<!-- END CUT -->` inside the notes:
`quality-detail` (Slide 10), `pipeline-checks` (Slide 13), `development-folds` (Slide 16). Seconds saved per block are
in the timing report. Each slide reads correctly without its block: the opening sentence and the hand-over stay.

**Rules kept.** Every number comes from the Milestone 5 report, with its section tag on the slide and in Sources. AQ3
and AQ4 appear only as designs with expected outputs. AQ2 results are associations, never causes; contact is an
option for a pilot. Team voice "we"; names only on Slide 1. Titles are topic headings; the message sits in the lead.

---

## Slide 1 – Early Identification of Disengaging Students in Online Courses   [Introduction]   (~29 seconds)
**Lead:** A final report on finding students who drift away from online courses early enough to help them.
**On the slide:** Early Identification of Disengaging Students in Online Courses · MTH045 – The Science of Data
Analytics, Milestone 5: Final Integration · Team N04: Lê Ngọc Trúc Huỳnh, Phan Trần Khanh, Dương Tấn Huỳnh Phong ·
Lecturers: Dr. Nguyễn Trần Minh Thư, MSc. Phạm Minh Tú · University of Science, VNU-HCM · 14 November 2026.
**Visual:** none (title, team, date and the university logo only).
**Speaker notes:** [0:00 · budget 62]
Good morning, teachers and friends. We are team N04, and this is our final presentation: Early Identification of
Disengaging Students in Online Courses. Over five milestones we followed one chain, from a problem staff describe, to
the data, their preparation, the method, the evidence, and the decisions it can support. Let's start with the moment
a drifting student is finally noticed. [click]
**Sources:** title page of the Milestone 5 report [M5 title page].

## Slide 2 – Noticed Too Late   [Introduction]   (~45 seconds)
**Lead:** Staff notice a student who has stopped taking part only after the window in which help works best.
**On the slide:** Setting: a Vietnamese university expanding online and blended learning on its learning management
system (LMS); one program of about 1,200 students (scenario assumption) [M5 §1]. Disengagement: a student misses a
task, opens the course less often and falls silent before a fail or withdrawal is recorded [M5 §1]. Window for
effective support: weeks 2–4 [M5 §1]. Lecturers become sure: around week 5 or 6; program manager sees counts: after
the semester; support office meets the student: on the academic warning list at the end of the semester [M5 §1].
Stakes: Circular 01/2024 caps withdrawal at 10% a year and 15% in the first year; Circular 83/2026 keeps these caps
from 15 November 2026 [M5 §1].
**Visual:** timeline of weeks 1–8 and semester end (sequence: the gap between "could help" and "does notice" is the
story); key on the slide: shaded accent band = window for effective support, grey markers = moment each group
notices.
**Speaker notes:** [0:30 · budget 98]
Picture a student in an online course. She misses one assignment, logs in less, then goes quiet. Nothing is recorded
yet: no fail, no withdrawal. When does anyone notice? In our setting, the lecturer becomes sure around week five or six. The program manager sees the numbers after the semester.
The support office meets these students on the warning list, at the very end. But published work puts the window
for effective support between week two and week four. Everyone who could help arrives after it closes. So here is
our answer in brief. [click]
**Sources:** setting, 1,200 (assumption), notice points, the 2–4-week window, withdrawal caps and dates [M5 §1].

## Slide 3 – Our Answer in Brief   [Introduction]   (~59 seconds)
**Lead:** Early records give staff a factual reason beside each name now; whether a model ranks better, and whether
contact helps, still needs one test and a pilot.
**On the slide:** Definitions: non-completion = a fail or a withdrawal; early sign = a record by the end of week 4,
such as a task missed or a week without any platform activity; add-drop period = the first weeks in which students
may still register or drop, which ends at day 14 on our data. Card 1 – Size: 45.3% of the 28,061 enrolments still
registered at day 14 did not complete [M5 §11.2]. Card 2 – Timing: under one in five non-completers had missed a task
by week 4 [M5 §11.2]. Card 3 – Signs: all five early signs go with later non-completion in 2013 and in 2014; a missed
task by 40.8 and 39.3 percentage points [M5 §11.3]. Open (grey strip): the prediction model and the ranked list are
designed, not run; the effect of contact is untested [M5 §10, §11.4].
**Visual:** three cards side by side (structure: three supporting points under one answer) with a grey strip below
for what remains open; no chart.
**Speaker notes:** [1:17 · budget 125]
[pause] Here's the whole talk on one slide. Non-completion means a fail or a withdrawal. An early sign is something
in the records by the end of week four, like a missed task or a week with no activity. Of the twenty-eight thousand
sixty-one enrolments still registered at day fourteen, forty-five point three percent did not
complete. Fewer than one in five of them had missed a task by week four, so a list built on missed tasks alone comes
too late. Yet all five early signs go with later non-completion in both years. That gives staff a
factual reason beside each name today. Not yet measured: whether a model beats a simple rule, and whether contact
helps. Now, how we got here. [click]
**Sources:** 28,061 and 45.3% [M5 §11.2]; under one in five (19.6% and 14.7%) [M5 §11.2]; five signs, 40.8 and 39.3
[M5 §11.3]; design status [M5 §10, §11.4]; day-14 proxy for add-drop [M5 §2.1].

## Slide 4 – Stakeholders, Needs and Decisions   [Part 1 · The Problem (Milestone 1)]   (~47 seconds)
**Lead:** Three groups of staff each take one decision, and all of them asked for a short list with a factual reason
beside each name.
**On the slide:** D1 – whom to contact at each review point: course lecturers, lecturer-advisors (lecturers who
advise a student class) and the support office; operational and reversible [M5 §1.1, §2.1]. D2 – where to place
support time each semester: the program manager [M5 §1.1]. D3 – whether to extend the approach: leadership with legal
staff and the data office; close to irreversible [M5 §1.1, §2.1]. Review point: a moment in week 3 or week 5 when
staff decide whom to contact. Needs: a list at weeks 3 and 5; a factual reason per name; about 30–40 contacts a week
for the support office, three to five for each lecturer-advisor; support only, no automated step [M5 §1.1]. Source of
the needs: simulated interviews, AI on both sides, five stakeholders, 51 key statements, six themes; they motivate the
design and are never evidence [M5 §1.1, App. I].
**Visual:** three decision cards D1–D3 in a row (structure: who decides what), D1 in the accent colour, each tagged
"reversible" or "close to irreversible"; the needs as a band underneath.
**Speaker notes:** [2:17 · budget 98]
Three groups take three decisions. D1 is whom to contact at each review point, in week three or
five; lecturers, lecturer-advisors and the support office take it, and it's reversible. D2 is where the program
manager puts support time. D3 is whether leadership extends the approach, which is close to irreversible. Their needs
come from simulated interviews where AI played both sides, so they shaped the design but are never evidence. All asked
for the same thing: a short list at weeks three and five, with a factual reason beside each name. Next, the goal
behind these decisions. [click]
**Sources:** decisions, deciders, needs, capacities, simulated interviews [M5 §1.1]; reversibility [M5 §2.1]; five
stakeholders, 51 statements, six themes [M5 App. I].

## Slide 5 – Business Goal and KPIs   [Part 1 · The Problem (Milestone 1)]   (~43 seconds)
**Lead:** Success is more students passing, measured by one completion KPI and two contact KPIs.
**On the slide:** Business Goal: improve successful course completion by identifying students who stop taking part
early enough to support them within the semester [M5 §2]. SMART Goal (specific, measurable, achievable, relevant,
time-bound): completion after add-drop in the pilot courses up five points from the recounted baseline (assumed 70% to
75%) by the end of 2027–2028; about four pilot courses, about 600 enrolments (assumptions) [M5 §2]. KPI (key
performance indicator) card: primary – completion rate after add-drop; secondary 1 – students meeting the early-sign
rule at week 4 contacted by the end of week 5; secondary 2 – listed students contacted within seven days [M5 §2.1].
On OULAD: primary KPI has a proxy at day 14 (28,061 enrolments); contact parts measured only in the pilot [M5 §2.1].
**Visual:** a goal tree (structure): Business Goal → SMART Goal → primary KPI and two secondary KPIs; key on the slide:
tag "proxy on OULAD" or "pilot only" beside each KPI; "70% → 75%" in large type marked "assumed".
**Speaker notes:** [3:04 · budget 98]
Those decisions serve one business goal: more students completing their courses, because we spot those who stop
taking part in time. The SMART goal makes it measurable: five more
points of completion in about four pilot courses by the end of the 2027–2028 year, from an assumed baseline of
seventy percent that the real recount replaces. The primary KPI is the completion rate after add-drop. The two
secondary KPIs ask whether contact happens, so they can be measured only in a pilot. Next, the questions that feed the
decisions. [click]
**Sources:** business and SMART goal, pilot size [M5 §2]; KPI definitions, proxy and 28,061 [M5 §2.1, Table 2.1].

## Slide 6 – Four Analytical Questions   [Part 1 · The Problem (Milestone 1)]   (~48 seconds)
**Lead:** Four questions climb the analytics levels, and each answer may claim only what its level allows.
**On the slide:** Unit: one student's enrolment in one module run [M5 §3]. AQ (analytical question) table:
AQ1 descriptive – share of pass, fail and withdrawal; week of the first missed task (D2, D3). AQ2 diagnostic – which
week-4 signs go with later non-completion, within module (D2; reasons in D1). AQ3 predictive – how well data up to
weeks 2 and 4 estimate non-completion, against the early-sign rule, built on 2013 and applied to 2014 (D1). AQ4
prescriptive – who ranks first on a list of fixed capacity, overall and by group (D1) [M5 §3, Table 3.1]. Reading
rule: descriptive = what happened; diagnostic = an association; predictive = foresight on proper validation;
prescriptive from observational data = an option to test [M5 §3]. Data cut-offs: day 13 for the week-3 list, day 27
for the week-5 list [M5 §3].
**Visual:** a four-step ladder, descriptive to prescriptive (structure), each rung labelled with its decision and its
reading rule.
**Speaker notes:** [3:51 · budget 98]
To serve the decisions, we asked four analytical questions on one unit: a student's
enrolment in one course run. AQ1 is descriptive: how many complete, and when do non-completers first miss a task? AQ2
is diagnostic: which signs by week four go with later non-completion? "Go with" means an association, never a cause.
AQ3 is predictive: can a model beat a simple early-sign rule? AQ4 is prescriptive: who should top a list staff can
handle? Each list sees only data up to its cut-off: day thirteen for week three, day twenty-seven for week five.
Where would the data come from? [click]
**Sources:** questions, levels, unit, decisions, reading rule and cut-offs [M5 §3, Table 3.1].

## Slide 7 – Data Requirements   [Part 2 · The Data (Milestone 2)]   (~46 seconds)
**Lead:** We wrote what the data must contain before searching, so the questions chose the data and not the reverse.
**On the slide:** Every question: one enrolment; the population enrolled after add-drop; the final result with a
dated withdrawal [M5 §4]. Each list may use only data recorded up to its cut-off, so every event needs a date [M5 §4].
Six must-have gates: a dated outcome; dated tasks; dated activity; at least three time-ordered runs; an open licence
with provenance; a persistent anonymised identifier [M5 §4]. Gap declared before the search: no dataset records staff
contacts [M5 §4].
**Visual:** a checklist of the six gates (structure); key on the slide: tick box = must-have gate, dashed grey box =
known gap (the contact record).
**Speaker notes:** [4:39 · budget 98]
In Milestone two, before searching, we wrote down what the data must contain, so the questions choose the data.
Every question needs the enrolment, the final result and a dated withdrawal. Above all, every event needs a date,
because a week-three list may only see what happened before its cut-off. That gave six must-have gates: a dated
outcome, dated tasks, dated activity, at least three runs in time order, an open licence, and a stable anonymised
identifier. We also declared one gap in advance: no dataset would record staff contacts. With these gates, we went
searching. [click]
**Sources:** requirement matrix, six gates, contact gap [M5 §4, Table 4.1].

## Slide 8 – Dataset Search and Selection   [Part 2 · The Data (Milestone 2)]   (~47 seconds)
**Lead:** Of seven open candidates, only OULAD passes every gate, so we chose it for fit, not for ease.
**On the slide:** Selection table, scores 0–2 on the brief's ten criteria, gates first [M5 §4.1, Table 4.2]:
OULAD 12 of 20, no gate failed, selected; UCI 697, UCI 320, UCI 856: 10, 6, 7, rejected (dated outcome, tasks,
activity; UCI 320 and 856 also runs); XuetangX, HarvardX: 8, 8, rejected (dated outcome, tasks, licence; HarvardX also
activity and runs); xAPI-Edu-Data: 4, rejected (dated
outcome, tasks, activity, runs). OULAD = Open University Learning Analytics Dataset: the only candidate with a dated
withdrawal, dated submissions and daily clicks; version 1, accessed 6 November 2026, CC BY 4.0 licence, anonymised; no
re-identification [M5 §4.1]. UCI = University of California, Irvine, Machine Learning Repository.
**Visual:** the selection table (comparison across candidates), OULAD row in the accent colour; key on the slide: red
cell = gate failed, accent row = selected.
**Speaker notes:** [5:26 · budget 98]
No open dataset of Vietnamese courses exists, so we needed a stand-in. We screened seven candidates from open
repositories, among them the UCI repository, and scored each from zero to two on the brief's ten criteria, with the
gates deciding first. OULAD, the Open University Learning Analytics Dataset, scores only twelve of twenty,
but every other candidate lacks a dated outcome and dated tasks. OULAD alone records
a dated withdrawal, dated submissions and daily clicks. So we chose it for fit, not for ease. It's openly licensed and
anonymised, and we never re-identify anyone. So what's inside? [click]
**Sources:** candidates, scores, gates, version, access date, licence [M5 §4.1, Table 4.2]; no Vietnamese dataset
[M5 §1.2].

## Slide 9 – OULAD and Its Fit   [Part 2 · The Data (Milestone 2)]   (~48 seconds)
**Lead:** OULAD dates every outcome, task and click, but lacks delivery mode, year of study, attendance and any
contact record.
**On the slide:** 22 runs of seven UK distance-learning modules (AAA–GGG), 2013 and 2014 [M5 §5]. Module run: one
offering of a module, named by year and start month (B = February, J = October), the counterpart of a semester; days
count from day 0, the run's start [M5 §5]. 32,593 enrolments of 28,785 students: Pass 12,361; Withdrawn 10,156; Fail
7,052; Distinction 3,024; completion = Pass or Distinction [M5 §5]. 2013: 9 runs, six modules, 13,529 enrolments;
2014: 13 runs, all seven modules, 19,064 enrolments [M5 §5]. Fit rating (GREEN = data enough; YELLOW = question
narrowed; RED = a key concept, variable or intervention missing): AQ1–AQ3 YELLOW; AQ4 RED, no contact data, ranking
part only [M5 §5.1, Table 5.2]. Nothing imputed or simulated; no question dropped [M5 §5.1].
**Visual:** one 100% stacked horizontal bar of the four final results with counts labelled directly (part-to-whole
without a pie); key on the slide: grey = Pass and Distinction (completion), accent = Fail and Withdrawn
(non-completion). Below it four fit chips coloured GREEN/YELLOW/RED with the colour key beside them.
**Speaker notes:** [6:13 · budget 98]
OULAD covers twenty-two runs of seven distance-learning modules at the Open University in the UK, in 2013 and
2014. A run is one offering of a module, our counterpart of a semester. It holds thirty-two thousand five hundred
ninety-three enrolments, each with a final result; completion means pass or distinction. Nine runs fall in 2013 and
thirteen in 2014. In Milestone three we rated each question against these data. AQ1 to AQ3 are yellow: we narrowed
them, because OULAD has no delivery mode, year of study or attendance. AQ4 is red: no contact record, so only its
ranking part stays. [click]
**Sources:** runs, modules, enrolments, students, outcome counts, year splits [M5 §5]; fit ratings and handling
[M5 §5.1, Table 5.2].

## Slide 10 – Data Quality   [Part 3 · Preparation (Milestone 3)]   (~61 seconds)
**Lead:** Of nineteen quality issues, three are serious enough to change the method.
**On the slide:** Profile of all 10.9 million rows of the seven raw tables; 13 figures recounted independently, all 13
agree [M5 §6]. Issue log: 19 issues, rated High (would change a rate, the target or a feature), Medium (changes a
measure by a known amount) or Low [M5 §6.1]. Three High issues → decision: 18 of 24 exams have no result rows → tasks
mean TMAs and CMAs only (TMA = tutor-marked assignment; CMA = computer-marked assessment, a quiz); few tasks due by the
cut-offs → the early-sign rule needs an activity part; seven UK modules of 2013–2014 → scope stated, comparisons
within module [M5 §6.1, Table 6.2]. Medium, by known amounts: duplicate click rows, 7.39% of rows, whose removal would
drop 3.19% of clicks → a de-duplicated twin of each click feature [M5 §6.1]. Activity is skewed: median 602 clicks,
3,365 enrolments without any click → counts as logarithms, no value removed [M5 §6].
**Visual:** three-row table of the High issues, each with an arrow to its change in method (structure); accent bar on
the second row, the one that returns on Slide 12.
**Speaker notes:** [7:00 · budget 125] [checkpoint 1: on time if this slide starts by 7:00]
Next, quality: nineteen issues, and three serious enough to change the method.
<!-- CUT: quality-detail -->
[if behind by more than 30 seconds: skip to the last sentence]
We profiled all ten point nine million rows, and recounted thirteen key figures with separate code;
all thirteen agreed. We rated each issue by whether ignoring it would change a rate, the target or a feature. First,
eighteen of twenty-four exams have no result rows, so a task means an assignment or a quiz, never the exam. Second,
few tasks fall due in the first weeks; keep that one in mind for later. Third, these are seven UK modules from two years, so we
compare students only within the same module. Clicks are very skewed, with a median of six hundred two, so we use
logarithms and remove nothing.
<!-- END CUT -->
Two of these facts forced changes. [click]
**Sources:** profile and recount, click distribution [M5 §6]; issue log, severities, High issues, 7.39% and 3.19%
[M5 §6.1, Table 6.2].

## Slide 11 – Who Counts: the Add-drop Rule   [Part 3 · Preparation (Milestone 3)]   (~43 seconds)
**Lead:** We count only students still registered at day 14, because that is when registration closes on OULAD.
**On the slide:** University rule: completion counts students enrolled after the add-drop period [M5 §1.2]. OULAD
proxy: an enrolment counts when it is still registered at day 14, because registration closes two weeks after a run
starts [M5 §2.1]. 58 enrolments registered after day 14, so one rule serves every population: day 14 for the
completion rate (28,061 enrolments), day 13 (28,069) and day 27 (27,535) for the two lists [M5 §2.1, §6, Table 6.1;
App. III, Table A.8]. The denominator alone can move a run's rate by up to 13.6 points (Slide 20) [M5 §11.2].
**Visual:** a day axis from day 0 to day 27 (sequence) with three markers, day 13, day 14 and day 27, each labelled with
its population; key on the slide: accent marker = KPI population, grey markers = list populations.
**Speaker notes:** [8:00 · budget 98]
The first change is about who counts. At the university, the completion rate counts only students enrolled
after the add-drop period, because those who leave during add-drop never really started. OULAD has no add-drop
field, but registration closes two weeks after a run starts. So an enrolment counts if it's still registered at day
fourteen. That leaves twenty-eight thousand sixty-one enrolments for the KPI. Fifty-eight enrolments registered even later, so the
same rule defines the lists at day thirteen and day twenty-seven. The second change is about the early sign. [click]
**Sources:** university rule [M5 §1.2]; day-14 proxy, 28,061 [M5 §2.1, Table 2.1]; populations at days 13 and 27
[M5 §6, Table 6.1]; 58 late registrants [M5 §6.1, Table 6.2; App. III, Table A.8]; 13.6 points [M5 §11.2].

## Slide 12 – The Early-sign Rule   [Part 3 · Preparation (Milestone 3)]   (~48 seconds)
**Lead:** Few tasks fall due in the first weeks, so the early-sign rule also counts a week without activity.
**On the slide:** Milestone 1 rule: two or more assessed tasks missed or late by week 4. Why it changed: two or more
tasks fall due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1 [M5 App. III, Table A.8]; no 2013 run has
a task due by day 13 [M5 §6.1]. Early-sign rule (final): by the data cut-off, a TMA or CMA due but not submitted, or a
TMA submitted late, or no platform activity in the previous seven days [M5 §2.1]. One rule on OULAD and in the pilot
[M5 §2.1]. Late quizzes stay out: counting them would raise the share flagged at day 27 from 28.8% to 41.2%
[M5 §6.1]. At day 27 the rule flags 28.8% of 27,535 enrolments [M5 §2.1].
**Visual:** simple text "1 of 22 runs" (two tasks due by day 27) in large type, with the rule's three parts as three
icons below (single key number); key on the slide: accent icon = the activity part added for the data.
**Speaker notes:** [8:47 · budget 98]
In Milestone one, interviews said the first sign is usually a missed quiz or assignment, so our rule was two or
more tasks missed or late by week four. The data said no. Two tasks fall due by day twenty-seven in only one of
twenty-two runs; even one task, in only sixteen. A task-only rule can't fire in many runs. So the final early-sign
rule has three parts: a task due and not submitted, an assignment submitted late, or no platform activity in the last
seven days. One rule serves OULAD and the pilot. Next, keeping the future out. [click]
**Sources:** Milestone 1 rule and task counts by cut-off [M5 App. III, Table A.8]; 2013 runs, late quizzes
[M5 §6.1]; final rule, one rule, 28.8% of 27,535 [M5 §2.1, Table 2.1]; interview theme [M5 App. I].

## Slide 13 – Preparation and Leakage Control   [Part 3 · Preparation (Milestone 3)]   (~58 seconds)
**Lead:** Every feature uses only events dated on or before its cut-off, and every learned value comes from 2013 alone.
**On the slide:** Leakage: using information that would not exist at the moment of prediction [M5 §7.1]. Three
governing decisions: nothing recorded is deleted or imputed; every feature uses only events up to its cut-off; every
learned parameter comes from the training runs [M5 §7]. Blocked by: the timing rule; learning on 2013 only; the split
by year; 1,586 test enrolments at day 27 of students already seen in 2013 flagged [M5 §7.1]. Features: 19 usable
predictors, 23 parameters once module and start month are coded [M5 §7.1]. Result: one versioned prepared dataset;
all 22 validation checks pass; 32,593 enrolments and their outcome mix unchanged; six features recomputed from raw by
separate code differ in none of 55,604 feature rows; 88 variables documented; one command rebuilds it [M5 §7.2].
**Visual:** a timeline cut at day 27 (worked example); key on the slide: grey = events left of the line that may feed
a feature; accent cross = events right of the line that never enter (later clicks, withdrawal day, final result).
**Speaker notes:** [9:34 · budget 125]
Preparation guards against leakage: using information that wouldn't exist when the list is made.
<!-- CUT: pipeline-checks -->
[if behind by more than 30 seconds: skip to the last sentence]
So every feature uses only what was recorded by its cut-off. Two more rules govern the pipeline: nothing recorded is
deleted or imputed, and every learned value comes from the 2013 runs alone, so the 2014 runs stay unseen. On the timeline,
everything right of the line is crossed out: later clicks, the withdrawal day, the final result. We also split by
year, and flag one thousand five hundred eighty-six test enrolments of students already seen in 2013. All twenty-two
validation checks pass, and features rebuilt from raw by separate code match in all fifty-five thousand six hundred
four rows.
<!-- END CUT -->
Now, which method for which question? [click]
**Sources:** governing decisions [M5 §7]; leakage definition and controls, 1,586, predictors [M5 §7.1]; checks,
recomputation, 55,604, dictionary, rebuild [M5 §7.2].

## Slide 14 – Methods by Question   [Part 4 · Method (Milestone 4)]   (~48 seconds)
**Lead:** Each question gets the simplest method that fits its level, judged against a baseline it must beat.
**On the slide:** Method / baseline [M5 §8.1, Table 8.1]: AQ1 – grouped rates with Wilson intervals (the 95% interval
of a share); two denominators / pooled rate, rate over all enrolments. AQ2 – logistic regression with run fixed
effects (a term per module run, so students are compared only within their run) and sign × module terms; effects as
average risk differences (the difference in later non-completion, in percentage points, with and without a sign) /
unadjusted rate difference. AQ3 – penalised logistic regression on the 19 predictors; challenger: gradient-boosted
trees / the early-sign rule ranked by its number of signs, a background-only model, a random list. AQ4 – top-k list
per run (the k highest-ranked students) from the AQ3 scores, with the signs behind each name / random list,
rule-ranked list. Eight course criteria; ties go to the simpler, more interpretable method [M5 §8.1].
**Visual:** four-row table, question · method · baseline (structure: every method has something to beat); key on the
slide: accent column = baseline.
**Speaker notes:** [10:34 · budget 98]
In Milestone four we chose a method for each question without training any model. The rule: the simplest method
that fits, and always a baseline to beat. AQ1 needs no model, only rates with Wilson intervals. AQ2 uses a logistic
regression with a term for each run, so students are compared only within their own run, and it reports risk
differences in percentage points. AQ3 proposes a penalised logistic regression, because staff need a reason beside
each name, and it must beat the early-sign rule. AQ4 cuts those scores into a short list per run. How do we judge it?
[click]
**Sources:** methods, baselines, criteria, tie rule [M5 §8, §8.1, Table 8.1].

## Slide 15 – Judging a Contact List   [Part 4 · Method (Milestone 4)]   (~49 seconds)
**Lead:** A list is judged by how many later non-completers it reaches against the most a list of its length could
reach.
**On the slide:** Capacity k: 3 or 5 contacts per 20 students, that is 15% or 25% of a run; main operating point 5 per
20 at day 27 [M5 §9, §8]. Recall at capacity: share of a run's non-completers who are on its list [M5 §9]. Normalised
recall: recall divided by the most a list of length k can reach; that ceiling ranges from 46% to 100% between training
runs [M5 §9]. Lift: share of non-completers on the list divided by the run's base rate (the share of the run who do
not complete); 1 = chance [M5 §9]. Why rank: the rule names 28.8% at day 27, more than a list of 15% or 25% can hold
[M5 §8]. Why not "precision of at least 50%" (Milestone 1): with non-completion near 45%, a random list already reaches
about 45% precision [M5 App. III, Table A.8].
**Visual:** worked example: 20 student icons, 9 later non-completers filled in the accent colour, a box around a list
of 5; caption computes recall 4 of 9 and normalised recall 4 of 5 for this illustrative group; key on the slide:
filled = later non-completer, box = on the list; the icons are an illustration, not data.
**Speaker notes:** [11:21 · budget 98]
Capacity fixes the list length: three or five per twenty. A toy
example: twenty students, nine won't complete, a list of five. If four of our five are right, recall is four of nine.
But five is the most a list of five can reach, so normalised recall is four of five, because that
ceiling ranges from forty-six to one hundred percent between runs. Lift compares the list with the run's base rate; one means
chance. And we must rank: the rule names twenty-eight point eight percent at day twenty-seven, more than any list
holds. So when is a model good enough? [click]
**Sources:** capacity, operating point, metrics, ceiling range [M5 §9]; 28.8%, 15% or 25% [M5 §8]; precision limit
[M5 App. III, Table A.8].

## Slide 16 – Validation and Gate S1   [Part 4 · Method (Milestone 4)]   (~63 seconds)
**Lead:** The model is built on 2013 and scored once on all 13 runs of 2014, under a protocol frozen in advance.
**On the slide:** Frozen protocol: evaluation choices fixed in advance so the test runs are scored once [M5 §9.1].
Development: leave-one-run-out folds on the 9 runs of 2013 (each run held out in turn); a challenger replaces the
primary model only with a gain of at least 0.03 in pooled normalised recall and in 7 of 9 folds [M5 §9.1]. Test: the
frozen model scored once on the 13 runs of 2014; 9 paired and 4 unpaired runs also reported apart [M5 §9.1]. Gate S1:
the model's pooled normalised recall must exceed the rule list's, with the paired bootstrap interval above 0 and a
sign-flip test p below 0.05 [M5 §9, Table 9.1]. Probabilities shown only if calibration holds (predicted risks match
observed rates) [M5 §9.1]. AQ2 criterion: risk difference of at least 5 points, interval excluding 0, same direction
in at least two-thirds of modules; p-values take no part [M5 §9, §9.1, Table 9.1].
**Visual:** two blocks, "2013: build and choose" (grey) and "2014: score once" (accent), joined by an arrow through a
lock icon (sequence); key on the slide: lock = protocol frozen before any 2014 outcome is used.
**Speaker notes:** [12:09 · budget 125]
The key word is "once". Under gate S1, the model's list must clearly beat the rule's list on the 2014 runs, or
the simple rule stays.
<!-- CUT: development-folds -->
[if behind by more than 30 seconds: skip to the last sentence]
Clearly means an interval above zero and a test below zero point zero five, scored once on all thirteen runs. Every
choice before that is made on the nine runs of 2013, holding out one run at a time. A more complex challenger replaces
the primary model only with a gain of at least zero point zero three in normalised recall, in at least seven of nine
folds. The test year even includes a module, CCC, that the model has never seen. And probabilities are shown only if calibration
holds, that is, if predicted risks match observed rates.
<!-- END CUT -->
A good list also has to be fair. [click]
**Sources:** frozen protocol, folds, challenger rule, test runs, calibration [M5 §9.1]; gate S1 and AQ2 criterion
[M5 §9, Table 9.1]; module CCC only in 2014 [M5 §6.2].

## Slide 17 – Fairness and Interpretability   [Part 4 · Method (Milestone 4)]   (~48 seconds)
**Lead:** The list is audited for equal recall across groups, and every name carries reasons from the model that
ranked it.
**On the slide:** Group attributes stay out of the predictors and are kept only for the audit, because bias cannot be
audited without group membership [M5 §9.2, §6.2]. Criterion: equal recall at capacity [M5 §9.2]. Rule FR1 (fairness
review rule): flag a group for human review when its recall is more than 10 points below the other students' and the
Holm-adjusted (corrected for several tests) one-sided interval of the gap lies below 0 [M5 §9.2]. Confirmatory groups
in the 2014 test at day 27: declared disability 1,488 enrolments; most deprived band 1,486; missing deprivation band
610 [M5 §9.2]. No flag = no evidence of a gap at that precision, not proof that the list is fair [M5 §9.2]. Reasons
come from the same model that ranks the student; no coefficient is read as a cause [M5 §9.2].
**Visual:** three group cards with their sizes (structure, not a result: no recall values exist) and the FR1
threshold drawn as a 10-point gap bar; key on the slide: bar = largest gap allowed before review.
**Speaker notes:** [13:09 · budget 98]
A list could still miss a whole group. Group attributes stay out of the predictors, but we keep them for the audit, because bias can't be audited without knowing
group membership. Rule FR1 flags a group for human review when its recall is more than ten points below the other
students', and the interval of that gap, corrected for several tests, lies below zero. We check three groups in the
test year. No flag means no evidence of a gap, not proof of fairness. And each name's reasons come from the model that
ranked it. So what have we run? [click]
**Sources:** audit rationale, FR1, groups and sizes, reasons [M5 §9.2]; sensitive attributes [M5 §6.2].

## Slide 18 – What We Ran   [Part 5 · Evidence (Milestone 5)]   (~48 seconds)
**Lead:** We answered AQ1 and AQ2 on both years; AQ3 and AQ4 remain complete designs with no model trained.
**On the slide:** Level 1, the compulsory level (modeling strategy and evaluation design): complete [M5 §10]. AQ1 and
AQ2: run as fixed in Milestone 4, on the 9 runs of 2013 and again on the 13 runs of 2014; no predictive model trained;
nothing in the AQ3 design changed [M5 §10, §11]. AQ3 and AQ4: designed in full; no model trained, so no model metric
exists; the 13 runs of 2014 are kept as the one independent test [M5 §10]. Status: AQ1 Answered; AQ2 Answered; AQ3
Deferred; AQ4 Deferred; none dropped [M5 §3, Table 3.1]. Answered = results answer all of the question; Deferred =
design complete, no result yet [M5 §3].
**Visual:** four status chips (comparison of status at a glance); key on the slide: filled accent chip = Answered,
grey outline = Deferred.
**Speaker notes:** [13:56 · budget 98] [checkpoint 2: on time if this slide starts by 14:00]
A word on status. Level one, the compulsory level, is complete: the modeling
strategy and the evaluation design. AQ1 and AQ2 need no predictive model, so we ran them as Milestone four fixed them,
on the nine runs of 2013 and again on the thirteen runs of 2014. AQ3 and AQ4 are designed in full, but no model has
been trained, so there's no model metric in this talk. That's our choice of scope: the 2014 runs are our only
independent test, and we keep them for one complete run of the frozen protocol. First, the size of the problem.
[click]
**Sources:** Level 1 status, scope choice, no model trained [M5 §10]; AQ1 and AQ2 runs [M5 §11]; statuses and their
meaning [M5 §3, Table 3.1].

## Slide 19 – AQ1: How Many Do Not Complete   [Part 5 · Evidence (Milestone 5)]   (~47 seconds)
**Lead:** Close to half of the students still registered at day 14 do not complete, and the two years agree.
**On the slide:** 45.3% (44.7–45.8) of 28,061 enrolments did not complete (12,700) [M5 §11.2, Figure 11.1]. 2013:
45.7% (44.8–46.6) of 12,076; 2014: 44.9% (44.2–45.7) of 15,985 [M5 §11.2]. About a quarter failed, a fifth withdrew
[M5 §11.2]. Modules: 26.3% (AAA) to 54.3% (CCC, 2014 only); February runs exceed October runs in both years
[M5 §11.2]. Check: prepared views and raw tables agree in all 176 outcome cells [M5 §11.2]. Wilson interval: the 95%
interval of a rate, in brackets.
**Visual:** the report's Figure 11.1 (comparison): non-completion per module in 2013 and 2014, students registered at
day 14, axis from 0; "45.3%" as a large callout; key on the slide: bar colour = year (2013 grey, 2014 accent), whisker
= 95% Wilson interval, dashed line = pooled rate 45.3% (12,700 of 28,061).
**Speaker notes:** [14:43 · budget 98]
Of the twenty-eight thousand sixty-one enrolments still registered at day fourteen, forty-five point three
percent did not complete, with a narrow interval, forty-four point seven to forty-five point eight. The two years
agree: forty-five point seven in 2013, forty-four point nine in 2014. Roughly a quarter failed and a fifth withdrew.
Bars are modules by year; the dashed line is the pooled rate. Modules range from twenty-six point
three percent in AAA to fifty-four point three in CCC. Two independent computations agree in all one hundred
seventy-six outcome cells. But one choice moves these rates a lot. [click]
**Sources:** pooled and yearly rates, intervals, shares, module range, February and October, 176 cells [M5 §11.2];
12,700 [M5 §11.2, Figure 11.1 caption].

## Slide 20 – AQ1: The Denominator Matters   [Part 5 · Evidence (Milestone 5)]   (~48 seconds)
**Lead:** Who counts as enrolled can move a run's rate by 13.6 points and reverse the year comparison, so the KPI must
fix the add-drop rule.
**On the slide:** Run rates span 24.9% (AAA 2013J) to 58.3% (CCC 2014B) [M5 §11.2]. The denominator alone moves a
run's rate by up to 13.6 points (BBB 2014J) [M5 §11.2]. 2014 minus 2013: over all enrolments +2.3 points (1.2 to 3.4);
registered at day 14 −0.7 points (−1.9 to 0.5); six modules run in both years −3.5 points (−4.8 to −2.3) [M5 §11.2].
Why: 16.2% of 2014 enrolments against 10.7% of 2013 were not registered at day 14 [M5 §11.2].
**Visual:** dot-and-whisker chart of the three year differences against a zero line (comparison); key on the slide:
dot = 2014 minus 2013 in points, whisker = 95% interval, accent = registered at day 14 (the KPI rule), grey = the other
two denominators.
**Speaker notes:** [15:30 · budget 98]
Runs differ, from twenty-four point nine percent in AAA 2013J to fifty-eight point three in
CCC 2014B, and the denominator alone moves one run's rate by up to thirteen point six points. Now the years. Count
every enrolment, and 2014 looks worse by two point three points. Count only those registered at day fourteen, and
2014 is slightly better, with an interval including zero. In the six modules run in both years, it's three point five
points better. Same data, opposite stories, because more 2014 enrolments left before day fourteen: sixteen point two
percent against ten point seven. Now, timing. [click]
**Sources:** run range, denominator shift, year differences and intervals, shares not registered [M5 §11.2].

## Slide 21 – AQ1: When Non-completers First Miss a Task   [Part 5 · Evidence (Milestone 5)]   (~61 seconds)
**Lead:** Most non-completers miss a task at some point, but under one in five has missed one by week 4.
**On the slide:** What staff expected: the first sign is usually a missed quiz or assignment (simulated interviews)
[M5 App. I]. Non-completers who missed a TMA or CMA during the run: 78.1% (2013), 72.7% (2014); completers: about one
in five [M5 §11.2]. Non-completers who had missed one by week 4: 19.6% (2013), 14.7% (2014) [M5 §11.2]. So: a rule on
tasks alone comes too late for most non-completers, which is why the early-sign rule counts inactivity [M5 §11.2].
Confidence: high for OULAD 2013–2014; the first missed week agrees for all 32,593 enrolments in two independent
computations; validity for the university's courses remains open [M5 §11.2].
**Visual:** horizontal bar chart, two pairs (2013, 2014), axis 0–100%, values labelled directly (comparison: the short
accent bars are the point); key on the slide: grey = missed a task during the run, accent = missed a task by week 4;
population: non-completers registered at day 14.
**Speaker notes:** [16:17 · budget 125]
[pause] Now the moment this talk was built around. Staff told us the first sign is usually a missed quiz or
assignment. And missing a task does separate the groups: seventy-eight point one percent of non-completers in 2013,
and seventy-two point seven in 2014, missed a task at some point, against about one in five completers. [point at the
accent bars] Now look at the short bars. By the end of week four, when the week-five list is made, only nineteen point
six percent of non-completers in 2013, and fourteen point seven in 2014, had missed one. A list built on missed tasks
alone arrives too late for most of the students it should reach. That's why our rule also counts a silent week. So,
does silence matter? [click]
**Sources:** missed-task shares, by-week-4 shares, conclusion, confidence and timing check [M5 §11.2]; completer
shares checked as 21.9% and 19.4% [M5 App. XII, Table A.31]; stakeholder expectation [M5 App. I].

## Slide 22 – AQ2: Five Early Signs   [Part 5 · Evidence (Milestone 5)]   (~49 seconds)
**Lead:** All five early signs, inactivity included, go with later non-completion within module, by similar amounts in
2013 and 2014.
**On the slide:** Population: registered at day 27; 2013: 11,811 enrolments (44.4% non-completion); 2014: 15,724
(44.0%) [M5 §11.3]. Risk difference: extra percentage points of later non-completion among enrolments with the sign
against those without, within module run, adjusted for the other signs. 2013 / 2014: missed task 40.8 (37.7–43.9) /
39.3 (36.4–42.1); late TMA 20.2 / 20.3; no click in the last seven days 14.5 / 15.8; activity below the run median
13.4 / 14.6; no click before the start 10.6 / 8.7 [M5 §11.3]. Criterion: at least 5 points, interval excluding 0, same
direction in two-thirds of modules [M5 §9, Table 9.1]. Task signs: runs with a task due by day 27 (9,960 and 12,585
enrolments) [M5 §11.3]. Associations, not causes [M5 §11.3].
**Visual:** the report's Figure 11.2 as a dot plot with 95% intervals, five signs as rows sorted by size, dashed line at
5 points (comparison with uncertainty); key on the slide: grey dot = 2013, accent dot = 2014, whisker = 95% interval,
dashed line = 5-point criterion; task signs on runs with a task due, click signs on all runs.
**Speaker notes:** [17:17 · budget 98]
AQ2 answers that. Each dot is a risk difference: how many more percentage points of
non-completion among students with the sign than without it, within the same run. A missed task: forty point eight in
2013, thirty-nine point three in 2014. A late assignment: twenty point two and twenty point three. No click in the last
seven days: fourteen point five and fifteen point eight. Activity below the run median: thirteen point four and
fourteen point six. No click before the start: ten point six and eight point seven. All five clear the five-point line
in both years. How firm is this? [click]
**Sources:** populations, estimates, intervals, task-sign runs [M5 §11.3, Figure 11.2]; criterion [M5 §9, Table 9.1].

## Slide 23 – AQ2: How Far the Signs Hold   [Part 5 · Evidence (Milestone 5)]   (~49 seconds)
**Lead:** The signs keep their direction across modules and checks, but the click signs are coarse, and every result
is an association, not a cause.
**On the slide:** No sign moves by more than two points between the years [M5 §11.3]. Each sign keeps its direction in
every module and under six sensitivity runs (repeats of an estimate under a changed choice), in both years [M5 §11.3].
Exception: late TMA in AAA 2014, −1.2 points on 348 enrolments, interval −14.4 to 12.1, includes 0; no CCC student had
a late TMA by day 27 [M5 §11.3]. With clicks added as a continuous adjustment, activity below the run median falls to
5.8 points (2013) and 5.9 (2014); in 2014 it keeps its direction in only 4 of 7 modules and no longer meets the
criterion; the other four signs still do [M5 §11.3]. Confidence: moderate – two years agree, but the click signs rest
on a known misfit and unrecorded reasons could explain the associations [M5 §11.3].
**Visual:** simple text "13.4 → 5.8 points" for the below-median sign (2013), beside a three-item checklist (years
agree, modules agree, sensitivity runs agree) (single key number); key on the slide: tick = check passed, amber mark =
the one exception.
**Speaker notes:** [18:04 · budget 98]
We tried to break this result. Between the years, no sign moves by more than two points, and each keeps its
direction in every module and under six sensitivity runs. One small exception: a late assignment in AAA in 2014, on
three hundred forty-eight students, with an interval including zero. One real weakness: our click signs are yes or
no. With clicks added as a continuous measure, below-median activity shrinks to five point eight points in 2013, and
in 2014 it no longer meets our criterion. The other four signs still do. So confidence is moderate, and these are
associations, not causes. [click]
**Sources:** stability, sensitivity runs, exception, continuous adjustment, confidence [M5 §11.3]; criterion [M5 §9,
Table 9.1].

## Slide 24 – Traceability Matrix   [Part 6 · Integration and Use (Milestone 5)]   (~43 seconds)
**Lead:** For AQ1 and AQ2 every link from goal to decision holds evidence; for AQ3 and AQ4 the chain stops at the
evaluation design.
**On the slide:** One row per question: goal and KPI → data → preparation → method → evaluation → decision → status
[M5 §11.1]. AQ1: primary KPI; 22 runs, day 14: 28,061; day-14 rule; grouped rates; paths agree, 45.3%; D2, D3;
Answered. AQ2: primary KPI and KPI 1; day 27: 11,811 and 15,724; dated by day 27; logistic, run effects; 5 of 5 signs,
both years; D2, D1; Answered. AQ3: KPI 1 (rule to beat); 19 predictors, 2014 test; refit per fold; penalised logistic;
S1 planned, N.A.; D1; Deferred. AQ4: KPIs 1–2 GAP; contacts GAP; 3 or 5 per 20; top-k with signs; S1, FR1, N.A.; D1;
Deferred [M5 §11.1, Tables 11.1–11.2]. GAP = a link without evidence; N.A. = no result exists [M5 §11.1].
**Visual:** condensed matrix, four rows by seven links (structure: where the chain holds and where it stops); key on
the slide: filled grey cell = evidence, outlined cell = GAP or N.A., accent column = status.
**Speaker notes:** [18:51 · budget 98]
The Traceability Matrix puts all four side by side. Each row follows one question from goal to
decision. In the first two rows every
link holds evidence. AQ1 rests on twenty-eight thousand sixty-one enrolments and feeds D2 and D3. AQ2 rests on both
years and five of five signs, and feeds D2 and the reasons for D1. GAP marks only what OULAD lacks: delivery mode, year
of study, attendance, contacts. The last two rows stop at the evaluation design, marked N.A. So what would AQ3 and AQ4
give? [click]
**Sources:** matrix rows and statuses [M5 §11.1, Tables 11.1–11.2].

## Slide 25 – AQ3 and AQ4: Expected Outputs   [Part 6 · Integration and Use (Milestone 5)]   (~48 seconds)
**Lead:** AQ3 and AQ4 would give a ranked, capacity-limited list with reasons, and the simple rule stays if the model
does not beat it.
**On the slide:** AQ3 would give: a risk rank per enrolment at days 13 and 27; a probability only if calibration
holds; answered by gate S1 on the 13 runs of 2014 [M5 §11.4]. If the model does not beat the rule: the rule's order
stays, its list measured as a baseline [M5 §11.4]. AQ4 would give: a list of 3 or 5 per 20 students per run, with the
signs behind each name; answered when it meets S1, rule FR1 passes or its flags are reviewed, and the risk order is
stated as untested for need [M5 §11.4]. Neither says who should make contact or whether contact helps [M5 §11.4].
Status: Deferred; expected outputs, no model metric [M5 §11.1, §11.4].
**Visual:** a mock list card labelled "expected output – not a result": five placeholder rows, each with a reason tag
(missed task, late assignment, silent week), no names and no numbers (worked example of the form only); key on the
slide: tag = sign behind the name.
**Speaker notes:** [19:39 · budget 98]
For AQ3 and AQ4 we can show only the shape of the answer; this card is a mock-up with no data. AQ3 would give
each enrolment a risk rank, with a probability only if calibration holds. Gate S1
decides it once, on the 2014 runs. If the model doesn't beat the rule, the rule's order stays. AQ4 would cut the
ranking to three or five names per twenty students, each with its signs, and must also pass the fairness rule or have
its flags reviewed. Neither says who should call, or whether calling helps. So what can decisions use today? [click]
**Sources:** expected outputs, gate, fallback, conditions, limits [M5 §11.4]; status [M5 §11.1].

## Slide 26 – Decision Support   [Part 6 · Integration and Use (Milestone 5)]   (~48 seconds)
**Lead:** The early-sign rule is the candidate list for whom to contact; the patterns are a hypothesis for where
support goes; the design is a method for whether to extend.
**On the slide:** D1 – whom to contact (reversible): the early-sign rule as the candidate list; interpretable,
computable from records the university already holds, each part goes with later non-completion in 2013 and in 2014; a
member of staff checks every name [M5 §11.5, §2.1]. The rule names 28.8% at day 27, so ranking within capacity is the
next test [M5 §8, §11.4]. D2 – where support time goes: first where non-completion and early signs are highest, as a
hypothesis for the university's records [M5 §11.5]. D3 – whether to extend (close to irreversible): a measurement
method, a gate and a fairness audit; extension waits for a pilot result [M5 §11.5, §2.1]. Decision option: a
statement from observational data offered as a hypothesis for the pilot, not a proven remedy [M5 §11.5].
**Visual:** the three decision cards of Slide 4 again (structure; the arc returns to the setting), each now with "what
it gets" and "what it still needs"; key on the slide: accent = usable now (D1), grey = waits for the pilot.
**Speaker notes:** [20:26 · budget 98]
D1, whom to contact, is reversible, so it can start with the early-sign rule:
computable from records the university already holds, and each part went with later non-completion
in both years. A staff member checks every name; nothing is automated. Since the rule names more students than staff
can reach, ranking within capacity is the next test. D2 gets a hypothesis: put early support time first where
non-completion and early signs are highest, to check on the university's records. D3 gets a measurement method, a
gate and a fairness audit, and waits for a pilot. How did AI help? [click]
**Sources:** decision support and decision option [M5 §11.5, Table 11.3]; reversibility and staff check [M5 §2.1];
28.8% [M5 §2.1, §8].

## Slide 27 – Generative AI Use   [Part 6 · Integration and Use (Milestone 5)]   (~46 seconds)
**Lead:** AI proposed and challenged, and we verified; it was never a source of data, statistics or results.
**On the slide:** Roles: simulated stakeholder; research and code assistant; critic; writing partner [M5 §13]. One
rule: AI is never a source of data, statistics, licence information or results; every fact it offered was checked
against a saved source, the data files or code we ran [M5 §13]. No AI produced a metric value, threshold or result
[M5 §13.1]. Checks matched to risk: quotes against transcripts; literature against saved copies; code against fixtures
and independent recounts; critics confined to the brief and the data [M5 §13.2]. Where it helped most: a critic found
tasks due before registration counted as missed, and a leakage check that could not fail [M5 §13.2]. Decisions that
stayed ours: keep 2014 out of every AQ3 choice; one early-sign rule; AQ3 and AQ4 as designs; every association stated
as an association [M5 §13.2].
**Visual:** a two-column panel (structure): four role chips under "AI proposed" leading into one "we verified with"
column of checks.
**Speaker notes:** [21:13 · budget 98]
We used generative AI in four roles: simulated stakeholder, research and code assistant, critic, and writing
partner. One rule held in all four: AI was never a source of data, statistics or results. Everything it offered, we
checked against a saved source, the data, or code we ran. It helped most as a critic: in
Milestone three it caught tasks due before a student registered being counted as missed, and a leakage check that
could never fail. The key decisions stayed ours, such as keeping 2014 out of every AQ3 choice. So, what can we
conclude? [click]
**Sources:** roles, rule, checks, critic findings, decisions [M5 §13, §13.1, §13.2].

## Slide 28 – Conclusions   [Conclusions]   (~59 seconds)
**Lead:** On OULAD, an early list cannot rest on missed tasks alone, and the early signs can serve as reasons that
staff check beside each name.
**On the slide:** Firmest first. 1. High confidence, OULAD 2013–2014: 45.3% of the enrolments registered at day 14 did
not complete; runs varied from 24.9% to 58.3%; the year comparison depends on the add-drop rule; most non-completers
first missed a task after week 4 [M5 §14, §11.2]. 2. Moderate confidence: all five early signs go with later
non-completion in both years, a missed task by 40.8 and 39.3 points, in the same direction across modules;
associations [M5 §14, §11.3]. 3. Design only: a penalised logistic model judged once against the rule, and a
capacity-limited list audited for fairness; outputs expected, not measured [M5 §14, §11.4]. Not concluded: that the
signs cause non-completion, that a model ranks better than the rule, or that contact raises completion [M5 §14].
**Visual:** a descending stack of three tiers, firmest at the top (structure), each tier labelled with its confidence;
the "not concluded" line in grey below a rule; key on the slide: tier label = confidence level.
**Speaker notes:** [22:00 · budget 125] [checkpoint 3: the last two slides must start by 22:00]
Let's bring it together, firmest first. [pause] One, with high confidence for OULAD: forty-five point three
percent of students still registered at day fourteen did not complete, in both years. Runs varied from twenty-four
point nine to fifty-eight point three percent, the year comparison depends on the add-drop rule, and most
non-completers first missed a task after week four. Two, with moderate confidence: all five early signs, silence
included, go with later non-completion in both years, a missed task by forty point eight and thirty-nine point three
points. That's an association. Three, for AQ3 and AQ4 we have the right design, not a result. What we can't conclude:
that the signs cause non-completion, that a model beats the rule, or that a call helps. [click]
**Sources:** conclusions, confidence and limits of conclusion [M5 §14]; supporting numbers [M5 §11.2, §11.3, §11.4].

## Slide 29 – Limitations, Open Problems and Take-home   [Conclusions]   (~61 seconds)
**Lead:** We keep apart what showed no evidence, what has no data to test and what is not yet tested, and each open
problem has the step that answers it.
**On the slide:** Limitation kinds [M5 §12, Table 12.1]: No evidence found – the year difference over all enrolments
in shared modules; click signs in small modules → no claim. No data to test – contact and its outcome; delivery mode,
year of study, attendance; capacity → randomised pilot. Not yet tested – AQ3 and AQ4 results → the single AQ3 test,
design unchanged. Measurement – binary click signs; KPI proxy and denominator. Scope and causal – UK distance learning
of 2013–2014; observational design → re-check on the university's records; options as hypotheses. A flag must not
become a label [M5 §12]. Next steps [M5 §12.1]: 1. on OULAD, the single AQ3 test under the frozen protocol, then the
AQ4 list and its fairness audit; 2. at the university, recount the baseline under the add-drop rule, replace every
assumed value, and carry out the risk classification Vietnamese law requires for ranking learners; 3. a randomised
pilot among flagged students, contacts logged with their outcomes before any model is retrained. Take-home: a missed
task comes too late; count silence too, and test contact before trusting it.
**Visual:** left, the limitation log with its "kind" column colour-coded (structure; key on the slide: one colour per
kind); right, a three-step path, OULAD test → university recount → randomised pilot (sequence), the pilot step in the
accent colour; the take-home line in large type across the bottom.
**Speaker notes:** [23:00 · budget 125]
Three kinds of limits stay apart. "No evidence found": we compared and saw no clear
difference, like the year difference in shared modules. "No data to test": no screened dataset holds it, like any
record of contact. "Not yet tested": AQ3 and AQ4. And our results describe UK distance learning in 2013 and 2014.
Three next steps. First, the single AQ3 test, then the AQ4 list and its fairness audit. Second, a recount on
the university's own records, and the risk classification the law requires. Third, a randomised pilot, because only
random assignment separates the effect of a call from the reasons a student was flagged. [pause] If you remember one
thing: a missed task comes too late; count silence too, and test contact before you trust it. [click]
**Sources:** limitation kinds and log, scope, labelling caution [M5 §12, Table 12.1]; next steps, legal requirement,
randomisation, logging [M5 §12.1]; take-home [M5 §14, §11.2].

## Slide 30 – Thank You   [Conclusions]   (~31 seconds)
**Lead:** Thank you; we welcome your questions.
**On the slide:** Thank you. Questions? Early Identification of Disengaging Students in Online Courses – team N04.
Take-home: a missed task comes too late; count silence too, and test contact before trusting it. Data: Open University
Learning Analytics Dataset (Kuzilek, Hlosta and Zdrahal), CC BY 4.0 [M5 §4.1].
**Visual:** none (the title and the take-home line only); this slide stays up during questions.
**Speaker notes:** [24:00 · budget 62]
We began with students noticed too late, and staff who asked for a short list with a reason beside each name.
Records dated by week four can give those reasons now, as long as silence counts beside missed tasks. Whether a model
ranks better, and whether a call helps, are the next test and the pilot. Thank you. We're happy to take your
questions.
**Sources:** dataset and licence [M5 §4.1]; summary of findings [M5 §14].

---

# Q&A hand-off

- **On time:** "Thank you. We're happy to take your questions." [stay at the front; Slide 30 stays up with the
  take-home line]
- **Running long (chair signalling):** "We'll stop here. The short version of the last slides: a missed task comes too
  late, the early signs give staff a reason to check, and contact must be tested in a pilot. Questions?"
- **If no question comes:** a natural first question is why we did not train the AQ3 model; the answer is on Slide 18
  (the 2014 runs are the only independent test, kept for one complete run of the frozen protocol).

# Running-long protocol

```
RUNNING-LONG PROTOCOL (checkpoints: Slide 10 at 7:00, Slide 18 at 14:00, Slide 28 at 22:00)
- Checkpoint behind by < 30 s  -> tighten delivery, skip nothing.
- Behind by 30–90 s            -> take the next CUT block, silently:
                                  quality-detail (Slide 10), pipeline-checks (Slide 13),
                                  development-folds (Slide 16).
- 5 minutes left before Slide 24 -> go straight from Slide 23 to Slide 26 and say:
                                  "Let me jump to what this means for the decisions."
- 2 minutes left                -> jump to Slide 28; deliver points one to three.
- 1 minute left                 -> Slide 29 take-home sentence, then the thank-you.
NEVER: speak faster, skip the take-home, skip a limitation, or apologise for time.
```

# Rehearsal checklist

1. **Calibrate the pace.** Each presenter reads 200 words of their own slides aloud for 60 seconds, standing; subtract
   about 10 words a minute for the room. If the measured rate differs from 125 words a minute by more than 10, rerun the
   word budget and the timer with that rate.
2. **Desk pass.** Read the whole script aloud, seated; rewrite every sentence that causes a stumble, then rerun the
   timer on the notes-only copy.
3. **Standing pass.** Full delivery with the clicker and a timer; note the real time at the three checkpoints beside
   the budgeted marks (7:00, 14:00, 22:00) and at the speaker hand-overs between team members.
4. **Recorded pass.** Record on a phone and watch it: total time must land between 24:00 and 24:30; check filler
   words and any slide where the notes only re-read the slide text.
5. **Cut drill.** Read Slides 10, 13 and 16 once with their CUT blocks removed, to confirm each seam reads cleanly.
6. **Numbers drill.** Say every number on Slides 19–23 and 28 aloud once against the slide, so spoken and shown
   numbers match.
7. The timing holds only after at least one full out-loud rehearsal with a timer; if pass 4 runs more than 30 seconds
   over despite the word count, re-budget with the measured pace rather than trimming sentence by sentence.
