# S409 – On over-fitting in model selection and subsequent selection bias in performance evaluation (Cawley & Talbot, JMLR 2010)

## Summary in my own words

The paper shows that a model selection criterion such as k-fold CV error has variance as well as bias, and that minimising a noisy criterion over hyperparameters over-fits the selection itself. The resulting performance loss and the optimistic bias of evaluation protocols that reuse the selection data are often as large as the differences between competing learning algorithms. Model selection must therefore be treated as part of model fitting and repeated afresh in each evaluation trial, for example through nested cross-validation. The authors also note that a difference between two algorithms that is smaller than the variation due to sampling of the data has little practical significance.

## Key facts

- Variance matters – "we demonstrate that a low variance is at least as important, as a nonnegligible variance introduces the potential for over-fitting in model selection as well as in training the model."
- Magnitude – "the effects of this form of over-fitting are often of comparable magnitude to differences in performance between learning algorithms, and thus cannot be ignored in empirical evaluation."
- Selection bias – "some common performance evaluation practices are susceptible to a form of selection bias as a result of this form of over-fitting and hence are unreliable."
- Treat selection as fitting – "model selection must be treated as an integral part of the model fitting process and performed afresh every time a model is fitted to a new sample of data."
- Nested CV, after Stone M. (JRSS B 1974) – "performance evaluation is likely to require more rigorous and computationally intensive protocols"
- Compare procedures, not algorithms – "we should instead compare learning algorithm/model selection procedure combinations."
- Few hyperparameters still biased – "the external crossvalidation protocol exhibits a consistent optimistic bias, potentially of a very substantial magnitude"
- Practical significance – "a difference in performance between two algorithms is unlikely to be of practical significance, even if it is statistically significant, if it is smaller than the variation in performance due to the random sampling of the data"
- Conclusion – "model selection should be viewed as an integral part of the model fitting procedure, and should be conducted independently in each trial in order to prevent selection bias"

## Used in

04-02-validation-strategy.md, 04-03-metrics-success.md

## Against reference.md

Confirms the outline's "single use of the test runs, frozen plan": tuning on the LORO folds and reporting the same fold scores would carry selection bias, so the final estimate comes from the 2014 runs scored once. Extends the "comparison with the rule, uncertainty" bullet: a model-versus-model gap smaller than sampling variation should not be read as a win. No contradiction.

## Reliability

Primary; peer-reviewed article by Cawley G.C. and Talbot N.L.C. (University of East Anglia); Journal of Machine Learning Research 11:2079–2107 (2010); official JMLR PDF. Citation traction not retrieved by metadata lookup (JMLR has no DOI); widely cited (no count recorded, as of 2026-11-06). Current as of November 2026.

## Open questions

Citation count not available from Crossref/OpenAlex by DOI.
