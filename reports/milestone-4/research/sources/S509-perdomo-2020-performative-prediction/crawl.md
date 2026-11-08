---
id: S509
url: https://arxiv.org/html/2002.06673
requested: arXiv:2002.06673
fetched: 2026-11-06T23:08+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T07
part: 5
raw: raw.html (661 KB)
conversion: html-text of https://arxiv.org/html/2002.06673 (readable, 14975 words)
---
title: Performative Prediction

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

arXiv:2002.06673v4 [cs.LG] 26 Feb 2021

# Performative Prediction

Juan C. Perdomo*    Tijana Zrnic*   Celestine Mendler-Dünner    Moritz Hardt

Affiliation: {jcperdomo, tijana.zrnic, mendler, hardt}@berkeley.edu

Affiliation: University of California, Berkeley

###### Abstract

When predictions support decisions they may influence the outcome they aim to predict. We call such predictions performative; the prediction influences the target. Performativity is a well-studied phenomenon in policy-making that has so far been neglected in supervised learning. When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining.

We develop a risk minimization framework for performative prediction bringing together concepts from statistics, game theory, and causality. A conceptual novelty is an equilibrium notion we call performative stability. Performative stability implies that the predictions are calibrated not against past outcomes, but against the future outcomes that manifest from acting on the prediction. Our main results are necessary and sufficient conditions for the convergence of retraining to a performatively stable point of nearly minimal loss.

In full generality, performative prediction strictly subsumes the setting known as strategic classification. We thus also give the first sufficient conditions for retraining to overcome strategic feedback effects.

## 1 Introduction

††

* Equal contribution.

Supervised learning excels at pattern recognition. When used to support consequential decisions, however, predictive models can trigger actions that influence the outcome they aim to predict. We call such predictions performative; the prediction causes a change in the distribution of the target variable.

Consider a simplified example of predicting credit default risk. A bank might estimate that a loan applicant has an elevated risk of default, and will act on it by assigning a high interest rate. In a self-fulfilling prophecy, the high interest rate further increases the customer's default risk. Put differently, the bank's predictive model is not calibrated to the outcomes that manifest from acting on the model.

Once recognized, performativity turns out to be ubiquitous. Traffic predictions influence traffic patterns, crime location prediction influences police allocations that may deter crime, recommendations shape preferences and thus consumption, stock price prediction determines trading activity and hence prices.

When ignored, performativity can surface as a form of distribution shift. As the decision-maker acts according to a predictive model, the distribution over data points appears to change over time. In practice, the response to such distribution shifts is to frequently retrain the predictive model as more data becomes available. Retraining is often considered an undesired — yet necessary — cat and mouse game of chasing a moving target.

What would be desirable from the perspective of the decision maker is a certain equilibrium where the model is optimal for the distribution it induces. Such equilibria coincide with the stable points of retraining, that is, models invariant under retraining. Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance.

This raises fundamental questions. When do such stable points exist? How can we efficiently find them? Under what conditions does retraining converge? When do stable points also have good predictive performance? In this work, we formalize performative prediction, tying together conceptual elements from statistical decision theory, causal reasoning, and game theory. We then resolve some of the fundamental questions that performativity raises.

### 1.1 Our contributions

We put performativity at the center of a decision-theoretic framework that extends the classical statistical theory underlying risk minimization. The goal of risk minimization is to find a decision rule, specified by model parameters θ\theta, that performs well on a fixed joint distribution 𝒟\mathcal{D} over covariates XX and an outcome variable YY.

Whenever predictions are performative, the choice of predictive model affects the observed distribution over instances Z=(X,Y)Z=(X,Y). We formalize this intuitive notion by introducing a map 𝒟⁡(⋅)\mathcal{D}(\cdot) from the set of model parameters to the space of distributions. For a given choice of parameters θ\theta, we think of 𝒟⁡(θ)\mathcal{D}(\theta) as the distribution over features and outcomes that results from making decisions according to the model specified by θ\theta. This mapping from predictive model to distribution is the key conceptual device of our framework.

A natural objective in performative prediction is to evaluate model parameters θ\theta on the resulting distribution 𝒟⁡(θ)\mathcal{D}(\theta) as measured via a loss function ℓ\ell. This results in the notion we call performative risk, defined as

|
| PR⁡(θ)=defEZ∼𝒟⁡(θ)ℓ​(Z,θ).\mathrm{PR}(\theta)\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\theta)\,.
|

The difficulty in minimizing PR⁡(θ)\mathrm{PR}(\theta) is that the distribution itself depends on the argument θ\theta, a dependence that defeats traditional theory for risk minimization. Moreover, we generally envision that the map 𝒟⁡(⋅)\mathcal{D}(\cdot) is unknown to the decision maker.

Perhaps the most natural algorithmic heuristic in this situation is a kind of fixed point iteration: repeatedly find a model that minimizes risk on the distribution resulting from the previous model, corresponding to the update rule

|
| θt+1=arg⁡minθ​EZ∼𝒟⁡(θt)ℓ​(Z,θ).\theta_{t+1}=\arg\min_{\theta}\E_{Z\sim\mathcal{D}(\theta_{t})}\ell(Z;\theta)\,.
|

We call this procedure repeated risk minimization. We also analyze its empirical counterpart that works in finite samples. These procedures exemplify a family of retraining heuristics that are ubiquitous in practice for dealing with all kinds of distributions shifts irrespective of cause.

When repeated risk minimization converges in objective value the model has minimal loss on the distribution it entails:

|
| PR⁡(θ)=minθ′⁡EZ∼𝒟⁡(θ)​ℓ​(Z,θ′).\mathrm{PR}(\theta)=\min_{\theta^{\prime}}\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\theta^{\prime})\,.
|

We refer to this condition as performative stability, noting that it is neither implied by nor does it imply minimal performative risk.

Our central result can be summarized informally as follows.

###### Theorem 1.1 (Informal).

If the loss is smooth, strongly convex, and the mapping 𝒟⁡(⋅)\mathcal{D}(\cdot) is sufficiently Lipschitz, then
repeated risk minimization converges to performative stability at a linear rate.

Moreover, if any one of these assumptions does not hold, repeated risk minimization can fail to converge at all.

The notion of Lipschitz continuity here refers to the Euclidean distance on model parameters and the Wasserstein distance on distributions. Informally, it requires that a small change in model parameters θ\theta does not have an outsized effect on the induced distribution 𝒟⁡(θ)\mathcal{D}(\theta).

In contrast to standard supervised learning, convexity alone is not sufficient for convergence in objective value, even if the other assumptions hold. Performative prediction therefore gives a new and interesting perspective on the importance of strong convexity.

Strong convexity has a second benefit. Not only does retraining converge to a stable point at a linear rate, this stable point also approximately minimizes the performative risk.

###### Theorem 1.2 (Informal).

If the loss is Lipschitz and strongly convex, and the map 𝒟⁡(⋅)\mathcal{D}(\cdot) is Lipschitz, all stable points and performative optima lie in a small neighborhood around each other.

Recall that performative stability on its own does not imply minimal performative risk. What the previous theorem shows, however, is that strong convexity guarantees that we can approximately satisfy both.

We complement our main results with a case study in strategic classification. Strategic classification aims to anticipate a strategic response to a classifier from an individual, who can change their features prior to being classified. We observe that strategic classification is a special case of performative prediction. On the one hand, this allows us to transfer our technical results to this established setting. In particular, our results are the first to give a guarantee on repeated risk minimization in the strategic setting. On the other hand, strategic classification provides us with one concrete setting for what the mapping 𝒟⁡(⋅)\mathcal{D}(\cdot) can be. We use this as a basis of an empirical evaluation in a semi-synthetic setting, where the initial distribution is based on a real data set, but the distribution map is modeled.

### 1.2 Related work

Performativity is a broad concept in the social sciences, philosophy, and economics [30, 18]. Below we focus on the relationship of our work to the most relevant technical scholarship.

#### Learning on non-stationary distributions.

A closely related line of work considers the problem of concept drift, broadly defined as the problem of learning when the target distribution over instances drifts with time. This setting has attracted attention both in the learning theory community [27, 3, 2] and by machine learning practitioners [14].

Concept drift is more general phenomenon than performativity in that it considers arbitrary sources of shift. However, studying the problem at this level of generality has led to a number of difficulties in creating a unified language and objective [14, 40], an issue we circumvent by assuming that the population distribution is determined by the deployed predictive model. Importantly, this line of work also discusses the importance of retraining [41, 14]. However, it stops short of discussing the need for stability or analyzing the long-term behavior of retraining.

#### Strategic classification.

Strategic classification recognizes that individuals often adapt to the specifics of a decision rule so as to gain an advantage (see, e.g.,  [11, 8, 15, 24]). Recent work in this area considers issues of incentive design [25, 32, 37, 4], control over an algorithm [10], and fairness concerns [20, 33]. Importantly, the concurrent work of Bechavod et al. [4] analyzes the implications of retraining in the context of causal discovery in linear models. Our model of performative prediction includes all notions of strategic adaption that we are aware of as a special case. Unlike many works in this area, our results do not depend on a specific cost function for changing individual features. Rather, we rely on an assumption about the sensitivity of the data-generating distribution to changes in the model parameters.

Recently, there has been increased interest within the algorithmic fairness community in classification dynamics. See, for example, Liu et al. [28], Hu and Chen [19], and Hashimoto et al. [17]. The latter work considers repeated risk minimization, but from the perspective of what it does to a measure of disparity between groups.

#### Causal inference.

The reader familiar with causality can think of 𝒟⁡(θ)\mathcal{D}(\theta) as the interventional distribution over instances ZZ resulting from a do-intervention that sets the model parameters to θ\theta in some underlying causal graph. Importantly, this mapping 𝒟⁡(⋅)\mathcal{D}(\cdot) remains fixed and does not change over time or by intervention: deploying the same model at two different points in time must induce the same distribution over observations ZZ. While causal inference focuses on estimating properties of interventional distributions such as treatment effects [35, 21], our focus is on a new stability notion and iterative retraining procedures for finding stable points.

#### Convex optimization.

The two solution concepts we introduce generalize the usual notion of optimality in (empirical) risk minimization to our new framework of performativity. Similarly, we extend the classical property of gradient descent acting as a contraction under smooth and strongly convex losses to account for distribution shifts due to performativity. Finally, we discuss how different regularity assumptions on the loss function affect convergence of retraining schemes, much like optimization works discuss these assumptions in the context of convergence of iterative optimization algorithms.

#### Reinforcement learning.

In general, any instance of performative prediction can be reframed as a reinforcement learning or contextual bandit problem. Yet, by studying performative prediction problems within such a broad framework, we lose many of the intricacies of performativity which make the problem interesting and tractable to analyze. We return to discuss some of the connections between both frameworks later on.

## 2 Framework and main definitions

In this section, we formally introduce the principal solution concepts of our framework: performative optimality and performative stability.

Throughout our presentation, we focus on predictive models that are parametrized by a vector θ∈�\theta\in\Theta, where the parameter space �⊆Rd\Theta\subseteq\mathbb{R}^{d} is a closed, convex set. We use capital letters to denote random variables and their lowercase counterparts to denote realizations of these variables. We consider instances z=(x,y)z=(x,y) defined as feature, outcome pairs, where x∈Rm−1x\in\mathbb{R}^{m-1} and y∈Ry\in\mathbb{R}. Whenever we define a variable θ∗=arg​minθ⁡g​(θ)\theta^{*}=\argmin_{\theta}g(\theta) as the minimizer of a function gg, we resolve the issue of the minimizer not being unique by setting θ∗\theta^{*} to an arbitrary point in the arg​minθ⁡g​(θ)\argmin_{\theta}g(\theta) set.

### 2.1 Performative optimality

In supervised learning, the goal is to learn a predictive model fθf_{\theta} which minimizes the expected loss with respect to feature, outcome pairs (x,y)(x,y) drawn i.i.d. from a fixed distribution 𝒟\mathcal{D}. The optimal model fθSLf_{{\theta_{\mathrm{SL}}}} solves the following optimization problem,

|
| θSL=arg​minθ∈�⁡EZ∼𝒟​ℓ​(Z,θ),{\theta_{\mathrm{SL}}}=\argmin_{\theta\in\Theta}\E_{Z\sim\mathcal{D}}\ell(Z;\theta),
|

where ℓ⁡(z,θ)\ell(z;\theta) denotes the loss of fθf_{\theta} at a point zz.

We contrast this with the performative optimum. As introduced previously, in settings where predictions support decisions, the manifested distribution over features and outcomes is in part determined by the deployed model. Instead of considering a fixed distribution 𝒟\mathcal{D}, each model fθf_{\theta} induces a potentially different distribution 𝒟⁡(θ)\mathcal{D}(\theta) over instances zz. A predictive model must therefore be evaluated with regard to the expected loss over the distribution 𝒟⁡(θ)\mathcal{D}(\theta) it induces: its performative risk.

###### Definition 2.1 (performative optimality and risk).

A model fθPOf_{{\theta_{\mathrm{PO}}}} is performatively optimal if the following relationship holds:

|
| θPO=arg​minθ⁡EZ∼𝒟⁡(θ)​ℓ​(Z,θ).{\theta_{\mathrm{PO}}}=\argmin_{\theta}\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\theta).
|

We define PR⁡(θ)=defEZ∼𝒟⁡(θ)ℓ​(Z,θ)\mathrm{PR}(\theta)\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\theta) as the performative risk; then, θPO=arg​minθ⁡PR​(θ){\theta_{\mathrm{PO}}}=\argmin_{\theta}\mathrm{PR}(\theta).

The following example illustrates the differences between the traditional notion of optimality in supervised learning and performative optima.

###### Example 2.2 (biased coin flip).

Consider the task of predicting the outcome of a biased coin flip where the bias of the coin depends on a feature XX and the assigned score fθ​(X)f_{\theta}(X).

In particular, define 𝒟⁡(θ)\mathcal{D}(\theta) in the following way. XX is a 1-dimensional feature supported on {±1}\{\pm 1\} and Y|X∼Bernoulli​(12+μ​X+ε​θ​X)Y~|~X\sim\text{Bernoulli}(\frac{1}{2}+\mu X+\varepsilon\theta X) with μ∈(0,12)\mu\in(0,\frac{1}{2}) and ε<12−μ\varepsilon<\frac{1}{2}-\mu. Assume that the class of predictors consists of linear models of the form fθ​(x)=θ​x+12f_{\theta}(x)=\theta x+\frac{1}{2} and that the objective is to minimize the squared loss: ℓ⁡(z,θ)=(y−fθ​(x))2\ell(z;\theta)=(y-f_{\theta}(x))^{2}.

The parameter ε\varepsilon represents the performative aspect of the model. If ε=0\varepsilon=0, outcomes are independent of the assigned scores and the problem reduces to a standard supervised learning task where the optimal predictive model is the conditional expectation fθSL​(x)=E[Y∣X=x]=12+μ​xf_{\theta_{\mathrm{SL}}}(x)=\E[Y\mid X=x]=\frac{1}{2}+\mu x, with θSL=μ{\theta_{\mathrm{SL}}}=\mu.

In the performative setting with ε​,0\varepsilon\neq 0, the optimal model θPO{\theta_{\mathrm{PO}}} balances between its predictive accuracy as well as the bias induced by the prediction itself. In particular, a direct calculation demonstrates that

|
| θPO=arg​minθ∈[0,1]EZ∼𝒟⁡(θ)(Y−θX−12)2⇔θPO=μ1−2​ε.{\theta_{\mathrm{PO}}}=\argmin_{\theta\in[0,1]}\E_{Z\sim\mathcal{D}(\theta)}\left(Y-\theta X-\frac{1}{2}\right)^{2}\quad\iff\quad{\theta_{\mathrm{PO}}}=\frac{\mu}{1-2\varepsilon}.
|

Hence, the performative optimum and the supervised learning solution are equal if ε=0\varepsilon=0 and diverge as the performativity strength ε\varepsilon increases.

### 2.2 Performative stability

