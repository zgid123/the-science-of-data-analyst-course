# 6. Data Understanding and Data Quality

Before any question is answered, the data must be understood well enough to know which of their features could change
a conclusion. In Milestone 3 we profiled all 10.9 million rows of the seven raw tables, and thirteen figures of that profile were recounted independently, all thirteen in agreement (Appendix VI). Non-completion joins Fail and Withdrawn, as the
primary KPI does, while AQ1 reports them apart. Of the 28,061 enrolments of all 22 runs registered at day 14, 54.7% completed;
non-completion is 45.3% at day 13 and 44.2% at day 27, and 24.9–58.3% between the 22 runs, so the classes are close in size and
no resampling is needed. The mix differs by module: withdrawal is highest in the CCC runs, at 43–46%, while GGG
has the fewest withdrawals but the most failures. Activity is strongly skewed, with a median of 602 clicks and 3,365 enrolments without any, so
counts enter models as logarithms and no value is removed. Model development uses the 9 runs of 2013 and keeps the
13 runs of 2014 for a single test, while AQ1 and AQ2 describe both years (C15); Table 6.1 gives the populations that every
later number refers to.

**Table 6.1. Populations of the 2013 development runs and the 2014 test runs**

| Population | Enrolments | Non-completers | Used by |
| :---- | :---- | :---- | :---- |
| All 2013 enrolments (9 runs) | 13,529 | 6,959 (51.4%) | AQ1, second denominator |
| 2013, registered at day 14 | 12,076 | 5,515 (45.7%) | AQ1, primary denominator |
| 2013, registered at day 13 | 12,080 | 5,519 | AQ3 development, day 13 |
| 2013, registered at day 27 | 11,811 | 5,245 (44.4%) | AQ2; AQ3 development, day 27 |
| 2013, day 27, 7 runs with a task due | 9,960 | – | AQ2 task-based signs |
| 2014, registered at day 14 | 15,985 | 7,185 (44.9%) | AQ1, primary denominator |
| 2014 test (13 runs), day 13 and day 27 | 15,989 and 15,724 | day 27: 6,911 (44.0%) | AQ2 replication; AQ3 and AQ4 test |
