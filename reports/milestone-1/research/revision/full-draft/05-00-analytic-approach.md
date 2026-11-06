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

The descriptive and diagnostic questions use the simplest families that answer them. AQ1 needs counts and rates broken
down by course, mode and year of study, and a comparison of timing between two groups. AQ2 compares the later
non-completion rate of students with and without each sign. Explanatory regression lets the team see whether a sign
still differs once other signs are taken into account, for example whether missed tasks matter beyond low LMS
activity. AQ2 reports differences, not causes, because the records are observational: they show what students did,
not why they did it, and the brief warns against causal language without a causal design [1].

The predictive question is judged against a simple rule. In the blended course described in Section 1.1,
continuous-assessment results such as quizzes and assignments were the strongest early predictor [8], so a rule that
simply counts missed tasks is a demanding standard. A classification method earns its place only if it reaches more
of the students who later fail or withdraw than the rule does on a list of the same length. Validation is
time-based: the method learns from earlier semesters and is tested on a later one, as it would be used in practice.
Courses that have no earlier semesters can use methods that learn from the current course's own submitted
assessments [20]. Survival analysis, which models the time until an event such as withdrawal, is a candidate for the
withdrawal part of the target.

The prescriptive question turns the AQ3 ordering into a list that staff can act on. Decision rules cut the ordering at
the length that capacity allows, apply the precision and fairness limits, and route each student to the lecturer,
the lecturer-advisor or the support office. What-if analysis shows how the limits change the list, for example how
many more non-completers a list of 40 names would reach than a list of 30. Each name carries its reason as an observed
fact, such as two quizzes missed since week 2, because staff said that a score without a reason would be ignored
(VCL3, PM9).
