# 5. Data Preparation Plan

Before any record was changed, each issue of the Data Quality Issue Log (Table 3.1) and each need of the questions
received a decision with its rationale, its implementation and the check that validates it, as the brief requires
[1]. The plan avoids the habits the brief names as wrong first moves: imputing every gap with a mean or zero without
analysis, dropping every duplicate without checking the grain, deleting every value outside the interquartile range,
merging rare categories at will, using future data to compute past features, and removing the sensitive attributes
that a bias audit needs [1].

Table 5.1 gives the Preparation Decision Matrix. It covers the eight needs of the brief's template, from missing values
to encoding and scaling, and four further needs of this project: the population of each table, activity after
withdrawal, the sensitive attributes and the split into training and test runs. The Validation column names the
checks V01 to V15 of the validation script, which Section 7 reports.

**Table 5.1. Preparation Decision Matrix**

| Issue / need | Decision | Rationale | Implementation | Validation |
| :---- | :---- | :---- | :---- | :---- |
| Population (C09) | Keep all 32,593 enrolments in the enrolment view with flags for days 13, 14 and 27; feature views hold only the enrolments enrolled at their cut-off | The KPI counts students enrolled after the add-drop period; a list can only name students enrolled on the day it is drawn | Enrolled at day d: registered by day d, or registration day unknown, and not unregistered by day d | V01: populations of 32,593, 28,061, 28,069 and 27,535 equal the profile |
| Missing values (DQ04, DQ11–DQ14) | imd_band "Missing" as its own category; registration day and withdrawal day left empty with an indicator; TMA score left empty; planned weeks not used | Missingness is informative (imd_band), small (45, 93, 173) or in an unused field; imputing would invent values the data do not hold | Indicators in the views; median filling of the registration lead only in the model matrices, fitted on training runs | V02: missing counts after equal those before; V12 |
| Duplicates and keys (DQ01, DQ02) | Keep every click row; sum clicks by enrolment and day, and by week, before any join; de-duplicated twin of each click feature | The cause of exact duplicates cannot be decided; a row is a logging record, not one student-day; the twin allows a sensitivity check | Daily aggregation with record count, clicks and de-duplicated clicks | V03: keys unique in every view; V04: click totals reconcile |
| Invalid category or type (DQ07, DQ12) | Label "10-20" corrected to "10-20%"; ordered categories for bands; banked results separated and never timed | Labels must sort and match; day −1 is a placeholder for a carried-over result, not a submission day | Standardisation step; status "banked" | V05: every category in its expected set; V06: no banked row in lateness or missed counts |
| Outliers (DQ10, DQ16) | Keep every value: 6,977-click record, 655 credits, submissions up to day 608 | Heavy users, students on many modules and very late submissions are real; capping would change real totals | No deletion; logarithm of counts only in the model matrices | V07: ranges after equal those before |
| Activity after withdrawal (DQ03) | Truncate engagement measures at the unregistration day | Activity after leaving is not engagement while enrolled and would blur AQ1 and AQ2 | Filter by day in the enrolment, task and week views | V08: no click or submission counted after the unregistration day |
| Table integration (DQ02, DQ17) | Left joins from the enrolment table after summing each table to the target grain; zero counts for no activity | Inner joins would drop 3,365 enrolments; a direct join of submissions and clicks returns 89 million rows | Row count asserted after every join | V09: rows equal the left table after each of 25 joins; V10: enrolments without activity kept with zero |
| Derived features (DQ08, DQ09, DQ18) | Task counts over TMA and CMA only, unweighted; lateness from due and submission days; CMA marks known by the cut-off; early-sign rule of C10; activity relative to the run's median | No exam results in five modules; weights differ by module; TMA marks have no release day; the rule must fire in every run | Formulas of Table A.13; target-derived flags kept out of feature views | V11: six features recomputed from raw by separate code; unit tests for every formula |
| Temporal aggregation | Weeks of seven days from day 0; cut-offs at day 13 and day 27; activity before day 0 as its own window | The prediction points are fixed in Milestone 2 (C02); activity before the start is known at the cut-off | Filter every event to on or before the cut-off | V13: a recount of the click features without the date filter changes them only for students who clicked after the cut-off, which shows the filter works; V11 and unit tests for task features |
| Encoding and scaling | Views keep original scales and labels; model matrices for linear models fitted on 2013 runs | A test run must never inform a parameter [1] | Ordinal codes with missing indicator, one-hot levels, logarithm, median filling and standardisation from training rows | V12: parameters unchanged when test rows are altered |
| Sensitive attributes | Gender, age band, disability, imd_band and region kept in every view as audit columns, outside both predictor sets | The fairness audit of AQ3 and AQ4 needs them; their use as predictors is a policy choice | Role "audit" in the data dictionary | V14: every column has a role; no audit column among the predictors |
| Split | Training on the 2013 runs, test on the 2014 runs; flags for paired runs and for test students seen in 2013 | The claim is prediction for a later run (C07) | Split flag at run level | V15: no run in both partitions; flags recomputed |

Three decisions shape the prepared data most. Nothing that was recorded is deleted or imputed in the prepared views,
so every count can be traced back to the raw files, and the model matrices alone hold filled and scaled values.
Every feature is built only from events dated on or before its cut-off, so no information from after the moment of
prediction reaches a model. And every parameter learned from the data, such as a median or a scale, comes from the
training runs alone, so the test runs remain an independent check. The full matrix, with the function of the
pipeline that carries out each decision, is `data/metadata/decision_matrix.md` in the Prepared Data Package.
