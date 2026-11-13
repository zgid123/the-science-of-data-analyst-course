# Log: 14b_headlines

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:34:33Z |
| Finished (UTC) | 2026-11-13T10:34:34Z |
| Duration | 0.5 s |
| Command | `../../venv/bin/python code/14_headlines.py` |
| Exit status | 0 |

## Console output

```text
wrote results/headlines.csv (29 rows)
                       name      value                                                                                 formula
                     nc_all 17208.0000                                              non-completers among all 32,593 enrolments
      share_gone_before_d14     0.2590                                             withdrew before day 14 / all non-completers
          share_gone_d14_27     0.0334                                                withdrew days 14–27 / all non-completers
  share_reachable_after_d27     0.7022                                   (withdrew after day 27 + failed) / all non-completers
           share_fail_of_nc     0.4098                                                             failed / all non-completers
           not_reg_d14_2013     0.1074                    share of 2013 enrolments (6 shared modules) not registered at day 14
           not_reg_d14_2014     0.1582                    share of 2014 enrolments (6 shared modules) not registered at day 14
         nc_normal_activity  4193.0000                        2014 non-completers at day 27 with clicks >= half the run median
   share_nc_normal_activity     0.6067                    normal-activity non-completers / all non-completers at day 27 (2014)
        recall_normal_model     0.1913                                       model recall among normal-activity non-completers
         recall_normal_rule     0.1565                                        rule recall among normal-activity non-completers
          recall_none_model     0.9844                               model recall among non-completers with no click by day 27
                  swap_size   903.0000                                      students on the model list only (= rule list only)
            rate_model_only     0.5969                                       non-completion of students on the model list only
             rate_rule_only     0.5061                                        non-completion of students on the rule list only
       model_only_with_sign     0.2126                                         share of model-only students with any rule sign
    model_only_prev_attempt     0.3068                                    share of model-only students with a previous attempt
     rule_only_prev_attempt     0.0642                                     share of rule-only students with a previous attempt
               tutor_groups   791.0000                            list places / 5 = tutor groups of 20 across the 13 test runs
       groups_per_extra_hit     9.6463                                tutor groups per extra non-completer listed by the model
   rule_share_of_model_hits     0.9714                                              rule hits / model hits at day 27, 5 per 20
      listed_withdrew_28_34   111.0000                                        listed non-completers who withdrew in days 28–34
       share_listed_nc_fail     0.5739                                listed non-completers who failed / listed non-completers
share_list_reason_education     0.1421                                  share of the list whose main reason is prior education
share_list_reason_behaviour     0.8071 share of the list whose main reason is low activity, a missed task or a late submission
                  m1_recall     0.4150                   share of all 2014 non-completers on the model lists, day 27, 5 per 20
               m1_precision     0.7252                                           share of listed students who did not complete
                  m1_missed  4043.0000                                                   non-completers not on the model lists
              m1_recall_d13     0.3856                                                        model recall at day 13, 5 per 20
```
