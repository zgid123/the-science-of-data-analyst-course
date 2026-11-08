---
id: S525
url: https://arxiv.org/html/1504.01132
requested: arXiv:1504.01132
fetched: 2026-11-06T23:15+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T07
part: 5
raw: raw.html (287 KB)
conversion: html-text of https://arxiv.org/html/1504.01132 (readable, 10678 words)
---
title: Recursive Partitioning for Heterogeneous Causal Effects

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
-
-

License: arXiv.org perpetual non-exclusive license

arXiv:1504.01132v3 [stat.ML] 30 Dec 2015

# Recursive Partitioning for Heterogeneous Causal EffectsThanks: We are grateful for comments provided at seminars at the National Academy of Science Sackler Colloquium, the Southern Economics Association, the Stanford Conference on Causality in the Social Sciences, the MIT Conference in Digital Experimentation, Harvard, University of Washington, Cornell, Microsoft Research, Facebook, KDD, the AAAI Embedded Machine Learning Conference, the University of Pennsylvania, the University of Arizona. Part of this research was conducted while the authors were visiting Microsoft Research.

Susan Athey
††thanks: Graduate School of Business, Stanford University, and NBER. Electronic correspondence: athey@stanford.edu
  
Guido W. Imbens
††thanks: Graduate School of Business, Stanford University, and NBER. Electronic correspondence: imbens@stanford.edu

First Draft: October 2013

This Draft:
August 2026

###### Abstract

In this paper we propose methods for estimating heterogeneity in causal effects in experimental and observational studies, and for conducting hypothesis tests about
the magnitude of the differences in treatment effects across subsets of the population. We
provide a data-driven approach to partition the data into subpopulations which differ in the magnitude of their treatment effects. The approach enables the construction of valid confidence intervals for treatment effects, even in samples with many covariates relative to the sample size, and without “sparsity” assumptions. To accomplish this, we propose an “honest” approach to estimation, whereby one sample is used to construct the partition
and another to estimate treatment effects for each subpopulation. Our
approach builds on regression tree methods, modified to optimize for goodness of fit in treatment effects and to account for honest
estimation. Our model selection criteria focus on improving the prediction of treatment effects conditional on covariates, anticipating that bias will be eliminated by honest estimation, but also
accounting for the change in the variance of treatment effect estimates within each subpopulation as a result of the split. We also address the challenge that the “ground truth” for a causal effect is not observed for any individual unit, so that standard approaches
to cross-validation must be modified. Through a simulation study, we show that honest estimation can result in substantial improvements in coverage of confidence intervals, where our method attains nominal coverage rates, without much sacrifice in terms of fitting
treatment effects.

In this paper we study two closely related problems: first, estimating heterogeneity by covariates or features in causal effects in experimental or observational studies, and second, conducting inference about
the magnitude of the differences in treatment effects across subsets of the population. Causal effects, in the Rubin Causal Model or potential outcome framework we use here ([19], [11], [14]), are comparisons between outcomes we observe and counterfactual outcomes we would have observed under a different regime or treatment. We introduce data-driven methods that
select subpopulations to estimate more precisely average treatment effects and to test hypotheses about the
differences between the effects in different subpopulations. For experiments, our method allows researchers to identify heterogeneity in treatment effects that was not specified in a
pre-analysis plan, without concern about invalidating inference due to concerns about multiple testing.

Our approach is tailored for applications where there may be many attributes of a unit relative to the number of units observed, and where the functional form of the
relationship between treatment effects and the attributes of units is not known. The supervised machine learning literature (e.g. [9]) has developed a variety of effective methods for a closely
related problem, the problem of predicting outcomes as a function of covariates in similar environments. The most popular approaches (e.g. regression trees ([4]), random forests ([3]), LASSO ([24]), support vector machines ([26]), etc.)
entail building a model of the relationship between attributes and outcomes, with a penalty parameter that penalizes model complexity. Cross-validation is often used to select the optimal level
of complexity (the one that maximizes predictive power without “overfitting”).

Within the prediction-based machine learning literature, regression trees differ from most other methods in that they produce a partition of the population according to covariates, whereby
all units in a partition receive the same prediction. In this paper, we focus on the analogous goal of deriving a partition of the population according to
treatment effect heterogeneity, building on standard regression trees ([4], [3]). Whether the ultimate goal in an application is to derive a partition or fully personalized treatment effect estimates depends on the setting;
settings where partitions may be desirable include those where decision rules must be remembered, applied or interpreted by human beings or computers with limited processing power or memory. Examples include treatment guidelines to be used by physicians or even online personalization applications where
having a simple lookup table reduces latency for the user.
We show that an attractive feature of focusing on partitions is that we can achieve nominal converage of confidence intervals for estimated treatment effects
even in settings with a modest number of observations and many covariates. Our approach has applicability even for settings such as clinical trials of drugs with only a few hundred patients, where the number of
patient characteristics is potentially quite large. Our method may also be viewed as a complement to the use of “pre-analysis plans”
where the researcher must commit in advance to the subgroups that will be considered for analysis. It enables researchers to let
the data discover relevant subgroups without falling prey to concerns of multiple hypothesis testing that would invalidate p-values.

A first challenge for our goal of finding a partition and then testing hypotheses about treatment effects is that many existing machine learning methods cannot be used directly for constructing confidence intervals.
This is because the methods are “adaptive”: they use the training
data for model selection, so that spurious correlations between covariates and outcomes affect the selected model, leading to biases that disappear only slowly as the sample
size grows. In some contexts, additional assumptions such as “sparsity” (only a few covariates affect the outcomes) can be applied to guarantee
consistency or asymptotic normality of predictions ([28]). In this paper, we use an alternative approach that places no
restrictions on model complexity, which we refer to as “honesty.” We say that a model is “honest” if it does
not use the same information for selecting the model structure (in our case, the partition of the covariate space) and for estimation given a model structure.
We accomplish this by splitting the training sample into two parts, one for constructing the tree (including the cross-validation step), and a second for estimating treatment
effects within leaves of the tree, implying that the asymptotic properties of treatment effect estimates within the partitions are the same
as if the partition had been exogenously given. Although there is a loss of precision due to sample splitting (which reduces sample size in each step of estimation), there is a benefit for fit in terms of eliminating bias that offsets at least part of the cost.

A novel contribution of this paper is to show that criteria for both constructing the partition
and cross-validation change when we anticipate honest estimation. In the first stage of estimation, the criteria is the expectation of
the mean-squared error when treatment effects are re-estimated in the second stage. Crucially, we anticipate that second-stage estimates of treatment effects will be unbiased in each leaf,
since they will be performed on a separate (and independent) sample. In that case, splitting and cross-validation criteria are adjusted to ignore systematic bias in estimation, and focus
instead on the tradeoff between more tailored prediction (smaller leaf size) and the variance that will arise in the second (honest estimation) stage due to noisy estimation within small leaves.

A second and perhaps more fundamental challenge to applying machine learning methods such as regression trees [4] off-the-shelf to the problem of causal inference is that regularization approaches based on cross-validation
typically rely on observing the “ground truth,” that is, actual outcomes in a cross-validation sample. However, if our goal is to minimize the mean-squared error of treatment
effects, we encounter what [11] calls the “fundamental problem of causal inference”: the causal effect is not observed for any individual unit, and so we don’t directly
have a ground truth. We address this by proposing approaches for constructing unbiased estimates of the mean-squared error of the causal effect of the treatment.

Using theoretical arguments and a simulation exercise we evaluate the costs and benefits of honest estimation and compare our approach with previously proposed ones.
We find in the settings we consider that
honest estimation results in improvements in fit, in some cases very large improvements, over a more traditional “adaptive” estimation approach.

## 1 The Problem

### 1.1 The Set Up