A natural, desirable property of a model fθf_{\theta} is that, given that we use the predictions of fθf_{\theta} as a basis for decisions, those predictions are also simultaneously optimal for distribution that the model induces. We introduce the notion of performative stability to refer to predictive models that satisfy this property.

###### Definition 2.3 (performative stability and decoupled risk).

A model fθPSf_{{\theta_{\mathrm{PS}}}} is performatively stable if the following relationship holds:

|
| θPS=arg​minθ⁡EZ∼𝒟⁡(θPS)​ℓ​(Z,θ).{\theta_{\mathrm{PS}}}=\argmin_{\theta}\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\ell(Z;\theta).
|

We define DPR⁡(θ,θ′)=defEZ∼𝒟⁡(θ)ℓ​(Z,θ′){\mathrm{DPR}}(\theta,\theta^{\prime})\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\theta^{\prime}) as the decoupled performative risk; then, θPS=arg​minθ⁡DPR​(θPS,θ){\theta_{\mathrm{PS}}}=\argmin_{\theta}{\mathrm{DPR}}({\theta_{\mathrm{PS}}},\theta).

A performatively stable model fθPSf_{\theta_{\mathrm{PS}}} minimizes the expected loss on the distribution 𝒟⁡(θPS)\mathcal{D}({\theta_{\mathrm{PS}}}) resulting from deploying fθPSf_{\theta_{\mathrm{PS}}} in the first place. Therefore, a model that is performatively stable eliminates the need for retraining after deployment since any retraining procedure would simply return the same model parameters. Performatively stable models are fixed points of risk minimization. We further develop this idea in the next section.

Observe that performative optimality and performative stability are in general two distinct solution concepts. Performatively optimal models need not be performatively stable and performatively stable models need not be performatively optimal. We illustrate this point in the context of our previous biased coin toss example.

###### Example 02.2 (continued).

Consider again our model of a biased coin toss. In order for a predictive model fθf_{\theta} to be performatively stable, it must satisfy the following relationship:

|
| θPS=arg​minθ∈[0,1]EZ∼𝒟⁡(θPS)(Y−θX−12)2⇔θPS=μ1−ε.{\theta_{\mathrm{PS}}}=\argmin_{\theta\in[0,1]}\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\left(Y-\theta X-\frac{1}{2}\right)^{2}\quad\iff\quad{\theta_{\mathrm{PS}}}=\frac{\mu}{1-\varepsilon}.
|

Solving for θPS{\theta_{\mathrm{PS}}} directly, we see that there is a unique performatively stable point.

Therefore, performative stability and performative optimality need not identify. In fact, in this example they identify if and only if ε=0\varepsilon=0. Note that, in general, if the map 𝒟⁡(θ)\mathcal{D}(\theta) is constant across θ\theta, performative optima must coincide with performatively stable solutions. Furthermore, both coincide with "static" supervised learning solutions as well.

For ease of presentation, we refer to a choice of parameters θ\theta as performatively stable (optimal) if the model parametrized by θ\theta, fθf_{\theta} is performatively stable (optimal). We will occasionally also refer to performative stability as simply stability.

###### Remark 2.4.

Notice that both performative stability and optimality can be expressed via the decoupled performative risk as follows:

|
|
| θPS​ is performatively stable\displaystyle{\theta_{\mathrm{PS}}}\text{ is performatively stable }
| ⇔\displaystyle\Leftrightarrow
|
| θPS=arg​minθ⁡DPR​(θPS,θ),\displaystyle{\theta_{\mathrm{PS}}}=\argmin_{\theta}\;{\mathrm{DPR}}({\theta_{\mathrm{PS}}},\theta),
|
|

|
|
| θPO​ is performatively optimal\displaystyle{\theta_{\mathrm{PO}}}\text{ is performatively optimal }
| ⇔\displaystyle\Leftrightarrow
|
| θPO=arg​minθ⁡DPR​(θ,θ).\displaystyle{\theta_{\mathrm{PO}}}=\argmin_{\theta}\;{\mathrm{DPR}}(\theta,\theta).
|
|

## 3 When retraining converges to stable points

Having introduced our framework for performative prediction, we now address some of the basic questions that arise in this setting and examine the behavior of common machine learning practices, such as retraining, through the lens of performativity.

As discussed previously, performatively stable models have the favorable property that they achieve minimal risk for the distribution they induce and hence eliminate the need for retraining. However, it is a priori not clear that such stable points exist; and even if they do exist, whether we can find them efficiently. Furthermore, seeing as how performative optimality and stability are in general distinct solution concepts, under what conditions can we find models that approximately satisfy both?

In this work, we begin to answer these questions by analyzing two different optimization strategies. The first is retraining, formally referred to as repeated risk minimization (RRM), where the exact minimizer is repeatedly computed on the distribution induced by the previous model parameters. The second is repeated gradient descent (RGD), in which the model parameters are incrementally updated using a single gradient descent step on the objective defined by the previous iterate. We introduce RGD as a computationally efficient approximation of RRM, which, as we show, adopts many favorable properties of RRM.

Our algorithmic analysis of these methods reveals the existence of stable points under the assumption that the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is sufficiently Lipschitz. We identify necessary and sufficient conditions for convergence to a performatively stable point and establish properties of the objective under which stable points and performative optima are close.

We begin by analyzing the behavior of these procedures when they operate at a population level and then extend our analysis to finite samples.

### 3.1 Assumptions

It is easy to see that one cannot make any guarantees on the convergence of retraining or the existence of stable points without making some regularity assumptions on 𝒟⁡(⋅)\mathcal{D}(\cdot). One reasonable way to quantify the regularity of 𝒟⁡(⋅)\mathcal{D}(\cdot) is to assume Lipschitz continuity; the Lipschitz constant determines how sensitive the induced distribution is to a change in model parameters. Intuitively, such an assumption captures the idea that, if decisions are made according to similar predictive models, then the resulting distributions over instances should also be similar. We now introduce this key assumption of our work, which we call ε\varepsilon-sensitivity.

###### Definition 3.1 (ε\varepsilon-sensitivity).

We say that a distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive if for all θ,θ′∈�\theta,\theta^{\prime}\in\Theta:

|
| W1​(𝒟⁡(θ),𝒟⁡(θ′))6ε​‖θ−θ′‖2,W_{1}\big(\mathcal{D}(\theta),\mathcal{D}(\theta^{\prime})\big)\leqslant\varepsilon\|\theta-\theta^{\prime}\|_{2},
|

where W1W_{1} denotes the Wasserstein-1 distance, or earth mover’s distance.

The earth mover’s distance is a natural notion of distance between probability distributions that provides access to a rich technical repertoire [38, 39]. Furthermore, we can verify that it is satisfied in various settings.

###### Remark 3.2.

A simple example where this assumption is satisfied is for a Gaussian family. Given θ=(μ,σ1,…,σp)∈R2​p\theta=(\mu,\sigma_{1},\dots,\sigma_{p})\in\mathbb{R}^{2p}, define 𝒟⁡(θ)=𝒩⁡(ε1​μ,ε22​diag​(σ12,…,σp2))\mathcal{D}(\theta)=\mathcal{N}(\varepsilon_{1}\,\mu,\varepsilon_{2}^{2}\,\text{diag}(\sigma_{1}^{2},\dots,\sigma_{p}^{2})) where ε1,ε2∈R\varepsilon_{1},\varepsilon_{2}\in\mathbb{R}. Then 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive for ε=max⁡{|ε1|,|ε2|}\varepsilon=\max\big\{|\varepsilon_{1}|,|\varepsilon_{2}|\big\}.

In addition to this assumption on the distribution map, we will often make standard assumptions on the loss function ℓ⁡(z,θ)\ell(z;\theta) which hold for broad classes of losses. To simplify our presentation, let 𝒵=def∪θ∈�supp(𝒟(θ))\mathcal{Z}\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\cup_{\theta\in\Theta}\text{supp}(\mathcal{D}(\theta)).

- ∙\bullet

(joint smoothness) We say that a loss function ℓ⁡(z,θ)\ell(z;\theta) is β\beta-jointly smooth if the gradient ∇θℓ​(z,θ)\nabla_{\theta}\ell(z;\theta) is β\beta-Lipschitz in θ\theta and zz, that is

|
| ‖∇θℓ​(z,θ)−∇θℓ​(z,θ′)‖26β​‖θ−θ′‖2,‖∇θℓ​(z,θ)−∇θℓ​(z′,θ)‖26β​‖z−z′‖2,\left\|\nabla_{\theta}\ell(z;\theta)-\nabla_{\theta}\ell(z;\theta^{\prime})\right\|_{2}\leqslant\beta\left\|\theta-\theta^{\prime}\right\|_{2},~~\left\|\nabla_{\theta}\ell(z;\theta)-\nabla_{\theta}\ell(z^{\prime};\theta)\right\|_{2}\leqslant\beta\left\|z-z^{\prime}\right\|_{2},
|
| (A1)

for all θ,θ′∈�\theta,\theta^{\prime}\in\Theta and z,z′∈𝒵z,z^{\prime}\in\mathcal{Z}.

- ∙\bullet

(strong convexity) We say that a loss function ℓ⁡(z,θ)\ell(z;\theta) is γ\gamma-strongly convex if

|
| ℓ⁡(z,θ)>ℓ⁡(z,θ′)+∇θℓ​(z,θ′)⊤​(θ−θ′)+γ2​‖θ−θ′‖22,\ell(z;\theta)\geqslant\ell(z;\theta^{\prime})+\nabla_{\theta}\ell(z;\theta^{\prime})^{\top}(\theta-\theta^{\prime})+\frac{\gamma}{2}\left\|\theta-\theta^{\prime}\right\|_{2}^{2},
|
| (A2)

for all θ,θ′∈�\theta,\theta^{\prime}\in\Theta and z∈𝒵z\in\mathcal{Z}. If γ=0\gamma=0, this assumption is equivalent to convexity.

We will sometimes refer to βγ\frac{\beta}{\gamma}, where β\beta is as in (A1) and γ\gamma as in (A2), as the condition number.

### 3.2 Repeated risk minimization

We now formally define repeated risk minimization and prove one of our main results: sufficient and necessary conditions for retraining to converge to a performatively stable point.

###### Definition 3.3 (RRM).

Repeated risk minimization (RRM) refers to the procedure where, starting from an initial model fθ0f_{\theta_{0}}, we perform the following sequence of updates for every t>0t\geqslant 0:

|
| θt+1\displaystyle\theta_{t+1}
| =G⁡(θt)=defarg​minθ∈�⁡EZ∼𝒟⁡(θt)​ℓ​(Z,θ).\displaystyle=G(\theta_{t})\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\argmin_{\theta\in\Theta}\E_{Z\sim\mathcal{D}(\theta_{t})}\ell(Z;\theta).
|

Using a toy example, we again argue that restrictions on the map 𝒟⁡(⋅)\mathcal{D}(\cdot) are necessary to enable interesting analyses of RRM, otherwise it might be computationally infeasible to find performative optima, and performatively stable points might not even exist.

###### Example 3.4.

Consider optimizing the squared loss ℓ⁡(z,θ)=(y−θ)2\ell(z;\theta)=(y-\theta)^{2}, where θ∈[0,1]\theta\in[0,1] and the distribution of the outcome YY, according to 𝒟⁡(θ)\mathcal{D}(\theta), is a point mass at 0 if θ>12\theta\geqslant\frac{1}{2}, and a point mass at 1 if θ<12\theta<\frac{1}{2}. Clearly there is no performatively stable point, and RRM will simply result in the alternating sequence 1,0,1,0,…1,0,1,0,\dots. The performative optimum in this case is θPO=12{\theta_{\mathrm{PO}}}=\frac{1}{2}.

To show convergence of retraining schemes, it is hence necessary to make a regularity assumption on 𝒟⁡(⋅)\mathcal{D}(\cdot), such as ε\varepsilon-sensitivity. We are now ready to state our main result regarding the convergence of repeated risk minimization.

###### Theorem 3.5.

Suppose that the loss ℓ⁡(z,θ)\ell(z;\theta) is β\beta-jointly smooth (A1) and γ\gamma-strongly convex (A2). If the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive, then the following statements are true:

- (a)

‖G⁡(θ)−G⁡(θ′)‖26ε​βγ​‖θ−θ′‖2,for all ​θ,θ′∈�.\|G(\theta)-G(\theta^{\prime})\|_{2}\leqslant\varepsilon\frac{\beta}{\gamma}\|\theta-\theta^{\prime}\|_{2},~~\text{for all }\theta,\theta^{\prime}\in\Theta.

- (b)

If ε<γβ\varepsilon<\frac{\gamma}{\beta}, the iterates θt\theta_{t} of RRM converge to a unique performatively stable point θPS{\theta_{\mathrm{PS}}} at a linear rate:
‖θt−θPS‖26δ​ for ​t>(1−ε​βγ)−1​log⁡(‖θ0−θPS‖2δ)\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta\text{ for }t\geqslant\left(1-\varepsilon\frac{\beta}{\gamma}\right)^{-1}\log\left(\frac{\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}}{\delta}\right).

The main message of this theorem is that in performative prediction, if the loss function is sufficiently "nice" and the distribution map is sufficiently (in)sensitive, then one need only retrain a model a small number of times before it converges to a unique stable point. The complete proof of Theorem 3.5 can be found in Appendix D.1. Here, we provide the main intuition through a proof sketch.

###### Proof Sketch.

Fix θ,θ′∈�\theta,\theta^{\prime}\in\Theta. Let f⁡(φ)=EZ∼𝒟⁡(θ)ℓ​(Z,φ)f(\varphi)=\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\varphi) and f′​(φ)=EZ∼𝒟⁡(θ′)ℓ​(Z,φ)f^{\prime}(\varphi)=\E_{Z\sim\mathcal{D}(\theta^{\prime})}\ell(Z;\varphi). By applying standard properties of strong convexity and the fact that G⁡(θ)G(\theta) is the unique minimizer of f⁡(φ)f(\varphi), we can derive that

|
| −γ∥G(θ)−G(θ′)∥22>(G(θ)−G(θ′))⊤∇f(G(θ′)).-\gamma\|G(\theta)-G(\theta^{\prime})\|_{2}^{2}\geqslant\left(G(\theta)-G(\theta^{\prime})\right)^{\top}\nabla f(G(\theta^{\prime})).
|

