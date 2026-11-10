# Full draft of Sections 11.2 and 11.3 before the move (T26, 2026-11-11)

The complete two-year text as written before the blocks listed in `02-aq1-aq2-both-years.md` ("Write full, then move") moved to Appendices XII and XIII. Kept here because the draft was not committed (the user did not ask for a snapshot commit); English pessimistic length with this text: 27.0 pages.

## `11-02-aq1-findings.md`

````markdown
## 11.2. AQ1: Completion and Timing of Non-completion

We computed AQ1 on all 22 runs, 2013 and 2014 apart and pooled, with the enrolments still registered at day 14 as
primary denominator, all enrolments as second denominator and Wilson intervals for rates (C15). The success criterion
is met in both years: the prepared views and the raw tables agree in all 176 outcome cells, the first missed week
agrees for all 32,593 enrolments, and the 2014 counts equal those Milestone 3 published (Appendix XII).

Of the 28,061 enrolments registered at day 14, 45.3% (44.7–45.8) did not complete, 45.7% (44.8–46.6) of 12,076 in
2013 and 44.9% (44.2–45.7) of 15,985 in 2014, a quarter failing and a fifth withdrawing (Table A.29). Over all
enrolments the rate rises to 51.4% in 2013 and 53.8% in 2014, because most enrolments outside the day-14 population
ended as withdrawals. Non-completion ranges from 26.3% in module AAA to 54.3% in CCC, which ran only in 2014; among the
six modules that ran in both years, AAA has the lowest and DDD the highest rate in each year, and February runs exceed
October runs in both years, 51.6% against 42.4% in 2013 and 49.6% against 41.6% in 2014 (Table A.30). Modules also
differ in how students leave: in GGG most non-completers fail, while in CCC 33.1% of the day-14 population withdrew.

The run rates span from 24.9% (AAA 2013J) to 58.3% (CCC 2014B), and the denominator alone moves a run's rate outside
its interval in 7 of 9 runs of 2013 and 10 of 13 of 2014, by up to 13.6 points (BBB 2014J), so the KPI fixes the
add-drop rule. The year comparison shows why: over all enrolments non-completion was 2.3 points higher in 2014 (1.2 to
3.4), a rise that comes from module CCC, but among students registered at day 14 it was 0.7 points lower (−1.9 to 0.5),
and 3.5 lower (−4.8 to −2.3) in the six modules run in both years, because 16.2% of 2014 enrolments against 10.7% of
2013 were not registered at day 14 (Table A.32).

Of the non-completers, 78.1% (2013) and 72.7% (2014) missed a TMA or CMA during the run, against about one in five
completers, but only 19.6% and 14.7% had missed one by week 4, and the median first missed week is 9 in both years
(Table A.31). Part of the lower 2014 share comes from the EEE and GGG runs, where no task falls due by day 27 and which
held 16.7% of the 2014 non-completers against 11.9% in 2013. A rule on tasks alone therefore comes too late for most
non-completers, which is why the early-sign rule counts inactivity. Students with a declared disability and those in
the most deprived band did not complete more often in both years, which the AQ4 fairness audit carries forward.

The answer has high confidence for OULAD 2013–2014: two independent computations agree in each year, while validity for
the university's courses remains open. It gives D2 a hypothesis on where support time would go first, to be checked on
the university's records. Figure 11.1 shows the rate of each module in each year.

![Figure 11.1. Non-completion per module in 2013 and 2014, students registered at day 14, with 95% Wilson intervals; dashed line: pooled rate of the 22 runs, 45.3% (12,700 of 28,061)](assets/figures/fig-11-1-aq1-rates.png){width=100%}
````

## `11-03-aq2-findings.md`

````markdown
## 11.3. AQ2: Early Signs Associated with Non-completion

We estimated AQ2 on the 11,811 enrolments of 2013 registered at day 27 (44.4% non-completion) and replicated it on the
15,724 of 2014 (44.0%), including module CCC, with a logistic regression with run fixed effects, background terms and
sign × module terms; the task signs are defined in the runs with a task due by day 27 (9,960 enrolments in 2013, 12,585
in 2014). Each estimate is an average risk difference in percentage points, an association and never an effect of the
sign [10] (Appendix XIII).

All five signs meet the criterion of a consistent association in both years (Table A.33): a missed task goes with 40.8
more points of non-completion in 2013 (37.7–43.9) and 39.3 in 2014 (36.4–42.1), a late TMA with 20.2 and 20.3, no
click in the last seven days with 14.5 and 15.8, activity below the run median with 13.4 and 14.6 and no click before
the start with 10.6 and 8.7. No sign moves by more than two points between the years, every difference has an interval
including 0, and pooled over the 22 runs the five signs go with 39.8, 20.6, 14.7, 14.0 and 9.4 points. The click signs
lose about half of their unadjusted size once the other signs enter, because they describe partly the same students.

Each sign keeps its direction in every module and under six sensitivity runs in both years, with one exception: a late
TMA in AAA 2014, −1.2 points on 348 enrolments, whose interval (−14.4 to 12.1) includes 0; no CCC student had submitted
a TMA late by day 27 (Tables A.34, A.35). Most module intervals that include 0 lie in the small module AAA. The binary
click signs miss part of a graded activity gradient in both years (Table A.36): with clicks added as a continuous
adjustment, the misfit disappears in 2013 and shrinks in 2014, and activity below the run median falls to 5.8 points in
2013 and 5.9 in 2014, where it keeps its direction in only 4 of 7 modules and no longer meets the criterion, while the
other four signs still do.

The several-modules sign marks 28 of the 15,724 enrolments of 2014, 27 of them non-completers, too few to change a list
(C12). Within groups of gender, disability and deprivation band, the missed-task sign keeps a clear association in
every group that could be modelled in both years. Confidence is moderate: two years agree, but the click signs rest on
a known misfit and associations that unrecorded reasons could explain. The signs give each name on a D1 list a factual
reason, while contact based on them stays an option to test. Figure 11.2 shows the five signs, mutually adjusted, in
each year.

![Figure 11.2. Mutually adjusted risk difference in later non-completion between enrolments with and without each early sign at day 27, 2013 and 2014, with 95% intervals; task signs: runs with a task due by day 27 (n = 9,960 and 12,585); click signs: all runs (n = 11,811 and 15,724)](assets/figures/fig-11-2-aq2-associations.png){width=100%}
````
