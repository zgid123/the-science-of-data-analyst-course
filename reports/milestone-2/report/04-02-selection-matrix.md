## 4.2. Selection Matrix and Rationale

**The matrix.** Table 4.1 applies the brief's selection matrix to the seven candidates, with scores from 0 to 2. The
brief's matrix has six criterion columns; two of them each pair two criteria (target and timing; documentation and
license), and we added one column that pairs the remaining two (unit and granularity; temporal coverage), so the
table shows all ten scores and their total out of 20. The last column gives the decision and, for each rejected
candidate, the gates it fails.

**Table 4.1. Dataset Selection Matrix**

| Candidate | AQ coverage | Population fit | Unit / temporal | Target / timing | Docs / license | Quality feasibility | Ethics / representativeness | Total (of 20) | Decision |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A OULAD | 1 | 1 | 2 / 1 | 1 / 1 | 1 / 2 | 1 | 1 | 12 | Selected, on condition that Section 6 confirms three facts |
| B UCI 697 | 0 | 1 | 0 / 1 | 1 / 0 | 2 / 2 | 2 | 1 | 10 | Rejected: fails G1, G2a, G2b |
| C UCI 320 | 0 | 0 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 6 | Rejected: fails G1–G3 |
| D UCI 856 | 0 | 1 | 0 / 0 | 1 / 0 | 1 / 2 | 2 | 0 | 7 | Rejected: fails G1–G3 |
| E XuetangX | 1 | 1 | 1 / 1 | 1 / 1 | 1 / 0 | 1 | 0 | 8 | Rejected: fails G1, G2a, G4 |
| F HarvardX | 0 | 1 | 1 / 0 | 1 / 0 | 2 / 0 | 2 | 1 | 8 | Rejected: fails G1–G4 |
| G xAPI-Edu-Data | 0 | 0 | 0 / 0 | 1 / 0 | 0 / 1 | 2 | 0 | 4 | Rejected: fails G1–G3 |

**Why OULAD.** OULAD is selected because it is the only candidate whose documentation meets the timing and license
gates and records a dated withdrawal. It records a final result for each enrolment, including Withdrawal with the day
of unregistration [3]; dated assessments and the day of each submission; and the daily number of clicks of each
student on each page of the learning platform [3]. It is published under the Creative Commons Attribution 4.0 license
(CC BY 4.0), which allows academic use with attribution [2].

**Why not the others.** Every other candidate fails at least the outcome gate (G1) and the dated-task gate (G2a). UCI
697 labels students by their degree after three or four years, not by course, and holds only semester totals, so it
cannot show when within a course a student stopped [4], [5]. UCI 320 and UCI 856 describe secondary-school pupils or a
single questionnaire, with grades but no withdrawal and no dated tasks or activity [6], [7]. The XuetangX data record dated activity,
but their outcome is a yes-or-no dropout label without pass or fail, and they state no license [8]. HarvardX records
only the first and last activity of each learner and is not openly licensed [10], and xAPI-Edu-Data has no dated
records and is known only from a Kaggle listing [11].

**A modest total, made conditional.** OULAD's total of 12 out of 20 is modest because its documentation leaves several
facts open, and the scores count only what is documented. Documentation scores 1, for example, because the provider
page gives no version number and its download link was broken; only the figshare deposit carries a version. The selection was therefore made conditional on the files
confirming three facts: that the result values separate pass from fail (G1), that each module has enough runs for
testing (G3), and that a student's identifier stays the same across runs (G5). Section 6 confirms the first and the
third. It shows the second met for five of the seven modules, which keeps OULAD under the rule of Section 4.1 and
narrows AQ3 to those runs; the rejected candidates have a single period or no dates, so they miss the history gate
outright.

**Limits that come with the choice.** OULAD describes UK distance-learning modules from 2013–2014, and its modules were
selected by the publisher partly because many students failed them [3], so its failure and withdrawal rates are likely
to exceed those of a typical program. It holds no delivery mode, year of study, attendance, leave or transfer status.
Its authors also advise analysing module runs that start in February and in October separately [3], which limits how
many comparable runs each module has.

**No supplementary dataset.** The brief allows at most one supplementary dataset when it is really needed [1]. None is
selected: no candidate holds the missing contact, capacity or attendance data, and the only other source of dated
activity, the XuetangX data, lacks a license and a pass or fail outcome [8].
