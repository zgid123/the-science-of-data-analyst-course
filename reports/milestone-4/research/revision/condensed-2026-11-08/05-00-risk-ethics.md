# 5. Risk, Ethics and Limitations

The evaluation of Part 4 measures how well the methods work, and what can go wrong when they are built and used
needs its own record. The risks are organised with the AI Risk Management Framework of the National Institute of Standards and Technology (NIST), whose four functions are govern, map,
measure and manage [38], and the brief names leakage, overfitting, causal overclaim, unfairness and high-stakes
automation as the risks to review [1]. Table 5.1 gives the Risk and Ethics Notes; the full register of sixteen risks,
each with its control, check and residual level, is in Appendix VI (Table A.17).

**Table 5.1. Risk and Ethics Notes**

| Area | Main risk in this project | Control | Section |
| :---- | :---- | :---- | :---- |
| Leakage | Information from after the cut-off or from the test runs reaching the model | Dated predictors; refitting inside folds; single logged test | 5.1 |
| Overfitting and test reuse | Optimistic fold scores; choosing a favourable test variant | Nested tuning; margin fixed in advance; one declared gate | 5.1 |
| Interpretability | Reasons that do not match the ranking; partial effects read as weights | Reasons from the scoring model; adjusted and unadjusted estimates together | 5.1 |
| Causal limits | Reading the list as proof that contact helps | No effect claim; randomised pilot before any benefit ranking | 5.2 |
| Fairness | Lower recall for disabled or deprived students; proxies | Separation as primary criterion; confirmatory check; proxy check | 5.2 |
| High-stakes use | Automation bias; labelling; legal duties at the university | Tutor decides and can override; flags expire; risk classification under Vietnamese AI law before a pilot | 5.2 |
| Data constraints | 9 training runs; module CCC unseen; British distance learning of 2013–2014 | Run-level split; module CCC reported separately; local validation before use | 5.1 |