We consider a setup where there are NN units, indexed by i=1,…,Ni=1,\ldots,N.
We postulate the existence of a pair of potential outcomes for each unit, (Yi​(0),Yi​(1))(Y_{i}(0),Y_{i}(1)) (following the potential outcome or Rubin Causal Model [19], [11], [14], with the unit-level causal effect defined as the difference in potential outcomes, τi=Yi​(1)−Yi​(0).\tau_{i}=Y_{i}(1)-Y_{i}(0).
Let Wi∈{0,1}W_{i}\in\{0,1\} be the binary indicator for the treatment, with Wi=0W_{i}=0 indicating that unit ii received the control treatment, and Wi=1W_{i}=1 indicating that unit ii received the active treatment.
The realized outcome for unit ii is the potential outcome corresponding to the treatment received:

|
| Yiobs=Yi​(Wi)={Yi​(0)if​Wi=0,Yi​(1)if​Wi=1.Y_{i}^{\rm obs}=Y_{i}(W_{i})=\left\{\begin{array}[]{ll}Y_{i}(0)&{\rm if}\ W_{i}=0,\\
Y_{i}(1)&{\rm if}\ W_{i}=1.\end{array}\right.
|

Let XiX_{i} be a KK-component vector of features, covariates or pretreatment variables, known not to be affected by the treatment.
Our data consist of the triple (Yiobs,Wi,Xi)(Y_{i}^{\rm obs},W_{i},X_{i}), for i=1,…,Ni=1,\ldots,N, which are regarded as an i.i.d sample drawn from a large population. Expectations and probabilities will refer to the distribution induced by the random sampling, or by the (conditional) random assignment of the treatment.
We assume that observations are exchangeable, and that there is no interference (the stable unit treatment value assumption, or sutva [20]). This assumption may be violated in settings where some units are connected through networks.
Let p=pr⁡(Wi=1)p={\rm pr}(W_{i}=1) be the marginal treatment probability, and let e⁡(x)=pr⁡(Wi=1|Xi=x)e(x)={\rm pr}(W_{i}=1|X_{i}=x) be the conditional treatment probability (the “propensity score” as defined by [17]). In a randomized experiment with constant treatment assignment probabilities e⁡(x)=pe(x)=p for all values of xx.

### 1.2 Unconfoundedness

Throughout the paper, we maintain the assumption of randomization conditional on the covariates, or “unconfoundedness” ([17]), formalized as:

###### Assumption 1.

(Unconfoundedness)

|
| Wi⟂⟂(Yi​(0),Yi​(1))|Xi.W_{i}\ \perp\!\!\!\perp\ \Bigl(Y_{i}(0),Y_{i}(1)\Bigr)\ \Bigl|\ X_{i}.
|

This assumption, sometimes referred to as “selection on observables” in the econometrics literature, is satisfied in a randomized experiment without conditioning on covariates, but also may be
justified in observational studies if the researcher is able to observe all the variables that affect the unit’s receipt of treatment and are associated with the potential outcomes.

To simplify exposition, in the main body of the paper we maintain the stronger assumption of complete randomization, whereby Wi⟂⟂(Yi​(0),Yi​(1),Xi)W_{i}\perp\!\!\!\perp(Y_{i}(0),Y_{i}(1),X_{i}). Later we show that by using propensity score weighting [19], we can adapt all of the methods to that case.

### 1.3 Conditional Average Treatment Effects and Partitioning

Define the conditional average treatment effect (CATE)

|
| τ⁡(x)≡𝔼⁡[Yi​(1)−Yi​(0)|Xi=x].\tau(x)\equiv\mathbb{E}[Y_{i}(1)-Y_{i}(0)|X_{i}=x].
|

A large part of the causal inference literature (e.g. [14], [15]) is focused on estimating the population (marginal) average treatment effect 𝔼⁡[Yi​(1)−Yi​(0)]\mathbb{E}[Y_{i}(1)-Y_{i}(0)].
The main focus of the current paper is on obtaining accurate estimates of and inferences for the conditional average treatment effect τ⁡(x)\tau(x).
We are interested in estimators τ^​(⋅)\hat{\tau}(\cdot) that are based on partitioning the feature space, and do not vary within the partitions.

## 2 Honest Inference for Population Averages

Our approach departs from conventional classification and regression trees (CART) in two fundamental ways. First, we focus on estimating conditional average treatment effects rather than predicting
outcomes.
This creates complications for conventional methods because we do not observe unit level causal effects for any unit.
Second, we impose a separation between constructing the partition and estimating effects within leaves of the partition, using separate samples for the two tasks,
in what we refer to as “honest” estimation. We contrast ‘’honest” estimation with “adaptive” estimation used in conventional CART, where the same data is used
to build the partition and estimate leaf effects. In this section we introduce the changes induced by honest estimation in the context of the conventional prediction setting; in the next section we consider causal effects. In the discussion in this section we observe for each unit ii a pair of variables (Yi,Xi)(Y_{i},X_{i}), with the interest in the conditional expectation μ⁡(x)≡𝔼⁡[Yi|Xi=x]\mu(x)\equiv\mathbb{E}[Y_{i}|X_{i}=x].

### 2.1 Set Up

We begin by defining key concepts and functions. First, a tree or partitioning Π{\Pi} corresponds to a partitioning of the feature space 𝕏\mathbb{X}, with #⁡(Π)\#({\Pi}) the number of elements in the partition. We write

|
| Π={ℓ1,…,ℓ#⁡(𝒯)},with∪j=1#⁡(Π)ℓj=𝕏.{\Pi}=\{\ell_{1},\ldots,\ell_{\#({\cal T})}\},\ \ {\rm with}\ \cup_{j=1}^{\#({\Pi})}\ell_{j}=\mathbb{X}.
|

Let ℙ\mathbb{P} denote the space of partitions.
Let ℓ⁡(x,Π)\ell(x;{\Pi}) denote the leaf ℓ∈Π\ell\in{\Pi} such that x∈ℓx\in\ell.
Let 𝕊\mathbb{S} be the space of data samples from a population. Let π:𝕊↦ℙ\pi:\mathbb{S}\mapsto\mathbb{P} be an algorithm that on the basis of a sample 𝒮∈𝕊{\cal S}\in\mathbb{S} constructs a partition.
As a very simple example, suppose the feature space is 𝕏={L,R}\mathbb{X}=\{L,R\}. In this case there are two possible partitions,
ΠN={L,R}\Pi_{N}=\{L,R\} (no split), or ΠS={{L},{R}}\Pi_{S}=\{\{L\},\{R\}\} (full split), and so the space of trees is ℙ={ΠN,ΠS}={{L,R},{{L},{R,}}}\mathbb{P}=\{\Pi_{N},\Pi_{S}\}=\{\{L,R\},\{\{L\},\{R,\}\}\}.
Given a sample 𝒮{\cal S}, the average outcomes in the two subsamples are Y¯L\overline{Y}_{L} and Y¯R\overline{Y}_{R}. A simple example of an algorithm is one that splits if the difference in average outcomes exceeds a threshold cc:

|
| π⁡(𝒮)={{{L,R}}if​Y¯L−Y¯R≤c,{{L},{R}}if​Y¯L−Y¯R>c.\pi({\cal S})=\left\{\begin{array}[]{ll}\{\{L,R\}\}&{\rm if}\ \overline{Y}_{L}-\overline{Y}_{R}\leq c,\\
\{\{L\},\{R\}\}&{\rm if}\ \overline{Y}_{L}-\overline{Y}_{R}>c.\end{array}\right.
|

The potential bias in leaf estimates from adaptive estimation can be seen in this simple example. While Y¯L−Y¯R\overline{Y}_{L}-\overline{Y}_{R} is in general an unbiased estimator
for the difference in the population conditional means μ⁡(L)−μ⁡(R)\mu(L)-\mu(R), if we condition on finding that
Y¯L−Y¯R≥c\overline{Y}_{L}-\overline{Y}_{R}\geq c in a particular sample, we expect that Y¯L−Y¯R\overline{Y}_{L}-\overline{Y}_{R} is larger than the population analog.

Given a partition Π{\Pi},
define the conditional mean function μ⁡(x,Π)\mu(x;{\Pi}) as

|
| μ⁡(x,Π)≡𝔼⁡[Yi|Xi∈ℓ⁡(x,Π)]=𝔼⁡[μ⁡(Xi)|Xi∈ℓ⁡(x,Π)],\mu(x;{\Pi})\equiv\mathbb{E}[Y_{i}|X_{i}\in\ell(x;{\Pi})]=\mathbb{E}[\mu(X_{i})|X_{i}\in\ell(x;{\Pi})],
|

which can be viewed as a step-function approximation to μ⁡(x)\mu(x).
Given a sample 𝒮{\cal S} the estimated counterpart is

|
| μ^(x;𝒮,Π)≡1#(i∈𝒮:Xi∈ℓ(x;Π))∑i∈𝒮:Xi∈ℓ⁡(x,Π)Yi,\hat{\mu}(x;{\cal S},{\Pi})\equiv\frac{1}{\#(i\in{\cal S}:X_{i}\in\ell(x;{\Pi}))}\sum_{i\in{\cal S}:X_{i}\in\ell(x;{\Pi})}Y_{i},
|

which is unbiased for μ⁡(x,Π)\mu(x;{\Pi}).
We index this estimator by the sample because we need to be precise which sample is used for estimation of the regression function.

### 2.2 The Honest Target

A central concern in this paper is the criterion used to compare alternative estimators; following
much of the literature, we focus on Mean-squared error (MSE) criteria, but we will modify these criteria in a variety of ways.
For the prediction case, we adjust the MSE by 𝔼⁡[Yi2]\mathbb{E}[Y^{2}_{i}]; since this does not depend on an estimator, subtracting it does not affect how the criterion ranks estimators.
Given a partition Π\Pi, define the mean squared error, where we average over a test sample 𝒮te{\cal S}^{\rm te} and the conditional mean is estimated on an estimation sample 𝒮est{\cal S}^{\rm est}, as

|
| MSE⁡(𝒮te,𝒮est,Π)≡1#⁡(𝒮te)​∑i∈𝒮te{(Yi−μ^​(Xi,𝒮est,Π))2−Yi2}.{\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi})\equiv\frac{1}{\#({\cal S}^{\rm te})}\sum_{i\in{\cal S}^{\rm te}}\left\{\left(Y_{i}-\hat{\mu}(X_{i};{\cal S}^{\rm est},{\Pi})\right)^{2}-Y^{2}_{i}\right\}.
|

The (adjusted) expected mean squared error is the expectation of MSE⁡(𝒮te,𝒮est,Π){\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi}) over the test sample and the estimation sample:

|
| EMSE⁡(Π)≡𝔼𝒮te,𝒮est​[MSE⁡(𝒮te,𝒮est,Π)],{\rm EMSE}({\Pi})\equiv\mathbb{E}_{{\cal S}^{\rm te},{\cal S}^{\rm est}}\left[{\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi})\right],
|

where the test and estimation samples are independent.
In the algorithms we consider, we will consider a variety of estimators for the (adjusted) EMSE,
all of which take the form of MSE estimators MSE⁡(𝒮te,𝒮est,Π){\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi}),
evaluated at the units in sample 𝒮te{\cal S}^{\rm te}, with the estimates based on sample 𝒮est{\cal S}^{\rm est} and the tree Π{\Pi}. For brevity in this paper we will henceforth omit the term “adjusted” and
abuse terminology slightly by referring
to these objects as MSE functions.

Our ultimate goal is to construct and assess algorithms π⁡(⋅)\pi(\cdot) that maximize the “honest” criterion

|
| QH​(π)≡−𝔼𝒮est,𝒮est,𝒮tr​[MSE⁡(𝒮te,𝒮est,π⁡(𝒮tr))].Q^{H}(\pi)\equiv-\mathbb{E}_{{\cal S}^{\rm est},{\cal S}^{\rm est},{\cal S}^{\rm tr}}\left[{\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi({\cal S}^{\rm tr}))\right].
|

Note that throughout the paper we focus on maximixing criterion functions, which typically involve the negative of mean-squared-error expressions.

### 2.3 The Adaptive Target

In the conventional CART approach the target is slightly different:

|
| QC​(π)≡−𝔼𝒮te,𝒮tr​[MSE⁡(𝒮te,𝒮tr,π⁡(𝒮tr))],Q^{C}(\pi)\equiv-\mathbb{E}_{{\cal S}^{\rm te},{\cal S}^{\rm tr}}\left[{\rm MSE}({\cal S}^{\rm te},{\cal S}^{\rm tr},\pi({\cal S}^{\rm tr}))\right],
|

where the same training sample is used to construct and estimate the tree. Compared to our target QH​(π)Q^{H}(\pi) the difference is that in our approach different samples 𝒮tr{\cal S}^{\rm tr} and 𝒮est{\cal S}^{\rm est} are used for construction of the tree and estimation of the conditional means respectively.
We refer to the conventional CART approach as “adaptive,” and our approach as “honest.”

In practice there will be costs and
benefits of the honest approach relative to the adaptive approach. The cost is sample size; given a data set, putting some data in the estimation sample leaves fewer units for the training data set.
The advantage of honest
estimation is that it avoids a problem of adaptive estimation, which is that spurious extreme values of YiY_{i} are likely to be placed into the same leaf as other extreme
values by the algorithm π⁡(⋅)\pi(\cdot),
and thus the sample means (in sample 𝒮tr{\cal S}^{{\rm tr}}) of the elements of π⁡(𝒮tr)\pi({\cal S}^{\rm tr}) are more extreme than they would be in an independent sample.

### 2.4 The Implementation of CART

There are two distinct parts of the conventional CART algorithm, initial
tree building and cross-validation to select a complexity parameter used for pruing. Each part of the algorithm relies on a criterion
function based on mean-squared error. In this paper we will take as given the overall structure of the CART algorithm (e.g., [4], [9]), and our
focus will be on modifying the criteria.

In the tree-building phase,
CART recursively partitions the observations of the training sample. For each leaf, the algorithm evaluates all candidate splits of that leaf (which induce alternative partitions Π\Pi)
using a “splitting” criterion that we refer to as the “in-sample” goodness of fit criterion −MSE⁡(𝒮tr,𝒮tr,Π)-{\rm MSE}({\cal S}^{{\rm tr}},{\cal S}^{{\rm tr}},{\Pi}).
It is well-understood that the conventional criterion leads to “over-fitting,” a problem that is solved by cross-validation to select a penalty on tree depth.
The in-sample goodness of fit criterion will always improve with additional splits, even though additional refinements of a partition Π{\Pi} might in fact increase
the expected mean squared error, especially when the leaf sizes become small.
The reason is that
the criterion ignores the fact that smaller leaves lead to higher-variance estimates of leaf means.

To account for this factor, the conventional approach to
avoiding “overfitting” is to add a penalty term to the criterion that is equal to a constant times the number of splits, so that essentially we only consider splits where the improvement in a goodness-of-fit criterion is above some threshold.
The penalty term is choosen to maximize a goodness of fit criterion in cross-validation samples.
In the conventional cross-validation the training sample is repeatedly split into two subsamples, the 𝒮tr,tr{\cal S}^{{\rm tr},{\rm tr}}
sample that is used to build a new tree as well as estimate the conditional means and the 𝒮tr,cv{\cal S}^{{\rm tr},{\rm cv}} sample that is used to evaluate the estimates.
We “prune” the tree using a penalty parameter that represents the cost of a leaf.
We choose the optimal penalty parameter by evaluating the trees associated with each value of the penalty parameter. The goodness of fit criterion for cross-validation can be written as
−MSE⁡(𝒮tr,cv,𝒮tr,tr,Π).-{\rm MSE}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}).
Note that the cross-validation
criterion directly addresses the issue we highlighted with the in-sample goodness of fit criterion, since 𝒮tr,cv{\cal S}^{{\rm tr},{\rm cv}} is independent of 𝒮tr,tr{\cal S}^{{\rm tr},{\rm tr}},
and thus too-extreme estimates of leaf means will be penalized. The issue
that smaller leaves lead to noisier estimates of leaf means is implicitly incorporated by the fact that a smaller leaf penalty will lead to
deeper trees and thus smaller leaves, and the noisier estimates will lead to larger average MSE{\rm MSE} across the cross-validation samples.

### 2.5 Honest Splitting

In our honest estimation algorithm, we modify CART in two ways. First, we use an independent sample 𝒮est{\cal S}^{\rm est} instead of 𝒮tr{\cal S}^{\rm tr} to estimate leaf means.
Second (and closely related), we modify our splitting and cross-validation criteria to incorporate the fact that we will generate unbiased estimates using 𝒮est{\cal S}^{\rm est} for
leaf estimation (eliminating one aspect of over-fitting), where 𝒮est{\cal S}^{\rm est} is treated as a random variable in the tree building phase. In addition, we explicitly incorporate the fact that finer partitions generate greater variance in leaf estimates.

To begin developing our criteria, let us
expand EMSE⁡(Π){\rm EMSE}({\Pi}):

|
| −EMSE⁡(Π)=−𝔼(Yi,Xi),𝒮est​[(Yi−μ⁡(Xi,Π))2−Yi2]-{\rm EMSE}({\Pi})=-\mathbb{E}_{(Y_{i},X_{i}),{\cal S}^{\rm est}}[(Y_{i}-\mu(X_{i};{\Pi}))^{2}-Y_{i}^{2}]
|

|
| −𝔼Xi,𝒮est​[(μ^​(Xi,𝒮est,Π)−μ⁡(Xi,Π))2]=-\mathbb{E}_{X_{i},{\cal S}^{\rm est}}\left[\left(\hat{\mu}(X_{i};{\cal S}^{\rm est},{\Pi})-\mu(X_{i};{\Pi})\right)^{2}\right]=
|

|
| 𝔼Xi[μ2(Xi;Π)]−𝔼𝒮est,Xi[𝕍(μ^2(Xi;𝒮est,Π)],\mathbb{E}_{X_{i}}[\mu^{2}(X_{i};{\Pi})]-\mathbb{E}_{{\cal S}^{\rm est},X_{i}}\left[{\mathbb{V}}(\hat{\mu}^{2}(X_{i};{\cal S}^{\rm est},{\Pi})\right],
|

where we exploit the equality 𝔼𝒮​[μ^​(x,𝒮,Π)]=μ⁡(x,Π)\mathbb{E}_{\cal S}[\hat{\mu}(x;{\cal S},{\Pi})]=\mu(x;{\Pi}).

We wish to estimate −EMSE⁡(Π)-{\rm EMSE}({\Pi}) on the basis of the training sample 𝒮tr{\cal S}^{\rm tr} and knowledge of the sample size of the estimation sample NestN^{\rm est}.
To construct an estimator for the second term, observe that within each leaf of the tree there is an unbiased estimator for the variance of the estimated mean in that leaf.
Specifically, to estimate the variance of μ^​(x,𝒮est,Π)\hat{\mu}(x;{\cal S}^{\rm est},{\Pi}) on the training sample we can use

|
| 𝕍^​(μ^​(x,𝒮est,Π))≡S𝒮tr2​(ℓ⁡(x,Π))Nest​(ℓ​(x,Π)),\widehat{{\mathbb{V}}}(\hat{\mu}(x;{\cal S}^{\rm est},{\Pi}))\equiv\frac{S^{2}_{{\cal S}^{\rm tr}}(\ell(x;{\Pi}))}{N^{\rm est}(\ell(x;{\Pi}))},
|

where S𝒮tr2​(ℓ)S^{2}_{{\cal S}^{\rm tr}}(\ell) is the within-leaf variance,
to estimate the variance.
We then weight this by the leaf shares pℓp_{\ell} to estimate the expected variance.
Assuming the leaf shares are approximately the same in the estimation and training sample, we can approximate this variance estimator by

|
| 𝔼^[𝕍(μ^2(Xi;𝒮est,Π)|i∈𝒮te]≡1Nest⋅∑ℓ∈ΠS𝒮tr2(ℓ).\widehat{\mathbb{E}}\left[{\mathbb{V}}(\hat{\mu}^{2}(X_{i};{\cal S}^{\rm est},{\Pi})|i\in{\cal S}^{\rm te}\right]\equiv\frac{1}{N^{\rm est}}\cdot\sum_{\ell\in{\Pi}}S^{2}_{{\cal S}^{\rm tr}}(\ell).
|

To estimate the average of the squared outcome μ2​(x,Π)\mu^{2}(x;{\Pi}) (the first term of the target criterion),
we can use the square of the estimated means in the training sample μ^2​(x,Π)\hat{\mu}^{2}(x;{\Pi}), minus an estimate of its variance,

|
| 𝔼^​[μ2​(x,Π)]=μ^2​(x,𝒮tr,Π)−S𝒮tr2​(ℓ⁡(x,Π))Ntr​(ℓ​(x,Π)).\widehat{\mathbb{E}}[\mu^{2}(x;{\Pi})]=\hat{\mu}^{2}(x;{\cal S}^{\rm tr},{\Pi})-\frac{S^{2}_{{\cal S}^{\rm tr}}(\ell(x;{\Pi}))}{N^{\rm tr}(\ell(x;{\Pi}))}.
|

Combining these estimators leads to the following unbiased estimator for EMSE⁡(Π){\rm EMSE}({\Pi}), denoted EMSE^​(𝒮tr,Nest,Π)\widehat{{\rm EMSE}}({\cal S}^{\rm tr},N^{\rm est},{\Pi}):

|
| 1Ntr​∑i∈𝒮trμ^2​(Xi,𝒮tr,Π)−(1Ntr+1Nest)⋅∑ℓ∈ΠS𝒮tr2​(ℓ).\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm tr}}\hat{\mu}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi})-\left(\frac{1}{N^{\rm tr}}+\frac{1}{N^{\rm est}}\right)\cdot\sum_{\ell\in{\Pi}}S^{2}_{{\cal S}^{\rm tr}}(\ell).
|

In practice we use the same sample size for the estimation sample and the training sample, so we use as the estimator

|
| EMSE^​(𝒮tr,Π)≡1Ntr​∑i∈𝒮trμ^2​(Xi,𝒮tr,Π)−2Ntr⋅∑ℓ∈ΠS𝒮tr2​(ℓ).\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi})\equiv\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm tr}}\hat{\mu}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi})-\frac{2}{N^{\rm tr}}\cdot\sum_{\ell\in{\Pi}}S^{2}_{{\cal S}^{\rm tr}}(\ell).
|

