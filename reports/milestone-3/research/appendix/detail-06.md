**Before-and-after checks explained.** The paragraphs below explain two results of Table 7.1 and the checks beyond it.

Two results need a word of explanation. The number of enrolments without a click row rises from 3,365 in the raw data
to 3,554 in the prepared view, because clicks after withdrawal are left out, so 189 students whose only activity came
after they unregistered now show none. The leakage check is built so that it can fail: if a feature used any click
after its cut-off, the feature would equal an unfiltered recount for every student, and the check would find no
difference for the students who clicked later.

Beyond the recount of every feature row, nine unit tests on synthetic test enrolments confirm each formula, and one
row was recounted by hand from the raw files: a TMA due on day 19 and submitted on day 24, with 168 clicks over 10
active days by day 27, matches the prepared view.

Table A.19 gives the state of each of the six conditions that the brief sets for starting Milestone 4.

**Table A.19. Entry conditions for Milestone 4**

| Condition | State |
| :---- | :---- |
| Core AQs have a prepared view with clear traceability | AQ1–AQ3 views ready; AQ4 ranking view ready, with the action part deferred (Appendix IV) |
| Target, features and dimensions stable | Defined in the feature specification and the data dictionary; 9 of 9 formula tests pass |
| Leakage and split defined for predictive tasks | Split and leakage specification; V11–V13 and V15 pass |
| Important quality issues handled or kept on purpose | DQ01–DQ19 each with a decision; residual risks stated (Section 7.3) |
| No synthetic data as evidence | Only labelled level A test enrolments |
| Prepared data reproducible from raw | Two runs from the raw files; 8 of 8 data files identical |
