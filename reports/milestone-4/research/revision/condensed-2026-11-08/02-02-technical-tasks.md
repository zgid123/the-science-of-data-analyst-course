## 2.2. Technical Task Definitions

Building on the briefs of Section 2.1, the first test of each question is its purpose. Explanatory modeling tests
causal hypotheses, predictive modeling forecasts new or future cases, and a regression used only to measure
association, without a causal or predictive aim, is descriptive in Shmueli's sense [3]. The brief places such
analysis under diagnostic questions and forbids reading it as cause [1], so AQ2 keeps the diagnostic level and its
task is named association. Prediction, unlike explanation, is judged on held-out data [3], [5]. Figure 2.1 maps each question to its task, output and
decision.

![Figure 2.1. From AQ to technical task, output and decision](assets/figures/fig-2-1-aq-map.png){width=85%}

AQ3 is a binary classification at two prediction points, the ends of day 13 and day 27, with the target known only
after the run, trained on earlier runs and tested on a later one, which mirrors deployment [6]. AQ4 is a ranking under
a fixed capacity: when predictions are used to rank, the quality of the final ranking matters more than the predicted
value [6], and studies that prioritise students for scarce support evaluate the top of the list [7]. A discrete-time
survival model would add when a student leaves [8], but the listing decision (D1) acts at fixed cut-offs, so it stays an extension; ranking
by the expected benefit of contact needs contact data that OULAD does not hold [9], so AQ4 remains decision support
and the choice of contact stays deferred (Section 5.2).
