---
id: S415
url: https://arxiv.org/html/1801.08494
requested: https://arxiv.org/html/1801.08494
fetched: 2026-11-06T23:13+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T06
part: 4
raw: raw.html (296 KB)
conversion: html-text of https://arxiv.org/html/1801.08494 (readable, 11708 words)
---
title: Evaluating Predictive Models of Student Success: Closing the Methodological Gap

Skip to main content

#####

Why HTML?

Back to Abstract

Download PDF

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
-
-
-

-
-

License: arXiv.org perpetual non-exclusive license

arXiv:1801.08494v2 [stat.AP] 13 Jun 2018

# Evaluating Predictive Models of Student Success: Closing the Methodological Gap

Josh Gardner

Affiliation: School of Information

Affiliation: The University of Michigan

Email: jpgard@umich.edu

  
Christopher Brooks

Affiliation: School of Information

Affiliation: The University of Michigan

Email: brooksch@umich.edu

###### Abstract

Model evaluation – the process of making inferences about the performance of predictive models – is a critical component of predictive modeling research in learning analytics. We survey the state of the practice with respect to model evaluation in learning analytics, which overwhelmingly uses only naïve methods for model evaluation or statistical tests which are not appropriate for predictive model evaluation. We conduct a critical comparison of both null hypothesis significance testing (NHST) and a preferred Bayesian method for model evaluation. Finally, we apply three methods – the naïve average commonly used in learning analytics, NHST, and Bayesian – to a predictive modeling experiment on a large set of MOOC data. We compare 96 different predictive models, including different feature sets, statistical modeling algorithms, and tuning hyperparameters for each, using this case study to demonstrate the different experimental conclusions these evaluation techniques provide.

## 1 Introduction

The past decade has seen an explosion in the use of data science methods in general, and predictive modeling in particular. Predictive modeling of student success has become a central task in learning analytics research. The increased use of digital learning tools such as Massive Open Online Courses (MOOCs) has made it easier than ever to store, replicate, transfer, and analyze learner data, and improvements in open-source statistical software for data science have generated an “embarrassment of riches” with seemingly limitless numbers of modeling techniques available for use.

A critical scientific component of predictive modeling research is the process of model evaluation, where inferences are drawn about the performance of a set of predictive models. In an optional step known as model selection, a single preferred model is selected according to some objective function.

In this paper, we argue that there is a significant methodological gap in current practice in the learning analytics and educational data mining communities with respect to model evaluation and selection, and we present a survey of techniques to close this gap. We present data from a review of prior predictive modeling work in MOOCs to establish the “state of the practice” in the field in Section 2. In Section 3, we present a brief survey of methods for model evaluation, drawing from several fields outside of learning analytics in order to identify methods which are most effective, and which techniques currently used by the field are ineffective, for predictive model evaluation. In Section 4, we conduct a predictive modeling experiment on a large sample of MOOCs, applying three techniques to demonstrate the different conclusions of three evaluation methods in practice. Our results also demonstrate specific empirical findings which are relevant to future modeling research in MOOCs, described in Section 5. We provide conclusions with an eye to practice within the learning analytics field in Section 6.

## 2 State of the Practice: Model Evaluation in Learning Analytics

The current work is concerned with experiments which construct multiple predictive models and attempt to compare their performance. In this section, we survey a large sample of 87 such experiments in MOOCs. Having passed the peer review process in several of the field’s flagship journals and conferences (Computers and Human Behavior, Journal of Educational Data Mining, International Conference on Learning Analytics and Knowledge, The International Conference on Educational Data Mining, Learning at Scale, etc.), these results also reflect the consensus of reviewers -- and the field as a whole-- on techniques for predictive model evaluation in MOOCs.11
1

The survey methodology is described in detail in [21]; complete results of the literature review, including citation and categorization information for each study evaluated, is provided in the appendix of that work. Due to considerations of length we omit a thorough description here. This consensus is surprisingly strong, considering the breadth of approaches taken to other aspects of predictive modeling (e.g. feature extraction, statistical algorithms). The existing consensus is also on a set of techniques which are often statistically problematic, as we will discuss in Section 3.

### 2.1 Model Evaluation in MOOCs

#### 2.1.1 Prediction Architecture

In order to obtain the model and its predictions for evaluation, an experiment must choose a prediction architecture – the procedure by which training and testing datasets are partitioned and model predictions are obtained. The prediction architectures used in the works included in our survey are shown in Figure 1.

Figure 1: Prediction architecture in works surveyed; this is the method by which estimates of model performance on unseen data are obtained (for further analysis, i.e., by applying statistical tests do the data).

These results demonstrate the prevalence of various forms of cross-validation in evaluating models (typically 2-, 5-, or 10-fold cross-validation; only two experiments surveyed use leave-one-out cross-validation). We found no cases where fold-level data was reported or evaluated (for example, to produce estimates of the variance of model performance across each fold). Model performance data was only evaluated and reported as an average for all works surveyed. The use of cross-validation is particularly relevant in light of concerns about statistical testing applied to cross-validated model performance data discussed in Section 3. In nine experiments (nearly 10% of the experiments surveyed), the prediction architecture was not even reported, despite the presentation of predictive results in the work.

#### 2.1.2 Model Evaluation

Model evaluation is the procedure by which observed differences in predictive performance are formally evaluated in order to draw inferences from the results of an experiment. We present data on model evaluation methods for any experiments where multiple predictive models were evaluated and compared, and where the authors reported inferences about which model was a “better” predictor of the outcome of interest, in Table 1. Note that strictly explanatory modeling experiments, where inspection of the model itself is the stated primary goal, are under the “No model comparison or explanatory” label. While our categorization cannot be perfect based only on the published descriptions of work, the results in Table 1 make clear the lack of use of statistical methods for model evaluation in current learning analytics research – a practice which we believe is scientifically problematic. Below, we will also demonstrate that the most prevalent methods for model evaluation shown in Table 1 are known to be ineffective for the contexts in which they are being used (e.g., with experimental data from a cross-validation architecture; for large numbers of comparisons).

|

Student’s tt-test

|

5

|

Other NHST (Chi-Square, etc.)

|

5

|

No model comparison or explanatory

|

24

|

Model comparison with no statistical test

|

51

|

Total

|

87

Table 1: Testing procedures for model evaluation in works surveyed.

This consensus on techniques for predictive model evaluation in the field of learning analytics is as surprising as it is strong. Cross-validation with no statistical testing is overwhelmingly adopted in the learning analytics and educational data mining predictive modeling research, to the point where the results of this procedure are considered sufficiently acceptable by authorities in the field to be published widely, despite known inferential flaws with such a procedure (discussed in Section 3).

Furthermore, the impact of these methods is compounded by large numbers of hypotheses being tested: Fewer than 20% of the works surveyed compare one or two models; the remainder compared more than two models – with the total number of comparisons unreported in an additional 20% of cases. For example, [47] compares at least 1400 models with various architectures and window formulations; [41] evaluates over 10,000 candidate models; neither correct or even acknowledge the large number of multiple comparisons in the context of their analysis. None of the works surveyed applied corrections for multiple testing, despite the fact that uncorrected multiple testing leads to elevated error rates, and existing methods were developed in the 1960s with “between 2 and perhaps 20” tests in mind and are not appropriate or effective for testing thousands of hypotheses [16, pp. 273].

#### 2.1.3 Hyperparameter Tuning

There is no broad consensus in practice regarding which feature extraction methods or algorithms should be used to construct models for student success prediction in MOOCs [21]. However, almost all algorithms require selecting and, optionally, tuning hyperparameters which control elements of model fit and therefore the model parameters selected when the algorithm is applied to a specific dataset. These hyperparameters control convergence of parameter estimates, feature selection or regularization, and the model loss or “cost” function. Little attention has been paid to hyperparameter tuning in prior work, despite the fact that tuning each additional hyperparameter setting adds an additional hypothesis test or pairwise comparison to an experiment.

Our survey finds that in practice, hyperparameter tuning is frequently not described in published research: in 20 out of 87 (23%) of the works surveyed, methods for hyperparameter tuning or selection were not reported or even mentioned, and in a remaining 9 (10%), hyperparameter tuning was reported as being performed manually, with no reproducible procedure offered. In cases where hyperparameter tuning is not reported, either the hyperparameter tuning is (a) simply not performed, and default settings are used; (b) performed by the experimenter, but not reported, or (c) performed automatically by a machine learning software toolkit. As we will describe in detail below, (b) and (c) require model evaluation methods which are robust to multiple comparisons even without knowing or reporting how many comparisons are conducted in an experiment. In (a), we might question whether an experiment sufficiently explored the performance of a given modeling approach; however, our case study in Section 4 showed little impact of hyperparameter tuning relative to the effects of different features or statistical algorithms, particularly when considering that tuning increases the number of models considered in a multiplicative fashion (because an experiment typically tests each algorithm/hyperparameter pairing with each set of features).

### 2.2 Why is Model Evaluation Rare in Learning Analytics?

While it is difficult to determine with certainty, the previous analysis raises the question of why learning analytics has arrived at the status quo of inadequate model evaluation, several factors have likely contributed to the current state of the practice, including:

Inadequate Tooling. Software for model evaluation is rare, and is currently not included in (or even integrated with) many of the most common statistical software tools for machine learning research. Tracking the entire process of model exploration in an experiment therefore requires extensive manual effort or the use of additional specialized tools (e.g. [42]). Furthermore, many machine learning toolkits ignore statistical model evaluation by design, and conduct intensive searches of the model and hyperparameter space without regard to statistical inference procedures (e.g. AutoWEKA, SuperLearner and caret in R, auto-sklearn in Python).

Evolution of Data Science. Many of the issues addressed in the current work were simply not concerns even a decade ago. Open-source data science methods, multicore computing, and statistical software have exploded in the time that learning analytics (and particularly MOOCs) have also come of age. As such, methods which addressed the research challenges of previous eras have become overwhelmed by these‘computer age statistical inference” problems, including the challenge of “large scale hypothesis testing” when the number of comparisons is massive [16].

