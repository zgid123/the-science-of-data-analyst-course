---
id: S104
url: reports/milestone-4/report/00-1-abbreviations.md
requested: reports/milestone-4/report/00-1-abbreviations.md reports/milestone-4/report/00-2-glossary.md reports/milestone-4/report/01-00-context-continuity.md reports/milestone-4/report/01-01-goal-decisions-aqs.md reports/milestone-4/report/01-02-prepared-data-entry-gate.md reports/milestone-4/report/02-00-aq-task-mapping.md reports/milestone-4/report/02-01-modeling-briefs.md reports/milestone-4/report/02-02-technical-tasks.md reports/milestone-4/report/03-00-candidate-approaches.md reports/milestone-4/report/03-01-criteria-matrix.md reports/milestone-4/report/03-02-descriptive-diagnostic.md reports/milestone-4/report/03-03-predictive.md reports/milestone-4/report/03-04-ranking-capacity.md reports/milestone-4/report/04-00-evaluation-design.md reports/milestone-4/report/04-01-evaluation-cards.md reports/milestone-4/report/04-02-validation-strategy.md reports/milestone-4/report/04-03-metrics-success.md reports/milestone-4/report/04-04-error-fairness.md reports/milestone-4/report/05-00-risk-ethics.md reports/milestone-4/report/05-01-leakage-interpretability.md reports/milestone-4/report/05-02-causal-fairness-use.md reports/milestone-4/report/06-00-genai-usage.md reports/milestone-4/report/07-00-prototype-protocol.md reports/milestone-4/report/08-00-traceability.md reports/milestone-4/report/09-references.md reports/milestone-4/report/10-00-appendices.md reports/milestone-4/report/10-01-candidate-comparison.md reports/milestone-4/report/10-02-metric-definitions.md reports/milestone-4/report/10-03-validation-protocol.md reports/milestone-4/report/10-04-fairness-spec.md reports/milestone-4/report/10-05-risk-register.md reports/milestone-4/report/10-06-ai-critiques.md reports/milestone-4/report/10-07-traceability-full.md
fetched: 2026-11-08T23:22+07:00
tool: fetch.py local (git show 19d35a4; verbatim, 33 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T05
part: 1
raw: raw.txt (132 KB)
conversion: verbatim copy of 33 file(s) from milestone-da at 19d35a4
---
===== reports/milestone-4/report/00-1-abbreviations.md @ 19d35a4 =====
# List of Abbreviations

The abbreviations below are listed in alphabetical order, each with its full form and its role in this report.

| Abbreviation | Full form | Role in this report |
| :---- | :---- | :---- |
| ABROCA | Absolute between-ROC area | Threshold-free measure of differential discrimination between a group and the rest (Section 4.4) |
| AI | Artificial intelligence | Modeling partner under the brief's rules (Part 6); subject of the regulation in Part 5 |
| AQ | Analytical question | AQ1–AQ4, the four questions of the project (Table 1.1) |
| CMA | Computer-marked assessment | Assessment type whose mean score is left out of the predictors (Section 2.1) |
| EU | European Union | Origin of the AI Act used as a reference standard (Section 5.2) |
| KPI | Key performance indicator | Completion rate and the two contact rates (Section 1.1) |
| NIST | National Institute of Standards and Technology | Author of the AI Risk Management Framework (Part 5) |
| OU | Open University | UK distance-learning university whose data form OULAD |
| OULAD | Open University Learning Analytics Dataset | The project's dataset, prepared as OULAD-N04-prepared-1.0 |
| PR-AUC | Area under the precision–recall curve | Secondary metric read against the base rate (Sections 4 and 4.3) |
| PROBAST+AI | Prediction model Risk Of Bias ASsessment Tool for AI | Appraisal tool for leakage and predictor availability (Section 6) |
| ROC | Receiver operating characteristic | Curve of true against false positive rates (Sections 4 and 4.3) |
| ROC-AUC | Area under the ROC curve | Secondary, within-run discrimination metric (Sections 4 and 4.3) |
| SMART | Specific, measurable, achievable, relevant and time-bound | Form of the project goal (Section 1.1) |
| TMA | Tutor-marked assignment | Assessment type whose late submission is an early sign (Section 1.1) |
| TRIPOD+AI | Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis statement updated for AI | Reporting standard that frames the evaluation (Part 4) |
| UK | United Kingdom | Country of the OULAD modules (Section 5.1) |

===== reports/milestone-4/report/00-2-glossary.md @ 19d35a4 =====
# List of Terms

The terms below are listed in alphabetical order with their meaning in this report and the section that defines them.

| Term | Meaning in this report |
| :---- | :---- |
| Add-drop period | The first weeks of a course in which students may still register for or drop it (Section 1.1) |
| Attainable recall | The largest share of a run's non-completers that a list of length k can hold, min(k, non-completers) divided by non-completers (Section 4.3) |
| Background-only model | A logistic model using module, start month, previous attempts, credits, education and registration lead, without any activity (Section 3.3) |
| Base rate | The share of a run's enrolments who do not complete; the precision of a random list (Section 1.1) |
| Baseline | The simple method that a candidate must beat to be worth its complexity (Section 3.1) |
| Calibration slope | The coefficient of the score's log-odds in a logistic recalibration, a logistic regression of the outcome on that log-odds; 1 when risks are neither too extreme nor too flat (Section 4.3) |
| Calibration | Agreement between predicted risks and observed rates (Section 4) |
| Calibration-in-the-large | The intercept of a logistic model of the outcome with the score's log-odds as offset (a term whose coefficient is fixed at 1); 0 when the average predicted risk is right (Section 4.3) |
| Capacity | The number of students tutors can contact: 3 or 5 per tutor group, a group assumed to hold 20 students, that is 15% or 25% of a run's enrolments (Section 3.4) |
| Cut-off | The day up to which a predictor may use data: day 13 (end of week 2) or day 27 (end of week 4) (Section 1.1) |
| Discrimination | How well a model separates students who will not complete from those who will (Section 4) |
| Early-sign rule | A task due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off (Section 1.1) |
| Enrolment | One student in one module run, the unit of analysis (Section 1.1) |
| Fixed effects | Terms for each module run, so that students are compared only within the same run (Section 3.2) |
| Freeze | A recorded point after which a choice cannot change: the first before training, the second before testing (Section 4.2) |
| Gradient-boosted trees | An ensemble of small decision trees, each fitted to the errors of the previous ones; the AQ3 challenger (Section 3.3) |
| Labels-available variant | A sensitivity analysis that scores the 2014 February runs with a model trained only on the 2013 February runs, the runs whose outcomes are known at that time (Section 4.2) |
| Leave-one-run-out folds | Development folds in which each 2013 run is held out once (Section 4.2) |
| Lift | Precision at capacity divided by the run's base rate; 1 means chance (Section 4.3) |
| Module run | One offering of an OU module, named by its year and start month, B for February and J for October (Section 1.1) |
| Non-completion | A final result of Fail or Withdrawn, the target of AQ3 (Section 1.2) |
| Normalised recall | Recall at capacity divided by attainable recall, pooled over runs; the primary metric (Section 4.3) |
| Overfitting | A model learning the noise of its training data, so that it performs worse on new cases (Section 3.3) |
| Paired run | A 2014 test run whose module and start month also ran in 2013 (Section 4.2) |
| Penalised logistic regression | A logistic regression whose coefficients are shrunk towards zero to limit overfitting; the AQ3 primary approach (Section 3.3) |
| Primary approach | The candidate chosen for a question, with its reasons (Section 3.1) |
| Precision at capacity | The share of a run's list of length k who do not complete (Section 4.1) |
| Recall at capacity | The share of a run's non-completers who are on its list of length k (Section 4.3) |
| Risk difference | The difference in non-completion rate, in percentage points, between students with and without a sign (Section 3.2) |
| Separation | The fairness criterion of equal recall at capacity across groups (Section 4.4) |
| Sign-flip permutation test | A test of how often per-run differences as favourable would appear if the sign of each run's difference were random (Section 4.2) |
| Slicing analysis | Evaluation of the frozen model separately for each audit group (Section 4.4) |
| Technical task | The kind of analysis a question needs: aggregation, association, classification or ranking (Section 2.2) |
| Two-level bootstrap | Resampling of runs and then of enrolments within each run, to estimate uncertainty that respects the run structure (Section 4.2) |

===== reports/milestone-4/report/01-00-context-continuity.md @ 19d35a4 =====
# 1. Project Context and Continuity

Milestone 4 is the step from modeling to evaluation. Its central question, in the words of the brief, is which family
of solutions or models suits each analytical question and how it will be evaluated [1]. The brief sets two levels of
work. Level 1, the Modeling and Evaluation Proposal, is required: for each question it fixes the technical task, a
baseline and candidate families of methods, the primary approach with its reasons, the evaluation plan and the risks.
Level 2, a prototype experiment, is optional, and a team that completes Level 1 well completes the milestone; a
prototype can show that a choice is feasible but cannot make up for a weak strategy [1].

This report covers Level 1 in full. Part 7 specifies how the optional prototype will run, as a protocol, and no model
performance is stated anywhere in the report, because no model has been trained: every number in it is a count from
the prepared data or a value we fixed in advance with its reason. Section 1.1 restates the goal, the decisions
and the questions as they stand after Milestone 3, and Section 1.2 the prepared data and the entry gate that admits
them to modeling.

===== reports/milestone-4/report/01-01-goal-decisions-aqs.md @ 19d35a4 =====
## 1.1. Goal, Decisions and Analytical Questions

**Goal and measures.** The Business Goal is to improve successful course completion in a university program's
online and blended courses by identifying students who stop taking part early enough to support them within the
semester. The specific, measurable, achievable, relevant and time-bound (SMART) Goal turns this into a target: the
completion rate of students enrolled after the add-drop period, the first weeks in which students may still register
for or drop a course, rises in the pilot courses from a baseline that the pilot will recount from the university's
records, assumed for now to be 70%, by five percentage points to 75% by the end of the 2027–2028 academic year.
That completion rate is the primary key performance indicator (KPI). Two secondary KPIs follow the contacts: the share
of students with early signs of disengagement who are contacted by the end of week 5, and the share of students on a
contact list who are contacted within seven days.

**Decisions.** The proposal supports three decisions. D1 is whom the lecturer-advisors and the support office contact
at each review point, a moment in weeks 3 and 5 when a contact list reaches staff; each list uses the data up to its
data cut-off, the end of week 2 for the week-3 list and the end of week 4 for the week-5 list. D2 is where the
program manager places the time of the support office and the lecturer-advisors each semester, and D3 is whether to
extend the approach to all courses after the pilot.

**Data and changes.** The data are the Open University Learning Analytics Dataset (OULAD), an open stand-in for the
university's own records: 22 runs of seven Open University (OU) modules from 2013 and 2014 [2]. A module is an OU course; its modules carry
anonymised codes, AAA to GGG, and each offering of a module, a module run, is named by its year and its start month, B
for February and J for October [2]. Milestone 3 prepared the data as enrolments, each one student in one module run. Milestones 2 and 3 recorded thirteen changes, C01 to C13, in the
Controlled Change Log, the list of every change to the proposal with its reason in the data. They set the population
to the OULAD module runs and time to days from the start of each run, with the two cut-offs at day 13 and day 27; they
replace comparisons by delivery mode, which OULAD does not vary because every run is distance learning, and year of study
with comparisons by module and run; and they restate how two
questions are measured, AQ3 (C10) and AQ4 (C13), as described below. The Business Goal, the SMART Goal and the three decisions are unchanged.

**The questions as they stand.** The brief allows only the analytical questions (AQ) that remain valid after the AQ–Data Fit of Milestone 3, the step
that rated each question against the real data, to be modelled, and a part that was deferred may not return without a recorded change [1].
Table 1.1 gives the four questions as they stand, with their readiness after Milestone 3 and the decision each
supports.

**Table 1.1. AQs entering Milestone 4**

| AQ | Analytics level | Question | Readiness after Milestone 3 | Decision |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | What share of enrolments end in pass, fail or withdrawal, by module, run, start month and year, and in which week non-completers first miss an assessed task? | Ready | D2, D3 |
| AQ2 | Diagnostic | Which signs recorded by the end of week 4 (missed and late tasks, inactivity, activity against the run's median) go with later non-completion, compared within each module? | Ready, for association only | D2, and the reasons shown with each name in D1 |
| AQ3 | Predictive | How well can non-completion be estimated from the data up to the end of week 2 and of week 4, compared with the early-sign rule, when a model built on the 2013 runs is applied to the 2014 runs? | Ready | D1 |
| AQ4 | Prescriptive (ranking) | Which enrolments should rank first on a list of an assumed capacity, with what gain over a random list and what recall, overall and by deprivation band and disability? | Ready as a ranking; the choice of contact deferred to the pilot (C11) | D1 |

Two definitions from the Change Log carry through the whole report. The early-sign rule flags a student who, by the cut-off, has not submitted a task (a tutor-marked or computer-marked assessment) that was due, has submitted a tutor-marked assignment (TMA) late, or has had no
activity on the learning platform in the previous seven days (C10). And a list is judged by its recall, the share of
later non-completers it reaches, against the most a list of its length can reach, and by its gain over the run's
base rate (lift), the share of non-completers on the list against the share of students in the whole run who do not
complete, because a random list already reaches that base rate (C13).

===== reports/milestone-4/report/01-02-prepared-data-entry-gate.md @ 19d35a4 =====
## 1.2. Prepared Data and Entry Gate

**Prepared data.** The prepared dataset OULAD-N04-prepared-1.0 of Milestone 3 holds one row per enrolment and two
feature views, the tables of predictors a model reads, one for each cut-off: the end of day 13 (week 2) and the end of day 27 (week 4). A feature view keeps
only the enrolments still registered at its cut-off, that is, not withdrawn by that day, and only information dated on or before that day, so nothing a
model reads could not have been known when the list was drawn. The target, called non_completion in the data, is a final result of Fail or Withdrawn, recorded when the run ends.
The KPI counts the enrolments still registered on day 14, when the two-week window for registering closes. The data are split by year: the 9 runs of 2013 are for development and the
13 runs of 2014 for the final test. At day 27 the development runs hold 11,811 enrolments, of whom 5,245 (44.4%) did
not complete, and the test runs hold 15,724 enrolments; at day 13 the figures are 12,080 enrolments with 5,519
non-completers, and 15,989 test enrolments. The outcomes of the test runs stay unopened until a single final test
(Section 4.2), so that no choice in this proposal can be shaped by them.

**Entry gate.** The brief admits a team to modeling only when five conditions hold: the questions are approved after
the AQ–Data Fit, the prepared dataset has a version, a dictionary, a unit of analysis, keys, a target and feature
windows, leakage controls are set for prediction, the known limitations are recorded, and the chain from question to
prepared data is traced [1]. Table 1.2 gives the evidence for each condition.

**Table 1.2. Entry gate**

| Condition | Evidence from Milestone 3 | Status |
| :---- | :---- | :---- |
| Approved AQs | AQ1–AQ3 ready; AQ4 as a ranking (C11, which defers the choice of contact) judged by its gain over chance (C13) | Met |
| Prepared dataset | OULAD-N04-prepared-1.0 with data dictionary, unit (the enrolment), keys, target and feature windows | Met |
| Leakage controls | Cut-offs at day 13 and day 27; split by year; transforms fitted on the 2013 runs only; 22 of 22 validation checks passed | Met |
| Known limitations | The 19 data-quality issues of Milestone 3 (DQ01–DQ19) each with a decision; audit attributes kept; representativeness and data protection stated | Met |
| Traceability | Question → data requirement → raw variables → prepared variables and views | Met |

All five conditions hold, so the questions can be modelled as they stand, with the contact part of AQ4 left deferred.
One further change to how a question is measured follows from the evaluation design of this milestone: AQ2 is
estimated on the 2013 runs and replicated on the 2014 runs only after the AQ3 test, so that no test outcome is seen
while the predictive model is chosen. It is recorded as Change Log entry C14 (Section 4.2).

===== reports/milestone-4/report/02-00-aq-task-mapping.md @ 19d35a4 =====
# 2. AQ-to-Technical-Task Mapping

With the entry gate met (Section 1.2), each question is first described by what it needs, and only then translated
into a technical task. The order matters: the brief asks for a Modeling Brief before any algorithm is named, so that
the method follows from the question, from the output the decision needs and from the data, rather than from habit
or from a suggestion of artificial intelligence (AI) [1]. Section 2.1 gives the four AQ Modeling Briefs, and Section
2.2 the technical task that each brief implies.

===== reports/milestone-4/report/02-01-modeling-briefs.md @ 19d35a4 =====
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

===== reports/milestone-4/report/02-02-technical-tasks.md @ 19d35a4 =====
## 2.2. Technical Task Definitions

**Purpose first.** Building on the briefs of Section 2.1, the first test of each question is its purpose, because the
same regression can serve three different purposes. Explanatory modeling tests causal hypotheses; predictive modeling
forecasts new or future cases; and a regression used only to measure association, with neither a causal nor a
predictive aim, is descriptive in Shmueli's sense [3]. The brief places association analysis under diagnostic
questions and forbids reading it as cause [1], so AQ2 keeps the diagnostic level and its technical task is named
association. Prediction, unlike explanation, is judged on data the model has not seen [3], [5], which is why AQ3 and
AQ4 are evaluated on later runs (Section 4.2). Appendix I (Figure A.1) maps each question to its technical task, its
output and the decision it serves.


**AQ1 and AQ2.** AQ1 is aggregation: rates and shares grouped by module, run, start month and year, each with its
denominator and an interval. AQ2 is association within module run: how much more often students with a sign by day 27
fail to complete than comparable students of the same run without it.

**AQ3.** AQ3 is binary classification at two prediction points, the ends of day 13 and day 27. The target is known
only after the run ends, the model is trained on earlier runs and tested on a later one, and this arrangement mirrors
how the model would be used, on a run that is still in progress [6].

**AQ4.** AQ4 is ranking under a fixed capacity. When predictions are used to rank cases, the quality of the final
ranking matters more than the predicted values themselves [6], and studies that prioritise students for scarce
support evaluate the top of the list, where the decision falls [7]. Two other framings were considered. A discrete-time survival model, a form of survival analysis, would add when a student leaves [8], but the listing decision (D1) acts at two fixed
cut-offs and needs no timing, and the target joins Fail, decided only at the end of the run, with Withdrawn, so
survival stays an extension. Ranking students by the expected benefit of contacting
them would need data on contacts and their outcomes, which OULAD does not hold [9], so AQ4 remains decision support,
and the choice of contact stays deferred to a pilot (Section 5.2).

===== reports/milestone-4/report/03-00-candidate-approaches.md @ 19d35a4 =====
# 3. Candidate Modeling Approaches

With the technical task of each question fixed in Part 2, each question now receives its methods. The brief asks for
at least one reasonable baseline per question, a simple approach against which any other is compared, and, where
modeling is needed, two or three candidate families before a primary approach is chosen; it rejects the name or the
popularity of an algorithm as a reason ("Random Forest is strong", "XGBoost is popular") [1]. Section 3.1 sets out the
selection criteria and the Candidate Solution Matrix, Section 3.2 treats the descriptive and diagnostic questions,
Section 3.3 the predictive question and Section 3.4 the ranking under capacity.

===== reports/milestone-4/report/03-01-criteria-matrix.md @ 19d35a4 =====
## 3.1. Selection Criteria and Candidate Solution Matrix

**Criteria.** Each candidate is judged on the eight criteria that the brief makes compulsory [1]: fit to the
question, whether the method directly produces the output the question needs; fit to the data, whether sample size,
feature types, sparsity, imbalance, time structure and granularity suit it; assumptions, what the method requires of
the data and whether the data roughly meet it; interpretability, how much of the logic the users need to understand;
complexity against the baseline, what a more complex method is expected to add; robustness and reproducibility,
whether the method can be evaluated stably, rerun and kept free of leakage; ethics and fairness, whether its errors
could harm a group of students and whether it uses a sensitive attribute; and actionability, whether its output
supports the decision named in Milestone 1.

**Findings that settle ties.** Four findings on prediction systems settle most ties between candidates. A simple
heuristic often delivers much of the gain, so predictive work should start from a rule baseline and a simple first
model [6]. When many models reach about the same error, the simpler one can be chosen without loss [5]. Complexity is
costly to maintain over time [10]. And for high-stakes decisions about people, an inherently interpretable model is
preferable to a black box explained afterwards [11].

**The matrix.** Table 3.1 is the Candidate Solution Matrix of the brief: for each question, its technical task, its
baseline, its candidate families, the primary approach chosen and a short rationale. Sections 3.2 to 3.4 give the
reasoning behind each row.

**Table 3.1. Candidate Solution Matrix**

| AQ | Technical task | Baseline | Candidate 1 | Candidate 2 | Primary approach | Short rationale |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Aggregation | Pooled rate; rate over all enrolments, not only those registered at day 14 (second denominator) | Grouped rates with 95% intervals | – | Grouped rates with intervals | Descriptive question; no model needed |
| AQ2 | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Mixed-effects logistic regression (shallow tree as supplement) | Candidate 1 | All runs of the modules observed, not sampled, so fixed effects suit; effect sizes within module; no causal claim |
| AQ3 | Binary classification at day 13 and day 27 | Early-sign rule ranked by signs; background-only logistic model; random list | Penalised logistic regression | Gradient-boosted trees (discrete-time survival as extension) | Candidate 1 on the primary predictors, unless Candidate 2 or the extended predictor set wins by a margin fixed in advance | Interpretable reasons for tutors; ample events per parameter, each parameter backed by many non-completers; transfer to a later run |
| AQ4 | Ranking under capacity | Random list; rule-ranked list | Top-k per run from AQ3 scores | Risk tiers from capacity | Candidate 1 with reasons | Fixed capacity; no contact data, so no benefit ranking |

===== reports/milestone-4/report/03-02-descriptive-diagnostic.md @ 19d35a4 =====
## 3.2. Descriptive and Diagnostic Questions

**No machine learning.** Following the matrix of Section 3.1, AQ1 and AQ2 describe runs that have ended and make no
forecast, so they are answered with descriptive statistics and an association model rather than machine learning,
as the brief advises when simple statistics answer the question [1], [3].

**AQ1.** AQ1 is answered by completion and non-completion rates and outcome shares per module, run, start month and
year, each with its denominator and a 95% confidence interval, and by the week in which each enrolment first misses an
assessed task, compared by outcome. Its baseline is the pooled rate over all runs, together with a second denominator:
all 32,593 enrolments instead of the 28,061 still registered at day 14. Comparing the two denominators shows which
rates depend on how the population is defined, which is the main way a descriptive rate can mislead.

**AQ2: the question.** AQ2 asks how much more often students with a sign by day 27 fail to complete than comparable
students without it. Its baseline is the unadjusted rate difference for each sign: the non-completion rate of students
with the sign minus that of students without it. Its primary approach is a logistic regression of non-completion on
the signs, with a fixed effect for each module run, which compares students only within the same run, adjustment for
previous attempts and credits studied, and sign × module terms, which let the size of a sign's association differ by
module.

**AQ2: why this model.** Fixed effects suit a design in which every run of the studied modules is observed, and
whether to cluster standard errors follows from how the data were sampled, not from the grouping alone [12]; since
every run is observed rather than sampled, the model uses robust standard errors without clustering. A
mixed-effects model, which treats modules as a sample from a larger population, is set aside, because 6 modules and 9
training runs are too few to estimate the variance between them. The effect is reported as the average risk
difference in percentage points, with odds ratios beside it. Odds ratios read larger than risk ratios when an outcome
is common, and 44–46% of students do not complete; a p-value, in turn, does not measure the size or importance of an
effect [13]. The signs are correlated with each other, so their mutually adjusted estimates are partial effects: each shows the gap linked to one sign when the other signs
are held equal, which is smaller than the gap the sign shows on its own and is not the share of non-completion that the
sign explains. Both are therefore shown side by side. On the remaining criteria,
the model assumes that signs add up on the log-odds scale within a module, which the sign × module terms relax; it fits
the data, since even the smallest training run holds 369 enrolments with 91 non-completers; it is deterministic, giving the same result on
every rerun, and is checked with robust standard errors and sensitivity runs; and it uses no sensitive attribute as a sign.

**AQ2: the data it uses.** AQ2 is estimated on the 9 runs of 2013 and replicated on the 13 runs of 2014 only after the
AQ3 test (C14), so that no test outcome is seen while the predictive model is chosen. Appendix I (Table A.1) compares the AQ2
candidates cell by cell against the eight criteria.

===== reports/milestone-4/report/03-03-predictive.md @ 19d35a4 =====
## 3.3. Predictive Question

**Purpose.** AQ3 differs from AQ2 in purpose: a predictive model is judged by its accuracy on cases it has not seen,
not by how well it fits the cases it learned from [5], and the main threat is overfitting, a model that learns the
noise of its training data [3].

**Baselines.** Three baselines set the bar. The first is a random list, the level that any method must beat. The
second is the early-sign rule (C10), ranked by its number of signs, with ties broken by lower activity relative to the run (a student's clicks up to the
cut-off against the median of the same run); Milestone 1 named this rule as the comparison for deciding who is listed (D1), so beating it is what makes a
model worth using. The third is a background-only logistic model, with module, start month, previous attempts, credits, education and registration lead (how many days before the start
the student registered) but no activity, which shows how much of a ranking comes from who the
student is rather than from what the student does.

**Primary approach.** The primary approach is a penalised logistic regression, a logistic regression whose
coefficients are shrunk towards zero to limit overfitting, on the 19 usable primary predictors, with one model per cut-off; module and start month are categorical and enter
as dummy terms, one per level except a reference level, so the model has 23 parameters in all. The primary predictors fall into four groups, all dated on or before the cut-off: background (module, start month,
highest education, previous attempts, credits studied, registration lead, banked results, which are assessment results carried over from an earlier run of the module); activity (clicks before
the start and from the start to the cut-off, active days, resources used, inactivity in the last seven days, activity
relative to the run); assessment tasks (tasks due, missed and late, with late TMAs and late CMAs counted apart); and
the number of CMA marks known by the cut-off. The extended set adds 10 further predictors (a missing-registration
indicator, clicks counted with exactly repeated records taken once, clicks in the 14 days before the start, days since the last click, the trend over the
last week, tasks submitted early and clicks on four kinds of resource) and the weekly click counts, 2 at day 13 and 4 at
day 27; it is tried as an alternative (Table 2.3). A logistic model assumes that each predictor shifts the log-odds of
non-completion by a fixed amount per unit, while activity is strongly skewed: per enrolment the median is 602 clicks over
the whole run, and 2,503 enrolments lie beyond the upper interquartile-range fence. The predictors are therefore
transformed before the model reads them: counts enter as the logarithm of one plus the count, missing values are
filled with the training median and marked by a missing-value indicator, and every predictor is standardised with the
training mean and standard deviation, so that the penalty shrinks all coefficients on the same scale. Milestone 3
fitted these transforms on the 2013 runs alone and showed that no test row changes them; here they are refitted inside
each fold (Section 4.2), while gradient-boosted trees read the predictors untransformed. The reasons
come from this project. Tutors must see why a student is listed, and a transparent model gives each student's reasons
from the same equation that ranks them [11]. The training runs hold 5,245 non-completers at day 27 and 5,519 at day
13, about 230 events (non-completers) per parameter, and the 11,811 training enrolments at day 27 are about seven times the 1,731 that the
minimum sample size criteria of Riley et al. require under their default assumptions [14], so the size of the data does not limit a logistic model. The two classes are close in size, 44–46% of enrolments not
completing, so no resampling or reweighting for imbalance is needed, and metrics are read against each run's base
rate (Section 4.3). The risk to be tested is transfer to a later run, and training on earlier runs
mirrors use [6], as OU early-warning studies do [15]. Differences between courses enter as module terms [16] rather
than as one model per module, because shrinkage does not rescue small samples [17]. A review of 71 clinical
comparisons supports the choice: among comparisons at low risk of bias, it found no difference in discrimination
between logistic regression and machine learning (author-reported) [18].

**Challenger and extension.** Gradient-boosted trees, an ensemble of small decision trees each fitted to the errors of
the previous ones, are the challenger, since tree ensembles outperform deep learning on tabular data of about 10,000
rows. That benchmark removed the datasets on which logistic regression came within 5% of the best models, so it does
not show that trees beat logistic regression [19]; they replace the primary approach only if they beat it by the
margin fixed in advance in Section 4.2. A discrete-time survival model would fit a weekly hazard of withdrawal with
the same software [8], but the target joins Fail, decided at the end of the run, with Withdrawn, so survival remains an
extension. Penalisation improves calibration only on average [17], so calibration is checked rather than assumed
(Section 4.3). Appendix I (Table A.2) compares the AQ3 baselines and candidates cell by cell against the eight criteria.

===== reports/milestone-4/report/03-04-ranking-capacity.md @ 19d35a4 =====
## 3.4. Ranking under Capacity

**The list.** AQ4 uses the AQ3 scores of Section 3.3 to form one list per module run, whose length k follows the
assumed capacity: 3 or 5 contacts per tutor group, with a tutor group assumed to hold 20 students, that is 15% or 25%
of the enrolments registered at the cut-off. OULAD records no tutor group, so one list per run stands in for the
tutors' lists. The list is judged by its top, where the ranking matters for the decision [6], [7]. Its baselines are a
random list, whose expected recall equals k/n, the list length over the run's size, and the rule-ranked list of the
same length. Risk tiers, a first tier of the top 3 per 20 and a second of the next 2 per 20, are the candidate form
for tutors who want a lighter second contact; both cut points come from capacity, not from the test data. On the remaining criteria, the top-k list needs no fitting
of its own, so it is as robust and reproducible as the AQ3 scores; its untested assumption is that the order of risk
matches the order of need; and its fairness is checked by group at the same capacity (Section 4.4).

**What tutors see.** The list gives tutors ranks and each student's main contributing signs, and shows probabilities
only when calibration holds (Section 4.3). The tutor decides whom to contact, using knowledge that the data do not
hold [11].

**A ranking by benefit is rejected.** Ranking students by the expected benefit of a contact is rejected, because
estimating how the effect of an intervention varies between people needs randomised or otherwise unconfounded data on
treatment [9], and in field experiments on customer retention, the customers at the highest predicted risk were not the best targets of an
intervention [20]. The assumption that the order of risk matches the order of need therefore stays untested until a
randomised pilot (Section 5.2). Appendix I (Table A.3) compares the AQ4 baselines and candidates cell by cell against the eight criteria.

===== reports/milestone-4/report/04-00-evaluation-design.md @ 19d35a4 =====
# 4. Evaluation Design

With the methods of Part 3 chosen, the evaluation is fixed before any code runs. The brief requires the evaluation
plan even when no code is written, and it rules out choosing metrics or thresholds after the results are seen, because
running many models and then picking the metric that looks best makes any result look good [1]. The current reporting
standard for prediction models built by regression or machine learning, the
Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis statement updated for AI (TRIPOD+AI), frames evaluation as
three properties, each measure stated with its rationale [21]: discrimination, how well the model separates students
who will not complete from those who will, measured here on the
receiver operating characteristic (ROC) curve by the
area under the ROC curve (ROC-AUC), and on the precision–recall curve by the
area under the precision–recall curve (PR-AUC); calibration, whether its predicted risks match the observed rates; and
usefulness for the decision the model supports. In addition, data leakage has affected at least 294 published studies
across 17 fields [22], so the design also fixes who may see which data, and when.

Section 4.1 gives the Evaluation Design Card of each question and defines the metrics, Section 4.2 the validation
strategy, Section 4.3 the metrics and success criteria, and Section 4.4 the error, subgroup and fairness analysis.

===== reports/milestone-4/report/04-01-evaluation-cards.md @ 19d35a4 =====
## 4.1. Evaluation Design Cards

**What a card holds.** The brief asks for an Evaluation Design Card for each question with seven items: the primary
and secondary metrics, the validation strategy, the baseline, the error analysis, the fairness or subgroup check and
the success criterion [1]. The metric follows the decision it supports: recall matters when a contact is cheap and
missing a struggling student is costly, precision when a contact is costly [23], and when only a limited number of
top-ranked cases can be acted on, performance among those cases is the practical measure [24].

**Capacity and the main operating point.** The capacity k of a run is 3 or 5 contacts per tutor group, with a group
assumed to hold 20 students, that is 15% or 25% of the enrolments registered at the cut-off. The main operating point
is 5 per 20 at day 27, because it serves the list delivered in week 5 and is close to the share of students the early-sign rule flags at day 27: 28.8% of the 27,535 enrolments registered then
across all 22 runs, a share computed without any outcome. A confusion matrix of listed and unlisted students against
their outcome is reported for each run; at a fixed list length its cells give recall, precision and lift, which
replace the F1 score, because the list length is set by capacity rather than chosen to balance the two kinds of error.
The Brier score that the AQ3 card lists is the mean squared difference between predicted risk and outcome.

**AQ1.** Table 4.1 gives the card of the descriptive question, whose evaluation checks counts and denominators rather
than accuracy.

**Table 4.1. Evaluation Design Card of AQ1**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Non-completion rate and outcome shares per module, run, start month and year, with 95% confidence intervals for proportions |
| Secondary metric(s) | Cumulative share of enrolments with a first missed task by week, by outcome |
| Validation strategy | Denominator checks: 32,593 enrolments in total and 28,061 in the KPI population; two independent aggregation paths (prepared view and raw tables) must agree exactly |
| Baseline | Pooled rate over all runs; rate over all 32,593 enrolments (second denominator); rate without the 138 enrolments flagged for missing withdrawal or registration days |
| Error analysis | Runs whose rate moves by more than its interval between the two denominators; runs with no task due by day 27 |
| Fairness / subgroup check | Rates by gender, disability, deprivation band and age band reported as description only |
| Success criterion | Both aggregation paths agree to the enrolment; every rate carries its denominator and interval; no rate is compared across runs without its interval |

**AQ2.** Table 4.2 gives the card of the diagnostic question, whose evaluation judges the size and consistency of each
association.

**Table 4.2. Evaluation Design Card of AQ2**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Average risk difference of each sign within module run, in percentage points, with 95% interval; odds ratios reported beside it, since at 44–46% non-completion they read larger than risk ratios; p-values are not used as the sole basis for a conclusion [13] |
| Secondary metric(s) | Unadjusted rate difference per sign; module-specific risk differences from the sign × module terms of the same model |
| Validation strategy | Estimated on the 9 runs of 2013 (6 modules); task-based signs only in runs with a task due by day 27; replicated on the 13 runs of 2014, including module CCC, the one module with no 2013 run, only after the AQ3 model is frozen and scored; no 2014 AQ2 result may change AQ3 |
| Baseline | Unadjusted rate difference per sign, shown beside the adjusted estimate |
| Error analysis | Binned residuals by run and activity level; correlation among the click-based signs; sensitivity to de-duplicated clicks, to the rule variant that also counts late CMAs, to the 138 flagged enrolments and to dropping runs with no task due |
| Fairness / subgroup check | Associations by gender, disability and deprivation band, described, not adjusted away |
| Success criterion | A sign is a consistent association when its adjusted risk difference is at least 5 percentage points with an interval excluding 0, the smallest gap we treat as worth a tutor's attention, which equals the SMART Goal's target gain, and has the same direction in at least two-thirds of the modules where it is defined; otherwise weak or inconsistent. No association is stated as a cause [1] |

**AQ3.** Table 4.3 gives the card of the predictive question, the one with a single success gate.

**Table 4.3. Evaluation Design Card of AQ3**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity, computed per run with the run's own list and pooled over runs: the non-completers listed in all runs divided by the most the lists could hold, which for each list is k non-completers, or all of the run's non-completers if there are fewer (day 27, k = 5 per 20) |
| Secondary metric(s) | Recall, precision and lift at capacity (re-expressions of the same true positives at fixed k); unweighted mean of per-run differences between model and rule; ROC-AUC and PR-AUC computed within run and averaged; calibration-in-the-large and calibration slope; Brier score; net benefit as context only, since it describes a threshold policy rather than a fixed capacity [25]; the same at day 13 and at k = 3 per 20 |
| Validation strategy | Development on the 9 runs of 2013 with leave-one-run-out folds; a single, logged scoring of the 13 runs of 2014 after the second freeze, which fixes the final model before any test outcome is opened (Section 4.2) [21], [26] (Section 4.2; Appendix III) |
| Baseline | Early-sign rule as frozen in Change Log entry C10, ranked by its number of signs with ties broken by lower relative activity; a background-only logistic model (module, start month, previous attempts, credits, education, registration lead, no activity); random list |
| Error analysis | Missed non-completers and listed completers by run, module, activity level, previous attempts, late registration and kind of non-completion (Fail or Withdrawn); recall among active students only; recall among reachable non-completers, those not withdrawn within 7 days after the cut-off; stability of list membership near rank k under the bootstrap; CCC runs apart |
| Fairness / subgroup check | Confirmatory check of recall at capacity by group (a formal test on groups fixed in advance) and descriptive checks (Section 4.4) |
| Success criterion | S1 (single gate): on all 13 test runs, all eligible enrolments, day 27, k = 5 per 20, the primary model's pooled normalised recall exceeds the rule-ranked list's, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip permutation test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses are counted apart. S2, precision at capacity, is reported and is not a gate (Table 4.5). S3 (condition for showing probabilities): calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2 on the pooled point estimates; otherwise tutors see ranks and reasons only. All other populations, cut-offs and capacities are sensitivity analyses that cannot change the verdict |

**AQ4.** Table 4.4 gives the card of the ranking question, which shares the AQ3 gate and adds the fairness check.

**Table 4.4. Evaluation Design Card of AQ4**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity (recall against the attainable maximum, Change Log C13) |
| Secondary metric(s) | Lift over the run base rate; overlap of the model list with the rule list; true positives on the list split into Fail and Withdrawn; recall at 3 and 5 per 20 |
| Validation strategy | As AQ3: lists formed per test run of 2014 from the frozen scores |
| Baseline | Random list (expected recall k/n) and rule-ranked list of the same length |
| Error analysis | Runs where the list fills its capacity with completers; students with no activity at all, whom every list catches, separated from active students at risk |
| Fairness / subgroup check | Selection rate, recall and precision at capacity by deprivation band and disability (named in AQ4), and by gender and age band (Appendix IV) |
| Success criterion | Gate S1 met by the list; the confirmatory fairness check of Section 4.4 passes or its flags are reviewed before use; the assumption that risk order matches need is stated as untested; no statement about the effect of contact [1] |

**Metric definitions.** The cards use metrics that are defined once here, for a run r with n enrolments, the set Y of
its non-completers, base rate b = |Y|/n, and a list L of the k highest scores. In words: recall at capacity is the
share of the run's non-completers who are on the list; attainable recall is the most a list of length k can reach,
which is below 1 when the run has more non-completers than places on the list; normalised recall divides recall by
that ceiling, so that 1 means the best list possible; precision is the share of the list who do not complete; and
lift divides precision by the base rate, so that 1 means no better than chance. Appendix II (Table A.4) gives the formula of every metric.

===== reports/milestone-4/report/04-02-validation-strategy.md @ 19d35a4 =====
## 4.2. Validation Strategy

**Test on unseen runs.** The cards of Section 4.1 rest on one validation design, drawn in Appendix III (Figure A.2). Testing on data
not used in model development is the core requirement of TRIPOD+AI [21], and the 13 test runs of 2014 share no run with
development. Testing on a later period is in addition a form of external validation [27], and in predicting student
success only an evaluation on a future course gives an honest estimate of how a model will perform in use [23]. The
1,586 test enrolments at day 27 of students already seen in the 2013 development data stay in the test, as they would in use, and are
removed in a sensitivity analysis.


**Development folds.** Development uses only the 9 runs of 2013. Each run forms its own fold, so each model is
validated on a whole run it did not see, because ignoring the group structure of data seriously underestimates
prediction error [28]. Students who also appear in the held-out run are removed from that fold's training data, since
a validation fold must hold only groups that are absent from training [29]. Every step that learns from data, including
the filling of missing values, the scaling and the tuning of the model, is repeated inside each fold, because a tuned
cross-validation score is substantially optimistic [30], and over-fitting the criterion used to select a model can
bias results as much as the differences between algorithms [31].

**When a challenger wins.** Gradient-boosted trees, or the extended set of 10 further predictors with the weekly
clicks, replace the primary choice only with a gain of at least 0.03 in pooled normalised recall, about 89 more non-completers listed over the 9 runs, and a gain in at least 7 of the 9 folds; if the two were equal,
a gain in 7 or more folds would occur by chance with a probability of about 0.09. The margin is fixed now, before any
fold result exists, so that a small, chance improvement cannot change the choice.

**Two freezes and one test.** The protocol follows the two-step freeze proposed for predictive modeling: the
question, splits, metrics and baselines are fixed before training, and the final model is fixed, with access to the
test data recorded, before testing [26]. The chosen model is refitted on all 2013 runs and scored once on the 13 runs
of 2014. Results are also reported apart for the 9 paired runs, whose module and start month also ran in 2013, and for
the 4 unpaired runs.

**Two features of the run structure.** Module CCC has no run in 2013, so module terms are coded as deviations from the
average module, and an unseen module receives the average. Presentations coded B start in February and those coded J
in October [2]. The 2013 J runs start in October 2013 and last 261–268 days, ending around mid-2014, whereas the 2014 B
runs start in February 2014 and reach their cut-offs a few weeks later, when the 2013 J outcomes are not yet known; a
labels-available variant therefore also scores the 2014 B runs with a model trained only on the 2013
B runs, the only runs whose outcomes a university would hold at that time.

**The protocol step by step.** Appendix III (Table A.5) lists the eight steps of the protocol in order, with the data
each uses, what happens and why; the paragraphs above describe each of them.

**Uncertainty.** Uncertainty about the gate comes from a paired two-level bootstrap: runs are resampled, then
enrolments within each sampled run, each run's list is formed again from its resampled enrolments, and the difference
between model and rule is computed on the same resample, because treating nested observations as independent inflates
false positives [32]. With only 13 test runs such intervals can be too narrow, so the gate also requires a sign-flip
permutation test on the 13 per-run differences, which asks how often differences as favourable would appear if the sign
of each run's difference were random.

**Sample sizes.** Appendix III (Table A.6) gives the sample sizes behind these choices, computed from the prepared views without
fitting a model; outcome counts come from the 2013 runs only, so the 2014 outcomes stay unseen. The minimum development size follows the three criteria of Riley et al. [14]: expected shrinkage of at least 0.9,
meaning that the fitted effects need to be pulled back by no more than 10% on new data; optimism of at most 0.05 in
Nagelkerke R², a measure of how much of the variation in the outcome the model explains, between the development data
and new data; and the overall risk, the non-completion rate in the development data, estimated within 0.05.

**C14.** AQ2 is replicated on 2014 only after the single test, which is Change Log entry C14: it changes when AQ2 is
estimated on the test runs, not what AQ2 asks, and it protects the independence of the AQ3 test.

===== reports/milestone-4/report/04-03-metrics-success.md @ 19d35a4 =====
## 4.3. Metrics and Success Criteria

**Primary metric.** Under the protocol of Section 4.2, the primary metric is normalised recall at capacity: the
non-completers on a run's list divided by the most a list of that length can hold, pooled over runs (Table A.4). It
reads the quality of a list against the ceiling that capacity sets, and that ceiling varies widely: in the training
runs, a list of 5 per 20 at day 27 can hold between 46% and 100% of a run's non-completers (C13). At a fixed list
length, recall, precision and lift are re-expressions of the same count of non-completers on the list, so they serve
as secondary views rather than separate criteria.

**Secondary metrics.** Precision and PR-AUC must be read against the base
rate, which is their level by chance [24]. The ROC curve plots the rate of true
positives against the rate of false positives at every threshold, and the area under it (ROC-AUC) is the probability
that a non-completer scores above a completer; it is computed within each run, so that a model cannot score well
merely by separating high-rate runs from low-rate ones.

**Calibration.** Calibration is assessed because predicted risks can be unreliable even when discrimination is good
[33]. Two numbers summarise it: the calibration-in-the-large, the intercept of a recalibration model (a logistic
regression of the outcome on the score's log-odds) with the slope fixed at 1, whose target is 0 and which shows whether risks are too high or too low on average; and the calibration slope,
whose target is 1 and which falls below 1 when risks are too extreme [33]. Calibration cannot be a success criterion on
its own, since a model that gives every student the base rate is perfectly calibrated and useless [27].

**Net benefit.** Net benefit compares the model with contacting every student, no student or the students the rule
flags, at a range of threshold probabilities [25]. It describes a policy of contacting everyone above a threshold,
whereas AQ4 acts on a fixed capacity, so it serves as context rather than as a criterion.

**Success criteria fixed before testing.** A difference smaller than the variation between samples has little
practical meaning [31], and judging a model on several gates or populations would let one of them pass by chance, so
the design names a single gate and a single population. Table 4.5 fixes the success
criteria before any result exists.

**Table 4.5. Success criteria fixed before testing**

| ID | Criterion | Population and operating point | Role |
| :---- | :---- | :---- | :---- |
| S1 | Pooled normalised recall of the primary model above that of the rule-ranked list, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses reported | All 13 test runs, all eligible enrolments, day 27, 5 per 20 | Single gate for AQ3 and AQ4 (who is listed, D1) |
| S2 | Precision at capacity against the base rate and the attainable maximum | Same | Reported, not a gate |
| S3 | Calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2, pooled point estimates | Same | Condition for showing probabilities; otherwise ranks and reasons only |
| FR1 | No confirmatory group in which recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups (a correction that keeps the chance of any false flag at 5% across them), lies entirely below 0; a group meeting both conditions is flagged for review | Same; three confirmatory groups (Section 4.4) | Condition for use; a flag leads to review |

**Reading the gate.** S1 asks whether the model's lists, at the main operating point, reach more non-completers than
the rule's lists of the same length, with enough certainty that the gain is not chance. The paired two-level bootstrap and the
sign-flip test of Section 4.2 supply that certainty. Every other population, cut-off and capacity is a sensitivity analysis that
cannot change the verdict. The bounds of S3 allow an average predicted risk between about 40% and 49% when the training rate is 44.4%, a tolerance
of about five points, the size of the SMART Goal's target gain, and a spread of risks 20% too wide or too narrow. A
failed calibration check limits the output to ranks and reasons, and it never leads to
recalibration on the 2014 runs, which would let the test data shape the model.

===== reports/milestone-4/report/04-04-error-fairness.md @ 19d35a4 =====
## 4.4. Error, Subgroup and Fairness Analysis

**Why groups are checked separately.** Building on the criteria of Section 4.3, the frozen model is evaluated
separately for each audit group, because aggregate metrics can hide differences between groups, an approach known as
slicing analysis [34]; TRIPOD+AI likewise asks for estimates by subgroup with intervals and for the approach used to
address fairness [21]. Gender, disability, deprivation band and age band stay out of the predictors and serve only the
audit, because leaving them out does not make a model blind to them: activity, previous attempts or credits can carry
the same information [35].

**One criterion must lead.** Fairness criteria cannot all hold at once when non-completion rates differ between
groups: a score with equal positive predictive value across groups cannot also have equal error rates [36], and
calibration within groups and balanced error rates conflict except in degenerate cases (perfect prediction or equal base rates across groups) [37]. The audit therefore names
one primary criterion, separation, measured as equal recall at capacity across groups. Separation is recommended for
dropout prediction that allocates extra support [35], and it matches a contact whose main harm is missing a student
who struggles.

**The audit groups.** The confirmatory check covers the three groups that AQ4 names and that hold at least 400 test
enrolments: students with a declared disability (1,488 at day 27), the most deprived band, 0–10% (1,486), and the
missing deprivation band (610). At the training non-completion rates even the lowest-rate eligible group, the missing
band (28%), holds more than 100 non-completers. The two numbers rest on one calculation: with about 100 non-completers in a group,
the standard error of a recall near 0.5 is about 5 percentage points, and the rest of the students are many times more numerous, so their recall has a much smaller standard error and the
group's recall is the main source of uncertainty in the gap; the gap of 10 points in rule FR1 is therefore about two
standard errors of the group's recall. In addition, 400 enrolments at the lowest group rate of 28% give about 112
non-completers (400 × 28%), above 100. Students aged 55 or over (118 test enrolments, below the threshold of
400) are reported as a point gap, marked "insufficient data, not cleared". Appendix IV (Table A.7) gives each group's size and
how it is handled; eligibility is fixed here from enrolment counts, before any test outcome is opened.

**The checks.** Rule FR1 of Table 4.5 flags a group for review; it does not reject the model, because a flag calls for
human judgement on why the gap arises. Earlier work on OULAD found that most published at-risk models reproduced and
slightly amplified a gap in favour of male students and showed erratic bias for students with a declared disability
(author-reported) [38], which is why the small groups are pooled over runs and reported with intervals. A proxy check
compares scores and predictors across groups, to show which predictors carry group information. The 
absolute between-ROC area (ABROCA), the area between a group's ROC curve and that of the other students [34], stays
descriptive, because it measures differences across all thresholds rather than at the capacity where the decision is
made. Appendix IV (Table A.8) lists every fairness and error check: the confirmatory check of separation, and descriptive
checks of selection, precision and calibration by group, the threshold-free gap in discrimination (ABROCA), the proxy check, errors by run,
activity, history and kind of non-completion, and the stability of the list.

===== reports/milestone-4/report/05-00-risk-ethics.md @ 19d35a4 =====
# 5. Risk, Ethics and Limitations

The evaluation of Part 4 measures how well the methods work; what can go wrong when they are built and used needs its
own record. The brief names leakage, overfitting, causal overclaim, unfairness and high-stakes automation as the risks
to review [1]. The risks are organised with the AI Risk Management Framework of the
National Institute of Standards and Technology (NIST), whose four functions are govern, map, measure and manage [39]: deciding who is responsible,
identifying where each risk arises, checking whether a control works and acting on what remains.

**Risk and Ethics Notes.** Table 5.1 gives the Risk and Ethics Notes of the brief: for each area, the main risk in
this project, the control the proposal builds in and the section that treats it.

**Table 5.1. Risk and Ethics Notes**

| Area | Main risk in this project | Control | Section |
| :---- | :---- | :---- | :---- |
| Leakage | Information from after the cut-off or from the test runs reaching the model | Dated predictors; refitting inside folds; single logged test | 5.1 |
| Overfitting and test reuse | Optimistic fold scores; choosing a favourable test variant | Nested tuning; margin fixed in advance; one declared gate | 5.1 |
| Interpretability | Reasons that do not match the ranking; partial effects read as weights | Reasons from the scoring model; adjusted and unadjusted estimates together | 5.1 |
| Causal limits | Reading the list as proof that contact helps | No effect claim; randomised pilot before any benefit ranking | 5.2 |
| Fairness | Lower recall for disabled or deprived students; proxies | Separation as primary criterion; confirmatory check; proxy check | 5.2 |
| High-stakes use | Automation bias; labelling; legal duties at the university | Tutor decides and can override; flags expire with the run; risk classification under Vietnamese AI law before a pilot | 5.2 |
| Data constraints | 9 training runs; module CCC unseen; distance learning in the United Kingdom (UK) of 2013–2014 | Run-level split; module CCC reported separately; local validation before use | 5.1 |

**Risk register.** Appendix V (Table A.9) gives the full register of sixteen risks. Each row names where a risk arises in this
project, the control that the proposal builds in, the check that shows whether the control works, and the risk that
remains after the control.

Section 5.1 treats the risks to the validity of the evaluation, and Section 5.2 the risks of using the list on real
students.

===== reports/milestone-4/report/05-01-leakage-interpretability.md @ 19d35a4 =====
## 5.1. Leakage, Overfitting and Interpretability

**Leakage.** Following the notes of Table 5.1, the first group of risks concerns the validity of the evaluation.
Leakage covers three failures that matter here: an unclean separation of training and test data, including
preprocessing fitted on the whole dataset; features that act as proxies of the outcome; and temporal leakage, or
dependence between training and test samples [22]. The modeller should not see information beyond the point that
separates training from testing [40]. The 2014 outcomes therefore stay unopened until the single test, AQ2 waits for it (Change Log entry C14, Appendix VII), and every learned step is refitted inside each fold. Predictors must have been available at the moment the
model is used [41], which the dated feature views ensure and the labels-available variant checks, since the outcomes of the
October 2013 runs are not yet known when the February 2014 runs reach their cut-offs.

**Overfitting.** Overfitting also enters through the choice of model: a fold score that was tuned on the same folds is
optimistic [30], so fold results serve only the choice between candidates and are never reported as performance.
Published comparisons of machine learning with logistic regression are often biased by flaws in validation and silent
on calibration [18], which the frozen validation of Section 4.2 is designed to avoid.

**Interpretability.** Interpretability is built into the choice of model rather than added afterwards. Each student's
reasons come from the same logistic model that ranks the student, which avoids explanations made afterwards that can
mislead [11]. Many different models, with different coefficients, fit about equally well [5]; the chosen
model's coefficients are one of many sets that fit the data, so no coefficient is read as a cause, and AQ2's
mutually adjusted estimates are shown beside the unadjusted gaps. The final model is to be documented in a model card,
which states its intended and out-of-scope uses with its performance by group [42], and the prepared data in a
datasheet, which records their composition, collection and recommended uses [43].

**Data constraints.** The data limit what can be claimed: 9 training runs from 6 modules, one module (CCC) seen only
in 2014, and distance learning in the UK in 2013–2014. Any use at a Vietnamese university therefore
starts with validation on the university's own records.

===== reports/milestone-4/report/05-02-causal-fairness-use.md @ 19d35a4 =====
## 5.2. Causal Limits, Fairness and High-Stakes Use

**Causal limits.** Beyond the validity risks of Section 5.1, the list will shape decisions about real students. Its
first limit is causal. The effect of an intervention is best answered by a randomised experiment, which observational
data can at most emulate [44], and estimating for whom a contact helps needs randomised or unconfounded data on
treatment [9], which OULAD lacks. Risk and benefit can also diverge: the students at highest risk do not always benefit
most, as field experiments in customer retention showed [20]. The choice of contact, and any ranking by the expected benefit of a contact, therefore stay deferred; AQ4
supplies only the list of whom to contact first (D1), and the next step is a randomised pilot whose time zero, the
moment from which every student in the pilot is followed, is the cut-off at which students become eligible for the list [44], with contacts and outcomes logged together.

**Fairness.** Fairness has a second limit: a score cannot have equal predictive value and equal error rates across
groups whose non-completion rates differ [36], so separation leads (Section 4.4). A flag leads to support and expires
with the run, because flagged students should be able to prove the prediction wrong [45], and labels must not bias how
staff see a student [46].

**High-stakes and regulated use.** The use is high-stakes, and it is regulated. The European Union (EU) AI Act, a
reference standard here rather than a law that binds a Vietnamese university, lists as high-risk the systems that
evaluate learning outcomes or steer learning, and requires that people can oversee and override them [47]; its main
obligations for these systems apply from 2 December 2027 under Regulation (EU) 2026/1744, according to a legal commentary [48]. Vietnam's Law on AI, No. 134/2025/QH15, applies from 1 March 2026 and requires human control over decisions made with AI
[49]; Decision 33/2026/QĐ-TTg lists as high-risk in education the systems that rank learners or analyse learner
behaviour [50]; and processing personal data with AI must be classified by level of risk [51]. Such a list at a
Vietnamese university is therefore likely to be high-risk, a reading that the university's legal staff must confirm
from the official texts before a pilot. A pilot needs a risk classification first, and tutors keep
the final say, can override any entry and see the reasons behind it.

**Feedback after use.** Once tutors act on the lists, the outcomes partly reflect the contacts, a performative effect
in which a prediction changes what it predicts [52], so contacts are logged with outcomes before any model is
retrained.

===== reports/milestone-4/report/06-00-genai-usage.md @ 19d35a4 =====
# 6. Generative AI Usage

**Roles.** Alongside the risks of Part 5, generative AI was used in the roles that the brief allows a modeling
partner: explaining methods, proposing and challenging candidate families, and reviewing metrics, splits, leakage,
class imbalance, calibration and fairness, while the final choice and the evidence for it remain ours [1]. We decided on every suggestion and verified it against the prepared data, the sources or the arithmetic,
as the log below shows. Three roles were used: a literature assistant that found and read sources, a model-selection
critic that challenged the briefs and the candidate comparison, and an evaluation reviewer that challenged the cards,
the protocol, the fairness analysis and the risks.

**AI Decision Log.** Table 6.1 is the AI Decision Log in the brief's five columns, one row per significant AI
contribution: the prompt or goal, the AI's suggestion, our decision, the evidence used to verify it and its
effect on the proposal.

**Table 6.1. AI Decision Log**

| Prompt / goal | AI suggestion | Team decision | Evidence / verification | Effect on the proposal |
| :---- | :---- | :---- | :---- | :---- |
| Find well-known sources on method choice for each AQ (literature assistant) | Explain-versus-predict distinction; rule and simple baselines first; interpretable models for high-stakes use; sample size criteria; survival and ranking framings | Accepted after reading each source | Every statement checked against a saved copy of its source, with a verbatim quotation | Parts 2–3; Appendices I–II |
| Find sources on evaluation design (literature assistant) | TRIPOD+AI and the Prediction model Risk Of Bias ASsessment Tool for AI (PROBAST+AI); calibration; grouped folds; nested tuning; leakage types; pre-registration; hierarchical bootstrap; slicing analysis | Accepted; the imbalance argument for precision–recall curves not used, since non-completion is 44–46% and the classes are therefore not imbalanced | Same verification | Part 4; Appendices III–V |
| Find sources on risk, causality, fairness and regulation (literature assistant) | Target trials and uplift need treatment data; fairness criteria conflict; EU AI Act and Vietnam's AI law and high-risk list; performative prediction | Accepted; the EU Act used as a reference standard, Vietnamese law as binding on a Vietnamese pilot | Legal texts read in official copies where available; the EU text in a secondary copy | Part 5; Appendix V |
| Review the model selection as a sceptical analyst (critic) | 12 critiques: within-run evaluation, run-grouped folds, one primary test comparison, AQ2 per-module output, reasons from the scoring model, rule for switching to the challenger, survival assumption, sample size versus transfer, ranks versus probabilities, fairness power, risk versus need, repeat students | 10 accepted, 2 accepted in part (Table A.10) | Each critique checked against the design facts and the run lengths | Appendices I–II and IV–VI |
| Review the evaluation design as a methodologist (reviewer) | 12 critiques: unseen module, per-run versus tutor capacity, S1 inference, S2 basis, primary population, calibration definition, model-choice aggregation, fairness gate, ABROCA reference, AQ2 effect measure, error-analysis gaps, missing risks | 12 accepted (Table A.11) | Arithmetic of each critique recomputed | Appendices III–VI; S2 (precision at capacity) reported, not a gate |

**Decisions on the critiques.** Appendix VI (Tables A.10 and A.11) gives our decision on each of the 24
critiques of the model-selection critic and of the evaluation reviewer, with the evidence used to check it, and the
reviewers' prompts.

**Reflection.** The reviewers made the most consequential points. They asked, for example, that every count be taken from the 6 modules of the training runs, that the end dates of the
October 2013 runs be checked against the cut-offs of the February 2014 runs, and that the chance of a success rule be
computed, which showed that requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be
met by chance about 13% of the time; we verified each point against the prepared data before adopting it. The reviews were
most useful where the AI had to argue from the counts of the prepared data rather than from general advice. No AI
produced a metric value, a threshold or a result: every number in this proposal is a count from the prepared data or a
value we fixed with its reason, as the brief requires [1].

===== reports/milestone-4/report/07-00-prototype-protocol.md @ 19d35a4 =====
# 7. Prototype Protocol

**Purpose.** The optional prototype of Level 2 tests whether the Level 1 choices are feasible and shows their
trade-offs; it does not compete for the best score, and it requires no large-scale tuning [1]. This report does not
run the prototype, so it states no model performance; it specifies how the prototype will run, so that whoever runs it
follows the evaluation fixed in Part 4.

**Steps.** Table 7.1 gives each step of the brief with how the prototype carries it out. Because the proposal is
frozen first, the prototype can confirm or refute the choices of Level 1, but it cannot reshape them after its results
are seen.

**Table 7.1. Prototype protocol**

| Brief step | Specification |
| :---- | :---- |
| 1. Reproduce data input | Load OULAD-N04-prepared-1.0, check its file hashes, change no raw data |
| 2. Implement baseline | Rule-ranked list, background-only model and random list, before any candidate |
| 3. Implement candidate | Penalised logistic regression (primary) and gradient-boosted trees (challenger), as in Table 3.1 |
| 4. Split and fit correctly | Protocol of Section 4.2 and Appendix III |
| 5. Evaluate | Metrics of the cards (Tables 4.1–4.4) and criteria of Table 4.5, including unfavourable results |
| 6. Error and subgroup analysis | Error slices and confirmatory fairness check of Section 4.4 |
| 7. Compare to Level 1 expectation | Whether S1 holds and the challenger's margin was met; any change recorded with its reason |
| 8. Reproducibility | Scripts, seeds, package and data versions, folds and test-access record in an experiment log |

**A baseline may win.** A baseline that matches the candidate is an acceptable outcome. The brief notes that a simple
baseline can be the better choice when the improvement of a complex model is small and its interpretability is lower
[1]; in that case the rule or the background-only model is carried forward with its reasons, and the change is recorded
in the experiment log.

===== reports/milestone-4/report/08-00-traceability.md @ 19d35a4 =====
# 8. Updated Traceability Matrix

**The matrix of the brief.** Parts 1 to 7 give each question one chain from the Business Goal to the decision it
supports. Table 8.1 gives that chain in the columns that the brief sets for the end of Milestone 4 [1]: the analytics
level, the technical task, the baseline, the primary approach, the primary metric, the validation and the decision supported. The prepared data behind each row are the views of Milestone 3: the
enrolment and task views for AQ1, the day-27 feature view for AQ2, and both feature views with their model-ready
matrices for AQ3 and AQ4.

**Table 8.1. Updated Traceability Matrix**

| AQ | Analytics level | Technical task | Baseline | Primary approach | Primary metric | Validation | Decision supported |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Aggregation | Pooled rate; second denominator | Grouped rates with 95% intervals | Rate with interval and denominator | Two aggregation paths; known totals | D2, D3 |
| AQ2 | Diagnostic | Association within module run | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval | 2013 runs; replication on 2014 after the AQ3 test | D2; signs for D1 |
| AQ3 | Predictive | Binary classification at day 13 and day 27 | Rule-ranked list; background-only model; random list | Penalised logistic regression on the primary predictors, unless gradient-boosted trees or the extended set win by the fixed margin | Normalised recall at capacity | Leave-one-run-out on 2013; single test on 2014 | D1 |
| AQ4 | Prescriptive (ranking) | Ranking under capacity | Random and rule-ranked lists | Top-k per run with reasons | Normalised recall at capacity | As AQ3; confirmatory fairness check | D1; choice of contact deferred |

**The full chain.** Appendix VII (Table A.12) extends the traceability of Milestone 3 to the modeling and evaluation choices, so that
each row runs from the Business Goal and its KPI, through the question, its level and task, to the prepared data, the
baseline and primary approach, the primary metric, the validation and the decision supported. The Business Goal is to
improve successful course completion by identifying students who stop taking part early enough to support them within
the semester, and the primary KPI is the completion rate of students enrolled after the add-drop period.

**The change of this milestone.** Appendix VII (Table A.13) gives Change Log entry C14 in the format of the Controlled
Change Log: AQ2 is replicated on the 2014 runs only after the AQ3 test, because estimating AQ2 on all 22 runs would open the test outcomes before the predictive model is frozen.

Every question keeps its link to the Business Goal and to the prepared views of Milestone 3, and the only change to how
a question is measured, C14, protects the independence of the AQ3 test.

===== reports/milestone-4/report/09-references.md @ 19d35a4 =====
# References

The references are formatted in APA style (American Psychological Association, 7th edition) and numbered for in-text citation in the form [n], in order of first citation.

[1] MTH045 – The Science of Data Analytics. (2026). *Milestone P4: From modeling to evaluation* [Course brief]. University of Science, VNU-HCM.

[2] Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, *4*, Article 170171. https://doi.org/10.1038/sdata.2017.171

[3] Shmueli, G. (2010). To explain or to predict? *Statistical Science*, *25*(3), 289–310. https://doi.org/10.1214/10-STS330

[4] Herodotou, C., Rienties, B., Hlosta, M., Boroowa, A., Mangafa, C., & Zdrahal, Z. (2020). The scalable implementation of predictive learning analytics at a distance learning university: Insights from a longitudinal case study. *The Internet and Higher Education*, *45*, Article 100725. https://doi.org/10.1016/j.iheduc.2020.100725

[5] Breiman, L. (2001). Statistical modeling: The two cultures (with comments and a rejoinder by the author). *Statistical Science*, *16*(3), 199–231. https://doi.org/10.1214/ss/1009213726

[6] Zinkevich, M. (2025). *Rules of machine learning: Best practices for ML engineering*. Google for Developers. Retrieved November 6, 2026, from https://developers.google.com/machine-learning/guides/rules-of-ml

[7] Aguiar, E., Lakkaraju, H., Bhanpuri, N., Miller, D., Yuhas, B., & Addison, K. L. (2015). Who, when, and why: A machine learning approach to prioritizing students at risk of not graduating high school on time. In *Proceedings of the Fifth International Conference on Learning Analytics and Knowledge* (pp. 93–102). ACM. https://doi.org/10.1145/2723576.2723619

[8] Singer, J. D., & Willett, J. B. (1993). It's about time: Using discrete-time survival analysis to study duration and the timing of events. *Journal of Educational Statistics*, *18*(2), 155–195. https://doi.org/10.3102/10769986018002155

[9] Athey, S., & Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects. *Proceedings of the National Academy of Sciences*, *113*(27), 7353–7360. https://doi.org/10.1073/pnas.1510489113

[10] Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J.-F., & Dennison, D. (2015). Hidden technical debt in machine learning systems. In *Advances in Neural Information Processing Systems 28* (pp. 2503–2511). Curran Associates.

[11] Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, *1*(5), 206–215. https://doi.org/10.1038/s42256-019-0048-x

[12] Abadie, A., Athey, S., Imbens, G. W., & Wooldridge, J. M. (2023). When should you adjust standard errors for clustering? *The Quarterly Journal of Economics*, *138*(1), 1–35. https://doi.org/10.1093/qje/qjac038

[13] Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician*, *70*(2), 129–133. https://doi.org/10.1080/00031305.2016.1154108

[14] Riley, R. D., Snell, K. I. E., Ensor, J., Burke, D. L., Harrell, F. E., Jr., Moons, K. G. M., & Collins, G. S. (2019). Minimum sample size for developing a multivariable prediction model: Part II – Binary and time-to-event outcomes. *Statistics in Medicine*, *38*(7), 1276–1296. https://doi.org/10.1002/sim.7992

[15] Hlosta, M., Zdrahal, Z., & Zendulka, J. (2017). Ouroboros: Early identification of at-risk students without models based on legacy data. In *Proceedings of the Seventh International Learning Analytics & Knowledge Conference* (pp. 6–15). ACM. https://doi.org/10.1145/3027385.3027449

[16] Gašević, D., Dawson, S., Rogers, T., & Gašević, D. (2016). Learning analytics should not promote one size fits all: The effects of instructional conditions in predicting academic success. *The Internet and Higher Education*, *28*, 68–84. https://doi.org/10.1016/j.iheduc.2015.10.002

[17] Van Calster, B., van Smeden, M., De Cock, B., & Steyerberg, E. W. (2020). Regression shrinkage methods for clinical prediction models do not guarantee improved performance: Simulation study. *Statistical Methods in Medical Research*, *29*(11), 3166–3178. https://doi.org/10.1177/0962280220921415

[18] Christodoulou, E., Ma, J., Collins, G. S., Steyerberg, E. W., Verbakel, J. Y., & Van Calster, B. (2019). A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models. *Journal of Clinical Epidemiology*, *110*, 12–22. https://doi.org/10.1016/j.jclinepi.2019.02.004

[19] Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why do tree-based models still outperform deep learning on typical tabular data? In *Advances in Neural Information Processing Systems 35* (Datasets and Benchmarks Track). https://arxiv.org/abs/2207.08815

[20] Ascarza, E. (2018). Retention futility: Targeting high-risk customers might be ineffective. *Journal of Marketing Research*, *55*(1), 80–98. https://doi.org/10.1509/jmr.16.0163

[21] Collins, G. S., Moons, K. G. M., Dhiman, P., Riley, R. D., Beam, A. L., Van Calster, B., Ghassemi, M., Liu, X., Reitsma, J. B., van Smeden, M., Boulesteix, A.-L., Camaradou, J. C., Celi, L. A., Denaxas, S., Denniston, A. K., Glocker, B., Golub, R. M., Harvey, H., Heinze, G., … Logullo, P. (2024). TRIPOD+AI statement: Updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*, *385*, Article e078378. https://doi.org/10.1136/bmj-2023-078378

[22] Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, *4*(9), Article 100804. https://doi.org/10.1016/j.patter.2023.100804

[23] Gardner, J., & Brooks, C. (2018). Student success prediction in MOOCs. *User Modeling and User-Adapted Interaction*, *28*(2), 127–203. https://doi.org/10.1007/s11257-018-9203-z

[24] Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLOS ONE*, *10*(3), Article e0118432. https://doi.org/10.1371/journal.pone.0118432

[25] Vickers, A. J., & Elkin, E. B. (2006). Decision curve analysis: A novel method for evaluating prediction models. *Medical Decision Making*, *26*(6), 565–574. https://doi.org/10.1177/0272989X06295361

[26] Hofman, J. M., Chatzimparmpas, A., Sharma, A., Watts, D. J., & Hullman, J. (2023). *Pre-registration for predictive modeling* (arXiv:2311.18807) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2311.18807

[27] Steyerberg, E. W., & Vergouwe, Y. (2014). Towards better clinical prediction models: Seven steps for development and an ABCD for validation. *European Heart Journal*, *35*(29), 1925–1931. https://doi.org/10.1093/eurheartj/ehu207

[28] Roberts, D. R., Bahn, V., Ciuti, S., Boyce, M. S., Elith, J., Guillera‐Arroita, G., Hauenstein, S., Lahoz‐Monfort, J. J., Schröder, B., Thuiller, W., Warton, D. I., Wintle, B. A., Hartig, F., & Dormann, C. F. (2017). Cross‐validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography*, *40*(8), 913–929. https://doi.org/10.1111/ecog.02881

[29] scikit-learn developers. (2026). *3.1. Cross-validation: Evaluating estimator performance* (Version 1.9.1) [Software documentation]. Retrieved November 6, 2026, from https://scikit-learn.org/stable/modules/cross_validation.html

[30] Varma, S., & Simon, R. (2006). Bias in error estimation when using cross-validation for model selection. *BMC Bioinformatics*, *7*, Article 91. https://doi.org/10.1186/1471-2105-7-91

[31] Cawley, G. C., & Talbot, N. L. C. (2010). On over-fitting in model selection and subsequent selection bias in performance evaluation. *Journal of Machine Learning Research*, *11*, 2079–2107. https://jmlr.org/papers/v11/cawley10a.html

[32] Saravanan, V., Berman, G. J., & Sober, S. J. (2020). Application of the hierarchical bootstrap to multi-level data in neuroscience. *Neurons, Behavior, Data Analysis, and Theory*, *3*(5). https://nbdt.scholasticahq.com/article/13927-application-of-the-hierarchical-bootstrap-to-multi-level-data-in-neuroscience

[33] Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., & Steyerberg, E. W. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine*, *17*(1), Article 230. https://doi.org/10.1186/s12916-019-1466-7

[34] Gardner, J., Brooks, C., & Baker, R. (2019). Evaluating the fairness of predictive student models through slicing analysis. In *Proceedings of the 9th International Conference on Learning Analytics & Knowledge* (pp. 225–234). ACM. https://doi.org/10.1145/3303772.3303791

[35] Kizilcec, R. F., & Lee, H. (2022). Algorithmic fairness in education. In W. Holmes & K. Porayska-Pomsta (Eds.), *The ethics of artificial intelligence in education* (pp. 174–202). Routledge. https://doi.org/10.4324/9780429329067-10

[36] Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction instruments. *Big Data*, *5*(2), 153–163. https://doi.org/10.1089/big.2016.0047

[37] Kleinberg, J., Mullainathan, S., & Raghavan, M. (2017). Inherent trade-offs in the fair determination of risk scores. In *8th Innovations in Theoretical Computer Science Conference (ITCS 2017)* (LIPIcs Vol. 67, pp. 43:1–43:23). https://doi.org/10.4230/LIPIcs.ITCS.2017.43

[38] Riazy, S., Simbeck, K., & Schreck, V. (2020). Fairness in Learning Analytics: Student At-risk Prediction in Virtual Learning Environments. In *Proceedings of the 12th International Conference on Computer Supported Education* (pp. 15–25). https://doi.org/10.5220/0009324100150025

[39] National Institute of Standards and Technology. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). https://doi.org/10.6028/NIST.AI.100-1

[40] Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data*, *6*(4), Article 15. https://doi.org/10.1145/2382577.2382579

[41] Moons, K. G. M., Damen, J. A. A., Kaul, T., Hooft, L., Andaur Navarro, C., Dhiman, P., Beam, A. L., Van Calster, B., Celi, L. A., Denaxas, S., Denniston, A. K., Ghassemi, M., Heinze, G., Kengne, A. P., Maier-Hein, L., Liu, X., Logullo, P., McCradden, M. D., Liu, N., … van Smeden, M. (2025). PROBAST+AI: An updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*, *388*, Article e082505. https://doi.org/10.1136/bmj-2024-082505

[42] Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220–229). https://doi.org/10.1145/3287560.3287596

[43] Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM*, *64*(12), 86–92. https://doi.org/10.1145/3458723

[44] Hernán, M. A., & Robins, J. M. (2016). Using big data to emulate a target trial when a randomized trial is not available. *American Journal of Epidemiology*, *183*(8), 758–764. https://doi.org/10.1093/aje/kwv254

[45] Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and dilemmas. *American Behavioral Scientist*, *57*(10), 1510–1529. https://doi.org/10.1177/0002764213479366

[46] Sclater, N. (2016). Developing a code of practice for learning analytics. *Journal of Learning Analytics*, *3*(1), 16–42. https://doi.org/10.18608/jla.2016.31.3

[47] Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744. (2024). *Official Journal of the European Union*, L 2024/1689. Text consulted at https://artificialintelligenceact.eu/article/14/

[48] Hunton Andrews Kurth. (2026, July). *EU Digital Omnibus on AI enters into force*. Privacy and Cybersecurity Law Blog. https://hunton.sitepilot11.firmseek.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force

[49] Quốc hội. (2025). *Luật Trí tuệ nhân tạo, Luật số 134/2025/QH15* [Law on Artificial Intelligence, No. 134/2025/QH15]. https://static3.luatvietnam.vn/uploaded/others/2025/12/25/luat-134-2025-qh15_2512152052.docx

[50] Bộ Tư pháp. (2026, July 2). *Ban hành Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao* [Issuing the list of high-risk AI systems; Decision 33/2026/QĐ-TTg]. https://moj.gov.vn/portal/tin-tuc/chi-tiet/ban-hanh-danh-muc-he-thong-tri-tue-nhan-tao-co-rui-ro-cao-ti1fq907ea.html

[51] Quốc hội. (2025). *Luật Bảo vệ dữ liệu cá nhân, Luật số 91/2025/QH15* [Personal Data Protection Law, No. 91/2025/QH15]. Công báo. https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf

[52] Perdomo, J., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. In *Proceedings of the 37th International Conference on Machine Learning* (PMLR 119, pp. 7599–7609). https://arxiv.org/abs/2002.06673

[53] Gardner, J. P., & Brooks, C. (2018). Evaluating predictive models of student success: Closing the methodological gap. *Journal of Learning Analytics*, *5*(2), 105–125. https://doi.org/10.18608/jla.2018.52.7

===== reports/milestone-4/report/10-00-appendices.md @ 19d35a4 =====
# Appendices

The appendices hold the detail behind the main text: the candidate comparison against the eight criteria (Appendix I),
the metric definitions (Appendix II), the validation and test protocol with sample sizes (Appendix III), the error and
fairness analysis (Appendix IV), the risk register (Appendix V), the decisions on the AI critiques with the reviewers'
prompts (Appendix VI) and the full traceability with Change Log entry C14 (Appendix VII). Counts come from the prepared
views of OULAD-N04-prepared-1.0; outcome counts use the 2013 training runs only.

===== reports/milestone-4/report/10-01-candidate-comparison.md @ 19d35a4 =====
## Appendix I – Candidate Comparison by Criterion

Figure A.1 maps each question to its technical task, its output and the decision it serves, as Section 2.2 sets
them out.

![Figure A.1. From AQ to technical task, output and decision](assets/figures/fig-2-1-aq-map.png){width=85%}

The brief asks that each choice be argued against eight criteria: fit to the question, fit to the data, assumptions,
interpretability, complexity against the baseline, robustness and reproducibility, ethics and fairness, and
actionability [1]. AQ1 is a descriptive question answered by grouped rates with confidence intervals, which need no
model, so the comparison applies to AQ2, AQ3 and AQ4. Facts about the data come from the 9 training runs of 2013, which
cover 6 of the 7 modules: 11,811 enrolments with 5,245 non-completers at day 27 and 12,080 with 5,519 at day 13.

Table A.1 compares the candidates for AQ2, whose purpose is association within module rather than prediction, so its
yardstick is the size and precision of each association, not accuracy on new data [3].

**Table A.1. AQ2 candidates against the eight criteria**

| Criterion | Baseline: unadjusted rate difference per sign | Candidate 1: logistic regression with run fixed effects and sign × module terms (primary) | Candidate 2: mixed-effects logistic regression | Supplement: shallow classification tree |
| :---- | :---- | :---- | :---- | :---- |
| Fit to question | Unadjusted rate difference per sign and module | Pooled within-run risk difference per sign, and module-specific differences from the interaction terms | Same, with module effects drawn from a population of modules (random effects) | Shows which combinations of signs separate outcomes |
| Fit to data | 9 runs, 6 modules | Smallest run 369 enrolments and 91 non-completers; task signs only in runs with a task due by day 27 | 6 modules and 9 runs are few for estimating a variance | Many rows, but the splits change between samples |
| Assumptions | None beyond counting | Additive log-odds within module; all runs of these modules observed, not sampled, so fixed effects suit the design [12] | Normal random effects; inference to unseen modules | None parametric; unstable splits |
| Interpretability | Highest | Risk differences in percentage points, with odds ratios beside them | Similar, plus variance terms | High for a depth of 2–3 |
| Complexity vs baseline | – | One model per cut-off with a few interaction terms | Adds a variance component for little gain within the observed modules | Low, but adds no effect size |
| Robustness and reproducibility | Exact | Deterministic; robust standard errors; sensitivity runs; signs correlated with each other checked | Convergence and few-cluster issues | Unstable across samples |
| Ethics and fairness | No sensitive attribute used | Sensitive attributes not used as signs | Same | Same |
| Actionability | Gives tutors the size of each sign's gap | Tells D2 which signs to look at; shown beside the unadjusted gap, because mutually adjusted estimates are partial effects | No extra action | Gives readable rules for tutors |

Table A.2 compares the candidates for AQ3, a predictive question judged by performance on a later run [5],
[6].

**Table A.2. AQ3 candidates against the eight criteria**

| Criterion | Baseline 1: early-sign rule | Baseline 2: background-only logistic model | Candidate 1: penalised logistic regression (primary) | Candidate 2: gradient-boosted trees | Extension: discrete-time survival model |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Fit to question | Flags a task missed, a TMA late or no activity in the last 7 days; ranks by number of signs | Risk from module, start month, previous attempts, credits, education and registration lead only | Risk of non-completion at each cut-off from all primary predictors | Same, with non-linear effects and interactions | Weekly hazard of withdrawal [8] |
| Fit to data | No fitting | Few parameters | 23 parameters against 5,245–5,519 training non-completers, about 230 per parameter; the 11,811–12,080 training enrolments are about seven times the 1,728–1,731 that the minimum sample size criteria require for this set [14] | Suits tabular data of about 10,000 rows [19] | Fail is decided at the end of the run, not at a time; withdrawal timing serves no decision at fixed cut-offs |
| Assumptions | Signs equally weighted | Additive log-odds | Additive log-odds on transformed predictors | Few; tuning of depth, rate and number of trees | Non-informative censoring (a student is censored when follow-up stops before withdrawal is observed, and the reason it stops is assumed unrelated to the risk of withdrawal); a competing-risk or separate model for Fail |
| Interpretability | Highest | High | Coefficients and per-student contributions from the same model that ranks [11] | Post-hoc explanations, which can mislead [11] | Readable, but per week |
| Complexity vs baseline | – | Small | Small step from the rule | Larger; maintenance and entanglement risks, entanglement being the dependence of a system's parts on each other [10] | Moderate; same software as logistic regression [8] |
| Robustness and reproducibility | Exact | Stable | Stable; penalty tuned in grouped folds | More tuning choices; selection bias risk [31] | Stable |
| Ethics and fairness | Equal weights do not give equal error rates; audited like the models | Audit | Audit; proxy check | Same audit; harder to explain a disparity | Same audit |
| Actionability | Directly explainable | Shows what background alone gives | Score plus each student's own largest contributions | Score; reasons only through approximations | Adds timing, which D1 does not use at fixed cut-offs |

The choice of logistic regression rests first on this project's constraints. Tutors must see why a student is listed,
and a transparent model gives each student's reasons from the same equation that ranks them [11]; the 23 parameters
leave about 230 events each, so the training data are large enough for a stable logistic model [14]; and the risk to be
tested is transfer to a later run, which favours a simple, stable model [6]. The literature supports this choice:
a systematic review of 71 clinical prediction comparisons found, as its authors report, no difference in discrimination between logistic regression and machine learning among comparisons at low risk of bias [18].
Gradient-boosted trees stay as the challenger, since a benchmark that removed datasets where logistic regression came within 5% of the best models cannot show that trees beat it [19]; they replace logistic regression only if they beat it by the margin fixed in Appendix III (Table A.5, step 4). Compared with the primary model, the background-only model, which uses no activity, shows how much of the ranking comes from engagement
rather than from module and history. The survival model fits withdrawal timing, whereas the target joins Fail and Withdrawn at the
end of the run, so it stays a later extension.

Table A.3 compares the candidates for AQ4, where the output is a list of fixed length per run.

**Table A.3. AQ4 candidates against the eight criteria**

| Criterion | Baseline 1: random list | Baseline 2: rule-ranked list | Candidate 1: top-k by AQ3 score (primary) | Candidate 2: risk tiers | Rejected: benefit (uplift) ranking |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Fit to question | Chance level | List from the number of signs, ties broken by lower relative activity | The k enrolments with the highest risk per run, k from capacity | First tier the top 3 per 20, second tier the next 2 per 20, both fixed from capacity | Ranks by expected benefit of contact |
| Fit to data | – | Rule known at each cut-off | k = 3 or 5 per 20 enrolled | Same scores | No contact or treatment variable in the data [9] |
| Assumptions | – | Signs equally weighted | Risk order matches need: untested | Same | Randomised or unconfounded treatment [9] |
| Interpretability | – | High | Score and reasons | High | Low |
| Complexity vs baseline | – | – | Uses AQ3 scores only | Same | Needs an experiment first |
| Robustness | – | Exact | As AQ3 | As AQ3 | – |
| Ethics and fairness | Audit | Audit | Confirmatory audit of recall at capacity by group (Appendix IV) | Same | – |
| Actionability | – | Direct | Tutor decides on the list; ranks and reasons, probabilities only if calibrated | Adds a second tier for lighter contact | Not available |

Ranking by risk is not ranking by benefit: in field experiments on customer retention, the customers at highest risk were not the best targets of an intervention [20]. The list therefore supports the tutor's decision, and choosing whom to contact by
expected benefit needs a randomised study first (Section 5.2).

===== reports/milestone-4/report/10-02-metric-definitions.md @ 19d35a4 =====
## Appendix II – Metric Definitions

The Evaluation Design Cards of Section 4.1 use the metrics that Table A.4 defines, for a run r with n enrolments, the set Y of its non-completers, base rate b = |Y|/n, and a list L of the k highest scores; Section 4.1 explains the main ones in words.

**Table A.4. Metric definitions**

| Metric | Definition | Reading |
| :---- | :---- | :---- |
| Recall at capacity | \|L ∩ Y\| / \|Y\| | Share of the run's non-completers on the list |
| Attainable recall | min(k, \|Y\|) / \|Y\| | The most a list of length k can reach |
| Normalised recall | recall / attainable recall | 1 = best attainable; equals precision when \|Y\| ≥ k |
| Pooled normalised recall | Σ\|L ∩ Y\| / Σ min(k, \|Y\|) over runs | Each run keeps its own list and k |
| Precision at capacity | \|L ∩ Y\| / k | Share of the list who do not complete |
| Lift | precision / b | 1 = chance; a random list has expected recall k/n |
| ROC-AUC (within run) | Probability that a non-completer scores above a completer of the same run | Discrimination without run differences |
| PR-AUC (within run) | Area under a run's precision–recall curve | Read against its chance level b [24] |
| Calibration-in-the-large | Intercept of a logistic model of the outcome with the score's log-odds as offset | Target 0 [33] |
| Calibration slope | Coefficient of the score's log-odds in a logistic recalibration | Target 1; below 1 means risks too extreme [33] |
| Brier score | Mean squared difference between predicted risk and outcome | Overall accuracy of probabilities |
| Net benefit | true positives/n − false positives/n × pt/(1 − pt) at threshold probability pt | Context: contact-all, contact-none and the rule [25] |
| ABROCA | Absolute area between the ROC curves of a group and the rest | Threshold-free differential discrimination [34] |

===== reports/milestone-4/report/10-03-validation-protocol.md @ 19d35a4 =====
## Appendix III – Validation and Test Protocol

Figure A.2 draws the validation and test protocol of Section 4.2, from the first freeze to the single test on the
2014 runs.

![Figure A.2. Validation and test protocol from the first freeze to the single test on the 2014 runs](assets/figures/fig-4-1-validation.png){width=100%}

The protocol separates development from evaluation so that no information from the evaluation runs reaches any choice
about the model, which is how leakage is avoided by design [40], [22]. It follows the two-step freeze proposed for
predictive modeling: the question, splits, metrics and baselines are fixed before training, and the final model is
fixed and test access recorded before testing [26]. Table A.5 lists the steps in order.

**Table A.5. Validation and test protocol**

| Step | Data | What happens | Why |
| :---- | :---- | :---- | :---- |
| 1. First freeze | – | This proposal fixes AQs, populations, predictor sets, the early-sign rule (Change Log entry C10), splits, metrics, baselines and success criteria | Choices cannot follow the results [26] |
| 2. Development folds | 9 runs of 2013 (6 modules) | Leave-one-run-out: each run is the validation fold once; rows of students who also appear in the validation run (121–129 students, 242–258 rows) are removed from that fold's training data, in outer loops (the cross-validation used to evaluate and choose the model) and inner loops (the cross-validation run inside each training fold to tune hyperparameters, step 3) alike | Validation folds must hold only groups absent from training [29]; random folds underestimate error on structured data [28] |
| 3. Fitting inside folds | Training fold only | Imputation, scaling and encoding refitted in each fold; penalty of the logistic regression and depth, learning rate and number of trees of the boosted trees tuned by nested cross-validation, an inner leave-one-run-out loop run on the training runs of each fold; optional logistic recalibration fitted inside development | Preprocessing learnt on training data only [29]; tuning inside each loop keeps the estimate nearly unbiased [30], [31] |
| 4. Model choice | Outer-fold results | Four configurations, penalised logistic regression and gradient-boosted trees each with the primary and with the extended predictor set, compared on pooled normalised recall at day 27, k = 5 per 20, the S1 metric: boosted trees replace logistic regression, and the extended predictor set the primary set, only with a gain of at least 0.03, about 89 more non-completers listed over the 9 runs, and a gain in at least 7 of 9 folds. Fold results serve the choice only and are never reported as expected performance | Ties go to the simpler model [5]; differences within sampling variation have little practical meaning [31], [53] |
| 5. Second freeze | All 2013 runs | The chosen model refitted on all 9 runs; specification, parameters and file hash recorded with the time of the first test access | Final model fixed before testing [26] |
| 6. Single test | 13 runs of 2014 | Scores, lists and all metrics of Appendix II computed once; S1 judged on all 13 runs and all eligible enrolments | Data sharing no run with development [21]; a later run is a temporal validation [27] |
| 7. Sensitivity | 13 runs of 2014 | Paired runs (9, module and start month also run in 2013) and unpaired runs (4); module CCC apart; without test enrolments of students seen in 2013; without the Withdrawn enrolments that lack a withdrawal day; labels-available variant; day 13 and k = 3 per 20. None can change the S1 verdict | Later-run estimates are the honest ones [23]; one declared primary comparison prevents choosing a favourable variant |
| 8. AQ2 replication | 13 runs of 2014 | AQ2 associations re-estimated, CCC included | Opens the test outcomes only after step 6; changes nothing in AQ3 |

Two features of the run structure need explicit rules. Module CCC has no run in 2013, and modules AAA, EEE and GGG have
one 2013 run each, so a fold or a test run can hold a module the training data lack; module terms are therefore coded
as deviations from the average module, and an unseen module receives the average, in development folds and test alike.
In addition, presentations coded B start in February and those coded J in October [2], and the 2013 J runs last 261
to 268 days, so they had not ended when the 2014 B runs reached their cut-offs. The main test follows the year split of
Milestone 3; the labels-available variant scores the 2014 B runs with a model trained only on the 2013 B runs, the only
runs whose outcomes a university would hold at that time.

Uncertainty for S1 comes from a paired two-level bootstrap: runs are resampled, then enrolments within each sampled
run, each run's list is re-formed as the top 25% of its resampled enrolments, and the model–rule difference is computed
on the same resample, because treating nested observations as independent inflates false positives [32]. With only
13 test runs of 348 to 2,021 enrolments, such intervals can be too narrow, so S1 also requires a one-sided sign-flip
permutation test on the 13 per-run differences, and wins, ties and losses are reported with the unweighted mean of the
per-run differences.

Table A.6 gives the sample sizes behind these choices, computed from the prepared views without fitting a model;
outcome counts come from the 2013 runs only, so the 2014 outcomes stay unseen until step 6.

**Table A.6. Sample sizes for development and evaluation**

| Quantity | Day 13 | Day 27 |
| :---- | :---- | :---- |
| Training enrolments (2013, 9 runs, 6 modules) | 12,080 | 11,811 |
| Training non-completers | 5,519 (45.7%) | 5,245 (44.4%) |
| Smallest training run: enrolments / non-completers | 370 / 92 | 369 / 91 |
| Most non-completers a list of 5 per 20 can hold, 9 training runs | 3,032 | 2,976 |
| Parameters, primary set (19 predictors, module and start-month terms) | 23 | 23 |
| Parameters, primary and extended sets with weekly clicks | 35 | 37 |
| Events per parameter, primary set / with extended set and weekly clicks | 240 / 158 | 228 / 142 |
| Minimum development size (Riley criteria), primary set / with extended set and weekly clicks | 1,728 / 2,629 | 1,731 / 2,784 |
| Test enrolments (2014, 13 runs, 7 modules) | 15,989 | 15,724 |
| Test enrolments in the 9 paired / 4 unpaired runs | 10,902 / 5,087 | 10,801 / 4,923 |
| Test enrolments of students seen in 2013 | 1,637 | 1,586 |
| Test enrolments Withdrawn without a withdrawal day | 89 | 90 |
| Test run size, smallest / largest | 350 / 2,079 | 348 / 2,021 |

The minimum development size follows the three criteria of Riley et al.: expected shrinkage of at least 0.9, optimism
in Nagelkerke R² of at most 0.05 and the overall risk estimated within 0.05 [14], under their default of an
anticipated Nagelkerke R² of 0.15 when no prior estimate exists [14]. The training runs hold about seven times the
required size for the primary set, so the number of enrolments does not limit the choice of model. Transfer to a new
run is a different matter: it rests on only 9 training runs, which is why it is tested by the run-level split rather
than inferred from the sample size, and why per-module models remain unattractive, since each module's data are small
and shrinkage does not rescue small samples [17].

===== reports/milestone-4/report/10-04-fairness-spec.md @ 19d35a4 =====
## Appendix IV – Error and Fairness Analysis Specification

Aggregate metrics can hide differences between groups, so the frozen model is evaluated separately for each audit
group of the test runs, an approach known as slicing analysis [34]. Gender, disability, deprivation band and age band
stay out of the predictors and serve only the audit, because leaving them out does not make a model blind to them:
activity, previous attempts or credits can carry the same information [35]. Table A.7 gives each group's size in the
prepared views and how it is handled; outcome counts are for the 2013 training runs, test sizes are enrolments only,
and eligibility for the confirmatory check is fixed in this proposal from enrolment counts, before any test outcome is opened.

**Table A.7. Audit groups at day 27**

| Group | Training enrolments / non-completers | Test enrolments | Fewest enrolments of the group in one test run | Handling |
| :---- | :---- | :---- | :---- | :---- |
| Female / male | 5,697 / 2,488 and 6,114 / 2,757 | 6,666 and 9,058 | 66 and 139 | Descriptive, per run and pooled |
| Declared disability | 1,123 / 602 | 1,488 | 18 | Confirmatory, pooled over runs |
| Deprivation band 0–10% | 1,163 / 699 | 1,486 | 17 | Confirmatory, pooled over runs |
| Deprivation band missing | 418 / 118 | 610 | 1 | Confirmatory, pooled; its own group, never merged with a band |
| Age 55 or over | 75 / 18 | 118 | 1 | Below the eligibility size: point gap only, "insufficient data, not cleared" |

Fairness criteria cannot all hold at once when non-completion rates differ between groups: a score with equal
positive predictive value across groups cannot also have equal error rates [36], and calibration within groups and
balanced error rates conflict except in degenerate cases [37]. The audit therefore names one primary criterion:
separation, measured as equal recall at capacity across groups, which suits a supportive contact where missing a
struggling student is the main harm [35]. Table A.8 lists the checks; only the first row is confirmatory, and every
other row is descriptive.

**Table A.8. Fairness and error checks**

| Check | Measure | Rule |
| :---- | :---- | :---- |
| Confirmatory fairness (separation) | Recall at capacity of each eligible group (at least 400 test enrolments) minus the rest, day 27, k = 5 per 20, pooled within run | A group is flagged for review when its recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups, lies entirely below 0; groups below 400 test enrolments are reviewed on the point gap alone and reported as not cleared |
| Selection | Share of each group on the list against its share of non-completers | Descriptive |
| Precision by group | Precision at capacity per group | Descriptive; differences expected when base rates differ [36] |
| Calibration by group | Calibration-in-the-large and slope; a curve only with about 200 events and 200 non-events [33] | Descriptive, with intervals |
| Threshold-free gap | ABROCA within run, pooled, with the sign of the difference in discrimination and a reference from group labels shuffled within run, the ABROCA that chance alone can produce [34] | Descriptive; never triggers review on its own |
| Proxy check | Score distribution and predictor means by group | Descriptive; shows which predictors carry group information |
| Errors by run and module | Missed non-completers and listed completers per run; module CCC reported separately | Runs below the rule are examined |
| Errors by activity and history | No, low and normal activity; previous attempts; late registration | Shows whether the model adds value beyond inactivity |
| Errors by outcome kind and reach | Fail and Withdrawn among missed and listed non-completers; withdrawal within 7 days after the cut-off | Shows which non-completion the list misses and whom it cannot reach |
| List stability | Share of bootstrap resamples in which a student near rank k stays on the list | Shows how arbitrary the cut at k is |

Earlier work on OULAD found a gap in favour of male students that most at-risk models reproduced and slightly
amplified, and erratic bias for the under-represented students with a declared disability, which is why the small
groups are pooled over runs and reported with intervals [38].

===== reports/milestone-4/report/10-05-risk-register.md @ 19d35a4 =====
## Appendix V – Risk Register

The register follows the four functions of the NIST AI Risk Management Framework, which organises risk work as
govern, map, measure and manage [39]. Each row names where a risk arises in this project, the control that the
proposal builds in, the check that shows whether the control works, and the risk that remains. Table A.9 lists the
sixteen risks.

**Table A.9. Risk register**

| # | Risk | Where it arises | Control | Check | Residual |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R1 | Target leakage | A predictor that carries information from after the cut-off | Predictors dated on or before the cut-off; target-derived flags outside the predictor list (Milestone 3) | Predictor legitimacy at the time of use [41]; validation of the prepared views | Low |
| R2 | Train–test contamination | Preprocessing or tuning that sees validation or test rows | Refit inside each fold; one test scoring after the second freeze | Logged test access [26]; pipeline review [22] | Low |
| R3 | Selection bias in model choice | The chosen configuration's fold score is optimistic | Nested tuning; choice by a margin fixed in advance; fold results never reported as performance | Fold-level results kept for the record [30] | Low to medium |
| R4 | Shift between years and to the university | 2014 runs differ from 2013; UK distance learning differs from a Vietnamese program | Temporal test; paired and unpaired runs apart; local validation before any use | Per-run metrics; a failed calibration check leads to ranks only, and recalibration only on a run after the 2014 test runs [33] | Medium |
| R5 | Unseen module | Module CCC appears only in 2014 | Module terms as deviations; unseen module scored with the average | CCC runs reported apart | Medium for CCC |
| R6 | Few-cluster inference | 13 test runs of unequal size | Paired two-level bootstrap with a sign-flip test; per-run results | Wins, ties and losses reported | Medium |
| R7 | Selective reporting | Many test variants | One primary comparison declared; variants cannot change the verdict | First and second freeze records [26] | Low |
| R8 | Run list versus tutor capacity | One run-wide list stands in for tutors' lists | Capacity expressed as a share of the run; limitation stated | Tutor-level check in the pilot | Medium |
| R9 | Misreading coefficients as causes | AQ2 estimates and AQ3 reasons read as effects | Association wording rule with a text review; unadjusted and adjusted estimates side by side | Review of all result wording against the brief | Low |
| R10 | Claiming that contact works | The list read as proof that contacting helps | No effect claim; randomised pilot proposed [44] | Wording review of tutor materials before the pilot | Medium until a pilot |
| R11 | Unequal errors across groups | Lower recall for disabled, deprived or older students | Separation as primary criterion; confirmatory check (Appendix IV) | Shortfall rule of Table A.8 | Medium for small groups |
| R12 | Proxies for excluded attributes | Activity, history or credits carry group information | Proxy check by group | Score and predictor means by group | Medium |
| R13 | Automation bias | Tutors follow the list without judgement | Tutor decides; can override any entry; reasons shown [47] | Scripted tutor walk-through before the pilot; overrides recorded | Medium |
| R14 | Labelling and stereotyping | A flag that follows a student | Flags lead to support and expire with the run [45] | Review of list use [46] | Medium |
| R15 | Feedback after deployment | Contacts change the outcomes the next model learns from | Contacts logged with outcomes before any retraining [52] | Monitoring of later cohorts [39] | Medium |
| R16 | Legal status and privacy at the university | Ranking learners is listed as high-risk in Vietnam [50]; university records are personal data [51] | Pilot only after risk classification and the duties of the AI law [49]; OULAD never linked to other data | Conformity assessment, the procedure that assesses a high-risk AI system before it is put into use [49]; data protection review | Depends on the university |

===== reports/milestone-4/report/10-06-ai-critiques.md @ 19d35a4 =====
## Appendix VI – Decisions on the AI Critiques and Prompts

The AI Decision Log of Section 6 (Table 6.1) records the significant AI contributions; this appendix gives
our decision on each critique of the two reviewers. Table A.10 covers the 12 critiques of the model-selection critic
and Table A.11 the 12 critiques of the evaluation reviewer, each with the evidence used to check it and its effect on
the proposal.

**Table A.10. Decisions on the model-selection critic's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | Pooled metrics can reward separating high-rate from low-rate runs | Accepted | Lists and normalised recall per run; ROC-AUC and PR-AUC within run; background-only baseline |
| 2 | Folds unspecified; unseen module; 2013 October labels not available for February 2014 | Accepted | Leave-one-run-out folds stated; module terms as deviations, CCC apart; labels-available variant for 2014 B runs |
| 3 | One test set judges many comparisons | Accepted | One primary comparison (S1); all variants are sensitivity analyses |
| 4 | AQ2 gives pooled, not per-module, associations; counts were not those of the 9 training runs | Accepted | Sign × module terms; fit stated for 9 runs and 6 modules; task signs only where a task is due |
| 5 | Reasons from AQ2 would contradict the AQ3 score; adjusted estimates are partial effects | Accepted | Reasons from the scoring model; unadjusted and adjusted estimates side by side; correlation check |
| 6 | Choice leans on literature; no switching rule | Accepted in part | Switching rule in Table A.5, step 4; rationale led by the project's constraints (Section 3.3) |
| 7 | Survival candidate rejected on a misstated assumption | Accepted | Fail is not a time-to-event outcome; non-informative censoring (follow-up stopping for reasons unrelated to the risk of withdrawal) stated as an assumption |
| 8 | Sample size says nothing about transfer; source of the anticipated R² | Accepted | Transfer tested by the run split; Riley default cited; minimums per cut-off |
| 9 | Ranks or probabilities for tutors not decided | Accepted | Ranks and reasons; probabilities only if S3 holds; tiers fixed from capacity |
| 10 | Fairness audit underpowered; dropping attributes is not enough | Accepted | Pooled confirmatory groups; proxy check; separation named |
| 11 | Risk order assumed to match need; recall has a ceiling | Accepted | Assumption stated as untested; normalised recall; Fail and Withdrawn split |
| 12 | Unknown withdrawal days and repeat students may leak | Accepted in part | Sensitivity analyses of Table A.5, step 7; previous attempts are recorded at registration and stay legitimate |

Table A.11 records the decision on each of the evaluation reviewer's 12 critiques.

**Table A.11. Decisions on the evaluation reviewer's critiques**

| # | Critique (short) | Decision | Where it is addressed |
| :---- | :---- | :---- | :---- |
| 1 | 2013 runs hold 6 modules, not 7 | Accepted | AQ2 rule as a share of modules; unseen-module rule; CCC apart |
| 2 | Run lists stand in for tutor capacity; metrics re-express one count | Accepted | Limitation and risk R8; normalised recall defined; net benefit as context |
| 3 | S1 inference under-specified with 13 runs | Accepted | Paired two-level bootstrap with re-formed lists; sign-flip test; wins, ties and losses |
| 4 | S2 ambiguous and unanchored | Accepted | S2 reported, not a gate |
| 5 | No primary test population | Accepted | S1 on all 13 runs, all eligible enrolments, day 27, k = 5 per 20 |
| 6 | Calibration intercept ill-defined; failure path reuses the test | Accepted | Calibration-in-the-large defined as the intercept with the score's log-odds as offset (coefficient fixed at 1); bounds on the estimates pooled over all runs; recalibration only in development or on a run after the 2014 test runs |
| 7 | Model choice on another aggregation; overlap removal in inner folds | Accepted | Same metric as S1; margin of about 89 students; removal in all loops, outer and inner |
| 8 | Fairness gate blind for small groups; two-sided and one-sided rules | Accepted | Eligibility from enrolments; one-sided; Holm adjustment; "not cleared" for small groups |
| 9 | ABROCA without reference | Accepted | Within run, permutation reference, sign reported, descriptive only |
| 10 | Odds ratios overstate effects at this base rate; the threshold is too easy; AQ2 and AQ3 are coupled | Accepted | Risk difference with a 5-point smallest effect; rule frozen; 2014 AQ2 cannot change AQ3 |
| 11 | Error-analysis gaps | Accepted | Reachable non-completers, active students, list stability, history slices, CCC |
| 12 | Missing risks and mismatched controls | Accepted | Sixteen risks in Table A.9; controls of misreading coefficients as causes (R9), claiming that contact works (R10) and automation bias (R13) matched to their risks |

Each reviewer was a separate generative AI session that could read only the brief and the appendices named in its prompt, and we checked every critique against the design facts before deciding. The prompts are given in English in abridged form, with documents named by their place in this report. The model-selection critic received this instruction:

> You act as the "Model selection" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the AQ Modeling Briefs (Section 2.1), the candidate comparison (Appendix I) and the
> sample sizes and counts from the prepared data (Appendix III). Do not search the web, do not open any data file, do
> not invent benchmark results, metric thresholds or performance numbers, and do not choose the model for the team.
> Challenge the model selection as a sceptical senior analyst would: (1) mismatch between each AQ's question, output
> and the chosen method; (2) whether each modeling AQ has a sensible baseline and 2–3 real candidate families, or a
> straw-man baseline; (3) whether the rationale is tied to the data facts and constraints, or rests on algorithm
> reputation; (4) assumptions the team has not checked; (5) causal overclaim or confusion between association,
> prediction and benefit; (6) leakage or test-set exposure risks created by the modeling plan; (7) anything that makes
> the choice hard to act on for tutors (decision D1) or unfair to groups. Write at most 12 numbered critiques, most
> important first, each with the passage, the problem, why it matters and a concrete recommendation.

The evaluation reviewer received this instruction:

> You act as the "Evaluation design" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the Evaluation Design Cards and metric definitions (Appendix II), the validation
> and test protocol (Appendix III), the error and fairness analysis (Appendix IV), the risk register (Appendix V) and the
> counts from the prepared data. Do not search the web, do not open any data file, do not invent results, benchmarks or
> performance numbers. Review the evaluation design as a sceptical methodologist: (1) whether each metric reflects the
> decision it serves and whether any metric is misleading for this base rate; (2) whether the success criteria are
> fixed in advance, falsifiable, internally consistent, and neither trivially easy nor impossible; (3) validation:
> leakage paths, test reuse, grouping of students across runs and years, nested tuning, the AQ2/AQ3 interaction; (4)
> uncertainty estimation with 9 training and 13 test runs; (5) calibration criteria and what happens when they fail;
> (6) fairness: choice of criterion, small groups, multiple comparisons, interpretation of ABROCA; (7) error analysis
> gaps; (8) risks missing from the register or controls that do not match their risk. Write at most 12 numbered
> critiques, most important first, each with the passage, the problem, why it matters and a concrete recommendation.

===== reports/milestone-4/report/10-07-traceability-full.md @ 19d35a4 =====
## Appendix VII – Full Traceability and Change Log

Table A.12 extends the traceability of Milestone 3 to the modeling and evaluation choices: each row runs from the
Business Goal and its KPI through the question, its analytics level and technical task to the prepared data, the
baseline and primary approach, the primary metric, the validation and the decision supported. The Business Goal is to
improve successful course completion by identifying students who stop taking part early enough to support them within
the semester; the primary KPI is the completion rate of students enrolled after the add-drop period.

**Table A.12. Full traceability from goal to decision**

| AQ | KPI | Level | Technical task | Prepared data | Baseline | Primary approach | Primary metric | Validation | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Descriptive | Aggregation and rate comparison | enrolment and assessed-task views (enrolment, assessment_due); population enrolled at day 14 | Pooled rate; second denominator | Grouped rates with 95% intervals; first missed week by outcome | Non-completion rate with interval | Two aggregation paths agree; known totals | D2, D3 |
| AQ2 | Primary KPI; secondary KPI 1 | Diagnostic | Association within module run | features_d27, enrolment; 2013 runs, then 2014 | Unadjusted rate difference per sign | Logistic regression with run fixed effects and sign × module terms | Risk difference with interval (odds ratio beside it) | Sensitivity runs; 2014 replication after the AQ3 test | D2; reasons on D1 |
| AQ3 | Secondary KPI 1 | Predictive | Binary classification at day 13 and day 27 | the two feature views (features_d13, features_d27) and the model-ready matrix (model_ready); 19 primary predictors | Rule-ranked list; background-only model; random list | Penalised logistic regression; boosted trees only by the pre-set margin | Normalised recall at capacity (day 27, 5 per 20) | Leave-one-run-out in 2013; single test on 2014 | D1 |
| AQ4 | Secondary KPIs 1 and 2 | Prescriptive (ranking) | Ranking under capacity | AQ3 scores; list lengths by capacity for each run (capacity_by_run) | Random list; rule-ranked list | Top-k per run from AQ3 scores with reasons | Normalised recall at capacity | As AQ3; audit by deprivation band and disability | D1; contact deferred |

Table A.13 records the one change to how a question is measured that the evaluation design introduces; it continues
the Controlled Change Log C01–C13 of Milestones 2 and 3.

**Table A.13. Controlled Change Log entry C14**

| ID | Milestone | Before | After | Reason | Effect |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C14 | 4 | AQ2 associations estimated on all 22 runs | AQ2 estimated on the 9 runs of 2013; replicated on the 13 runs of 2014 only after the AQ3 model is frozen and scored | Looking at 2014 outcomes while choosing AQ3 predictors would leak test information into the model [40] | AQ2 results on 2014 are a replication; AQ3's test stays independent |
