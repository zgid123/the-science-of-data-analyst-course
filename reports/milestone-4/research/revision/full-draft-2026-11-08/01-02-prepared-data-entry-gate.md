## 1.2. Prepared Data and Entry Gate

**Prepared data.** The prepared dataset OULAD-N04-prepared-1.0 of Milestone 3 holds one row per enrolment and two
feature views, one for each cut-off: the end of day 13 (week 2) and the end of day 27 (week 4). A feature view keeps
only the enrolments still registered at its cut-off and only information dated on or before that day, so nothing a
model reads could not have been known when the list was drawn. The target, non_completion, is a final result of Fail
or Withdrawn, recorded when the run ends. The data are split by year: the 9 runs of 2013 are for development and the
13 runs of 2014 for the final test. At day 27 the development runs hold 11,811 enrolments, of whom 5,245 (44.4%) did
not complete, and the test runs hold 15,724 enrolments; at day 13 the figures are 12,080 enrolments with 5,519
non-completers, and 15,989 test enrolments. The outcomes of the test runs stay unopened until a single final test
(Section 4.2), so that no choice in this proposal can be shaped by them.

**Entry gate.** The brief admits a team to modeling only when five conditions hold: the questions are approved after
the AQ–Data Fit, the prepared dataset has a version, a dictionary, a unit of analysis, keys, a target and feature
windows, leakage controls are set for prediction, the known limitations are recorded, and the chain from question to
prepared data is traced [1]. Table 1.2 gives the evidence for each condition.

**Table 1.2. Entry gate**

| Condition | Evidence from Milestone 3 | Status |
| :---- | :---- | :---- |
| Approved AQs | AQ1–AQ3 ready; AQ4 as a ranking, with the choice of contact deferred (C11, C13) | Met |
| Prepared dataset | OULAD-N04-prepared-1.0 with data dictionary, unit (the enrolment), keys, target and feature windows | Met |
| Leakage controls | Cut-offs at day 13 and day 27; split by year; transforms fitted on the 2013 runs only; 22 of 22 validation checks passed | Met |
| Known limitations | Quality issues DQ01–DQ19 each with a decision; audit attributes kept; representativeness and data protection stated | Met |
| Traceability | Question → data requirement → raw variables → prepared variables and views | Met |

All five conditions hold, so the questions can be modelled as they stand, with the contact part of AQ4 left deferred.
One further change to how a question is measured follows from the evaluation design of this milestone: AQ2 is
estimated on the 2013 runs and replicated on the 2014 runs only after the AQ3 test, so that no test outcome is seen
while the predictive model is chosen. It is recorded as Change Log entry C14 (Section 4.2).