Lack of Training and Theory. Many researchers who utilize predictive modeling simply were not trained in appropriate research methods for large-scale machine learning experiments; indeed, the theory guiding these methods is still the subject of active research [16].

Lack of Incentive. As the prior review demonstrates, there is currently little incentive to perform rigorous model evaluation in published work: reviewers do not expect it. Predictive modeling experiments can be published without the rigorous statistical evaluation that is expected of many other types of experimental work (e.g. randomized trials). Such evaluation may be perceived as even reducing the chances of publication by revealing “insignificant” results.

The above factors reflect the advancement of statistical and modeling capabilities which have not yet been matched by an advancement in methods or accepted practices. We hope that, through works such as the current experiment, we can contribute to gradual progress on each; of course, future work is needed to address each of these more deeply.

## 3 Predictive Model Evaluation and Selection

Our focus in this section is to survey prior work on statistical model evaluation techniques which are (a) widely used in the field of learning analytics, or (b) particularly effective for tasks commonly faced in this field (e.g. evaluating multiple models across multiple datasets). We mention additional methods for model evaluation only where relevant; an exhaustive survey is beyond the scope of the current work. We conclude by presenting a series of criteria for an acceptable model evaluation procedure in Section 3.4, which lead us to prefer the Bayesian procedure for predictive model evaluation in learning analytics.

### 3.1 Naïve Average Method

The most common technique for comparing the performance of predictive models in MOOC research is what we term the “naïve average” method. In this approach, models are evaluated by comparing their average performance (often, averaged across cross-validation folds) with no statistical test. As shown in Table 1, 51 out of the 87 studies (59%) surveyed use the naïve average method to draw inferences about a comparison between multiple predictive models (either implicitly, by presenting the predictive results from several models, or explicitly, by referring to models as “more accurate” or having the “best performance”). Drawing inferences about which model may be “best” based on a simple sample average or the observed rankings is inappropriate for machine learned models for the same reasons it is inappropriate for drawing inferences from any other data: it provides no robustness against spurious results, no measure of confidence in the conclusion given the observed data, and little basis for comparison across studies. We call this method the “naïve average” method because, by simply choosing the “best” average performance, this approach naïvely assumes that any differences observed must be (a) due to genuine differences in model performance (and not, for instance, random variation), and (b) that these differences must be both practically significant (large or important enough to be useful) and (in frequentist terms) statistically significant.

Statistical testing was developed to draw principled, reliable inductive inferences from data under uncertainty. This is particularly important when evaluating the complex performance data from predictive models of student success, which itself reflects underlying samples of student populations, randomized resamples of subpopulations (for instance, via cross-validation), and other stochastic procedures inherent to many modeling algorithms (such as random feature selection or parameter initialization methods). Failing to utilize any testing in the presence of intentional randomization makes the observation of spurious results more likely, and in the worst cases, could allow for exploitation of randomization to produce desired results (this behavior has been observed in other fields, such as reinforcement learning, where random seed “optimization” has been cited as a threat to reproducibility in the field [25]).

Furthermore, averaging itself may be particularly uninformative or misleading for model evaluation. The naïve average method must assume commensurability across datasets in order to justify the use of averaging. In the case of predictive models of student success, this assumption may not be justified: some courses might be easier or more difficult to predict on for a variety of reasons, including variability in student subpopulations, level of difficulty, quality of instruction, course durations and requirements, etc. Demšar notes that “[i]f the results on different data sets are not comparable, their averages are meaningless” [13, pp. 6]. Averages are also susceptible to outliers, which particularly distort experimental results when relatively small populations are used (as is the case in our review, where nearly 50% of studies evaluated only a single course). Furthermore, average cross-validated performance can generate “optimistically” biased model performance estimates [19], because models are repeatedly trained and tested on overlapping subsets of the same dataset, not a disjoint, truly unseen dataset as in a prediction architecture using an independent test set.

### 3.2 Null Hypothesis Significance Testing (NHST)

In this section, we discuss model evaluation procedures based on null hypothesis significance testing (NHST). As Table 1 demonstrates, this is the second most common model evaluation method in learning analytics.

A great deal of early work on model evaluation and selection in the field of machine learning focused on selecting from two models evaluated on a single dataset [15, e.g.]. While the field of learning analytics often addresses tasks which are more complex (multiple models and datasets), this early work highlighted several issues which any model evaluation procedure must address. These include having an acceptable error rate [4, 15], using methods which provide inferential replicability [5, 6], and accurate estimation of statistical parameters in the presence of correlated data (such as the data generated by cross-validation) including the standard error [38, e.g.] and degrees of freedom [44].

One two-model test is worth discussion here, due to its wide use in learning analytics research, as shown in Table 1: the Student’s tt-test. The tt-test has been analyzed at length for predictive model evaluation, and many variants of the tt-test have been roundly rejected as inappropriate and misleading for evaluating cross-validated model performance data, to which it is often applied in learning analytics. An important analysis was presented two decades ago in [15], where a series of experiments demonstrated that several variants of the tt-test (difference in proportions, paired tt-test using repeated random subsampling, and tt-test with 10-fold cross-validation) display an elevated Type I error rate and are therefore ineffective for model evaluation. Other empirical work has shown similar results with tt-tests with a variety of other resampling and cross-validation architectures [6, e.g.]. While various corrections have been proposed to this test [38, e.g.] and other alternatives exist [4, e.g. the sorted runs scheme explored in], they are rarely used in practice and were not used in any of the works surveyed, and are therefore not considered in detail here.

In practice, comparison of only two models on a single dataset account for only 10 (11%) of the works surveyed, and it would be preferable to use model evaluation methods which can be easily extended to experiments with more than a single dataset. One method to adapt a tt-test or other significance tests (e.g. Chi-square) to the multiple-comparisons case involves making an adjustment for multiple testing (which were not applied in any of the works surveyed which utilized these NHST procedures), such as that proposed in [2]. However, such procedures are not considered appropriate for cases where k>>20k>>20 [16], and additional procedures for the multiple-model-multiple-dataset task exist which both address the multiple testing concerns and issues with parameter estimation mentioned above, as well as broader concerns with the suitability of NHST procedures such as the tt-test.

The assumptions of traditional statistical tests used for data analysis, such as the paired tt-test, are often strongly violated by predictive model performance data, which makes them particularly ineffective for evaluating hypotheses about predictive models. For example, the classical statistical procedure to determine whether there is a difference between several experimental subsamples is analysis of variance (ANOVA) [18], perhaps with a post-hoc test if groupwise differences were detected. This procedure is unfit for predictive model evaluation, however, because its assumptions of normality, sphericity, and independence (or non-correlation) are not guaranteed – and frequently violated – by the data from predictive modeling experiments [13]. We do not discuss the fitness of ANOVA for model evaluation further because it was not used in any of the work surveyed, but refer the reader to [13, 26] for further discussion.

Nonparametric procedures are often more appropriate when the assumptions of parametric procedures (such as the tt-test) are likely to be violated. The Friedman test, in particular, has gained increasing adoption across the field of machine learning for model evaluation [13, 26]. The Friedman test is a nonparametric version of the ANOVA test, and compares the average rankings of the kk algorithms across each of NN datasets, calculating a test statistic measuring the probability of the observed rankings under the null hypothesis of all algorithms having equivalent performance (and therefore equal expected average rankings). The observed value of the Friedman statistic

|
| χF2=12​Nk⁡(k+1)​[∑jRj2−k​(k+1)24]\chi_{F}^{2}=\frac{12N}{k(k+1)}\left[\sum_{j}R_{j}^{2}-\frac{k(k+1)^{2}}{4}\right]
|
| (1)

where RjR_{j} is the rank of the jjth of kk algorithms on NN datasets and the statistic is distributed according to a chi-square distribution with k−1k-1 degrees of freedom, is compared to a critical value for the given values of NN and kk [20].

If the null hypothesis is rejected at the selected significance level, the post-hoc Nemenyi test is used to compare all classifiers to each other. The Nemenyi test is similar to a nonparametric version of the Tukey test for ANOVA, and uses a critical difference

|
| C​D=qα​k⁡(k+1)6​NCD=q_{\alpha}\sqrt{\frac{k(k+1)}{6N}}
|
| (2)

as a threshold to determine whether the performance between any two classifiers is significantly different, where the critical value qαq_{\alpha} is based on the Studentized range statistic divided by 2\sqrt{2}.

The results of the Friedman and Nemenyi tests are often visualized using a Critical Difference (CD) diagram, originally proposed in [13]. An example is shown in Figure 2. Models are plotted on a number line according to their average rank across all datasets, and bold CD lines are used to link models which are statistically indistinguishable at α\alpha.

Figure 2: A Critical Difference (CD) diagram, which is used to visualize the results of the Friedman + Nemenyi testing procedure.

One advantage of this method is that because the Friedman test uses only the rankings of the algorithms on each dataset, it does not require estimates of the variance of model performance – recall that inaccurate estimates of variance were one of the primary confounding issues with tt-tests applied to cross-validated model performance data. Instead, it only requires that the estimates of model performance and the measured rankings they produce are reliable and “…that enough experiments were done on each data set and, preferably, that all the algorithms were evaluated using the same random samples” [13, pp. 2] and that the datasets, and therefore the rankings of the algorithms across each dataset, are independent. In contrast to many other statistical approaches to comparing model performance, such as ANOVA, the Friedman test makes no further assumptions about the sampling scheme.

