# Final Project Traceability Matrix

This document reproduces the Final Project Traceability Matrix of the final report: Section 11.1 (Tables 11.1 and
11.2) and its full-length version in Appendix XI (Tables A.27 and A.28). Section and appendix numbers below refer to
the final report; Change Log entries (C01–C17) are in `data/metadata/change_log.md`, and result files are in
`results/` (`2013/`, `2014/`, `all_runs/` and `compare/`).

The matrix follows each final question in one row from the goal to the data and on from the preparation to the
decision, with GAP or N.A. where a link has no evidence. All four rows share one Business Goal: improve successful
course completion in the program's online and blended courses by identifying students who stop taking part early
enough to support them within the semester. They also share one SMART Goal: raise the completion rate of students
enrolled after the add-drop period in the pilot courses from the recounted baseline (assumed 70%) by five percentage
points (assumed 75%) by the end of 2027–2028. The decisions supported are D1 (whom to list first at the week-3 and
week-5 review points), D2 (where to place support time across courses and groups) and D3 (whether to extend the
approach).

**Scope of the results.** The AQ1 and AQ2 results cover both years of OULAD. AQ1 is computed on the 9 runs of 2013
(13,529 enrolments; 12,076 registered at day 14), on the 13 runs of 2014 (19,064; 15,985) and on the 22 runs pooled
(32,593; 28,061), with the year comparison on both denominators (C15). AQ2 is estimated on the 9 runs of 2013 (11,811
enrolments registered at day 27) and replicated on the 13 runs of 2014 (15,724), including module CCC, with the
several-modules sign described on 2014, where it almost only exists (C12). The AQ3 test keeps the predictors, candidate
configurations, selection rule and gate that Milestone 4 fixed on 2013 alone; the one choice made after 2014 results
existed is the tuning criterion (C18). For AQ1 and AQ2 every link holds evidence, GAP marking only variables OULAD
lacks, and both meet their criteria in each year. AQ3 meets gate S1 on the 13 runs of 2014, and AQ4 turns the frozen
AQ3 scores into lists that pass fairness rule FR1; the contact part of AQ4 stays a GAP (Section 10).

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
| AQ-ID | Goal + KPI | Final AQ (short) | Level | Required data / unit | Actual data & variables | Preparation / feature logic | Method + rationale | Evaluation / result | Decision | Status |
| AQ1 | Completion +5 points; primary KPI (proxy on OULAD: completion of enrolments still registered at day 14) | Outcome shares by module, run, start month and year; week in which non-completers first miss an assessed task | Descriptive | Enrolment in one course and semester; dated final result and tasks | OULAD 2013: 9 runs, 13,529 enrolments, 12,076 at day 14; 2014: 13 runs, 19,064, 15,985 at day 14; GAP: delivery mode, year of study | Day-14 rule; non-completion = Fail or Withdrawn; first missed task over TMA and CMA | Grouped rates with 95% intervals under two denominators; no model, since the question is descriptive | Two aggregation paths agree (176 of 176 cells); non-completion 45.3% (44.7–45.8) of 28,061: 45.7% in 2013, 44.9% in 2014 | D2, D3 | Answered |
| AQ2 | Primary KPI; secondary KPI 1 (early-sign rule built from these signs) | Signs by the end of week 4 that go with later non-completion, within module | Diagnostic (association only) | Enrolment with its signs in weeks 1–4 | Day-27 features, 2013: 11,811 enrolments, task signs in 7 runs (9,960); 2014: 15,724, task signs in 9 runs (12,585); GAP: attendance; several-modules sign almost only in 2014 | Every sign dated on or before day 27; lateness for TMA only; task signs only where a task falls due | Logistic regression with run fixed effects and sign × module terms; within-module association | All 5 signs consistent in both years (≥ 5 points, interval excluding 0); missed task 40.8 points (37.7–43.9) and 39.3 (36.4–42.1) | D2; reasons on the D1 list | Answered |
| AQ3 | Secondary KPI 1 (the rule the model must beat); primary KPI through D1 | Non-completion estimated at the end of weeks 2 and 4 against the early-sign rule, 2013 → 2014 | Predictive | Enrolment at each cut-off; runs in time order | Feature views at days 13 and 27, 19 usable predictors; development 9 runs of 2013, test all 13 runs of 2014, no 2014 outcome in any model choice | Only events dated by the cut-off; every learned step refitted inside each fold | Penalised logistic regression against the rule, a background-only model and a random list; staff need each student's reasons | Gate S1 met: pooled normalised recall 0.725 against 0.704 for the rule, +0.021 (+0.006 to +0.036), 11 of 13 runs; S3 met pooled, 5 of 13 runs | D1 | Answered |
| AQ4 | Secondary KPIs 1 and 2 (contacts): GAP on OULAD | Ranked list per group of 20 students, with gain over a random list, recall and fairness | Prescriptive (ranking, decision support) | Enrolment within a run; contacts | Frozen AQ3 scores of the 13 runs of 2014 (15,724 enrolments at day 27); audit fields; GAP: contacts, contact types, outcomes after contact | Lists of 3 or 5 per 20 per run; ties broken by a fixed random number | Top-k list from the AQ3 scores with the main reason per name; fairness rule FR1 | 41.5% of non-completers on lists of 5 per 20, 72.5% of listed students do not complete; FR1: 0 of 3 groups flagged | D1 | Partial |

