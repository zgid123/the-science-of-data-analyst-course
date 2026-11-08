## 2.1. AQ Modeling Briefs

A Modeling Brief records, for one question and before any algorithm is named, eight attributes: the question's
identifier and wording, its analytics level, the decision it supports, the unit of analysis, the outcome or target,
the information allowed as input with its time window, the expected output and the main constraint [1]. Naming the
expected output matters, because the same binary outcome can be reported as classes, as probabilities or as a
ranking, and each form needs its own measure of quality [3]. All four briefs use the prepared dataset
OULAD-N04-prepared-1.0, in which an enrolment is one student in one module run, the cut-offs are the ends of day 13
and day 27 of the run, and non-completion means a final result of Fail or Withdrawn.

**AQ1.** Table 2.1 gives the brief of the descriptive question, which needs counts and rates, not a model.

**Table 2.1. Modeling Brief of AQ1**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ1: What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss an assessed task? |
| Analytics level | Descriptive |
| Decision supported | D2 (where advisors' time goes) and D3 (whether to extend after the pilot): programme leaders see which modules and runs lose most students and how early the first missed task appears |
| Unit of analysis | Enrolment, restricted to enrolments still registered at day 14 (the KPI population); assessment task for the first missed task |
| Outcome / target | N/A (no supervised task); measures: completion and non-completion rates, outcome shares, week of the first task due and not submitted |
| Input information | Enrolment view (outcome, module, run, start month, year); assessment-due view (task, due day, submission); whole run, because the question describes completed runs |
| Expected output | Rate tables with 95% confidence intervals by module, run, start month and year; distribution of the week of the first missed task by outcome |
| Main constraint | Correct denominator (enrolled at day 14) and per-run task schedules, which differ by module; exam results missing in five modules, so the first missed task counts tutor-marked and computer-marked assessments only |

**AQ2.** Table 2.2 gives the brief of the diagnostic question, which measures how strongly each sign goes with
non-completion and does not claim that a sign causes it.

**Table 2.2. Modeling Brief of AQ2**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ2: Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module? |
| Analytics level | Diagnostic (association; no causal claim) |
| Decision supported | D2 and the reasons attached to each name on the D1 list: which signs tutors should look at |
| Unit of analysis | Enrolment registered at day 27 |
| Outcome / target | non_completion at the end of the run, used as the outcome of an association model, not as a prediction target |
| Input information | Signs up to day 27: a task missed, a TMA submitted late, no platform activity in the last seven days, activity relative to the run median, activity before the start; adjustment for module run, previous attempts and credits studied |
| Expected output | Risk differences in percentage points with 95% intervals, unadjusted and within module run, odds ratios beside them; direction of each association per module |
| Main constraint | Association only; tasks due by day 27 exist in 16 of 22 runs; correlated signs; estimation on the 9 training runs of 2013 (6 modules) so that the 2014 test outcomes stay unseen |

**AQ3.** Table 2.3 gives the brief of the predictive question, whose output is a risk score per enrolment at each
cut-off.

**Table 2.3. Modeling Brief of AQ3**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ3: How well can non-completion be estimated from the data up to the end of week 2 (day 13) and of week 4 (day 27), compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs? |
| Analytics level | Predictive |
| Decision supported | D1 (who is listed for contact) |
| Unit of analysis | Enrolment registered at the cut-off |
| Outcome / target | non_completion (Fail or Withdrawn) at the end of the run, known only after the run |
| Input information | The 19 usable primary predictors of the prepared views (the mean computer-marked assessment (CMA) score is left out because fewer than 10% of training rows carry it) all dated on or before the cut-off; an extended set of 10 further predictors plus the weekly click counts (2 at day 13, 4 at day 27) as an alternative |
| Expected output | A risk score per enrolment at each cut-off, used as a rank within the run; shown as a probability only if calibration holds |
| Main constraint | Leakage and transfer to a later run; interpretability for tutors; calibration; train on 2013 runs, test once on 2014 runs |

**AQ4.** Table 2.4 gives the brief of the ranking question, which turns the AQ3 scores into a list of the length that
staff can follow up.

**Table 2.4. Modeling Brief of AQ4**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ4: Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability? |
| Analytics level | Prescriptive (ranking), as decision support; the choice of contact is deferred |
| Decision supported | D1: tutors receive a ranked list and decide whom to contact |
| Unit of analysis | Enrolment within a module run |
| Outcome / target | Uses the AQ3 target to judge the list; no outcome of contact exists in the data |
| Input information | AQ3 scores and the reasons behind them; list size per run for 3 or 5 contacts per assumed tutor group of 20 students |
| Expected output | A ranked list per run of the size the capacity allows, with the signs behind each name |
| Main constraint | Fixed capacity; risk is not benefit; human decision; fairness across deprivation band and disability; no claim that contact works |

Read together, the briefs show how the questions depend on each other. AQ3 and AQ4 share one target and one
population, so AQ4 reuses the AQ3 scores and adds only the rule that cuts the ranking at the length capacity allows,
whereas AQ1 and AQ2 describe runs that have ended and need no prediction. The design resembles the OU's own
early-warning system, which also gives tutors a weekly list of students at risk, although that system predicts
whether a student will submit the next assignment rather than whether the student will complete the run [4].
