# 7. Data Preparation and Analytic-ready Data

In Milestone 3 we built the pipeline that turns the seven raw tables into analytic-ready views, and every analysis
reads them. Before any record changed, each issue received a decision with its reason and a validation check,
V01 to V15, that fails if the decision is not carried out. Three decisions govern the result: nothing recorded is
deleted or imputed in the views, every feature uses only events dated on or before its cut-off, and every learned
parameter comes from the training runs alone. Table 7.1 is the Preparation Decision Matrix (Table A.17, Appendix VII,
adds the reasons); the ten scripted steps of the pipeline and their counts are in Appendix VII.

**Table 7.1. Preparation Decision Matrix**

| Need | Decision | Check |
| :---- | :---- | :---- |
| Population | Flags for days 13, 14 and 27 (C09); views hold those enrolled at the cut-off | V01 |
| Missing values | "Missing" category or indicator; no imputation | V02, V12 |
| Duplicates, keys, integration | Every row kept; clicks summed by day; left joins from the enrolments | V03, V04, V09, V10 |
| Invalid values, outliers | Labels corrected; banked results untimed; every value kept | V05–V07 |
| Activity after withdrawal | Truncated at the unregistration day | V08 |
| Derived features | TMA and CMA tasks; early-sign rule (C10); activity against the run median | V11 |
| Time, encoding | Cut-offs at days 13 and 27; transforms learned on training rows | V12, V13 |
| Sensitive attributes, split | Audit columns outside the predictors; train 2013, test 2014 | V14, V15 |
