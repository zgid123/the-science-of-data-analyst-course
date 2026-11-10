## 7.1. Derived Variables, Encoding and Leakage Control

Every feature uses only records dated on or before its cut-off, so activity after it, the withdrawal day and the final
result never enter a feature, and TMA marks, which have no release day, are never used. The derived variables include
clicks before and after day 0, activity against the median of the same run, inactivity in the last seven days, missed
and late tasks, and the early-sign rule (Table A.18, Appendix VII). The primary set holds 19 usable predictors, 23
parameters once module and start month are coded; every transform is refitted inside each development fold, and module
terms are deviation-coded so that an unseen module receives the average effect. Leakage, the use of information that
would not exist at the moment of prediction, is blocked by the timing rule, by learning parameters on 2013 alone, by the
split by year and by flagging the 1,586 test enrolments at day 27 of students seen in 2013 (Table A.19). The date-filter
check can fail: without the filter, features change only for the enrolments that clicked after the cut-off.
