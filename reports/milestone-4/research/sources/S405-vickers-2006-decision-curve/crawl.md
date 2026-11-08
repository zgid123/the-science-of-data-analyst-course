---
id: S405
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/
requested: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/
fetched: 2026-11-06T23:13+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T06
part: 4
raw: raw.html (161 KB)
conversion: html-text of https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/ (readable, 6720 words)
---
title: Decision curve analysis: a novel method for evaluating prediction models - PMC
        Lock
citation_abstract_html_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/
citation_author: Andrew J Vickers
citation_author: Elena B Elkin
citation_author_institution: Department of Epidemiology and Biostatistics, Memorial Sloan-Kettering Cancer Center, New York, NY
citation_author_institution: Department of Medicine, Memorial Sloan-Kettering Cancer Center, New York, NY
citation_author_institution: Department of Urology, Memorial Sloan-Kettering Cancer Center, New York, NY
citation_doi: 10.1177/0272989X06295361
citation_firstpage: 565
citation_fulltext_html_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/
citation_issue: 6
citation_journal_title: Medical decision making : an international journal of the Society for Medical Decision Making
citation_pdf_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577036/pdf/nihms74373.pdf
citation_pmid: 17099194
citation_publication_date: 2006
citation_title: Decision curve analysis: a novel method for evaluating prediction models
citation_volume: 26

Skip to main content

An official website of the United States government

Here's how you know

Official websites use .gov

A
.gov website belongs to an official
government organization in the United States.

Secure .gov websites use HTTPS

A lock (

) or https:// means you've safely
connected to the .gov website. Share sensitive
information only on official, secure websites.

-

Dashboard

-

Publications

-

Account settings

-

-
-
-

-

Journal List

-

User Guide

-

-

-

-

-

-

## PERMALINK

As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with,
the contents by NLM or the National Institutes of Health.

Learn more:
PMC Disclaimer
|

PMC Copyright Notice

. Author manuscript; available in PMC: 2008 Oct 31.

Published in final edited form as: Med Decis Making. 2006;26(6):565–574. doi: 10.1177/0272989X06295361

-
-
-
-

# Decision curve analysis: a novel method for evaluating prediction models

Andrew J Vickers

###
Andrew J Vickers, PhD

1 Department of Epidemiology and Biostatistics, Memorial Sloan-Kettering Cancer Center, New York, NY

2 Department of Urology, Memorial Sloan-Kettering Cancer Center, New York, NY

3 Department of Medicine, Memorial Sloan-Kettering Cancer Center, New York, NY

Find articles by Andrew J Vickers

1,2,3, Elena B Elkin

###
Elena B Elkin, PhD

1 Department of Epidemiology and Biostatistics, Memorial Sloan-Kettering Cancer Center, New York, NY

Find articles by Elena B Elkin

1

-

-

1 Department of Epidemiology and Biostatistics, Memorial Sloan-Kettering Cancer Center, New York, NY

2 Department of Urology, Memorial Sloan-Kettering Cancer Center, New York, NY

3 Department of Medicine, Memorial Sloan-Kettering Cancer Center, New York, NY

✉
Corresponding author: Andrew J. Vickers, PhD, 1275 York Ave., New York, NY 10021, tel: 212 639 6556, fax: 212 794 5851

PMC Copyright notice

PMCID: PMC2577036  NIHMSID: NIHMS74373  PMID: 17099194

The publisher's version of this article is available at Med Decis Making

## Abstract

### Background

Diagnostic and prognostic models are typically evaluated with measures of accuracy that do not address clinical consequences. Decision-analytic techniques allow assessment of clinical outcomes, but often require collection of additional information, and may be cumbersome to apply to models that yield a continuous result. We sought a method for evaluating and comparing prediction models that incorporates clinical consequences, requires only the dataset on which the models are tested, and can be applied to models that have either continuous or dichotomous results.

### Method

We describe decision curve analysis, a simple, novel method of evaluating predictive models. We start by assuming that the threshold probability of a disease or event at which a patient would opt for treatment is informative of how the patient weighs the relative harms of a false-positive and a false-negative prediction. This theoretical relationship is then used to derive the net benefit of the model across different threshold probabilities. Plotting net benefit against threshold probability yields the “decision curve”. We apply the method to models for the prediction of seminal vesicle invasion in prostate cancer patients. Decision curve analysis identified the range of threshold probabilities in which a model was of value, the magnitude of benefit, and which of several models was optimal.

### Conclusion

Decision curve analysis is a suitable method for evaluating alternative diagnostic and prognostic strategies that has advantages over other commonly used measures and techniques.

Keywords: prediction models, multivariate analysis, decision analysis

## Introduction

A typical prediction model provides the probability of an event, such as recurrence after surgery for prostate cancer, on the basis of a set of prognostic factors, such as cancer stage and grade1. Such models can be used to predict disease outcome, as in the case of cancer recurrence, or to make a diagnosis, such as whether a patient has appendicitis. Prediction models are usually evaluated by applying the model to a dataset and comparing the predictions of the model with actual patient outcome. Results are typically expressed as the area under the receiver operating characteristic (ROC) curve. The area under the curve (AUC) can be interpreted as the probability that in a pair of individuals, one who did and one who did not experience the event, the individual who experienced the event had the higher predicted probability. As such, it is commonly used as a single statistic to compare two or more prediction models2–4.

