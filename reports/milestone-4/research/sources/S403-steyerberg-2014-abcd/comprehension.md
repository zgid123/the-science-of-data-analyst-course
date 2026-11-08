# S403 – Towards better clinical prediction models: seven steps for development and an ABCD for validation (Steyerberg & Vergouwe, European Heart Journal 2014)

## Summary in my own words

The paper gives a seven-step recipe for developing a prediction model and four validation measures summarised as ABCD: A, calibration-in-the-large (the intercept); B, the calibration slope; C, the concordance (c) statistic for discrimination; D, decision-curve net benefit for clinical usefulness. It separates internal validity (reproducibility, best checked with cross-validation or bootstrap rather than a single random split) from external validity (transportability), which includes temporal validation on more recently treated patients. It explains why calibration and discrimination do not show whether a model leads to better decisions, why a threshold reflects the relative weight of harms and benefits, and why a range of thresholds should be examined. Its worked example shows the slope dropping below 1 for a model developed on a small sample.

## Key facts

- ABCD – "We propose four key measures in the assessment of the validation of prediction models, related to calibration, discrimination, and clinical usefulness."
- Split sample is weak – "Using a random sample for model development, and the remaining patients for validation (‘split sample validation’) is a common, but suboptimal form of internal validation."
- Better internal validation – "Better methods are cross-validation and bootstrap resampling"
- Temporal validation – "External validity may be evaluated by studying patients who were more recently treated (temporal validation)"
- External is stronger – "External validation is commonly considered a stronger test for prediction models than internal validation, since it addresses transportability rather than reproducibility."
- A – "The intercept A relates to calibration-in-the-large, which compares the mean of all predicted risks with the mean observed risk."
- B – "The calibration slope B is often smaller than 1 if a model was developed in a relatively small data set."
- Author-reported example – "For the model based on 259 patients, the slope was 0.70 among the 17 796 non-US patients"
- Perfect calibration without discrimination is useless – "a model that predicts for all subjects the same predicted risk equal to the incidence shows perfect calibration, but is useless since it does not discriminate between patients."
- D – "these aspects do not assess clinical usefulness, i.e. the ability to make better decisions with a model than without."
- Threshold range – "It is therefore advised to consider a range of thresholds when quantifying the clinical usefulness of a prediction model."
- Sensitivity plus specificity is naive – "The sum of sensitivity and specificity can only be used as a naive summary indicator of usefulness"
- Net benefit, after Vickers A.J. & Elkin E.B. (Med Decis Making 2006; S405) – "Recently proposed and more appropriate summary measures include the net benefit (NB)."

## Used in

04-02-validation-strategy.md, 04-03-metrics-success.md

## Against reference.md

Confirms the outline's validation bullet "time split": temporal validation on later cases is named as a form of external validation that tests transportability, which is the role of the 2014 test runs. Confirms and structures the metrics bullet (discrimination, calibration, comparison with the rule) through the ABCD measures, with net benefit as the decision-based comparison. No contradiction.

## Reliability

Primary; review by Steyerberg E.W. and Vergouwe Y. (Leiden and Erasmus MC); European Heart Journal 35(29):1925–1931 (2014); open access PMC4155437. Citation traction: 1764 Crossref / 1945 OpenAlex citations as of 2026-11-06. Still current as of November 2026 as a widely cited framework; TRIPOD+AI (S400) and PROBAST+AI (S401) supersede it as the formal standard.

## Open questions

None.