Comparing this to the criterion used in the conventional CART algorithm, which can be written as

|
| MSE⁡(𝒮tr,𝒮tr,Π)=1Ntr​∑i∈𝒮trμ^2​(Xi,𝒮tr,Π),{\rm MSE}({\cal S}^{\rm tr},{\cal S}^{\rm tr},{\Pi})=\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm tr}}\hat{\mu}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi}),
|

the difference comes from the terms involving the variance. In the prediction setting the adjustment makes very little difference. Because of the form of the within-leaf sample variances, it follows that the gain from a particular split according to the unadjusted criterion
MSE⁡(𝒮tr,𝒮tr,Π){\rm MSE}({\cal S}^{\rm tr},{\cal S}^{\rm tr},{\Pi}) is proportional to the gain based on EMSE^​(𝒮tr,Π)\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi}), with the constant of proportionality a function of the leaf size. Thus, in contrast to the treatment effect case discussed below, the variance adjustment does matter much here.

### 2.6 Honest Crossvalidation

Even though EMSE^​(𝒮tr,Π)\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi}) is approximately unbiased as an estimator of our ideal criterion EMSE⁡(Π){\rm EMSE}({\Pi}) for a fixed Π{\Pi},
it is not unbiased when we use it repeatedly to evaluate splits using recursive partitioning on the training data 𝒮tr{\cal S}^{\rm tr}. The reason is that
initial splits tend to group together observations with similar, extreme outcomes. So after the training data has been divided once, the sample variance of observations
in the training data within a given leaf is on average lower than the sample variance would be in a new, independent sample. Thus, EMSE^​(𝒮tr,Π)\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi}) is likely to overstate goodness of fit as we grow a deeper and deeper tree,
implying that cross-validation can still play an important role with our honest estimation approach,
though perhaps less so than in the conventional CART.

Because the conventional CART cross-validation criterion
does not account for honest estimation we consider the analogue of our unbiased estimate of the criterion,
which accounts for honest estimation by evaluating a partition Π{\Pi}
using only outcomes for units from the cross-validation sample 𝒮tr,cv{\cal S}^{{\rm tr},{\rm cv}}:

|
| −EMSE^​(𝒮tr,cv,Π)-\widehat{{\rm EMSE}}({\cal S}^{{\rm tr},{\rm cv}},{\Pi})
|

This estimator for the honest criterion is unbiased, although it may have higher variance than
MSE⁡(𝒮tr,cv,𝒮tr,tr,Π){\rm MSE}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}) due to the small sample
size of the cross-validation sample.

## 3 Honest Inference for Treatment Effects

In this section we change the focus to estimating conditional average treatment effects instead of estimating conditional population means. We refer to the estimators developed in this section as “Causal Tree” (CT) estimators.
The setting with treatment effects creates some specific problems because we do not observe the value of the treatment effect whose conditional mean we wish to estimate. This complicates the calculation of the criteria we introduced in the previous section. However, a key point of this paper is that we can estimate these criteria and use those estimates for splitting and cross-validation.

We now observe in each sample the
triple (Yiobs,Xi,Wi)(Y^{\rm obs}_{i},X_{i},W_{i}).
For a sample 𝒮{\cal S} let 𝒮treat{\cal S}_{\rm treat} and 𝒮control{\cal S}_{\rm control} denote the subsamples of treated and control units respectively, with cardinality NtreatN_{\rm treat} and NcontrolN_{\rm control} respectively, and let p=Ntreat/Np=N_{\rm treat}/N be the share of treated units.
The concept of a tree remains the same as in the previous section. Given a tree Π\Pi, define for all xx and both treatment levels ww
the population average outcome

|
| μ(w,x;Π)≡𝔼[Yi(w)|Xi∈ℓ(x;Π)],\mu(w,x;{\Pi})\equiv\mathbb{E}\left[\left.Y_{i}(w)\right|X_{i}\in\ell(x;{\Pi})\right],
|

and the
average causal effect

|
| τ(x;Π)≡𝔼[Yi(1)−Yi(0)|Xi∈ℓ(x;Π)].\tau(x;\Pi)\equiv\mathbb{E}\left[\left.Y_{i}(1)-Y_{i}(0)\right|X_{i}\in\ell(x;{\Pi})\right].
|

The estimated counter parts are

|
| μ^(w,x;𝒮,Π)≡1#⁡({i∈𝒮w:Xi∈ℓ⁡(x,Π)})∑i∈𝒮w:Xi∈ℓ⁡(x,Π)Yiobs,\hat{\mu}(w,x;{\cal S},{\Pi})\equiv\frac{1}{\#(\{i\in{\cal S}_{w}:X_{i}\in\ell(x;{\Pi})\})}\sum_{i\in{\cal S}_{w}:X_{i}\in\ell(x;{\Pi})}Y_{i}^{\rm obs},
|

and

|
| τ^​(x,𝒮,Π)≡μ^​(1,x,𝒮,Π)−μ^​(0,x,𝒮,Π).\hat{\tau}(x;{\cal S},{\Pi})\equiv\hat{\mu}(1,x;{\cal S},{\Pi})-\hat{\mu}(0,x;{\cal S},{\Pi}).
|

Define the mean-squared error for treatment effects as

|
| MSEτ​(𝒮te,𝒮est,Π)≡1#⁡(𝒮te)​∑i∈𝒮te{(τi−τ^​(Xi,𝒮est,Π))2−τi2},{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi})\equiv\frac{1}{\#({\cal S}^{\rm te})}\sum_{i\in{\cal S}^{\rm te}}\left\{\left(\tau_{i}-\hat{\tau}(X_{i};{\cal S}^{\rm est},{\Pi})\right)^{2}-\tau^{2}_{i}\right\},
|

and define EMSEτ​(Π){\rm EMSE}_{\tau}({\Pi}) to be its expectation over the estimation and test samples,

|
| EMSEτ​(Π)≡𝔼𝒮te,𝒮est​[MSEτ​(𝒮te,𝒮est,Π)].{\rm EMSE}_{\tau}({\Pi})\equiv\mathbb{E}_{{\cal S}^{\rm te},{\cal S}^{\rm est}}\left[{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi})\right].
|

A key challenge is
that the workhorse mean-squared error function MSEτ​(𝒮te,𝒮est,Π){\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi}) is infeasible,
because we do not observe the τi\tau_{i}.
However, we show below that we can estimate it.

### 3.1 Modifying Conventional CART for Treatment Effects

Consider first modifying conventional (adaptive) CART to estimate heterogeneous treatment effects. Note that in the prediction case, using the fact that μ^\hat{\mu} is constant within each leaf, we can write

|
| MSEμ(𝒮te,𝒮tr,Π)=−2Ntr∑i∈𝒮teμ^(Xi;𝒮te,Π)⋅μ^(Xi;𝒮tr,Π){\rm MSE}_{\mu}({\cal S}^{\rm te},{\cal S}^{\rm tr},{\Pi})=-\frac{2}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm te}}\hat{\mu}(X_{i};{\cal S}^{\rm te},{\Pi})\cdot\hat{\mu}(X_{i};{\cal S}^{\rm tr},{\Pi})
|

|
| +1Ntr∑i∈𝒮teμ^2(Xi;𝒮tr,Π).+\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm te}}\hat{\mu}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi}).
|

In the treatment effect case we can use the fact that

|
| 𝔼𝒮te[τi|i∈𝒮te:i∈ℓ(x,Π)]=𝔼𝒮te[τ^(x;𝒮te,Π)]\mathbb{E}_{{\cal S}^{\rm te}}\left[\tau_{i}|i\in{\cal S}^{\rm te}:i\in\ell(x,{\Pi})\right]=\mathbb{E}_{{\cal S}^{\rm te}}\left[\hat{\tau}(x;{\cal S}^{\rm te},{\Pi})\right]
|

to construct an unbiased estimator of MSEτ​(𝒮te,𝒮tr,Π){\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm tr},{\Pi}):

|
| MSE^τ(𝒮te,𝒮tr,Π)≡−2Ntr∑i∈𝒮teτ^(Xi;𝒮te,Π)⋅τ^(Xi;𝒮tr,Π)\widehat{{\rm MSE}}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm tr},{\Pi})\equiv-\frac{2}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm te}}\hat{\tau}(X_{i};{\cal S}^{\rm te},{\Pi})\cdot\hat{\tau}(X_{i};{\cal S}^{\rm tr},{\Pi})
|

|
| +1Ntr∑i∈𝒮teτ^2(Xi;𝒮tr,Π).+\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm te}}\hat{\tau}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi}).
|

This leads us to propose, by analogy to CART’s in-sample mean-squared error criterion −MSEμ​(𝒮tr,𝒮tr,Π)-{\rm MSE}_{\mu}({\cal S}^{\rm tr},{\cal S}^{\rm tr},{\Pi}),

|
| −MSE^τ​(𝒮tr,𝒮tr,Π)=1Ntr​∑i∈𝒮trτ^2​(Xi,𝒮tr,Π),-\widehat{{\rm MSE}}_{\tau}({\cal S}^{\rm tr},{\cal S}^{\rm tr},{\Pi})=\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm tr}}\hat{\tau}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi}),
|

as an estimator for the infeasible
in-sample goodness of fit criterion.

For cross-validation we used in the prediction case −MSEμ​(𝒮tr,cv,𝒮tr,tr,Π)-{{\rm MSE}}_{\mu}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}). Again, the treatment
effect analog is infeasible, but we can use an unbiased estimate of it, which leads to
−MSE^τ​(𝒮tr,cv,𝒮tr,tr,Π).-\widehat{{\rm MSE}}_{\tau}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}).

### 3.2 Modifying the Honest Approach

The honest approach described in the previous section for prediction problems also needs to be modified for the treatment effect setting. Using the same expansion as before, now applied to the treatment effect setting, we find

|
| −EMSEτ(Π)=𝔼Xi[τ2(Xi;Π)]−𝔼𝒮est,Xi[𝕍(τ^2(Xi;𝒮est,Π)].-{\rm EMSE}_{\tau}({\Pi})=\mathbb{E}_{X_{i}}[\tau^{2}(X_{i};{\Pi})]-\mathbb{E}_{{\cal S}^{\rm est},X_{i}}\left[{\mathbb{V}}(\hat{\tau}^{2}(X_{i};{\cal S}^{\rm est},{\Pi})\right].
|

For splitting we can estimate both components of this expectation using only the training sample. This leads to an estimator for the infeasible criterion that depends only on 𝒮tr{\cal S}^{\rm tr}:

|
| EMSE^τ​(𝒮tr,Π)≡1Ntr​∑i∈𝒮trτ^2​(Xi,𝒮tr,Π)\widehat{{\rm EMSE}}_{\tau}({\cal S}^{\rm tr},{\Pi})\equiv\frac{1}{N^{\rm tr}}\sum_{i\in{\cal S}^{\rm tr}}\hat{\tau}^{2}(X_{i};{\cal S}^{\rm tr},{\Pi})
|

|
| −2Ntr⋅∑ℓ∈Π(S𝒮treattr2​(ℓ)p+S𝒮controltr2​(ℓ)1−p).-\frac{2}{N^{\rm tr}}\cdot\sum_{\ell\in{\Pi}}\left(\frac{S^{2}_{{\cal S}^{\rm tr}_{\rm treat}}(\ell)}{p}+\frac{S^{2}_{{\cal S}^{\rm tr}_{\rm control}}(\ell)}{1-p}\right).
|

For cross-validation we use the same expression, now with the cross-validation sample:
EMSE^τ​(𝒮tr,cv,Π)\widehat{{\rm EMSE}}_{\tau}({\cal S}^{{\rm tr},{\rm cv}},{\Pi}).

These expressions are directly analogous to the criteria we proposed for the honest version of CART in the prediction case. The criteria reward a partition for finding strong heterogeneity in treatment effects, and penalize a partition
that creates variance in leaf estimates. One difference with the prediction case,
however, is that in the prediction case, the two terms are proportional; whereas for the treatment effect case they are not. It is possible to reduce the variance of a treatment effect estimator by introducing a split,
even if both child leaves have the same average treatment effect, if a covariate affects the mean outcome but not treatment
effects. In such a case, the split results in more homogenous leaves, and thus lower-variance estimates of the means of the
treatment group and control group outcomes. Thus, the distinction
between adaptive and honest splitting criterion will be more pronounced in this case.

The cross-validation criterion estimates treatment effects within
leaves using the 𝒮tr,cv{\cal S}^{{\rm tr},{\rm cv}} sample rather than 𝒮tr,tr{\cal S}^{{\rm tr},{\rm tr}}, to account for the fact that leaf estimates will subsequently be constructed using an estimation sample
that is independent of the training sample.

## 4 Four Partitioning Estimators for Causal Effects

In this section we briefly summarize our CT estimator, and then describe three alternative types of estimators. We compare CT to the alternatives theoretically and through simulations. For each of the four types there is an adaptive version and an honest version, where the latter takes into account that estimation will be done on a sample separate from the sample used for constructing the partition, leading to a total of eight estimators. Note that further variations
are possible; for example, one could use adaptive splitting and cross-validation methods to construct a tree, but still perform honest estimation on a separate sample. We do not consider those variations in this paper.

### 4.1 Causal Trees (CT)

The discussion above developed our preferred estimator, Causal Trees. To summarize, for the adaptive version of causal trees, denoted CT-A, we use for splitting the objective −MSE^​(𝒮tr,𝒮tr,Π)-\widehat{{\rm MSE}}({\cal S}^{\rm tr},{\cal S}^{\rm tr},{\Pi}). For cross-validation we use the same objective function, but evaluated at the samples 𝒮tr,cv{\cal S}^{{\rm tr},{\rm cv}} and 𝒮tr,tr{\cal S}^{{\rm tr},{\rm tr}}, namely
−MSE^​(𝒮tr,cv,𝒮tr,tr,Π)-\widehat{{\rm MSE}}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}).
For the honest version, CT-H, the splitting objective function is −EMSE^​(𝒮tr,Π)-\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi}). For cross-validation we use the same objective function, but now evaluated at the cross validation sample,
−EMSE^​(𝒮tr,cv,Π)-\widehat{{\rm EMSE}}({\cal S}^{{\rm tr},{\rm cv}},{\Pi}).