The AUC metric focuses solely on the predictive accuracy of a model. As such, it cannot tell us whether the model is worth using at all or which of two more models is preferable. This is because metrics that concern accuracy do not incorporate information on consequences. Take the case where a false-negative result is much more harmful than a false-positive result. A model that had a much greater specificity but slightly lower sensitivity than another would have a higher AUC, but would be a poorer choice for clinical use.

Decision-analytic methods incorporate consequences and, in theory, can tell us whether a model is worth using at all, or which of several alternative models should be used5. In a typical decision analysis, possible consequences of a clinical decision are identified and the expected outcomes of alternative clinical management strategies then simulated using estimates of the probability and sequelae of events in a hypothetical cohort of patients. Decision analysis requires explicit valuation of health outcomes, such as the number of complications prevented, life-years saved, or quality-adjusted life-years saved. In a decision analysis of alternative diagnostic or prognostic models, the optimal model is the one that maximizes the outcome of interest. Techniques have been proposed to simplify decision analyses of diagnostic and prognostic tests by using a risk/benefit ratio to summarize the health outcomes associated with the consequences of testing6.

There are two general problems associated with applying traditional decision-analytic methods to prediction models. First, they require data, such as on costs or quality-adjusted-life-years, not found in the validation data set, that is, the result of the model and the true disease state or outcome. This means that a prediction model cannot be evaluated in a decision analysis without further information being obtained. Moreover, decision-analytic methods often require explicit valuation of health states or risk-benefit ratios for a range of outcomes. Health state utilities, used in the quality-adjustment of expected survival7, are prone to a variety of systematic biases8 and may be burdensome to elicit from subjects. The second general problem is that decision analysis typically requires that the test or prediction model being evaluated give a binary result so that the rate of true- and false-positive and negative results can be estimated. Prediction models often provide a result in continuous form, such as the probability of an event from 0 to 100%. In order to evaluate such a model using decision-analytic methods, the analyst must dichotomize the continuous result at a given threshold, and potentially evaluate a wide range of such thresholds.

We sought a method for evaluating prediction models that incorporates consequences and so can be used to make decisions about whether to use a model at all or which of several models to use. We hoped to improve upon currently available techniques by developing a method that can be applied directly to a validation data set and does not require the collection of additional information. Moreover, we required a method that could be applied to a model regardless of whether it gave a binary or continuous result. Here we present a novel technique, decision curve analysis, which fulfills these criteria.

## Introductory Theory

Take the case of a patient deciding whether to undergo treatment for a specific disease. The patient is unsure whether or not disease is present. A simple decision-tree is given in figure 1: p is the probability of disease, and a, b, c and d give the value associated with each outcome in terms such as quality-adjusted life-years. Let us imagine that there is a prediction model available. This provides a probability that the patient has the disease: if the probability of disease is near one, the patient will ask to be treated; if the probability is near zero, he is likely to forgo treatment. At some probability between 0 and 1, the patient will be unsure whether or not to be treated. This threshold probability, pt, is where the expected benefit of treatment is equal to the expected benefit of avoiding treatment. Solving the decision tree:

| pta+(1−pt)b=ptc+(1−pt)d

### Figure 1. A decision tree for treatment.

Open in a new tab

The probability of disease is given by p; a, b, c and d give, respectively, the value of true positive, false positive, false negative and true negative.

By some simple algebra:

| pta−ptc=(1−pt)d−(1−pt)b=>pt(a−c)=(1−pt)(d−b)=>a−cd−b=1−ptpt
| (1)

Now d − b is the consequence of being treated unnecessarily. If treatment is guided by a prediction model, this is the harm associated with a false-positive result (compared to a true-negative result). Comparably, a − c is the consequence of avoiding treatment when it would have been of benefit, that is, the harm from a false-negative result (compared to a true-positive result). Equation 1 therefore tells us that the threshold probability at which a patient will opt for treatment is informative of how a patient weighs the relative harms of false-positive and false-negative results. In this formulation, “harm” is considered holistically, as the overall effect of all negative consequences of a particular decision.

Our formula has been described previously to derive an optimal threshold for an action such as using a drug or performing diagnostic test9, 10. In a typical example, Djulbegovic, Hozo and Lyman use data from randomized trial to estimate the benefit and harm of prophylactic treatment for deep vein thrombosis (DVT). They find that if a patient’s risk of DVT is 15% or more, he should be treated; if it is less than 15%, treatment should be avoided11. Our method allows this threshold to vary, depending on uncertainties associated with the likelihood of each outcome and differences between individuals as to how they value outcomes.

## Principal example

The example that we will use to illustrate our methodology comes from a prostate cancer study. Surgery for prostate cancer normally involves total removal of the seminal vesicles as well as the prostate, on the grounds that the tumor may invade the seminal vesicles. The presence of seminal vesicle invasion (SVI) can be observed prior to or during surgery only in rare cases of widespread disease. SVI is therefore typically diagnosed after surgery by pathologic examination of the surgical sample. It has recently been suggested that the likelihood of SVI can be predicted on the basis of information available before surgery, such as cancer stage, tumor grade, and prostate specific antigen (PSA)12. Although some surgeons will remove the seminal vesicles regardless of the predicted probability of SVI, others have argued that patients with a low predicted probability of SVI might be spared total removal of the seminal vesicles: most of the seminal vesicles would be dissected but the tip, which is in close proximity to several important nerves and blood vessels, would be preserved. According to this viewpoint, sparing the seminal vesicle tip might therefore reduce the risk of common side-effects of prostatectomy such as incontinence and impotence13. Previous investigators have published both binary decision rules12 and multivariable prediction models13 to help clinicians identify candidates for tip-sparing surgery. These investigators typically present metrics such as sensitivity, specificity or AUC to evaluate their models13. Accordingly, they are unable to tell us whether their model does more good than harm and therefore should actually be used. To demonstrate the use of decision curve analysis, we used data from an unpublished study of 902 men with prostate cancer who underwent prostatectomy and developed a multivariable model that gave the probability of SVI on the basis of stage, grade and PSA.

