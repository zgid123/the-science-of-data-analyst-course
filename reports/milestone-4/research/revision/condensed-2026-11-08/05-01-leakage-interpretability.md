## 5.1. Leakage, Overfitting and Interpretability

Following the notes of Table 5.1, the first group of risks concerns the validity of the evaluation. Leakage covers
three failures that matter here: unclean separation of training and test data, including preprocessing on the whole
dataset; features that act as proxies of the outcome; and temporal leakage or dependence between training and test
samples [22]. The modeller should not see information beyond the separation point [39], so the 2014 outcomes stay
unopened until the single test, AQ2 waits for it (Change Log entry C14, Appendix VIII), and every learned step is refitted inside each fold. Predictors
must have been available at the moment of use [40], which the dated views ensure and the labels-available variant
checks. Overfitting also enters through model choice: a tuned fold score is optimistic [28], so fold results serve only the choice and are never reported as performance. Published comparisons of machine learning with logistic regression are often biased by validation flaws and silent on calibration [18], which the frozen validation of Section 4.2 avoids.

Interpretability is built into the choice of model rather than added afterwards. Each student's reasons come from the
same logistic model that ranks them, which avoids post-hoc explanations that can mislead [11]. Many models fit about
equally well [5], so no coefficient is read as a cause, and AQ2's mutually adjusted estimates are shown beside the
unadjusted gaps. The final model is to be documented in a model card, which states intended and out-of-scope uses with performance by group [41], and the prepared data in a datasheet, which records composition, collection and recommended uses [42]. The data limit what can be claimed: 9 training runs from 6 modules, one module seen only in
2014, and distance learning in the United Kingdom (UK) of 2013–2014, so any use at a Vietnamese university starts with local validation.
