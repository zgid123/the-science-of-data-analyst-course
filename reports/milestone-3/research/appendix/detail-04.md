**Reasoning behind each fit rating.** The paragraphs below explain, question by question, the ratings of the AQ–Data
Fit Decision Log (Table 4.1) and the changes C09 to C13 that follow from them.

**AQ1, descriptive.** OULAD records the final result of every enrolment and the due day of every task, so completion
rates by module, run, start month and year can be computed, and the week of the first missed task can be derived
from due days and submissions. The question is YELLOW rather than GREEN because two of its comparisons, by year of
study and by delivery mode, have no field in OULAD, and because exam results are missing in five modules, so the
first missed task is taken over TMA and CMA only. In addition, the population of the rates is restated: an enrolment
counts as enrolled on a given day when the student registered by that day, or the registration day is unknown, and
did not unregister by it. This rule (C09) adds the registration condition to the Milestone 2 definition, which counted
every enrolment still registered on day 14 (28,119); it removes the 58 students who registered after day 14 and leaves
28,061 enrolments in the KPI population, and the same rule gives the populations at both cut-offs.

**AQ2, diagnostic.** Each sign of AQ2 can be derived from the click and submission records with a stated formula and
window. Two parts of the question narrow. Task signs exist only in the 16 runs where a task falls due by day 27.
The sign "tasks missed in several modules at once" needs students enrolled in two runs at the same time, and of the
1,382 such enrolments at day 14, only 12 fall in the 2013 runs; the sign is therefore described for the 2014 runs
only and does not enter the predictive features, which are learned on 2013 (C12). AQ2 measures association, not
cause, and the attendance sign of Milestone 1 has no counterpart in distance learning.

**AQ3, predictive.** The target exists for every enrolment, the populations at both cut-offs are large, and nine
module and start-month pairs ran in both years, so a model built on 2013 can be tested on 2014. The comparison rule is
the weak part. In Milestone 1, the early-sign rule reads "two or more assessed tasks missed or late by the end of week
4"; two tasks fall due by day 27 in only one run, so Milestone 2 counted one missed or late task (C06), but even that
form cannot fire in the 6 runs without a task due by day 27 or in 21 runs at day 13. The meaning of a late CMA in
2013–2014 is also undocumented (DQ10). The rule is therefore restated (C10): a student shows early signs when a task
due by the cut-off has not been submitted, or a TMA has been submitted late, or the student has had no platform
activity in the seven days before the cut-off. The rule can now fire in every run, and the CMA-lateness version is kept
only as a sensitivity variant. Scores, in turn, enter only where the mark is known by the cut-off, which holds for CMA
marks submitted at least seven days earlier and never for TMA marks.

**AQ4, prescriptive.** AQ4 asks whom to list, in what order and with which contact, within capacity. OULAD records no
contact, no type of contact, no staff capacity and no outcome after a contact, and none of the seven candidate datasets
of Milestone 2 records them either, so the question is RED. Following the brief's order, it is rewritten to the part
the data support: under an assumed weekly capacity, which enrolments rank first at each cut-off, and what recall, the
share of later non-completers who appear on the list, and what precision, the share of listed students who later fail
or withdraw, the list reaches overall and by deprivation band and disability (C11). The choice of contact and its effect
are deferred to the pilot, where the contact record will exist. In addition, the Milestone 1 limit of at least 50%
precision says little when 44–45% of students do not
complete, since a random list already reaches about 45%. List quality is therefore measured as lift, the precision of
the list divided by the run's rate of non-completion, and as recall against the most that a list of the same length
can reach, with a random list and the early-sign rule as baselines (C13).

**Changes C09 to C13 in full.** Five changes follow from these ratings, and each narrows how a question is measured without changing what it asks.
The population rule (C09) counts an enrolment as enrolled on a given day when the student registered by that day, or
the registration day is unknown, and did not unregister by it; it removes the 58 late registrants from the Milestone 2
count of 28,119, which took every enrolment still registered on day 14, and leaves 28,061 enrolments in the KPI population.

The sign "tasks missed in several modules at once" is described for the 2014 runs only, because only 12 of the 1,382 concurrent enrolments fall in the 2013 training
runs (C12).