This procedure also accounts for multiple comparisons. The number of models compared, kk, is accounted for in both the Friedman statistic (Equation 1) and the post-hoc Nemenyi test (Equation 2). The number of comparisons conducted in the course of a model evaluation experiment can grow quite large even with modest numbers of feature sets, algorithms, and hyperparameter settings (for example, in the case study in Section 4, k=96k=96 and the number of pairwise comparisons is 96×952=4560\frac{96\times 95}{2}=4560); adequate controls to moderate the error rate and inferential replicability are necessary for any test suited for model evaluation. For an example of the use of this method in another domain, see [35].

### 3.3 Bayesian Model Evaluation

The application of Bayesian statistical methods to model evaluation has increased over the past two decades as scientific consensus around the concerns outlined above has grown, and as Bayesian modeling techniques and the computational infrastructure necessary to conduct them have become more widely accessible to researchers. There are several approaches to model evaluation which use Bayesian techniques, and we refer the reader to [1] for a review. In this work, we focus on an approach which Benavoli et al. refer to as Bayesian parameter estimation or simply Bayesian analysis [1]. We will refer to this approach as Bayesian model evaluation, but occasionally use Benavoli et al.’s nomenclature when the meaning is clear.

Bayesian hierarchical models are used to address statistical applications which involve multiple parameters that can be regarded as related or connected. The hierarchical model encodes the dependence between these parameters such that certain aspects of the model depend on other parameters, which are referred to as hyperparameters. The distributions of these hyperparameters are referred to as prior distributions in this section to avoid confusion with the hyperparameters of machine learning models discussed in other sections. In a hierarchical model, the data are used to estimate the distribution of all parameters by either direct evaluation (which is rare) or by Markov Chain Monte Carlo (MCMC) sampling. As with any Bayesian model, a hierarchical model treats the parameters as random; we therefore estimate and explore their distribution instead of testing hypotheses about the ‘‘true’’ value of the parameter.22
2

While a detailed introduction of Bayesian hierarchical modeling is beyond the scope of this paper, we refer the reader to [22, Ch. 5] or [31, Ch. 9] for a thorough introduction.

In the current work, we consider the Bayesian hierarchical correlated tt-test of [9]. This test compares the results of multiple classifiers over multiple datasets when cross-validation is used. This test uses the following hierarchical model to account for the mean, variance, and correlation of the results of fold-level model performance data (an example of the data used for such a model is shown in Table 5):

|
| μ1,…,μk∼t⁡(μ0,σ0,ν)\mu_{1},\ldots,\mu_{k}\sim t(\mu_{0},\sigma_{0},\nu)
|
| (3)

|
| σ1,…,σk∼U​n​i​f​o​r​m​(0,σ¯)\sigma_{1},\ldots,\sigma_{k}\sim Uniform(0,\bar{\sigma})
|
| (4)

|
| xi∼M​V​N​(𝟙​μi,Σi)x_{i}\sim MVN(\mathbbm{1}\mu_{i},\Sigma_{i})
|
| (5)

Equation (5), where xix_{i} is the vector of differences between models, captures the correlation between cross-validation measures on the iith dataset by modeling these as draws from a multivariate normal distribution with mean μi\mu_{i}, and correlation ρ\rho. 𝟙\mathbbm{1} is a vector of ones, and the covariance matrix Σ\Sigma has diagonal elements σi2\sigma_{i}^{2} and off-diagonal elements ρ​σi2\rho\sigma_{i}^{2} where ρ=nt​ent​r\rho=\frac{n_{t}e}{n_{t}r}, following Nadeau and Bengio [9, 38]. Equation (4) allows each dataset to have its own estimation uncertainty, standard deviation σi\sigma_{i}, drawn from a common uniform distribution where σ¯=1000⋅∑i=1qσi^k\bar{\sigma}=1000\cdot\sum_{i=1}^{q}\frac{\hat{\sigma_{i}}}{k}. We refer the reader to [1, 9] for further details.

Equation (3) models the differences between two classifiers on each dataset, and thus allows that some classifiers might perform better or worse on certain datasets, leading to variability in the difference μi\mu_{i} on each dataset ii. Equation (3) also models the fact that each observed mean difference on a single dataset, μi\mu_{i}, depends on the average difference of accuracy between the two classifiers on the population of data sets, μ0\mu_{0}. This parameter, μ0\mu_{0}, is typically the quantity of interest, and is modeled with a tt-distribution with variance σ02\sigma_{0}^{2} and degrees of freedom ν\nu. The use of a tt-distribution here makes the model more robust to outliers [32], and slightly more conservative than its frequentist counterpart [9].

Prior distributions for the model are given by:

|
| σ0∼U​n​i​f​o​r​m​(0,s¯0),\sigma_{0}\sim Uniform(0,\bar{s}_{0}),
|
| (6)

|
| μ0∼U​n​i​f​o​r​m​(−1,1),\mu_{0}\sim Uniform(-1,1),
|
| (7)

|
| ν∼G​a​m​m​a​(α,β)\nu\sim Gamma(\alpha,\beta)
|
| (8)

|
| α∼U​n​i​f​o​r​m​(α¯=0.5,α¯=5)\alpha\sim Uniform(\underaccent{\bar}{\alpha}=0.5,\bar{\alpha}=5)
|
| (9)

|
| β∼U​n​i​f​o​r​m​(β¯=0.05,β¯=0.15)\beta\sim Uniform(\underaccent{\bar}{\beta}=0.05,\bar{\beta}=0.15)
|
| (10)

A detailed discussion of these priors is beyond the scope of this work, but we note that these are considered appropriate for most measures of predictive model performance when used with this procedure, including AUC, the measure used in the experiment below. The reader is referred to [9] for a detailed discussion.

This Bayesian hierarchical model is used to make inferences about average differences in model performance for each pair of candidate models XX and YY. From the fitted model, MCMC is used to generate samples of θ=(P⁡(X>Y),P⁡(R​O​P​E),P⁡(X<Y))\theta=(P(X>Y),P(ROPE),P(X<Y)), where θi\theta_{i} represents the posterior probability that model X is better, the models are equivalent, and model Y is better, respectively. These samples represent the hypothetical differences in performance on a future unseen dataset [9]; generating N=50,000N=50,000 samples on a typical laptop computer takes only a few seconds, and conducting this comparison for all 4560 pairwise comparisons in the experiment below takes less than 10 minutes using the BayesianTestsML Python library.33
3

https://github.com/BayesianTestsML

Figure 3: A Bayesian posterior plot resulting from a Bayesian hierarchical correlated tt-test, which visualizes the results of Markov-Chain Monte Carlo (MCMC) sampling for the comparison of two models XX and YY. The estimated probability of each outcome is the proportion of samples that fall in each section of the plot.

The MCMC samples are used to estimate θ\theta by simply counting the proportion of samples for which θi\theta_{i} has the highest posterior probability. The results of this sampling can be visualized by projecting the (θX>Y,θR​O​P​E,θX<Y\theta_{X>Y},\theta_{ROPE},\theta_{X<Y}) triplets onto barycentric coordinates to produce a posterior plot, shown in Figure 3. Inspection of these plots can be useful for small comparisons, but for experiments with large models spaces, inspecting all k⁡(k−1)2\frac{k(k-1)}{2} pairwise plots is impractical.

This method is able to account for the different uncertainty which characterizes each dataset by estimating unique parameters for each dataset, and, because the hierarchical model applies shrinkage to the μi\mu_{i} values when estimating them jointly, it estimates them more accurately than previous approaches which use maximum likelihood estimation [9].

### 3.4 The Case for Bayesian Model Evaluation

In the survey presented above and in other work [21], we have described the common practices of predictive modeling experiments in learning analytics. These include (a) a massive space of potential models due to many data sources, feature types, and algorithms used; (b) relatively small collections of datasets, for example, even the largest prior MOOC studies of which we are aware evaluate around 40 MOOCs (i.e., [47, 17]) and (c) large individual datasets, which make repeated model-fitting undesirable, if not intractable.

These, along with more general scientific considerations common to model evaluation in any domain, give rise to a series of desiderata which any ideal model evaluation procedure must meet. We introduce the criteria individually below, and describe how each the model evaluation methods discussed above do or do not satisfy these criteria.

Computationally tractable: Statistical testing should require as little computational overhead as possible. It should scale well with the number of datasets NN, the number of models kk, and the dimensionality of the data. This consideration does not particularly count in favor of any of the schemes considered, but also does not rule any out. All are computationally tractible with consumer-level computing hardware. The MCMC sampling method used by the Bayesian method incurs a higher computational overhead than NHST, but for the modest NN used in most MOOC research (at most N=44N=44 in the largest known prior analysis [17]), the computational cost is negligible. For equally effective schemes, we might decide to choose the one which can provide the most efficient estimates.

Impose minimal assumptions on the data: An ideal method will make few assumptions about the underlying data, such as normality, symmetry, commensurability across datasets, sphericity, etc. This alone excludes many common parametric NHST methods, such the tt-test, ANOVA, or the naïve average method, which make strong assumptions which are not met by model performance data in practice [13]. While this excludes most parametric NHST methods, it does not provide a clear reason to prefer nonparametric NHST over Bayesianism.

Account for cross-validation: As discussed in section 3.2, the use of cross-validation requires correction for the overlap between the training data used in each fold. This is particularly important because cross-validation is widely used in learning analytics. As discussed in Section 3.2, the tt-test in particular shows highly elevated inflated Type I error rates and low inferential replicability with cross-validated model performance data. To avoid this, the method in Section 3.2 ranks models over each dataset, ignoring important information in the fold-level performance data (such as the variability of model performance across folds). The Bayesian procedure, in contrast, utilizes the fold-level data directly to compute estimates of the variability of each pairwise model comparison, as shown in Equation 5.

