# 7. Prototype Protocol

**Purpose.** The optional prototype of Level 2 tests whether the Level 1 choices are feasible and shows their
trade-offs; it does not compete for the best score, and it requires no large-scale tuning [1]. This report does not
run the prototype, so it states no model performance; it specifies how the prototype will run, so that whoever runs it
follows the evaluation fixed in Part 4.

**Steps.** Table 7.1 gives each step of the brief with how the prototype carries it out. Because the proposal is
frozen first, the prototype can confirm or refute the choices of Level 1, but it cannot reshape them after its results
are seen.

**Table 7.1. Prototype protocol**

| Brief step | Specification |
| :---- | :---- |
| 1. Reproduce data input | Load OULAD-N04-prepared-1.0, check its file hashes, change no raw data |
| 2. Implement baseline | Rule-ranked list, background-only model and random list, before any candidate |
| 3. Implement candidate | Penalised logistic regression (primary) and gradient-boosted trees (challenger), as in Table 3.1 |
| 4. Split and fit correctly | Protocol of Section 4.2 and Appendix IV |
| 5. Evaluate | Metrics and criteria of Table 4.2, including unfavourable results |
| 6. Error and subgroup analysis | Error slices and confirmatory fairness check of Section 4.4 |
| 7. Compare to Level 1 expectation | Whether S1 holds and the challenger's margin was met; any change recorded with its reason |
| 8. Reproducibility | Scripts, seeds, package and data versions, folds and test-access record in an experiment log |

**A baseline may win.** A baseline that matches the candidate is an acceptable outcome. The brief notes that a simple
baseline can be the better choice when the improvement of a complex model is small and its interpretability is lower
[1]; in that case the rule or the background-only model is carried forward with its reasons, and the change is recorded
in the experiment log.