Next, we observe that (G⁡(θ)−G⁡(θ′))⊤​∇θℓ​(z,G⁡(θ′))(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla_{\theta}\ell(z;G(\theta^{\prime})) is ‖G⁡(θ)−G⁡(θ′)‖2​β\|G(\theta)-G({\theta^{\prime}})\|_{2}\beta-Lipschitz in zz. This follows from applying the Cauchy-Schwarz inequality and the fact that the loss is β\beta-jointly smooth. Using the dual formulation of the earth mover’s distance (Lemma C.3) and ε\varepsilon-sensitivity of 𝒟⁡(⋅)\mathcal{D}(\cdot), as well as the first-order conditions of optimality for convex functions, a short calculation reveals that

|
| (G(θ)−G(θ′))⊤∇f(G(θ′))>−εβ∥G(θ)−G(θ′)∥2∥θ−θ′∥2.(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla f(G(\theta^{\prime}))\geqslant-\varepsilon\beta\|G(\theta)-G({\theta^{\prime}})\|_{2}\|\theta-\theta^{\prime}\|_{2}.
|

Claim (a) then follows by combining the previous two inequalities and rearranging. Intuitively, strong convexity forces the iterates to contract after retraining, yet this contraction is offset by the distribution shift induced by changing the underlying model parameters. Joint smoothness and ε\varepsilon-sensitivity ensure that this shift is not too large. Part (b) is essentially a consequence of applying the Banach fixed-point theorem to the result of part (a).
∎

One intriguing insight from our analysis is that this convergence result is in fact tight; removing any single assumption required for convergence by Theorem 3.5 is enough to construct a counterexample for which RRM diverges.

###### Proposition 3.6.

Suppose that the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε>0\varepsilon>0. RRM can fail to converge at all in any of the following cases, for any choice of parameters β,γ>0\beta,\gamma>0:

- (a)

The loss is β\beta-jointly smooth and convex, but not strongly convex.

- (b)

The loss is γ\gamma-strongly convex, but not jointly smooth.

- (c)

The loss is β\beta-jointly smooth and γ\gamma-strongly convex, but ε>γβ\varepsilon\geqslant\frac{\gamma}{\beta}.

We include a counterexample for statement (a), and defer the proofs of (b) and (c) to Appendix D.2.

###### Proof of Proposition 3.6(a):

Consider the linear loss defined as ℓ⁡((x,y),θ)=β​y​θ\ell\left((x,y);\theta\right)=\beta y\theta, for θ∈[−1,1]\theta\in[-1,1]. Note that this objective is β\beta-jointly smooth and convex, but not strongly convex. Let the distribution of YY according to 𝒟⁡(θ)\mathcal{D}(\theta) be a point mass at ε​θ\varepsilon\theta, and let the distribution of XX be invariant with respect to θ\theta. Clearly, this distribution is ε\varepsilon-sensitive.

Here, the decoupled performative risk has the following form DPR⁡(θ,φ)=ε​β​θ​φ{\mathrm{DPR}}(\theta,\varphi)=\varepsilon\beta\theta\varphi. The unique performatively stable point is 0. However, if we initialize RRM at any point other than 0, the procedure generates the sequence of iterates …,1,−1,1,−1​…\dots,1,-1,1,-1\dots, thus failing to converge. Furthermore, this behavior holds for all ε,β>0\varepsilon,\beta>0.
∎

Proposition 3.6 suggests a fundamental difference between strong and weak convexity in our framing of performative prediction (weak meaning γ=0\gamma=0). In supervised learning, using strongly convex losses generally guarantees a faster rate of optimization, yet asymptotically, the solution achieved with either strongly or weakly convex losses is globally optimal. However, in our framework, strong convexity is in fact necessary to guarantee convergence of repeated risk minimization, even for arbitrarily smooth losses and an arbitrarily small sensitivity parameter.

### 3.3 Repeated gradient descent

Theorem 3.5 demonstrates that repeated risk minimization converges to a unique performatively stable point if the sensitivity parameter ε\varepsilon is small enough. However, implementing RRM requires access to an exact optimization oracle. We now relax this requirement and demonstrate how a simple gradient descent algorithm also converges to a unique stable point.

###### Definition 3.7 (RGD).

Repeated gradient descent (RGD) is the procedure where, starting from an initial model fθ0f_{\theta_{0}}, we perform the following sequence of updates for every t>0t\geqslant 0:

|
| θt+1=Ggd​(θt)=def��​(θt−η​EZ∼𝒟⁡(θt)​∇θℓ​(Z,θt)),\theta_{t+1}=G_{\text{gd}}(\theta_{t})\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\Pi_{\Theta}\left(\theta_{t}-\eta\E_{Z\sim\mathcal{D}(\theta_{t})}\nabla_{\theta}\ell(Z;\theta_{t})\right),
|

where η>0\eta>0 is a fixed step size and ��\Pi_{\Theta} denotes the Euclidean projection operator onto �\Theta.

Note that repeated gradient descent only requires the loss ℓ\ell to be differentiable with respect to θ\theta. It does not require taking gradients of the performative risk. Like RRM, we can show that RGD is a contractive mapping for small enough sensitivity parameter ε\varepsilon.

###### Theorem 3.8.

Suppose that the loss ℓ⁡(z,θ)\ell(z;\theta) is β\beta-jointly smooth (A1) and γ\gamma-strongly convex (A2). If the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε<γ(β+γ)​(1+1.5​η​β)\varepsilon<\frac{\gamma}{(\beta+\gamma)(1+1.5\eta\beta)}, then RGD with step size η62β+γ\eta\leqslant\frac{2}{\beta+\gamma} satisfies the following:

- (a)

‖Ggd​(θ)−Ggd​(θ′)‖26(1−η​(β​γβ+γ−ε​(1.5​η​β2+β)))​∥θ−θ′∥2<∥θ−θ′∥2.\|G_{\text{gd}}(\theta)-G_{\text{gd}}(\theta^{\prime})\|_{2}\leqslant\left(1-\eta\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(1.5\eta\beta^{2}+\beta)\right)\right)\lVert\theta-\theta^{\prime}\rVert_{2}<\lVert\theta-\theta^{\prime}\rVert_{2}.

- (b)

The iterates θt\theta_{t} of RGD converge to a unique performatively stable point θPS{\theta_{\mathrm{PS}}} at a linear rate, ‖θt−θPS‖26δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta for t>1η​(β​γβ+γ−ε​(1.5​η​β2+β))−1​log⁡(‖θ0−θPS‖2δ)t\geqslant\frac{1}{\eta}{\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(1.5\eta\beta^{2}+\beta)\right)^{-1}}\log\left(\frac{\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}}{\delta}\right).

The conclusion of Theorem 3.8 is a strict generalization of a classical optimization result which considers a static objective, in which case the rate of contraction is (1−η​β​γβ+γ)\left(1-\eta\frac{\beta\gamma}{\beta+\gamma}\right) (see for example Theorem 2.1.15 in [34] or Lemma 3.7 in [16]). Our rate exactly matches this classical result in the case that ε=0\varepsilon=0. The proof of Theorem 3.8 can be found in Appendix D.3.

### 3.4 Finite-sample analysis

We now extend our main results regarding the convergence of RRM and RGD to the finite-sample regime. To do so, we leverage the fact that, under mild regularity conditions, the empirical distribution 𝒟n\mathcal{D}^{n} given by nn samples drawn i.i.d. from a true distribution 𝒟\mathcal{D} is with high probability close to 𝒟\mathcal{D} in earth mover’s distance [13].

We begin by defining the finite-sample version of these procedures.

###### Definition 3.9 (RERM & REGD).

Define repeated empirical risk minimization (RERM) to be the procedure where starting from a model fθ0f_{\theta_{0}} at every iteration t>0t\geqslant 0, we collect ntn_{t} samples from 𝒟⁡(θt)\mathcal{D}(\theta_{t}) and perform the update:

|
| θt+1=Gnt​(θt)=defarg​minθ⁡EZ∼𝒟nt​(θt)​ℓ​(Z,θ).\theta_{t+1}=G^{n_{t}}\left(\theta_{t}\right)\;\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\;\argmin_{\theta}\E_{Z\sim\mathcal{D}^{n_{t}}(\theta_{t})}\ell(Z;\theta).
|

Similarly, define repeated empirical gradient descent (REGD) to be the optimization procedure with update rule:

|
| θt+1=Ggdnt​(θt)=def��​(θt−η​EZ∼𝒟nt​(θt)​∇θℓ​(Z,θt)).\theta_{t+1}=G_{\text{gd}}^{n_{t}}(\theta_{t})\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\Pi_{\Theta}\left(\theta_{t}-\eta\E_{Z\sim\mathcal{D}^{n_{t}}(\theta_{t})}\nabla_{\theta}\ell(Z;\theta_{t})\right).
|

Here, η>0\eta>0 is a step size and ��\Pi_{\Theta} denotes the Euclidean projection operator onto �\Theta.

The following theorem illustrates that with enough samples collected at every iteration, with high probability both algorithms converge to a small neighborhood around a stable point. Recall that mm is the dimension of data samples zz.

###### Theorem 3.10.

Suppose that the loss ℓ⁡(z,θ)\ell(z;\theta) is β\beta-jointly smooth (A1) and γ\gamma-strongly convex (A2), and that there exist α>1,μ>0\alpha>1,\mu>0 such that ξα,μ=def∫Rmeμ​|x|α​𝑑𝒟​(θ)\xi_{\alpha,\mu}\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\intop\nolimits_{\mathbb{R}^{m}}e^{\mu|x|^{\alpha}}d\mathcal{D}(\theta) is finite ∀θ∈�\forall\theta\in\Theta. Let δ∈(0,1)\delta\in(0,1) be a radius of convergence. Consider running RERM or RGD with nt=O⁡(1(ε​δ)m​log⁡(tp))n_{t}=O\left(\frac{1}{(\varepsilon\delta)^{m}}\log\big(\frac{t}{p}\big)\right) samples at time tt.

- (a)

If 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε<γ2​β\varepsilon<\frac{\gamma}{2\beta}, then with probability 1−p1-p, RERM satisfies,

|
| ‖θt−θPS‖26δ, for all ​t>log⁡(1δ​‖θ0−θPS‖2)(1−2​ε​βγ).\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta,\text{ for all }t\geqslant\frac{\log\left(\frac{1}{\delta}\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}\right)}{\left(1-\frac{2\varepsilon\beta}{\gamma}\right)}.
|

- (b)

If 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε<γ(β+γ)​(1+1.5​η​β)\varepsilon<\frac{\gamma}{(\beta+\gamma)(1+1.5\eta\beta)}, then with probability 1−p1-p, REGD with satisfies,

|
| ‖θt−θPS‖26δ, for all ​t>log⁡(1δ​‖θ0−θPS‖2)η​(β​γβ+γ−ε​(3​η​β2+2​β)),\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta,\text{ for all }t\geqslant\frac{\log\left(\frac{1}{\delta}\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}\right)}{\eta\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(3\eta\beta^{2}+2\beta)\right)},
|

for a constant choice of step size η62β+γ.\eta\leqslant\frac{2}{\beta+\gamma}.

###### Proof sketch.

The basic idea behind these results is the following. While ‖θt−θPS‖2>δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}>\delta, the sample size ntn_{t} is sufficiently large to ensure a behavior similar to that on a population level: as in Theorems 3.5 and 3.8, the iterates θt\theta_{t} contract toward θPS{\theta_{\mathrm{PS}}}. This implies that θt\theta_{t} eventually enters a δ\delta-ball around θPS{\theta_{\mathrm{PS}}}, for some large enough tt. Once this happens, contrary to population-level results, a contraction is no longer guaranteed due to the noise inherent in observing only finite-sample approximations of 𝒟⁡(θt)\mathcal{D}(\theta_{t}). Nevertheless, the sample size ntn_{t} is sufficiently large to ensure that θt\theta_{t} cannot escape a δ\delta-ball around θPS{\theta_{\mathrm{PS}}} either.
∎

## 4 Relating performative optimality and stability

As we discussed previously, while performative optima are always guaranteed to exist,11
1

In particular, they are guaranteed to exist over the extended real line, i.e. we allow θ∈(R∪{±∞})d\theta\in(\mathbb{R}\cup\{\pm\infty\})^{d}. it is not clear whether performatively stable points exist in all settings. Our algorithmic analysis of repeated risk minimization and repeated gradient descent revealed the existence of unique stable points under the assumption that the objective is strongly convex and smooth. The first result of this section illustrates existence of stable points under weaker assumptions on the loss, in the case where the solution space �\Theta is constrained. All proofs can be found in Appendix D.

###### Proposition 4.1.

Let the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) be ε\varepsilon-sensitive and �⊂Rd\Theta\subset\mathbb{R}^{d} be compact. If the loss ℓ⁡(z,θ)\ell(z;\theta) is convex and jointly continuous in (z,θ)(z,\theta), then there exists a performatively stable point.

A natural question to consider at this point is whether there are procedures analogous to RRM and RGD for efficiently computing performative optima.

Our analysis suggests that directly minimizing the performative risk is in general a more challenging problem than finding performatively stable points. In particular, we can construct simple examples where the performative risk PR⁡(θ)\mathrm{PR}(\theta) is non-convex, despite strong regularity assumptions on the loss and the distribution map.

###### Proposition 4.2.

The performative risk PR⁡(θ)\mathrm{PR}(\theta) can be concave in θ\theta, even if the loss ℓ⁡(z,θ)\ell(z;\theta) is β\beta-jointly smooth (A1), γ\gamma-strongly convex (A2), and the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε<γβ\varepsilon<\frac{\gamma}{\beta}.

However, what we can show is that there are cases where finding performatively stable points is sufficient to guarantee that the resulting model has low performative risk. In particular, our next result demonstrates that if the loss function ℓ⁡(z,θ)\ell(z;\theta) is Lipschitz in zz and γ\gamma-strongly convex, then all performatively stable points and performative optima lie in a small neighborhood around each other. Moreover, the theorem holds for cases where performative optima and performatively stable points are not necessarily unique.

###### Theorem 4.3.

Suppose that the loss ℓ⁡(z,θ)\ell(z;\theta) is LzL_{z}-Lipschitz in zz, γ\gamma-strongly convex (A2), and that the distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive. Then, for every performatively stable point θPS{\theta_{\mathrm{PS}}} and every performative optimum θPO{\theta_{\mathrm{PO}}}:

|
| ‖θPO−θPS‖262​Lz​εγ.\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\frac{2L_{z}\varepsilon}{\gamma}.
|

This result shows that in cases where repeated risk minimization converges to a stable point, the resulting model approximately minimizes the performative risk.

Moreover, Theorem 4.3 suggests a way of converging close to performative optima in objective value even if the loss function is smooth and convex, but not strongly convex. In particular, by adding quadratic regularization to the objective, we can ensure that RRM or RGD converge to a stable point that approximately minimizes the performative risk, see Appendix E.

## 5 A case study in strategic classification

Having presented our model for performative prediction, we now proceed to illustrate how these ideas can be applied within the context of strategic classification and discuss some of the implications of our theorems for this setting.

We begin by formally establishing how strategic classification can be cast as a performative prediction problem and illustrate how our framework can be used to derive results regarding the convergence of popular retraining heuristics in strategic classification settings. Afterwards, we further develop the connections between both fields by empirically evaluating the behavior of repeated risk minimization on a dynamic credit scoring task.

### 5.1 Stackelberg equilibria are performative optima

Strategic classification is a two-player game between an institution which deploys a classifier and agents who selectively adapt their features in order to improve their outcomes.

A classic example of this setting is that of a bank which uses a machine learning classifier to predict whether or not a loan applicant is creditworthy. Individual applicants react to the bank’s classifier by manipulating their features with the hopes of inducing a favorable classification. This game is said to have a Stackelberg structure since agents adapt their features only after the bank has deployed their classifier.

The optimal strategy for the institution in a strategic classification setting is to deploy the solution corresponding to the Stackelberg equilibrium, defined as the classifier fθf_{\theta} which achieves minimal loss over the induced distribution 𝒟⁡(θ)\mathcal{D}(\theta) in which agents have strategically adapted their features in response to fθf_{\theta}. In fact, we see that this equilibrium notion exactly matches our definition of performative optimality:

|
| fθSE​ is a Stackelberg equilibrium⇔θSE∈arg​minθ⁡PR​(θ).f_{\theta_{\mathrm{SE}}}\text{ is a Stackelberg equilibrium}\iff\theta_{\mathrm{SE}}\in\argmin_{\theta}\mathrm{PR}(\theta).
|

We think of 𝒟\mathcal{D} as a "baseline" distribution over feature-outcome pairs before any classifier deployment, and 𝒟⁡(θ)\mathcal{D}(\theta) denotes the distribution over features and outcomes obtained by strategically manipulating 𝒟\mathcal{D}. As described in existing work [15, 33, 8], the distribution function 𝒟⁡(θ)\mathcal{D}(\theta) in strategic classification corresponds to the data-generating process outlined in Figure 1.

Input: base distribution 𝒟\mathcal{D}, classifier fθf_{\theta}, cost function cc, and utility function uu

Sampling procedure for 𝒟⁡(θ)\mathcal{D}(\theta):

1.

Sample (x,y)∼𝒟(x,y)\sim\mathcal{D}

2.

Compute best response xBR←arg​maxx′⁡u​(x′,θ)−c⁡(x′,x)x_{\mathrm{BR}}\leftarrow\argmax_{x^{\prime}}u(x^{\prime},\theta)-c(x^{\prime},x)

3.

Output sample (xBR,y)(x_{\mathrm{BR}},\;y)

Figure 1: Distribution map for strategic classification.

