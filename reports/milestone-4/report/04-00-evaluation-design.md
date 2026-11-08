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
