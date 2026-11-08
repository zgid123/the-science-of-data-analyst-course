# 5. Risk, Ethics and Limitations

The evaluation of Part 4 measures how well the methods work; what can go wrong when they are built and used needs its
own record. The brief names leakage, overfitting, causal overclaim, unfairness and high-stakes automation as the risks
to review [1]. The risks are organised with the AI Risk Management Framework of the
National Institute of Standards and Technology (NIST), whose four functions are govern, map, measure and manage [39]: deciding who is responsible,
identifying where each risk arises, checking whether a control works and acting on what remains.

**Risk and Ethics Notes.** Table 5.1 gives the Risk and Ethics Notes of the brief: for each area, the main risk in
this project, the control the proposal builds in and the section that treats it.

**Table 5.1. Risk and Ethics Notes**

| Area | Main risk in this project | Control | Section |
| :---- | :---- | :---- | :---- |
| Leakage | Information from after the cut-off or from the test runs reaching the model | Dated predictors; refitting inside folds; single logged test | 5.1 |
| Overfitting and test reuse | Optimistic fold scores; choosing a favourable test variant | Nested tuning; margin fixed in advance; one declared gate | 5.1 |
| Interpretability | Reasons that do not match the ranking; partial effects read as weights | Reasons from the scoring model; adjusted and unadjusted estimates together | 5.1 |
| Causal limits | Reading the list as proof that contact helps | No effect claim; randomised pilot before any benefit ranking | 5.2 |
| Fairness | Lower recall for disabled or deprived students; proxies | Separation as primary criterion; confirmatory check; proxy check | 5.2 |
| High-stakes use | Automation bias; labelling; legal duties at the university | Tutor decides and can override; flags expire with the run; risk classification under Vietnamese AI law before a pilot | 5.2 |
| Data constraints | 9 training runs; module CCC unseen; distance learning in the United Kingdom (UK) of 2013–2014 | Run-level split; module CCC reported separately; local validation before use | 5.1 |

**Risk register.** Appendix V (Table A.9) gives the full register of sixteen risks. Each row names where a risk arises in this
project, the control that the proposal builds in, the check that shows whether the control works, and the risk that
remains after the control.

Section 5.1 treats the risks to the validity of the evaluation, and Section 5.2 the risks of using the list on real
students.