Here, uu and cc are problem-specific functions which determine the best response for agents in the game. Together with the base distribution 𝒟\mathcal{D}, these define the relevant distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) for the problem of strategic classification.

A strategy that is commonly adapted in practice as a means of coping with the distribution shift that arises in strategic classification is to repeatedly retrain classifiers on the induced distributions. This procedure corresponds to the repeated risk minimization procedure introduced in Definition 3.3. Our results describe the first set of sufficient conditions under which repeated retraining overcomes strategic effects.

###### Corollary 5.1.

Let the institution’s loss ℓ⁡(z,θ)\ell(z;\theta) be LzL_{z}- and LθL_{\theta}-Lipschitz in zz and θ\theta respectively, β\beta-jointly smooth (A1), and γ\gamma-strongly convex (A2). If the induced distribution map is ε\varepsilon-sensitive, with ε<γβ\varepsilon<\frac{\gamma}{\beta}, then RRM converges at a linear rate to a performatively stable classifier θPS{\theta_{\mathrm{PS}}} that is 2​Lz​ε​(Lθ+Lz​ε)​γ−12L_{z}\varepsilon(L_{\theta}+L_{z}\varepsilon)\gamma^{-1} close in objective value to the Stackelberg equilibrium.

### 5.2 Simulations

We next examine the convergence of repeated risk minimization and repeated gradient descent in a simulated strategic classification setting. We run experiments on a dynamic credit scoring simulator in which an institution classifies the creditworthiness of loan applicants.22
2

Code is available at https://github.com/zykls/performative-prediction, and the simulator has been integrated into the WhyNot software package [31]. As motivated previously, agents react to the institution’s classifier by manipulating their features to increase the likelihood that they receive a favorable classification.

To run our simulations, we construct a distribution map 𝒟⁡(θ)\mathcal{D}(\theta), as described in Figure 1. For the base distribution 𝒟\mathcal{D}, we use a class-balanced subset of a Kaggle credit scoring dataset [22]. Features x∈Rm−1x\in\mathbb{R}^{m-1} correspond to historical information about an individual, such as their monthly income and number of credit lines. Outcomes y∈{0,1}y\in\{0,1\} are binary variables which are equal to 1 if the individual defaulted on a loan and 0 otherwise.

Figure 2: Convergence in domain of RRM (left) and RGD (right) for varying ε\varepsilon-sensitivity parameters. We add a marker if at the next iteration the distance between iterates is numerically zero. We normalize the distance by c=‖θ0,S‖2−1c=\|\theta_{0,S}\|_{2}^{-1}.

The institution makes predictions using a logistic regression classifier. We assume that individuals have linear utilities u⁡(θ,x)=−⟨θ,x⟩u(\theta,x)=-\langle\theta,x\rangle and quadratic costs c⁡(x′,x)=12​ε​∥x′−x∥22c(x^{\prime},x)=\frac{1}{2\varepsilon}\lVert x^{\prime}-x\rVert_{2}^{2}, where ε\varepsilon is a positive constant that regulates the cost incurred by changing features. Linear utilities indicate that agents wish to minimize their assigned probability of default.

We divide the set of features into strategic features S⊆[m−1]S\subseteq[m-1], such as the number of open credit lines, and non-strategic features (e.g., age). Solving the optimization problem described in Figure 1, the best response for an individual corresponds to the following update,

|
| xS′=xS−ε​θS,x^{\prime}_{S}=x_{S}-\varepsilon\theta_{S},
|

where xS,xS′,θS∈R|S|x_{S},x^{\prime}_{S},\theta_{S}\in\mathbb{R}^{|S|}. As per convention in the literature [8, 15, 33], individual outcomes yy are unaffected by strategic manipulation.

Intuitively, this data-generating process is ε\varepsilon-sensitive since for a given choice of classifiers, fθf_{\theta} and fθ′f_{\theta^{\prime}}, an individual feature vector is shifted to xS−ε​θSx_{S}-\varepsilon\theta_{S} and to xS−ε​θS′x_{S}-\varepsilon\theta^{\prime}_{S}, respectively. The distance between these two shifted points is equal to ε​‖θS−θS′‖2\varepsilon\|\theta_{S}-\theta^{\prime}_{S}\|_{2}. Since the optimal transport distance is bounded by ε​‖θ−θ′‖2\varepsilon\|\theta-\theta^{\prime}\|_{2} for every individual point, it is also bounded by this quantity over the entire distribution. A full proof of this claim is presented in Appendix B.2.

For our experiments, instead of sampling from 𝒟⁡(θ)\mathcal{D}(\theta), we treat the points in the original dataset as the true distribution. Hence, we can think of all the following procedures as operating at the population level. Furthermore, we add a regularization term to the logistic loss to ensure that the objective is strongly convex.

#### Repeated risk minimization.

The first experiment we consider is the convergence of RRM. From our theoretical analysis, we know that RRM is guaranteed to converge at a linear rate to a performatively stable point if the sensitivity parameter ε\varepsilon is smaller than γβ\frac{\gamma}{\beta}. In Figure 2 (left), we see that RRM does indeed converge in only a few iterations for small values of ε\varepsilon while it divergences if ε\varepsilon is too large.

Figure 3: Performative risk (left) and accuracy (right) of the classifier θt\theta_{t} at different stages of RRM for ε=80\varepsilon=80. Blue lines indicates the optimization phase and green lines indicate the effect of the distribution shift after the classifier deployment.

The evolution of the performative risk during the RRM optimization is illustrated in Figure 3. We evaluate PR⁡(θ)\mathrm{PR}(\theta) at the beginning and at the end of each optimization round and indicate the effect due to distribution shift with a dashed green line. We also verify that the surrogate loss is a good proxy for classification accuracy in the performative setting.

#### Repeated gradient descent.

In the case of RGD, we find similar behavior to that of RRM. While the iterates again converge linearly, they naturally do so at a slower rate than in the exact minimization setting, given that each iteration consists only of a single gradient step.
Again, we can see in Figure 2 that the iterates converge for small values of ε\varepsilon and diverge for large values.

## 6 Discussion and Future Work

Our work draws attention to the fundamental problem of performativity in statistical learning and decision-making. Performative prediction enjoys a clean formal setup that we introduced, drawing on elements from causality and game theory.

Retraining is often considered a nuisance intended to cope with distribution shift. In contrast, our work interprets retraining as the natural equilibrating dynamic for performative prediction. The fixed points of retraining are performative stable points. Moreover, retraining converges to such stable points under natural assumptions, including strong convexity of the loss function. It is interesting to note that (weak) convexity alone is not enough. Performativity thus gives another intriguing perspective on why strong convexity is desirable in supervised learning.

Several interesting questions remain. For example, by letting the step size of repeated gradient descent tend to 00, we see that this procedure converges for ε<γβ+γ\varepsilon<\frac{\gamma}{\beta+\gamma}. Exact repeated risk minimization, on the other hand, provably converges for every ε<γβ\varepsilon<\frac{\gamma}{\beta}, and we showed this inequality is tight. It would be interesting to understand whether this gap is a fundamental difference between both procedures or an artifact of our analysis.

Lastly, we believe that the tools and ideas from performative prediction can be used to make progress in other subareas of machine learning. For example, in this paper, we have illustrated how reframing strategic classification as a performative prediction problem leads to a new understanding of when retraining overcomes strategic effects. However, we view this example as only scratching the surface of work connecting performative prediction with other fields.

In particular, reinforcement learning can be thought of as a case of performative prediction. In this setting, the choice of policy fθf_{\theta}, affects the distribution 𝒟⁡(θ)\mathcal{D}(\theta) over z={(sh,ah)}h=1∞z=\{(s_{h},a_{h})\}_{h=1}^{\infty}, the set of visited states, ss, and actions, aa, in a Markov Decision Process. Building off this connection, we can reinterpret repeated risk minimization as a form of off-policy learning in which an agent first collects a batch of data under a particular policy fθf_{\theta}, and then finds the optimal policy for that trajectory offline. We believe that some of the ideas developed in the context of performative prediction can shed new light on when these off-policy methods can converge.

## Acknowledgements

We wish to acknowledge support from the U.S. National Science Foundation Graduate Research Fellowship Program and the Swiss National Science Foundation Early Postdoc Mobility Fellowship Program.

## References

- [1]

C.D. Aliprantis and K.C. Border.

Infinite Dimensional Analysis: A Hitchhiker’s Guide.

Springer Berlin Heidelberg, 2006.

- [2]

Peter L. Bartlett.

Learning with a Slowly Changing Distribution.

In Proceedings of the Fifth Annual ACM Conference on
Computational Learning Theory (COLT), pages 243–252, 1992.

- [3]

Peter L. Bartlett, Shai Ben-David, and Sanjeev R. Kulkarni.

Learning Changing Concepts by Exploiting the Structure of Change.

Machine Learning, 41(2):153–174, 2000.

- [4]

Yahav Bechavod, Katrina Ligett, Zhiwei Steven Wu, and Juba Ziani.

Causal Feature Discovery through Strategic Modification.

arXiv preprint arXiv:2002.07024, 2020.

- [5]

Claude Berge.

Topological Spaces.

Courier Corporation, 1997.

- [6]

Richard J Bolton and David J Hand.

Statistical Fraud Detection: A Review.

Statistical Science, pages 235–249, 2002.

- [7]

Léon Bottou, Jonas Peters, Joaquin Quiñonero-Candela, Denis X Charles,
D Max Chickering, Elon Portugaly, Dipankar Ray, Patrice Simard, and
Ed Snelson.

Counterfactual Reasoning and Learning Systems: The Example of
Computational Advertising.

The Journal of Machine Learning Research, 14(1):3207–3260,
2013.

- [8]

Michael Brückner, Christian Kanzow, and Tobias Scheffer.

Static Prediction Games for Adversarial Learning Problems.

Journal of Machine Learning Research, 13(Sep):2617–2654, 2012.

- [9]

Sébastien Bubeck.

Convex Optimization: Algorithms and Complexity.

Foundations and Trends® in Machine Learning,
8(3-4):231–357, 2015.

- [10]

Jenna Burrell, Zoe Kahn, Anne Jonas, and Daniel Griffin.

When Users Control the Algorithms: Values Expressed in Practices on
Twitter.

Proceedings of the ACM on Human-Computer Interaction, 3:19,
2019.

- [11]

Nilesh Dalvi, Pedro Domingos, Sumit Sanghai, and Deepak Verma.

Adversarial Classification.

In Proceedings of the 1010th ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining, pages 99–108, 2004.

- [12]

Danielle Ensign, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger, and
Suresh Venkatasubramanian.

Runaway Feedback Loops in Predictive Policing.

In Proceedings of the 1st ACM Conference on Fairness,
Accountability and Transparency, pages 160–171, 2018.

- [13]

Nicolas Fournier and Arnaud Guillin.

On the Rate of Convergence in Wasserstein Distance of the Empirical
Measure.

Probability Theory and Related Fields, 162(3):707–738, 2015.

- [14]

João Gama, Indrė Žliobaitė, Albert Bifet, Mykola Pechenizkiy,
and Abdelhamid Bouchachia.

A Survey on Concept Drift Adaptation.

ACM Computing Surveys (CSUR), 46(4):1–37, 2014.

- [15]

Moritz Hardt, Nimrod Megiddo, Christos Papadimitriou, and Mary Wootters.

Strategic Classification.

In Proceedings of the ACM Conference on Innovations in
Theoretical Computer Science, pages 111–122, 2016.

- [16]

Moritz Hardt, Ben Recht, and Yoram Singer.

Train Faster, Generalize Better: Stability of Stochastic Gradient
Descent.

In Proceedings of the 33rd International Conference on Machine
Learning (ICML), pages 1225–1234, 2016.

- [17]

Tatsunori Hashimoto, Megha Srivastava, Hongseok Namkoong, and Percy Liang.

Fairness Without Demographics in Repeated Loss Minimization.

In Proceedings of the 35th International Conference on Machine
Learning (ICML), pages 1929–1938, 2018.

- [18]

Kieran Healy.

The Performativity of Networks.

European Journal of Sociology/Archives Européennes de
Sociologie, 56(2):175–205, 2015.

- [19]

Lily Hu and Yiling Chen.

A Short-term Intervention for Long-term Fairness in the Labor
Market.

In Proceedings of the World Wide Web Conference, pages
1389–1398, 2018.

- [20]

Lily Hu, Nicole Immorlica, and Jennifer Wortman Vaughan.

The Disparate Effects of Strategic Manipulation.

In Proceedings of the 2nd ACM Conference on Fairness,
Accountability, and Transparency, pages 259–268, 2019.

- [21]

Guido W Imbens and Donald B Rubin.

Causal Inference in Statistics, Social, and Biomedical
sciences.

Cambridge University Press, 2015.

- [22]

Kaggle.

Give me some credit.

https://www.kaggle.com/c/GiveMeSomeCredit/data, 2012.

- [23]

Shizuo Kakutani.

A Generalization of Brouwer’s Fixed Point Theorem.

Duke Mathematical Journal, 8(3):457–459, 1941.

- [24]

Moein Khajehnejad, Behzad Tabibian, Bernhard Schölkopf, Adish Singla, and
Manuel Gomez-Rodriguez.

Optimal Decision Making Under Strategic Behavior.

arXiv preprint arXiv:1905.09239, 2019.

- [25]

Jon Kleinberg and Manish Raghavan.

How Do Classifiers Induce Agents to Invest Effort Strategically?

In Proceedings of the ACM Conference on Economics and
Computation (EC), pages 825–844, 2019.

- [26]

Amanda Kube, Sanmay Das, and Patrick J Fowler.

Allocating Interventions Based on Predicted Outcomes: A Case Study
on Homelessness Services.

In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 33, pages 622–629, 2019.

- [27]

Anthony Kuh, Thomas Petsche, and Ronald L Rivest.

Learning Time-Varying Concepts.

In Advances in Neural Information Processing Systems (NIPS),
pages 183–189, 1991.

- [28]

Lydia T Liu, Sarah Dean, Esther Rolf, Max Simchowitz, and Moritz Hardt.

Delayed Impact of Fair Machine Learning.

In Proceedings of the 35th International Conference on Machine
Learning (ICML), pages 3150–3158, 2018.

- [29]

Kristian Lum and William Isaac.

To Predict and Serve?

Significance, 13(5):14–19, 2016.

- [30]

Donald A MacKenzie, Fabian Muniesa, and Lucia Siu.

Do Economists Make Markets?: On the Performativity of
Economics.

Princeton University Press, 2007.

- [31]

John Miller, Chloe Hsu, Jordan Troutman, Juan Perdomo, Tijana Zrnic, Lydia Liu,
Yu Sun, Ludwig Schmidt, and Moritz Hardt.

Whynot, 2020.

- [32]

John Miller, Smitha Milli, and Moritz Hardt.

Strategic Classification is Causal Modeling in Disguise.

arXiv preprint arXiv:1910.10362, 2019.

- [33]

Smitha Milli, John Miller, Anca D Dragan, and Moritz Hardt.

The Social Cost of Strategic Classification.

In Proceedings of the 2nd ACM Conference on Fairness,
Accountability, and Transparency, pages 230–239, 2019.

- [34]

Yurii Nesterov.

Introductory Lectures on Convex Optimization: A Basic Course,
volume 87.

Springer Science & Business Media, 2013.

- [35]

Judea Pearl.

Causality.

Cambridge University Press, 2009.

- [36]

Shai Shalev-Shwartz and Shai Ben-David.

Understanding Machine Learning: From Theory to Algorithms.

Cambridge University Press, 2014.

- [37]

Yonadav Shavit, Benjamin Edelman, and Brian Axelrod.

Learning From Strategic Agents: Accuracy, Improvement, and
Causality.

arXiv preprint arXiv:2002.10066, 2020.

- [38]

Cédric Villani.

Topics in optimal transportation.

Number 58. American Mathematical Society, 2003.

- [39]

Cédric Villani.

Optimal Transport: Old and New, volume 338.

Springer Science & Business Media, 2008.

- [40]

Geoffrey I. Webb, Roy Hyde, Hong Cao, Hai Long Nguyen, and Francois Petitjean.

