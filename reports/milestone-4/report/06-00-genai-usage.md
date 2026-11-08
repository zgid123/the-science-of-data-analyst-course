# 6. Generative AI Usage

**Roles.** Alongside the risks of Part 5, generative AI was used in the roles that the brief allows a modeling
partner: explaining methods, proposing and challenging candidate families, and reviewing metrics, splits, leakage,
class imbalance, calibration and fairness, while the final choice and the evidence for it remain the team's [1]. Team members decided on every suggestion and verified it against the prepared data, the sources or the arithmetic,
as the log below shows. Three roles were used: a literature assistant that found and read sources, a model-selection
critic that challenged the briefs and the candidate comparison, and an evaluation reviewer that challenged the cards,
the protocol, the fairness analysis and the risks.

**AI Decision Log.** Table 6.1 is the AI Decision Log in the brief's five columns, one row per significant AI
contribution: the prompt or goal, the AI's suggestion, the team's decision, the evidence used to verify it and its
effect on the proposal.

**Table 6.1. AI Decision Log**

| Prompt / goal | AI suggestion | Team decision | Evidence / verification | Effect on the proposal |
| :---- | :---- | :---- | :---- | :---- |
| Find well-known sources on method choice for each AQ (literature assistant) | Explain-versus-predict distinction; rule and simple baselines first; interpretable models for high-stakes use; sample size criteria; survival and ranking framings | Accepted after reading each source | Every statement checked against a saved copy of its source, with a verbatim quotation | Parts 2–3; Appendices I–II |
| Find sources on evaluation design (literature assistant) | TRIPOD+AI and the Prediction model Risk Of Bias ASsessment Tool for AI (PROBAST+AI); calibration; grouped folds; nested tuning; leakage types; pre-registration; hierarchical bootstrap; slicing analysis | Accepted; the imbalance argument for precision–recall curves not used, since non-completion is 44–46% and the classes are therefore not imbalanced | Same verification | Part 4; Appendices III–V |
| Find sources on risk, causality, fairness and regulation (literature assistant) | Target trials and uplift need treatment data; fairness criteria conflict; EU AI Act and Vietnam's AI law and high-risk list; performative prediction | Accepted; the EU Act used as a reference standard, Vietnamese law as binding on a Vietnamese pilot | Legal texts read in official copies where available; the EU text in a secondary copy | Part 5; Appendix V |
| Review the model selection as a sceptical analyst (critic) | 12 critiques: within-run evaluation, run-grouped folds, one primary test comparison, AQ2 per-module output, reasons from the scoring model, rule for switching to the challenger, survival assumption, sample size versus transfer, ranks versus probabilities, fairness power, risk versus need, repeat students | 10 accepted, 2 accepted in part (Table A.10) | Each critique checked against the design facts and the run lengths | Appendices I–II and IV–VI |
| Review the evaluation design as a methodologist (reviewer) | 12 critiques: unseen module, per-run versus tutor capacity, S1 inference, S2 basis, primary population, calibration definition, model-choice aggregation, fairness gate, ABROCA reference, AQ2 effect measure, error-analysis gaps, missing risks | 12 accepted (Table A.11) | Arithmetic of each critique recomputed | Appendices III–VI; S2 (precision at capacity) reported, not a gate |

**Decisions on the critiques.** Appendix VI (Tables A.10 and A.11) gives the team's decision on each of the 24
critiques of the model-selection critic and of the evaluation reviewer, with the evidence used to check it, and the
reviewers' prompts.

**Reflection.** The reviewers made the most consequential points. They asked, for example, that every count be taken from the 6 modules of the training runs, that the end dates of the
October 2013 runs be checked against the cut-offs of the February 2014 runs, and that the chance of a success rule be
computed, which showed that requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be
met by chance about 13% of the time; the team verified each point against the prepared data before adopting it. The reviews were
most useful where the AI had to argue from the counts of the prepared data rather than from general advice. No AI
produced a metric value, a threshold or a result: every number in this proposal is a count from the prepared data or a
value fixed by the team with its reason, as the brief requires [1].
