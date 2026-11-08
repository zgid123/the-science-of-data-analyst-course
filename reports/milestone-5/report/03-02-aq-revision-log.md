## 3.2. AQ Revision Log

The final questions of Table 3.1 differ from the questions proposed in Milestone 1, because the proposal was written
for the university's own records and the analysis runs on an open stand-in dataset. Every difference is traced to a
finding in the data and to an entry of the Controlled Change Log, the numbered list of every change to the proposal
with its reason (entries C01–C17, given in full in the appendices). The AQ Revision Log below records, for each
question, its Milestone 1 wording, the finding from Milestones 2 and 3 that forced a change, the final wording, the
action on the brief's scale (Keep, Modify, Defer or Drop), the reason and the effect on the method.

**The changes that touch every question.** Four entries of Milestone 2 (C01–C04) apply to all questions. Because no open dataset
of Vietnamese university courses exists, OULAD stands in for the university's courses, while the university's records
remain the target of the pilot (C01). A semester becomes a module run counted in days, with the cut-offs of the week-3 and week-5 lists on day 13 and day 27 (C02). The add-drop period maps onto the first 14 days of a run, when the Open University's registration window closes, so the KPI population counts the enrolments still registered on day 14 (C03). Comparisons by delivery mode and year of study, which OULAD does not
record, are replaced by comparisons by module and run, and the fairness limit of AQ4 moves to deprivation band and
disability (C04). Milestone 3 then fixed one population rule for every question: an enrolment counts on a given day
when the student registered by that day, or the registration day is unknown, and had not unregistered by it (C09); this refines C03 by also removing the 58 late registrants.

**The log.** Table 3.3 is the AQ Revision Log. The ratings named in the finding column are those of the AQ–Data Fit
of Milestone 3 (Section 5.1), where YELLOW means that the question must be narrowed or its claim changed and RED means
that a key concept, variable or intervention is missing.

**Table 3.3. AQ Revision Log**

