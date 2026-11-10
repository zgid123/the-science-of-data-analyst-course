# Final Project Traceability Matrix

This document reproduces the Final Project Traceability Matrix of the final report: Section 11.1 (Tables 11.1 and
11.2) and its full-length version in Appendix XI (Tables A.27 and A.28). Section and appendix numbers below refer to
the final report; Change Log entries (C01–C17) are in `data/metadata/change_log.md`, and result files are in
`results/`.

The matrix follows each final question in one row from the goal to the data and on from the preparation to the
decision, with GAP or N.A. where a link has no evidence. All four rows share one Business Goal: improve successful
course completion in the program's online and blended courses by identifying students who stop taking part early
enough to support them within the semester. They also share one SMART Goal: raise the completion rate of students
enrolled after the add-drop period in the pilot courses from the recounted baseline (assumed 70%) by five percentage
points (assumed 75%) by the end of 2027–2028. The decisions supported are D1 (whom to list first at the week-3 and
week-5 review points), D2 (where to place support time across courses and groups) and D3 (whether to extend the
approach).

**Scope of the results.** The AQ1 and AQ2 results cover the 9 module runs of 2013 only. AQ1 is computed on the 9 runs
of 2013 (13,529 enrolments; 12,076 registered at day 14); the year comparison uses the 2014 outcome counts per run that
Milestone 3 published (C15). AQ2 is estimated on the 9 runs of 2013 and replicated on the 13 runs of 2014 only after
the AQ3 model is frozen and scored (C14). The 2014 runs stay unopened for the single AQ3 test. For AQ1 and AQ2 every
link holds evidence and both meet their criteria; for AQ3 and AQ4 the chain ends at the evaluation design, because the
prototype has not been run (Section 10).

The status of each row follows one rule. A question is Answered when real results answer all of it on its stated
population; Partial when real results answer its core while a named part waits for data or for a later step; Deferred
when no result exists yet but the design is complete and the answer waits for a named step; and Dropped when the
question is abandoned. No question is Dropped, because every change since Milestone 1 narrowed how a question is
measured or deferred a part of it, as the AQ Revision Log records (Section 3.2).

## Table 1. Final Project Traceability Matrix with detailed cells

Table 1 gives the matrix with each cell written out, one row per final question, in the eleven columns of the course
brief (Table A.27 of the final report).

| AQ-ID | Business / SMART Goal + KPI | Final Analytical Question (short) | Analytics Level | Required Data / Unit | Actual Dataset & Variables | Preparation / Feature Logic | Candidate Method / Model + Rationale | Evaluation / Result | Decision Supported | Final Status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Completion +5 points; primary KPI (proxy on OULAD: completion of enrolments still registered at day 14) | Outcome shares by module, run, start month and year; week in which non-completers first miss an assessed task | Descriptive | Enrolment in one course and semester; dated final result and tasks | OULAD 2013: 9 runs, 13,529 enrolments, 12,076 at day 14; 2014 by the outcome counts Milestone 3 published; GAP: delivery mode, year of study | Day-14 rule; non-completion = Fail or Withdrawn; first missed task over TMA and CMA | Grouped rates with 95% intervals under two denominators; no model, since the question is descriptive | Two aggregation paths agree (72 of 72 cells); non-completion 45.7% (44.8–46.6) of 12,076 | D2, D3 | Partial |
| AQ2 | Primary KPI; secondary KPI 1 (early-sign rule built from these signs) | Signs by the end of week 4 that go with later non-completion, within module | Diagnostic (association only) | Enrolment with its signs in weeks 1–4 | Day-27 features, 2013: 11,811 enrolments; task signs in 7 runs (9,960); GAP: attendance; several-modules sign almost only in 2014 | Every sign dated on or before day 27; lateness for TMA only; task signs only where a task falls due | Logistic regression with run fixed effects and sign × module terms; within-module association | All 5 signs consistent (≥ 5 points, interval excluding 0); missed task 40.8 points (37.7–43.9) | D2; reasons on the D1 list | Partial |
| AQ3 | Secondary KPI 1 (the rule the model must beat); primary KPI through D1 | Non-completion estimated at the end of weeks 2 and 4 against the early-sign rule, 2013 → 2014 | Predictive | Enrolment at each cut-off; runs in time order | Feature views at days 13 and 27, 19 usable predictors; development 9 runs of 2013, test all 13 runs of 2014 (unopened) | Only events dated by the cut-off; every learned step refitted inside each fold | Penalised logistic regression against the rule, a background-only model and a random list; staff need each student's reasons | Gate S1 planned; N.A.: no model trained | D1 | Deferred |
| AQ4 | Secondary KPI 1 (contact part) and KPI 2; GAP on OULAD: measured only in the pilot | Top of a list of assumed capacity: gain over a random list and recall, by deprivation band and disability | Prescriptive (ranking) | Enrolment at each review point; capacity; contact record | AQ3 scores (not yet produced), capacity per run; GAP: no contacts or outcomes after contact | List of 3 or 5 per 20 students per run; sensitive fields for the audit only | Top-k per run with the signs behind each name; no ranking by benefit without contact data; a decision option, untested | S1 and fairness rule FR1 planned; N.A. | D1; contact choice deferred | Deferred |