We use this example to illustrate Equation 1. Take the case of a surgeon who needs to decide whether to dissect or preserve the seminal vesicle tip in a man scheduled for prostatectomy. The surgeon suspects that total dissection may increase the risk of impotence or incontinence; however, preservation might increase the chance of a cancer recurrence if the patient had SVI and the tumor extended to the seminal vesicle tip. Imagine that the surgeon would definitely opt for total seminal vesicle dissection if the patient’s predicted risk of SVI were 30%, that preservation would be chosen if the risk were only 1%, but if the risk were 10%, the surgeon would be uncertain as to the correct approach. By equation 1, we infer that the surgeon feels that, for this patient, failing to remove the tip of a cancerous seminal vesicle (i.e. a false-negative result) is nine times worse than unnecessary tip dissection (i.e. a false-positive result).

## Application: Decision curve analysis

As it turns out, our method does not require that we obtain information regarding treatment preferences in this way. We use the theoretical relationship between the threshold probability of disease and the relative value of false-positive and false-negative results to ascertain the value of a prediction model. Take a group of patients scheduled for treatment by a surgeon who would be unsure whether to preserve or remove the seminal vesicle tip if the probability of SVI were 10%. We can now calculate each patient’s probability of SVI using the multivariable model, and class the result positive if it is equal to or higher than 10% and negative otherwise. Applying these results to the dataset yields the data shown in Table 1.

### Table 1.

Relationship between true seminal vesicle invasion (SVI) status and result of prediction model with a positivity criterion of 10% predicted probability of SVI.

|
|
| SVI

|
| n = 902
| Positive
| Negative

| Prediction Model: Probability of SVI ≥10%
| Yes
| 65
| 225

| No
| 22
| 590

Open in a new tab

To place a value on this result, we fix a −c, the value of a true-positive result, at 1. We thenobtain the value of a false-positive result, b − d, as - pt/(1− pt). We can now calculate net benefit using the following formula (first attributed to Peirce14):

| NetBenefit=TruePositiveCountn−FalsePositiveCountn(pt1−pt)

In this formula, true- and false-positive count is the number of patients with true- and false-positive results and n is the total number of patients. In short, we subtract the proportion of all patients who are false-positive from the proportion who are true-positive, weighting by the relative harm of a false-positive and a false-negative result. In table 1, where pt is 10%, the true-positive count is 65, the false-positive count is 225 and the total number of patients (n) is 902. The net benefit is therefore (65/902) – (225/902) × (0.1/0.9) = 0.0443. A good model will have a high net benefit: the theoretical range of net benefit is from negative infinity to the incidence of disease.

To determine whether this value is a good one, that is, whether the prediction model should be used for a pt of 10%, we need a comparison. The clinical alternative to using a prediction model is to assume that all patients are positive and treat them – as might be done for individuals possibly exposed to a dangerous infection easily treated with antibiotics – or assume that all patients are negative and offer no treatment, as is done for diseases for which there are no proven screening methods. The true- and false-positive count for considering all patients negative are both 0, and hence the net benefit for leaving the seminal vesicle tip in all patients is 0. Hence if the net benefit for the prediction model is positive, it is better to use the model than to assume that everyone is negative. The true- and false-positive count for the strategy of treating all patients are simply the number of patients with and without SVI respectively. Calculating net benefit gives: (87/902) − (815/902) × (0.1/0.9) = − 0.0039 for the strategy of removing seminal vesicles in all patients. This is less than the net benefit of 0.0443 from the prediction model.

At a pt of 10%, our prediction model is therefore better than both treating no one and treating everyone. However, patients differ as to how they rate possible side-effects of surgery. For example, a surgeon might be tempted treat more aggressively a man who was impotent but had many responsibilities. For such a man, the surgeon might use a much lower pt, say, 2%, that is, the seminal vesicle tip would be removed even if there was only a 2% chance of SVI. At this pt, the strategies of treating all men and treating using the model are almost identical (net benefit of 0.0780 and 0.0782 respectively). Similarly, there is a difference of opinion between surgeons regarding the increase in recurrence risk associated with preservation of the seminal tip in a patient with SVI: some surgeons feel that even if a patient has SVI, it is unlikely that the seminal vesicle tip will be involved and, even then, it is not clear that preservation will inevitably lead to recurrence; other surgeons feel that leaving any part of cancerous seminal vesicle will substantively increase recurrence rates. We therefore recommend repeating the above steps for different values of pt. Hence:

-
Chose a value for pt.

-
Calculate the number of true- and false-positive results using pt as the cut-point for determining a positive or negative result.

-
Calculate the net benefit of the prediction model.

-
Vary pt over an appropriate range and repeat steps 2 – 3.

-
Plot net benefit on the y axis against pt on the x axis.

-
Repeat steps 1 – 5 for each model under consideration.

-
Repeat steps 1 – 5 for the strategy of assuming all patients are positive

-
Draw a straight line parallel to the x-axis at y=0 representing the net benefit associated with the strategy of assuming that all patients are negative

