# S301 – No Performance Benefit of ML over Logistic Regression for Clinical Prediction (Christodoulou et al., J Clin Epidemiol 2019)

## Summary in my own words

This systematic review compared logistic regression with machine-learning models (trees, random forests, neural networks, SVMs) in 71 clinical prediction studies with binary outcomes. Among comparisons at low risk of bias the difference in logit(AUC) was zero; ML appeared better only in comparisons at high risk of bias. Most studies ignored calibration. For a tabular risk model the lesson is that ML's apparent advantage often reflects flawed validation, so a fair, pre-registered comparison against logistic regression is needed.

## Key facts

- Scope – "We included 71 of 927 studies."
- Study characteristics – "The median sample size was 1,250 (range 72-3,994,872), with 19 predictors considered (range 5-563) and eight events per predictor (range 0.3-6,697)."
- Validation bias common – "In 48 (68%) studies, we observed potential bias in the validation procedures."
- Calibration neglected – "Calibration was not addressed in 56 (79%) studies."
- Low-bias result (author-reported) – "For 145 comparisons at low risk of bias, the difference in logit(AUC) between LR and ML was 0.00 (95% confidence interval, -0.18 to 0.18)."
- High-bias result (author-reported) – "For 137 comparisons at high risk of bias, logit(AUC) was 0.34 (0.20-0.47) higher for ML."
- Conclusion – "We found no evidence of superior performance of ML over LR."

## Used in

03-00-candidate-approaches.md, 03-01-criteria-matrix.md, 03-03-predictive.md

## Against reference.md

Confirms the outline's Part 3 ordering "regularised logistic regression; tree ensembles" and the criterion "complexity vs baseline": a tree ensemble should be adopted only if it beats logistic regression under the same frozen validation. Clinical, not educational, data: the transfer to OULAD is by analogy (tabular, binary outcome, few dozen predictors).

## Reliability

Primary; peer-reviewed systematic review by E. Christodoulou, J. Ma, G. S. Collins, E. W. Steyerberg, J. Y. Verbakel and B. Van Calster, *Journal of Clinical Epidemiology* 110, 12–22, doi:10.1016/j.jclinepi.2019.02.004. OpenAlex cited-by count 2,180 as of 2026-11-06. Status partial: structured abstract from Europe PMC (full text closed). Literature window 2016–2017; no updated review by the same group was checked.

## Open questions

Whether newer reviews (2022–2026) changed the finding was not checked.
