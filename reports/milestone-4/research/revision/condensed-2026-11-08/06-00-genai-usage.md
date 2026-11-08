# 6. Generative AI Usage

Alongside the risks of Part 5, generative AI was used in the roles the brief allows:
explaining methods, proposing and challenging candidate families, and reviewing metrics, splits, leakage, calibration
and fairness, while the final choice and its evidence remain the team's [1]. Table 6.1 summarises the AI Decision
Log; the full log, the team's decision on each critique and the reviewers' prompts are in Appendix VII (Tables
A.18–A.20).

**Table 6.1. AI Decision Log (summary)**

| Role | AI contribution | Team decision | Verification | Effect |
| :---- | :---- | :---- | :---- | :---- |
| Literature assistant | Sources on method choice, evaluation design, risk and regulation | Accepted after reading | Every statement matched to a verbatim quotation in a saved copy of its source | Parts 2–5 |
| Model-selection critic | 12 critiques of the briefs and candidate comparison | 10 accepted, 2 in part | Checked against counts and run lengths from the prepared data | Within-run metrics, unseen-module rule, labels-available variant, reasons from the scoring model |
| Evaluation reviewer | 12 critiques of the cards, protocol, fairness analysis and risks | 12 accepted | Arithmetic recomputed | Single gate S1 with a sign-flip test; S2 reported only; fairness check one-sided with Holm adjustment |

The two reviewers made the most consequential points, for example that the training runs cover 6 modules rather than 7, that the October 2013 runs end after the February 2014 runs need scores, and that a success rule requiring the model to beat the early-sign rule in at least 9 of the 13 test runs would be met by chance about 13% of the time; the team verified each point against the prepared data before adopting it. No AI produced a metric value, threshold or result: every number is a count from the prepared data or a value
fixed by the team with its reason, as the brief requires [1].
