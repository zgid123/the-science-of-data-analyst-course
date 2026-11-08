# S410 – Leakage and the reproducibility crisis in machine-learning-based science (Kapoor & Narayanan, Patterns 2023)

## Summary in my own words

A survey of 22 review papers across 17 fields finds data leakage in every field, affecting at least 294 papers. The authors give an eight-type taxonomy in three families: L1, no clean train–test separation (no test set, pre-processing or feature selection on all data, duplicates); L2, illegitimate features (proxies of the outcome); L3, a test set not drawn from the distribution of interest (temporal leakage, non-independence between training and test samples, sampling bias). They propose model info sheets – 21 questions that make authors argue clean separation, legitimate features and a representative test set. In a civil-war prediction case study, the claimed superiority of complex ML over logistic regression disappeared once leakage was corrected, and most papers compared classifiers without uncertainty quantification.

## Key facts

- Scale – "data leakage affects at least 294 studies across 17 fields, leading to overoptimistic findings."
- Taxonomy – "We classified these errors into eight different types."
- L1 – "[L1] Lack of clean separation of training and test dataset."
- L1.2 – "Using the entire dataset for any pre-processing steps, such as imputation or over/under sampling, results in leakage."
- L1.3 – "Feature selection on the entire dataset results in using information about which feature performs well on the test set"
- L2 – "[L2] Model uses features that are not legitimate."
- L2 judgement – "we suggest that researchers clearly specify which features are suitable for a modeling task and justify their choice using domain expertise."
- L3.1 temporal – "When an ML model is used to make predictions about a future outcome of interest, the test set should not contain any data from a date before the training set."
- L3.2 non-independence – "Nonindependence between training and test samples constitutes leakage, unless the scientific claim is about a distribution that has the same dependence structure."
- L3.3 – "[L3.3] Sampling bias in test distribution."
- Model info sheets – "by answering 21 questions based on our taxonomy of leakage."
- Separation is not enough – "it is not enough to simply separate the training and test sets and report performance metrics on the test set."
- Author-reported case study – "When the errors are corrected, complex ML models perform no better than baseline LR models in each case except Wang,77"
- Uncertainty missing – "We found that 9 of the 12 papers for which complete code and data were available included no significance tests or uncertainty quantification for classifier performance comparison"
- Model info sheets are inspired by Mitchell M. et al. (FAT* 2019; S505 model cards) – "They are inspired by the model cards in Mitchell et al.40"

## Used in

04-02-validation-strategy.md, 04-00-evaluation-design.md, 04-03-metrics-success.md

## Against reference.md

Confirms the outline's validation bullet: a time split (train 2013, test 2014) addresses L3.1, grouped folds address L3.2, and single use of the test runs plus a frozen plan addresses L1. Extends the outline with L2: each predictor must be legitimately available at the day-13 or day-27 cut-off. Extends the "uncertainty" bullet: model comparisons need uncertainty quantification. No contradiction.

## Reliability

Primary; peer-reviewed article by Kapoor S. and Narayanan A. (Princeton University); Patterns 4(9):100804 (2023); open access PMC10499856. Citation traction: 1512 Crossref / 1893 OpenAlex citations as of 2026-11-06. Current as of November 2026; the authors version their model info sheets, so the 21-question template may have later versions.

## Open questions

The model info sheet template (supplement S4) was not fetched; the report cites only the three arguments stated in the main text.
