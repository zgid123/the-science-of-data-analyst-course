## 4.4. Error, Subgroup and Fairness Analysis

**Why groups are checked separately.** Building on the criteria of Section 4.3, the frozen model is evaluated
separately for each audit group, because aggregate metrics can hide differences between groups, an approach known as
slicing analysis [34]; TRIPOD+AI likewise asks for estimates by subgroup with intervals and for the approach used to
address fairness [21]. Gender, disability, deprivation band and age band stay out of the predictors and serve only the
audit, because leaving them out does not make a model blind to them: activity, previous attempts or credits can carry
the same information [35].

**One criterion must lead.** Fairness criteria cannot all hold at once when non-completion rates differ between
groups: a score with equal positive predictive value across groups cannot also have equal error rates [36], and
calibration within groups and balanced error rates conflict except in degenerate cases (perfect prediction or equal base rates across groups) [37]. The audit therefore names
one primary criterion, separation, measured as equal recall at capacity across groups. Separation is recommended for
dropout prediction that allocates extra support [35], and it matches a contact whose main harm is missing a student
who struggles.

**The audit groups.** The confirmatory check covers the three groups that AQ4 names and that hold at least 400 test
enrolments: students with a declared disability (1,488 at day 27), the most deprived band, 0–10% (1,486), and the
missing deprivation band (610). At the training non-completion rates even the lowest-rate eligible group, the missing
band (28%), holds more than 100 non-completers. The two numbers rest on one calculation: with about 100 non-completers in a group,
the standard error of a recall near 0.5 is about 5 percentage points, and the rest of the students are many times more numerous, so their recall has a much smaller standard error and the
group's recall is the main source of uncertainty in the gap; the gap of 10 points in rule FR1 is therefore about two
standard errors of the group's recall. In addition, 400 enrolments at the lowest group rate of 28% give about 112
non-completers (400 × 28%), above 100. Students aged 55 or over (118 test enrolments, below the threshold of
400) are reported as a point gap, marked "insufficient data, not cleared". Appendix IV (Table A.7) gives each group's size and
how it is handled; eligibility is fixed here from enrolment counts, before any test outcome is opened.

**The checks.** Rule FR1 of Table 4.5 flags a group for review; it does not reject the model, because a flag calls for
human judgement on why the gap arises. Earlier work on OULAD found that most published at-risk models reproduced and
slightly amplified a gap in favour of male students and showed erratic bias for students with a declared disability
(author-reported) [38], which is why the small groups are pooled over runs and reported with intervals. A proxy check
compares scores and predictors across groups, to show which predictors carry group information. The 
absolute between-ROC area (ABROCA), the area between a group's ROC curve and that of the other students [34], stays
descriptive, because it measures differences across all thresholds rather than at the capacity where the decision is
made. Appendix IV (Table A.8) lists every fairness and error check: the confirmatory check of separation, and descriptive
checks of selection, precision and calibration by group, the threshold-free gap in discrimination (ABROCA), the proxy check, errors by run,
activity, history and kind of non-completion, and the stability of the list.

