## 5.1. Leakage, Overfitting and Interpretability

**Leakage.** Following the notes of Table 5.1, the first group of risks concerns the validity of the evaluation.
Leakage covers three failures that matter here: an unclean separation of training and test data, including
preprocessing fitted on the whole dataset; features that act as proxies of the outcome; and temporal leakage, or
dependence between training and test samples [22]. The modeller should not see information beyond the point that
separates training from testing [40]. The 2014 outcomes therefore stay unopened until the single test, AQ2 waits for it (Change Log entry C14, Appendix VII), and every learned step is refitted inside each fold. Predictors must have been available at the moment the
model is used [41], which the dated feature views ensure and the labels-available variant checks, since the outcomes of the
October 2013 runs are not yet known when the February 2014 runs reach their cut-offs.

**Overfitting.** Overfitting also enters through the choice of model: a fold score that was tuned on the same folds is
optimistic [30], so fold results serve only the choice between candidates and are never reported as performance.
Published comparisons of machine learning with logistic regression are often biased by flaws in validation and silent
on calibration [18], which the frozen validation of Section 4.2 is designed to avoid.

**Interpretability.** Interpretability is built into the choice of model rather than added afterwards. Each student's
reasons come from the same logistic model that ranks the student, which avoids explanations made afterwards that can
mislead [11]. Many different models, with different coefficients, fit about equally well [5]; the chosen
model's coefficients are one of many sets that fit the data, so no coefficient is read as a cause, and AQ2's
mutually adjusted estimates are shown beside the unadjusted gaps. The final model is to be documented in a model card,
which states its intended and out-of-scope uses with its performance by group [42], and the prepared data in a
datasheet, which records their composition, collection and recommended uses [43].

**Data constraints.** The data limit what can be claimed: 9 training runs from 6 modules, one module (CCC) seen only
in 2014, and distance learning in the UK in 2013–2014. Any use at a Vietnamese university therefore
starts with validation on the university's own records.
