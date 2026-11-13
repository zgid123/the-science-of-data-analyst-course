## 3.4. Ranking under Capacity

**The list.** AQ4 uses the AQ3 scores of Section 3.3 to form one list per module run, whose length k follows the
assumed capacity: 3 or 5 contacts per tutor group, with a tutor group assumed to hold 20 students, that is 15% or 25%
of the enrolments registered at the cut-off. OULAD records no tutor group, so one list per run stands in for the
tutors' lists. The list is judged by its top, where the ranking matters for the decision [6], [7]. Its baselines are a
random list, whose expected recall equals k/n, the list length over the run's size, and the rule-ranked list of the
same length. Risk tiers, a first tier of the top 3 per 20 and a second of the next 2 per 20, are the candidate form
for tutors who want a lighter second contact; both cut points come from capacity, not from the test data. On the remaining criteria, the top-k list needs no fitting
of its own, so it is as robust and reproducible as the AQ3 scores; its untested assumption is that the order of risk
matches the order of need; and its fairness is checked by group at the same capacity (Section 4.4).

**What tutors see.** The list gives tutors ranks and each student's main contributing signs, and shows probabilities
only when calibration holds (Section 4.3). The tutor decides whom to contact, using knowledge that the data do not
hold [11].

**A ranking by benefit is rejected.** Ranking students by the expected benefit of a contact is rejected, because
estimating how the effect of an intervention varies between people needs randomised or otherwise unconfounded data on
treatment [9], and in field experiments on customer retention, the customers at the highest predicted risk were not the best targets of an
intervention [20]. The assumption that the order of risk matches the order of need therefore stays untested until a
randomised pilot (Section 5.2). Appendix I (Table A.7) compares the AQ4 baselines and candidates cell by cell against the eight criteria.