| AQ | AQ at Milestone 1 | Finding from Milestones 2 and 3 | Final AQ | Action | Reason | Effect on method |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | In the program's online and blended courses over the four semesters of 2024–2025 and 2025–2026, what share of students enrolled after the add-drop period passed, failed or withdrew, by course, delivery mode and year of study, and how does the week of the first missed assessed task compare between students who passed and students who did not? | No open dataset of Vietnamese courses exists, so OULAD stands in (C01); a semester becomes a module run counted in days (C02); OULAD has a final result for all 32,593 enrolments and due days for 182 TMA and CMA tasks, but no delivery mode or year of study (C04), and exam results in only 2 of 7 modules (18 of the 24 exams have no result row); 58 enrolments registered after day 14 (C09). Rated YELLOW. | What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss an assessed task? | Modify (C01, C02, C03, C04, C09) + Defer (2014 detail, computed after the AQ3 test, C15) | Fields the question names do not exist in any open dataset, and the population must count only students enrolled at day 14; computing 2014 by outcome before the AQ3 test would open the test outcomes. | Rates by module, run, start month and year replace rates by course, delivery mode and year of study; the first missed task counts TMA and CMA only; the KPI population follows the day-14 rule (28,061 enrolments over 22 runs); the rates are computed on the 9 runs of 2013, and the year comparison uses the 2014 outcome counts published in Milestone 3. |
| AQ2 | Which signs observable in weeks 1–4 (missed or late quizzes and assignments, LMS activity compared with the course's own average, missed tasks in several courses at once, and, in blended courses only, attendance at in-class sessions) show the largest difference in later non-completion rates between students who have the sign and students who do not, and are these differences similar across courses, delivery modes and years of study? | OULAD has no in-class sessions, so attendance has no counterpart (C05); no delivery mode or year of study (C04); tasks fall due by day 27 in only 16 of 22 runs; only 12 of the 1,382 enrolments taken at the same time as another fall in 2013, so the several-modules sign exists in 2014 only (C12). Rated YELLOW; ready for association only. | Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module? | Modify (C01, C02, C04, C05, C12) + Defer (2014 replication and several-modules sign, C14) | Attendance, delivery mode and year of study are absent from OULAD; estimating AQ2 on 2014 before the AQ3 model is frozen would leak test information into AQ3 (C14). | Within-module association by logistic regression with run fixed effects on the 9 runs of 2013; task signs only in runs with a task due by day 27; comparison across modules replaces comparison across delivery modes and years of study; replication on the 13 runs of 2014 (with module CCC and the several-modules sign) after the AQ3 test; association, never cause. |
| AQ3 | For each student enrolled in a pilot course, how well can failing or withdrawing by the end of the semester be estimated from the data recorded by the end of week 2 and by the end of week 4, compared with a simple rule such as "two or more assessed tasks missed"? Accuracy is measured on a list as long as staff can follow up each week, as recall and precision, and is compared between first-year and later-year students and across courses. | A non-exam task falls due by day 13 in 1 of 22 runs and by day 27 in 16, so the week-3 list rests on activity (C06), and a task-only rule cannot fire in 6 runs at day 27 or 21 at day 13 (C10); each module has at most one earlier run of the same start month, and 9 module and start-month pairs ran in both years (C07); no year of study (C04). Rated YELLOW. | How well can non-completion be estimated from the data up to the end of week 2 and of week 4, compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs? | Modify (C01, C02, C04, C06, C07, C10, C13, C16) | Assessed tasks rarely fall due by the cut-offs, so the comparison rule needs an activity part to flag anyone; testing on a later year mirrors use on a later semester; year of study does not exist. | Train on the 9 runs of 2013 and test once on all 13 runs of 2014, with the 9 paired and 4 unpaired runs reported apart (C16); the comparison rule is the early-sign rule (C10); group checks by deprivation band and disability replace first-year against later-year students; recall and precision at capacity become normalised recall at capacity (C13). |
| AQ4 | At each review point (weeks 3 and 5), which students should be listed, in what order, and with which contact (a message from the lecturer or lecturer-advisor, a call from the support office, or a referral to the student affairs office, which handles financial and personal matters, separate from the support office), so that the list reaches as many as possible of the students most likely not to complete? The list must fit weekly capacity (three to five contacts per lecturer-advisor, about 30–40 for the support office), reach a precision of at least 50%, and keep first-year recall within ten points of later-year recall. | No candidate dataset records contacts, contact types, staff capacity or outcomes after a contact (C08), so AQ4 is rated RED; non-completion is 44–45% at the cut-offs, so a random list already reaches about 45% precision (C13); year of study is absent, so the fairness limit moves to deprivation band and disability (C04). | Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability? | Modify (ranking part; C04, C08, C11, C13) + Defer (contact choice and its effect, to the pilot; C11) | The contact part has no data in OULAD or in any screened dataset, and the 50% precision limit says nothing when the base rate is about 45%. | Top-k list per run from the AQ3 scores under an assumed capacity of 3 or 5 per 20 students, judged by lift and normalised recall against random and rule-ranked lists; the ten-point fairness gap returns as review rule FR1 on declared disability, deprivation band 0–10% and the missing band, where a flag leads to human review; no prescriptive or causal claim; the contact choice waits for a randomised pilot. |

**Reading the actions.** Each milestone rated the questions on the scale of its own brief, and Table 3.4 maps those
ratings onto the two scales of the final report: the revision action of Table 3.3 and the final status of Table 3.1.
Each mapping follows the definition of the scale it translates; for example, a YELLOW fit rating asks to narrow the
question, which is the action Modify.

**Table 3.4. Status scales of the milestones and the final scales**

| Milestone and scale | AQ1 | AQ2 | AQ3 | AQ4 | Maps to |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Milestone 2 – coverage (Full, Partial, None) | Partial | Partial | Partial | Partial (ranking) / None (action) | Full → Keep; Partial → Modify; None → Defer or Drop |
| Milestone 3 – AQ–Data Fit (GREEN, YELLOW, RED) | YELLOW | YELLOW | YELLOW | RED | GREEN → Keep; YELLOW → Modify; RED → Modify the supported part and Defer the rest, or Drop |
| Milestone 3 – model readiness (Ready, Revise) | Ready | Ready, for association only | Ready | Revise: ranking ready, contact deferred | Revise → Defer the missing part |
| Milestone 4 – entry status | Ready | Ready, for association only | Ready | Ready as a ranking; contact deferred | Same content as the Milestone 3 readiness |
| Final revision action (Keep, Modify, Defer, Drop) | Modify + Defer (2014 detail) | Modify + Defer (2014 replication) | Modify | Modify + Defer (contact choice) | – |
| Final status (Answered, Partial, Deferred, Dropped) | Partial | Partial | Deferred | Deferred | – |

The two kinds of scale answer different questions. The fit, readiness and entry ratings and the revision action describe a question and its data before analysis, while the final status describes the results available now. A question rated Ready can therefore be Deferred when its design is complete and its result waits for a named step, as AQ3 and AQ4 do.

**Three entries recorded in the final integration.** Integrating the four milestones brought three changes to the
Change Log, each with its reason. First, AQ1 is computed on the 9 runs of 2013 (13,529 enrolments, of which 12,076 were
registered at day 14), and its year comparison uses the 2014 outcome counts per run that Milestone 3 published (19,064
enrolments, all-enrolment denominator), because relating 2014 outcomes to task and activity measures before the AQ3
model is frozen would open the test outcomes, the same leak that C14 prevents for AQ2 (C15). Second, the AQ3 test set
moved in Milestones 3 and 4 from the 2014 runs of the 9 paired modules and start months to all 13 runs of 2014 (15,724
enrolments at day 27), so that the test also covers a module and start months the model has not seen; the 9 paired
runs (10,801 enrolments) and the 4 unpaired runs (4,923) are reported apart, and the entry records a change that had
been made without one (C16). Third, one early-sign rule serves the project on OULAD and in the pilot, so that secondary
KPI 1 counts the same students as the rule the AQ3 model must beat (C17).

**What did not change.** No question was dropped: every question keeps a core that the data answer, and only the
contact part of AQ4 is deferred, to a pilot in which contacts and their outcomes are logged. The fairness limit of
Milestone 1, first-year recall within ten points of later-year recall, was not lost when year of study proved absent:
Milestone 4 restored the ten-point gap as review rule FR1 on the groups OULAD records, added the condition that the
one-sided 95% interval of the gap, adjusted for several groups, lies below zero, and turned the limit from a
constraint on the list into a flag for human review. Section 4 turns to the data that these final questions require.
