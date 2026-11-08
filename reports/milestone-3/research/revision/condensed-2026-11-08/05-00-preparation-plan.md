# 5. Data Preparation Plan

Before any record was changed, each issue of Table 3.1 received a decision with its rationale, implementation and
check, as the brief requires [1], avoiding the habits the brief names: imputing everything with a mean, dropping
all duplicates, deleting every value outside the interquartile range, using future data for past features and
removing the sensitive attributes a bias audit needs [1]. Table 5.1 gives the Preparation Decision Matrix; checks
V01–V15 are those of Section 7, and the full matrix is `data/metadata/decision_matrix.md`.

**Table 5.1. Preparation Decision Matrix**

| Issue / need | Decision | Rationale | Implementation | Validation |
| :---- | :---- | :---- | :---- | :---- |
| Population | All enrolments flagged; feature views hold those enrolled at the cut-off | KPI and lists concern enrolled students | Enrolled-at-day rule (C09) | V01 |
| Missing values | "Missing" category; indicators; no imputation in views | Informative or small | Training medians in model matrices only | V02, V12 |
| Duplicates and keys | All click rows kept; daily sums; de-duplicated twin | Cause undecidable; record grain | Aggregate before joins | V03, V04 |
| Invalid category or type | "10-20" label fixed; banked results never timed | Placeholder day −1 | Status "banked" | V05, V06 |
| Outliers | Every value kept | Real heavy users and late submissions | log1p in model matrices only | V07 |
| Activity after withdrawal | Truncated at unregistration | Not engagement while enrolled | Filter by day | V08 |
| Table integration | Left joins; zero counts | Inner joins drop 3,365 enrolments | Checked joins | V09, V10 |
| Derived features | TMA and CMA unweighted; CMA marks after 7 days; rule of C10 | No exam results or release days | Table 6.1 | V11 |
| Temporal aggregation | Weeks of 7 days; cut-offs day 13 and 27 | Prediction points of Milestone 2 | Filter to the cut-off | V13 |
| Encoding and scaling | Original scales in views; linear-model matrices from 2013 runs | No test run informs a parameter | Ordinal, one-hot, log1p, standardise | V12 |
| Sensitive attributes | Kept as audit columns | Fairness audit | Role "audit" | V14 |
| Split | Train 2013, test 2014 | Later-run claim | Split flag | V15 |