Characterizing Concept Drift.

Data Mining and Knowledge Discovery, 30(4):964–994, 2016.

- [41]

Indrė Žliobaitė.

Learning under Concept Drift: An Overview.

arXiv preprint arXiv:1010.4784, 2010.

- [42]

Indrė Žliobaitė, Mykola Pechenizkiy, and Joao Gama.

An Overview of Concept Drift Applications.

In Big Data Analysis: New Algorithms for a New Society, pages
91–114. Springer, 2016.

## Appendix A Applications of performativity

To illustrate the fact that performativity is a common cause for concept drift, we review a table of concepts drift applications from [42]. In Table 1, we highlight those settings that naturally occur due to performativity. Below we briefly discuss the role of performativity in such applications.

Monitoring & control
Information management
Analytics & diagnostics

Security,

Police

fraud detection,

insider trading detection,

adversary actions detection

next crime place

prediction

crime volume

prediction

Finance,

Banking,

Telecom,

Insurance,

Marketing,

Retail,

Advertising

monitoring & management

of customer segments,

bankruptcy prediction

product or service

recommendation,

including complimentary,

user intent or information

need prediction

demand prediction,

response rate

prediction, budget

planning

Production

industry

controlling output quality
-
predict bottlenecks

Education

(e-Learning,

e-Health),

Media,

Entertainment

gaming the system,

drop out prediction

music, VOD, movie,

news, learning object

personalized search

& recommendations

player-centered game

design, learner-centered

education

Table 1: Table of concept drift applications from Žliobaitė et al. [42]

The role of fraud detection systems is to predict whether an instance such as a transaction or email is legitimate or not. It is well-known that designers of such fraudulent instances adapt to the fraud detection system in place in order to breach security [6]. Therefore, the deployment of fraud detection systems shapes the features of fraudulent instances.

Crime place prediction, sometimes referred to as predictive policing [12, 26, 29], uses historical data to estimate the likelihood of crime at a given location. Those locations where criminal behavior is deemed likely by the system typically get more police patrols and better surveillance which act on the one hand to deter crime. These actions resulting from prediction significantly decrease the probability of crime taking place, thus changing the data used for future predictions.

In personalized recommendations, instances are recommended to a user based on their historical context, such as their ratings or purchases. The set of recommendations thus depends on the trained machine learning model, which in turn changes the user’s future ratings or purchases [7]. In other words, user features serving as input to a recommender inevitably depend on the previously used recommendation mechanisms.

In online two-player games, it is common to request an AI opponent. The level of sophistication of the AI opponent might be chosen depending on the user’s success history in the given game, with the goal of making the game appropriately challenging. This choice of AI opponent changes players’ future success profiles, again causing a distribution shift in the features serving as an input to the prediction system.

Gaming the system falls under the umbrella of strategic classification, which we discuss in detail in Section 5, so we avoid further discussion in this section.

## Appendix B Experiments

### B.1 Visualizing the performative risk and trajectory of RRM

(a) ε=25\varepsilon=25

(b) ε=100\varepsilon=100

Figure 4: Performative risk surface and trajectory of repeated risk minimization for two different values of sensitivity parameter ε\varepsilon. The initial iterate is the risk minimizer on the base dataset (∙\color[rgb]{1,0,0}\bullet). We mark the performative optimum (⋆\color[rgb]{1,0,0}\star) and performatively stable point (×\color[rgb]{0.71,0.65,0.26}\bm{\times}).

We provide additional experimental results in which we visualize the trajectory of repeated risk minimization on the surface of the performative risk. We adopt the general setting of Section 5. However, to properly visualize the loss, we rerun the experiments on a reduced version of the dataset with only two features (i.e x∈R2x\in\mathbb{R}^{2}), both of which are adapted strategically according to the update described in Section 5.

Figure 4 plots the performative risk surface, together with the trajectory of RRM given by straight black lines. The top plot shows the trajectory for a suitably small sensitivity parameter ε\varepsilon. We see that RRM converges to a stable point which is close to the performative optimum.
We contrast this behavior with that of RRM when ε\varepsilon is large in the bottom plot. Here, we observe that the iterates oscillate and that the algorithm fails to converge.
Both plots mark the risk minimizer on the initial data set (∙\color[rgb]{1,0,0}\bullet), before any strategic adaptation takes place. This point also corresponds to the initial iterate of RRM θ0\theta_{0}. We additionally mark the performative optimum (⋆\color[rgb]{1,0,0}\star) on the risk curve. The top plot additionally marks the last iterate of RRM, which serves as a proxy for the performatively stable point (×\color[rgb]{0.71,0.65,0.26}\bm{\times}). As predicted by our theory, this stable point is in a small neighborhood around the performative optimum.

### B.2 Experimental details

#### Base distribution.

The base distribution consists of the Kaggle data set [22]. We subsample n=18,357n=18,357 points from the original training set such that both classes are approximately balanced (45% of points have yy equal to 1). There are a total of 10 features, 3 of which we treat as strategic features: utilization of credit lines, number of open credit lines, and number of real estate loans. We scale features in the base distribution so that they have zero mean and unit variance.

#### Verifying ε\varepsilon-sensitivity.

We verify that the map 𝒟⁡(⋅)\mathcal{D}(\cdot), as described in Section 5, is ε\varepsilon-sensitive. To do so, we analyze W1​(𝒟⁡(θ),𝒟⁡(θ′))W_{1}(\mathcal{D}(\theta),\mathcal{D}(\theta^{\prime})), for arbitrary θ,θ′∈�\theta,\theta^{\prime}\in\Theta. Fix a sample point x∈Rm−1x\in\mathbb{R}^{m-1} from the base dataset. Because the base distribution 𝒟\mathcal{D} is supported on nn points, we can upper bound the optimal transport distance between any pair of distributions 𝒟⁡(θ)\mathcal{D}(\theta) and 𝒟⁡(θ′)\mathcal{D}(\theta^{\prime}) by the Euclidean distance between the shifted versions of xx in 𝒟⁡(θ)\mathcal{D}(\theta) and 𝒟⁡(θ′)\mathcal{D}(\theta^{\prime}).

In our construction, the point xx is shifted to x−ε​θx-\varepsilon\theta and to x−ε​θ′x-\varepsilon\theta^{\prime} in 𝒟⁡(θ)\mathcal{D}(\theta) and 𝒟⁡(θ′)\mathcal{D}(\theta^{\prime}) respectively. The distance between these two shifted points is ‖x−ε​θ−x+ε​θ′‖2=ε​‖θ−θ′‖2\|x-\varepsilon\theta-x+\varepsilon\theta^{\prime}\|_{2}=\varepsilon\|\theta-\theta^{\prime}\|_{2}. Since the same relationship holds for all other samples xx in the base dataset, the optimal transport from 𝒟⁡(θ)\mathcal{D}(\theta) to 𝒟⁡(θ′)\mathcal{D}(\theta^{\prime}) is at most ε​‖θ−θ′‖2\varepsilon\|\theta-\theta^{\prime}\|_{2}.

#### Verifying joint smoothness of the objective.

For the experiments described in Figure 2, we run repeated risk minimization and repeated gradient descent on the logistic loss with ℓ2\ell_{2} regularization:

|
| 1n∑i=1n−yiθ⊤xi+log(1+exp(θ⊤xi))+γ2∥θ∥22\frac{1}{n}\sumop\displaylimits_{i=1}^{n}-y_{i}\theta^{\top}x_{i}+\log\big(1+\exp(\theta^{\top}x_{i})\big)+\frac{\gamma}{2}\lVert\theta\rVert_{2}^{2}
|
| (1)

For both the repeated risk minimization and repeated gradient descent we set γ=1000/n\gamma=1000/n, where nn is the size of the base dataset.

For a particular feature-outcome pair (xi,yi)(x_{i},y_{i}), the logistic loss is 14​∥xi∥22\frac{1}{4}\lVert x_{i}\rVert_{2}^{2} smooth [36]. Therefore, the entire objective is 14​n​∑i=1n∥xi∥22+γ\frac{1}{4n}\sumop\displaylimits_{i=1}^{n}\lVert x_{i}\rVert_{2}^{2}+\gamma smooth. Due to the strategic updates, xB​R=x−ε​θx_{BR}=x-\varepsilon\theta, the norm of individual features change depending on the choice of model parameters.

Theoretically, we can upper bound the smoothness of the objective by finding the implicit constraints on �\Theta, which can be revealed by looking at the dual of the objective function for every fixed value of ε\varepsilon. However, for simplicity, we simply calculate the worst-case smoothness of the objective, given the trajectory of iterates {θt}\{\theta_{t}\}, for every fixed ε\varepsilon.

Furthermore, we can verify the logistic loss is jointly smooth. For a fixed example z=(x,y)z=(x,y), the gradient of the regularized logistic loss with respect to θ\theta is,

|
| ∇θℓ​(z,θ)=y​x+exp⁡(θ⊤​x)1+exp⁡(θ⊤​x)​x+γ​θ,\nabla_{\theta}\ell(z;\theta)=yx+\frac{\exp(\theta^{\top}x)}{1+\exp(\theta^{\top}x)}x+\gamma\theta,
|

which is 2-Lipschitz in zz due to y∈{0,1}y\in\{0,1\}. Hence, the overall objective is β\beta-jointly smooth with parameter

|
| β=max⁡{2,14​n​∑i=1n∥xi∥22+γ}.\beta=\max\big\{2,\frac{1}{4n}\sumop\displaylimits_{i=1}^{n}\lVert x_{i}\rVert_{2}^{2}+\gamma\big\}.
|

For RRM, ε\varepsilon is less than γβ\frac{\gamma}{\beta} only in the case that ε=0.01\varepsilon=0.01. For RGD, ε\varepsilon is never smaller than the theoretical cutoff of γ(β+γ)​(1+1.5​η​β)\frac{\gamma}{(\beta+\gamma)(1+1.5\eta\beta)}.

#### Optimization details.

The definition of RRM requires exact minimization of the objective at every iteration. We approximate this requirement by minimizing the objective described in expression (1) to small tolerance, 10−810^{-8}, using gradient descent. We choose the step size at every iteration using backtracking line search.

In the case of repeated gradient descent, we run the procedure as described in Definition 3.7 with a fixed step size of η=2β+γ\eta=\frac{2}{\beta+\gamma}.

## Appendix C Auxiliary lemmas

###### Lemma C.1 (First-order optimality condition).

Let ff be convex and let
\Omega be a closed convex set on which ff is differentiable, then

|
| x∗∈arg​minx∈
f(x)x_{*}\in\argmin_{x\in\Omega}f(x)
|

if and only if

|
| ∇f(x∗)T(y−x∗)>0,∀y∈
.\nabla f(x_{*})^{T}(y-x_{*})\geqslant 0,\quad\forall y\in\Omega.
|

###### Lemma C.2 (Bubeck, 2015 [9], Lemma 3.11).

Let f:Rd→Rf:\mathbb{R}^{d}\rightarrow\mathbb{R} be β\beta-smooth and γ\gamma-strongly convex, then for all x,yx,y in Rd\mathbb{R}^{d},

|
| (∇f​(x)−∇f​(y))⊤​(x−y)>γ​βγ+β​∥x−y∥22+1γ+β​∥∇f​(x)−∇f​(y)∥22.(\nabla f(x)-\nabla f(y))^{\top}(x-y)\geqslant\frac{\gamma\beta}{\gamma+\beta}\lVert x-y\rVert_{2}^{2}+\frac{1}{\gamma+\beta}\lVert\nabla f(x)-\nabla f(y)\rVert_{2}^{2}.
|

###### Lemma C.3 (Kantorovich-Rubinstein).

A distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive if and only if for all θ,θ′∈�\theta,\theta^{\prime}\in\Theta:

|
| sup{|EZ∼𝒟⁡(θ)g(Z)−EZ∼𝒟⁡(θ′)g(Z)|6ε∥θ−θ′∥2:g:Rp→R,g 1-Lipschitz}.\sup\left\{\Big|~\E_{Z\sim\mathcal{D}(\theta)}g(Z)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}g(Z)~\Big|\leqslant\varepsilon\|\theta-\theta^{\prime}\|_{2}~:~g:\mathbb{R}^{p}\rightarrow\mathbb{R},~g\text{ 1-Lipschitz}\right\}.
|

###### Lemma C.4.

Let f:Rn→Rdf:\mathbb{R}^{n}\rightarrow\mathbb{R}^{d} be an LL-Lipschitz function, and let X,X′∈RnX,X^{\prime}\in\mathbb{R}^{n} be random variables such that W1​(X,X′)6CW_{1}(X,X^{\prime})\leqslant C. Then

|
| ‖E[f⁡(X)]−E[f⁡(X′)]‖26LC.\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}\leqslant LC.
|

###### Proof.

|
| ‖E[f⁡(X)]−E[f⁡(X′)]‖22\displaystyle\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}^{2}
| =(E[f⁡(X)]−E[f⁡(X′)])⊤​(E[f⁡(X)]−E[f⁡(X′)])\displaystyle=(\E[f(X)]-\E[f(X^{\prime})])^{\top}(\E[f(X)]-\E[f(X^{\prime})])
|

|
|
| =‖E[f⁡(X)]−E[f⁡(X′)]‖2​(E[f⁡(X)]−E[f⁡(X′)])⊤‖E[f⁡(X)]−E[f⁡(X′)]‖2​(E[f⁡(X)]−E[f⁡(X′)]).\displaystyle=\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}\frac{(\E[f(X)]-\E[f(X^{\prime})])^{\top}}{\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}}(\E[f(X)]-\E[f(X^{\prime})]).
|

Now define the unit vector v:=E[f⁡(X)]−E[f⁡(X′)]‖E[f⁡(X)]−E[f⁡(X′)]‖2v:=\frac{\E[f(X)]-\E[f(X^{\prime})]}{\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}}. By linearity of expectation, we can further write

|
| ‖E[f⁡(X)]−E[f⁡(X′)]‖22=‖E[f⁡(X)]−E[f⁡(X′)]‖2​(E[v⊤​f​(X)]−E[v⊤​f​(X′)]).\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}^{2}=\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}~(\E[v^{\top}f(X)]-\E[v^{\top}f(X^{\prime})]).
|

For any unit vector vv and LL-Lipschitz function ff, v⊤​fv^{\top}f is a one-dimensional LL-Lipschitz function, so we can apply Lemma C.3 to obtain

|
| ‖E[f⁡(X)]−E[f⁡(X′)]‖226‖E[f⁡(X)]−E[f⁡(X′)]‖2​LC.\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}^{2}\leqslant\|\E[f(X)]-\E[f(X^{\prime})]\|_{2}LC.
|

Canceling out ‖E[f⁡(X)]−E[f⁡(X′)]‖2\|\E[f(X)]-\E[f(X^{\prime})]\|_{2} from both sides concludes the proof.
∎

## Appendix D Proofs of main results

### D.1 Proof of Theorem 3.5

Fix θ,θ′∈�\theta,\theta^{\prime}\in\Theta. Let f⁡(φ)=EZ∼𝒟⁡(θ)ℓ​(Z,φ)f(\varphi)=\E_{Z\sim\mathcal{D}(\theta)}\ell(Z;\varphi) and f′​(φ)=EZ∼𝒟⁡(θ′)ℓ​(Z,φ)f^{\prime}(\varphi)=\E_{Z\sim\mathcal{D}(\theta^{\prime})}\ell(Z;\varphi). Since ff is γ\gamma-strongly convex and G⁡(θ)G(\theta) is the unique minimizer of f⁡(x)f(x) we know that,

|
| f⁡(G⁡(θ))−f⁡(G⁡(θ′))\displaystyle f(G(\theta))-f(G(\theta^{\prime}))
| >(G(θ)−G(θ′))⊤∇f(G(θ′))+γ2∥G(θ)−G(θ′)∥22\displaystyle\geqslant\left(G(\theta)-G(\theta^{\prime})\right)^{\top}\nabla f(G(\theta^{\prime}))+\frac{\gamma}{2}\|G(\theta)-G(\theta^{\prime})\|_{2}^{2}
|
| (2)