Applying these steps to our data gives Figure 2. We term this a “decision curve”. Note that as expected, the two lines reflecting the strategies of “assume all patients have SVI” (i.e., treat all) and “assume no patients have SVI” (i.e., treat none) cross at the prevalence. Also note that the prediction model is comparable to the strategy of treat all at low pt and comparable to treat none at high pt. This is because the probability of SVI predicted by the model ranges from a minimum of 1.8% to a maximum of 84.3%. Using the model for pt < 1.8% or pt > 84.3% therefore gives the same result as treat all or treat none, respectively. Between 50% and 84.3%, the value of the model is sometimes negative: this is due to random noise.

### Figure 2. Decision curve for a model to predict seminal vesicle invasion (SVI) in patients with prostate cancer.

Open in a new tab

Solid line: Prediction model. Dotted line: assume all patients have SVI. Thin line: assume no patients have SVI. The graph gives the expected net benefit per patient relative to no seminal vesicle tip removal in any patient (“treat none”). The unit is the benefit associated with one SVI patient duly undergoing surgical excision of seminal vesicle tip.

In between these two extremes there is a range of pt where the prediction model is of value. In the case of SVI prediction this is between ~2% and ~50%. To determine whether the model is of clinical value, we need to consider the likely range of pt in the population, that is, the typical threshold probabilities of SVI at which surgeons would opt for complete dissection of seminal vesicles. If it were the case that all surgeons remove the seminal vesicle tip only if there was at least a 60 – 70% risk of SVI, the model clearly has no clinical role. But it is unlikely that any surgeon would consider removal of a healthy seminal vesicle tip to be worse than failing to remove a potentially cancerous one. If, on the other hand, we assume that the likely range of pt in the population is between 20% and 30%, we would use the model, because it is of clear benefit at these pt’s.

In consultation with clinicians, we estimate that although few if any surgeons would ever have a pt much above 10% for any patient, some may have pt approaching 1% or less in certain cases. This means that our prediction model will be of benefit in some, but not all cases. Where pt is less than 2%, the model is no better than a strategy of treating all patients. Hence where pt is less than 2% the model is of no value, and patients should have total seminal vesicle dissection. On the other hand, the model is never worse than the strategy of treating all patients, and because it is based on routinely collected data, it has no obvious downside. Therefore the model will be of use for clinicians who, at least some of the time, would opt for seminal vesicle tip preservation if a patient’s predicted probability of SVI was low.

If the prediction model required obtaining data from medical tests that were invasive, dangerous or involved expenditure of time, effort and money, we can use a slightly different formulation of net benefit:

| NetBenefit=TruePositiveCountn−FalsePositiveCountn(pt1−pt)−TestHarm

The harm from the test is a “holistic” estimate of the negative consequence of having to take the test (cost, inconvenience, medical harms and so on) in the units of a true-positive result. For example, if a clinician or a patient thought that missing a case of disease was 50 times worse than having to undergo testing, the test harm would be rated as 0.02. Test harm can also be thought of in terms of the number of patients a clinician would subject to the test to find one case of disease if the test were perfectly accurate.

If the test were harmful in any way, it is possible that the net benefit of testing would be very close to or less than the net benefit of the “treat all” strategy for some pt. In such cases we would recommend that the clinician have a careful discussion with the patient, and perhaps, if appropriate, implement a formal decision-analysis. In this sense, interpretation of a decision curve is comparable to interpretation of a clinical trial: if an intervention is of clear benefit, it should be used; if it is clearly ineffective, it should not be used; if its benefit is likely sufficient for some, but not all patients, a careful discussion with patients is indicated.

## Extensions of decision curve analysis

Decision curve analysis has two important additional advantages. First, the benefit of using a prediction model can be quantified in simple, clinically applicable terms. Table 2 gives the results of our analysis for pt’s between 1 and 10%. The net benefit of 0.062 at a pt of 5% can be interpreted in terms that use of the model, compared with assuming that all patients are negative, leads to the equivalent of a net 6.2 true-positive results per 100 patients without an increase in the number of false-positive results. In terms of our specific example, we can state that if we perform surgeries based on the prediction model, compared to tip preservation in all patients, the net consequence is equivalent to removing the tip of affected seminal vesicles in 6.2 patients per 100 and treating no unaffected patients. Moreover, at a pt of 5% the net benefit for the prediction model is 0.013 greater than assuming all patients are positive. We can use the net benefit formula to calculate that this is the equivalent of a net 0.013 × 100/(0.05/0.95) = 25 fewer false-positive results per 100 patients. In other words, use of the prediction model would lead to the equivalent of 25% fewer tip surgeries in patients in patients without SVI with no increase in the number of patients with an affected seminal vesicle left untreated.

### Table 2. Net benefit for removing the tip of the seminal vesicles from all patients or according to a prediction model, using a threshold of pt.

The reduction in the number of unnecessary surgeries removing the seminal vesicle tip per 100 patients is calculated as: (net benefit of the model – net benefit of treat all)/(pt/(1− pt)) × 100. This value is net of false negatives, and is therefore the equivalent to the reduction in unnecessary surgeries without a decrease in the number of patients with SVI who duly have tip surgery.

|
pt (%)
| Net Benefit
| Advantage of model

| Treat All
| Prediction Model
| Net benefit
| Reduction in avoidable tip surgeries per 100 patients

| 1
| 0.087
| 0.087
| 0
| 0

