## 8.1. Prepared Views by Analytics Level

Each analytics level has its own prepared view, and each view adds to the one before it. The brief sets a check for
each level before Milestone 4: descriptive views must give summaries without double counting or join bias;
diagnostic views must compute associations from real data with comparison groups; predictive views must hold a
target, a prediction point, features from before that point, a split and enough cases of each class; and prescriptive
views need data on actions, constraints, costs and outcomes [1]. Appendix III (Table A.11) gives, for each level, the
prepared view, its population and grain, the check of the brief and its result; the paragraphs below state them.

The descriptive views, enrolment, assessment_due and student_week, give rates on the right denominator, because
every enrolment appears once and the populations of Section 4.1 are flags rather than filters; their keys are unique,
every join kept its rows and their clicks reconcile with the raw log. The diagnostic view, features_d27 with the
enrolment view, adds the signs at day 27 for the 27,535 enrolments enrolled then, so that their association with
non-completion can be compared within each of the seven modules. The predictive views, features_d13, features_d27
and the model-ready matrices, add a second cut-off at day 13, the time split into 9 training and 13 test runs and
transforms fitted on the training runs, with at least 92 enrolments in the smaller class of every run. The prescriptive table, capacity_by_run, supplies
only list sizes under assumed capacities, because the data hold no action, no cost and no outcome after a contact,
and the brief rules out turning a predictive result into a prescriptive one by advice [1].