|
| f⁡(G⁡(θ′))−f⁡(G⁡(θ))\displaystyle f(G(\theta^{\prime}))-f(G(\theta))
| >γ2​‖G⁡(θ)−G⁡(θ′)‖22\displaystyle\geqslant\frac{\gamma}{2}\|G(\theta)-G(\theta^{\prime})\|_{2}^{2}
|
| (3)

Together, these two inequalities imply that

|
| −γ∥G(θ)−G(θ′)∥22>(G(θ)−G(θ′))⊤∇f(G(θ′)).-\gamma\|G(\theta)-G(\theta^{\prime})\|_{2}^{2}\geqslant\left(G(\theta)-G(\theta^{\prime})\right)^{\top}\nabla f(G(\theta^{\prime})).
|

Next, we observe that (G⁡(θ)−G⁡(θ′))⊤​∇θℓ​(z,G⁡(θ′))(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla_{\theta}\ell(z;G(\theta^{\prime})) is ‖G⁡(θ)−G⁡(θ′)‖2​β\|G(\theta)-G({\theta^{\prime}})\|_{2}\beta-Lipschitz in zz. This follows from applying Cauchy-Schwarz and the fact that the loss is β\beta-jointly smooth. Using the dual formulation of the optimal transport distance (Lemma C.3) and ε\varepsilon-sensitivity of 𝒟⁡(⋅)\mathcal{D}(\cdot),

|
| (G(θ)−G(θ′))⊤∇f(G(θ′))−(G(θ)−G(θ′))⊤∇f′(G(θ′))>−εβ∥G(θ)−G(θ′)∥2∥θ−θ′∥2.(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla f(G(\theta^{\prime}))-(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla f^{\prime}(G(\theta^{\prime}))\geqslant-\varepsilon\beta\|G(\theta)-G({\theta^{\prime}})\|_{2}\|\theta-\theta^{\prime}\|_{2}.
|

Furthermore, using the first-order optimality conditions for convex functions, we have (G(θ)−G(θ′))⊤∇f′(G(θ′))>0(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla f^{\prime}(G(\theta^{\prime}))\geqslant 0, and hence (G(θ)−G(θ′))⊤∇f(G(θ′))>−εβ∥G(θ)−G(θ′)∥2∥θ−θ′∥2.(G(\theta)-G({\theta^{\prime}}))^{\top}\nabla f(G(\theta^{\prime}))\geqslant-\varepsilon\beta\|G(\theta)-G({\theta^{\prime}})\|_{2}\|\theta-\theta^{\prime}\|_{2}. Therefore, we conclude that,

|
| −γ​‖G⁡(θ)−G⁡(θ′)‖22>−ε​β​‖G⁡(θ)−G⁡(θ′)‖2​‖θ−θ′‖2.-\gamma\|G(\theta)-G(\theta^{\prime})\|_{2}^{2}\geqslant-\varepsilon\beta\|G(\theta)-G({\theta^{\prime}})\|_{2}\|\theta-\theta^{\prime}\|_{2}.
|

Claim (a) then follows by rearranging.

To prove claim (b) we note that θt=G⁡(θt−1)\theta_{t}=G({\theta_{t-1}}) by the definition of RRM, and G⁡(θPS)=θPSG({{\theta_{\mathrm{PS}}}})={\theta_{\mathrm{PS}}} by the definition of stability. Applying the result of part (a) yields

|
| ‖θt−θPS‖26ε​βγ​‖θt−1−θPS‖26(ε​βγ)t​‖θ0−θPS‖2.\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\varepsilon\frac{\beta}{\gamma}\|\theta_{t-1}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\left(\varepsilon\frac{\beta}{\gamma}\right)^{t}\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}.
|
| (4)

Setting this expression to be at most δ\delta and solving for tt completes the proof of claim (b).

### D.2 Proof of Proposition 3.6

As for statement (a), we provide one counterexample for each of the statements (b) and (c).

#### Proof of (b):

Consider a type of regularized hinge loss ℓ⁡(z,θ)=C​max⁡(−1,y​θ)+γ2​(θ−1)2\ell(z;\theta)=C\max(-1,y\theta)+\frac{\gamma}{2}(\theta-1)^{2}, and suppose �⊇[−12​ε,12​ε]\Theta\supseteq[-\frac{1}{2\varepsilon},\frac{1}{2\varepsilon}].

Let the distribution of YY according to 𝒟⁡(θ)\mathcal{D}(\theta) be a point mass at ε​θ\varepsilon\theta, and let the distribution of XX be invariant with respect to θ\theta. Clearly, this distribution is ε\varepsilon-sensitive.

Let θ0=2\theta_{0}=2. Then, by picking CC big enough, RRM prioritizes to minimize the first term exactly, and hence we get θ1=−12​ε\theta_{1}=-\frac{1}{2\varepsilon}. In the next step, again due to large CC, we get θ2=2\theta_{2}=2. Thus, RRM keeps oscillating between 22 and −12​ε-\frac{1}{2\varepsilon}, failing to converge. This argument holds for all γ,ε>0\gamma,\varepsilon>0.

#### Proof of (c):

Suppose that the loss function is the squared loss, ℓ⁡(z,θ)=(y−θ)2\ell(z;\theta)=(y-\theta)^{2}, where y,θ∈Ry,\theta\in\mathbb{R}. Note that this implies β=γ\beta=\gamma. Let the distribution of YY according to 𝒟⁡(θ)\mathcal{D}(\theta) be a point mass at 1+ε​θ1+\varepsilon\theta, and let the distribution of XX be invariant with respect to θ\theta. This distribution family satisfies ε\varepsilon-sensitivity, because

|
| W1​(𝒟⁡(θ),𝒟⁡(θ′))=ε​|θ−θ′|.W_{1}(\mathcal{D}(\theta),\mathcal{D}(\theta^{\prime}))=\varepsilon|\theta-\theta^{\prime}|.
|

By properties of the squared loss, we know

|
| arg​minθ′⁡DPR​(θ,θ′)=EZ∼𝒟⁡(θ)[Y]=1+ε​θ.\argmin_{\theta^{\prime}}{\mathrm{DPR}}(\theta,\theta^{\prime})=\E_{Z\sim\mathcal{D}(\theta)}\left[Y\right]=1+\varepsilon\theta.
|

It is thus not hard to see that RRM does not contract if ε>γβ=1\varepsilon\geqslant\frac{\gamma}{\beta}=1:

|
| |G⁡(θ)−G⁡(θ′)|=|1+ε​θ−1−ε​θ′|=ε​|θ−θ′|,|G(\theta)-G(\theta^{\prime})|=\left|1+\varepsilon\theta-1-\varepsilon\theta^{\prime}\right|=\varepsilon|\theta-\theta^{\prime}|,
|

which exactly matches the bound of Theorem 3.5 and proves the first statement of the proposition. The unique performatively stable point of this problem is θ\theta such that θ=1+ε​θ\theta=1+\varepsilon\theta, which is θPS=11−ε{\theta_{\mathrm{PS}}}=\frac{1}{1-\varepsilon} for ε>1\varepsilon>1.

For ε=1\varepsilon=1, no performatively stable point exists, thereby proving the second claim of the proposition. If ε>1\varepsilon>1 on the other hand, and θ0,θPS\theta_{0}\neq{\theta_{\mathrm{PS}}}, we either have θt→∞\theta_{t}\rightarrow\infty or θt→−∞\theta_{t}\rightarrow-\infty, because

|
| θt=1+ε​θt−1=∑k=0t−1εk+θ0​εt=εt−1ε−1+θ0​εt,\theta_{t}=1+\varepsilon\theta_{t-1}=\sumop\displaylimits_{k=0}^{t-1}\varepsilon^{k}+\theta_{0}\varepsilon^{t}=\frac{\varepsilon^{t}-1}{\varepsilon-1}+\theta_{0}\varepsilon^{t},
|

thus concluding the proof.

### D.3 Proof of Theorem 3.8

Since projecting onto a convex set can only bring two iterates closer together, in this proof we ignore the projection operator ��\Pi_{\Theta} and treat GgdG_{\text{gd}} as performing merely the gradient step.

We begin by expanding out ∥Ggd​(θ)−Ggd​(θ′)∥22\lVert G_{\text{gd}}(\theta)-G_{\text{gd}}({\theta^{\prime}})\rVert_{2}^{2},

|
| ∥Ggd​(θ)−Ggd​(θ′)∥22\displaystyle\lVert G_{\text{gd}}(\theta)-G_{\text{gd}}({\theta^{\prime}})\rVert_{2}^{2}
| =‖θ−η​EZ∼𝒟⁡(θ)​∇θℓ​(Z,θ)−θ′+η​EZ∼𝒟⁡(θ′)​∇θℓ​(Z,θ′)‖22\displaystyle=\left\|\theta-\eta\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\theta^{\prime}+\eta\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}^{2}
|

|
|
| =∥θ−θ′∥22−2​η​(θ−θ′)⊤​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle=\lVert\theta-\theta^{\prime}\rVert_{2}^{2}-2\eta(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
|
| +η2​‖EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖22\displaystyle\quad+\eta^{2}\left\|\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}^{2}
|

|
|
| =defT1−2​η​T2+η2​T3.\displaystyle\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}T_{1}-2\eta T_{2}+\eta^{2}T_{3}.
|

Next, we analyze each term individually,

|
| T1\displaystyle T_{1}
| =def∥θ−θ′∥22,\displaystyle\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\lVert\theta-\theta^{\prime}\rVert_{2}^{2},
|

|
| T2\displaystyle T_{2}
| =def(θ−θ′)⊤​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)),\displaystyle\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right),
|

|
| T3\displaystyle T_{3}
| =def∥EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)∥22.\displaystyle\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\lVert\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\rVert_{2}^{2}.
|

We start by lower bounding T2T_{2}:

|
| T2\displaystyle T_{2}
| =(θ−θ′)⊤​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)+EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle=(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)+\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
|
| =(θ−θ′)⊤​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ))+(θ−θ′)⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle=(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right)+(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
|
| >−‖θ−θ′‖2​‖EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)‖2+(θ−θ′)⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)),\displaystyle\geqslant-\|\theta-\theta^{\prime}\|_{2}~\|\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\|_{2}+(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right),
|

where in the last step we apply the Cauchy-Schwarz inequality.
By smoothness, ∇θℓ​(Z,θ)\nabla_{\theta}\ell(Z;\theta) is β\beta-Lipschitz in ZZ. Together with the fact that ZZ is ε\varepsilon-sensitive, we can lower bound the first term in the above expression by applying Lemma C.4, which results in −β​ε​∥θ−θ′∥22-\beta\varepsilon\lVert\theta-\theta^{\prime}\rVert_{2}^{2}.

We apply Lemma C.2 to lower bound the second term by

|
|
| (θ−θ′)⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle(\theta-\theta^{\prime})^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
| >\displaystyle\geqslant~
| β​γβ+γ​∥θ−θ′∥22+1β+γ​EZ∼𝒟⁡(θ′)[∥∇θℓ​(Z,θ)−∇θℓ​(Z,θ′)∥22]\displaystyle\frac{\beta\gamma}{\beta+\gamma}\lVert\theta-\theta^{\prime}\rVert_{2}^{2}+\frac{1}{\beta+\gamma}\E_{Z\sim\mathcal{D}(\theta^{\prime})}\left[\lVert\nabla_{\theta}\ell(Z;\theta)-\nabla_{\theta}\ell(Z;\theta^{\prime})\rVert_{2}^{2}\right]
|

|
| >\displaystyle\geqslant~
| β​γβ+γ​∥θ−θ′∥22+1β+γ​‖EZ∼𝒟⁡(θ′)[∇θℓ​(Z,θ)−∇θℓ​(Z,θ′)]‖22,\displaystyle\frac{\beta\gamma}{\beta+\gamma}\lVert\theta-\theta^{\prime}\rVert_{2}^{2}+\frac{1}{\beta+\gamma}\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\left[\nabla_{\theta}\ell(Z;\theta)-\nabla_{\theta}\ell(Z;\theta^{\prime})\right]\right\|_{2}^{2},
|

where we have applied Jensen’s inequality in the last line. Putting everything together, we get

|
| T2>(β​γβ+γ−β​ε)​∥θ−θ′∥22+1β+γ​‖EZ∼𝒟⁡(θ′)[∇θℓ​(Z,θ)−∇θℓ​(Z,θ′)]‖22.T_{2}\geqslant\left(\frac{\beta\gamma}{\beta+\gamma}-\beta\varepsilon\right)\lVert\theta-\theta^{\prime}\rVert_{2}^{2}+\frac{1}{\beta+\gamma}\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\left[\nabla_{\theta}\ell(Z;\theta)-\nabla_{\theta}\ell(Z;\theta^{\prime})\right]\right\|_{2}^{2}.
|

Now we upper bound T3T_{3}. We begin by expanding out the square just as before,

|
| T3=‖EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)+EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖2=‖EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)‖22+‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖22+2​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ))⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)).\displaystyle\begin{split}T_{3}&=\left\|\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)+\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|^{2}\\
&=\left\|\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right\|_{2}^{2}+\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}^{2}\\
&\quad+2\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right)^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right).\end{split}
|
| (5)

We again bound each term individually. By the smoothness of the loss and Lemma C.4,

|
| ‖EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)‖226β2​ε2​‖θ−θ′‖22.\left\|\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right\|_{2}^{2}\leqslant\beta^{2}\varepsilon^{2}\|\theta-\theta^{\prime}\|_{2}^{2}.
|

Moving on to the last term in (5):

|
|
| 2​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ))⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle 2\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right)^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
| =def\displaystyle\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}~
| 2​‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖2​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ))⊤​v\displaystyle 2\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right)^{\top}v
|

|
| =\displaystyle=~
| 2​‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖2​(EZ∼𝒟⁡(θ)v⊤​∇θℓ​(Z,θ)−EZ∼𝒟⁡(θ′)v⊤​∇θℓ​(Z,θ)),\displaystyle 2\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}\left(\E_{Z\sim\mathcal{D}(\theta)}v^{\top}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}v^{\top}\nabla_{\theta}\ell(Z;\theta)\right),
|

where we define the unit vector v=defEZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)∥EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)∥2v\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\frac{\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})}{\lVert\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\rVert_{2}}. By smoothness of the loss, we can conclude that v⊤​∇θℓ​(Z,θ)v^{\top}\nabla_{\theta}\ell(Z,\theta) is β\beta-Lipschitz, so by ε\varepsilon-sensitivity we get

|
|
| 2​(EZ∼𝒟⁡(θ)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ))⊤​(EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′))\displaystyle 2\left(\E_{Z\sim\mathcal{D}(\theta)}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)\right)^{\top}\left(\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right)
|

|
| 6\displaystyle\leqslant~
| 2​‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖2​β​ε​‖θ−θ′‖2\displaystyle 2\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}\beta\varepsilon\|\theta-\theta^{\prime}\|_{2}
|

|
| 6\displaystyle\leqslant~
| 2​β2​ε​∥θ−θ′∥22,\displaystyle 2\beta^{2}\varepsilon\lVert\theta-\theta^{\prime}\rVert_{2}^{2},
|

where in the last step we again apply smoothness. Hence,

|
| T36(ε2​β2+2​β2​ε)​‖θ−θ′‖22+‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖22.T_{3}\leqslant(\varepsilon^{2}\beta^{2}+2\beta^{2}\varepsilon)\left\|\theta-\theta^{\prime}\right\|_{2}^{2}+\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}^{2}.
|

Having bounded all the terms, we now conclude that

|
| ‖Ggd​(θ)−Ggd​(θ′)‖22\displaystyle\left\|G_{\text{gd}}(\theta)-G_{\text{gd}}({\theta^{\prime}})\right\|_{2}^{2}
| 6(1+η2​ε2​β2+2​η2​β2​ε−2​η​β​γβ+γ+2​η​β​ε)​∥θ−θ′∥22\displaystyle\leqslant\left(1+\eta^{2}\varepsilon^{2}\beta^{2}+2\eta^{2}\beta^{2}\varepsilon-2\eta\frac{\beta\gamma}{\beta+\gamma}+2\eta\beta\varepsilon\right)\lVert\theta-\theta^{\prime}\rVert_{2}^{2}
|