Reading the rows across shows where the chain is complete and where it is broken. For AQ1 and AQ2 every link holds
evidence, from the KPI to a measured result, and both questions meet the success criteria Milestone 4 fixed for them
(Sections 11.2 and 11.3). For AQ3 and AQ4 the chain is complete up to the evaluation design, while the result cell
stays N.A. because the predictive prototype has not been run (Section 10). The GAP cells mark data that OULAD does not
hold: delivery mode and year of study for AQ1 and AQ2, attendance for AQ2, and contacts, contact types and outcomes
after contact for AQ4. In addition, secondary KPI 2 and the contact part of secondary KPI 1 need a contact record that
only the pilot can create, so their link to AQ4 is a GAP on OULAD rather than a measured value.

## Table 2. Final status of each question and its justification

Table 2 justifies the final status of each question in one sentence (Table A.28 of the final report).

| AQ | Final Status | Justification |
| :---- | :---- | :---- |
| AQ1 | Partial | AQ1 is answered for the 9 runs of 2013 with its success criterion met and with a year comparison from the 2014 outcome counts that Milestone 3 published, while the 2014 rates on the day-14 population and the 2014 first missed week, including those of module CCC, wait until the AQ3 test has opened the 2014 outcomes (C15, AQ1 computed on 2013). |
| AQ2 | Partial | All five signs meet the consistent-association criterion on the 2013 runs, while the planned replication on the 13 runs of 2014 (including module CCC) and the several-modules sign, which exists almost only in 2014, wait until after the AQ3 test (C14, replication after the AQ3 test; C12, several-modules sign described for 2014 only). |
| AQ3 | Deferred | The Level 1 design (baselines, primary model, single gate S1, frozen protocol) is complete, but no model has been trained and the 2014 test runs stay unopened, so no predictive result exists; the run is deferred by our choice of scope, because Level 2 is optional and the single-use 2014 test is kept for one complete run of the frozen protocol (Section 10). |
| AQ4 | Deferred | The ranking needs the frozen AQ3 scores, which do not yet exist, and its contact part has no data in OULAD and is deferred to the pilot (C11, contact choice deferred). |

## Table 3. Compact matrix

Table 3 gives the same chain in the short cells of the report's main text (Tables 11.1 and 11.2 of the final report,
joined into one row per question).

| AQ-ID | Goal + KPI | Final AQ | Analytics level | Required data / unit | Actual dataset & variables | Preparation / features | Method + rationale | Evaluation / result | Decision | Final status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Outcome shares; first missed week | Descriptive | Dated result, tasks | 2013, day 14: 12,076; GAP: mode, year | Day-14 rule; TMA, CMA | Grouped rates; no model needed | Paths agree; 45.7% | D2, D3 | Partial |
| AQ2 | Primary KPI; KPI 1 | Signs by week 4, within module | Diagnostic | Signs, weeks 1–4 | 2013, day 27: 11,811; GAP: attendance | Dated by day 27 | Logistic, run effects | 5 of 5 signs consistent | D2; D1 | Partial |
| AQ3 | KPI 1 (rule to beat) | Weeks 2 and 4 against the rule | Predictive | Enrolment at cut-off | 19 predictors; 2014 closed | Refit per fold | Penalised logistic; reasons | S1 planned; N.A. | D1 | Deferred |
| AQ4 | KPIs 1–2: GAP | Ranked list by group | Prescriptive | Capacity; contacts | GAP: contacts | 3 or 5 per 20 | Top-k with signs | S1, FR1; N.A. | D1 | Deferred |

## Evidence in this package

| Number in the matrix | Result file (`results/`) |
| :---- | :---- |
| AQ1 populations: 13,529 enrolments, 12,076 registered at day 14 | `aq_results.json` (`aq1.all_enrolments`, `aq1.day14_registered`), `aq1_rates.csv` |
| AQ1 validation: two aggregation paths agree in 72 of 72 outcome cells | `aq_results.json` (`aq1.validation`), `aq1_validation_two_paths.csv` |
| AQ1 non-completion 45.7% (44.8–46.6) of 12,076 | `aq1_rates.csv` |
| AQ2 population 11,811 at day 27; 9,960 in the 7 runs with a task due by day 27 | `aq_results.json` (`aq2.population`), `aq1_runs_task_due.csv`, `aq2_associations.csv` |
| AQ2 verdicts of the five signs; missed task 40.8 points (37.7–43.9) | `aq2_associations.csv` |
| AQ3 and AQ4 designs, gate S1, fairness rule FR1 | Milestone 4 report (evaluation design) and Section 9 of the final report; no result file, since no model has been trained |
