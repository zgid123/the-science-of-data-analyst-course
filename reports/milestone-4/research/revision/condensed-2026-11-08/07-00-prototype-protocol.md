# 7. Prototype Protocol

The optional prototype of Level 2 tests the feasibility of the Level 1 choices without competing for the best score
[1]. Building on the evaluation of Part 4, Table 7.1 specifies how it runs, step by step as the brief sets them;
because the proposal is frozen first, the prototype can confirm or refute the choices but cannot reshape them.

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

A baseline that matches the candidate is an acceptable outcome: a simple baseline can be the better choice [1], and
in that case the rule or the background-only model is carried forward with its reasons.
