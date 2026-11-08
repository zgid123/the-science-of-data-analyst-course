## 3.3. Distributions, Outliers and Outcome Balance

**Activity.** Activity is strongly skewed. Per enrolment, the median is 602 clicks over the whole run, a quarter of
enrolments have 142 clicks or fewer and a quarter 1,585 or more, and 3,365 enrolments have none. The upper fence of
the interquartile range, the usual statistical boundary for an outlier (the third quartile plus one and a half times
the distance between the first and third quartiles), lies at 3,750 clicks, and 2,503 enrolments lie beyond it; a
single record of one student on one resource on one day reaches 6,977 clicks. These students are heavy users of the
platform rather than errors in the data, since nothing in the records marks their activity as false, so no value is
removed or capped (DQ16). Because a few students carry a large share of all clicks, models that are sensitive to
scale receive the logarithm of the counts instead (Section 6.2).

**Scores and study load.** Scores lean the other way: the median is 80 and a quarter of scores reach 90 or more. In
addition, 45.8% of CMA scores fall on a multiple of ten, against 17.4% of TMA scores, a sign that computer marking
moves in coarse steps. Study load reaches 655 credits, against a 99th percentile of 240; such students are taking many
modules at once, which is unusual but possible, so the value is kept.

**Outcome balance.** The brief asks whether the outcome is badly imbalanced and whether the smaller class has enough
cases [1]. The KPI population is the enrolments registered by day 14 and not unregistered by it, 28,061 enrolments, of
whom 54.7% completed. Non-completion reaches 45.3% among the enrolments still enrolled at day 13 and 44.2% among those
enrolled at day 27, so the two classes are close in size and no resampling is needed. Between runs, non-completion
ranges from 24.9% to 58.3%, and the smaller class holds at least 92 enrolments in every run, enough to estimate a rate
for each run. Figure 3.1 shows the final results of every run: withdrawal is highest in the CCC runs (43–46%), while
GGG has the fewest withdrawals but the most failures.

![Figure 3.1. Final result of every enrolment, by module run](assets/figures/fig-3-1-outcomes.png)
