## 4.1. AQ–Data Fit Ratings

Each question is rated against the claim it carries after the Milestone 2 changes C01–C08. Table 4.1, the AQ–Data
Fit Decision Log, gives for each question its rating, what the real data support, what is missing or weak, the step
of the decision procedure that settles the gap and the change it leads to.

**Table 4.1. AQ–Data Fit Decision Log**

| AQ | Rating | Supported by real data | Missing or weak | Action (step) | Change |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | YELLOW | Final result of all 32,593 enrolments in 22 runs; due days of 182 TMA and CMA tasks and their submissions | Year of study and delivery mode (all runs are distance learning); exam results in 5 of 7 modules | Derive the first missed task over TMA and CMA (2); keep the comparisons OULAD holds (4) | C09 |
| AQ2 | YELLOW | Daily click records; tasks due by day 27 in 16 of 22 runs; 1,382 enrolments in two runs at once, 1,370 of them in 2014 | Attendance; year of study and delivery mode | Derive each sign with a formula and a window (2); task signs in the 16 runs with a task due; the several-modules sign for 2014 only (4) | C12 |
| AQ3 | YELLOW | Target for every enrolment; 28,069 enrolled at day 13 and 27,535 at day 27; 9 module and start-month pairs in both years | The rule counting missed or late tasks fires in 1 run at day 13 and 16 at day 27; no day on which a TMA mark was released | No marking dates in any field (1); restate the rule (2); CMA marks known by the cut-off only (4) | C10 |
| AQ4 | RED | Ranking from AQ3; enrolment counts for capacity scenarios | Contacts, contact types, staff capacity and outcomes after contact | No compatible open dataset (3); rewrite to the ranking part (4); defer the contact choice (5) | C11, C13 |

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