| 2
| 0.078
| 0.078
| 0
| 0

| 3
| 0.069
| 0.072
| 0.004
| 13

| 4
| 0.059
| 0.066
| 0.007
| 17

| 5
| 0.049
| 0.062
| 0.013
| 25

| 6
| 0.039
| 0.059
| 0.020
| 31

| 7
| 0.028
| 0.056
| 0.027
| 36

| 8
| 0.018
| 0.053
| 0.035
| 40

| 9
| 0.007
| 0.048
| 0.041
| 41

| 10
| −0.004
| 0.044
| 0.048
| 43

Open in a new tab

A second advantage of decision curve analysis is that it can be used to compare several different models. To illustrate this we compare the basic prediction model with an expanded model and with a simple clinical decision rule. The expanded model includes all of the variables in the basic model as well as some additional biomarkers. The clinical decision rule separates patients into two risk groups based on Gleason grade and tumor stage: those with grade greater than 6 or stage greater than 1 are considered high risk. To calculate a decision curve for this rule, we used the methodology outlined above except that the proportions of true- and false-positive results remained constant for all levels of pt. Figure 3 shows the decision curve for these three models in the key range of pt from 1 – 10%. There are three important features to note. First, although the expanded prediction model has a better AUC than the basic model (0.82 vs. 0.80), this makes no practical difference: the two curves are essentially overlapping. Second, the basic model has a considerably larger AUC than the simple clinical rule, yet for pt’s above 2%, there is essentially no difference between the two models. Third, at some low values of pt, using the simple clinical rule actually leads to a poorer outcome than simply treating everyone, despite a reasonably high AUC (0.72). In addition to illustrating the use of decision curves to compare multiple prediction models, Figure 3 also demonstrates that the methodology can easily be applied to a test or model with an inherently binary outcome, such as the simple clinical decision rule.

### Figure 3. Decision curve for seminal vesicle invasion (SVI): Comparison of three models.

Open in a new tab

Dotted line: assume all patients have SVI. Grey line: Binary decision rule. Solid line: Basic prediction model. Dashed line: Expanded prediction model incorporating additional biomarkers. The graph gives the expected net benefit per patient relative to no seminal vesicle tip removal in any patient (“treat none”). The unit is the benefit associated with one SVI patient duly undergoing surgical excision of seminal vesicle tip.

## Additional example: prognosis

In addition to evaluating diagnostic models, such as the model for SVI in men with prostate cancer, decision curves can also be used to assess the value of prognostic models. For example, a number of models have been developed to obtain a patient’s pre-operative probability of prostate cancer recurrence at five years based on PSA, clinical stage and grade of cancer at biopsy15, 16. These models are used to counsel patients but also to inform decision making because a patient with a high risk of recurrence might be asked to consider adjuvant hormonal therapy. We will use an observational cohort of men treated for prostate cancer to examine three models that predict recurrence within five years: one based on a multivariable model (“model”) and two clinical rules: “assume that any man with Gleason grade 8 or above will recur” (“Gleason rule”) and “assume that any man with Gleason grade 8 or above, or stage 2 or above, will recur” (“stage rule”). We will assess these models to determine how well they aid the decision whether or not to undergo adjuvant hormonal therapy.

Figure 4 shows the decision curves. Although a cancer recurrence is a serious event, the benefit of adjuvant hormonal therapy is somewhat unclear, and the drugs have important side-effects such as hot flashes, decreased libido, and fatigue. Due to differences in opinion about the value of hormonal therapy, and differences between patients in the importance attached to side-effects, the probability used as a threshold to determine hormonal therapy varies from case to case. A typical range of pt’s is 30% – 60%, that is, if you took a group of clinicians and patients and documented the probability of recurrence at which the clinician would advise hormonal therapy, this would vary between 30 – 60%. For much of this range, the simple Gleason rule is comparable to the multivariable model, even though it has far less discriminative accuracy (for example, AUC 0.56 compared to 0.73). Moreover, the Gleason rule is much better than the stage rule in the key 30% – 60% range even though it has a lower AUC (0.56 vs. 0.58). This is no doubt because the stage rule is highly sensitive and the Gleason rule more specific. But while sensitivity and specificity give a general indication as to which test is superior in which situation, decision curve analysis can delineate precisely the conditions under which each test should be preferred.

### Figure 4. Decision curve for prediction of recurrence after surgery for prostate cancer.

Open in a new tab

Thin line: assume no patient will recur. Dotted line: assume all patients will recur. Long dashes: binary decision rule based on cancer grade (“Gleason rule”). Grey line: binary decision rule based on both grade and stage of cancer (“stage rule”). Solid line: multivariable prediction model. The graph gives the expected net benefit per patient relative to no hormonal therapy for any patient (“treat none”). The unit is the benefit associated with one patient who would recur without treatment and who receives hormonal therapy.

As a further illustration, figures 5 and 6 show the decision curves for some theoretical distributions. Note that the results of the decision curve analysis accord well with our expectations. For example, a sensitive predictor is superior to a specific predictor where pt is low, that is, where the harm of a false-negative is greater than the harm of a false-positive; the situation is reversed at high pt; the curves for the sensitive and specific predictor cross near the incidence; a near-perfect predictor is of value except where pt is close to 1, that is, where the patient or clinician has to be nearly certain before he would take action; a predictor that is two standard deviations higher in patients who have the event is superior across nearly the full range of pt.

### Figure 5. Decision curve for a theoretical distribution.

Open in a new tab

