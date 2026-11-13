## 5.1. Leakage, Overfitting and Interpretability

**Validity of the evaluation.** Following the notes of Table 5.1, the first group of risks concerns the validity of the
evaluation. Leakage is controlled by design: the 2014 outcomes stay unopened until the single test, every predictor is
dated on or before the cut-off, and every learned step is refitted inside each fold [22], [40], [41]. Overfitting
through the choice of model is limited by nested tuning, the margin fixed in advance and fold results that are never
reported as performance [30], [18]. Interpretability is built into the choice of model: each student's reasons come
from the same logistic model that ranks the student [11], no coefficient is read as a cause [5], and the final model
and the prepared data are to be documented in a model card and a datasheet [42], [43]. The data limit what can be
claimed: 9 training runs from 6 modules, module CCC seen only in 2014, and distance learning in the UK in 2013–2014, so
any use at a Vietnamese university starts with validation on the university's own records. Appendix V, item 2,
treats each of these risks in full.
