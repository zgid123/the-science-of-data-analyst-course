# 6. Generative AI Usage

**Roles.** Alongside the risks of Part 5, generative AI was used in the roles that the brief allows a modeling
partner: explaining methods, proposing and challenging candidate families, and reviewing metrics, splits, leakage,
class imbalance, calibration and fairness, while the final choice and the evidence for it remain ours [1]. We decided on every suggestion and verified it against the prepared data, the sources or the arithmetic,
as the log below shows. Three roles were used: a literature assistant that found and read sources, a model-selection
critic that challenged the briefs and the candidate comparison, and an evaluation reviewer that challenged the cards,
the protocol, the fairness analysis and the risks.

**AI Decision Log.** Table 6.1 is the AI Decision Log in the brief's five columns for the two reviews that shaped the
proposal most: the prompt or goal, the AI's suggestion, our decision, the evidence used to verify it and its effect on
the proposal. The three literature searches, whose suggestions we accepted after reading each source, are logged in
the same columns in Appendix VI (Table A.19).

**Table 6.1. AI Decision Log**

| Prompt / goal | AI suggestion | Team decision | Evidence / verification | Effect on the proposal |
| :---- | :---- | :---- | :---- | :---- |
| Review the model selection as a sceptical analyst (critic) | 12 critiques: within-run evaluation, run-grouped folds, one primary test comparison, AQ2 per-module output, reasons from the scoring model, rule for switching to the challenger, survival assumption, sample size versus transfer, ranks versus probabilities, fairness power, risk versus need, repeat students | 10 accepted, 2 accepted in part (Table A.20) | Each critique checked against the design facts and the run lengths | Appendices I–II and IV–VI |
| Review the evaluation design as a methodologist (reviewer) | 12 critiques: unseen module, per-run versus tutor capacity, S1 inference, S2 basis, primary population, calibration definition, model-choice aggregation, fairness gate, ABROCA reference, AQ2 effect measure, error-analysis gaps, missing risks | 12 accepted (Table A.21) | Arithmetic of each critique recomputed | Appendices III–VI; S2 (precision at capacity) reported, not a gate |

**Decisions on the critiques.** Appendix VI (Tables A.20 and A.21) gives our decision on each of the 24
critiques of the model-selection critic and of the evaluation reviewer, with the evidence used to check it, and the
reviewers' prompts.

**Reflection.** The reviewers made the most consequential points. They asked, for example, that every count be taken from the 6 modules of the training runs, that the end dates of the
October 2013 runs be checked against the cut-offs of the February 2014 runs, and that the chance of a success rule be
computed, which showed that requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be
met by chance about 13% of the time; we verified each point against the prepared data before adopting it. The reviews were
most useful where the AI had to argue from the counts of the prepared data rather than from general advice. No AI
produced a metric value, a threshold or a result: every number in this proposal is a count from the prepared data or a
value we fixed with its reason, as the brief requires [1].