In this example, disease incidence is 20%. Thin line: assume no patient has disease. Dotted line: assume all patients have disease. Thick line: a perfect prediction model. Grey line: a near-perfect binary predictor (99% sensitivity and 99% specificity). Solid line: a sensitive binary predictor (99% sensitivity and 50% specificity). Dashed line: a specific binary predictor (50% sensitivity and 99% specificity).

### Figure 6. Decision curve for a theoretical distribution.

Open in a new tab

In this example, disease incidence is 20%; the predictor example is a normally distributed laboratory marker. Thin line: assume no patient has disease. Dotted line: assume all patients have disease. Solid lines: prediction model from a single, continuous laboratory marker: from left to right, the lines represent a mean shift of 0.33, 0.5, 1 and 2 standard deviations in patients with disease.

## Discussion

Given the exponential increase in molecular markers in medicine, and the integration of information technology into clinical management, the development of prognostic and diagnostic models is likely to increase1. This lends urgency to the search for appropriate methods to determine the value of such models.

We have introduced a novel method for the evaluation of prediction models. This method is decision-analytic in nature and can therefore inform the decision of whether to use a model at all, or which of several models is optimal. Applying our method to several prediction models on two data sets confirms the general principle that metrics of accuracy, such as sensitivity, specificity and AUC, do not address the clinical value of a model. Although a model with a higher AUC is likely to be more valuable than one with a lower AUC, we have shown that, as would be expected from decision theory, models with very different AUCs can be comparable, and that models with higher AUCs can sometimes lead to inferior outcomes.

Decision curve analysis can be applied to both multivariable prediction models that give the probability of an event and to standard diagnostic tests that produce a simple binary result. Moreover, this method does not require information on the costs or effectiveness of treatment or how patients value different health states. We see this as beneficial because the method can be directly applied to a model validation dataset. A search of the medical literature suggests that the number of studies on diagnostic and prognostic markers using metrics of accuracy, such as the AUC, dwarfs the number of those using decision analytic methods. This is likely due to the burden of obtaining additional data, especially if health state utilities are required.

Nonetheless, interpretation of a decision curve analysis requires some understanding of the likely range of patients’ values. We believe that this is comparable to interpretation of clinical trial results. To determine the value of a treatment tested in a trial, a clinician needs to have some idea of a just how effective the treatment needs to be before patients would be prepared to take it, bearing in mind its side-effects. If the benefits of treatment are either much larger or smaller than most patients would require, the clinician can either give or withhold treatment without a detailed understanding of a patient’s preferences. If, on the other hand, effects of the treatment might be large enough for some patients, but not for others, a careful discussion with the patient is indicated, perhaps with formal elicitation of health state preferences and a decision analysis. In short, we do not propose decision curve analysis as a substitute for existing decision-analytic methods, though it may help indicate where such methods may be of benefit.

Similarly, we are not suggesting that decision curve analysis can replace measures of accuracy such as sensitivity and specificity. First, such measures are vital in the early stages of developing diagnostic and prognostic strategies, for example, when determining whether a biomarker shows any evidence of value on a convenience sample or when calibrating instruments or techniques17. Second, although it is possible for a model to be accurate but useless, the converse is not true: those proposing diagnostic or prognostic methods must show that they are reasonably accurate as well as demonstrating that they improve decision-making.

As pointed out when describing our methods, several previous workers have used the relative benefit and harm associated with true- and false-positive results to determine a single, optimal threshold for a diagnostic test10, 11, 18. Determining a single threshold is only possible under two conditions: first, the benefits and harms of action must be well understood; second, how benefits and harms are valued must be similar between individuals. As an illustration, compare one of the examples given by Djulbegovic, Hozo and Lyman11 – prevention of DVT – with our prostatectomy example. In the DVT case, precise estimates for the treatment benefit (reduction in rate of DVT) and harm (major bleeding) are available from a randomized trial, moreover, there are no important differences between individuals as to the relative harm of a DVT and a bleed: the authors use the assumption that “the avoidance of DVT and bleeding complications represents approximately the same value to the patient”11. In the prostatectomy example, conversely, estimates of the benefits (improved urinary and erectile function) and harms (increased rate of cancer recurrence) of the seminal vesicle tip sparing approach are available only from observational studies of moderate size13 and are subject to considerable disagreement. Moreover, how different individuals value potency and continence compared to cancer recurrence varies greatly. Other investigators have used the relative benefits and harms associated with different test outcomes in net benefit or loss functions to compare predictive models19, 20. However, this requires investigators to specify a value for harms and benefits. For example, Habbema and Hilden describe a method to assess a prediction tool for management of acute abdominal pain by ascribing losses to outcomes such as failure to diagnose appendicitis (36 units), appendectomy for a patient with a healthy appendix (10 units) and intensive follow-up in a patient with non-specific abdominal pain (2 units)20. Such methods can be adapted for sensitivity analysis using different values for such outcomes, but this is generally complex and does not clearly maintain the inherent relationship between values and probability thresholds. Our method combines values and thresholds in a simple, parsimonious method to determine whether a predictive model should be used clinically, whilst allowing each to co-vary appropriately.

One assumption of our method is that the predicted probability and threshold probability are independent. This is true for the examples we give in this paper: there is no relationship between, say, the appearance of a cancer cell under the microscope (Gleason grade) and how a patient values sexual and urinary function relative to cancer recurrence. It is possible that a third variable, such as age, might influence both the probability of recurrence and treatment preferences; however, in our data set, the correlation between age and SVI was very low (0.04). We think that an important correlation between predicted probability and threshold probability will be very much the exception rather than the rule. One possible example would be gender. If gender was indeed correlated with both outcome and threshold probability, the analyst might consider constructing a decision curve separately for men and women.