### 4.2 Transformed Outcome Trees (TOT)

Our first alternative method is based on the insight that by using a transformed version of the outcome Yi∗=(Yi−Wi)/(p⋅(1−p))Y^{*}_{i}=(Y_{i}-W_{i})/(p\cdot(1-p)), it is possible to
use off-the-shelf regression tree methods to focus splitting and cross-validation on treatment effects rather than outcomes. Similar approaches are
used in [2], [6], [22], and [29]. Because 𝔼⁡[Yi∗|Xi=x]=τ⁡(x)\mathbb{E}[Y^{*}_{i}|X_{i}=x]=\tau(x), off-the-shelf CART methods can be used directly, where estimates of the sample average of Yi∗Y^{*}_{i} within each leaf
can be interpreted as estimates of treatment effects. This ease of application is the key attraction of this method. The main drawback
(relative to CT-A) is that in general it is not efficient because it does not use the information in the treatment indicator beyond the construction of the transformed outcome.
For example, the sample average in 𝒮{\cal S} of Yi∗Y^{*}_{i} within a given leaf ℓ⁡(x,Π)\ell(x;{\Pi}) will only be equal to τ^​(x,Π,𝒮)\hat{\tau}(x;{\Pi},{\cal S}) if the fraction of treated observations within the leaf is exactly equal to pp. Since this method is primarily considered as a benchmark, in simulations we focus only on an adaptive version that can use existing learning methods
entirely off-the-shelf. The adaptive version of the transformed outcome tree estimator we consider, TOT-A, uses the conventional CART algorithm with the transformed outcome replacing the original outcome. The honest version, TOT-H, uses the same splitting and
cross-validation criteria, so that it builds the same trees; it differs only in that a separate estimation sample is used to construct
the leaf estimates. The treatment effect estimator within a leaf is the same as the adaptive method, that is, the sample
mean of Yi∗Y_{i}^{*} within the leaf.

### 4.3 Fit-based Trees (F)

We consider two additional alternative methods for constructing trees, based on suggestions in the literature.
In the first of these alternatives the choice of which feature to split on, and at what value of the feature to split, is based on comparisons of the goodness–of–fit of the outcome rather than the treatment effect.
In standard CART of course goodness–of–fit of outcomes is also the split criterion, but here we estimate a model for treatment
effects within each leaf. Specifically, we have a linear model with an intercept and an indicator for the treatment as the regressors, rather only an intercept as in standard CART. This approach is used in [30], who consider building general models at the leaves of the trees. Treatment
effect estimation is a special case of their framework. [30] propose using statistical tests based on improvements in goodness-of-fit
to determine when to stop growing the tree, rather than relying on cross-validation, but for ease of comparison to CART, in this
paper we will stay closer to traditional CART in terms of growing deep trees and pruning them. We modify the mean-squared error function:

|
| MSEμ,W​(𝒮te,𝒮est,Π)≡∑i∈𝒮te((Yiobs−μ^w​(Wi,Xi,𝒮est,Π))2−Yi2).{\rm MSE}_{\mu,W}({\cal S}^{\rm te},{\cal S}^{\rm est},{\Pi})\equiv\sum_{i\in{\cal S}^{\rm te}}((Y_{i}^{\rm obs}-\hat{\mu}_{w}(W_{i},X_{i};{\cal S}^{\rm est},{\Pi}))^{2}-Y^{2}_{i}).
|

For the adaptive version F-A we follow conventional CART, using the criterion −MSEμ,W-{\rm MSE}_{\mu,W} in place of −MSE-{\rm MSE} for splitting,
and the analog of −MSE^​(𝒮tr,cv,𝒮tr,tr,Π)-\widehat{{\rm MSE}}({\cal S}^{{\rm tr},{\rm cv}},{\cal S}^{{\rm tr},{\rm tr}},{\Pi}) with with μ^w\hat{\mu}_{w} in place of μ^\hat{\mu} for cross-validation. For the honest version we use the analogs
of −EMSE^​(𝒮tr,Π)-\widehat{{\rm EMSE}}({\cal S}^{\rm tr},{\Pi}) and −EMSE^​(𝒮tr,cv,Π)-\widehat{{\rm EMSE}}({\cal S}^{{\rm tr},{\rm cv}},{\Pi}), with μ^w\hat{\mu}_{w} in place of μ^\hat{\mu}, for splitting and cross-validation. Similar to the prediction case, the variance term in the honest splitting criterion does not make much of a difference for the choice of splits.
An advantage of the fit-based tree approach is that it is a straightforward extension of conventional CART methods. In particular, the mean-squared error criterion is feasible, since YiY_{i} is observed.
To highlight the disadvantages of the F approach, consider a case where two splits improve the fit to an equal degree. In one case, the split leads to variation in average treatment effects, and in the other case it does not. The first split would be better from the perspective of estimating heterogeneous treatment effects, but the fit criterion would view the two splits as equally attractive.

### 4.4 Squared T-statistic Trees (TS)

For the last estimator we look for splits with the largest value for the square of the
t-statistic for testing the null hypothesis that the average treatment effect is the same in the two potential leaves.
This estimator was proposed by [21].
If the two leaves are denoted LL (Left) and RR (Right), the square of the t-statistic is

|
| T2≡N⋅(Y¯L−Y¯R)2S2/NL+S2/NR,T^{2}\equiv N\cdot\frac{(\overline{Y}_{L}-\overline{Y}_{R})^{2}}{S^{2}/N_{L}+S^{2}/N_{R}},
|

where S2S^{2} is the conditional sample variance given the split.
At each leaf, successive splits are determined by selecting the split that maximizes T2T^{2}.
The concern with this criterion is that it places no value on splits that improve the fit. While such splits do not deserve as much weight as the fit criterion puts on them, they do have some value.

Both the adaptive and honest versions of the TS approach use T2T^{2} as the splitting criterion. For cross-validation and pruning, it is less
obvious how to proceed.
[30] suggests that
when using a statistical test for splitting, if it is desirable in an application to grow deep trees and then cross-validate to determine
depth, then one can use a standard goodness of fit measure for pruning and cross-validation.
However, this could
undermine the key advantage of TS, to focus on heterogeneous treatment effects. For this reason, we instead propose
to use the CT-A and CT-H criteria for cross-validation for TS-A and TS-H, respectively.

### 4.5 Comparison of the Causal Trees, the Fit Criterion, and the Squared t-statistic Criterion

It is useful to compare our proposed criterion to the F and TS criteria in a simple setting to gain insight into the relative merits of the three approaches. We do so here focusing on a decision whether to proceed with a single possible split, based on a binary covariate Xi∈{L,R}X_{i}\in\{L,R\}.
Let ΠN{\Pi}_{N} and ΠS{\Pi}_{S} denote the trees without and with the split, and
let Y¯w\overline{Y}_{w}, Y¯L​w\overline{Y}_{Lw} and Y¯R​w\overline{Y}_{Rw} denote the average outcomes for units with treatment status Wi=wW_{i}=w. Let NwN_{w}, NL​wN_{Lw}, and NR​wN_{Rw} be the sample sizes for the corresponding subsamples.
Let S2S^{2} be the sample variance of the outcomes given a split,
and let S~2\tilde{S}^{2} be the sample variance without a split.
Define the squared t-statistics for testing that the average outcomes for control (treated) units in both leaves are identical,

|
| T02≡(Y¯L​0−Y¯R​0)2S2/NL​0+S2/NR​0,T12≡(Y¯L​1−Y¯R​1)2S2/NL​1+S2/NR​1.T_{0}^{2}\equiv\frac{(\overline{Y}_{L0}-\overline{Y}_{R0})^{2}}{S^{2}/N_{L0}+S^{2}/N_{R0}},\ \ T_{1}^{2}\equiv\frac{(\overline{Y}_{L1}-\overline{Y}_{R1})^{2}}{S^{2}/N_{L1}+S^{2}/N_{R1}}.
|

Then we can write the improvement in goodness of fit from splitting the single leaf into two leaves as

|
| F=S~2⋅2⋅(T02+T12)1+2⋅(T02+T12)/N.F=\tilde{S}^{2}\cdot\frac{2\cdot(T_{0}^{2}+T_{1}^{2})}{1+2\cdot(T_{0}^{2}+T_{1}^{2})/N}.
|

Ignoring degrees-of-freedom correctcions, the change in our proposed criterion for the honest version of the causal tree in this simple setting can be written as a combination of the F and TS criteria:

|
| EMSE^τ​(𝒮,ΠN)−EMSE^τ​(𝒮,ΠS)=(T2−4)​(S~2−F/N)+2​S~2p⋅(1−p).\widehat{{\rm EMSE}}_{\tau}({\cal S},{\Pi}_{N})-\widehat{{\rm EMSE}}_{\tau}({\cal S},{\Pi}_{S})=\frac{(T^{2}-4)(\tilde{S}^{2}-F/N)+2\tilde{S}^{2}}{p\cdot(1-p)}.
|

Our criterion focuses primarily on T2T^{2}. Unlike the TS approach, however, it incorporates the benefits of splits due to improvement in the fit.

## 5 Inference

