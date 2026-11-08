# S408 – Bias in error estimation when using cross-validation for model selection (Varma & Simon, BMC Bioinformatics 2006)

## Summary in my own words

The authors tune two classifiers by minimising cross-validation (CV) error and then report that same CV error as the performance estimate. On simulated "null" data where the classes do not differ, the tuned classifiers often reported low CV error although their error on 20,000 independent samples was at chance level. The reported CV error of a tuned classifier is therefore substantially optimistic. A nested CV – an outer loop for estimation with all tuning inside an inner loop – gave estimates very close to the independent test error. The general rule is that every step of training, including tuning, must be repeated inside each CV loop.

## Key facts

- Author-reported bias on null data – "the CV error estimate for the Shrunken Centroid with the optimal parameters was less than 30% on 18.5% of simulated training data-sets. For SVM with optimal parameters the estimated error rate was less than 30% on 38% of "null" data-sets."
- Test performance – "Performance of the optimized classifiers on the independent test set was no better than chance."
- Conclusion – "using CV to compute an error estimate for a classifier that has itself been tuned using CV gives a significantly biased estimate of the true error."
- Rule – "requires that all steps of the algorithm, including classifier parameter tuning, be repeated in each CV loop."
- Remedy – "A nested CV procedure provides an almost unbiased estimate of the true error."
- Nested CV close to test – "gives an estimate of the error that is very close to that obtained on the independent testing set"
- Feature selection outside the loop is a known violation, after Ambroise C. & McLachlan G.J. (PNAS 2002) – "all aspects of training a classifier e.g. feature selection, classifier type selection and classifier parameter tuning takes place on the data not left out during each CV loop."

## Used in

04-02-validation-strategy.md

## Against reference.md

Confirms the outline's validation bullets "grouped folds inside the training years" and "single use of the test runs": the fold score used to choose settings is optimistic, so the reported performance must come either from a nested loop or from the untouched 2014 test runs. No contradiction.

## Reliability

Primary; research article by Varma S. and Simon R. (US National Cancer Institute); BMC Bioinformatics 7:91 (2006); open access PMC1397873. Citation traction: 2393 Crossref / 2638 OpenAlex citations as of 2026-11-06. Current as of November 2026; small-sample microarray setting (40 samples) – the bias is largest when data are small, which the OULAD training years are not.

## Open questions

The size of the selection bias with thousands of students and few hyperparameters is not quantified here; Cawley & Talbot (S409) show it persists with few hyperparameters.
