## 3.4. Ranking under Capacity

**The list.** AQ4 uses the AQ3 scores of Section 3.3 to form one list per module run, whose length k follows the
assumed capacity: 3 or 5 contacts per tutor group, with a tutor group assumed to hold 20 students, that is 15% or 25%
of the enrolments registered at the cut-off. OULAD records no tutor group, so one list per run stands in for the
tutors' lists. The list is judged by its top, where the ranking matters for the decision [6], [7]. Its baselines are a
random list, whose expected recall equals k/n, the list length over the run's size, and the rule-ranked list of the
same length. Risk tiers, a first tier of the top 3 per 20 and a second of the next 2 per 20, are the candidate form
for tutors who want a lighter second contact; both cut points come from capacity, not from the test data.

**What tutors see.** The list gives tutors ranks and each student's main contributing signs, and shows probabilities
only when calibration holds (Section 4.3). The tutor decides whom to contact, using knowledge that the data do not
hold [11].

**A ranking by benefit is rejected.** Ranking students by the expected benefit of a contact is rejected, because
estimating how the effect of an intervention varies between people needs randomised or otherwise unconfounded data on
treatment [9], and in field experiments the customers at the highest predicted risk were not the best targets of an
intervention [20]. The assumption that the order of risk matches the order of need therefore stays untested until a
randomised pilot (Section 5.2). Table 3.4 compares the AQ4 baselines and candidates against the eight criteria.

**Table 3.4. AQ4 candidates against the eight criteria**

| Criterion | Baseline 1: random list | Baseline 2: rule-ranked list | Candidate 1: top-k by AQ3 score (primary) | Candidate 2: risk tiers | Rejected: benefit (uplift) ranking |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Fit to question | Chance level | List from the number of signs, ties broken by lower relative activity | The k enrolments with the highest risk per run, k from capacity | First tier the top 3 per 20, second tier the next 2 per 20, both fixed from capacity | Ranks by expected benefit of contact |
| Fit to data | – | Rule known at each cut-off | k = 3 or 5 per 20 enrolled | Same scores | No contact or treatment variable in the data [9] |
| Assumptions | – | Signs equally weighted | Risk order matches need: untested | Same | Randomised or unconfounded treatment [9] |
| Interpretability | – | High | Score and reasons | High | Low |
| Complexity vs baseline | – | – | Uses AQ3 scores only | Same | Needs an experiment first |
| Robustness | – | Exact | As AQ3 | As AQ3 | – |
| Ethics and fairness | Audit | Audit | Confirmatory audit of recall at capacity by group (Appendix V) | Same | – |
| Actionability | – | Direct | Tutor decides on the list; ranks and reasons, probabilities only if calibrated | Adds a second tier for lighter contact | Not available |
