# S305 – Regression Shrinkage Methods for Clinical Prediction Models Do Not Guarantee Improved Performance (Van Calster, van Smeden & Steyerberg, SMMR 2020)

## Summary in my own words

In a simulation study for binary outcomes, the authors compare maximum likelihood with uniform shrinkage, ridge, lasso, adaptive lasso, non-negative garrote, penalised likelihood and Firth's correction, focusing on the calibration slope. Shrinkage improves calibration slopes on average but varies a lot between samples, and the estimated shrinkage is typically negatively correlated with the shrinkage actually needed. Penalisation therefore does not rescue a small sample or few events per variable; it is a refinement, not a licence for less data.

## Key facts

- Methods compared – "uniform shrinkage (likelihood-based and bootstrap-based), ridge regression, penalized maximum likelihood, LASSO regression, adaptive LASSO, non-negative garrote, and Firth’s correction."
- Average gain – "First, shrinkage improved calibration slopes on average."
- Variability – "Second, the between-sample variability of calibration slopes was often increased relative to maximum likelihood."
- Fails when needed – "although shrinkage improved predictions on average, it often worked poorly in individual datasets, in particular when shrinkage was most needed."
- Small samples not solved – "these methods do not solve problems associated with small sample size or low number of events per variable."
- Key finding – "Shrinkage does not lead to more reliable prediction models at low sample size, and hence does not justify using lower sample sizes."
- Bootstrap uniform shrinkage – "Among the shrinkage methods, the bootstrap-based uniform shrinkage worked well overall."

## Used in

03-03-predictive.md, 03-00-candidate-approaches.md

## Against reference.md

Qualifies the outline's "regularised logistic regression" for AQ3: regularisation is advisable with 20 correlated predictors, but its benefit must be checked through calibration on the held-out 2014 runs, and it does not justify small per-module models.

## Reliability

Primary; peer-reviewed simulation study by B. Van Calster, M. van Smeden, B. De Cock and E. W. Steyerberg (KU Leuven, Leiden UMC; the preprint lists the three authors other than De Cock), *Statistical Methods in Medical Research* 29(11), 3166–3178, doi:10.1177/0962280220921415; read from the arXiv preprint 1907.11493 (title "On the variability of regression shrinkage methods for clinical prediction models: simulation study on predictive performance"), whose abstract matches the published findings. OpenAlex cited-by count 127 as of 2026-11-06. Related: Riley et al. (2021, J Clin Epidemiol) reached a similar conclusion; not fetched.

## Open questions

Wording of the published version may differ slightly from the preprint.
