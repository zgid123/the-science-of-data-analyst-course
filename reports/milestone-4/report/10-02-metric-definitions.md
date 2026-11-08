## Appendix II – Metric Definitions

The Evaluation Design Cards of Section 4.1 use the metrics that Table A.4 defines, for a run r with n enrolments, the set Y of its non-completers, base rate b = |Y|/n, and a list L of the k highest scores; Section 4.1 explains the main ones in words.

**Table A.4. Metric definitions**

| Metric | Definition | Reading |
| :---- | :---- | :---- |
| Recall at capacity | \|L ∩ Y\| / \|Y\| | Share of the run's non-completers on the list |
| Attainable recall | min(k, \|Y\|) / \|Y\| | The most a list of length k can reach |
| Normalised recall | recall / attainable recall | 1 = best attainable; equals precision when \|Y\| ≥ k |
| Pooled normalised recall | Σ\|L ∩ Y\| / Σ min(k, \|Y\|) over runs | Each run keeps its own list and k |
| Precision at capacity | \|L ∩ Y\| / k | Share of the list who do not complete |
| Lift | precision / b | 1 = chance; a random list has expected recall k/n |
| ROC-AUC (within run) | Probability that a non-completer scores above a completer of the same run | Discrimination without run differences |
| PR-AUC (within run) | Area under a run's precision–recall curve | Read against its chance level b [24] |
| Calibration-in-the-large | Intercept of a logistic model of the outcome with the score's log-odds as offset | Target 0 [33] |
| Calibration slope | Coefficient of the score's log-odds in a logistic recalibration | Target 1; below 1 means risks too extreme [33] |
| Brier score | Mean squared difference between predicted risk and outcome | Overall accuracy of probabilities |
| Net benefit | true positives/n − false positives/n × pt/(1 − pt) at threshold probability pt | Context: contact-all, contact-none and the rule [25] |
| ABROCA | Absolute area between the ROC curves of a group and the rest | Threshold-free differential discrimination [34] |