Reading the rows across shows where the chain is complete and where it is broken. For AQ1 and AQ2 every link holds
evidence, from the KPI to a measured result, and both questions meet the success criteria Milestone 4 fixed for them
(Sections 11.2 and 11.3). AQ3 meets its gate S1 and AQ4 its fairness rule FR1 on the 13 runs of 2014 (Sections 10 and
11.4); AQ4 is Partial because whether a contact helps cannot be measured on OULAD. The GAP cells mark data that OULAD does not
hold: delivery mode and year of study for AQ1 and AQ2, attendance for AQ2, and contacts, contact types and outcomes
after contact for AQ4. In addition, secondary KPI 2 and the contact part of secondary KPI 1 need a contact record that
only the pilot can create, so their link to AQ4 is a GAP on OULAD rather than a measured value.

## Table 2. Final status of each question and its justification

Table 2 justifies the final status of each question in one sentence (Table A.28 of the final report).

| AQ | Final status | Justification |
| :---- | :---- | :---- |
| AQ1 | Answered | AQ1 is answered for the 9 runs of 2013, the 13 runs of 2014, including module CCC, and the 22 runs pooled, with its success criterion met in each year and the year comparison on both denominators (C15, AQ1 and AQ2 on both years). |
| AQ2 | Answered | All five signs meet the consistent-association criterion on the 2013 runs and again on the 13 runs of 2014, including module CCC, and the several-modules sign is described on 2014, where it almost only exists (C15, AQ1 and AQ2 on both years; C12, several-modules sign described for 2014 only). |
| AQ3 | Answered | The Level 2 prototype developed and froze the model on the 9 runs of 2013 and tested it once on the 13 runs of 2014: gate S1 is met (Section 10); probabilities are not shown because calibration holds pooled but in 5 of 13 runs only (S3; C18). |
| AQ4 | Partial | The ranked lists are built from the frozen AQ3 scores and pass fairness rule FR1 (0 of 3 groups flagged); the contact part has no data in OULAD and is deferred to the pilot (C11, contact choice deferred). |

## Table 3. Compact matrix

Table 3 gives the same chain in the short cells of the report's main text (Tables 11.1 and 11.2 of the final report,
joined into one row per question).

| AQ-ID | Goal + KPI | Final AQ | Analytics level | Required data / unit | Actual dataset & variables | Preparation / features | Method + rationale | Evaluation / result | Decision | Final status |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Primary KPI | Outcome shares; first missed week | Descriptive | Dated result, tasks | 22 runs, day 14: 28,061; GAP: mode, year | Day-14 rule; TMA, CMA | Grouped rates; no model needed | Paths agree; 45.3% | D2, D3 | Answered |
| AQ2 | Primary KPI; KPI 1 | Signs by week 4, within module | Diagnostic | Signs, weeks 1–4 | Day 27: 11,811 and 15,724; GAP: attendance | Dated by day 27 | Logistic, run effects | 5 of 5 signs, both years | D2; D1 | Answered |
| AQ3 | KPI 1 (rule to beat) | Weeks 2 and 4 against the rule | Predictive | Enrolment at cut-off | 19 predictors; 2014 test | Refit per fold | Penalised logistic; reasons | S1 met (0.725 vs 0.704) | D1 | Answered |
| AQ4 | KPIs 1–2: GAP | Ranked list per group of 20 students | Prescriptive | Capacity; contacts | GAP: contacts | 3 or 5 per 20 | Top-k with reasons | FR1: 0 of 3 flagged | D1 | Partial |

## Evidence in this package

| Number in the matrix | Result file (`results/`) |
| :---- | :---- |
| AQ1 populations: 2013, 13,529 enrolments and 12,076 registered at day 14; 2014, 19,064 and 15,985; 22 runs, 32,593 and 28,061 | `2013/aq_results.json`, `2014/aq_results.json`, `all_runs/aq_results.json` (`aq1.all_enrolments`, `aq1.day14_registered`); `aq1_rates.csv` in each of the three folders |
| AQ1 validation: two aggregation paths agree in 72 of 72 outcome cells (2013), 104 of 104 (2014) and 176 of 176 (22 runs) | `aq_results.json` of each folder (`aq1.validation`), `aq1_validation_two_paths.csv` of each folder |
| AQ1 non-completion 45.3% (44.7–45.8) of 28,061; 45.7% (44.8–46.6) of 12,076 in 2013; 44.9% of 15,985 in 2014 | `all_runs/aq1_rates.csv`, `2013/aq1_rates.csv`, `2014/aq1_rates.csv` (7,185 of 15,985; the file stores the rate rounded to 0.4495) |
| AQ2 populations at day 27: 11,811 (2013) and 15,724 (2014); task signs in 7 runs of 2013 (9,960) and 9 runs of 2014 (12,585) | `2013/aq_results.json` and `2014/aq_results.json` (`aq2.population`), `aq1_runs_task_due.csv`, `aq2_associations.csv` of each folder |
| AQ2 verdicts of the five signs in each year; missed task 40.8 points (37.7–43.9) in 2013 and 39.3 (36.4–42.1) in 2014 | `2013/aq2_associations.csv`, `2014/aq2_associations.csv`, `compare/aq2_year_comparison.csv` |
| Several-modules sign described on 2014 (C12) | `compare/aq2_concurrent_2014.csv` |
| AQ3 development choice (M1) and gate S1: 0.725 against 0.704, +0.021 (+0.006 to +0.036), 11 of 13 runs | `2013/aq3_dev_choice.csv`, `2014/aq3_s1_gate.csv` |
| AQ3 calibration S3: met pooled, 5 of 13 runs within the bounds | `2014/aq3_discrimination_calibration.csv` |
| AQ4 lists of 5 per 20: recall 41.5%, precision 72.5%; FR1 0 of 3 groups flagged | `2014/aq3_pooled.csv`, `2014/aq4_fairness_confirmatory.csv` |
