# 5. Proposed Analytic Approach

The four questions of Section 4 call for different kinds of analysis. At this milestone the proposal names the family
of techniques likely to fit each question, not a final algorithm; the specific methods are chosen in later milestones,
once the data have been audited [1]. Table 5.1 matches each question to its analytics type, its candidate technique
family, the expected output and the person who uses it.

**Table 5.1. Analytics type, candidate technique family and expected output per question**

| AQ | Analytics type | Candidate technique family | Expected output | Main user |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Rates, distributions, segmentation by course and group, trends over semesters; repeated after the pilot for pilot and comparison courses | A profile of completion by course and student group; a timeline of when non-completers first miss a task | Program manager |
| AQ2 | Diagnostic | Group comparison, association measures and statistical tests, explanatory regression, comparison of cohorts | Early signs ranked by their association with non-completion, with a check of whether the ranking holds across courses and groups | Program manager, lecturers |
| AQ3 | Predictive | Classification with time-based validation, compared against a simple rule; survival analysis of the time to withdrawal | An estimated likelihood of not completing for each enrolment at weeks 3 and 5, with recall and precision by group | Data Analytics Team |
| AQ4 | Prescriptive | Decision rules, prioritisation under capacity, routing between offices, what-if analysis of list length and limits | An ordered list for each review point, with a factual reason and a suggested contact for each name | Lecturer-advisors, support office |

Three choices shape the approach. AQ2 reports differences, not causes, because the records are observational and the
brief warns against causal language without a causal design [1]. AQ3 is
judged against a simple rule that counts missed tasks, because continuous-assessment results were the strongest early
predictor in the blended course described in Section 1.1 [8]; a classification method earns its place only if it
reaches more later non-completers than the rule on a list of the same length, tested on a later semester than the one
it learned from. Courses with no earlier semesters can use methods that learn from the current course's own submitted
assessments [20]. AQ4 shows each reason as an observed fact, such as two quizzes missed since week 2, because staff said
that a score without a reason would be ignored (VCL3, PM9). Appendix IX explains the choice of each technique family
in more detail.