Given the estimated conditional average treatment effect we also would like to do inference. Once constructed, the tree is a
function of covariates, and if we use a distinct sample to
conduct inference, then the problem reduces to that of estimating treatment effects in each member of a partition of the covariate space. For this problem, standard approaches are therefore valid for the estimates obtained via honest estimation, and in particular,
no assumptions about model complexity are required. For the adaptive methods standard approaches to confidence intervals are not generally valid for the reasons discussed above, and below we document through simulations that this can be important in practice.

## 6 A Simulation Study

To assess the relative performance of the proposed algorithms we carried out a small simulation study with three distinct designs. In Table 1 we report a number of
summary statistics from the simulations. We report averages; results for medians are similar. We report results for
Ntr=NestN^{\rm tr}=N^{\rm est} with either 500 or 1000 observations. When comparing adaptive to honest approaches, we report the ratio of the MSEτ{\rm MSE}_{\tau} for adaptive estimation with Ntr=1000N^{\rm tr}=1000 to MSEτ{\rm MSE}_{\tau} for honest estimation
with Ntr=Nest=500N^{\rm tr}=N^{\rm est}=500, in order to highlight the tradeoff between sample
size and bias reduction that arises with honest estimation. We evaluate MSEτ{\rm MSE}_{\tau} using a test sample with Nte=6000N^{\rm te}=6000 observations to test the methods in order to minimize the sampling variance in our simulation results.

In all designs, the marginal treatment probability is p=0.5p=0.5. KK denotes the number of features. In each design, we have a model η⁡(x)\eta(x) for the mean
effect and κsim​(x)\kappa^{\text{sim}}(x) for the treatment effect. Then, the potential outcomes are written

|
| Yi​(w)=ηsim​(Xi)+12⋅(2​w−1)⋅κ⁡(Xi)+ϵi,Y_{i}(w)=\eta^{\text{sim}}(X_{i})+\frac{1}{2}\cdot(2w-1)\cdot\kappa(X_{i})+\epsilon_{i},
|

where ϵi∼𝒩⁡(0,.01)\epsilon_{i}\sim{\cal N}(0,.01), and the XiX_{i} are independent of ϵi\epsilon_{i} and one another, and Xi∼𝒩⁡(0,1)X_{i}\sim{\cal N}(0,1).
The designs are summarized as follows:

|
| 1: K=2;η(x)=12x1+x2;κ(x)=12x1.\text{1: }K=2;\eta(x)=\frac{1}{2}x_{1}+x_{2};\kappa(x)=\frac{1}{2}x_{1}.
|

|
| 2: K=10;η(x)=12∑k=12xk+∑k=36xk;κ(x)=∑k=121{xk>0}⋅xk\text{2: }K=10;\eta(x)=\frac{1}{2}\sum_{k=1}^{2}x_{k}+\sum_{k=3}^{6}x_{k};\kappa(x)=\sum_{k=1}^{2}1\{x_{k}>0\}\cdot x_{k}
|

|
| 3: K=20;η(x)=12∑k=14xk+∑k=58xk;κ(x)=∑k=141{xk>0}⋅xk\text{3: }K=20;\eta(x)=\frac{1}{2}\sum_{k=1}^{4}x_{k}+\sum_{k=5}^{8}x_{k};\kappa(x)=\sum_{k=1}^{4}1\{x_{k}>0\}\cdot x_{k}
|

In each design, there are some covariates that affect treatment effects (κ\kappa) and mean outcomes (η\eta); some covariates
that enter η\eta but not κ\kappa; and some covariates that do not
affect outcomes at all (“noise” covariates). Design 1 does not have noise covariates. In Designs 2 and 3, the first few covariates
enter κ\kappa, but only when their signs are positive, while they affect η\eta throughout their range. Different criterion will thus
lead to different optimal splits, even within a covariate; F will focus more on splits when the covariates are negative.

The first panel of Table 1 compares the number of leaves in different designs and different values of Ntr=NestN^{\rm tr}=N^{\rm est}. Recalling that TOT-A and TOT-H have the same splitting method, we see that it tends to build shallow trees. The failure to control for the
realized value of WiW_{i} leads to additional noise in estimates, which tends to lead to aggressive
pruning. For the other estimators, the adaptive versions lead to shallower trees than the honest versions, as the honest versions
correct for overfitting, and the main cost of small leaf size is high variance in leaf estimates. F-A and F-H are very similar; as discussed above, the splitting criterion are very similar, and further,
the F estimators are less prone to overfitting treatment effects, because they split based upon overall model fit. We also observe
that the F estimators build the deepest trees; they reward splitting on covariates that affect mean outcomes as well as treatment effects.

The second panel of Table 1 examines the performance of the alternative honest estimators, as evaluated by the infeasible
criterion MSEτ{\rm MSE}_{\tau}. We report the average of the ratio of MSEτ{\rm MSE}_{\tau} for a given estimator to MSEτ{\rm MSE}_{\tau} for our preferred
estimtor, CT-H. The TOT-H estimator performs well in Designs 2 and 3, but suffers in Design 1. In Design 1, the variance of
YiY_{i} conditional on (Wi,Xi)(W_{i},X_{i}) is very low at .01.01, and so the failure of TOT to account for the realization of WiW_{i} results
in a noticeable loss of performance. The F-H estimator suffers in all 3 designs; all designs give the F-H criterion attractive
opportunities to split based on covariates that do not enter κ\kappa. F-H would perform better in alternative designs
where η⁡(x)=κ⁡(x)\eta(x)=\kappa(x); F-H also does well at avoiding splits on noise covariates. The TS-H estimator performs
well in Design 1, where x1x_{1} affects η\eta and κ\kappa the same way, so that the CT-H criterion is aligned with TS-H.
Design 3 is more complex, and the ideal splits from the perspective of balancing overall mean-squared error of treatment effects
(including variance reduction) are different from those favored by TS-H. Thus, TS performs worse, and the difference is
exacerbated with larger sample size, where there are more opportunities for the estimators to build deeper trees and thus to make different choices. We also calculate comparisons based on a feasible criterion, the average squared difference between the transformed outcome Yi∗Y^{*}_{i} and the estimated treatment effect τ^i\hat{\tau}_{i}. For details for this comparison see the SI Appendix. In general the results are consistent with those from the infeasible criterion.

