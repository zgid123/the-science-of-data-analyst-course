## 4.4. Error, Subgroup and Fairness Analysis

Building on the criteria of Section 4.3, the frozen model is evaluated separately for each audit group, because
aggregate metrics can hide differences between groups [34], and TRIPOD+AI asks for subgroup estimates with intervals
and for the approach used to address fairness [21]. When non-completion rates differ between groups, equal positive
predictive value rules out equal error rates [35], so one criterion must lead: separation, measured as equal recall at
capacity, which is recommended for dropout prediction that allocates extra support [36] and matches a contact whose
main harm is missing a struggling student.

The confirmatory check covers the three groups that AQ4 names and that hold at least 400 test enrolments: students
with a declared disability (1,488 at day 27), the most deprived band, 0–10% (1,486) and the missing deprivation band (610). Rule F1 of Table 4.2 flags a group for review; at the training non-completion rates even the lowest-rate eligible group, the missing band (28%), holds more than 100 non-completers. Students aged 55 or over (118 test enrolments, below the 400 threshold) are reported as a point gap, "insufficient data, not cleared". On OULAD, most published at-risk models reproduced and slightly amplified a gap in favour of male students and showed
erratic bias for students with a declared disability (author-reported) [37], and leaving attributes out does not make
a model blind to them [36], so a proxy check compares scores and predictors across groups. The absolute between-ROC area (ABROCA),
the area between a group's ROC curve and that of the rest [34], stays descriptive, and the error
analysis by run, activity, history, reach and kind of non-completion is specified in Appendix V.
