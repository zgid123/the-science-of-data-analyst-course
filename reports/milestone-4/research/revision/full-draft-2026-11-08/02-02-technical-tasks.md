## 2.2. Technical Task Definitions

**Purpose first.** Building on the briefs of Section 2.1, the first test of each question is its purpose, because the
same regression can serve three different purposes. Explanatory modeling tests causal hypotheses; predictive modeling
forecasts new or future cases; and a regression used only to measure association, with neither a causal nor a
predictive aim, is descriptive in Shmueli's sense [3]. The brief places association analysis under diagnostic
questions and forbids reading it as cause [1], so AQ2 keeps the diagnostic level and its technical task is named
association. Prediction, unlike explanation, is judged on data the model has not seen [3], [5], which is why AQ3 and
AQ4 are evaluated on later runs (Section 4.2). Figure 2.1 maps each question to its technical task, its output and the
decision it serves.

![Figure 2.1. From AQ to technical task, output and decision](assets/figures/fig-2-1-aq-map.png){width=85%}

**AQ1 and AQ2.** AQ1 is aggregation: rates and shares grouped by module, run, start month and year, each with its
denominator and an interval. AQ2 is association within module run: how much more often students with a sign by day 27
fail to complete than comparable students of the same run without it.

**AQ3.** AQ3 is binary classification at two prediction points, the ends of day 13 and day 27. The target is known
only after the run ends, the model is trained on earlier runs and tested on a later one, and this arrangement mirrors
how the model would be used, on a run that is still in progress [6].

**AQ4.** AQ4 is ranking under a fixed capacity. When predictions are used to rank cases, the quality of the final
ranking matters more than the predicted values themselves [6], and studies that prioritise students for scarce
support evaluate the top of the list, where the decision falls [7]. Two other framings were considered. A
discrete-time survival model would add when a student leaves [8], but the listing decision (D1) acts at two fixed
cut-offs and needs no timing, so survival stays an extension. Ranking students by the expected benefit of contacting
them would need data on contacts and their outcomes, which OULAD does not hold [9], so AQ4 remains decision support,
and the choice of contact stays deferred to a pilot (Section 5.2).