The third panel of Table 1 explores the costs and benefits to honest estimation. The Table reports the ratio of MSEτ​(𝒮te,𝒮est∪𝒮tr,πEstimator-A​(𝒮est∪𝒮tr)){\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est}\cup{\cal S}^{\rm tr},\pi^{\text{Estimator-A}}({\cal S}^{\rm est}\cup{\cal S}^{\rm tr})) to MSEτ​(𝒮te,𝒮est,πEstimator-H​(𝒮tr)CLOSE{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{Estimator-H}}({\cal S}^{\rm tr}) for each estimator. The adaptive version uses the union of the training and estimation
samples for tree-building, cross-validation, and leaf estimation. Thus it has double the sample size (1000 observations) at each step,
while the honest version uses 500 of the observations in training and cross-validation, with the complement used for estimating
treatment effects within leaves. The results
show that there is a cost to honest estimation in terms of MSEτ{\rm MSE}_{\tau}, varying by design and estimator.

The final two panels of Table 1 show the coverage rate for 90% confidence intervals. We achieve nominal coverage rates for honest
methods in all designs, where, in contrast, the adaptive methods have coverage rates substantially below nominal rates. Thus, our simulations bear out the tradeoff that honest estimation sacrifices some goodness of fit (of
treatment effects) in exchange for valid confidence intervals.

## 7 Observational Studies with Unconfoundedness

The discussion so far has focused on the setting where the assignment to treatment is randomized. The proposed methods can be adapted to observational studies under the assumption of unconfoundedness. In that case we need to modify the estimates within leaves to remove the bias from simple comparisons of treated and control units. There is a large literature on methods for doing so, e.g., [14]. For example, as in [10] we can do so by propensity score weighting.
Efficiency will improve if we renormalize the weights within each leaf and and within the treatment and control group when estimating treatment effects. [5] propose approaches to trimming observations with extreme values for the propensity score to
improve robustnesses.
Note that there are some additional conditions required to establish asymptotic normality
of treatment effect estimates when propensity score weighting is used (see, e.g., [10]); these results apply without
modification to the estimation phase of honest partitioning algorithms.

## 8 The Literature

A small but growing literature seeks to apply supervised machine learning techniques to the problem of estimating heterogeneous treatment effects. Beyond those previously discussed,
[23] transform the features rather than the outcomes and then apply LASSO to the model with the original outcome and the transformed features.
[7] estimate μ⁡(w,x)=𝔼⁡[Yi​(w)|Xi=x]\mu(w,x)=\mathbb{E}[Y_{i}(w)|X_{i}=x] for w=0,1w=0,1 using random forests, then calculate τ^i=μ^​(1,Xi)−μ^​(0,Xi)\hat{\tau}_{i}=\hat{\mu}(1,X_{i})-\hat{\mu}(0,X_{i}). They then use machine learning algorithms to estimate τ^i\hat{\tau}_{i} as a function of the units’ attributes, XiX_{i}. Our approach differs in that we apply machine learning methods directly to the treatment effect in a single stage procedure.
[13] use LASSO to estimate the effects of both treatments and attributes, but with different penalty terms for the two types of features to allow for the possibility that the treatment effects are present but the magnitudes of the interactions are small. Their approach is similar to ours in that they distinguish between the estimation of treatment effects and the estimation of the impact of other
attributes of units.
[25] consider a model with the outcome linear in the covariates and the interaction with the treatment variable. Using Bayesian nonparametric methods with Dirichlet priors, they project their estimates of heterogeneous treatment effects down onto the feature space using LASSO-type regularization methods to get low-dimensional summaries of the heterogeneity.
[6] and [2] propose a related appoach for finding the optimal treatment policy
that combines inverse propensity score methods with “direct methods” (e.g. the “single tree” approach considered above) that predict the outcome as a function of the treatment and the unit attributes. The methods can be
used to evaluate the average difference in outcomes from any two policies that map attributes to treatments, as well as to select the optimal policy function. They do not focus
on hypothesis testing for heterogeneous treatment effects, and they use conventional approaches for cross-validation.
Also related is the work on Targeted Learning [27], which
modifies the loss function to increase the weight on the parts of the likelihood that concern the parameters of interest.

## 9 Conclusion

In this paper we introduce new methods for constructing trees for causal effects that allow us to do valid inference for the causal effects in randomized experiments and in observational studies satisfying unconfoundedness, without restrictions on the number of covariates or the complexity of the data generating process. Our methods partition the feature space into subspaces. The output of our method is a set of treatment effects and confidence intervals for each subspace.

A potentially important application of the techniques is to “data-mining” in randomized experiments. Our method can be used
to explore any previously conducted randomized controlled trial, for example, medical studies or field experiments in developed economics. A researcher can apply our methods and discover subpopulations with lower-than-average or higher-than-average treatment
effects, and can report confidence intervals for these estimates without concern about multiple testing.

## References

- [1]

A. Abadie and G. Imbens,
Large Sample Properties of Matching Estimators for Average Treatment
Effects, Econometrica, 74(1), 235-267.

- [2]

A. Beygelzimer and J. Langford, The Offset Tree for Learning with Partial Labels, http://arxiv.org/pdf/0812.4044v2.pdf, (2009).

- [3]

L. Breiman, Random forests,
Machine Learning, 45, (2001), 5-32.

- [4]

L. Breiman, J. Friedman, R. Olshen, and C. Stone,
Classification and Regression Trees, (1984), Wadsworth.

- [5]

R. Crump, R., J. Hotz, G. Imbens, and O. Mitnik, Nonparametric Tests for Treatment Effect Heterogeneity, Review of Economics and Statistics, 90(3), (2008), 389-405.

- [6]

M. Dudik, J. Langford and L. Li, Doubly Robust Policy Evaluation and Learning , Proceedings of the 28th International Conference on Machine Learning (ICML-11), (2011).

- [7]

J. Foster, J. Taylor and S. Ruberg, Subgroup Identification from Randomized Clinical Data, Statistics in Medicine, 30, (2010), 2867-2880.

- [8]

Green, D., and H. Kern, (2010), Detecting Heterogeneous Treatment Effects in Large-Scale Experiments Using Bayesian Additive Regression Trees, Unpublished Manuscript, Yale University.

- [9]

T. Hastie, R. Tibshirani, and J. Friedman,
The Elements of Statistical Learning: Data Mining, Inference, and Prediction,
Second Edition, (2011), Springer.

- [10]

K. Hirano, G. Imbens and G. Ridder, Efficient Estimation of Average Treatment Effects Using the
Estimated Propensity Score, Econometrica, 71 (4), (2003), 1161-1189.

- [11]

P. Holland, Statistics and
Causal Inference (with discussion), Journal of the American
Statistical Association, 81, (1986), 945-970.

- [12]

D. Horvitz, and D. Thompson,
A generalization of sampling without replacement from a finite universe, Journal of the American Statistical Association,
Vol. 47, (1952), 663�685.

- [13]

K. Imai and M. Ratkovic, Estimating Treatment Effect Heterogeneity in Randomized Program Evaluation, Annals of Applied Statistics, 7(1), (2013), 443-470.

- [14]

G. Imbens and D. Rubin,
Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction, Cambridge University Press, (2015).

- [15]

J. Pearl,
Causality: Models, Reasoning and Inference, Cambridge University Press, (2000).

- [16]

P. Rosenbaum,
Observational Studies, (2002), Springer.

- [17]

P. Rosenbaum and D. Rubin, The
Central Role of the Propensity Score in Observational Studies for
Causal Effects, Biometrika, 70, (1983), 41-55.

- [18]

M. Rosenblum and M. Van Der Laan., Optimizing Randomized Trial Designs to Distinguish which Subpopulations Benefit from Treatment , Biometrika, 98(4), (2011), 845-860.

- [19]

D. Rubin, Estimating Causal Effects of Treatments in
Randomized
and Non-randomized Studies Journal of Educational Psychology, 66,
(1974), 688-701.

- [20]
D. Rubin, Bayesian inference for causaleffects: The Role of Randomization, Annals of Statistics, 6, (1978), 34-58.

- [21]

X. Su, C. Tsai, H. Wang, D. Nickerson, and B. Li, Subgroup Analysis via Recursive Partitioning, Journal of Machine Learning Research, 10, (2009), 141-158.

- [22]

J. Signovitch, J., Identifying informative biological markers
in high-dimensional genomic data and clinical trials, PhD Thesis, Department of Biostatistics, Harvard University, (2007).

- [23]

L. Tian, A. Alizadeh, A. Gentles, and R. Tibshirani, A Simple Method for Estimating Interactions Between a Treatment and a Large Number of Covariates, Journal of the American Statistical Association, 109(508), (2014) 1517-1532.

- [24]

R. Tibshirani, Regression shrinkage and selection via the lasso, Journal of the Royal Statistical Society. Series B (Methodological), Volume 58, Issue 1. (1996), 267-288.

- [25]

M. Taddy, M. Gardner, L. Chen, and D. Draper,, Heterogeneous Treatment Effects in Digital Experimentation, Unpublished Manuscript, (2015), arXiv:1412.8563.

- [26]

V. Vapnik,
Statistical Learning Theory, Wiley, (1998).

- [27]

M. Van Der Laan, and S. Rose, Targeted Learning: Causal Inference for Observational and Experimental Data, Springer, (2011).

- [28]

S. Wager, and S. Athey, Estimation and Inference of Heterogeneous Treatment Effects using Random Forests, http://arxiv.org/pdf/1510.04342v2.pdf, (2015).

- [29]

H. Weisburg, H. and V. Pontes, Post hoc subgroups in Clinical Trials: Anathema or Analytics? Clinical Trials, June, 2015.

- [30]

A. Zeileis, T. Hothorn, and K. Hornik,
Model-based recursive partitioning. Journal of Computational and Graphical Statistics, 17(2), (2008), 492-514.

| Table 1: Simulation Study

| Design
| 1
| 2
| 3

| Ntr=NestN^{\rm tr}=N^{\rm est}
| 500
| 1000
| 500
| 1000
| 500
| 1000

| Estimator
| Number of Leaves

| TOT
| 2.8
| 3.4
| 2.1
| 2.7
| 4.7
| 6.1

| F-A
| 6.1
| 13.2
| 6.3
| 13.1
| 6.1
| 13.2

| TS-A
| 4.0
| 5.6
| 2.5
| 3.3
| 4.4
| 8.9

| CT-A
| 4.0
| 5.7
| 2.3
| 2.5
| 4.5
| 6.2

| F-H
| 6.1
| 13.2
| 6.4
| 13.3
| 6.3
| 13.4

| TS-H
| 4.4
| 7.7
| 5.3
| 11.0
| 6.0
| 12.3

| CT-H
| 4.2
| 7.5
| 5.3
| 11.2
| 6.2
| 12.3

| Infeasible MSE Divided by Infeasible MSE for CT-H∗

| TOT-H
| 1.77
| 2.12
| 1.03
| 1.04
| 1.03
| 1.05

| F-A
| 1.93
| 1.54
| 1.69
| 2.07
| 1.63
| 2.08

| TS-H
| 1.01
| 1.02
| 1.06
| 0.99
| 1.24
| 1.38

| CT-H
| 1.00
| 1.00
| 1.00
| 1.00
| 1.00
| 1.00

| Ratio of Infeasible MSE: Honest to Adaptive∗∗

| TOT-H/TOT-A
|
| 0.99
|
| 0.86
|
| 0.76

| F-H/F-A
|
| 0.50
|
| 0.98
|
| 0.91

| TS-H/TS-A
|
| 0.92
|
| 0.90
|
| 0.85

| CT-H/CT-A
|
| 0.91
|
| 0.93
|
| 0.76

| Coverage of 90% Confidence Intervals - Adaptive

| TOT-A
| 0.83
| 0.86
| 0.83
| 0.83
| 0.74
| 0.79

| F-A
| 0.89
| 0.89
| 0.86
| 0.86
| 0.82
| 0.82

| TS-A
| 0.85
| 0.85
| 0.80
| 0.83
| 0.77
| 0.80

| CT-A
| 0.85
| 0.85
| 0.81
| 0.83
| 0.80
| 0.81

| Coverage of 90% Confidence Intervals - Honest

| TOT-H
| 0.90
| 0.89
| 0.90
| 0.92
| 0.89
| 0.89

| F-H
| 0.91
| 0.90
| 0.90
| 0.90
| 0.90
| 0.89

| TS-H
| 0.89
| 0.90
| 0.90
| 0.90
| 0.90
| 0.90

| CT-H
| 0.90
| 0.90
| 0.90
| 0.89
| 0.90
| 0.90

MSEτ∗(𝒮te,𝒮est,πEstimator(𝒮tr))/MSEτ(𝒮te,𝒮est,πCT-H(𝒮tr)){}^{*}{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{Estimator}}({\cal S}^{\rm tr}))/{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{CT-H}}({\cal S}^{\rm tr}))

MSEτ∗⁣∗(𝒮te,𝒮est∪𝒮tr,πEstimator-A(𝒮est∪𝒮tr))/{}^{**}{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est}\cup{\cal S}^{\rm tr},\pi^{\text{Estimator-A}}({\cal S}^{\rm est}\cup{\cal S}^{\rm tr}))/
  MSEτ​(𝒮te,𝒮est,πEstimator-H​(𝒮tr)CLOSE{\rm MSE}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{Estimator-H}}({\cal S}^{\rm tr})

Additional Simulation Details (Online Appendix)

This Appendix describes some additional details of the simulation study, and also presents additional simulation results in Appendix
Table A1.

The code for our simulations was written as an R software package that is in preparation for public release. It is based on the ‘rpart’
R package, available at https://cran.r-project.org/web/packages/rpart/index.html. For TOT, we directly use rpart
applied to the transformed outcome Yi∗Y_{i}^{*}, and we use 10-fold cross-validation for pruning the tree. For each of our other estimators, we modified several components of
the package. In the remainder of this Appendix, discussions of modifications apply to F, CT, and TS estimators. For these estimators, we create new versions of the “anova” functions, functions that in the standard rpart package are used for calculating the total goodness of fit for a node of the tree,
evaluating the quality of alternative splits, and estimating the goodness of fit for pruned trees using cross-validation samples. We maintain the overall
structure of the rpart package. The rpart package has an important tuning parameter, which is the minimum number of observations
per leaf, denoted nmn_{m}. We modify the rpart routine to insist on at least nmn_{m} treated and nmn_{m} control observations per leaf, to ensure
that we can calculate a treatment effect within each leaf. In the simulations reported in Table 1 of the paper and in this Appendix,
we use nm=25n_{m}=25 for all models except TOT, while for the TOT model the minimum leaf size is 50 (without restrictions on treated
and control observations).

We make one additional modification to the way the standard rpart splitting function works. We restrict the set of potential split points considered,
and further, in the splitting process we rescale the covariate values within each leaf and each treatment group
in order to ensure that when moving
from one potential split point to the next, we move the same number of treatment and control observations from the right leaf to the left leaf. We begin by describing the motivation
for these modifications, and then we give details.

