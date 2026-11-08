## 1.2. Prepared Data and Entry Gate

The prepared dataset OULAD-N04-prepared-1.0 holds one row per enrolment and two feature views, one for each cut-off at the end of day 13 (week 2) and day 27 (week 4). Each view keeps the enrolments still registered at its cut-off and only information dated on or before it, and the target non_completion is a final result of Fail or Withdrawn. Training uses the 9 runs of 2013, with
11,811 enrolments and 5,245 non-completers (44.4%) at day 27, and testing the 13 runs of 2014, whose 15,724 outcomes at day 27
stay unopened until the single final test (Appendix IV, Table A.14).

The brief admits a team to modeling only when five conditions hold [1]. Table 1.2 gives the evidence for each.

**Table 1.2. Entry gate**

| Condition | Evidence from Milestone 3 | Status |
| :---- | :---- | :---- |
| Approved AQs | AQ1–AQ3 ready; AQ4 as ranking, contact deferred (Change Log entries C11 and C13) | Met |
| Prepared dataset | OULAD-N04-prepared-1.0: dictionary, unit, keys, target, feature windows | Met |
| Leakage controls | Cut-offs at day 13 and 27; split by year; transforms fitted on 2013; 22 of 22 checks passed | Met |
| Known limitations | Quality issues DQ01–DQ19; audit attributes; representativeness and data protection | Met |
| Traceability | AQ → data requirement → raw and prepared variables | Met |

All five conditions hold, so the questions can be modelled as they stand, with the contact part of AQ4 left deferred.
One change to how AQ2 is measured follows from the evaluation design and is recorded as Change Log entry C14 (Section 4.2; Appendix
VIII).