Robust to multiple comparisons As discussed in Section 2.1.2, more than 80% of the works surveyed compared more than two models. The practice of comparing many models is also often useful, allowing for the exploration of a diverse model space, providing many reference points, and allowing for benchmarking relative to other work. Model evaluation should therefore allow for many comparisons with minimal effect on inferential error rates. When existing NHST procedures are adjusted for multiple comparisons, these adjustments are often impractically conservative with large kk and small to moderate NN to avoid Type I error, as our case study demonstrates in Section 5 (see also [16]). In contrast, the Bayesian approach does not “accept” or “reject” hypotheses and is generally unconcerned with Type I errors as it only estimates posterior probabilities. A Bayesian hierarchical model can directly account for the uncertainty from multiple comparisons, and applies shrinkage to estimators to account for this uncertainty [23].

Test an informative H0H_{0}: In the case of the NHST in Section 3.2, we are testing a series of hypotheses of pairwise equivalence between the candidate models. That is, we are evaluating H0H_{0}: the performance of models XX and YY are exactly equivalent (while the naïve average does not test an H0H_{0}, here we could think of it as equivalent to an NHST that simply always rejects). However, as noted previously, an H0H_{0} of exactly equivalent performance is almost always false [1, 14]. This H0H_{0} has been called “the nil hypothesis” after the probability that this hypothesis is true [27, pp. 1000]. Particularly in the case of machine learning models, it is unlikely that any two algorithms have exactly equivalent performance. Tests of this hypothesis, even when properly interpreted, are not indicative of any likely true state of the world, and are potentially misleading.

Provide direct evidence about H0H_{0}: When conducting model evaluation, we are interested in directly drawing inferences about some H0H_{0}. NHST cannot prove the null hypothesis or provide direct evidence of it [14, 45], although they are commonly misinterpreted as doing so both in the broader scientific literature [8, 14, 8] and in several of the MOOC experiments surveyed here. The Bayesian procedure, in contrast, allows for direct inference about the probability of models having similar or equivalent performance, using the estimated posterior distribution of the difference in performance between two models.

Separate magnitude, uncertainty, and sample size during inference: The effects of the magnitude of observed differences, the uncertainty of estimates, and the number of data points should be separable in model evaluation. However, both the naïve average and NHST obscure the influence of each of these factors. The naïve average does so by simply ignoring all three factors. An NHST only provides a pp-value which reflects a mix of effect size and uncertainty [36], even when the observed effects might be too small to be considered practically significant, or might be associated with a high level of uncertainty. Even if the procedure itself might separate these factors, the reported pp-value does not allow the reader to differentiate between the magnitude of the effect, uncertainty, and sample size [1, 45]. This leads to the further complication that detecting a “significant” difference under a null hypothesis of equivalence only requires collecting enough data (or conducting enough runs of cross-validation), under which conditions H0H_{0} can always be rejected [8, 14, 15, 36, 45, 48]. By using a region of practical equivalence (ROPE), the Bayesian method separately estimates the magnitude and variability of each estimated effect (here, differences in AUC between a pair of models).

Together, these criteria collectively mount a strong imperative in favor of Bayesian model evaluation.

## 4 Case Study: Evaluating MOOC Dropout Models

In this section, we present and evaluate the results of an experiment which constructs and compares several dropout models across a large sample of MOOCs using the three model evaluation methods discussed (naïve average; NHST; Bayesian). Our goal in this section is twofold. First, such a side-by-side comparison stands not only to illuminate procedural and inferential differences between these approaches, but also demonstrate how they can produce different conclusions from the same underlying data in practice when evaluating many candidate models. Second, we hope to demonstrate interesting and useful results in this experiment: the data, feature extraction, and statistical modeling methods used here are common in applied predictive modeling research in learning analytics, but have not been collectively compared in previous work. For additional examples of case studies utilizing this method for classifier selection across multiple datasets, see [1, 9].

### 4.1 Data

The data used in this experiment are a large and diverse sample of N=48N=48 sessions of MOOCs offered by the University of Michigan on Coursera. These courses are from several diverse domains, including science and technology, finance, healthcare, politics, and literature. A summary of the data for the courses used is shown in Table 2. The data are used to predict a binary dropout label indicating whether a user showed any activity in the final week of the course.

| Metric
| Value

| Number of Sessions
| 48

| Number of Unique Courses
| 17

| Total Number of Active Students
| 117,028

| Total Number of Interactions
| 2,479,900

| Average Number of Active Students
| 2490 (2391)

| Average Length in weeks
| 9.8 (2.6)

| Average Number of Unique Forum Posters
| 507 (447)

| Average Number of Course Assignments
| 1.2 (0.9)

| Average Number of Quizzes
| 18 (16.8)

| Average Number of Human-Graded Quizzes
| 1.6 (1.5)

Table 2: Summary statistics for courses used in case study. Standard deviations in parentheses.

This dataset represents one of the largest MOOC dropout prediction studies to date in terms of number of courses evaluated.44
4

The largest-scale work on predictive modeling in MOOCs to date are [33, 34], which each build predictive models on 39 XuetangX MOOCs; and [47], which builds predictive models on 40 HarvardX MOOCs. This means the current experiment represents a reasonable upper bound for the number of datasets, NN, that a MOOC predictive modeling experiment might utilize (which serves as a limiting factor in the NHST procedure, as our results demonstrate).

### 4.2 Experimental Setup

Figure 4: Experiment overview.

The experimental setup, shown in Figure 4, is as follows: For each course session, we extract all four sets of features (clickstream, forum, assignments, all). We train each of the 96 candidate models on each feature set, using 5× 25\>\times\>2-fold cross-validation, using the same random cross-validation folds for every model, and recording the Area Under the Receiver Operating Characteristic curve (AUC) as the evaluation metric for each model. We retain the fold-level results (the model performance on the held-out model fold), which provides 10 estimates of model performance for every model on each session of the course. A sample of this data is shown in Table 5). We then apply the three methods for model evaluation to this data.

#### 4.2.1 Feature Extraction/Data Source

This process of transforming raw data into structured information suitable for use as input to a supervised learning algorithm is considered one of the most important and difficult tasks in predictive modeling in MOOCs [33, 39, 40]. This experiment is designed to provide insight into which of these data sources within the Coursera platform [10] might be most useful for MOOC dropout prediction. We evaluate four sets of features, each extracted from a single data source, with all individual features based on prior work:

- •

Clickstream: Counting-based features representing the number of accesses to various course pages, number of forum views, and number of video views. These features are common in activity-based dropout modeling [29, 49, e.g.]. This is the simplest and smallest feature set.

- •

Forum Posts: Natural language processing-based metrics which measure sentiment, text complexity, and posting activity gathered from [11, 40, 46].

- •

Assignments: Academic performance metrics derived from students’ quizzes, peer-graded assignments, in-video quizzes, and exams, including both simple features (e.g. average grade) as well as more complex features (e.g. number of submissions relative to the highest number of submissions by any student that week) [3, 30, 43]. Where courses used no assignments, models using this method defaulted to majority-class prediction.

- •

All: Union of the three features sets above.

All features and their definitions are shown in Table 3.

| Clickstream

|

Forum Views: Number of pageviews of forum pages.

|

Active Days: Number of days for which user registered any clickstream activity (maximum of 7).

|

Quiz Views: Number of pageviews of quiz attempt pages, as measured by clickstream features.

|

Exam Views: Number of pageviews of exam-type quiz pages, as measured by clickstream features.

|

Human-Graded Quiz Pageview: Number of pageviews of human-graded quiz pages, as measured by clickstream features.

| Assignments

|

Pre-Submission Lead Time: Time between a quiz submission and deadline for all submissions; discretized buckets for t≥7t\geq 7 days, 3≤t<73\leq t<7, 1≤t<31\leq t<3, 0≤t<10\leq t<1, and late.

|

Total Raw Points: Sum of total raw points earned on quizzes.

|

Average Raw Score*: Average raw score on all assignments.

|

Raw Points Per Submission: Total raw points divided by total submissions.

|

Total quiz submissions: Total count of quiz submissions.

|

Percent of allowed submissions: Total count of quiz submissions as a percent of the maximum allowed submissions.

|

Percent of max student submissions: A student total number of quiz submissions as a percent of the maximum number of submissions made by any student in the course.

|

Correct submissions percent*: Percentage of the total submissions that were correct.

|

Change in weekly average*: Difference between current week average and previous week average quiz grade.

| Forum

|

Number of Posts: Total number of posts.

|

Number of Replies: Number of posts by user which were replies to other users (i.e., not to themselves, and not first post in thread).

|

Average Post Sentiment: Average net sentiment of posts (positive - negative) [24].

|

Average Post Length: Average length of posts, in characters.

|

Positive Posts: Number of posts with net sentiment ≥1\geq 1 standard deviation above thread average.

|

Negative Posts: Number of posts with net sentiment ≤−1\leq-1 standard deviation below thread average.

|

Neutral Posts: Number of posts with net sentiment within 1 standard deviation of thread average.

|

Sentiment Relative to Thread: Average of (post sentiment - avg sentiment for thread).

|

Threads Started: Total number of threads initiated by student.

|

Unique Words/Bigrams: Count of unique words/bigrams used across all posts.

|

Flesch Reading Ease: Flesch Reading Ease score, discretized into separate features in increments of 10 from 0 to 100 [28].

|

Flesch-Kincaid Grade Level: Flesch-Kincaid grade level, discretized into separate features in increments of 1 from 0 to 20 [28].

|

Net Votes Received: Total net upvotes users’ posts received (positive - negative).

Table 3: Feature name and definition by category. Each feature is calculated at the student-week level, resulting in p⋅np\cdot n features at week nn. Features marked with a (*) were calculated by quiz type (homework, quiz, and video), resulting in three different features, one per quiz type, using that definition.

#### 4.2.2 Algorithms and Hyperparameters

We consider the following models in our experiment: (1) classical decision trees (CART) [7], (2) L2 (or “ridge”) regularized logistic regression (L2LR); (3) gradient boosted tree (Adaboost) [12], used as a a stand-in for the widely used [21] random forest method55
5

The random forest method did not allow us to test consistent values of the mtry parameter, number of variables to consider at each split, because this value depends on the number of variables in a dataset, and our experiment requires testing feature sets with different numbers of dimensions.; (4) support vector machine (SVM) with linear kernel; (5) naïve Bayes (NB). These represent five of the most commonly used modeling algorithm in predictive models of student success in MOOCs [21]. A summary of the models considered, and any special preprocessing, is shown in Table 4. In addition to constituting a representative sample of the models most often used for dropout modeling tasks, these algorithms represent a broad spectrum of model types, including relatively simple, high-bias parametric models and complex, flexible, nonparametric models.

| Algorithm
| Hyperparameters Tuned
| Total Models
|

| Classification Tree
| Cost-complexity parameter (c​pcp)
| 4
|

| Logistic Regression
| L2 (ridge) penalty term (λ\lambda)
| 5
|

| Adaboost
|

| Boosting Algorithm (“Real Adaboost”, M1)

| Number of iterations

| 6
|

| SVM *, †
| Cost (γ\gamma)
| 5
|

| Naïve Bayes *
|

| Laplacian smoothing (f​LfL)

| Kernel

| 4
|

| Total
|
| 24
|

Table 4: Algorithms used and hyperparameters tuned for each. Each (algorithm, hyperparameter) set was used with each of the four feature types, yielding a total of 24×4=9624\times 4=96 models. Preprocessing codes: *indicates zero-variance predictors, if any, were dropped for model training (as a requirement of model-fitting algorithms); †indicates predictors were centered and scaled.

| AUC
| Resample
| Course
| Session
| Model

| 0.946
| Fold1.Rep1
| Digital Democracy
| 1
| CART(c​p=0.01cp=0.01, Features = All)

| 0.937
| Fold1.Rep1
| Digital Democracy
| 1
| CART(c​p=0.1cp=0.1, Features = All)

| 0.500
| Fold1.Rep1
| Digital Democracy
| 1
| CART(c​p=1cp=1, Features = All)

| 0.941
| Fold1.Rep2
| Digital Democracy
| 1
| CART(c​p=0.001cp=0.001, Features = All)

| …
| …
| …
| …
| …

| 0.748
| Fold1.Rep1
| Digital Democracy
| 1
| L2LR (λ=0.1\lambda=0.1, Features = Clickstream)

| 0.742
| Fold1.Rep1
| Digital Democracy
| 1
| L2LR (λ=0.01\lambda=0.01, Features = Clickstream)

| 0.743
| Fold1.Rep1
| Digital Democracy
| 1
| L2LR (λ=0.001\lambda=0.001, Features = Clickstream)

| 0.701
| Fold2.Rep1
| Digital Democracy
| 1
| L2LR (λ=1\lambda=1, Features = Clickstream)

| …
| …
| …
| …
| …

| 0.523
| Fold1.Rep1
| Digital Democracy
| 1
| SVM (γ=10\gamma=10, Features = Forum)

| 0.529
| Fold1.Rep1
| Digital Democracy
| 1
| SVM (γ=1\gamma=1, Features = Forum)

| 0.517
| Fold1.Rep1
| Digital Democracy
| 1
| SVM (γ=0.1\gamma=0.1, Features = Forum)

| 0.507
| Fold2.Rep1
| Digital Democracy
| 1
| SVM (γ=10\gamma=10, Features = Forum)

| 0.508
| Fold2.Rep1
| Digital Democracy
| 1
| SVM (γ=1\gamma=1, Features = Forum)

Table 5: A sample of the experimental data generated. Each row represents a specific feature/algorithm/hyperparameter model on a specific cross-validation fold; all models were evaluated on identical folds.

## 5 Results Analysis

With four feature sets, 24 candidate models representing all algorithm/hyperparameter settings, and 10 iterations of cross-validation on 48 course sessions, this resulted in a total of 4×24×10×48=46,0804\times 24\times 10\times 48=46,080 total observations of model performance. We apply each method (naïve average, NHST, and Bayesian) in order to identify the family of “best” models, which we define as:

Family of best models: a set ℱ\mathcal{F} of mm models, selected from a pool of NN candidate models, which have the best predicted performance on an unseen dataset. All models f∈ℱf\in\mathcal{F} have equivalent (or practically equivalent) generalization performance to all others in ℱ\mathcal{F}, but better performance than any model not in ℱ\mathcal{F}. Models f∈ℱf\in\mathcal{F} are sorted in descending order of performance, such that ℱ={f1>f2>…>fm}\mathcal{F}=\{f_{1}>f_{2}>\ldots>f_{m}\}.

All three model evaluation methods provide identical recommendations about the highest-performing model in this experiment (e.g. f1,n​a​i​v​e=f1,N​H​S​T=f1,B​a​y​e​sf_{1,naive}=f_{1,NHST}=f_{1,Bayes}): while differences are possible between the Bayesian method, which uses fold-level data, and the other two methods, which use average performance and rankings, the model performance was consistent enough that such differences in ℱ\mathcal{F} were not observed here. However, these methods vary in terms of (a) the statistical inferences they support; (b) the size of ℱ\mathcal{F}, and (c) their ability to discriminate between pairwise comparisons across entire space of models, even those not within ℱ\mathcal{F} (we explore this because experiments often seek to evaluate results besides the composition of ℱ\mathcal{F}). We demonstrate (i) the NHST method’s limitations with the modest number of comparisons being performed on this dataset, which results in an inability to discern differences between more than 50% of the models considered and a family of nearly 20 “best” models; (ii) that the Bayesian method generates the most robust and reliable inferences about model performance; and (iii) that the Bayesian method supports useful inferences about the relative performance of many features and algorithms for dropout prediction in MOOCs.

### 5.1 Naïve Average Method

Recall in the naïve average model evaluation approach, the experimental results are simply averaged by model, sorted according to performance, and the model with the best average performance is selected (assuming no ties).

Applying naïve average method, we select ℱn​a​i​v​e\mathcal{F}_{naive} as the single model with the highest average performance. This is the decision tree (CART) algorithm, with all features and a cost-complexity parameter of 0.001. The “family” of best models is thus a family of one (this corresponds to the top row of Table 6). With the naïve average method, every pairwise difference is considered significant, regardless of the magnitude of any observed difference, the total number of models tested, or the number of observations collected in the experiment: the observed differences are assumed to be accurate, not spurious, and large enough to be practically significant.

These results make clear how problematic the naïve average method is. The difference in average AUC between f1,n​a​i​v​ef_{1,naive} and the next-highest performing algorithm is less than 0.003 (see Table 7). This difference is indeed small enough to be spurious, practically useless, or both. With 96×952\frac{96\times 95}{2} pairwise comparisons, we might expect to observe some differences in model performance due to randomness alone. Thinking in terms of Tukey’s card analogy, the question of how many “deals” we made, and therefore how surprised we should be by the hand we have been dealt, is not considered by the naïve average method.

Furthermore, the naïve average method provides no principled estimate of the confidence or significance of our results, which provides no basis for comparison for future work which attempts to replicate these findings on new data: is our confidence low, in which case a different result would be surprising? Or is our confidence quite high, in which case we would expect similarly strong results in replications? The naïve average method provides no answer.

Finally, because ℱn​a​i​v​e\mathcal{F}_{naive} contains only one model, the naïve average method does not allow us to easily introduce other considerations, such as model interpretability or training time, into our decision despite the fact that many models seem to have performance reasonably close to the highest-performing model. If we had a set of practically equivalent “best” models to choose from (if ℱ\mathcal{F} contained more than a single element), we might select a final preferred model based on these other considerations. However, under the naïve average method, we only ever have a single model in ℱn​a​i​v​e\mathcal{F}_{naive}, leaving no principled method for model selection even when the observed differences with other models are arbitrarily small.

### 5.2 NHST Method: Frequentist Nemenyi Test

The NHST procedure recommended in section 3.2 compares models via a two-stage, nonparametric test. Recall that first, the Friedman test (Equation 1) is applied. If this test indicates a significant difference (as it did in this experiment), a post-hoc Nemenyi test is conducted on all pairwise comparisons to determine where significant differences between individual models may exist. Typically, the results of this procedure are reported using a Critical Difference (CD) diagram, shown in Figure 5. However, the CD diagram is difficult to interpret with a large number of models, which is one way in which this procedure breaks down under large numbers of comparisons; we instead present a “windowpane plot” of the results in Figure 6.

Figure 5: Critical Difference (CD) diagram for models evaluated in this experiment. The bold CD bars connect models statistically indistinguishable at α=0.05\alpha=0.05; ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} is indicated in orange. This figure illustrates the breakdown of the CD diagram with large numbers of comparisons: the diagram is difficult to read and interpret, with large groups of statistically indistinguishable models.

The models in ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} are shown in Table 6, and correspond to the set of models in Figure 5 linked by an orange CD bar. They are also shown in the windowpane plot in Figure 6 as the models which have white-colored cells in the top row (indicating that the models are statistically indistinguishable from the top-ranked model).

| Algorithm
| Feature Type
| Hyperparameters
|

Avg. Rank

|

Avg. AUC

|

Diff. In Ranks

|

Diff. In AUC

| CART
| All
| c​p=0.001cp=0.001
|

3.376

|

0.901

|

NA

|

NA

| Adaboost
| All
| N​I​t​e​r=50NIter=50, Boosting = M1
|

3.978

|

0.899

|

-0.602

|

0.002

| Adaboost
| All
| N​I​t​e​r=100NIter=100, Boosting = M1
|

4.118

|

0.899

|

-0.742

|

0.002

| Adaboost
| All
| N​I​t​e​r=500NIter=500, Boosting = M1
|

5.198

|

0.897

|

-1.822

|

0.004

| Adaboost
| Clickstream
| N​I​t​e​r=50NIter=50, Boosting = M1
|

6.725

|

0.89

|

-3.349

|

0.011

| Adaboost
| Clickstream
| N​I​t​e​r=100NIter=100, Boosting = M1
|

7.344

|

0.889

|

-3.968

|

0.012

| Adaboost
| Clickstream
| N​I​t​e​r=500NIter=500, Boosting = M1
|

8.704

|

0.887

|

-5.328

|

0.014

| Naïve Bayes
| Clickstream
| f​L=1fL=1, Kernel = True
|

10.708

|

0.872

|

-7.332

|

0.029

| Naïve Bayes
| Clickstream
| f​L=0fL=0, Kernel = True
|

10.708

|

0.872

|

-7.332

|

0.029

| Naïve Bayes
| Clickstream
| f​L=1fL=1, Kernel = False
|

19.288

|

0.788

|

-15.911

|

0.113

| Naïve Bayes
| Clickstream
| f​L=0fL=0, Kernel = False
|

19.288

|

0.788

|

-15.911

|

0.113

| L2LR
| All
| λ=0.01\lambda=0.01
|

19.521

|

0.78

|

-16.145

|

0.121

| L2LR
| All
| λ=0\lambda=0
|

20.036

|

0.779

|

-16.66

|

0.121

| L2LR
| All
| λ=0.001\lambda=0.001
|

20.036

|

0.779

|

-16.66

|

0.121

| L2LR
| All
| λ=0.1\lambda=0.1
|

20.039

|

0.778

|

-16.662

|

0.123

| L2LR
| All
| λ=1\lambda=1
|

24.258

|

0.752

|

-20.882

|

0.149

| L2LR
| Clickstream
| λ=0.001\lambda=0.001
|

24.578

|

0.75

|

-21.202

|

0.151

| L2LR
| Clickstream
| λ=0\lambda=0
|

24.578

|

0.75

|

-21.202

|

0.151

| L2LR
| Clickstream
| λ=0.01\lambda=0.01
|

24.744

|

0.75

|

-21.368

|

0.151

Table 6: Family of models ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} which are statistically indistinguishable from the “best” model with differences in average rank less than the critical difference of C​D=22.5936CD=22.5936 relative to the highest-ranked model f~1,N​H​S​T\widetilde{f}_{1,NHST}. All differences are relative to f~1,N​H​S​T\widetilde{f}_{1,NHST}, which has average rank 3.376, average AUC 0.901.

The large size of ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST}, which consists of 19 models, is due to the large critical difference CD, computed via Equation 2. This is the NHST’s control for the number of comparisons relative to the number of datasets. The large number of hypotheses in this experiment drastically reduces the NHST’s ability to discriminate between closely-ranked models. As Figure 5 shows, the orange CD bar connecting the models in ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} occupies nearly 25% of the length of the number line of possible rankings. The procedure’s discrimination could be improved if the procedure used fold-level data (which would increase the sample size NN), but this would require applying a correction for the overlapping training samples. Such a correction to this test has not, to the authors’ knowledge, been theoretically evaluated.

In sections 3.2 and 3.3, we discussed how NHST procedures fail to differentiate between the magnitude and the uncertainty of the effects under examination during model evaluation. This is reflected in the results shown in Table 6. The NHST procedure does not discriminate between models with large differences in performance (high magnitude) but high variability (high uncertainty), and models with small differences in performance (low magnitude) but also low variability (low uncertainty). This yields an ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} where models may either show (i) large differences in average performance from the best model, but with large enough variability that this might not constitute a real effect, or (ii) models with small average differences but low variability.

As an example, consider the Adaboost models in Table 6 (the six highest-performing models after the decision tree). For these models, the magnitude is quite small, with the difference in AUC from the highest-performing model never greater than 0.01, and we might agree with the NHST’s decision to include these in ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST}. In contrast, each of the logistic regression models shown in the lower portion of Table 6 has an average AUC more than 0.1 worse than the highest-performing model – a magnitude large enough to be considered practically important. However, the NHST treats both models as equivalent to f1f_{1}. A user simply presented with ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} would have no way of differentiating between the Adaboost models, which achieved comparable performance to f~1,N​H​S​T\widetilde{f}_{1,NHST} with low variability, and the logistic regression models, which achieved inferior average performance but higher variability.

Figure 6 also shows that the NHST procedure makes decisions in only 44.08% of the pairwise comparisons conducted (those indicated by nonwhite cells). This provides little information about many pairwise model comparisons; it will make fewer decisions as the number of comparisons kk grows for a fixed number of datasets NN. This illustrates how the frequentist method is only able to make decisions when the observed differences in performance are large (or have low variability) and the hypothesis space moderate, with significant differences only detected between the highest- and lowest-performing models in the sample. This leaves little room for interpretation of the relative difference between, for example, models using quiz vs. forum features (and leads us to conclude that, in most cases, all we can do is draw no conclusion based on the observed data).

Figure 6: A “windowpane” plot showing decisions for frequentist method (adapted from [37] via [23]). All models are shown along each axis in identical order of decreasing performance. Cells are labeled with the rank of the model along the x axis.

Finally, we must correct an abuse of our notation of ℱ\mathcal{F}. While we would like to conclude that the models shown in Table 6 are the “best” models, and while this is often implied in the analysis of NHST procedures, to do so would be incorrect. Instead, we are not able to draw any conclusions regarding the differences in performance between these models using the NHST procedure. For these models, “the experimental data is not sufficient to reach any conclusion” [13, pp. 14]. This is the inferential equivalent of not being able to reject the null hypothesis, and is why we use the notation of ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST} instead of ℱN​H​S​T\mathcal{F}_{NHST}. A frequentist approach can never prove the the null hypothesis of equivalent performance [9, 32], and instead only produces inconclusive results. NHST can therefore never positively identify ℱN​H​S​T\mathcal{F}_{NHST} as defined.

This is a scientifically unsatisfying result, and it is crucial to the argument of this work: the NHST does not tell us about what we want to know about our experiment. In fact, it allows us only to draw conclusions conditional on a nil hypothesis that is almost certainly false: that all of the 96 models evaluated above have exactly equivalent performance to all other models. Estimating the probability of observing our results conditional on this hypothesis yields little useful information about the observed data and no information about ℱ\mathcal{F}, or about pairwise comparisons between more than half of the models in our experiment.

### 5.3 Bayesian Model Evaluation Method

Recall that the Bayesian method, described in Section 3.3, uses the differences in AUC for each pair of models on each cross-validation fold to estimate θ=(P⁡(X>Y),P⁡(R​O​P​E),P⁡(X<Y))\theta=(P(X>Y),P(ROPE),P(X<Y)). ROPE is the “region of practical equivalence,” and denotes that the difference between XX and YY is smaller than some pre-specified threshold. This can be thought of as creating a posterior plot, as in Figure 3, for each pair of models, and using this posterior distribution to compute each probability in θ\theta. For this experiment, as in previous work using this procedure [1], we use R​O​P​E=0.01ROPE=0.01; that is, models are considered practically equivalent if the difference in their AUC is smaller than 0.01.

| Algorithm
| Feature Type
| Hyperparameters
|

Avg. Rank

|

Avg. AUC

|

Diff. In Ranks

|

Diff. In AUC

| CART
| All
| c​p=0.001cp=0.001
|

3.376

|

0.901

|

NA

|

NA

| Adaboost
| All
| N​I​t​e​r=50NIter=50, Boosting = M1
|

3.978

|

0.899

|

-0.602

|

0.002

| Adaboost
| All
| N​I​t​e​r=100NIter=100, Boosting = M1
|

4.118

|

0.899

|

-0.742

|

0.002

| Adaboost
| All
| N​I​t​e​r=500NIter=500, Boosting = M1
|

5.198

|

0.897

|

-1.822

|

0.004

Table 7: Family of models ℱB​a​y​e​s\mathcal{F}_{Bayes}.

The Bayesian procedure thus allows us to differentiate between cases where the magnitude of the difference is small (the difference |X−Y|≤R​O​P​E|X-Y|\leq ROPE, and therefore the models are “practically equivalent”), and cases where this magnitude is large (|X−Y|>R​O​P​E|X-Y|>ROPE, the model performance is meaningfully different). This is useful because we tend only to care about the latter: if the difference in performance of two models is small, we might consider other aspects of the model, such as training time or interpretability, in order to select which to use.

We present ℱB​a​y​e​s\mathcal{F}_{Bayes} in Table 7 and Figure 7. The Bayesian procedure returns a more precise family of “best” models than NHST: ℱB​a​y​e​s\mathcal{F}_{Bayes} contains only four models. All models in ℱB​a​y​e​s\mathcal{F}_{Bayes} have a P⁡(R​O​P​E)P(ROPE) greater than the decision threshold of 0.95. This threshold value is selected to replicate [1]; adjustments of the threshold even to 0.999 had minimal effects on the decision in most cases (the model has high confidence, given the data).

Additionally, there is an important epistemic distinction between ℱB​a​y​e​s\mathcal{F}_{Bayes} and its frequentist counterpart ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST}. Using NHST, recall that we were not able to conclude anything about the models in ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST}: we cannot reject the null hypothesis of equivalence, but we do not prove or provide evidence that these models are equivalent. However, the Bayesian procedure directly estimates the probability of two models being equal: this is P⁡(R​O​P​E)P(ROPE), the probability that models XX and YY are practically equivalent. Being able to model practical equivalence is quite beneficial for a large hypothesis space: there are many comparisons for which the model performance is reliably within the region of practical equivalence (ROPE), and the Bayesian approach can assign high probability to ROPE in such cases. In contrast, the frequentist paradigm can never conclude that no difference exists; indeed, given infinite data, as noted above, the frequentist paradigm will always conclude that a significant different exists (even when this difference is very small).

Figure 7: Windowpane plot showing ℱB​a​y​e​s\mathcal{F}_{Bayes}. The Bayesian method estimates the posterior probability that two models are within the “region of practical equivalence” (ROPE), which is not estimable via NHST.

ℱB​a​y​e​s\mathcal{F}_{Bayes} is smaller than ℱ~N​H​S​T\widetilde{\mathcal{F}}_{NHST}, in part because ℱB​a​y​e​s\mathcal{F}_{Bayes} is sensitive to the magnitude of the difference between models. Only those models with small differences in performance relative to the best model f1f_{1} are in ℱB​a​y​e​s\mathcal{F}_{Bayes}; those with large, but highly variable, differences from f1f_{1} are not). The Bayesian method allows us to make substantive conclusions about those models. These conclusions are not conditional on the assumption of a null hypothesis of equivalent performance (which is almost certainly incorrect in most cases), and is instead only conditional on the data we observe.

While the naïve average approach may be favored for its ability to yield a small, precise ℱ\mathcal{F} consisting of only a single model, the Bayesian approach nearly matches the precision of using a naïve average approach in this case. However, the Bayesian method does so without making unwarranted assumptions about the significance of observed differences – recall that the naïve average method simply assumes that all differences are significant. Instead, the Bayesian approach uses hierarchical modeling to directly estimate the probability that each pair of models is practically equivalent, given their observed performance.

Above, we demonstrated how the NHST method is especially sensitive to the number of comparisons, for a fixed number of datasets, in order to control the size of the cricial difference. Additionally, this requires researchers to track, report, and account for the full scope of comparisons performed in the course of an experiment – despite the fact that increasing the number of comparisons will reduce their ability to detect a statistically significant effect (by increasing the size of the CD). For Bayesian model evaluation, large numbers of comparisons are generally not considered to be a concern [23], because the concept of a Type I error does not exist under a Bayesian framework. Additionally, the hierarchical model accounts for the variability within and across models, reducing the estimated effect sizes (in this case, differences in observed performance) as necessary [23].

### 5.4 Implications for Predictive Modeling in MOOCs

In previous sections, we focused on the methodological implications of our case study. In this section, we evaluate the practical conclusions from the case study. We intended this experiment to be useful, interesting, and realistic, and we present the main findings with respect to predictive modeling in MOOCs here (using the results of the Bayesian analysis).

Table 7 and Figure 7 both show that all models in ℱB​a​y​e​s\mathcal{F}_{Bayes} use all features – clickstream, forum, and assignments: models that used these combined features made better predictions than those with only one of the feature sets. Additionally, Figure 7 provides further information on which individual feature sets (and data sources) demonstrated the best performance: by inspecting the model rankings, and the large “blocks” of models which are practically equivalent, we see that models using clickstream features consistently outperformed models using forum or assignment features, and in many cases clickstream-only models were competitive with, or practically equivalent to, models using all features. In most cases, models with forum or assignment features produced practically equivalent performance, regardless of algorithm and hyperparameters used, as indicated by the large “ROPE” block in the lower right-hand section of Figure 7. This suggests that no model was able to extract substantially more information than any other from the forum and assignment features; we hypothesize that this is because these features are highly sparse and are only available for a small subset of students who choose to complete those optional activities.

In terms of particular algorithms, ℱB​a​y​e​s\mathcal{F}_{Bayes} shows that nonparametric tree-based models show the best performance across the large and diverse sample of MOOCs used here. This comports with current practice in learning analytics, where tree-based methods are already widely used [21].

Additionally, Figure 7 demonstrates that, for many algorithms, hyperparameter tuning appears to have had little effect, especially relative to the obvious effects of feature type: many different tunings of otherwise-identical models are practically equivalent, or even adjacent in the average model rankings. This suggests that future modeling efforts might achieve the most substantial performance improvements from feature engineering using a rich data source, such as the clickstream, and not from extensively tuning sophisticated algorithms on sparse or uninformative feature sets. Using a reasonable default hyperparameter setting might, in most cases, be sufficient to realize most of the models’ performance benefits if the feature set is of high quality, as our experiment included the default hyperparameters for each model.

Often, predictive models in learning analytics require interpretability in order to communicate the findings to stakeholders or inspect the model itself. This case study demonstrates several findings of interest here. First, it shows that a highly interpretable model (CART) can achieve excellent performance. Other interpretable models, such as the L2LR model (models 15-23 in Figure 7) also achieved relatively strong performance. Second, the procedure demonstrated here could be implemented with any class of candidate models; if a researcher wished only to use a certain type of highly interpretable algorothm (such as the logistic regression models considered), these could be used as the candidate model space instead. Third, in a case where interpretability is perhaps secondary to predictive performance but still important, the most interpretable model could be selected from ℱ\mathcal{F}; in the case of ℱB​a​y​e​s\mathcal{F}_{Bayes}, this would likely be the CART model.

## 6 Conclusion and Notes for Practice

In this work, we are concerned with advancing the state of the learning analytics field with respect to the evaluation of predictive models. We presented the results of a comprehensive literature review to assess the state of the practice in the field, and presented an overview of several techniques for model evaluation. By applying these results to a realistic and comprehensive case study using a large set of MOOC data, we demonstrated the differences in substantive conclusions supported by each method. In particular, we demonstrated the power of Bayesian model evaluation to draw highly precise, informative conclusions about the performance of feature-algorithm-hyperparamter combinations, even across a large space of candidate models. Under the Bayesian model evaluation method, our case study specifically demonstrated the importance of feature extraction to model performance, and in particular demonstrated the predictive performance of clickstream-based features for dropout prediction (and the relatively poor performance achieved by using only forum- or assignment-based features, regardless of the statistical model used).

We hope that this work contributes to a growing movement in the field toward addressing several of the existing barriers to rigorous model evaluation in learning analytics and across domains, including those described in Section 2.2.

While the fields of learning analytics and educational data mining are only a decade old66
6

Based on annual conferences in the area, though we note that educational data mining itself has roots in the much older Artificial Intelligence in Education (AIED) community. the techniques we have presented here borrow from the work of others done over the last 15 years in the broader machine learning community, and largely reflect the evolution of the field of machine learning as a whole as it develops methods to address new challenges brought by the expansion of data science and computing.

With the growth in the size of datasets available (e.g. MOOCs), and the ability to run thousands of permutations of analyses on desktop hardware, we are concerned with the lack of rigor when selecting and reporting on the “best” predictive model. This is especially important as there a number of pragmatic elements when operationalizing predictive models – computational speed, robustness in the face of missing data, and interpretability – all of which might influence adoption ability. In this work we have shed light on techniques which can help inform these choices, and we look forward to the growth of rigor in the community as a result.

## References

- [1]

A. Benavoli, G. Corani, J. Demsar, and M. Zaffalon.

Time for a change: a tutorial for comparing multiple classifiers
through bayesian analysis.

J. Mach. Learn. Res., 18(1):2653–2688, 2017.

- [2]

Y. Benjamini and Y. Hochberg.

Controlling the false discovery rate: A practical and powerful
approach to multiple testing.

J. R. Stat. Soc. Series B Stat. Methodol., 57(1):289–300,
1995.

- [3]

M. L. Bote-Lorenzo and E. Gómez-Sánchez.

Predicting the decrease of engagement indicators in a MOOC.

In Proceedings of the Seventh International Learning Analytics
& Knowledge Conference, LAK ’17, pages 143–147, New York, NY, USA, 2017.
ACM.

- [4]

R. R. Bouckaert.

Choosing between two learning algorithms based on calibrated tests.

In Proceedings of the Twentieth International Conference on
Machine Learning (ICML-2003), 2003.

- [5]

R. R. Bouckaert.

Estimating replicability of classifier learning experiments.

In Proceedings of the Twenty-first International Conference on
Machine Learning, ICML ’04, pages 15–, New York, NY, USA, 2004. ACM.

- [6]

R. R. Bouckaert and E. Frank.

Evaluating the replicability of significance tests for comparing
learning algorithms.

In Advances in Knowledge Discovery and Data Mining, pages
3–12. Springer, Berlin, Heidelberg, May 2004.

- [7]

L. Breiman, J. Friedman, C. J. Stone, and R. A. Olshen.

Classification and regression trees.

CRC press, 1984.

- [8]

J. Cohen.

The Earth Is Round (p <.05).

American Psychologist, 49(12):997–1003, Dec. 1994.

- [9]

G. Corani, A. Benavoli, J. Demšar, F. Mangili, and M. Zaffalon.

Statistical comparison of classifiers through bayesian hierarchical
modelling.

Mach. Learn., 106(11):1817–1837, 2017.

- [10]

Coursera.

Coursera Data Export Procedures.

Coursera, June 2013.

- [11]

S. Crossley, L. Paquette, M. Dascalu, D. S. McNamara, and R. S. Baker.

Combining click-stream data with NLP tools to better understand
MOOC completion.

In Proceedings of the Sixth International Conference on Learning
Analytics & Knowledge, pages 6–14, 2016.

- [12]

M. Culp, K. Johnson, and G. Michailidis.

ada: An r package for stochastic boosting.

J. Stat. Softw., 17(2):9, 2006.

- [13]

J. Demšar.

Statistical comparisons of classifiers over multiple data sets.

J. Mach. Learn. Res., 7(Jan):1–30, 2006.

- [14]

J. Demšar.

On the appropriateness of statistical tests in machine learning.

In Workshop on Evaluation Methods for Machine Learning in
conjunction with ICML, 2008.

- [15]

T. G. Dietterich.

Approximate statistical tests for comparing supervised classification
learning algorithms.

Neural Comput., 10(7):1895–1923, Sept. 1998.

- [16]

B. Efron and T. Hastie.

Computer Age Statistical Inference.

Cambridge University Press, 2016.

- [17]

B. J. Evans, R. B. Baker, and T. S. Dee.

Persistence patterns in massive open online courses (MOOCs).

J. Higher Educ., 87(2):206–242, Mar. 2016.

- [18]

R. A. Fisher.

Statistical methods for research workers.

Genesis Publishing Pvt Ltd, 1925.

- [19]

J. Friedman, T. Hastie, and R. Tibshirani.

The elements of statistical learning, volume 1.

Springer series in statistics New York, 2001.

- [20]

M. Friedman.

A comparison of alternative tests of significance for the problem of
m rankings.

Ann. Math. Stat., 11(1):86–92, 1940.

- [21]

J. Gardner and C. Brooks.

Student success prediction in MOOCs.

User Modeling and User-Adapted Interaction, 2018.

- [22]

A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B.
Rubin.

Bayesian data analysis.

CRC Press Boca Raton, FL, 2014.

- [23]

A. Gelman, J. Hill, and M. Yajima.

Why we (usually) don’t have to worry about multiple comparisons.

J. Res. Educ. Eff., 5(2):189–211, 2012.

- [24]

C. J. Hutto and E. Gilbert.

VADER: A parsimonious Rule-Based model for sentiment analysis of
social media text.

In Eighth International AAAI Conference on Weblogs and Social
Media, May 2014.

- [25]

R. Islam, P. Henderson, M. Gomrokchi, and D. Precup.

Reproducibility of benchmarked deep reinforcement learning tasks for
continuous control.

Aug. 2017.

- [26]

N. Japkowicz and M. Shah.

Evaluating Learning Algorithms: A Classification Perspective.

Cambridge University Press, Jan. 2011.

- [27]

D. D. Jensen and M. D. Schmill.

Adjusting for multiple comparisons in decision tree pruning.

In KDD, pages 195–198. ocs.aaai.org, 1997.

- [28]

J. P. Kincaid, R. P. Fishburne, Jr, R. L. Rogers, and B. S. Chissom.

Derivation of new readability formulas (automated readability index,
fog count and flesch reading ease formula) for navy enlisted personnel.

Technical report, Naval Technical Training Command Millington TN
Research Branch, 1975.

- [29]

M. Kloft, F. Stiehler, Z. Zheng, and N. Pinkwart.

Predicting MOOC dropout over weeks using machine learning methods.

In Proceedings of the EMNLP 2014 Workshop on Analysis of Large
Scale Social Interaction in MOOCs, pages 60–65. aclweb.org, 2014.

- [30]

S. Kotsiantis, K. Patriarcheas, and M. Xenos.

A combinational incremental ensemble of classifiers as a technique
for predicting students’ performance in distance education.

Knowledge-Based Systems, 23(6):529–535, Aug. 2010.

- [31]

J. Kruschke.

Doing Bayesian Data Analysis: A Tutorial with R, JAGS, and
Stan.

Academic Press, Nov. 2014.

- [32]

J. K. Kruschke.

Bayesian estimation supersedes the t test.

J. Exp. Psychol. Gen., 142(2):573–603, May 2013.

- [33]

W. Li, M. Gao, H. Li, Q. Xiong, J. Wen, and Z. Wu.

Dropout prediction in MOOCs using behavior features and multi-view
semi-supervised learning.

In 2016 International Joint Conference on Neural Networks
(IJCNN), pages 3130–3137, July 2016.

- [34]

J. Liang, C. Li, and L. Zheng.

Machine learning application in MOOCs: Dropout prediction.

In 2016 11th Intl. Conf. on Computer Science Education
(ICCSE), pages 52–57, 2016.

- [35]

G. Madjarov, D. Kocev, D. Gjorgjevikj, and S. Džeroski.

An extensive experimental comparison of methods for multi-label
learning.

Pattern Recognit., 45(9):3084–3104, 2012.

- [36]

B. B. McShane, D. Gal, A. Gelman, C. Robert, and J. L. Tackett.

Abandon statistical significance.

Sept. 2017.

- [37]

I. V. S. Mullis.

NAEP 1992 mathematics report card for the nation and the states.

Technical Report ED360190, Education Information Branch, Office of
Educational Research and Improvement, U.S. Department of Education, 1993.

- [38]

C. Nadeau and Y. Bengio.

Inference for the generalization error.

Mach. Learn., 52(3):239–281, 2003.

- [39]

S. Nagrecha, J. Z. Dillon, and N. V. Chawla.

MOOC dropout prediction: Lessons learned from making pipelines
interpretable.

In Proceedings of the 26th International Conference on World
Wide Web Companion, WWW ’17 Companion, pages 351–359, Republic and Canton
of Geneva, Switzerland, 2017. International World Wide Web Conferences
Steering Committee.

- [40]

C. Robinson, M. Yeomans, J. Reich, C. Hulleman, and H. Gehlbach.

Forecasting student achievement in MOOCs with natural language
processing.

In Proceedings of the Sixth International Conference on Learning
Analytics & Knowledge, LAK ’16, pages 383–387, New York, NY, USA, 2016.
ACM.

- [41]

C. Taylor, K. Veeramachaneni, and U.-M. O’Reilly.

Likely to stop? predicting stopout in massive open online courses.

Aug. 2014.

- [42]

M. Vartak, H. Subramanyam, W.-E. Lee, S. Viswanathan, S. Husnoo, S. Madden, and
M. Zaharia.

M odel DB: a system for machine learning model management.

In Proceedings of the Workshop on Human-In-the-Loop Data
Analytics, page 14. dl.acm.org, 2016.

- [43]

K. Veeramachaneni, U.-M. O’Reilly, and C. Taylor.

Towards feature engineering at scale for data from massive open
online courses.

July 2014.

- [44]

Y. Wang, J. Li, and Y. Li.

Choosing between two classification learning algorithms based on
calibrated balanced 5x2 Cross-Validated F-Test.

Neural Process. Letters, pages 1–13, 2016.

- [45]

R. L. Wasserstein and N. A. Lazar.

The ASA’s statement on p-values: Context, process, and purpose.

Am. Stat., 70(2):129–133, Apr. 2016.

- [46]

M. Wen, D. Yang, and C. Rose.

Sentiment analysis in MOOC discussion forums: What does it tell us?

In Proceedings of the 7th International Conference on
Educational Data Mining, pages 130–137, 2014.

- [47]

J. Whitehill, K. Mohan, D. Seaton, Y. Rosen, and D. Tingley.

Delving deeper into MOOC student dropout prediction.

Feb. 2017.

- [48]

I. H. Witten, E. Frank, M. A. Hall, and C. J. Pal.

Data Mining: Practical Machine Learning Tools and Techniques.

Morgan Kaufmann, Oct. 2016.

- [49]

W. Xing, X. Chen, J. Stein, and M. Marcinkowski.

Temporal predication of dropouts in MOOCs: Reaching the low hanging
fruit through stacking generalization.

Comput. Human Behav., 58:119–129, 2016.

##

-

<!-- fetch 2: https://api.crossref.org/works/10.18608/jla.2018.52.7 + https://api.openalex.org/works/doi:10.18608/jla.2018.52.7 | fetch.py json-metadata | 2026-11-06T23:14+07:00 | metadata -->
source: Crossref
title: Evaluating Predictive Models of Student Success: Closing the Methodological Gap
authors: Gardner, Joshua Patrick; Brooks, Christopher
container: Journal of Learning Analytics
published: 2018-8-5
volume: 5
issue: 2
pages: 105-125
article number: 
publisher: Society for Learning Analytics Research
doi: 10.18608/jla.2018.52.7
type: journal-article
is-referenced-by-count (Crossref citations): 14

abstract:
Model evaluation – the process of making inferences about the performance of predictive models – is a critical component of predictive model-ing research in learning analytics. In this work, we present an overview of the state-of-the-practice of model evaluation in learning analytics, which overwhelmingly uses only na ̈ıve methods for model evaluation or, less commonly, statistical tests which are not appropriate for predictive model evaluation. We then provide an overview of more appropriate methods for model evaluation, presenting both frequentist and a preferred Bayesian method. Finally, we apply three methods – the na ̈ıve average commonly used in learning analytics, frequentist null hypothesis significance test(NHST), and hierarchical Bayesian model evaluation – to a large set ofMOOC data. We compare 96 different predictive modeling techniques,including different feature sets, statistical modeling algorithms, and tuning hyperparameters for each, using this case study to demonstrate the different experimental conclusions these evaluation techniques provide.

source: OpenAlex
title: Evaluating Predictive Models of Student Success: Closing the Methodological Gap
authors: Josh Gardner; Christopher A. Brooks
institutions: University of Michigan
venue: Journal of Learning Analytics
publication date: 2018-08-05
volume: 5
issue: 2
pages: 105–125
doi: https://doi.org/10.18608/jla.2018.52.7
cited_by_count (OpenAlex): 21
type: article
location: https://learning-analytics.info/index.php/JLA/article/download/5814/6484 (open access: True)
location: https://arxiv.org/pdf/1801.08494 (open access: True)
location: https://arxiv.org/abs/1801.08494 (open access: True)
location: https://learning-analytics.info/journals/index.php/JLA/article/view/5814 (open access: True)
location: https://doi.org/10.48550/arxiv.1801.08494 (open access: True)

abstract:
Model evaluation – the process of making inferences about the performance of predictive models – is a critical component of predictive model-ing research in learning analytics. In this work, we present an overview of the state-of-the-practice of model evaluation in learning analytics, which overwhelmingly uses only na ̈ıve methods for model evaluation or, less commonly, statistical tests which are not appropriate for predictive model evaluation. We then provide an overview of more appropriate methods for model evaluation, presenting both frequentist and a preferred Bayesian method. Finally, we apply three methods – the na ̈ıve average commonly used in learning analytics, frequentist null hypothesis significance test(NHST), and hierarchical Bayesian model evaluation – to a large set ofMOOC data. We compare 96 different predictive modeling techniques,including different feature sets, statistical modeling algorithms, and tuning hyperparameters for each, using this case study to demonstrate the different experimental conclusions these evaluation techniques provide.