In the examples presented here, we have not considered the uncertainty associated with model predictions and their possible impact on the decision curve. We are currently evaluating methods to characterize uncertainty, including confidence bands and metrics such as the probability that the net benefit of a model is superior to a comparator.

Hilden21 has written of the schism between what he describes as “ROCographers”, those who are interested solely in accuracy, and “VOIographers”, who are interested in the clinical value of information (VOI). He notes that while the former ignore the fact that their methods have no clinical interpretation, the latter have not agreed upon an appropriate mathematical approach. We feel that decision curve analysis may help bridge this schism by combining the direct clinical applicability of decision-analytic methods with the mathematical simplicity of accuracy metrics.

## Acknowledgments

Dr Vickers’ work on this research was funded by a P50-CA92629 SPORE from the National Cancer Institute.

## References

-
1.Freedman AN, Seminara D, Gail MH, et al. Cancer risk prediction models: a workshop on development, evaluation, and application. J Natl Cancer Inst. 2005 May 18;97(10):715–723. doi: 10.1093/jnci/dji128. [DOI] [PubMed] [Google Scholar]

-
2.Das SK, Baydush AH, Zhou S, et al. Predicting radiotherapy-induced cardiac perfusion defects. Med Phys Jan. 2005;32(1):19–27. doi: 10.1118/1.1823571. [DOI] [PubMed] [Google Scholar]

-
3.Hendriks DJ, Broekmans FJ, Bancsi LF, Looman CW, de Jong FH, te Velde ER. Single and repeated GnRH agonist stimulation tests compared with basal markers of ovarian reserve in the prediction of outcome in IVF. J Assist Reprod Genet Feb. 2005;22(2):65–73. doi: 10.1007/s10815-005-1495-3. [DOI] [PMC free article] [PubMed] [Google Scholar]

-
4.Cindolo L, Patard JJ, Chiodini P, et al. Comparison of predictive accuracy of four prognostic models for nonmetastatic renal cell carcinoma after nephrectomy. Cancer. 2005 Oct 1;104(7):1362–1371. doi: 10.1002/cncr.21331. [DOI] [PubMed] [Google Scholar]

-
5.Hunink M, Glasziou P, Siegel J. Decision-Making in Health and Medicine: Integrating Evidence and Values. New York: Cambridge University Press; 2001. [Google Scholar]

-
6.Djulbegovic B, Desoky AH. Equation and nomogram for calculation of testing and treatment thresholds. Med Decis Making Apr-Jun. 1996;16(2):198–199. doi: 10.1177/0272989X9601600215. [DOI] [PubMed] [Google Scholar]

-
7.Loomes G, McKenzie L. The use of QALYs in health care decision making. Soc Sci Med. 1989;28(4):299–308. doi: 10.1016/0277-9536(89)90030-0. [DOI] [PubMed] [Google Scholar]

-
8.van Osch SM, Wakker PP, van den Hout WB, Stiggelbout AM. Correcting biases in standard gamble and time tradeoff utilities. Med Decis Making Sep-Oct. 2004;24(5):511–517. doi: 10.1177/0272989X04268955. [DOI] [PubMed] [Google Scholar]

-
9.Weinstein MC, Fineberg HV. Clinical Decision Analysis. Philadelphia, PA: W.B. Saunders; 1980. [Google Scholar]

-
10.Pauker SG, Kassirer JP. The threshold approach to clinical decision making. N Engl J Med. 1980 May 15;302(20):1109–1117. doi: 10.1056/NEJM198005153022003. [DOI] [PubMed] [Google Scholar]

-
11.Djulbegovic B, Hozo I, Lyman GH. Linking evidence-based medicine therapeutic summary measures to clinical decision analysis. MedGenMed. 2000 Jan 13;2(1):E6. [PubMed] [Google Scholar]

-
12.Zlotta AR, Roumeguere T, Ravery V, et al. Is seminal vesicle ablation mandatory for all patients undergoing radical prostatectomy? A multivariate analysis on 1283 patients. Eur Urol Jul. 2004;46(1):42–49. doi: 10.1016/j.eururo.2004.03.021. [DOI] [PubMed] [Google Scholar]

-
13.Guzzo TJ, Vira M, Wang Y, et al. Preoperative parameters, including percent positive biopsy, in predicting seminal vesicle involvement in patients with prostate cancer. J Urol. 2006 Feb;175(2):518–521. doi: 10.1016/S0022-5347(05)00235-1. discussion 521–512. [DOI] [PubMed] [Google Scholar]

-
14.Peirce CS. The numerical measure of the success of predictions. Science. 1884;4:453–454. doi: 10.1126/science.ns-4.93.453-a. [DOI] [PubMed] [Google Scholar]

-
15.Kattan MW, Eastham JA, Stapleton AM, Wheeler TM, Scardino PT. A preoperative nomogram for disease recurrence following radical prostatectomy for prostate cancer. J Natl Cancer Inst. 1998;90(10):766–771. doi: 10.1093/jnci/90.10.766. [DOI] [PubMed] [Google Scholar]

-
16.Steuber T, Karakiewicz PI, Augustin H, et al. Transition zone cancers undermine the predictive accuracy of Partin table stage predictions. J Urol Mar. 2005;173(3):737–741. doi: 10.1097/01.ju.0000152591.33259.f9. [DOI] [PubMed] [Google Scholar]

-
17.Pepe MS, Etzioni R, Feng Z, et al. Phases of biomarker development for early detection of cancer. J Natl Cancer Inst. 2001 Jul 18;93(14):1054–1061. doi: 10.1093/jnci/93.14.1054. [DOI] [PubMed] [Google Scholar]

-
18.Moons KG, Stijnen T, Michel BC, et al. Application of treatment thresholds to diagnostic-test evaluation: an alternative to the comparison of areas under receiver operating characteristic curves. Med Decis Making. 1997 Oct-Dec;17(4):447–454. doi: 10.1177/0272989X9701700410. [DOI] [PubMed] [Google Scholar]

-
19.Parmigiani G. Modeling in Medical Decision Making. New York: John Wiley & Sons Inc; 2002. [Google Scholar]

-
20.Habbema JDF, Hilden J. The measurement of performance in probabilistic diagnosis. IV. Utility considerations in therapeutics and prognostics. Meth Inform Med. 1978;17:238–246. [PubMed] [Google Scholar]

-
21.Hilden J. Evaluation of diagnostic tests - the schism. Society for Medical Decision Making Newsletter. 2004;16(4):5–6. [Google Scholar]

## ACTIONS

-

View on publisher site

-

PDF (711.0 KB)

-

-

-

## PERMALINK

## RESOURCES

###

###

###

## Cite

-

-

Download .nbib
.nbib

-

Format:

## Add to Collections

-
-
-

-
-
-

-
-
-
-

<!-- fetch 2: https://api.crossref.org/works/10.1177/0272989X06295361 + https://api.openalex.org/works/doi:10.1177/0272989X06295361 | fetch.py json-metadata | 2026-11-06T23:14+07:00 | metadata -->
source: Crossref
title: Decision Curve Analysis: A Novel Method for Evaluating Prediction Models
authors: Vickers, Andrew J.; Elkin, Elena B.
container: Medical Decision Making
published: 2006-11
volume: 26
issue: 6
pages: 565-574
article number: 
publisher: SAGE Publications
doi: 10.1177/0272989x06295361
type: journal-article
is-referenced-by-count (Crossref citations): 5986

abstract:
Background. Diagnostic and prognostic models are typically evaluated with measures of accuracy that do not address clinical consequences. Decision-analytic techniques allow assessment of clinical outcomes but often require collection of additional information and may be cumbersome to apply to models that yield a continuous result. The authors sought a method for evaluating and comparing prediction models that incorporates clinical consequences, requires only the data set on which the models are tested, and can be applied to models that have either continuous or dichotomous results. Method. The authors describe decision curve analysis, a simple, novel method of evaluating predictive models. They start by assuming that the threshold probability of a disease or event at which a patient would opt for treatment is informative of how the patient weighs the relative harms of a false-positive and a false-negative prediction. This theoretical relationship is then used to derive the net benefit of the model across different threshold probabilities. Plotting net benefit against threshold probability yields the “decision curve.” The authors apply the method to models for the prediction of seminal vesicle invasion in prostate cancer patients. Decision curve analysis identified the range of threshold probabilities in which a model was of value, the magnitude of benefit, and which of several models was optimal. Conclusion. Decision curve analysis is a suitable method for evaluating alternative diagnostic and prognostic strategies that has advantages over other commonly used measures and techniques.

source: OpenAlex
title: Decision Curve Analysis: A Novel Method for Evaluating Prediction Models
authors: Andrew Julian Vickers; Elena B. Elkin
institutions: Memorial Sloan Kettering Cancer Center
venue: Medical Decision Making
publication date: 2006-11-01
volume: 26
issue: 6
pages: 565–574
doi: https://doi.org/10.1177/0272989x06295361
cited_by_count (OpenAlex): 6594
type: article
location: https://doi.org/10.1177/0272989x06295361 (open access: False)
location: https://pubmed.ncbi.nlm.nih.gov/17099194 (open access: False)
location: https://www.ncbi.nlm.nih.gov/pmc/articles/2577036 (open access: True)
location: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.620.4039 (open access: False)
location: https://journals.sagepub.com/doi/10.1177/0272989X06295361 (open access: False)

abstract:
BACKGROUND: Diagnostic and prognostic models are typically evaluated with measures of accuracy that do not address clinical consequences. Decision-analytic techniques allow assessment of clinical outcomes but often require collection of additional information and may be cumbersome to apply to models that yield a continuous result. The authors sought a method for evaluating and comparing prediction models that incorporates clinical consequences,requires only the data set on which the models are tested,and can be applied to models that have either continuous or dichotomous results. METHOD: The authors describe decision curve analysis, a simple, novel method of evaluating predictive models. They start by assuming that the threshold probability of a disease or event at which a patient would opt for treatment is informative of how the patient weighs the relative harms of a false-positive and a false-negative prediction. This theoretical relationship is then used to derive the net benefit of the model across different threshold probabilities. Plotting net benefit against threshold probability yields the "decision curve." The authors apply the method to models for the prediction of seminal vesicle invasion in prostate cancer patients. Decision curve analysis identified the range of threshold probabilities in which a model was of value, the magnitude of benefit, and which of several models was optimal. CONCLUSION: Decision curve analysis is a suitable method for evaluating alternative diagnostic and prognostic strategies that has advantages over other commonly used measures and techniques.
