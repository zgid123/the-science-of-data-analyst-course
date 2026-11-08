## Appendix VI – Risk Register

The register follows the four functions of the NIST AI Risk Management Framework, which organises risk work as
govern, map, measure and manage [38]. Each row names where a risk arises in this project, the control that the
proposal builds in, the check that shows whether the control works, and the risk that remains. Table A.17 lists the
sixteen risks.

**Table A.17. Risk register**

| # | Risk | Where it arises | Control | Check | Residual |
| :---- | :---- | :---- | :---- | :---- | :---- |
| R1 | Target leakage | A predictor that carries information from after the cut-off | Predictors dated on or before the cut-off; target-derived flags outside the predictor list (Milestone 3) | Predictor legitimacy at the time of use [40]; validation of the prepared views | Low |
| R2 | Train–test contamination | Preprocessing or tuning that sees validation or test rows | Refit inside each fold; one test scoring after the second freeze | Logged test access [30]; pipeline review [22] | Low |
| R3 | Selection bias in model choice | The chosen configuration's fold score is optimistic | Nested tuning; choice by a margin fixed in advance; fold results never reported as performance | Fold-level results kept for the record [28] | Low to medium |
| R4 | Shift between years and to the university | 2014 runs differ from 2013; UK distance learning differs from a Vietnamese programme | Temporal test; paired and unpaired runs apart; local validation before any use | Per-run metrics; a failed calibration check leads to ranks only, recalibration on a later run [31] | Medium |
| R5 | Unseen module | Module CCC appears only in 2014 | Module terms as deviations; unseen module scored with the average | CCC runs reported apart | Medium for CCC |
| R6 | Few-cluster inference | 13 test runs of unequal size | Paired two-level bootstrap with a sign-flip test; per-run results | Wins, ties and losses reported | Medium |
| R7 | Selective reporting | Many test variants | One primary comparison declared; variants cannot change the verdict | First and second freeze records [30] | Low |
| R8 | Run list versus tutor capacity | One run-wide list stands in for tutors' lists | Capacity expressed as a share of the run; limitation stated | Tutor-level check in the pilot | Medium |
| R9 | Misreading coefficients as causes | AQ2 estimates and AQ3 reasons read as effects | Association wording rule with a text review; unadjusted and adjusted estimates side by side | Review of all result wording against the brief | Low |
| R10 | Claiming that contact works | The list read as proof that contacting helps | No effect claim; randomised pilot proposed [43] | Wording review of tutor materials before the pilot | Medium until a pilot |
| R11 | Unequal errors across groups | Lower recall for disabled, deprived or older students | Separation as primary criterion; confirmatory check (Appendix V) | Shortfall rule of Table A.16 | Medium for small groups |
| R12 | Proxies for excluded attributes | Activity, history or credits carry group information | Proxy check by group | Score and predictor means by group | Medium |
| R13 | Automation bias | Tutors follow the list without judgement | Tutor decides; can override any entry; reasons shown [46] | Scripted tutor walk-through before the pilot; overrides recorded | Medium |
| R14 | Labelling and stereotyping | A flag that follows a student | Flags lead to support and expire with the run [44] | Review of list use [45] | Medium |
| R15 | Feedback after deployment | Contacts change the outcomes the next model learns from | Contacts logged with outcomes before any retraining [51] | Monitoring of later cohorts [38] | Medium |
| R16 | Legal status and privacy at the university | Ranking learners is listed as high-risk in Vietnam [49]; university records are personal data [50] | Pilot only after risk classification and the duties of the AI law [48]; OULAD never linked to other data | Conformity assessment before use [48]; data protection review | Depends on the university |