|
|
| −(2​ηβ+γ−η2)​‖EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ)−EZ∼𝒟⁡(θ′)∇θ​ℓ​(Z,θ′)‖22.\displaystyle-\left(\frac{2\eta}{\beta+\gamma}-\eta^{2}\right)\left\|\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta)-\E_{Z\sim\mathcal{D}(\theta^{\prime})}\nabla_{\theta}\ell(Z;\theta^{\prime})\right\|_{2}^{2}.
|

If we take the step size η\eta to be small enough, namely η62β+γ\eta\leqslant\frac{2}{\beta+\gamma}, we get

|
| ‖Ggd​(θ)−Ggd​(θ′)‖226(1+η2​ε2​β2+2​η2​β2​ε−2​η​β​γβ+γ+2​η​β​ε)​∥θ−θ′∥22.\left\|G_{\text{gd}}(\theta)-G_{\text{gd}}({\theta^{\prime}})\right\|_{2}^{2}\leqslant\left(1+\eta^{2}\varepsilon^{2}\beta^{2}+2\eta^{2}\beta^{2}\varepsilon-2\eta\frac{\beta\gamma}{\beta+\gamma}+2\eta\beta\varepsilon\right)\lVert\theta-\theta^{\prime}\rVert_{2}^{2}.
|

To ensure a contraction, we need 2​η​β​γβ+γ−η2​ε2​β2−2​η2​β2​ε−2​η​β​ε>02\eta\frac{\beta\gamma}{\beta+\gamma}-\eta^{2}\varepsilon^{2}\beta^{2}-2\eta^{2}\beta^{2}\varepsilon-2\eta\beta\varepsilon>0. Canceling out η​β\eta\beta, and assuming ε61\varepsilon\leqslant 1, it suffices to have 2​γβ+γ−3​η​ε​β−2​ε>0\frac{2\gamma}{\beta+\gamma}-3\eta\varepsilon\beta-2\varepsilon>0.
Therefore, if ε<γ(β+γ)​(1+1.5​η​β)61\varepsilon<\frac{\gamma}{(\beta+\gamma)(1+1.5\eta\beta)}\leqslant 1, the map GgdG_{\text{gd}} is contractive. In particular, we have

|
| ‖Ggd​(θ)−Ggd​(θ′)‖2\displaystyle\left\|G_{\text{gd}}(\theta)-G_{\text{gd}}({\theta^{\prime}})\right\|_{2}
| 6(1−η​(2​β​γβ+γ−ε​(3​η​β2+2​β)))​∥θ−θ′∥2\displaystyle\leqslant\sqrt{\left(1-\eta\left(2\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(3\eta\beta^{2}+2\beta)\right)\right)}\lVert\theta-\theta^{\prime}\rVert_{2}
|

|
|
| 6(1−η​(β​γβ+γ−ε​(1.5​η​β2+β)))​∥θ−θ′∥2,\displaystyle\leqslant\left(1-\eta\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(1.5\eta\beta^{2}+\beta)\right)\right)\lVert\theta-\theta^{\prime}\rVert_{2},
|

where we use the fact that 1−x61−x2\sqrt{1-x}\leqslant 1-\frac{x}{2} for x∈[0,1]x\in[0,1]. This completes the proof of part (a).

Since we have shown GgdG_{\text{gd}} is contractive, by the Banach fixed-point theorem we know that there exists a unique fixed point of GgdG_{\text{gd}}. That is, there exists θPS{\theta_{\mathrm{PS}}} such that EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,θPS)=0\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\nabla_{\theta}\ell(Z;{\theta_{\mathrm{PS}}})=0. By convexity of the loss function, this means that θPS{\theta_{\mathrm{PS}}} is the optimum of EZ∼𝒟⁡(θPS)ℓ​(Z,θ)\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\ell(Z;\theta) over θ\theta, which in turn implies that θPS{\theta_{\mathrm{PS}}} is performatively stable. Recursively applying the result of part (a) we get the rate of convergence of RRM to θPS{\theta_{\mathrm{PS}}}:

|
| ‖θt−θPS‖2\displaystyle\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}
| 6(1−η​(β​γβ+γ−ε​(1.5​η​β2+β)))t​‖θ0−θPS‖2\displaystyle\leqslant\left(1-\eta\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(1.5\eta\beta^{2}+\beta)\right)\right)^{t}\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}
|

|
|
| 6exp⁡(−t​η​(β​γβ+γ−ε​(1.5​η​β2+β)))​‖θ0−θPS‖2,\displaystyle\leqslant\exp\left(-t\eta\left(\frac{\beta\gamma}{\beta+\gamma}-\varepsilon(1.5\eta\beta^{2}+\beta)\right)\right)\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2},
|

where in the last step we use the fact that 1−x6e−x1-x\leqslant e^{-x}. Setting this expression to be at most δ\delta and solving for tt completes the proof.

### D.4 Proof of Theorem 3.10

#### Proof of (a):

We introduce the main proof idea and then present the full argument. The proof proceeds by case analysis. First, we show that if ‖θt−θPS‖2>δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}>\delta, performing ERM ensures that with high probability ‖θt+1−θPS‖262​ε​βγ​‖θt−θPS‖2\|\theta_{t+1}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant 2\varepsilon\frac{\beta}{\gamma}\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}. Using our assumption that ε<γ2​β\varepsilon<\frac{\gamma}{2\beta}, this implies that the iterate θt+1\theta_{t+1} contracts toward θPS{\theta_{\mathrm{PS}}}.

On the other hand, if ‖θt−θPS‖26δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta, we show that while ERM might not contract, it cannot push θt+1\theta_{t+1} too far from θPS{\theta_{\mathrm{PS}}} either. In particular, θt+1\theta_{t+1} must be in a ε​β2​γ​δ\frac{\varepsilon\beta}{2\gamma}\delta-ball around θPS{\theta_{\mathrm{PS}}}. The proof then concludes by arguing that θt\theta_{t} for t>log⁡(‖θ0−θPS‖2/δ)log⁡(γ/2​ε​β)t\geqslant\frac{\log(\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}/\delta)}{\log(\gamma/2\varepsilon\beta)} must enter a ball of radius δ\delta around θPS{\theta_{\mathrm{PS}}}. Once this event occurs, no future iterate can exit the ε​β2​γ​δ\frac{\varepsilon\beta}{2\gamma}\delta-ball around θPS{\theta_{\mathrm{PS}}}.

Case 1: ‖θt−θPS‖2>δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}>\delta. If the current iterate is outside the ball, we show that with high probability the next iterate contracts towards a performatively stable point. In particular,

|
| ∥θt+1−θPS∥262​ε​βγ​∥θt−θPS∥2.\lVert\theta_{t+1}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant\frac{2\varepsilon\beta}{\gamma}\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2}.
|

To prove this claim, we begin by showing that

|
| W1​(𝒟nt​(θt),𝒟⁡(θPS))62​ε​‖θt−θPS‖2, with probability ​1−6​pπ2​t2.W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant 2\varepsilon\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2},\text{ with probability }1-\frac{6p}{\pi^{2}t^{2}}.
|
| (6)

Since the W1W_{1}-distance is a metric on the space of distributions, we can apply the triangle inequality to get

|
| W1​(𝒟nt​(θt),𝒟⁡(θPS))6W1​(𝒟nt​(θt),𝒟⁡(θt))+W1​(𝒟⁡(θt),𝒟⁡(θPS)).W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}(\theta_{t}))+W_{1}(\mathcal{D}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}})).
|

The second term is bounded deterministically by ε​∥θt−θPS∥2\varepsilon\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2} due to ε\varepsilon-sensitivity. By Theorem 2 of Fournier & Guillin, 2015 [13], for nt>1c2​(ε​δ)m​log⁡(t2​π2​c16​p)n_{t}\geqslant\frac{1}{c_{2}(\varepsilon\delta)^{m}}\log\left(\frac{t^{2}\pi^{2}c_{1}}{6p}\right), the probability that the first term is greater than ε​δ\varepsilon\delta is less that 6​pt2​π2\frac{6p}{t^{2}\pi^{2}}. Here, the positive constants c1,c2c_{1},c_{2} depend on α,μ,ξα,μ\alpha,\mu,\xi_{\alpha,\mu} and mm. Therefore,

|
| W1​(𝒟nt​(θt),𝒟⁡(θPS))6ε​δ+ε​∥θt−θPS∥262​ε​∥θt−θPS∥2, with probability ​1−6​pπ2​t2.W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant\varepsilon\delta+\varepsilon\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant 2\varepsilon\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2},\text{ with probability }1-\frac{6p}{\pi^{2}t^{2}}.
|

Using this, we can now prove that the iterates contract. Following the first steps of the proof of Theorem 3.5, we have that

|
| (Gnt​(θt)−G⁡(θPS))⊤​(EZ∼𝒟nt​(θt)∇θ​ℓ​(Z,Gnt​(θt))−EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,Gnt​(θt)))+(Gnt​(θt)−G⁡(θPS))⊤​(EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,Gnt​(θt))−EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,G⁡(θPS)))60.\displaystyle\begin{split}&\left(G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\right)^{\top}\Big(\E_{Z\sim{\mathcal{D}^{n_{t}}(\theta_{t})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))-\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))\Big)\\
+&\left(G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\right)^{\top}\Big(\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))-\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G({\theta_{\mathrm{PS}}}))\Big)\leqslant 0.\end{split}
|
| (7)

Like in the proof of Theorem 3.5, the term (Gnt​(θt)−G⁡(θPS))⊤​EZ∼𝒟nt​(θt)​∇θℓ​(Z,Gnt​(θt))(G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}}))^{\top}\E_{Z\sim{\mathcal{D}^{n_{t}}(\theta_{t})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t})) is ∥Gnt​(θt)−G⁡(θPS)∥2⋅β\lVert G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\rVert_{2}\cdot\beta Lipschitz in ZZ. Using equation (6), with probability 1−6​pπ2​t21-\frac{6p}{\pi^{2}t^{2}} we can bound the first term by

|
|
| (Gnt​(θt)−G⁡(θPS))⊤​(EZ∼𝒟nt​(θt)∇θ​ℓ​(Z,Gnt​(θt))−EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,Gnt​(θt)))\displaystyle\left(G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\right)^{\top}\Big(\E_{Z\sim{\mathcal{D}^{n_{t}}(\theta_{t})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))-\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))\Big)
|

|
| >\displaystyle\geqslant~
| −2​ε​β​‖Gnt​(θt)−G⁡(θPS)‖2​‖θt−θPS‖2.\displaystyle-2\varepsilon\beta\left\|G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\right\|_{2}\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}.
|

And by strong convexity,

|
|
| (Gnt​(θt)−G⁡(θPS))⊤​(EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,Gnt​(θt))−EZ∼𝒟⁡(θPS)∇θ​ℓ​(Z,G⁡(θPS)))\displaystyle\left(G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\right)^{\top}\Big(\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G^{n_{t}}(\theta_{t}))-\E_{Z\sim{\mathcal{D}({\theta_{\mathrm{PS}}})}}\nabla_{\theta}\ell(Z;G({\theta_{\mathrm{PS}}}))\Big)
|

|
| >\displaystyle\geqslant~
| γ​∥Gnt​(θt)−G⁡(θPS)∥22.\displaystyle\gamma\lVert G^{n_{t}}(\theta_{t})-G({\theta_{\mathrm{PS}}})\rVert_{2}^{2}.
|

Plugging back into equation (7), we conclude that with high probability

|
| ∥θt+1−θPS∥262​ε​βγ​∥θt−θPS∥2.\lVert\theta_{t+1}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant\frac{2\varepsilon\beta}{\gamma}\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2}.
|

Applying a union bound, we conclude that the iterates contract at every iteration where ‖θt−θPS‖2>δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}>\delta with probability at least 1−∑t=1∞6​pπ2​t2=1−p1-\sumop\displaylimits_{t=1}^{\infty}\frac{6p}{\pi^{2}t^{2}}=1-p. Therefore, for t>(1−2​ε​βγ)−1​log⁡(‖θ0−θPS‖2δ)t\geqslant\left(1-\frac{2\varepsilon\beta}{\gamma}\right)^{-1}\log\left(\frac{\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}}{\delta}\right) steps we have

|
| ∥θt−θPS∥26(2​ε​βγ)t​∥θ0−θPS∥26(2​ε​βγ)t​‖θ0−θPS‖26exp⁡(−t⁡(1−2​ε​βγ))​‖θ0−θPS‖26δ,\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant\left(\frac{2\varepsilon\beta}{\gamma}\right)^{t}\lVert\theta_{0}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant\left(\frac{2\varepsilon\beta}{\gamma}\right)^{t}\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\exp\left(-t\left(1-\frac{2\varepsilon\beta}{\gamma}\right)\right)\|\theta_{0}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta,
|

where we use 1−x6e−x1-x\leqslant e^{-x}. This implies that θt\theta_{t} eventually contracts to a ball of radius δ\delta around θPS{\theta_{\mathrm{PS}}}.

Case 2: ‖θt−θPS‖26δ\|\theta_{t}-{\theta_{\mathrm{PS}}}\|_{2}\leqslant\delta. We show that the RERM iterates can leave a ball of radius δ\delta around θPS{\theta_{\mathrm{PS}}} only with negligible probability. We begin by applying the triangle inequality just as we did in the previous case,

|
| W1​(𝒟nt​(θt),𝒟⁡(θPS))6W1​(𝒟nt​(θt),𝒟⁡(θt))+W1​(𝒟⁡(θt),𝒟⁡(θPS))6W1​(𝒟nt​(θt),𝒟⁡(θt))+ε​δ.W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}(\theta_{t}))+W_{1}(\mathcal{D}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}(\theta_{t}))+\varepsilon\delta.
|

For our choice of ntn_{t}, with probability at least 1−6​pπ2​t21-\frac{6p}{\pi^{2}t^{2}} this quantity is upper bounded by

|
| W1​(𝒟nt​(θt),𝒟⁡(θPS))62​ε​δ.W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant 2\varepsilon\delta.
|

With this information, we can now apply the exact same steps as in the previous case, but now using the fact that W1​(𝒟nt​(θt),𝒟⁡(θPS))62​ε​δW_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant 2\varepsilon\delta instead of W1​(𝒟nt​(θt),𝒟⁡(θPS))62​ε​∥θt−θPS∥2W_{1}(\mathcal{D}^{n_{t}}(\theta_{t}),\mathcal{D}({\theta_{\mathrm{PS}}}))\leqslant 2\varepsilon\lVert\theta_{t}-{\theta_{\mathrm{PS}}}\rVert_{2}, to conclude that with probability at least 1−6​pπ2​t21-\frac{6p}{\pi^{2}t^{2}}

|
| ∥θt+1−θPS∥262​ε​βγ​δ6δ.\lVert\theta_{t+1}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant 2\varepsilon\frac{\beta}{\gamma}\delta\leqslant\delta.
|

As before, a union bound argument proves that the entire analysis holds with probability 1−p1-p.

#### Proof of (b):

The only difference between part (b) in relation to part (a) is the fact that one needs to invoke the steps of Theorem 3.8 rather than Theorem 3.5.

### D.5 Proof of Proposition 4.1

We begin by defining the set-valued function, g⁡(θ)=arg​minθ′∈�⁡DPR​(θ,θ′)g(\theta)=\argmin_{\theta^{\prime}\in\Theta}{\mathrm{DPR}}(\theta,\theta^{\prime}). Observe that fixed points of this function correspond to models which are performatively stable. The proof thereby follows from showing that the function g⁡(⋅)g(\cdot) has a fixed point.