The rpart algorithm considers every value of Xi,kX_{i,k} in 𝒮tr{\cal S}^{\rm tr} as a possible split point for covariate XkX_{k}.
An obvious disadvantage of this approach is that computation time can grow prohibitively large in models with many observations
and covariates. But there are some more subtle disadvantages as well. The first is that there will naturally be sampling variation
in estimates of τ^\hat{\tau} as we vary the possible split points. A problem akin to a multiple hypothesis testing problem arises:
since we are looking for the maximum value of an estimated criterion across a large number of possible split points,
as the number of split points tested grows, it becomes more and more likely that one of the splits for a given covariate appears to improve the fit criterion even if the true
value of the criterion would indicate that it is better not to split. One way to mitigate both the computation time problem and
the multiple-testing problem is to consider only a limited number of split points.

A third problem is specific to considering treatment effect heterogeneity. To see the problem, suppose that a covariate
strongly affects the mean of outcomes, but not treatment effects. Within a leaf, some observations are treated and some
are control. If we consider every level of the covariate in the leaf as a possible split point, then shifting from one split point to the
next shifts a single observation from the right leaf to the left leaf. This observation is in the treatment or the control group,
but not both; suppose it is in the treatment group. If the covariate has a strong effect on the level of outcomes, the observation that is shifted will be likely have an
outcome more extreme than average. It will change the sample average of the treatment group, but not the control group, leading
to a large change in the estimated treatment effect difference.
We expect the estimated difference in treatment effects across the left and right leaves to fluctuate greatly with the split point in this scenario. This
variability around the true mean difference in treatment effects occurs more often when covariates affect mean outcomes, and thus it
can lead the estimators to split too much on such covariates, and also to find spurious opportunities to split.

To address this problem, we propose the following modifications to the splitting rule. We include a parameter bb,
the target number of observations per “bucket.” For each leaf, before testing possible
splits for a particular covariate, we order the observations by the covariate value in the treatment and control group separately. Within each group, we place the observations into buckets with bb observations per bucket. If this results in less than nmn_{m} buckets, then we use fewer observations
per bucket (to attain nmn_{m} buckets). We number the buckets, and considering splitting by bucket number rather than the raw
values of the covariates. This guarantees that when we shift from one split point to the next, we add both treatment and
control observations, leading to a smoother estimate of the goodness of fit function as a function of the split point. After the
best bucket number to split on is selected, we translate that into a split point by averaging the maximum covariate value in
the corresponding treatment and control buckets. In the simulations presented in this paper, we do not constrain the maximum number of buckets, and we let b=4b=4. We found that this discretization approach improved goodness of fit on average for the
simulations we considered, although
it can in principle make things worse.

In the simulations reported in Table 1 of ths paper, we used the infeasible MSEτ{\rm MSE}_{\tau} to evalute alternative estimators. In practice,
we must estimate the infeasible criterion. In the paper, we propose estimators that rely on the tree structure of our estimator,
but we may also wish to compare our performance to estimators that don’t rely on partitions. One alternative
is the M​S​ETOTMSE^{\text{TOT}} criterion. Given an estimator τ^i\hat{\tau}_{i}, it is equal to

|
| M​S​ETOT=1Nte​∑i=1Nte(Yi∗−τ^i)2.MSE^{\text{TOT}}=\frac{1}{N^{\rm te}}\sum_{i=1}^{N^{\rm te}}(Y^{*}_{i}-\hat{\tau}_{i})^{2}.
|

Because 𝔼⁡[Yi∗|Xi]=τ⁡(Xi)\mathbb{E}[Y_{i}^{*}|X_{i}]=\tau(X_{i}), this is an unbiased (but noisy) estimator for MSEτ{\rm MSE}_{\tau}. In Appendix Table A1, we present rankings
of estimators using this criterion. We see that it ranks estimators in the same way as MSEτ{\rm MSE}_{\tau} except in one case (Design 3 with 500 observations), but the percentage differences between
estimators are smaller than with the infeasible criterion.

Another tuning parameter for standard CART as well as the methods proposed here is the number of cross-validation samples. A
common convention is to use 10 samples. We deviate from that convention and use 5 cross-validation samples. The reason is
that our methods require various quantities to be estimated within leaves. Given a minimum leaf restriction of 25 treated and control
units, if we take a cross-validation sample of one-tenth of the original training sample, we might end up with no treated or no
control observations in a leaf in a cross-validation sample. In addition, it may be difficult to estimate a sample variance within a leaf.
Rather than require larger leaf sizes, we simply use fewer cross-validation samples.

Appendix Table A1 also includes the full set of estimates for the infeasible criterion MSEτ{\rm MSE}_{\tau}, to illustrate how sample size and
honest versus adaptive estimation affects the criterion. Note that for purposes of comparison to the simulation results from Table 1,
Table 1 reports the average over simulations of the ratio of the goodness of fit measures; the second panel of this table shows
the average of goodness of fit measures, but the ratio of the averages shown here is not exactly equal to the average of the ratios
shown in Table 1.

Appendix Table A1: Infeasible and Feasible MSE Estimates for Simulation Study

Design
1
2
3

Ntr=NestN^{\rm tr}=N^{\rm est}
500
1000
500
1000
500
1000

Estimator
M​S​EτTOTMSE^{\text{TOT}}_{\tau} Divided by M​S​EτTOTMSE^{\text{TOT}}_{\tau} for CT-H∗

TOT-H
1.010
1.009
1.001
1.001
1.004
1.008

F-H
1.013
1.004
1.039
1.049
1.121
1.161

TS-H
0.999
1.000
1.003
0.999
1.046
1.056

CT-H
1.000
1.000
1.000
1.000
1.000
1.000

Infeasible MSEτ{\rm MSE}_{\tau}

TOT-A
0.171
0.139
1.267
1.010
3.235
2.344

F-A
0.150
0.075
1.914
1.861
4.914
4.443

TS-A
0.103
0.077
1.509
1.080
4.068
3.169

CT-A
0.104
0.079
1.418
1.071
3.324
2.314

TOT-H
0.140
0.104
1.176
0.932
3.102
2.252

F-H
0.151
0.075
1.898
1.850
4.860
4.420

TS-H
0.083
0.053
1.201
0.887
3.732
2.935

CT-H
0.087
0.054
1.149
0.910
3.033
2.143

MSEτTOT∗(𝒮te,𝒮est,πEstimator(𝒮tr))/MSEτTOT(𝒮te,𝒮est,πCT-H(𝒮tr)){}^{*}{\rm MSE}^{\text{TOT}}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{Estimator}}({\cal S}^{\rm tr}))/{\rm MSE}^{\text{TOT}}_{\tau}({\cal S}^{\rm te},{\cal S}^{\rm est},\pi^{\text{CT-H}}({\cal S}^{\rm tr}))

##

-

<!-- fetch 2: https://api.crossref.org/works/10.1073/pnas.1510489113 + https://api.openalex.org/works/doi:10.1073/pnas.1510489113 | fetch.py json-metadata | 2026-11-06T23:17+07:00 | metadata -->
source: Crossref
title: Recursive partitioning for heterogeneous causal effects
authors: Athey, Susan; Imbens, Guido
container: Proceedings of the National Academy of Sciences
published: 2016-7-5
volume: 113
issue: 27
pages: 7353-7360
article number: 
publisher: National Academy of Sciences
doi: 10.1073/pnas.1510489113
type: journal-article
is-referenced-by-count (Crossref citations): 1330

abstract:
In this paper we propose methods for estimating heterogeneity in causal effects in experimental and observational studies and for conducting hypothesis tests about the magnitude of differences in treatment effects across subsets of the population. We provide a data-driven approach to partition the data into subpopulations that differ in the magnitude of their treatment effects. The approach enables the construction of valid confidence intervals for treatment effects, even with many covariates relative to the sample size, and without “sparsity” assumptions. We propose an “honest” approach to estimation, whereby one sample is used to construct the partition and another to estimate treatment effects for each subpopulation. Our approach builds on regression tree methods, modified to optimize for goodness of fit in treatment effects and to account for honest estimation. Our model selection criterion anticipates that bias will be eliminated by honest estimation and also accounts for the effect of making additional splits on the variance of treatment effect estimates within each subpopulation. We address the challenge that the “ground truth” for a causal effect is not observed for any individual unit, so that standard approaches to cross-validation must be modified. Through a simulation study, we show that for our preferred method honest estimation results in nominal coverage for 90% confidence intervals, whereas coverage ranges between 74% and 84% for nonhonest approaches. Honest estimation requires estimating the model with a smaller sample size; the cost in terms of mean squared error of treatment effects for our preferred method ranges between 7–22%.

source: OpenAlex
title: Recursive partitioning for heterogeneous causal effects
authors: Susan Carleton Athey; Guido W. Imbens
institutions: Stanford University
venue: Proceedings of the National Academy of Sciences
publication date: 2016-07-05
volume: 113
issue: 27
pages: 7353–7360
doi: https://doi.org/10.1073/pnas.1510489113
cited_by_count (OpenAlex): 1618
type: article
location: https://www.pnas.org/content/pnas/113/27/7353.full.pdf (open access: True)
location: https://www.ncbi.nlm.nih.gov/pmc/articles/4941430 (open access: True)
location: https://pubmed.ncbi.nlm.nih.gov/27382149 (open access: False)
location: http://arxiv.org/pdf/1504.01132 (open access: False)
location: https://arxiv.org/pdf/1504.01132 (open access: True)
location: http://deepblue.lib.umich.edu/bitstream/2027.42/135101/2/jep12592_am.pdf (open access: True)
location: https://hdl.handle.net/2027.42/135025 (open access: True)
location: https://arxiv.org/pdf/1504.01132.pdf (open access: True)
location: https://ideas.repec.org/p/arx/papers/1504.01132.html (open access: False)
location: https://doi.org/10.48550/arxiv.1504.01132 (open access: True)

abstract:
In this paper we propose methods for estimating heterogeneity in causal effects in experimental and observational studies and for conducting hypothesis tests about the magnitude of differences in treatment effects across subsets of the population. We provide a data-driven approach to partition the data into subpopulations that differ in the magnitude of their treatment effects. The approach enables the construction of valid confidence intervals for treatment effects, even with many covariates relative to the sample size, and without "sparsity" assumptions. We propose an "honest" approach to estimation, whereby one sample is used to construct the partition and another to estimate treatment effects for each subpopulation. Our approach builds on regression tree methods, modified to optimize for goodness of fit in treatment effects and to account for honest estimation. Our model selection criterion anticipates that bias will be eliminated by honest estimation and also accounts for the effect of making additional splits on the variance of treatment effect estimates within each subpopulation. We address the challenge that the "ground truth" for a causal effect is not observed for any individual unit, so that standard approaches to cross-validation must be modified. Through a simulation study, we show that for our preferred method honest estimation results in nominal coverage for 90% confidence intervals, whereas coverage ranges between 74% and 84% for nonhonest approaches. Honest estimation requires estimating the model with a smaller sample size; the cost in terms of mean squared error of treatment effects for our preferred method ranges between 7-22%.
