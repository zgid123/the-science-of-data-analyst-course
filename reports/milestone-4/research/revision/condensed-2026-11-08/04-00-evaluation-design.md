# 4. Evaluation Design

With the methods of Part 3 chosen, the evaluation is fixed before any code runs, because the brief requires the
evaluation plan even without code and forbids setting thresholds after the results are seen [1]. The current
reporting standard for prediction models built by regression or machine learning, the Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis statement updated for AI (TRIPOD+AI), frames evaluation as
discrimination, calibration and usefulness for decisions, each measure stated with its rationale [21]. Data leakage
has affected at least 294 published studies across 17 fields [22], so the design also fixes who may see which data
and when. Section 4.1 gives the Evaluation Design Cards, Section 4.2 the validation strategy, Section 4.3 the metrics
and success criteria, and Section 4.4 the error, subgroup and fairness analysis.
