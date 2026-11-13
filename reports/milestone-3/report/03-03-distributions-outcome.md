## 3.3. Distributions, Outliers and Outcome Balance

Activity is strongly skewed: per enrolment the median is 602 clicks, 3,365 enrolments have none, 2,503 lie beyond the
upper fence of the interquartile range, the usual statistical boundary for an outlier, and a single click record
reaches 6,977 clicks; these are heavy users rather than errors, so no value is removed or capped, and models sensitive
to scale receive the logarithm of the counts instead (DQ16). The two outcome classes are close in size. Of the 28,061
enrolments registered by day 14 and not unregistered by it, the KPI population, 54.7% completed, a value of OULAD that
is not the university's assumed baseline of 70%; non-completion reaches 45.3% among those enrolled at day 13 and 44.2%
at day 27, and the smaller class holds at least 92 enrolments in every run, so no resampling is needed. Figure 3.1
shows the final results of every run: withdrawal is highest in the CCC runs (43–46%), while GGG has the fewest
withdrawals but the most failures. Appendix I gives the full evidence of this section, including the distributions of
scores and study load.

![Figure 3.1. Final result of every enrolment, by module run](assets/figures/fig-3-1-outcomes.png)