The early-sign rule counts one missed or late task on OULAD (C06), but no task falls due by day 27 in 6 runs or
by day 13 in 21, so in those runs it can flag no one; it therefore becomes "a task due by the cut-off not submitted, or a TMA submitted late, or no platform
activity in the seven days before the cut-off" (C10), whose inactivity part can flag students in every run.

AQ4 is rated RED because its contact part has no data
at all; it is rewritten to its ranking part, which rests on AQ3, and the choice of contact
is deferred to the pilot, because no dataset records contacts (C11).

Finally, the Milestone 1 limit of 50% precision,
the share of listed students who later fail or withdraw, says little when 44–45% of students do not complete, since a random list already reaches about 45%, so a
list is judged by its lift, its precision divided by the run's rate of non-completion, and by its recall, the share of
later non-completers it reaches, against the most a list of its length can reach (C13).

**Baseline in full.** The paragraphs below give the goal, the measures and the decisions of the baseline that
Section 1.1 summarises.

**Goal and measures.** The Business Goal is to improve successful course completion in a university program's online
and blended courses by identifying students who stop taking part early enough to support them within the semester.
The SMART Goal turns this into a target: the completion
rate of students enrolled after the add-drop period, the first weeks in which students may still register for or
drop a course, rises in the pilot courses from a baseline that the pilot will recount from the university's records,
assumed for now to be 70%, by five percentage points to 75% by the end of the 2027–2028 academic year. Completion means passing the course; a fail or a withdrawal counts as
non-completion.

Three KPIs track the goal. The primary KPI is the course completion rate itself. The
first secondary KPI, the early-sign contact rate, is the share of students showing early signs of disengagement who
are contacted by the end of week 5; the early signs are defined by the early-sign rule, which in Milestone 1 reads
"two or more assessed tasks missed or submitted late by the end of week 4". The second secondary KPI, the follow-up
rate, is the share of students on a contact list who are contacted within seven days of the list reaching staff.
Both secondary KPIs rely on a contact record, a shared log of who contacted which student, when and with what result,
which the university does not keep yet.

**Decisions.** The proposal supports three decisions. D1 is whom the lecturer-advisors and the support office contact
at each review point, a moment in weeks 3 and 5 of the semester when a contact list reaches staff; each list uses the
data up to its data cut-off, the end of week 2 for the week-3 list and the end of week 4 for the week-5 list,
because data exports take about a week. D2 is where the program manager places the time of the support office and
the lecturer-advisors each semester, and D3 is whether to extend the approach to all courses after the pilot.

**Changes from Milestone 2 in full.** Milestone 2 selected OULAD as an open
stand-in for the university's own records, which cannot be used yet, and recorded eight changes, C01 to C08, in the
Controlled Change Log, the list of every change to the baseline with its reason in the data. The population became
the OULAD module runs of 2013–2014, the courses of a distance-learning university in the UK, in place of
the program's courses (C01). Time became a count of days from the start of each run, which places the two data
cut-offs at day 13 and day 27 (C02). The KPI denominator became the enrolments still registered on day 14 (C03).
Comparisons by delivery mode and year of study became comparisons by module and run, since OULAD records neither
(C04), and the attendance sign was dropped because distance learning has no classes to attend (C05). The week-3 list
rests on activity alone, because a task falls due by day 13 in only one run, and on OULAD the early-sign rule counts
one missed or late task rather than two (C06). The predictive question is trained on the 2013 runs and tested on the
2014 runs (C07), and the choice of contact and its outcome remain a requirement for the pilot, because OULAD records
no contact (C08).

**Synthetic-data policy in full.**

The brief allows synthetic data at five levels with different conditions: small test data for
code (level A) and simulation to illustrate a method (level B) are allowed; augmentation of training data (level C)
needs the lecturer's approval; and synthetic data that fill a missing concept, label or intervention (level D) or that
enter descriptive or diagnostic evidence (level E) are not allowed [1]. This project uses level A only: a few
hand-made test enrolments, labelled as synthetic in the `tests/` folder of the Prepared Data Package, check that each
feature formula gives the expected value. They never enter a prepared view, a statistic or a finding, and no
augmentation is planned.