Since the loss is jointly continuous and the set �\Theta is compact, we can apply Berge’s Maximum Theorem [5, 1] to conclude that the function g⁡(⋅)g(\cdot) is upper hemicontinuous with compact and non-empty values. Furthermore, by convexity of the loss, it follows that in addition to being compact and non-empty, g⁡(θ)g(\theta) is a convex set for every θ∈�\theta\in\Theta. Therefore, the conditions of Kakutani’s Theorem [23] (also see Ch 17. in [1]) hold and we can conclude that g⁡(⋅)g(\cdot) has a fixed point. Hence, a performatively stable model exists.

### D.6 Proof of Proposition 4.2

We make a slight modification to Example 2.2 to prove the proposition. As in the example, 𝒟⁡(θ)\mathcal{D}(\theta) is given as follows: XX is a single feature supported on {±1}\{\pm 1\} and Y|X∼Bernoulli​(12+μ​X+ε​θ​X)Y~|~X\sim\text{Bernoulli}(\frac{1}{2}+\mu X+\varepsilon\theta X), where �=[0,1]\Theta=[0,1]. We let ε>12\varepsilon\geqslant\frac{1}{2}, and constrain μ\mu to satisfy |μ+ε|612\lvert\mu+\varepsilon\rvert\leqslant\frac{1}{2}. We assume that outcomes are predicted according to the model fθ​(x)=θ​x+12f_{\theta}(x)=\theta x+\frac{1}{2} and that performance is measured via the squared loss, ℓ⁡(z,θ)=(y−fθ​(x))2\ell(z;\theta)=(y-f_{\theta}(x))^{2}. This loss has condition number βγ=1\frac{\beta}{\gamma}=1.

A direct calculation demonstrates that the performative risk is a quadratic in θ\theta:

|
| PR⁡(θ)=14−2​θ​μ+(1−2​ε)​θ2.\mathrm{PR}(\theta)=\frac{1}{4}-2\theta\mu+(1-2\varepsilon)\theta^{2}.
|

Therefore, if ε∈[12,1)\varepsilon\in\left[\frac{1}{2},1\right), the performative risk is a concave function of θ\theta, even though ε<γβ\varepsilon<\frac{\gamma}{\beta}.

### D.7 Proof of Theorem 4.3

By definition of performative optimality and performative stability we have that:

|
| DPR⁡(θPO,θPO)6DPR⁡(θPS,θPS)6DPR⁡(θPS,θPO).{\mathrm{DPR}}({\theta_{\mathrm{PO}}},{\theta_{\mathrm{PO}}})\leqslant{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PS}}})\leqslant{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}}).
|

We claim that DPR⁡(θPS,θPO)−DPR⁡(θPS,θPS)>γ2​‖θPO−θPS‖22{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}})-{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PS}}})\geqslant\frac{\gamma}{2}\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}^{2}. By definition of DPR{\mathrm{DPR}}, we can write

|
| DPR⁡(θPS,θPO)−DPR⁡(θPS,θPS)=EZ∼𝒟⁡(θPS)[ℓ⁡(Z,θPO)−ℓ⁡(Z,θPS)].{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}})-{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PS}}})=\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\big[\ell(Z;{\theta_{\mathrm{PO}}})-\ell(Z;{\theta_{\mathrm{PS}}})\big].
|

Since ℓ⁡(z,θPO)>ℓ⁡(z,θPS)+∇θℓ​(z,θPS)⊤​(θPO−θPS)+γ2​‖θPO−θPS‖22\ell(z;{\theta_{\mathrm{PO}}})\geqslant\ell(z;{\theta_{\mathrm{PS}}})+\nabla_{\theta}\ell(z;{\theta_{\mathrm{PS}}})^{\top}({\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}})+\frac{\gamma}{2}\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}^{2} for all zz, we have that

|
| EZ∼𝒟⁡(θPS)[ℓ⁡(Z,θPO)−ℓ⁡(Z,θPS)]>EZ∼𝒟⁡(θPS)[∇θℓ​(Z,θPS)⊤​(θPO−θPS)]+γ2​‖θPO−θPS‖22.\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\big[\ell(Z;{\theta_{\mathrm{PO}}})-\ell(Z;{\theta_{\mathrm{PS}}})\big]\geqslant\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\big[\nabla_{\theta}\ell(Z;{\theta_{\mathrm{PS}}})^{\top}({\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}})\big]+\frac{\gamma}{2}\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}^{2}.
|
| (8)

Now, by Lemma C.1, EZ∼𝒟⁡(θPS)[∇θℓ​(Z,θPS)⊤​(θPO−θPS)]>0\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\big[\nabla_{\theta}\ell(Z;{\theta_{\mathrm{PS}}})^{\top}({\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}})\big]\geqslant 0, so we get that equation (8) implies

|
| EZ∼𝒟⁡(θPS)[ℓ⁡(Z,θPO)−ℓ⁡(Z,θPS)]>γ2​‖θPO−θPS‖22.\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}})}\big[\ell(Z;{\theta_{\mathrm{PO}}})-\ell(Z;{\theta_{\mathrm{PS}}})\big]\geqslant\frac{\gamma}{2}\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}^{2}.
|

Since the population distributions are ε\varepsilon-sensitive and the loss is LzL_{z}-Lipschitz in zz, we have that DPR⁡(θPS,θPO)−DPR⁡(θPO,θPO)6Lz​ε​‖θPO−θPS‖2{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}})-{\mathrm{DPR}}({\theta_{\mathrm{PO}}},{\theta_{\mathrm{PO}}})\leqslant L_{z}\varepsilon\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}. If ε<γ​‖θPO−θPS‖22​Lz\varepsilon<\frac{\gamma\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}}{2L_{z}} then we have that Lz​ε​‖θPO−θPS‖2<γ2​‖θPO−θPS‖22L_{z}\varepsilon\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}<\frac{\gamma}{2}\|{\theta_{\mathrm{PO}}}-{\theta_{\mathrm{PS}}}\|_{2}^{2} which is a contradiction since it must hold that

|
| DPR⁡(θPS,θPO)−DPR⁡(θPO,θPO)>DPR⁡(θPS,θPO)−DPR⁡(θPS,θPS).{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}})-{\mathrm{DPR}}({\theta_{\mathrm{PO}}},{\theta_{\mathrm{PO}}})\geqslant{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PO}}})-{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{PS}}}).
|

### D.8 Proof of Corollary 5.1

By Theorem 3.5 we know that repeated risk minimization converges at a linear rate to a performatively stable point θPS{\theta_{\mathrm{PS}}}. Furthermore, by Theorem 4.3, this performatively stable point is close in domain to the institution’s Stackelberg equilibrium classifier θSE{\theta_{\mathrm{SE}}},

|
| ∥θSE−θPS∥262​Lz​εγ.\lVert{\theta_{\mathrm{SE}}}-{\theta_{\mathrm{PS}}}\rVert_{2}\leqslant\frac{2L_{z}\varepsilon}{\gamma}.
|

We can then use the fact that the loss is Lipschitz to show that this performatively stable classifier is close in objective value to the Stackelberg equilibrium:

|
| PR⁡(θPS)−PR⁡(θSE)\displaystyle\mathrm{PR}({\theta_{\mathrm{PS}}})-\mathrm{PR}({\theta_{\mathrm{SE}}})
| 6|PR⁡(θPS)−DPR⁡(θPS,θSE)|+|DPR⁡(θPS,θSE)−PR⁡(θSE)|\displaystyle\leqslant\big|\mathrm{PR}({\theta_{\mathrm{PS}}})-{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{SE}}})\big|+\big|{\mathrm{DPR}}({\theta_{\mathrm{PS}}},{\theta_{\mathrm{SE}}})-\mathrm{PR}({\theta_{\mathrm{SE}}})\big|
|

|
|
| 6Lθ​∥θSE−θPS∥2+Lz​ε​∥θSE−θPS∥2\displaystyle\leqslant L_{\theta}\lVert{\theta_{\mathrm{SE}}}-{\theta_{\mathrm{PS}}}\rVert_{2}+L_{z}\varepsilon\lVert{\theta_{\mathrm{SE}}}-{\theta_{\mathrm{PS}}}\rVert_{2}
|

|
|
| 62​Lz​ε​(Lθ+Lz​ε)γ\displaystyle\leqslant\frac{2L_{z}\varepsilon(L_{\theta}+L_{z}\varepsilon)}{\gamma}
|

Here, we have used the Kantorovich-Rubinstein Lemma (C.3) to bound the second term.

## Appendix E Approximately minimizing performative risk via regularization

Recall that in Proposition 3.6 we have shown that RRM might not converge at all if the objective is smooth and convex, but not strongly convex. In this section, we show how adding a small amount of quadratic regularization to the objective guarantees that RRM will converge to a stable point which approximately minimizes the performative risk on the original loss.

To do so, we additionally require that the space of model parameters �\Theta be bounded with diameter D=supθ,θ′∈�‖θ−θ′‖2D=\sup_{\theta,\theta^{\prime}\in\Theta}\|\theta-\theta^{\prime}\|_{2}. We can assume without loss of generality that D=1D=1.

###### Proposition E.1.

Suppose that the loss ℓ⁡(z,θ)\ell(z;\theta) is LzL_{z}-Lipschitz iz zz and LθL_{\theta}-Lipschitz in θ\theta, β\beta-jointly smooth (A1) and convex (but not necessarily strongly convex). Furthermore, suppose that distribution map 𝒟⁡(⋅)\mathcal{D}(\cdot) is ε\varepsilon-sensitive with ε<1\varepsilon<1, and that the set �\Theta is bounded with diameter 1. Then, there exists a choice of α\alpha, such that running RRM with loss ℓreg​(z,θ)=defℓ⁡(z,θ)+α2​‖θ−θ0‖22\ell^{\text{reg}}(z;\theta)\stackrel{{\scriptstyle\small\mathrm{def}}}{{=}}\ell(z;\theta)+\frac{\alpha}{2}\|\theta-\theta_{0}\|^{2}_{2} converges to a performatively stable point θPSreg\theta_{\mathrm{PS}}^{\text{reg}} which satisfies the following

|
| PR⁡(θPSreg)6minθ⁡PR⁡(θ)+O⁡(ε1−ε).\mathrm{PR}(\theta_{\mathrm{PS}}^{\text{reg}})\leqslant\min_{\theta}\mathrm{PR}(\theta)+O\left(\frac{\sqrt{\varepsilon}}{1-\varepsilon}\right).
|

We note that in the case where ε=0\varepsilon=0, the limit point θPSreg\theta_{\mathrm{PS}}^{\text{reg}} of regularized repeated risk minimization is also performatively optimal.

###### Proof.

First, we observe that the regularized loss function ℓreg​(z,θ)\ell^{\text{reg}}(z;\theta) is α\alpha-strongly convex and α+β\alpha+\beta-jointly smooth. Since ε<1\varepsilon<1, we can then choose an α\alpha such that ε<αα+β\varepsilon<\frac{\alpha}{\alpha+\beta}. In particular, we choose α=ε​β/(1−ε)\alpha=\sqrt{\varepsilon}\beta/(1-\varepsilon).

From our choice of α\alpha, we have that ε\varepsilon is smaller than the inverse condition number. Hence, by Theorem 3.5 repeated risk minimization converges at a linear rate to a performatively stable solution θPSr​e​g\theta_{\mathrm{PS}}^{reg} of the regularized objective.

To finish the proof, we show that the objective value at the θPSr​e​g\theta_{\mathrm{PS}}^{reg} is close to the objective value at the performative optima of the original objective θPO\theta_{\mathrm{PO}}. We do so by bounding their difference using the triangle inequality:

|
| EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPSreg)−EZ∼𝒟⁡(θPO)ℓ​(Z,θPO)\displaystyle\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PS}}^{\text{reg}})-\E_{Z\sim\mathcal{D}(\theta_{\mathrm{PO}})}\ell(Z;\theta_{\mathrm{PO}})
| =EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPSreg)−EZ∼𝒟⁡(θPOreg)ℓreg​(Z,θPOreg)\displaystyle=\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PS}}^{\text{reg}})-\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})
|

|
|
| +EZ∼𝒟⁡(θPOreg)ℓreg​(Z,θPOreg)−EZ∼𝒟⁡(θPO)ℓ​(Z,θPO)\displaystyle+\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})-\E_{Z\sim\mathcal{D}(\theta_{\mathrm{PO}})}\ell(Z;\theta_{\mathrm{PO}})
|

We can bound the first difference via Lipschitzness:

|
| EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPSreg)−EZ∼𝒟⁡(θPOreg)ℓreg​(Z,θPOreg)\displaystyle\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PS}}^{\text{reg}})-\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})
| =EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPSreg)−EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPOreg)\displaystyle=\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PS}}^{\text{reg}})-\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})
|

|
|
| +EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPOreg)−EZ∼𝒟⁡(θPOreg)ℓreg​(Z,θPOreg)\displaystyle+\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})-\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})
|

|
|
| 6(Lθ+α​supθ,θ′∈�‖θ−θ′‖2)​‖θPSreg−θPOreg‖2\displaystyle\leqslant(L_{\theta}+\alpha\sup_{\theta,\theta^{\prime}\in\Theta}\|\theta-\theta^{\prime}\|_{2})\|\theta_{\mathrm{PS}}^{\text{reg}}-\theta_{\mathrm{PO}}^{\text{reg}}\|_{2}
|

|
|
| +ε​Lz​‖θPSreg−θPOreg‖2\displaystyle+\varepsilon L_{z}\|\theta_{\mathrm{PS}}^{\text{reg}}-\theta_{\mathrm{PO}}^{\text{reg}}\|_{2}
|

|
|
| =(Lθ+α+ε​Lz)​‖θPSreg−θPOreg‖2\displaystyle=(L_{\theta}+\alpha+\varepsilon L_{z})\|\theta_{\mathrm{PS}}^{\text{reg}}-\theta_{\mathrm{PO}}^{\text{reg}}\|_{2}
|

|
|
| 62​(Lθ+α+ε​Lz)​Lz​εα.\displaystyle\leqslant\frac{2(L_{\theta}+\alpha+\varepsilon L_{z})L_{z}\varepsilon}{\alpha}.
|

In the last two lines, we have applied the fact that D=supθ,θ′∈�‖θ−θ′‖2=1D=\sup_{\theta,\theta^{\prime}\in\Theta}\|\theta-\theta^{\prime}\|_{2}=1 as well as Theorem 4.3. For the second difference, by definition of performative optimality we have that,

|
| EZ∼𝒟⁡(θPOreg)ℓreg​(Z,θPOreg)6EZ∼𝒟⁡(θPO)ℓreg​(Z,θPO)6EZ∼𝒟⁡(θPO)ℓ​(Z,θPO)+α2.\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}}^{\text{reg}})\leqslant\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PO}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PO}})\leqslant\E_{Z\sim\mathcal{D}(\theta_{\mathrm{PO}})}\ell(Z;\theta_{\mathrm{PO}})+\frac{\alpha}{2}.
|

Where we have again used the fact that D=1D=1 for the last inequality. Combining these two together, we can bound the total difference:

|
| EZ∼𝒟⁡(θPSreg)ℓreg​(Z,θPSreg)−EZ∼𝒟⁡(θPO)ℓ​(Z,θPO)62​(Lθ+α+ε​Lz)​Lz​εα+α2.\E_{Z\sim\mathcal{D}({\theta_{\mathrm{PS}}^{\text{reg}}})}\ell^{\text{reg}}(Z;\theta_{\mathrm{PS}}^{\text{reg}})-\E_{Z\sim\mathcal{D}(\theta_{\mathrm{PO}})}\ell(Z;\theta_{\mathrm{PO}})\leqslant\frac{2(L_{\theta}+\alpha+\varepsilon L_{z})L_{z}\varepsilon}{\alpha}+\frac{\alpha}{2}.
|

Plugging in α=ε​β1−ε\alpha=\frac{\sqrt{\varepsilon}\beta}{1-\varepsilon} completes the proof.
∎

##

-

<!-- fetch 2: arXiv:2002.06673 | fetch.py none | 2026-11-06T23:17+07:00 | error -->
No readable copy was found. Attempts:

