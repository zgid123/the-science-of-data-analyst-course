---
id: S310
url: https://arxiv.org/pdf/1710.02926
requested: arXiv:1710.02926
fetched: 2026-11-06T23:06+07:00
tool: fetch.py (curl + pdfkit; ladder L2)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T05
part: 3
raw: raw.pdf (514 KB)
conversion: pdfkit of https://arxiv.org/pdf/1710.02926 (readable, 19392 words)
---
<!-- page 1 -->
When Should You Adjust Standard Errors for Clustering?
arXiv:1710.02926v4 [math.ST] 20 Sep 2022
Alberto Abadie Susan Athey
MIT Stanford
Guido W. Imbens Jeffrey M. Wooldridge
Stanford MSU
September 21, 2022
Abstract
Clustered standard errors, with clusters defined by factors such as geography, are
widespread in empirical research in economics and many other disciplines. Formally, clustered standard errors adjust for the correlations induced by sampling
the outcome variable from a data-generating process with unobserved clusterlevel components. However, the standard econometric framework for clustering
leaves important questions unanswered: (i) Why do we adjust standard errors for
clustering in some ways but not others, e.g., by state but not by gender, and in
observational studies, but not in completely randomized experiments? (ii) Why is
conventional clustering an “all-or-nothing” adjustment, while within-cluster correlations can be strong or extremely weak? (iii) In what settings does the choice
of whether and how to cluster make a difference? We address these and other
questions using a novel framework for clustered inference on average treatment
effects. In addition to the common sampling component, the new framework
incorporates a design component that accounts for the variability induced on the
estimator by the treatment assignment mechanism. We show that, when the
number of clusters in the sample is a non-negligible fraction of the number of
clusters in the population, conventional cluster standard errors can be severely
inflated, and propose new variance estimators that correct for this bias.
The questions addressed in this article partly originated in discussions with Gary Chamberlain. We are
grateful for questions raised by Chris Blattman and seminar audiences, and for insightful comments by
Colin Cameron, Vicente Guerra, four reviewers, Larry Katz, and Jesse Shapiro. Jaume Vives-i-Bastida
provided expert research assistance. This work was supported by the Office of Naval Research under grants
N00014-17-1-2131 and N00014-19-1-2468.

<!-- page 2 -->
1. Introduction
Imagine you estimated the effect of attending college on labor earnings using linear regression
on a cross-section of U.S. workers. How should you calculate the standard error? Empirical studies in economics often report heteroskedasticity-robust standard errors (henceforth
“robust”) associated with the work by Eicker [1963], Huber [1967], and White [1980]. A
common alternative is to report cluster-robust standard errors (henceforth “cluster”) associated with the work by Liang and Zeger [1986] and Arellano [1987], with clustering often applied within geographic units such as states or counties. Moulton [1986, 1987] and
Bertrand, Duflo, and Mullainathan [2004] have shown that clustering adjustments can make
a substantial difference, and since the 1980s cluster standard errors have become commonplace in empirical economics.
Later in this section, we estimate a log-linear regression of earnings on an indicator for
some college using data from the 2000 U.S. Census. We find that standard errors clustered at
the state level are more than 20 times larger than robust standard errors. Which ones should
a researcher report? The conventional framework for clustering [see Cameron and Miller,
2015, MacKinnon, Nielsen, and Webb, 2021, for recent reviews] suggests that if the clustering adjustment matters, in the sense that the cluster standard errors are substantially larger
than the robust standard errors, one should use the cluster standard errors. In this article,
we develop a new framework for cluster adjustments to standard errors that nests the conventional framework as a limiting case. The new framework suggests novel standard error
formulas that can substantially improve over robust and cluster standard errors in settings
like the earnings regression described above.
Our proposed clustering framework differs from the standard one in that it includes a
design component that accounts for between-clusters variation in treatment assignments.
We argue that the new design component is important because between-cluster variation
in treatment assignments often motivates the use of clustered standard errors in empirical studies [see, e.g., Gentzkow and Shapiro, 2008, Cohen and Dupas, 2010]. In addition,
our framework shifts the focus of interest from features of infinite super-populations/data-
2

<!-- page 3 -->
generating processes to average treatment effects defined for the finite (but potentially large)
population at hand. As a result of this shift, it is the sampling process and the treatment
assignment mechanism that solely determine the correct level of clustering; the presence
of cluster-level unobserved components of the outcome variable becomes irrelevant for the
choice of clustering level. Moreover, by focusing on finite populations (which could be entirely or substantially sampled in the data) we obtain standard errors smaller than those
aiming to measure uncertainty with respect to features of infinite super-populations. We
derive the large sample variances for the least squares and fixed effect estimators under our
proposed framework and show that they differ in general from both the robust and the cluster variances. We also propose two estimators for the large sample variances, one analytic
and one based on a re-sampling (bootstrap) approach. For the U.S. earnings application,
our proposals produce standard errors that are substantially larger than the robust standard
errors, but also substantially smaller than the conventional version of cluster standard errors.
We use our framework to highlight three common misconceptions surrounding clustering
adjustments. The first misconception is that the need for clustering hinges on the presence
of a non-zero correlation between residuals for units belonging to the same cluster. We show
that the presence of such correlation does not imply the need to use cluster adjustments,
and that the absence of such correlation does not imply that clustering is not required. The
second misconception is that there is no harm in using clustering adjustments when they are
not required, with the implication that if clustering the standard errors makes a difference,
one should do so. To see that both of these claims are in fact incorrect, consider the following
simple example. Suppose that, based on a random sample from the population of interest,
we use the sample average of a variable to estimate its population mean. Suppose also
that the population can be partitioned into clusters such as geographical units. If outcomes
are positively correlated within clusters, the cluster variance will be larger than the robust
variance. However, standard sampling theory directly implies that if the units are sampled
randomly from the population there is no need to cluster. The harm in clustering in this case
is that confidence intervals will be unnecessarily conservative, possibly by a wide margin.
3

<!-- page 4 -->
A third misconception is that researchers have only two choices: either fully adjust for
clustering and use the cluster standard errors, or not adjust the standard errors at all and
use the robust standard errors. We show that a combination of the robust and the cluster
variance estimators can substantially improve accuracy over its two components.
The new clustering framework in this article has the advantage of providing actionable
guidance on a question of substantial consequence for empirical practice in econometrics:
When should standard errors be clustered, and at what level? In the conventional modelbased econometric framework, the researcher takes a stand on the error component structure
of a model for the outcome variable. For example, suppose that, following Moulton [1986,
1987], the researcher posits a random effects model, with random effects at the state level. In
this setting, a repeated sampling thought experiment entails that, for each sample, different
values of the state random effects are drawn from their distributions. This model-based
approach implies that if we are estimating a population mean using a sample average one
needs to cluster the standard errors at the state level even if the sample is a random sample
of individuals and not a clustered sample. A drawback of the model-based econometric
framework for clustering is that empirical researchers need to take a stand on the structure
of the error components of their models.
A second, closely related, framework for clustering that is often invoked in the econometrics literature is motivated by a sampling mechanism that in a first stage selects clusters at
random from an infinite population, followed by a second stage of random sampling of units
from the sampled clusters (or keeping all units in a cluster). Although this framework is
appropriate for some applications in the analyses of surveys, where it originated [Kish, 1995,
Thompson, 2012], we argue that it is not appropriate for many of the data sets economists
and other social scientists analyze. In many applications in economics, researchers do observe units from all the clusters they are interested in, e.g., all the states in the U.S., and
a framework based on randomly sampling a small fraction of a large population of clusters
does not apply.
Neither of the two conventional frameworks for clustered inference described above fully
4

<!-- page 5 -->
incorporates the design aspect of clustering. And it is the lack of a design component that
makes them inappropriate for inference on treatment effects. To gain insight on the importance of the assignment mechanism for the standard errors of treatment effects estimators,
consider a setting with individuals sampled at random from a population, but where treatment is assigned at the cluster level, with the same treatment value for all the individuals in
the same cluster. Assume that the quantity of interest is the population average treatment
effect. Clustered assignment to treatment is equivalent to clustered sampling of potential
outcomes. Because the parameter of interest depends on averages of potential outcomes,
which are sampled in a clustered manner, clustering of the standard errors is required in this
setting, even when the individual observations are sampled at random. Our framework for
clustered inference in this setting is close in spirit to the sampling framework described in
the previous paragraph, but it incorporates a design component.
By shifting the attention from parameters of a data generating process for the outcomes to
the average treatment effect for the population at hand, a researcher applying the proposals
in this article does not need to take a stand on the error component structure of a model
for the outcome variable to calculate standard errors. Instead, all the relevant variability
of the estimator with respect to the average treatment effect is generated by the sampling
mechanism, which extracts the sample from the population, and the assignment mechanism,
which determines which units are exposed to the treatment. We see this as an intrinsic
advantage of the framework proposed in this article in settings where it is difficult to justify
a particular error component structure.
In this article we make three contributions. The first one is a novel framework for
clustering, building on the one developed by Abadie et al. [2020] for the analysis of regression
estimators from a design perspective. We allow for clustering both in the sampling process
and in the assignment process. As a result, the framework nests both the traditional case of
clustered sampling and the case of clustered treatment assignment in experiments as special
cases. It also allows for intermediate cases. In particular, treatment assignment may depend
on cluster but not perfectly so, and there remains variation in treatments within-clusters.
5

<!-- page 6 -->
This framework clarifies the separate roles of clustering in the sampling process and clustering
in the assignment process. It also clarifies what we can learn from the data about the need
to adjust standard errors for clustering. In our framework, the data are not informative
about the need to adjust for clustering in the sampling process, but they are informative
about the need to adjust for clustering in the assignment process.
In our second contribution, we derive central limit theorems and large sample variances
for the least squares and the fixed effect estimators of average treatment effects that take
into account variation both from sampling and assignment. Comparing these variances to
limit versions of the robust and cluster variances shows that the robust standard errors are
generally too small, and the cluster standard errors are unnecessarily conservative. These
comparisons also highlight how heterogeneity in treatment effects affects inference in the estimation of average treatment effects. Often researchers specify models that implicitly assume
constant treatment effects without appreciating the implications for inference. We show,
however, that heterogeneity in treatment effects introduces additional variance components
that affect the need for clustering adjustments.
In our third contribution, we propose new variance formulas and bootstrap procedures
for treatment effects estimators in the presence of clustering. We use the term Causal Cluster
Variance (CCV) for the analytic variance formulas. For the case of a least squares estimator
of average treatment effects, the intuition for the CCV variance formula is as follows. The
error of the least squares estimator is approximately equal to a sum, over all units, of
an expression involving products of regression errors and regressors values. The robust
variance is approximately equal to a sum, over all units, of the squares of these products.
In contrast, the conventional cluster variance estimator is approximately equal to a sum,
over all clusters, of squares of within-cluster sums of the same products. Although the sum
over all clusters of the expectation of the within-cluster sums of these products is zero, the
expectation for each cluster separately is not. For each cluster in the sample, it is possible to
estimate the expectation of the sum of the products between regression errors and regressors
values. The CCV formula uses these estimates to correct the bias of the conventional cluster
6

<!-- page 7 -->
variance. The CCV correction does not help much if only a small fraction of clusters are
sampled. However, when a large fraction of the clusters are represented in the sample, the
CCV correction can lead to substantial improvements. This adjustment relies on estimates
of cluster-level treatment effects, and thus requires within-cluster variation in treatment
assignment. In addition, we propose a bootstrap version of the variance estimator., which
we compare to two benchmarks. In contrast to conventional bootstrap procedures, which
are based on resampling individual units or entire clusters of units, our proposed Two-Stage-
Cluster-Bootstrap (TSCB) conducts resampling in two stages. In the first stage, the fraction
treated for each cluster is drawn from the empirical distribution of cluster-specific treatment
fractions. In the second stage, the researcher samples the treated and control units from
each cluster, with their number of units determined in the first stage. The CCV and TSCB
variance estimators are designed for applications with large number of observations and
substantial variation in treatment assignment within clusters.
To illustrate the empirical relevance of our results, we analyze a sample from the 2000
U.S. Decennial Census, which includes 2,632,838 individuals. We define 52 clusters according
to residency in the 50 states, Puerto Rico, and the District of Columbia. We consider two
log-linear regressions of individual earnings on a treatment variable that encodes information
on college attendance. In the first specification, the treatment variable is measured as an
average, at the state level. In a second specification, we measure college attendance at the
individual level.
In Panel A of Table 1, we report results for a regression where the only explanatory
variable is a binary treatment that takes value one if the fraction of individuals with at least
some college residing in the state is 0.55 or higher, and value zero otherwise (we chose the
0.55 value to ensure sufficient variation in the treatment over the 52 clusters). Notice that the
treatment is constant within states. We report the ordinary least squares (OLS) estimate, as
well as robust and cluster standard errors. Since the late 1980s, it has been common practice
to report cluster standard errors in settings where the regressors are constant within a cluster.
Clustering at the state level makes a substantial difference relative to using robust standard
7

<!-- page 8 -->
Table 1: College effects in the Census sample
Dependent variable: Log labor earnings
Panel A
Treatment: State indicator for share of some
college greater than 0.55
OLS
coefficient 0.1022
standard error:
robust (0.0012)
cluster (0.0312)
Panel B
Treatment: Individual indicator for some college
OLS FE
coefficient 0.4656 0.4570
standard error:
robust (0.0012) (0.0012)
cluster (0.0269) (0.0276)
causal cluster variance (CCV) (0.0035) (0.0014)
two-stage cluster bootstrap (TSCB) (0.0036) (0.0014)
errors, with the cluster standard errors approximately twenty-six times larger than the robust
standard errors.
In Panel B of Table 1, the sole regressor is an individual-level indicator for at least some
college. In addition to OLS, we report the fixed effects (FE) estimate (with fixed effects for
the 50 states, plus Washington DC and Puerto Rico) and robust, cluster, CCV, and TSCB
standard errors in parentheses. Like for the regression of the first panel, clustering at the
state level makes a substantial difference in the standard errors, with the cluster standard
errors approximately twenty-three times larger than the robust standard errors, both for the
OLS and the FE regressions. In Panel B, our proposed CCV and TSCB standard errors for
the OLS estimate are 0.0035 and 0.0036 respectively, in between the robust standard errors
(0.0012) and the cluster standard errors (0.0269), and substantially different from both. The
same holds for the FE estimator. The cluster standard error is 0.0276, quite different from
the robust standard errors, 0.0012. The CCV and TSCB standard errors are 0.0014, in
8

<!-- page 9 -->
between robust and cluster but much closer to robust.
2. A Framework for Clustering
In this section, we describe in detail the framework for our analysis. There are multiple
components to our set-up that are not explicitly modeled in the usual analysis of the variance
of econometric estimators. In general, quantifying the uncertainty of parameter estimates
requires describing the population and articulating the assumptions that describe how the
sample was generated from that population (that is, building a model for the data generating
process). In our framework, there are three distinct sources of sampling variation that lead
to variation in the estimates. First, there is variation across samples in which units are
observed in each cluster. Second, there is potentially variation in which clusters are observed
(which leads to different units being observed). Third, there is variation in the treatment
assignment across units. Whereas the standard framework for clustering focuses solely on
the first two (sampling) sources of uncertainty, our proposed framework allows for all three.
How much these three components matter for the variance of the least squares and fixed
effects estimators of the average treatment effect depends on (i) the sampling process, (ii)
the assignment process, and (iii) the heterogeneity in the treatment effects across clusters.
To facilitate the calculation of asymptotic approximations in a range of relevant settings
for empirical practice, it is convenient to formally consider a sequence of populations where
we can separately control the fraction of units in the population that are sampled and the
fraction of clusters in the population that is sampled, as well as the assignment mechanism.
2.1. A Sequence of Populations
We have a sequence of populations indexed by k. The k-th population has nk units, indexed
by i“ 1, . . . , nk. The population is partitioned into mk clusters. Let mk,i P t1, . . . , mku
denote the cluster that unit i of population k belongs to. The number of units in cluster m
of population k is nk,m ě 1. For each unit, i, there are two potential outcomes, yk,ip1q and
yk,ip0q, corresponding to treatment and no treatment. Thus the population is characterized
by the set of triples pmk,i, yk,ip0q, yk,ip1qq, for units 1, . . . , nk and clusters 1, . . . , mk. The
9

<!-- page 10 -->
object of interest is the population average treatment effect
1
τk “
nk
nk
ÿ
i“1
`yk,ip1q ´ yk,ip0q˘.
The population average treatment effect by cluster is
1
τk,m“
nk,m
nk
ÿ
i“1
1tmk,i“ mupyk,ip1q ´ yk,ip0qq.
Therefore,
mk
τk “
ÿ
nk,m
nk
τk,m.
m“1
We assume that potential outcomes, yk,ip1q and yk,ip0q, are bounded in absolute value, uniformly for all pk, iq.
For each unit in the population, we define the stochastic treatment indicator, Wk,i P t0, 1u.
The realized outcome for unit i in population k is Yk,i“ yk,ipWk,iq. For a random sample of
the population, we observe the triple pYk,i, Wk,i, mk,iq. Inclusion in the sample is represented
by the random variable Rk,i, which takes value one if unit i belongs to the sample, and value
zero if not. We next describe the two components of the stochastic nature of the sample:
the sampling process that determines the values of Rk,i, and the assignment process that
determines the values of Wk,i.
2.2. The Sampling Process
The sampling process that determines the values of Rk,i is independent of the potential
outcomes and the assignments. It consists of two stages. First, clusters are sampled with
cluster sampling probability qk P p0, 1s. Second, units are sampled from the subpopulation
consisting of all the sampled clusters, with unit sampling probability equal to pk P p0, 1s.
Both qk and pk may be equal to one, or close to zero. If qk “ 1, we sample all clusters.
If pk “ 1, we sample all units from the sampled clusters. If qk “ pk “ 1, all units in the
population are sampled. The standard framework for analyzing clustering focuses on the
special case where qk Ñ 0, so only a small fraction of the clusters in the population are
sampled. The case qk “ 1 and pk Ñ 0 corresponds to taking a relatively small random
10

<!-- page 11 -->
sample of units from the population. While this is an important special case, there are also
many applications where the sampled clusters comprise a large fraction of the overall set of
clusters. We refer to the case of qk “ 1 as random sampling and to the case of qk ă 1 as
clustered sampling.
2.3. The Assignment Process
The assignment process that determines the values of Wk,i also consists of two stages. In the
first stage of the assignment process, for cluster m in population k, an assignment probability
Ak,m P r0, 1s is drawn randomly from a distribution with mean µk, bounded away from zero
and one uniformly in k, and variance σ2
k , independently for each cluster. The variance σ2
k
is key. If σ2
k is zero, then Ak,m is the same for all m, and Wk,i is randomly assigned across
clusters. We refer to this case as random assignment. For positive values of σ2
k assignment
probabilities depend on cluster. Because A2
k,m ď Ak,m, it follows that σ2
k is bounded above
by µkp1´ µkq and that the bound is attained when Ak,m can only take values zero or one, so
all units within a cluster have the same values for the treatment. We use the term clustered
assignment to refer to the case σ2
k “ µkp1´ µkq, when there is no within-cluster variation in
Wk,i. We use the term partially clustered assignment to refer to the case 0 ă σ2
k ă µkp1´ µkq,
where assignment depends on cluster but not all units in the same cluster necessarily have
the same value of Wk,i. In the second stage of the assignment process, each unit in cluster
m is assigned to the treatment independently, with cluster-specific probability Ak,m.
3. The Least Squares Estimator and its Variance
Let
Nk,1 “
nk
ÿ
i“1
Rk,iWk,i and Nk,0 “
nk
ÿ
i“1
Rk,ip1´ Wk,iq
be the number of treated and untreated units in the sample, respectively; these are random
variables. The total sample size is Nk “ Nk,1 ` Nk,0.
We first analyze the OLS estimator of a regression of the outcome Yk,i on an intercept
and the treatment indicator Wk,i. The OLS estimator (modified so it is well-defined even
11

<!-- page 12 -->
when Nk,1 “ 0 or Nk,0 “ 0) is equal to the difference in means:
p
τk “
1
Nk,1 _ 1
nk
ÿ
i“1
Rk,iWk,iYk,i´
1
Nk,0 _ 1
nk
ÿ
i“1
Rk,ip1´ Wk,iqYk,i, (1)
where Nk,1 _ 1 and Nk,0 _ 1 are the maxima of Nk,1 and 1 and of Nk,0 and 1, respectively.
We make the following assumptions about the sampling process and the cluster sizes: (i)
mkqk Ñ 8, (ii) lim infkÑ8 pk minm nk,m ą 0, and (iii) lim supkÑ8 maxm nk,m{ minm nk,m ă
8. The first assumption implies that the expected number of sampled clusters goes to infinity
as k increases. The second assumption implies that the average number of observations
sampled per cluster, conditional on the cluster being sampled, does not go to zero. The third
assumption restricts the imbalance between the number of units across clusters. Notice that
assumptions (i) and (ii) imply nkpkqk Ñ 8, so the sample size becomes larger in expectation
as k increases.
3.1. Large k Distribution of the Least Squares Estimator
Our first main result derives the large k distribution ofp
τk . Let αk “ p1{nkq řnk
i“1 yk,ip0q,
uk,ip1q “ yk,ip1q ´ pαk ` τkq, and uk,ip0q “ yk,ip0q ´ αk. Under additional regularity conditions
in the Appendix,
aNkpp
τk´ τkq{v
1{2
k
d
ÝÑ N p0, 1q,
where
1
vk “
nk
´ pk
nk
ÿ
i“1 ˆu2
k,ip1q
µk
1
nk
ÿ
nk
i“1
`
u2
k,ip0q
1´ µk ˙
` pkp1´ qkq 1
nk
1
` pkσ2
k
nk
`uk,ip1q ´ uk,ip0q˘2
1
nk
´ pkσ2
k
ÿ
nk
i“1 ˆuk,ip1q
uk,ip0q
`
µk
1´ µk ˙2
mk
m“1 ˜nk
ÿ
ÿ
i“1
mk
m“1 ˜nk
ÿ
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
1tmk,i“ muˆuk,ip1q
µk
uk,ip0q
`
1´ µk ˙¸2
. (2)
The expression for the variance vk has multiple terms that make its interpretation challenging. We first interpret vk in some special cases to highlight the implications of clustered
12

<!-- page 13 -->
sampling and clustered assignment. In Section 3.3, we compare vk to the large-k form of the
robust and cluster variance estimators.
For the case of random sampling (qk “ 1) and random assignment (σ2
k “ 0), the variance
simplifies to
1
nk
nk
ÿ
i“1 ˆu2
k,ip1q
µk
`
u2
k,ip0q
1´ µk ˙´ pk
1
nk
nk
ÿ
i“1
`uk,ip1q ´ uk,ip0q˘2
.
As we show in Section 3.2 below, the first term in this variance is estimated by the robust
variance estimator. The second term is a finite sample correction that is familiar from the
literature on randomized experiments [e.g., Neyman, 1923/1990, Imbens and Rubin, 2015,
Abadie et al., 2020]. This finite sample correction vanishes if there is either no heterogeneity
in the treatment effects (so uk,ip1q ´ uk,ip0q “ yk,ip1q ´ yk,ip0q ´ τk “ 0), or if the sample is a
small fraction of the population (pk « 0).
Adding clustered sampling, qk ă 1, increases the variance by
pkp1´ qkq 1
nk
mk
m“1 ˜nk
ÿ
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
,
which is the same as
pkp1´ qkq 1
mk
ÿ
n2
k,mpτk,m´ τkq2
.
nk
m“1
This term vanishes if there is no heterogeneity in the average treatment effect across clusters.
Although the sample is informative about heterogeneity in cluster average treatment effects,
it is not informative about the value of qk. Information about the need to adjust for clustered
sampling (qk ă 1) must come from outside the sample.
Clustered assignment, σ2
k ą 0, adds two terms to the variance,
1
´pkσ2
k
nk
nk
ÿ
i“1 ˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙2
1
` pkσ2
k
nk
mk
m“1 ˜nk
ÿ
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙¸2
.
As we explain in more detail in section 3.3, the sign of this expression depends on the
amount of variation in potential outcomes that can be explained by the clusters. Note that
in contrast to the lack of sample information about the need to adjust for clustered sampling,
the sample is potentially informative about the need to account for clustered assignment.
13

<!-- page 14 -->
The five terms making up the asymptotic variance vk can be of different order. The first
term is an average of bounded terms, and so under our assumptions will be of order Op1q.
The second and third terms will be at most of the same order as the first one. If pk « 0 so
we can think of the sample as small relative to the population of sampled clusters, the first
term dominates the second and third terms. If cluster sizes are bounded as k increases, the
fourth and fifth terms in are also order Op1q. If, on the other hand, cluster sizes increase
with k, these terms can be of higher order and dominate the variance. Whether they do
so or not depends on the (i) magnitude of pk, (ii) presence of clustering in sampling, (iii)
presence of clustering in assignment, and (iv) heterogeneity in potential outcomes.
3.2. The Robust and Cluster Robust Variance Estimators
Letp
Uk,i“ Yk,i´
p
αk´
p
τkWk,i be the residuals from the regression of Yk,i or a constant and
Wk,i. Here,p
αk is the intercept of the regression andp
τk is the coefficient on Wk,i (equal to
the expression in (1) with probability approaching one).
There are two common estimators of the variance of ?Nkpp
τk´τkq. First, the conventional
robust variance estimator (Eicker [1963], Huber [1967], White [1980]):
p
1
V robust
k “
W 2
kp1´ W kq2 #1
Nk
nk
ÿ
i“1
p
Rk,i
U 2
k,ipWk,i´ W kq2+, (3)
where
W k “
1
Nk _ 1
nk
ÿ
i“1
Rk,iWk,i.
Let
1
vrobust
k “
nk
Under regularity conditions (see appendix),
nk
ÿ
i“1 ˆu2
k,ip1q
`
µk
u2
k,ip0q
1´ µk ˙.
p
V robust
k and vrobust
k are close in the following sense,
p
V robust
k
vrobust
k
“
` Opp1q,
vk
vk
motivating our focus on the comparison of vrobust
k and vk. In general the difference vrobust
k´ vk
can be positive or negative, so the robust variance estimator can be invalid in large samples.
14

<!-- page 15 -->
The second common variance estimator is the cluster variance [Liang and Zeger, 1986,
Arellano, 1987],
p
V cluster
k “
mk
ÿ
m“1 ˜nk
ÿ
i“1
p
1tmk,i“ muRk,i
Uk,ipWk,i´ W kq¸2, . -. (4)
Define
1
W 2
kp1´ W kq2
$ & %
1
Nk
1
nk
´ pk
vcluster
k “
` pk
` pkσ2
k
nk
ÿ
i“1 ˆu2
k,ip1q
`
µk
1
nk
ÿ
nk
i“1
1
mk
nk
m“1 ˜nk
ÿ
ÿ
i“1
1
mk
nk
m“1 ˜nk
ÿ
ÿ
i“1
u2
k,ip0q
1´ µk ˙
`uk,ip1q ´ uk,ip0q˘2
1
nk
´ pkσ2
k
nk
ÿ
i“1 ˆuk,ip1q
`
µk
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
1tmk,i“ muˆuk,ip1q
µk
uk,ip0q
`
1´ µk ˙¸2
.
uk,ip0q
1´ µk ˙2
Then,
p
V cluster
k is close to vcluster
k in the sense that
p
V cluster
k
vcluster
k
“
` Opp1q.
vk
vk
The difference vcluster
k´ vk is always nonnegative. Therefore, for large k, the cluster variance
estimator can be conservative but cannot underestimate the variance ofp
τk.
3.3. Discussion
From the formulas for vk, vrobust
k , and vcluster
k it follows that if pk is small enough, then vrobust
k
and vcluster
k are approximately equal to vk. In this case, clustered sampling and clustered
assignment do not matter much because the probability that two sample units belong to the
same cluster is small.
The difference vrobust
k´ vk depends on two terms. The first term,
1
pk
nk «nk
ÿ
i“1
`uk,ip1q ´ uk,ip0q˘2 ´ p1´ qkqmk
ÿ
m“1
n2
k,mpτk,m´ τkq2ff, (5)
is equal to zero when treatment effects are constant (in which case, uk,ip1q ´ uk,ip0q “ 0 for
i“ 1, . . . , nk and τk,m´ τk “ 0 for all m “ 1, . . . , mk). If all clusters are sampled, so qk “ 1,
15

<!-- page 16 -->
and treatment effects are heterogeneous, (5) is positive. When only a fraction of the clusters
are sampled, qk ă 1, the sign of (5) depends on the extent to which heterogeneity in treatment
effects can be explained by the clusters. If there is no variation in average treatment effects
across clusters, the expression in (5) is non-negative. However, when clusters explain much
of the variation in treatment effects, the expression in (5) can be negative and very large in
magnitude because of the factor n2
k,m. The second term of vrobust
k´ vk is equal to
pkσ2
k
mk
ÿ
m“1
nk,m
nk «1
nk,m
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
´ nk,m˜1
nk,m
`
uk,ip0q
1´ µk ˙2
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙¸2ff. (6)
This term is equal to zero if there is no clustered assignment, that is, σ2
k “ 0. If σ2
k ą 0, the
sign of (6) depends on how much of the heterogeneity in potential outcomes is explained by
the clusters. The expression in (6) is close to zero when there is little heterogeneity in potential outcomes, so uk,ip1q and uk,ip0q are close to zero. If there is heterogeneity in potential
outcomes but average potential outcomes are nearly constant across clusters, (6) is positive.
When the clusters explain enough heterogeneity in potential outcomes (6) can be negative
and potentially very large in magnitude because of the factor nk,m multiplying the second
term of the sum in (6). That is, the robust variance formula can severely underestimate the
variance ofp
τk.
Clustered standard errors are conservative in general, that is, vcluster
k ě vk. In particular,
the difference vcluster
k´ vk is
1
vcluster
k´ vk “ pkqk
nk
mk
m“1 ˜nk
ÿ
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
,
which can be rewritten as
vcluster
k´ vk “ ˆpknk
mk ˙qk #1
mk
mk
ÿ
m“1 ˆnk,mmk
nk ˙2
pτk,m´ τkq2+. (7)
When the expected fraction of clusters in the sample, qk, is small, or when the average
treatment effect is nearly constant between clusters, then vcluster
k « vk. Aside from these
16

<!-- page 17 -->
special cases, the pknk{mk factor in the formula above indicates that cluster standard errors
can be extremely conservative in general.
4. Two New Variance Estimators
Estimation of the variance ofp
τk is challenging because the different terms in vk can be of
different orders of magnitude. In this section, we propose two estimators of the variance of
p
τk that allow us to correct the bias of the cluster variance estimator, one analytic, and one
resampling-based. As the expression for the bias of the cluster variance in (7) shows, the
cluster variance is heavily biased if the fraction of the sampled clusters is large and there is
substantial variation in the cluster-specific treatment effects. Although the proposed analytic
variance estimator is defined irrespective of the value of σ2
k, in order to for the correction to
be effective we need to be able to estimate the cluster-specific treatment effects, and thus we
need σ2
k to be less than its maximum value of µkp1´µkq to ensure that there is variation in the
treatment assignment within clusters. One of the proposed variance estimators is based on
a correction top
V cluster
k , and the other is based on resampling methods. An alternative would
be to directly estimate the bias term in (7) and subtract that from the cluster variance.
A challenge with this approach is that the estimation error for the adjustment term is
large (often leading to negative variances estimates) because the order of magnitude of the
correction is itself large and this approach did not work well in our simulations. We do not
report formal results for the variance estimators in the current paper. We demonstrate their
performance in the simulations in Section 6. There may well be further refinements possible.
p
If qk is close to zero, the proposed variance estimators are close to
V cluster
k , which has
little bias in that case. If σ2
k “ µkp1´ µkq (that is, when Wk,i is constant within clusters),
the proposed resampling variance estimator is not defined. To be effective both variance
estimators rely on estimating the variation in treatment effects across clusters, and therefore
require a substantial number of both treated and control observations per cluster. The
p
proposed variance estimators lead to substantial improvements over
V cluster
k in cases where
p
V cluster
k has a large upward bias. The downside of the proposed variance estimators is that
they can be conservative when there is no need to cluster because there is no heterogeneity
17

<!-- page 18 -->
in treatment effects, or when there are too few treated and control observations per cluster
to estimate the heterogeneity in the treatment effects precisely.
We first consider in Section 4.1 the case with qk “ 1 so we have random sampling. Next we
consider in Section 4.2 the case with clustered sampling qk ă 1. In Section 4.3 we propose a
bootstrap procedure for estimating the variance. The proposed variance estimators perform
very well in the simulation study of Section 6. The derivation of their formal properties is
left for future work.
4.1. The Case with All Clusters Observed
First we focus on the case with qk “ 1 (all clusters observed), but allowing for general pk.
Let Uk,i“ Wk,iuk,ip1q ` p1´ Wk,iquk,ip0q. The first step is to approximate the normalized
error of the least squares estimatorp
τk by a normalized sample average over clusters,
aNkpp
τk´ τkq{v
1{2
k “
1
?nkpkvkµkp1´ µkq
mk
ÿ
m“1
Ck,m ` Opp1q, (8)
where the terms
nk
Ck,m“
ÿ
1tmk,i“ muRk,ipWk,i´ µkqUk,i
i“1
are independent across clusters. In the appendix, we show
1
p
V cluster
k {vk “
nkpkvk ˆ1
µkp1´ µkq ˙2 mk
ÿ
m“1
The expectation of Cm,k is
C2
k,m ` Opp1q. (9)
ErCk,ms “ nk,mpkµkp1´ µkqpτk,m´ τkq,
with sum over clusters
mk
ÿ
m“1
ErCk,ms “ pkµkp1´ µkqmk
ÿ
m“1
nk,mpτk,m´ τkq “ 0. (10)
That is, although the sum of the expectations of Ck,m over clusters is equal to zero, these
expectations are not equal to zero in general for each cluster separately. Because varpCk,mq ď
ErC2
k,ms, the first term on the right-hand side of (9) is conservative on expectation relative
to the variance of ?Nkpp
τk´ τkq{v
1{2
p
k , which explains the conservativeness of
V cluster
k.
18

<!-- page 19 -->
Because of (10), we can replace the terms Ck,m in (8) by Ck,m´ErCk,ms “ Ck,m,1 `Ck,m,2,
where
Ck,m,1 “
and
Ck,m,2 “
nk
ÿ
i“1
nk
ÿ
i“1
1tmk,i“ mupRk,i´ pkqpτk,m´ τk qµkp1´ µkq,
1tmk,i“ muRk,i´pWk,i´ µkqUk,i ´ pτk,m´ τkqµkp1´ µkq¯.
Therefore,
aNkpp
τk´ τkq{v
1{2
1
k “
?nkpkvkµkp1´ µkq ˜mk
ÿ
Ck,m,1 `
m“1
mk
ÿ
m“1
Ck,m,2¸` Opp1q. (11)
It can be shown that Ck,m,1 and Ck,m,2 have means equal to zero and are uncorrelated. In addition, Ck,m,1 and Ck,m,2 are uncorrelated across clusters. The variance of řmk
m“1 Ck,m,1{p?nkpkµkp1´
µkqq is
p1´ pkqmk
ÿ
nk,m
pτk,m´ τkq2
.
nk
m“1
Letp
τk,m be difference between the sample average of the outcome for treated and nontreated
units in cluster m. A direct estimator the variance of řmk
m“1 Ck,m,2 is
mk
m“1 ˜nk
ÿ
ÿ
1tmk,i“ muRk,i´pWk,i´ W kqp
Uk,i ´ pp
τk,m´
p
i“1
τkqW kp1´ W kq¯¸2
, (12)
In practice, the estimator in (12) is biased from the correlations between the estimation
errors of its components. We apply sampling splitting to address this bias. We first split the
sample randomly into two subsamples. Let Zk,i P t0, 1u be the indicator that unit i belongs
to the second subsample, and let Zk be the mean of Zk,i. Using the subsample with Zk,i“ 0,
we obtain estimatesp
τ ˚
p
α ˚
k,m,
k , andp
τ ˚
k of τk,m, αk, and τk, respectively. Next, for observations
p
with Zk,i“ 1, we calculate the residuals
U ˚
k,i“ Yk,i´
p
α ˚
p
k´
τ ˚
k Wk,i. Finally, we estimate the
normalized variance for the case with qk “ 1 as
p
V CCV
k p1q “ 1
mk
NkW 2
kp1´ W kq2
m“1 «1
ÿ
Z2
k ˜nk
ÿ
1tmk,i“ muRk,iZk,i´pWk,i´ W kqp
U ˚
k,i
i“1
´ pp
τ ˚
k,m´
p
τ ˚
k qW kp1´ W kq¯¸2
19

<!-- page 20 -->
1´ Zk
nk
´
Z2
ÿ
k
i“1
` p1´ pkqmk
ÿ
m“1
1tmk,i“ muRk,iZk,i´pWk,i´ W kqp
U ˚
k,i ´ pp
τ ˚
k,m´
p
τ ˚
k qW kp1´ W kq¯2ff
Nk,m
Nk
pp
τk,m´
p
τkq2
, (13)
where Nk,m is the size of the sample in cluster m. For clusters with no variation in the
treatment variable, we replacep
τk,m in (13) withp
τk. For clusters with no variation in the
treatment variable for a particular subsample, we replacep
τ ˚
k,m in (13) withp
τ ˚
k . We derive
the form of the CCV estimator in the appendix. To improve the precision ofp
V CCV
k p1q, we
re-estimate it multiple times with new sample splits (new values for Zk,i) and then average
the corresponding variance estimators. In our simulations of section 6, we re-estimate the
variance estimator four times, and use sample splits with in expectation an equal number of
units in each subsample, so ErZks “ 1{2.
4.2. The Case When Not All Clusters Are Sampled
To motivate the modification of the variance estimatorp
V CCV
k p1q for the qk ă 1 case, notice
that
vkpqkq ´ vcluster
k “ qk ˆ pvkp1q ´ vcluster
k q,
where vkpqkq denotes the value of the true variance vk evaluated at qk. That is, the variance
for the general qk case is a convex combination of the true variance at qk “ 1 and the cluster
variance,
vkpqkq “ qk ˆ vkp1q ` p1´ qkq ˆ vcluster
k.
Letp
qk be the ratio between the number of sampled clusters and the total number of clusters
p
in the population. The proposed variance estimator,
V CCV
k , is a convex combination of
p
V CCV
k p1q andp
V cluster
k with weightsp
qk and 1´
p
qk,
p
V CCV
k “
p
qk ˆ
p
V CCV
k p1q ` p1´
p
qkq ˆp
V cluster
k. (14)
Computation ofp
qk requires knowledge of mk, the total number of clusters in the population.
20

<!-- page 21 -->
4.3. A Bootstrap Variance Estimator
In the previous sections, we have discussed an analytic variance estimator. Here we suggest
a resampling-based variance estimator, initially for the case with qk “ 1. Like the causal
bootstrap in Imbens and Menzel [2021], the proposed bootstrap procedure takes into account the causal nature of the estimand and creates bootstrap samples where units (in this
case clusters) have different assignments and assignment probabilities than they have in the
original sample. It differs from earlier bootstrap variance estimators for clustered settings
[e.g., Cameron and Miller, 2015, Menzel, 2021] in that it allows for the possibility that a
large fraction of clusters are observed.
The specific resampling procedure, which we call the two-stage-cluster-bootstrap (TSCB),
consists of two stages. For each of the clusters, let Nk,m be the cluster-level sample size and
W k,m“ Nk,m,1{pNk,m _ 1q the cluster-level fraction of treated units. In the first stage of the
bootstrap procedure, for each cluster we draw W b
k,m with replacement from the empirical
distribution of the cluster-level fractions of treated units, that is with probability 1{mk from
the set tW k,1, . . . , W k,mku. In the second stage, we draw Nk,mW b
k,m units with replacement
from the set of treated units in cluster m and Nk,mp1´ W b
k,mq units with replacement from
the set of untreated units in cluster m. In order for this to be well-defined we do need
all the W k,1 to be strictly between zero and one. We do this for all clusters to create the
bootstrap sample, and calculate the bootstrap standard errors as the standard deviation of
the treatment effect estimates across bootstrap iterations.
Next, consider the case with qk ă 1. In this case, we need to take into account the fact
that we see a fraction of the clusters in the population. We follow the approach proposed in
Chao and Lo [1985]. Suppose q“ 1{2, so we observe half the clusters in the population. The
bootstrap procedure first creates a pseudo population consisting of the original population
of clusters, plus one additional replica of each cluster. Then, to get a bootstrap sample, we
sample randomly, without replacement, from the clusters in this pseudo population. Given
the clusters in the bootstrap sample, we proceed as before, and ultimately calculate the
bootstrap variance as the variance of the estimator over the bootstrap samples. Chao and Lo
21

<!-- page 22 -->
[1985] provide details and extensions to the case for the case where 1{qk is not an integer.
The algorithm for the TSCB is summarized here.
Algorithm 1 Two Stage Cluster Bootstrap
Input:
Sample pYk,i, Wk,i, mk,iq
Fraction sampled clusters qk
Number of bootstrap replications B
Stage 1:
1a: Create pseudo population by replicating each cluster 1{qk times
1b: For each cluster in the pseudo population, calculate the assignment probability
W k,m
1c: Create a bootstrap sample of clusters by randomly drawing clusters from the pseudo
population from Stage 1a
1d: For each sampled cluster, draw an assignment probability Ak,m from the empirical
distribution of the W k,m from Stage 1b
Stage 2:
2a: Randomly draw from the set of treated units in cluster m, tNk,mAk,mu units
2b: Randomly draw from the set of control units in cluster m, tNk,mp1´ Ak,mqu units
Calculations:
For the units in the bootstrap sample constructed in Stage 2, collect the values for
pYk,i, Wk,i, mk,iq and calculate the least squares or fixed effect estimator
Calculate the standard deviation of the least squares or fixed effect estimator over the
B bootstrap samples
5. The Fixed Effect Estimator
In this section, we report results for the fixed effect estimator often used in empirical research
in economics. Arellano [1987], Bertrand, Duflo, and Mullainathan [2004], Cameron and Miller
[2015] and MacKinnon, Nielsen, and Webb [2021] have pointed out that cluster adjustments
may still be necessary in fixed effects regressions. However, a view of clustering based on
models with cluster-specific variance components creates ambiguity in the role of clustered
standard errors for estimators with cluster fixed effects, which are specifically aimed to absorb
cluster-level variation.
We first characterize the fixed effect estimator and derive its large k distribution. Then,
we discuss the properties of the two conventional variance estimators, the robust and cluster
22

<!-- page 23 -->
robust variance estimators. As in the least squares case, we find that the robust standard
errors may be too small and the cluster standard errors may be unnecessarily large, especially
in cases when the number of observations per cluster is large. We propose CCV and TSCB
variance estimators. The CCV estimator for fixed effects has a different form than the one
for least squares in section A.4.
The fixed effect estimator is based on a regression of the outcome on the treatment
indicator and indicators for each of the clusters in the sample. It can be written as the
least squares estimate for a regression of the outcome on the treatment, with both variables
measured in deviation from cluster means,
p
τ fixed
k “
mk
ÿ
m“1
mk
ÿ
m“1
nk
ÿ
i“1
nk
ÿ
i“1
1tmk,i“ muRk,iYk,ipWk,i´ W k,mq
. (15)
1tmk,i“ muRk,iWk,ipWk,i´ W k,mq
Like in section 3, we assume that that potential outcomes are bounded, mkqk Ñ 8,
and lim supkÑ8 maxm nk,m{ minm nk,m ă 8. In addition, we assume (i) pmkqkq{pppknkq{mkq
Ñ 0, and (ii) the supports of the cluster probabilities, Ak,m, are bounded away from zero
and one (uniformly in k and m). Assumption (i) restricts the focus of our analysis in this
section to settings where the expected number of sampled clusters is small relative to the
expected number of sampled observations per sampled cluster. Together with the previous
assumptions, assumption (i) implies ppknkq{mk Ñ 8, nkpkqk Ñ 8, and pk minm nk,m Ñ 8.
This last result, along with assumption (ii), ensures thatp
τ fixed
k in (15) is well-defined with
probability approaching one.
Let αk,m “ p1{nk,mq řnk
i“1 1tmk,i“ muyk,ip0q. For an observation, i, with mk,i“ m, we
define the within-cluster residuals ek,ip0q “ yk,ip0q ´ αk,m and ek,ip1q “ yk,ip1q ´ τk,m´ αk,m.
Let
˜
vk “ fk{pµkp1´ µkq ´ σ2
kq2 (16)
where
fk “ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
i“1
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
nk
ÿ
i“1
e2
k,ip0q
23

<!-- page 24 -->
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
` ´ErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2s
` 2qkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
nk,m
nk
pτk,m´ τkq2
m“1
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
n2
k,m
nk
pτk,m´ τkq2
.
Under additional regularity conditions, which are described in the Appendix, we obtain the
large k distribution of the fixed effects estimator,
aNkpp
τ fixed
k´ τkq{˜
1{2
v
k
d
ÝÑ N p0, 1q. (17)
Letr
r
Ă
r
Uk,i“
Yk,i´
p
τ fixed
k
Wk,i, where
Yk,i“ Yk,i´ Y k,mk,i,
robust estimator of the variance of ?Nkpp
τ fixed
k´ τkq is
Ă
Wk,i “ pWk,i´ W k,mk,iq. The
r
V robust
k “
1
Nk
nk
ÿ
i“1
Ă
r
Rk,i
W 2
U 2
k,i
k,iO ˜1
Nk
nk
ÿ
i“1
Ă
Rk,i
W 2
k,i¸2
. (18)
Now let,
˜
vrobust
k “ f robust
k {pµkp1´ µkq ´ σ2
k q2
.
with
f robust
k “ ErAk,mp1´ Ak,mq2s 1
nk
ÿ
nk
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
i“1
nk
ÿ
i“1
` ErAk,mp1´ Ak,mqp1´ 3Ak,mp1´ Ak,mqqsmk
ÿ
nk,m
nk
pτk,m´ τkq2
.
m“1
e2
k,ip0q
Notice that all terms of f robust
k are bounded. In the appendix, we show that
r
V robust
k “
˜
vrobust
k ` Opp1q.
The cluster variance estimator for fixed effects is
r
V cluster
k “
1
Nk
mk
ÿ
m“1 ˜nk
ÿ
i“1
Ă
r
1tmk,i“ muRk,i
Wk,i
Uk,i¸2O ˜1
Nk
nk
ÿ
i“1
Ă
Rk,i
W 2
k,i¸2
24
. (19)

<!-- page 25 -->
Let,
˜
vcluster
k “ f cluster
k {pµkp1´ µkq ´ σ2
k q2
.
with
f cluster
k “ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
i“1
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
nk
ÿ
i“1
e2
k,ip0q
` pErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2sqmk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
` pkErA2
k,mp1´ Ak,mq2smk
ÿ
m“1
n2
k,m
nk
pτk,m´ τk q2
.
We obtain in the appendix,
r
V cluster
k
˜
vk
˜
vcluster
k
“
˜
` Opp1q.
vk
Similar to the least squares case, the robust variance can underestimate the true variance,
and the cluster variance is generally too large. Our proposed variance estimator is a convex
combination ofr
V cluster
k and andr
V robust
k , with the weights selected to correct the bias of the
cluster variance estimator as k increases (see appendix for details).
r
V CCV
k “
p
r
λk
V cluster
k ` p1´
p
λkqr
V robust
k. (20)
where the estimated weight for the cluster variance is
p
λk “ 1´ qk
˜1
Mk
1
Mk
mk
ÿ
m“1
mk
ÿ
m“1
Qk,mW k,mp1´ W k,mq¸2
,
Qk,mW 2
k,mp1´ W k,mq2
where Qk,m is an indicator that takes value one if cluster m of population k is sampled, and
Mk “ řmk
m“1 Qk,m is the total number of sampled clusters. The second factor in the second
term approximately (that is, ignoring the variance of W k,m conditional on Ak,ms) estimates
the variance of Ak,mp1´ Ak,mq divided by its second moment, so that
˜
V pAk,mp1´ Ak,mqq
λ « 1´ qk
ErpAk,mp1´ Ak,mqq2s.
25

<!-- page 26 -->
If there is no variation in Wk,i within any of the clusters the fixed effect estimator is not
defined, and neither is this variance estimator. In all other cases the variance estimator is
well-defined.
We also consider a bootstrap standard error, based on the same resampling procedure
described in Section 4.3.
6. Simulations
We next report simulation results that illustrate the performance of the proposed variance
estimators relative to existing alternatives. To operate in an empirically relevant setting, we
create an artificial population based on the Census data briefly described in the introduction,
which contains information on log earnings, an indicator for college attendance, and an
indicator for state of residence for 2,632,838 individuals.
For each individual in this population of 2,632,838 individuals, we define mk,i using
state of residence (plus Washington, DC, and Puerto Rico), for a total of 52 clusters. We
assign potential outcomes as yk,ip0q “ Yk,i´
p
τk,mWk,i and yk,ip1q “ Yk,i `p
τk,mp1´ Wk,iq,
so treatment effects are constant within clusters. We then repeatedly create samples from
this population. Creating a sample requires fixing pk, qk, and fixing the distribution of Ak,m
and then drawing from the implied distribution for Rk,i and Wk,i to generate outcomes for
all sampled units. In the baseline design, we set pk “ qk “ 1, so we sample all mk “ 52
clusters and all nk “ 2,632,838 individuals in the population. For the assignment mechanism
in the baseline design, we convert cluster means of the treatment variable into log-odds,
p
ℓk,m“ lnpW k,m{p1´ W k,mqq. Let pp
p
µℓ,
σℓq be the average and the sample standard deviation
ofp
ℓk,m. We then draw lnpAk,m{p1´ Ak,mqq for cluster m from a normal distribution with
expected valuep
µℓ and standard deviationp
σℓ. Given the cluster assignment probability Ak,m,
we assign the treatment in cluster m by drawing from a binomial distribution with parameter
Ak,m.
We calculate the standard deviation of the least squares and fixed effect estimators,
normalized by the square root of the sample size, N 1{2
k s.d., across 10,000 samples drawn
according to the procedure outlined above. This is the benchmark against which we compare
26

<!-- page 27 -->
Table 2: Average standard errors across simulations
N 1{2
k s.d. v
1{2
k
normalized standard error
r
1{2
v
k robust cluster CCV TSCB
Baseline design:
pk “ 1, qk “ 1,
στk
“
.120, σk “
.057
Second Design:
pk “
.1, qk “ 1,
στk
“
.120, σk “
.057
Third Design:
pk “
.1, qk “ 1,
στk
“
.480, σk “
.206
Fourth design:
pk “
.1, qk “ 1,
στk
“ 0, σk “
.206
Fifth design:
pk “
.1, qk “ 1,
στk
“
.480, σk “ 0
OLS 5.91 5.90 1.90 44.86 6.32 5.80
FE 2.34 2.32 1.90 44.63 2.31 2.29
OLS 2.61 2.59 1.90 14.28 3.78 2.60
FE 1.95 1.95 1.90 14.21 1.95 1.94
OLS 14.50 14.17 1.98 56.46 13.70 14.33
FE 12.14 11.89 2.13 56.79 11.61 12.07
OLS 9.39 9.39 1.90 8.20 9.19 9.37
FE 2.04 2.04 2.04 1.97 2.04 2.09
OLS 1.95 1.97 1.97 56.42 4.53 2.04
FE 1.91 1.94 1.94 56.42 1.96 1.90
Notes: N {
k s.d. is the standard deviation of the estimators over the simulations, multiplied by the square
root of the sample size. v {
k is the square root of the asymptotic variance in equation (2). ˜ v {
k is the square
root of the asymptotic variance of the fixed effect estimator in (16). The remaining four columns report
average values of robust, cluster, CCV, and TSCB standard errors across simulations (multiplied by N {
k ).
pk and qk are the unit and cluster sampling probabilities, respectively. στk is the standard deviation of the
cluster average treatment effect. σk is the standard deviation across clusters of the treatment assignment
probabilities.
the various estimates of standard errors. For the least squares and the fixed effects estimators,
respectively, we first calculate the (infeasible) asymptotic standard errors v
1{2
k andr
1{2
v
k to
benchmark the performance of the feasible variance estimators. Next, we calculate the
averages across 10,000 simulations of the robust, cluster, CCV, and TCSB standard errors,
where we use 100 bootstrap replications in each simulation. Table 2 reports the results.
Table 3 reports coverage rates for 95 percent confidence intervals. In the design column of
the two tables στk is the standard deviation of the cluster average treatment effect.
For the baseline design, the normalized standard deviation of the least squares estimator is
27

<!-- page 28 -->
Table 3: Coverage rates across simulations
coverage of 95 percent confidence interval
1{2
v
k
r
1{2
v
k robust cluster CCV TSCB
Baseline design:
pk “ 1, qk “ 1,
στk
“
.120, σk “
.057
Second design:
pk “
.1, qk “ 1,
στk
“
.120, σk “
.057
Third design:
pk “
.1, qk “ 1,
στk
“
.480, σk “
.206
Fourth design:
pk “
.1, qk “ 1,
στk
“ 0, σk “
.206
Fifth design:
pk “
.1, qk “ 1,
στk
“
.480, σk “ 0
Notes: See notes of Table 2.
OLS 0.949 FE 0.467 1.000 0.971 0.947
0.950 0.893 1.000 0.947 0.942
OLS 0.951 FE 0.846 1.000 0.996 0.952
0.950 0.944 1.000 0.950 0.948
OLS 0.947 FE 0.208 1.000 0.960 0.950
0.941 0.284 1.000 0.918 0.948
OLS 0.952 FE 0.308 0.905 0.966 0.952
0.952 0.951 0.932 0.951 0.955
OLS 0.952 FE 0.953 1.000 1.000 0.959
0.954 0.955 1.000 0.957 0.949
5.91. This is well approximated by the asymptotic standard error, 5.90. The robust standard
error is on average over the simulations 1.90, less than one-third of the normalized standard
deviation of the estimator. The cluster standard error is far too large, on average 44.86, more
than seven times the value of the normalized standard deviation. CCV improves considerably
over robust and cluster. The average CCV standard error is 6.32, about 7 percent higher
than the normalized standard deviation. The TSCB standard error is the most accurate, on
average equal to 5.80. For the fixed effect estimator, the asymptotic standard error is again
accurate. The robust standard error is about 16 percent too small, leading to a coverage
rate for the nominal 95 percent confidence interval of 0.89 in Table 3. The cluster standard
error is too large by a factor of 20. CCV and TSCB standard errors closely approximate the
normalized standard error.
28

<!-- page 29 -->
It is also interesting to consider the variation in the different variance estimators over the
repeated samples relative to the true value of the standard deviation of the estimator. In
the baseline design the normalized standard deviation is 5.91. The robust standard error is
very precisely estimated, with a standard deviation of the normalized robust standard over
the 10,000 simulations equal to 0.005. The standard deviation of the cluster standard error
is much larger, 1.48. For the CCV standard error the standard deviation is 1.21, and for the
resampling-based TSCB the standard deviation is consideralby lower at 0.69.
We vary the design from the baseline case by changing piq the fraction of sampled units
pk, piiq the amount of treatment effect heterogeneity across clusters, στk, and piiiq the crosscluster standard deviation of the assignment probability, σk. In the second design, pk “ 0.1
is the only change relative to the baseline design. This makes the robust standard errors
less biased downward, and the cluster standard errors less biased upward. The result of
decreasing the fraction of sampled units (and thus decreasing the sample size) is that the
performance of the analytic CCV variance estimator declines, whereas the bootstraping
vaiance estimator TSCB continues to perform well. We keep pk “ 0.1 for the remaining
three designs. In the third design, we increase both the treatment effect heterogeneity and
the within-cluster correlation of the treatment by increasing the differences in treatment
effects τk,m´ τk and the differences of the logs odds ratio ℓk,m´ ℓk by a factor of four. The
resulting increase in σ2
k makes the performance of the robust standard error substantially
worse, consistent with equation (6). In this design, the bias of the robust standard error is
substantial, also for the fixed effect estimator. The difference between the cluster variance
and the true variance for the least squares estimator is proportional to the variation in the
cluster average treatment effects, implying that the bias will increase for this design relative
to the second design. In the fourth design, we remove the heterogeneity in the treatment
effect but keep the correlation in the treatment assignment the same as in the third design.
Now, the cluster variance performs well, but the robust variance remains poor. In the
fifth design, the assignment probabilities are identical in all clusters, and the treatment
effect heterogeneity is the same as in the third and fourth designs. In this case the robust
29

<!-- page 30 -->
standard errors perform well, but the cluster standard errors substantially over-estimate the
uncertainty, as expected. In all designs, the CCV and especially the TSCB standard errors
outperform the robust and cluster standard errors.
7. Implications for Practice
The analysis in this article has several implications for how to compute and, most importantly, interpret, standard errors in a variety of empirical settings. Some settings are clear
cut and others are more subtle. First, we discuss the case where there is no cluster sampling.
If one has a random sample of units from a large population with randomized treatment
assignment at the unit level, there is no reason to cluster the standard errors of the least
squares estimator. Doing so can be harmful, resulting in unnecessarily wide confidence intervals. In this case, clustering is not appropriate even if there is within-cluster correlation in
outcomes (however those clusters are defined), and thus even if clustering makes a substantial difference in the magnitude of the standard errors. For example, if workers are sampled
at random from a some population of interest and then randomly assigned to a job training
program, clustering the standard errors at, say, the industry, county, or state level can result
in standard errors that are unnecessarily conservative, often by a wide margin. Similarly, in a
judge-leniency design—where defendants are randomly assigned to judges—standard errors
should not be clustered at the level of the judge [Chyn, Frandsen, and Leslie, 2022]. If the
sample represents a large fraction of the population and treatment effects are heterogeneous
across units, robust standard errors are also conservative. If the data contains information
on attributes of the units that are correlated with unit-level treatment effects, the methods
in Abadie et al. [2020] can be applied to obtain less conservative standard errors.
Next, consider the case of clustered assignment, and where we either have random sampling or we observe the entire population. This is one case where clustering becomes relevant,
although conventional cluster standard errors can be extremely conservative. If assignment
is perfectly clustered so that units that belong to the same cluster have the same treatment
assignment, there is no improvement from using the CCV variance and the TSCB variance
estimator is not applicable. If assignment is partially clustered—so there is variation in
30

<!-- page 31 -->
treatment assignment within clusters—and cluster sizes are large, the CCV and TSCB can
be applied and can produce standard errors considerably smaller than the usual clustered
standard errors.
Another reason to cluster standard errors is cluster sampling. The case with qk close to
zero is sometimes relevant, especially when the sample is a panel data on individuals or a
cross-section of families, and the individuals or families in the sample are a small fraction
of the population. Then, the clustered variance estimator of the least squares estimator is
asymptotically correct regardless of whether the treatment assignment is clustered or not.
The same result holds when clusters are large (e.g., states), qk is a substantial fraction of
the clusters in the population, but pk is small—so the sample includes only a small number
of units from each cluster. In other cases, cluster standard errors can be considerably larger
than necessary. If cluster sizes are large and there is treatment variation within clusters,
CCV and TSCB can substantially reduce the magnitude of standard errors.
The insights in this article are relevant in other common settings of empirical economics.
Consider a setting with unit-level panel data on outcomes and a treatment that is implemented on the same period for all units in the treatment group. The difference-in-difference
estimator is in this case equal to the coefficient on the treatment variable in a cross-sectional
regression of the change in unit-level average outcomes between the post-treatment and the
pre-treatment periods on a constant and a treatment indicator that takes value one if the
unit belongs to the treatment group. If treatment assignment is random across units, and the
sample includes a random subset of the population or the entire population, robust standard
error provide inference that is generally conservative if the sample is large relative to the
population and treatment effects are heterogeneous. Here too, the methods in Abadie et al.
[2020] can be applied to correct the bias of robust standard errors. With clustered assignment, one should cluster the standard errors at the level of assignment—for example, cluster
at the village level if all farmers are assigned the same treatment status. Adding group-level
fixed effects to this regression allows for group-specific linear trends in the underlying potential outcomes series but does not change the answer to the question whether one needs to
31

<!-- page 32 -->
adjust for clustering. Under partially clustered assignment, CCV and TSCB standard errors
can continue to provide substantial improvements over conventional cluster standard errors
for the fixed effect estimator.
8. Conclusion
This article proposes a research framework aimed to address a question of central relevance
for empirical practice: when and how we should cluster standard errors. Like in Abadie et al.
[2020], we shift the attention from estimation of features of a data-generating process (i.e.,
infinite superpopulation) to estimation of average treatment effects of the finite population
at hand. We show that, in this framework, the decision on when and how to cluster standard
errors depends on the nature of the sampling and the assignment processes only, and not on
the presence of within-cluster error components in the outcome variable. We derive expressions of the large sample variances of the OLS and FE estimators of the average treatment
effect for a setting with clustered sampling and where assignment is random within clusters
with assignment probabilities that may vary across clusters. For this setting, we demonstrate
that robust standard errors can be too small and conventional cluster standard errors can
be unnecessarily large. We propose two novel procedures, CCV and TSCB, that can be used
to calculate more precise standard errors in settings with large clusters and where there is
enough variation in treatment assignment within cluster (so that average treatment effects
within clusters can be precisely estimated). While CCV and TSCB are designed for this particular setting, the general principles of the framework remain valid for other settings and
estimators. If sampling is not clustered, standard errors should be clustered at the treatment
assignment level because the estimand of interest depends on potential outcomes and the
sampling of potential outcomes is determined only by the assignment mechanism. When
the fraction of sampled clusters is non-negligible and there is variation in average treatment
effects across clusters, conventional clustered standard errors may be off, and we provide an
analytical framework that can be applied to derive appropriate standard errors. When sampling and assignment are random, clustering standard errors is not appropriate regardless
of the structure of the covariance of the outcomes across the units in the population. In
32

<!-- page 33 -->
this setting, if there is substantial treatment effect heterogeneity and the sample represents
a large fraction of the population of interest, robust standard errors are conservative in large
samples. This bias can be corrected using the methods in Abadie et al. [2020]. Deriving
standard error formulas for sampling and assignment processes other than the ones featured
in this article is an important avenue for future research. Rambachan and Roth [2022] is a
recent contribution in this direction. In addition, in the present article we have restricted
the analysis to linear estimators (least squares and fixed effects). Xu [2019] extends the ideas
and framework of this article to analyze the distribution of non-linear estimators.
References
Alberto Abadie, Susan Athey, Guido W Imbens, and Jeffrey M Wooldridge. Sampling-based
versus design-based uncertainty in regression analysis. Econometrica, 88(1):265–296, 2020.
Manuel Arellano. Practitioners corner: Computing robust standard errors for within-groups
estimators. Oxford Bulletin of Economics and Statistics, 49(4):431–434, 1987.
Marianne Bertrand, Esther Duflo, and Sendhil Mullainathan. How much should we trust
differences-in-differences estimates? The Quarterly Journal of Economics, 119(1):249–275,
2004.
A Colin Cameron and Douglas L Miller. A practitioner’s guide to cluster-robust inference.
Journal of Human Resources, 50(2):317–372, 2015.
Min-Te Chao and Shaw-Hwa Lo. A bootstrap method for finite population. Sankhy¯a: The
Indian Journal of Statistics, Series A, pages 399–405, 1985.
Eric Chyn, Brigham Frandsen, and Emily Leslie. Examiner and judge designs in economics:
A practitioner’s guide. 2022. Working paper.
Jessica Cohen and Pascaline Dupas. Free distribution or cost-sharing? evidence from a
randomized malaria prevention experiment. The Quarterly Journal of Economics, 125(1):
1–45, 2010.
33

<!-- page 34 -->
F. Eicker. Asymptotic normality and consistency of the least squares estimators for families
of linear regressions. Annals of Mathematical Statististics, 34(2):447–456, 06 1963. doi:
10.1214/aoms/1177704156.
Matthew Gentzkow and Jesse M. Shapiro. Preschool television viewing and adolescent test
scores: Historical evidence from the coleman study. The Quarterly Journal of Economics,
123(1):279–323, 2008.
Peter J Huber. The behavior of maximum likelihood estimates under nonstandard conditions.
In Proceedings of the fifth Berkeley symposium on mathematical statistics and probability,
volume 1, pages 221–233. University of California Press, 1967.
Guido Imbens and Konrad Menzel. A causal bootstrap. Annals of Statistics, 49(3):1460–
1488, 2021.
Guido W Imbens and Donald B Rubin. Causal Inference in Statistics, Social, and Biomedical
Sciences. Cambridge University Press, 2015.
Leslie Kish. Survey Sampling. Wiley-Interscience, 1995.
Kung-Yee Liang and Scott L Zeger. Longitudinal data analysis using generalized linear
models. Biometrika, 73(1):13–22, 1986.
James G MacKinnon, Morten Ørregaard Nielsen, and Matthew Webb. Cluster-robust inference: A guide to empirical practice. 2021. Working paper.
Konrad Menzel. Bootstrap with cluster-dependence in two or more dimensions. Econometrica, 89(5):2143–2188, 2021.
Brent R Moulton. Random group effects and the precision of regression estimates. Journal
of econometrics, 32(3):385–397, 1986.
Brent R Moulton. Diagnostics for group effects in regression analysis. Journal of Business
& Economic Statistics, 5(2):275–282, 1987.
34

<!-- page 35 -->
Jerzey Neyman. On the application of probability theory to agricultural experiments. Essay
on principles. Section 9. Statistical Science, 5(4):465–472, 1923/1990.
Ashesh Rambachan and Jonathan Roth. Design-based uncertainty for quasi-experiments.
2022. arXiv:2008.00602.
Steven K Thompson. Sampling. John Wiley & Sons, 2012.
Halbert White. A heteroskedasticity-consistent covariance matrix estimator and a direct test
for heteroskedasticity. Econometrica, pages 817–838, 1980.
Ruonan Xu. Asymptotic properties of M-estimators with finite populations under cluster
sampling and cluster assignment. 2019. Working paper.
35

<!-- page 36 -->
On-Line Appendix
When Should You Adjust Standard Errors for Clustering?
Alberto Abadie, Susan Athey, Guido W. Imbens, and Jeffrey M. Wooldridge
Current version: 0, 0
A.1. Setting and notation
We have a sequence of populations indexed by k. The k-th population has nk units, indexed by
i“ 1,...,nk. The population is partitioned into mk strata or clusters. Let mk,i P t1,...,mku
denote the stratum that unit i of population k belongs to. The number of units in cluster m of
population k is nk,m ě 1. For each unit, i, there are two potential outcomes, yk,ip1q and yk,ip0q,
corresponding to treatment and no treatment. The parameter of interest is the population average
treatment effect
1
τk“
nk
nk
ÿ
i“1
pyk,ip1q ´ yk,ip0qq.
The population treatment effect by cluster is
1
τk,m“
nk,m
nk
ÿ
i“1
1tmk,i“ mupyk,ip1q ´ yk,ip0qq.
Therefore,
mk
τk“
ÿ
nk,m
nk
τk,m.
m“1
We will assume that potential outcomes, yk,ip1q and yk,ip0q, are bounded in absolute value, uniformly for all pk,iq.
We next describe the two components of the stochastic nature of the sample. There is a stochastic
binary treatment for each unit in each population, Wk,i P t0,1u. The realized outcome for unit i
in population k is Yk,i“ yk,ipWk,iq. For a random sample of the population, we observe the triple
pYk,i,Wk,i,mk,iq. Inclusion in the sample is represented by the random variable Rk,i, which takes
value one if unit i belongs to the sample, and value zero if not.
The sampling process that determines the values of Rk,i is independent of the potential outcomes
and the assignments. It consists of two stages. First, clusters are sampled with cluster sampling
probability qk P p0,1s. Second, units are sampled from the subpopulation consisting of all the
sampled clusters, with unit sampling probability equal to pk P p0,1s. Both qk and pk may be equal
to one, or close to zero. If qk“ 1, we sample all clusters. If pk“ 1, we sample all units from the
sampled clusters. If qk“ pk“ 1, all units in the population are sampled.
The assignment process that determines the values of Wk,i also consists of two stages. In the first
stage, for cluster m in population k, an assignment probability Ak,m P r0,1s is drawn randomly
from a distribution with mean µk, bounded away from zero and one uniformly in k, and variance
σ2
k, independently for each cluster. The variance σ2
k is key. If it is zero, we have random assignment
across clusters. For positive values of σ2
k we have correlated assignment within the clusters. Because
A2
k,m ď Ak,m, it follows that σ2
k is bounded above by µkp1´µkq and that the bound is attained when
1

<!-- page 37 -->
Ak,m can only take values zero or one (so all units within a cluster have the same values for the
treatment). In the second stage, each unit in cluster mis assigned to the treatment independently,
with cluster-specific probability Ak,m.
A.2. Base case: Difference in means
Let
Nk,1 “
nk
ÿ
i“1
nk
Rk,iWk,i and Nk,0 “
ÿ
Rk,ip1´ Wk,iq
i“1
be the number of treated and untreated units in the sample, respectively. The total sample size is
Nk“ Nk,1 ` Nk,0. We consider the simple difference of means between treated and non-treated,
which is obtained as the coefficient on the treatment indicator in a regression of the outcome on a
constant and the treatment,
p
τk“
1
Nk,1 _ 1
nk
ÿ
i“1
Rk,iWk,iYk,i´
1
Nk,0 _ 1
nk
ÿ
i“1
Rk,ip1´ Wk,iqYk,i.
We make the following assumptions about the sampling process and the cluster sizes: (i)qkmk Ñ 8,
(ii) lim infkÑ8 pk minm nk,m ą 0, and (iii) lim supkÑ8 maxm nk,m{ minm nk,m ă 8. The first
assumption implies that the expected number of sampled clusters goes to infinity as kincreases. The
second assumption implies that the average number of observations sampled per cluster, conditional
on the cluster being sampled, does not go to zero. The third assumption restricts the imbalance
between the number of units across clusters. Notice that assumptions (i) and (ii) imply nkpkqk Ñ
8, so the sample size becomes larger in expectation as k increases.
A.2.1. Large k distribution
Let αk “ p1{nkq řnk
i“1 yk,ip0q and τk “ p1{nkq řnk
i“1pyk,ip1q ´ yi,kp0qq, uk,ip1q “ yk,ip1q ´ pαk ` τkq,
and uk,ip0q “ yk,ip0q ´ αk. Notice that,
nk
ÿ
i“1
uk,ip1q “nk
ÿ
i“1
uk,ip0q “ 0.
This implies
where
p
ak,1 “
p
ak,0 “
?nkpkqkpp
τk´ τkq “ bk,1
p
bk,1
p
ak,1´
bk,0
p
bk,0
p
ak,0,
1
?nkpkqkµk
nk
ÿ
i“1
pRk,iWk,i´ pkqkµkquk,ip1q,
1
?nkpkqkp1´ µkq
nk
ÿ
i“1
pRk,ip1´ Wk,iq ´ pkqkp1´ µkqquk,ip0q,
2

<!-- page 38 -->
p
p
bk,1 “ pNk,1 _ 1q{nk,
bk,0 “ pNk,0 _ 1q{nk, bk,1 “ pkqkµk and bk,0 “ pkqkp1´ µkq. We will first
derive the large sample distribution of
p
ak“
“
p
ak,1´
mk
ÿ
m“1
p
ak,0
`ξk,m,1´ ξk,m,0˘,
where
ξk,m,1 “
1
?nkpkqkµk
nk
ÿ
i“1
1tmk,i“ mu`Rk,iWk,i´ pkqkµk˘uk,ip1q,
and
1
ξk,m,0 “
?nkpkqkp1´ µkq
nk
ÿ
i“1
1tmk,i“ mu`Rk,ip1´ Wk,iq ´ pkqkp1´ µkq˘uk,ip0q.
Notice that Erξk,m,1s “ Erξk,m,0s “ 0. Moreover, notice that the terms ξk,m,1´ ξk,m,0 are independent across clusters, m. In addition,
Erξ2
k,m,1s “ 1
nk
nk
ÿ
i“1
1tmk,i“ mu 1´ pkqkµk
µk
u2
k,ip1q
2
`
nk
nk´1
ÿ
i“1
nk
ÿ
j“i`1
1tmk,i“ mk,j“ mu pkpσ2
k ` µ2
kp1´ qkqq
uk,ip1quk,j p1q.
µ2
k
Erξ2
k,m,0s “ 1
nk
nk
ÿ
i“1
1tmk,i“ mu 1´ pkqkp1´ µkq
p1´ µkq u2
k,ip0q
2
`
nk
nk´1
ÿ
i“1
nk
ÿ
j“i`1
1tmk,i“ mk,j“ mu pkpσ2
k ` p1´ µkq2p1´ qkqq
p1´ µkq2 uk,ip0quk,j p0q,
and
Erξk,m,1ξk,m,0s “ ´ 1
nk
nk
ÿ
i“1
1tmk,i“ mupkqkuk,ip1quk,ip0q
1
`
nk
nk´1
ÿ
i“1
nk
ÿ
j“i`1
1tmk,i“ mk,j“ mu pkpµkp1´ µkqp1´ qkq ´ σ2
kq
µkp1´ µkq `uk,ip0quk,j p1q ` uk,ip1quk,j p0q˘.
We obtain:
nkErpξk,m,1´ ξk,m,0q2s
1
“
µk
nk
ÿ
i“1
nk´1
ÿ
i“1
1tmk,i“ muu2
k,ip1q ` 1
1´ µk
nk
ÿ
i“1
1tmk,i“ muu2
k,ip0q
` 2pk
nk
ÿ
j“i`1
1tmk,i“ mk,j“ mu´uk,ip1quk,j p1q ` uk,ip0quk,j p0q ´ uk,ip0quk,j p1q ´ uk,ip1quk,j p0q¯
3

<!-- page 39 -->
´ pkqk˜nk
ÿ
i“1
nk´1
nk
` 2
ÿ
ÿ
i“1
j“i`1
` 2pkσ2
ÿ
k˜nk´1
nk
ÿ
i“1
j“i`1
1tmk,i“ mu`u2
k,ip1q ` u2
k,ip0q ´ 2uk,ip1quk,ip0q˘
1tmk,i“ mk,j“ mu`uk,ip1quk,j p1q ` uk,ip0quk,j p0q ´ uk,ip0quk,j p1q ´ uk,ip1quk,j p0q˘¸
1tmk,i“ mk,j“ muˆuk,ip1quk,j p1q
uk,ip0quk,j p0q
uk,ip0quk,j p1q
`
µ2
k
p1´ µkq2 `
µkp1´ µkq `
uk,ip1quk,j p0q
µkp1´ µkq ¸.
Therefore,
nkErpξk,m,1´ ξk,m,0q2s
1
nk
“
ÿ
1tmk,i“ muu2
k,ip1q ` 1
nk
ÿ
1tmk,i“ muu2
k,ip0q
µk
1´ µk
i“1
i“1
` pk«˜nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
´
nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘2ff
´ pkqk˜nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
` pkσ2
k«˜nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
uk,ip0q
`
µk
1´ µk ˙¸2
´
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙2ff.
Let vk“ řmk
m“1 Erpξk,m,1´ ξk,m,0q2s, then
nk
nkvk“
i“1 ˆu2
k,ip1q
u2
k,ip0q
ÿ
`
µk
1´ µk ˙
mk
` pk
m“1 «˜nk
ÿ
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
´
nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘2ff
mk
´ pkqk
m“1 ˜nk
ÿ
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
mk
` pkσ2
k
m“1 «˜nk
ÿ
ÿ
i“1
1tmk,i“ muˆuk,ip1q
uk,ip0q
`
µk
1´ µk ˙¸2
´
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙2ff.
Alternatively, we can write this expression as
nk
nkvk“
i“1 ˆu2
k,ip1q
ÿ
`
µk
u2
k,ip0q
1´ µk ˙
nk
´ pk
ÿ
`uk,ip1q ´ uk,ip0q˘2
´ pkσ2
k
`
i“1
` pkp1´ qkqmk
m“1 ˜nk
ÿ
ÿ
i“1
nk
ÿ
i“1 ˆuk,ip1q
µk
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
uk,ip0q
1´ µk ˙2
4

<!-- page 40 -->
` pkσ2
k
mk
ÿ
m“1 ˜nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙¸2
.
The sum of the first three terms is minimized for pk“ 1 and σ2
k“ µkp1´ µkq, in which case this
sum is equal to zero. Therefore,
vk ě ppk min
m
` ppk min
m
nk,mqp1´ qkqmk
ÿ
nk,m
m“1
nk ˜1
nk,m
nk,mq σ2
k
mk
ÿ
m“1
nk,m
nk ˜1
nk,m
nk
ÿ
i“1
nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
1tmk,i“ muˆuk,ip1q
µk
uk,ip0q
`
1´ µk ˙¸2
. (A.1)
We will assume that lim infkÑ8pp1´ qkq _ σ2
kq ą 0, so either sampling or assignment or both are
correlated within cluster. (We study the case qk“ 1 and σ2
k“ 0 separately below.) In addition,
assume (i) lim infkÑ8p1´ qkq ą 0 and
lim inf
kÑ8
mk
ÿ
m“1
nk,m
nk ˜1
nk,m
nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
ą 0, (A.2)
or (ii) lim infkÑ8 σ2
k ą 0 and
lim inf
kÑ8
mk
ÿ
m“1
nk,m
nk ˜1
nk,m
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙¸2
ą 0. (A.3)
Equation (A.2) would be violated if, as kincreases, there is no variation in average treatment effects
across clusters. Equation (A.3) would be violated if as k increases there is no variation in average
potential outcomes across clusters. If equations (A.2) and (A.3) hold, vk is bounded below by a
term of order at least pk minm nk,m. Recall our assumption, lim infkÑ8 pk minm nk,m ą 0, so the
average number of observations sampled per cluster, conditional on the cluster being sampled, does
not go to zero. Then,
lim inf
kÑ8
vk ą 0.
To obtain a CLT, we will check Lyapunov’s condition,
lim
kÑ8
mk
ÿ
m“1
1
1`δ{2
v
k
Er|ξk,m,1´ ξk,m,0|2`δ s “ 0,
for some δ ą 0. Because potential outcomes are uniformly bounded and µk is uniformly bounded
away from zero, we obtain
n2`δ
|ξk,m,1|2`δ ď c
k,m
pnkpkqkq1`δ{2
ˇ ˇ ˇ ˇ ˇ
1
nk,m
nk
ÿ
i“1
1tmk,i“ mu|Rk,iWk,i´ pkqkµk|
ˇ ˇ ˇ ˇ ˇ
2`δ
,
where c is some generic positive constant, whose value may change across equations. Consider
δ“ 1, and let
S3
k,m,1 “ E» –
ˇ ˇ ˇ ˇ ˇ
1
nk,m
nk
ÿ
i“1
1tmk,i“ mu|Rk,iWk,i´ pkqkµk|
ˇ ˇ ˇ ˇ ˇ
3fi fl
5

<!-- page 41 -->
ď
`
`
1
n3
nk,mEr|Rk,iWk,i´ pkqkµk|3s
k,m
3
n3
nk,mpnk,m´ 1qE“|Rk,iWk,i´ pkqkµk|2|Rk,j Wk,j´ pkqkµk|ˇ ˇmk,i“ mk,j“ m‰
k,m
6
n3
k,m ˆnk,m
3 ˙E“|Rk,iWk,i´ pkqkµk||Rk,j Wk,j´ pkqkµk||Rk,tWk,t´ pkqkµk|ˇ ˇmk,i“ mk,j“ mk,t“ m‰,
for i‰ j ‰ t. (The second and third terms on the left-hand side of last equation only appear when
nk,m ě 2 and nk,m ě 3, respectively) As a result,
S3
k,m,1 ď c˜pkqk
` p2
kqk
n2
k,m
nk,m
` p3
kqk¸
ď cp3
kqk ˜1
`
p2
k minm n2
k,m
1
pk minm nk,m
` 1¸.
Because lim infkÑ8 pk minm nk,m ą 0, for large enough k we obtain,
p3
kqkn3
Er|ξk,m,1|3s ď c
k,m
pnkpkqkq3{2 ,
and the same bound applies for Er|ξk,m,0|3s. Notice that
mk
ÿ
m“1
Er|ξk,m,1´ ξk,m,0|3s ďmk
ÿ
m“1
mk
“
ÿ
m“1
mk
` 3
ÿ
m“1
Erp|ξk,m,1| ` |ξk,m,0|q3s
Er|ξk,m,1|3s `mk
ÿ
m“1
Er|ξk,m,0|3s
Er|ξk,m,1|2|ξk,m,0|s ` 3
mk
ÿ
m“1
Er|ξk,m,1||ξk,m,0|2s.
Now, H¨older’s inequality implies that
p3
kqk řmk
m“1 n3
k,m
3{2
v
k pnkpkqkq3{2
ÝÑ 0, (A.4)
is sufficient for the Lyapunov condition to hold. Because maxm nk,m{ minm nk,m is bounded asymptotically, we obtain,
lim sup
kÑ8
p3
kqk řmk
m“1 n3
k,m
3{2
v
k pnkpkqkq3{2
p3
kqkmk maxm n3
k,m
ď lim sup
kÑ8
c
pp2
kqkmk minm n2
k,mq3{2
ď lim sup
kÑ8 ˆmaxm nk,m
minm nk,m ˙3
c
?qkmk
and so the Lyapunov condition holds. As a result, we obtain
p
ak{?vk
d
ÝÑ Np0,1q.
6
“ 0,

<!-- page 42 -->
We will next prove that bothp
ak,1{?vk andp
ak,0{?vk are Opp1q.
Erp
a2
k,1s “ 1
nkpkqk
1
µ2
k
mk
ÿ
m“1
E» –˜nk
ÿ
i“1
1tmk,i“ mupRk,iWk,i´ pkqkµkquk,ip1q¸2fi fl
1
ď c
nkpkqk
“ c´1 `
mk
ÿ
m“1
mk
ÿ
m“1
`nk,mpkqk ` nk,mpnk,m´ 1qp2
kqk˘
nk,mpnk,m´ 1qpk
nk ¯.
Therefore,
Erpp
ak,1{?vkq2s ď c˜1
pk minm nk,m
`
mk
ÿ
m“1
pmaxm nk,mqpnk,m´ 1qpk
nkpk minm nk,m ¸.
Because lim sup maxm nk,m{ minm nk,m ă 8, we obtain lim supkÑ8 Erpp
ak,1{vkq2s ă 8. As a result,
p
ak,1{?vk is Opp1q.
Letr
bk,1 “ Nk,1{nk. Consider k large enough, so pk minm nk,m is bounded away from zero, making
r
bk,1{bk,1 well-defined. Notice that Err
bk,1{bk,1s “ 1 and
varpr
bk,1{bk,1q “ 1
pnkpkqkµkq2
“
ď
ď
mk
ÿ
m“1
E» –˜nk
ÿ
i“1
nkpkqkµkp1´ pkqkµkq
mk
pnkpkqkµkq2 `
ÿ
m“1
1´ pkqkµk
nkpmaxm nk,m´ 1qp2
k qk
` c
nkpkqkµk
1´ pkqkµk
pnkpkqkq2
` cpmaxm nk,m´ 1q
1
nkpkqkµk
min nk,m
qkmk
1tmk,i“ mupRk,iWk,i´ nkpkqkµkq¸2fi fl
nk,mpnk,m´ 1qp2
kqkpσ2
k ` p1´ qkqµ2
kq
pnkpkqkµkq2
ÝÑ 0.
r
This implies
bk,1{bk,1
p
Ñ 1. Analogous calculations yield
r
b0,k{b0,k
p
Ñ 1. For large enough k,
r
bk,1{bk,1 “ 0 if and only if Nk,1 “ 0, which implies PrpNk,1 “ 0q Ñ 0. It follows that, for
large enough k,
Prp|r
bk,1{bk,1´
p
bk,1{bk,1| “ 0q “ PrpNk,1 ą 0q ÝÑ 1
andp
bk,1{bk,1
p
Ñ 1. Using analogous calculations, we obtain
p
bk,0{bk,0
p
Ñ 1. As a result,
?nkpkqkpp
τk´ τkq{v
1{2
k“
“
“
bk,1
p
bk,1
p
ak,1
bk,0
p
ak,0
´
1{2
p
v
k
bk,0
1{2
v
k
p
ak
1{2
v
k
` ˜bk,1
p
bk,1
´ 1¸ p
ak,1
1{2
v
k
p
ak{?vk ` Opp1q.
´ ˜bk,0
p
bk,0
´ 1¸ p
ak,0
1{2
v
k
7

<!-- page 43 -->
Therefore,
Using
r
b1,k{b1,k
p
Ñ 1 andr
b0,k{b0,k
?nkpkqkpp
τk´ τkq{v
1{2
k
d
ÝÑ Np0,1q.
p
Ñ 1, it is easy to show Nk{pnkpkqkq p
Ñ 1, which implies
aNkpp
τk´ τkq{v
1{2
k
d
ÝÑ Np0,1q.
We will next consider the case of qk“ 1 and σ2
k“ 0, where no clustering is required. Consider
1
ϑk,i,1 “
?nkpkµk `Rk,iWk,i´ pkµk˘uk,ip1q
and
1
ϑk,i,0 “
?nkpkp1´ µkq `Rk,ip1´ Wk,iq ´ pkp1´ µkq˘uk,ip0q.
Redefine now vk“ řnk
i“1 E“pϑk,i,1´ ϑk,i,0q2‰. Then,
1
vk“
nk
nk
i“1 ˆu2
k,ip1q
ÿ
µk
`
u2
k,ip0q
1´ µk ˙´ pk
1
nk
nk
ÿ
i“1
`uk,ip1q ´ uk,ip0q˘2
.
Notice that vk is minimized for pk“ 1, in which case
vk“
1
nk
ÿ
nk
i“1 ˆu2
k,ip1q
µk
1
nk
“
ÿ
nk
i“1 ˆ1´ µk
µk
“ µkp1´ µkq 1
nk
`
u2
k,ip0q
1´ µk ˙´
u2
k,ip1q ` µk
1´ µk
“ µkp1´ µkq 1
nk
nk
i“1 ˆu2
k,ip1q
ÿ
µ2
k
nk
ÿ
i“1 ˆuk,ip1q
µk
`
`
1
nk
ÿ
`uk,ip1q ´ uk,ip0q˘2
nk
i“1
u2
k,ip0q ` 2uk,ip1quk,ip0q˙
u2
k,ip0q
p1´ µkq2 ` 2
uk,ip1quk,ip0q
µkp1´ µkq ˙
uk,ip0q
1´ µk ˙2
.
Therefore, the assumption
1
lim inf
kÑ8
nk
nk
ÿ
i“1 ˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙2
ą 0
is enough for lim infkÑ8 vk ą 0. Notice now that
Er|ϑk,i,1|3s ď 1
pnkpkq3{2 Er|Rk,iWk,i´ pkµk|3s
1
“
pnkpkq3{2 p1´ pkµkq3pkµk ` ppkµkq3p1´ pkµkq
pk
ď c
pnkpkq3{2 ,
8

<!-- page 44 -->
and the same bound holds for Er|ϑk,i,0|3s. Therefore, for the Lyapunov condition to hold, it is
enough that
nkpk
1
“
ÝÑ 0,
pnkpkq3{2
?nkpk
or nkpk Ñ 8. That is, assumptions (i)-(iii), which we used for the clustered case, are replaced by
nkpk Ñ 8.
A.2.2. Estimation of the variance
Letp
Uk,i“ Yk,i´
p
p
αk´
τkWk,i be the residuals from the regression of Yk,i or a constant and Wk,i.
Here,p
αk is the coefficient on the constant regressor equal to one, andp
τk is the coefficient on Wk,i.
We have already shown v´1{2
k pp
τk´ τkq “ Opp1{?nkpkqkq. The same is true aboutp
αk (e.g., apply
p
p
the proof forp
τk after replacing each yk,ip1q with a zero). Define
Σk“ řmk
m“1
Σk,m, where
p
Σk,m“ ˜nk
ÿ
i“1
1tmk,i“ muRk,i ˜ p
Uk,i
Wk,i
Uk,i ¸¸ ˜nk
p
ÿ
i“1
1tmk,i“ muRk,i ˜ p
Uk,i
Wk,i
Uk,i ¸¸1
p
.
Also, let
p
Qk“
nk
ÿ
i“1
Rk,i ˆ1
Wk,i ˙ ˆ1
Wk,i ˙1
,
and z“ p0,1q1 . Then, the cluster estimator of the variance of ?Nkpp
τk´ τkq is
p
Vcluster
k“ Nkz1 p
p
p
Q´1
k
Σk
Q´1
k z.
Notice that
In addition,
var˜nk
ÿ
i“1
pnkpkqkq´1Erp
Qks “ ˆ1 µk
µk µk ˙.
1
p
Qkp2,2q “ 1
mk
ÿ
nkpkqk
nkpkqk
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,i.
1tmk,i“ muRk,iWk,i¸“ nk,mpkqkµkp1´ pkqkµkq
` nk,mpnk,m´ 1qp2
kqkpσ2
k ` µ2
kp1´ qkqq.
Therefore, under conditions (i)-(iii), we obtain
var˜1
nkpkqk
p
Qkp2,2q¸ď
“ c
ď c
c
nkpkqk ˜1 ` pkpmaxm nk,m´ 1q¸
maxm nk,m
` Op1q
nkqk
maxm nk,m
1
` Op1q ÝÑ 0.
minm nk,m
qkmk
9

<!-- page 45 -->
Analogous calculations yield varppnkpkqkq´1p
Qkp1,1qq Ñ 0. Therefore,
1
p
nkpkqk
Qk“ ˆ1 µk
µk µk ˙` Opp1q
and
1
p
nkqkpk
Q´1
k“ Hk ` Opp1q, where Hk“
µkp1´ µkq ˆµk´µk
´µk 1 ˙.
Now, let Uk,i“ Yk,i´ αk´ τkWk,i“ Wk,iuk,ip1q ` p1´ Wk,iquk,ip0q. Notice that
v´1{2
k max
i“1,...,nk
|p
Uk,i´ Uk,i| ď v´1{2
k |p
αk´ αk| ` v´1{2
k |p
τk´ τk| “ Opp1{?nkpkqkq.
Define Σk“ řmk
m“1 Σk,m, where
Σk,m“ ˜nk
ÿ
i“1
1tmk,i“ muRk,i ˆUk,i
Wk,iUk,i ˙¸ ˜nk
ÿ
i“1
1tmk,i“ muRk,i ˆUk,i
Wk,iUk,i ˙¸1
We will show
1
pp
Σk´ Σkq p
ÝÑ 0.
nkpkqkvk
.
Notice that
p
Σk,mp2,2q ´ Σk,mp2,2q “ ˜nk
ÿ
i“1
` 2˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipp
Uk,i´ Uk,iq¸2
1tmk,i“ muRk,iWk,iUk,i¸˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipp
Uk,i´ Uk,iq¸.
Therefore,
1
1
mk
|p
Σkp2,2q ´ Σkp2,2q| ď c
ÿ
nkpkqkvk
nkpkqkvk
m“1 ˜nk
ÿ
i“1
ˆ ˜max
|p
Uk,i´ Uk,i|2 ` max
i“1,...,nk
1tmk,i“ muRk,iWk,i¸2
|p
Uk,i´ Uk,i|¸.
i“1,...,nk
p
The same expression holds for the off-diagonal elements of
Σk,m´ Σk,m. Forp
Σk,mp1,1q ´ Σk,mp1,1q,
the expression holds once we replace each Wk,i with a one. Let } ¨ } be the Frobenius norm of a
matrix. Then,
1
nkpkqkvk
}p
Σk´ Σk} ď c
1
mk
nkpkqkvk
m“1 ˜nk
ÿ
ÿ
i“1
ˆ ˜max
i“1,...,nk
1tmk,i“ muRk,i¸2
|p
Uk,i´ Uk,i|2 ` max
i“1,...,nk
|p
Uk,i´ Uk,i|¸.
10

<!-- page 46 -->
We will prove that the right-hand side of the previous equation converges to zero in probability.
We will factorize each term into a expression that is bounded in probability and one that converges
to zero in L1.
ÿ
E«mk
m“1 ˜nk
ÿ
i“1
1tmk,i“ muRk,i¸2ffď nkpkqk ` nkpmax
m
nk,m´ 1qp2
kqk.
For the first term, notice that
max
i“1,...,nk
|p
Uk,i´ Uk,i|2 nkpkqk ` nkpmaxm nk,m´ 1qp2
kqk
nkpkqkvk
“
nkpkqk
vk
max
i“1,...,nk
|p
Uk,i´ Uk,i|2˜nkpkqk ` nkpmaxm nk,m´ 1qp2
kqk
pnkpkqkq2 ¸
ď
nkpkqk
vk
max
i“1,...,nk
|p
Uk,i´ Uk,i|2˜1
`
nkpkqk
maxm nk,m´ 1
minm nk,m
1
qkmk ¸
“ Opp1q Op1q.
For the second term, using the fact that vk is greater or equal to pk minm nk,m ą 0 times a term
with limit inferior that is bounded away from zero, we obtain
max
i“1,...,nk
|p
Uk,i´ Uk,i| nkpkqk ` nkpmaxm nk,m´ 1qp2
kqk
nkpkqkvk
“ ´nkpkqk
vk ¯1{2
max
i“1,...,nk
|p
Uk,i´ Uk,i|˜nkpkqk ` nkpmaxm nk,m´ 1qp2
kqk
pnkpkqkq3{2v
k ¸
1{2
ď ´nkpkqk
vk ¯1{2
max
i“1,...,nk
|p
Uk,i´ Uk,i|˜1
maxm nk,m´ 1
1
pnkpkqkvkq1{2 `
minm nk,m
pqkmkq1{2 ¸
“ Opp1q Op1q.
As a result, we obtain
1
nkpkqkvk
}p
Σk´ Σk} “ Opp1q.
Notice that
nkpkqk
vk
p
p
p
Q´1
k
Σk
Q´1
k´ Hk
Σk
Hk“ Hk
nkpkqkvk
Σk
nkpkqkvk ´nkpkqk
p
Q´1
k´ Hk¯
p
` ´nkpkqk
p
Q´1
k´ Hk¯Σk
nkpkqkvk ´nkpkqk
p
Q´1
k ¯` ´nkpkqk
p
Q´1
k ¯
Σk´ Σk
nkpkqkvk ´nkpkqk
p
Q´1
k ¯.
Therefore, to show that the left-hand side of the last equation is Opp1q, it is only left to show that
Σk{pnkpkqkvkq is Opp1q. We will prove this next. Notice that
1
1
mk
}Σk} ď c
ÿ
nkpkqkvk
nkpkqkvk
m“1 ˜nk
ÿ
i“1
1tmk,i“ muRk,i¸2
.
11

<!-- page 47 -->
Therefore,
E«1
nkpkqkvk
}Σk}ffď c
1
nkpkqkvk ˜nkpkqk ` nkpmax
m
nk,m´ 1qp2
kqk¸.
Then,
E«1
nkpkqkvk
}Σk}ffď c˜1
vk
` pkpmaxm nk,m´ 1q
pk minm nk,m ¸ă 8.
We, therefore, obtain,
nkpkqk
p
p
p
Σk
Q´1
k
Σk
Q´1
k´ Hk
vk
nkpkqkvk
Because Nk{pnkpkqkq p
Ñ 1, we obtain
Hk
p
ÝÑ 0.
p
Vcluster
k {vk“ z1Hk
“
Σk
Hkz` Opp1q
nkpkqkvk
1
nkpkqkvk ˆ1
µkp1´ µkq ˙2 mk
ÿ
m“1 ˆnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙2
Recall that U2
k,i“ u2
k,ip1qWk,i ` u2
k,ip0qp1´ Wk,iq. Notice that
E„ˆnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙2
nk
“
ÿ
1tmk,i“ mupkqkµkp1´ µkq´p1´ µkqu2
k,ip1q ` µku2
k,ip0q¯
i“1
nk´1
nk
` 2
ÿ
ÿ
1tmk,i“ mk,j“ mup2
kqk”pσ2
k ` µ2
kqp1´ µkq2uk,ip1quk,j p1q
i“1
j“i`1
` µkp1´ µkqpσ2
k´ µkp1´ µkqqpuk,ip0quk,j p1q ` uk,ip1quk,j p0qq
` pσ2
k ` p1´ µkq2qµ2
kuk,ip0quk,j p0qı.
vcluster
k“
1
nkpkqk ˆ1
µkp1´ µkq ˙2 mk
ÿ
m“1
E„ˆnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙2.
` Opp1q.
Let
Then,
nkvcluster
k“
nk
i“1 ˆu2
k,ip1q
u2
k,ip0q
ÿ
`
µk
1´ µk ˙
mk
` pk
ÿ
m“1 «˜nk
ÿ
i“1
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
´
nk
ÿ
i“1
mk
` pkσ2
k
m“1 «˜nk
ÿ
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
uk,ip0q
1´ µk ˙¸2
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘2ff
´
nk
ÿ
i“1
1tmk,i“ muˆuk,ip1q
µk
`
12
uk,ip0q
1´ µk ˙2ff.

<!-- page 48 -->
Alternatively, we can write
nkvcluster
k“
nk
i“1 ˆu2
k,ip1q
ÿ
`
µk
nk
´ pk
ÿ
i“1
mk
` pk
ÿ
m“1 ˜nk
ÿ
i“1
mk
` pkσ2
k
ÿ
m“1 ˜nk
ÿ
i“1
u2
k,ip0q
1´ µk ˙
nk
`uk,ip1q ´ uk,ip0q˘2
´ pkσ2
k
ÿ
i“1 ˆuk,ip1q
`
µk
1tmk,i“ mu`uk,ip1q ´ uk,ip0q˘¸2
1tmk,i“ muˆuk,ip1q
µk
uk,ip0q
`
1´ µk ˙¸2
.
uk,ip0q
1´ µk ˙2
We will next show that
Σk
vcluster
k
z1Hk
Hkz´
p
ÝÑ 0.
nkpkqkvk
vk
Given the µkp1´ µkq is bounded away from zero, by the weak law of large numbers for arrays, it
is enough to show
1
pnkpkqkvkq2
mk
ÿ
m“1
E„ˆnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙4ÝÑ 0.
Applying the multinomial theorem and the fact that all moments of Wk,i as well as all potential
outcomes are bounded, we obtain:
1
pnkpkqkvkq2
mk
ÿ
m“1
ď
E„ˆnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙4
c
pnkpkqkvkq2 ´nkpkqk ` nkp2
kqk max
m
nk,m ` nkp3
kqk max
m
n2
k,m ` nkp4
kqk max
m
n3
k,m¯.
Now, using lim supkÑ8 maxm nk,m{ minm nk,m ă 8, lim supkÑ8 pk minm nk,m{vk ă 8, and qkmk Ñ
8 we obtain
1
pnkpkqkvkq2
mk
ÿ
m“1
E„ˆnk
ÿ
i“1
ď c˜1
nkpkqkv2
k
ÝÑ 0.
1tmk,i“ muRk,ipWk,i´ µkqUk,i˙4
`
maxm nk,m
minm nk,m
1
qkmkv2
k
pk maxm n2
k,m
`
vk minm nk,m
1
`
qkmkvk
p2
k maxm n3
k,m
v2
k minm nk,m
1
qkmk ¸
As a result,
p
Vcluster
k
vcluster
k
“
` Opp1q.
vk
vk
The robust (sandwich) estimator of the variance of ?Nkpp
τk´ τkq is given by
p
Vrobust
1 p
p
p
k“ Nkz
Q´1
k
Ωk
Q´1
k z.
13

<!-- page 49 -->
where
p
Ωk“
nk
ÿ
i“1
Rk,i ˜ p
Uk,i
Wk,i
Uk,i ¸ ˜ p
Uk,i
p
Wk,i
Uk,i ¸1
p
.
We will derive the limit ofp
Vrobust
k {vk. Let
Ωk“
nk
ÿ
i“1
Rk,i ˆUk,i
Wk,iUk,i ˙ ˆUk,i
Wk,iUk,i ˙1
.
Because potential outcomes (and Wk,i) are bounded, we obtain
1
nkpkqkvk
}p
Ωk´ Ωk} ď c˜1
nkpkqkvk
nk
ÿ
i“1
Rk,i¸max
i“1,...,nk
|p
U2
k,i´ U2
k,i|.
Because the limsup of the expectation of the first factor (which is non-negative) is bounded and
the second factor converges to zero in probability as proved above, we obtain
1
}p
Ωk´ Ωk} “ Opp1q.
nkpkqkvk
Notice that
1
nkpkqkvk
}Ωk} ď c˜1
nkpkqkvk
nk
ÿ
i“1
Rk,i¸
Again, the limsup of the expectation of the right-hand side of this equation is non-negative and
bounded. As a result, we obtain }Ωk}{pnkpkqkvkq “ Opp1q.
p
Vrobust
k {vk“ z1Hk
“
Ωk
Hkz` Opp1q
nkpkqkvk
1
nkpkqkvk ˆ1
µkp1´ µkq ˙2 nk
ÿ
i“1
Rk,ipWk,i´ µkq2U2
k,i ` Opp1q.
Notice that
E„nk
ÿ
Rk,ipWk,i´ µkq2U2
i“1
k,i“
Finally, notice that
1
pnkpkqkvkq2
mk
ÿ
m“1
nk
ÿ
pkqkµkp1´ µkq´p1´ µkqu2
k,ip1q ` µku2
k,ip0q¯.
i“1
E«˜nk
ÿ
i“1
Rk,ipWk,i´ µkq2U2
k,i¸2ffď c
nkpkqk ` nkp2
kqk maxm nk,m
pnkpkqkvkq2
ď c˜1
`
nkpkqkv2
k
maxm nk,m
minm nk,m
ÝÑ 0.
1
qkmkv2
k ¸
14

<!-- page 50 -->
Therefore, by the weak law of large numbers for arrays, we obtain
where
p
Vrobust
k
vrobust
k
“
` Opp1q,
vk
vk
1
vrobust
k“
nk
nk
i“1 ˆu2
k,ip1q
ÿ
µk
`
u2
k,ip0q
1´ µk ˙.
A.3. Fixed effects
A.3.1. Large k distribution
Let
Nk,m“
nk
ÿ
i“1
1tmk,i“ muRk,i
and
p
τfixed
k“
mk
ÿ
m“1
mk
ÿ
m“1
nk
ÿ
1tmk,i“ muRk,iYk,ipWk,i´ Wk,mq
i“1
nk
ÿ
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq, (A.5)
i“1
where
Wk,m“
1
Nk,m _ 1
nk
ÿ
1tmk,i“ muRk,iWk,i.
i“1
Notice that we need lim infkÑ8 µkp1´ µkq ´ σ2
k“ lim infkÑ8 ErAk,mp1´ Ak,mqs ą 0 for this
estimator to be well-defined in large samples (otherwise, the denominator in the formula forp
τfixed
k
could be equal to zero). Although it is not strictly necessary, and because it entails little loss of
generality and simplifies the exposition, we will assume that the supports of the cluster probabilities,
Ak,m, are bounded away from zero and one (uniformly in k and m). In finite samples we assign
p
τfixed
k“ 0 to the cases when the denominator ofp
τfixed
k in equation (A.5) is equal to zero. Notice
that
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Wk,mq “ 0.
Let
1
αk,m“
nk,m
nk
ÿ
i“1
1
1tmk,i“ muyk,ip0q, τk,m“
nk,m
nk
ÿ
i“1
1tmk,i“ mupyk,ip1q ´ yk,ip0qq,
ek,ip0q “ yk,ip0q ´ αk,mk,i, and ek,ip1q “ yk,ip1q ´ αk,mk,i
´ τk,mk,i. It follows that
nk
ÿ
i“1
1tmk,i“ muek,ip1q “nk
ÿ
i“1
1tmk,i“ muek,ip0q “ 0.
15

<!-- page 51 -->
Now, Yk,i“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` αk,mk,i ` τk,mk,iWk,i. Then,
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,ippek,ip1q ` τk,mqWk,i ` ek,ip0qp1´ Wk,iqqpWk,i´ Wk,mq
p
τfixed
k“
.
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
Let
τk“
mk
ÿ
m“1
mk
ÿ
m“1
τk,m
nk
ÿ
i“1
nk
ÿ
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq, (A.6)
where, as before, we make τk“ 0 if the denominator on the right-hand side of (A.6) is equal to
zero. Now,p
τfixed
k´ τk “ pp
τfixed
k´ τkq ` pτk´ τkq, where
mk
ÿ
p
τfixed
m“1
k´ τk“
nk
ÿ
i“1
1tmk,i“ muRk,ipek,ip1qWk,i ` ek,ip0qp1´ Wk,iqqpWk,i´ Wk,mq
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
and
mk
ÿ
m“1
pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
τk´ τk“
.
mk
ÿ
m“1
nk
ÿ
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
i“1
Notice that outcomes enter the termp
τfixed
k´ τk only through the intra-cluster errors, ek,ip1q and
ek,ip0q. In contrast, the term τk´ τk depends on outcomes only through inter-cluster variability
in treatment effects, τk,m´ τk. The numerator in the expression for τk´ τk in the last displayed
equation does not have mean zero in general, and this will be reflected in a bias term, Bk, which
we define next. Let,
1
Dk“
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq,
and
1
nkpk
ErAk,mp1´ Ak,mqsmk
ÿ
m“1
pτk,m´ τkqp1 ´ p1´ pkqnk,mq
Bk“ ´
.
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq
Then, ?nkpkqkpp
τfixed
k´ τk´ Bkq “ Fk{Dk, where
Fk“
mk
ÿ
m“1
pψk,m´ ψk,mq ` pϕk,m´ ϕk,mq,
16

<!-- page 52 -->
ψk,m“
ψk,m“
and
ϕk,m“
ϕk,m“
1
?nkpkqk
1
?nkpkqk
1
?nkpkqk
1
?nkpkqk
nk
ÿ
i“1
nk
ÿ
i“1
pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,ipek,ip1qWk,i ` ek,ip0qp1´ Wk,iqqpWk,i´ Ak,mq,
1tmk,i“ muRk,ipek,ip1qWk,i ` ek,ip0qp1´ Wk,iqqpWk,m´ Ak,mq,
1tmk,i“ mu`Rk,iWk,ipWk,i´ Ak,mq ´ pkqkErAk,mp1´ Ak,mqs˘,
pτk,m´ τkq˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mq
´ qkErAk,mp1´ Ak,mqsp1 ´ p1´ pkqnk,mq¸.
The terms ψk,m and ψk,m depend on the within-cluster errors ek,ip1q and ek,ip0q. The terms ϕk,m
and ϕk,m depend on the inter-clusters errors τk,m´ τk. ψk,m and ϕk,m replace Wk,m with Ak,m,
while ψk,m and ϕk,m correct for the difference, Wk,m´ Ak,m.
It can be seen (in intermediate calculations below) that
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqff“ nk,mpkqkErAk,mp1´ Ak,mqs
and
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqff“ qkErAk,mp1´ Ak,mqsp1 ´ p1´ pkqnk,mq.
These two expectations are substracted in ϕk,m and ϕk,m , so ϕk,m and ϕk,m have mean zero. Doing
so for ϕk,m does not require adjustments elsewhere. Because
mk
ÿ
m“1
pτk,m´ τkqnk,m“ 0,
the nk,mpkqkErAk,mp1´ Ak,mqs terms do not change the sum Fk. In contrast, demeaning ϕk,m
creates the bias term Bk. If the size of the clusters nk,m does not vary across clusters, then Bk is
equal to zero. More generally, ?nkpkqkDkBk“ Opmkaqk{pnkpkqq. Therefore, if
mkqk
pkpnk{mkq
ÝÑ 0, (A.7)
(that is, if the expected number of sampled clusters is small relative to the expected number of
sampled observations per sampled cluster) then ?nkpkqkDkBk converges to zero. As a result,
?nkpkqkBk converges in probability to zero, because, as we will show later, Dk converges in probability to µkp1´ µkq ´ σ2
k, which is bounded away from zero. In our large sample analysis, we will
assume that the expected number of sampled clusters grows to infinity, mkqk Ñ 8. Then, equation (A.7) implies that the expected number of observations per sampled cluster goes to infinity,
pkpnk{mkq Ñ 8. Notice also that nkpkqk “ pnkpk{mkqpmkqkq Ñ 8.
17

<!-- page 53 -->
We summarize now the assumptions we made thus far. We first assumed that the supports of the
cluster probabilities, Ak,m, are bounded away from zero and one (uniformly in k and m), and that
potential outcomes are bounded. Moreover, we assumed mkqk Ñ 8 and pmkqkq{pppk nkq{mkq Ñ 0.
These imply ppknkq{mk Ñ 8 and nkpkqk Ñ 8. We will add the assumption that the ratio between
maximum and minimum cluster size is bounded, lim supkÑ8 maxm nk,m{ minm nk,m ă 8. This
assumption implies pk minm nk,m Ñ 8 and pmkqkq{ppk minm nk,mq Ñ 0.
We will now study the behavior of Dk. Notice that
ÿ
E«mk
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mqff
nk
ÿ
“ E«mk
ÿ
m“1
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqff
nk
ÿ
´ E«mk
ÿ
m“1
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqff
“ nkpkqkErAk,mp1´ Ak,mqs ´ qkErAk,mp1´ Ak,mqsmk
ÿ
p1 ´ p1´ pkqnk,mq.
m“1
In addition,
1
pnkpkqkq2
mk
ÿ
m“1
E«˜nk
ÿ
i“1
ď c
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2ff
nkpkqk ` nkp2
kqk maxm nk,m
pnkpkqkq2
“ c˜1
nkpkqk
`
maxm nk,m
minm nk,m
1
mkqk ¸ÝÑ 0.
The weak law of large numbers for arrays implies
Dk´ ErAk,mp1´ Ak,mqs ` 1
nkpk
ErAk,mp1´ Ak,mqsmk
ÿ
m“1
p1 ´ p1´ pkqnk,mq p
ÝÑ 0.
Because mk{pnkpkq Ñ 0 and ErAk,mp1´ Ak,mqs “ µkp1´ µkq ´ σ2
k, we obtain
Dk ´ pµkp1´ µkq ´ σ2
kq p
ÝÑ 0.
We now turn our attention to Fk. We will first calculate the variance of ψk,m. Let Qk,m be a binary
variable that takes value one if cluster m in population k is sampled, and zero otherwise. Notice
that
ErRk,iWk,ipWk,i´ Ak,mq|Ak,m,Qk,m“ 1,mk,i“ ms “ pkAk,mp1´ Ak,mq,
and
ErRk,ip1´ Wk,iqpWk,i´ Ak,mq|Ak,m,Qk,m“ 1,mk,i“ ms “ ´pkAk,mp1´ Ak,mq.
18

<!-- page 54 -->
Consider now
ψk,m,1 “
“
1
?nkpkqk
Qk,m
?nkpkqk
nk
ÿ
i“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqek,ip1q
1tmk,i“ mu´Rk,iWk,ipWk,i´ Ak,mq ´ pkAk,mp1´ Ak,mq¯ek,ip1q,
and
ψk,m,0 “
“
1
?nkpkqk
Qk,m
?nkpkqk
nk
ÿ
i“1
nk
ÿ
i“1
1tmk,i“ muRk,ip1´ Wk,iqpWk,i´ Ak,mqek,ip0q
1tmk,i“ mu´Rk,ip1´ Wk,iqpWk,i´ Ak,mq ` pkAk,mp1´ Ak,mq¯ek,ip0q.
It holds that ψk,m“ ψk,m,1 ` ψk,m,0 and Erψk,ms “ 0. Now, notice that
Erψ2
k,m,1s “ 1
nk
ErAk,mp1´ Ak,mq2
´ pkA2
k,mp1´ Ak,mq2snk
ÿ
i“1
Erψ2
k,m,0s “ 1
ErA2
k,mp1´ Ak,mq ´ pkA2
k,mp1´ Ak,mq2snk
ÿ
nk
i“1
1tmk,i“ mue2
k,ip1q,
1tmk,i“ mue2
k,ip0q,
and
Erψk,m,1ψk,m,0s “ 1
pkErA2
k,mp1´ Ak,mq2snk
ÿ
nk
i“1
1tmk,i“ muek,ip1qek,ip0q.
Therefore,
Erpψk,m,1 ` ψk,m,0q2s “ 1
nk
`
´
ErAk,mp1´ Ak,mq2snk
ÿ
i“1
1
ErA2
k,mp1´ Ak,mqsnk
ÿ
nk
i“1
1
pkErA2
k,mp1´ Ak,mq2snk
ÿ
nk
i“1
1tmk,i“ mue2
k,ip1q
1tmk,i“ mue2
k,ip0q
1tmk,i“ mupek,ip1q ´ ek,ip0qq2
,
and
mk
ÿ
m“1
Erpψk,m,1 ` ψk,m,0q2s “ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
i“1
` ErA2
k,mp1´ Ak,mqs 1
nk
nk
ÿ
i“1
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
e2
k,ip1q
e2
k,ip0q
nk
ÿ
pek,ip1q ´ ek,ip0qq2
. (A.8)
i“1
19

<!-- page 55 -->
We will next show that the terms ψk,m do not matter for the asymptotic distribution of ?nkpkqkpp
τk´
τkq. Notice that, because the cluster sum of ek,ip1q is equal to zero, we obtain Erψk,ms “ 0 and,
therefore,
mk
ÿ
m“1
E”ψk,mı“ 0.
Moreover
2
nk´1
ÿ
i“1
nk
ÿ
j“i`1
1tmk,i“ mk,j“ muek,ip1qek,j p1q “ ´nk
ÿ
i“1
1tmk,i“ mue2
k,ip1q ď 0.
In addition, ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ ms ď qkErAk,mp1´ Ak,mqs{nk,m (see intermediate
calculations). Therefore,
E«˜nk
ÿ
i“1
“
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqek,ip1q¸2ff
nk
ÿ
1tmk,i“ muE”Rk,iWk,ipWk,m´ Ak,mq2|mk,i“ mıe2
k,ip1q
i“1
nk´1
ÿ
E”1tmk,i“ mk,j“ muRk,iRk,j Wk,iWk,j pWk,m´ Ak,mq2ıek,ip1qek,j p1q
i“1
nk
` 2
ÿ
j“i`1
ď qkErAk,mp1´ Ak,mqs 1
nk,m
nk
ÿ
i“1
1tmk,i“ mue2
k,ip1q.
Now, because errors are bounded, we obtain
mk
ÿ
m“1
E«˜1
?nkpkqk
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqek,ip1q¸2ffď c
mk
nkpk
. (A.9)
Because mk{pnkpkq Ñ 0, the weak law of large numbers for arrays, implies,
1
?nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqek,ip1q p
ÝÑ 0.
with the analogous result involving the errors ek,ip0q. If follows that
mk
ÿ
m“1
ψk,m
p
ÝÑ 0.
Consider now ϕk,m. Notice that
E”´Rk,iWk,ipWk,i´ Ak,mq ´ pkqkErAk,mp1´ Ak,mqsq¯2ı
“ pkqkErAk,mp1´ Ak,mq2s ´ p2
kq2
k`ErAk,mp1´ Ak,mqs˘2
,
20

<!-- page 56 -->
and
E”´Rk,iWk,ipWk,i´ Ak,mq ´ pkqkErAk,mp1´ Ak,mqsq¯
ˆ ´Rk,j Wk,j pWk,j´ Ak,mq ´ pkqkErAk,mp1´ Ak,mqsq¯ˇ ˇmk,i“ mk,j“ mı
“ p2
kqkErA2
k,mp1´ Ak,mq2s ´ p2
kq2
k`ErAk,mp1´ Ak,mqs˘2
.
Therefore,
Erϕ2
k,ms “ ´ErAk,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯nk,m
pτk,m´ τkq2
nk
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯nk,mpnk,m´ 1q
nk
pτk,m´ τkq2
,
and
mk
ÿ
Erϕ2
k,ms “ ´ErAk,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
m“1
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
nk,mpnk,m´ 1q
nk
pτk,m´ τkq2
.
Next, we calculate the variance of ϕk,m. Using results on the moments of a Binomial distribution,
we obtain, for ně 1,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mq¸2
ˇ ˇ ˇ
Qk,m“ 1,
Nk,m“ n ff
1
“
n2 E«˜nk
ÿ
1tmk,i“ muRk,iWk,i´nk
ÿ
i“1
i“1
1tmk,i“ muRk,iWk,i´ nAk,m¯¸2
ˇ ˇ ˇ
Qk,m“ 1,
Nk,m“ n ff
“ nErA3
k,mp1´ Ak,mqs ` ErA2
k,mp1´ Ak,mqp5´ 7Ak,mqs
1
`
ErAk,mp1´ Ak,mqp6A2
k,m´ 6Ak,m ` 1qs.
n
Therefore,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mq¸2ff
“ nk,mpkqkErA3
k,mp1´ Ak,mqs ` qkErA2
k,mp1´ Ak,mqp5´ 7Ak,mqsp1 ´ p1´ pkqnk,mq
` qkErAk,mp1´ Ak,mqp6A2
k,m´ 6Ak,m ` 1qsrk,m,
where
rk,m“
nk,m
1
ÿ
n
n“1
PrpNk,m“ n|Qk,m“ 1q ďnk,m
ÿ
n“1
PrpNk,m“ n|Qk,m“ 1q ď 1.
It follows that,
Erϕ2
k,ms “ pτk,m´ τkq2´nk,m
ErA3
k,mp1´ Ak,mqs ` 1
ErA2
k,mp1´ Ak,mqp5´ 7Ak,mqsp1 ´ p1´ pkqnk,mq
nk
nkpk
21

<!-- page 57 -->
`
´
Therefore,
1
nkpk
qk
nkpk
ErAk,mp1´ Ak,mqp6A2
k,m´ 6Ak,m ` 1qsrk,m
pErAk,mp1´ Ak,mqsq2p1 ´ p1´ pkqnk,mq2¯.
mk
ÿ
m“1
Erϕ2
k,ms “mk
ÿ
pτk,m´ τkq2´nk,m
nk ¯ErA3
k,mp1´ Ak,mqs ` Op1q.
m“1
We will now study the covariance between ϕk,m and ϕk,m. Using results on the moments of a
Binomial distribution, we obtain, for ně 1,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mq¸˜nk
ÿ
i“1
“ E«1´ Ak,m
n ˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,i¸2˜nk
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mq¸ˇ ˇ ˇ
1tmk,i“ muRk,iWk,i´ nAk,mq¸ˇ ˇ ˇ
ÿ
i“1
Qk,m“ 1,
Nk,m“ n ff
Qk,m“ 1,
Nk,m“ n ff
“ 2nErA2
k,mp1´ Ak,mq2s ` ErAk,mp1´ Ak,mq2p1´ 2Ak,mqs.
Therefore,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mq¸˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mq¸ff
“ 2nk,mpkqkErA2
k,mp1´ Ak,mq2s ` qkErAk,mp1´ Ak,mq2p1´ 2Ak,mqs PrpNk,m ě 1|Qk,m“ 1q.
In addition,
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqffE«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqff
“ nk,mpkq2
kpErAk,mp1´ Ak,mqsq2 PrpNk,m ě 1|Qk,m“ 1q.
As a result,
Erϕk,mϕk,ms “ ´2ErA2
k,mp1´ Ak,mq2s ´ qkpErAk,mp1´ Ak,mqsq2¯pτk,m´ τkq2 ˆnk,m
nk ˙` Oˆ1
nkpk ˙
` Oˆqk
pk minm nk,m `pk min
m
nk,mp1´ pkqminm nk,m˘˙.
Notice that mk{pnkpkq Ñ 0. In addition, mkqk{ppk minm nk,mq Ñ 0 and
pk min
nk,mp1´ pkqminm nk,m “ pk min
m
m
nk,m ˆ1´
pk minm nk,m
minm nk,m ˙minm nk,m
ă pk min
nk,me´pk minm nk,m ÝÑ 0.
m
Therefore,
mk
ÿ
m“1
Erϕk,mϕk,ms “ ´2ErA2
k,mp1´Ak,mq2s´qkpErAk,mp1´Ak,mqsq2¯mk
ÿ
m“1
pτk,m´τkq2 ˆnk,m
nk ˙` Op1q.
22

<!-- page 58 -->
Next, we will study the remaining covariances between ψk,m, ϕk,m, ψk,m, and ϕk,m. Because the
intra-cluster errors, ek,ip1q and ek,ip0q sum to zero, it can be easily seen that Erψk,mϕk,ms “
Erψk,mϕk,ms “ 0. It can also be seen that the inter-clusters sums of covariances between ψk,m and
any of the other terms go to zero. To prove this for the covariance with ψk,m, we have
ÿ
˜mk
m“1
Er|ψk,mψk,m|s¸2
ÿ
ď ˜mk
m“1
mk
ď
ÿ
Erψ2
k,msmk
ÿ
m“1
m“1
“ Op1qOp1q “ Op1q.
pErψ2
k,msErψ2
k,msq1{2¸2
Erψ2
k,ms
The same argument and result applies to Erψk,mϕk,ms and Erψk,mϕk,ms. Putting all the pieces
together, we obtain
nkpkqkErD2
k pp
τfixed
k´ τkq2s “ fk ` Op1q,
where
fk“ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
i“1
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
` ´ErAk,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
nk
ÿ
i“1
e2
k,ip0q
nk,m
nk
pτk,m´ τkq2
nk,mpnk,m´ 1q
pτk,m´ τkq2
nk
` ErA3
k,mp1´ Ak,mqsmk
ÿ
m“1
pτk,m´ τkq2´nk,m
nk ¯
´ 2´2ErA2
k,mp1´ Ak,mq2s ´ qkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
pτk,m´ τkq2 ˆnk,m
nk ˙.
Collecting terms with identical factors, we obtain
fk“ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
i“1
nk
ÿ
i“1
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
` ´ErAk,mp1´ Ak,mq2s ´ p4 ` pkqErA2
k,mp1´ Ak,mq2s
` ErA3
k,mp1´ Ak,mqs ` 2qkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
e2
k,ip0q
nk,m
nk
pτk,m´ τkq2
23

<!-- page 59 -->
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
n2
k,m
nk
pτk,m´ τkq2
.
The first three terms in the expression above depend on intra-cluster heterogeneity in potential
outcomes and treatment effects. The last two terms depend on inter-cluster variation in average
treatment effects.
A more compact expression for fk is
fk“ ErAk,mp1´ Ak,mq2s 1
nk
ÿ
nk
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
i“1
´ pkErA2
k,mp1´ Ak,mq2s 1
nk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
` ´ErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2s
` 2qkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
nk,m
nk
pτk,m´ τkq2
m“1
` ´pkErA2
k,mp1´ Ak,mq2s ´ pkqkpErAk,mp1´ Ak,mqsq2¯mk
ÿ
m“1
nk
ÿ
i“1
e2
k,ip0q
n2
k,m
nk
pτk,m´ τkq2
. (A.10)
Notice that the first four terms in (A.10) are bounded, and that
ErA2
k,mp1´Ak,mq2s´qkpErAk,mp1´Ak,mqsq2
“ varpAk,mp1´Ak,mqq`p1´qkqpErAk,mp1´Ak,mqsq2
.
Assume that
lim inf
kÑ8
mk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2 ą 0, (A.11)
and
lim inf
kÑ8
varpAk,mp1´ Ak,mqq _ p1´ qkq ą 0. (A.12)
The last term in equation (A.10) is greater than
pk min
m
nk,m`ErA2
k,mp1´ Ak,mq2s ´ pErAk,mp1´ Ak,mqsq2˘mk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
,
which converges to infinity because pk minm nk,m Ñ 8. That is, the last term dominates the
variance in large samples provided that (A.11) and (A.12) hold.
We will now derive the large sample distribution ofp
τfixed
k . To show that Lyapunov’s condition
holds for Fk, notice that
|pψk,m´ ψk,mq ` pϕk,m´ ϕk,mq|3
“
1
pnkpkqkq3{2
ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,ippek,ip1q ` τk,m´ τkqWk,i ` ek,ip0qp1´ Wk,iqqpWk,i´ Wk,mq
´ pτk,m´ τqqkErAk,mp1´ Ak,mqsp1 ´ p1´ pkqnk,mq
ˇ ˇ ˇ ˇ ˇ
3
,
24

<!-- page 60 -->
where the last term inside the absolute value comes from the bias correction. Notice that,
ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,ipek,ip1q ` τk,m´ τkqWk,ipWk,i´ Wk,mq
ˇ ˇ ˇ ˇ ˇ
3
“
ˇ ˇ ˇ ˇ ˇ
p1´ Wk,mqnk
ÿ
i“1
1tmk,i“ muRk,ipek,ip1q ` τk,m´ τkqWk,i
ˇ ˇ ˇ ˇ ˇ
3
ď c
ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
ď cN3
k,m.
1tmk,i“ muRk,iWk,i
ˇ ˇ ˇ ˇ ˇ
3
From the formula of the third moment of a binomial random variable, we obtain
ErN3
k,ms “ qkErN3
k,m|Qk,m“ 1s
“ n3
k,mp3
kqk ` Opn3
k,mp3
kqkq,
as pknk,m Ñ 8. Now,
1
f3{2
k
mk
ÿ
k“1
E«ˇ ˇ ˇ ˇ ˇ
1
?nkpkqk
ď c
nk
ÿ
i“1
nk maxn n2
k,mp3
kqk
pnkpkqkq3{2ppk minm nk,mq3{2
1tmk,i“ muRk,ipek,ip1q ` τk,m´ τkqWk,ipWk,i´ Wk,mq
ˇ ˇ ˇ ˇ ˇ
3ff
“ cˆmaxm nk,m
minm nk,m ˙2 1
pmkqkq1{2
ÝÑ 0.
Similar calculations deliver the analogous result for the term involving ek,ip0q, and proving the
result for the bias term is straightforward. Therefore, we obtain
1
f3{2
k
mk
ÿ
m“1
|pψk,m´ ψk,mq ` pϕk,m´ ϕk,mq|3 ÝÑ 0.
By the Central Limit Theorem for arrays, this implies
?nkpkqkFk{f1{2
k
d
ÝÑ Np0,1q.
Let ˜ vk“ fk{pµkp1´ µkq ´ σ2
kq2. Then,
?nkpkqkpp
τfixed
k´ τkq{˜
1{2
v
k
d
ÝÑ Np0,1q.
As a result,
aNkpp
τfixed
k´ τkq{˜
1{2
v
k
d
ÝÑ Np0,1q.
A.3.2. Estimation of the variance
Let
Nk,m,0 “
nk
ÿ
i“1
1tmk,i“ muRk,ip1´ Wk,iq
25

<!-- page 61 -->
and
Nk,m,1 “
nk
ÿ
i“1
1tmk,i“ muRk,iWk,i.
Let
Yk,m“
1
Nk,m _ 1
nk
ÿ
i“1
1tmk,i“ muRk,iYk,i.
Then,
Yk,m“
p
αk,m `p
τk,mWk,m,
where
p
αk,m“
1
Nk,m,0 _ 1
nk
ÿ
i“1
1tmk,i“ muRk,ip1´ Wk,iqYk,i,
1
p
τk,m“
Nk,m,1 _ 1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,iYk,i´
1
Nk,m,0 _ 1
nk
ÿ
i“1
1tmk,i“ muRk,ip1´ Wk,iqYk,i,
and, as before,
Wk,m“
1
Nk,m _ 1
nk
ÿ
i“1
1tmk,i“ muRk,iWk,i.
Letr
r
Ă
r
Uk,i“
Yk,i´
p
τfixed
k
Wk,i, where
within estimator of τk. Letr
Σk“ řmk
m“1
Yk,i“ Yk,i´ Yk,mk,i,
r
Σk,m, where
Ă
Wk,i “ pWk,i´ Wk,mk,iq, andp
τfixed
k is the
r
Σk,m“ ˜nk
ÿ
i“1
Ă
r
1tmk,i“ muRk,i
Wk,i
Uk,i¸2
.
Also, let
r
Qk“
nk
ÿ
i“1
Ă
Rk,i
W2
k,i.
Then, the cluster estimator of the variance of ?Nkpp
τfixed
k´ τkq is
r
Vcluster
r
k“ Nk
Q´1
r
r
k
Σk
Q´1
k.
We know already that
1
r
Qk ´ pµkp1´ µkq ´ σ2
kq p
ÝÑ 0,
nkpkqk
with µkp1´ µkq ´ σ2
k bounded away from zero. To establish convergence of
notice that, for mk,i“ m, we have
r
Σk{pnkpkqkfkq, first
r
Uk,i“ Yk,i ´ pp
αk,m `p
τk,mWk,mq ´p
τfixed
k pWk,i´ Wk,mq
“ yk,ip1qWk,i ` yk,ip0qp1´ Wk,iq ´ pαk,m ` τk,mWk,mq ´p
τfixed
k pWk,i´ Wk,mq
´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m
“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´
p
τfixed
k qpWk,i´ Wk,mq
26

<!-- page 62 -->
´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m
“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´ τkqpWk,i´ Wk,mq
´ pp
τfixed
k´ τkqpWk,i´ Wk,mq ´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m.
For mk,i“ m and Nk,m,0,Nk,m,1 ě 1, let
Uk,i“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´ τkqpWk,i´ Wk,mq,
and let Uk,i“ 0 for mk,i“ mand Nk,m,0Nk,m,1 “ 0. Then, for mk,i“ mand Nk,m,0Nk,m,1 ě 1, we
have
r
Uk,i´ Uk,i “ ´pp
τfixed
k´ τkqpWk,i´ Wk,mq ´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m.
Then,
˜nk
ÿ
i“1
“ ˜nk
ÿ
i“1
“ ˜nk
ÿ
i“1
“ ˜nk
ÿ
i“1
Ă
r
1tmk,i“ muRk,i
Wk,i
Uk,i¸2
Ă
1tmk,i“ muRk,i
Wk,i´Uk,i ` ` r
Uk,i´ Uk,i˘¯¸2
Ă
1tmk,i“ muRk,i
Wk,i´Uk,i ´ pp
τfixed
k´ τkqpWk,i´ Wk,mq¯¸2
Ă
1tmk,i“ muRk,i
Wk,iUk,i ´ pp
τfixed
k´ τkqnk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2
.
Using the formula for the second moment of a binomial distribution and ně 1, we obtain,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2
ˇ ˇ ˇ
Nk,m“ nff
“ E«˜nk
ÿ
i“1
1tmk,i“ mup1´ Wk,mqRk,iWk,i¸2
ˇ ˇ ˇ
Nk,m“ nff
ď E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,i¸2
ˇ ˇ ˇ
Nk,m“ nff
ď n2 ` n.
From the formula of the sum of the first two moments of a binomial distribution, we obtain
mk
ÿ
m“1
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2ffď
mk
ÿ
m“1
pn2
k,mp2
kqk ` nk,mpkqkq.
Therefore,
1
nkpkqkfk
pp
τfixed
k´ τkq2
mk
ÿ
m“1
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2ff
27

<!-- page 63 -->
ď
nkpkqk
fk
pp
τfixed
k´ τkq2 1
pnkpkqkq2
“ Opp1q ˆmaxm nk,m
minm nk,m
1
`
mkqk
mk
ÿ
pn2
k,mp2
kqk ` nk,mpkqkq
m“1
1
nkpkqk ˙p
ÝÑ 0.
Now, notice that
1
nkpkqkfk
mk
ÿ
m“1 ˜nk
ÿ
i“1
1
“
nkpkqkfk
Ă
1tmk,i“ muRk,i
Wk,iUk,i¸2
mk
ÿ
m“1 ˜nk
ÿ
i“1
1tmk,i“ muRk,i`ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq˘pWk,i´ Wk,mq
` pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Wk,mq2¸2
.
Equation (A.9) (and the analogous result for the sum involving terms with ek,ip0q), implies
1
nkpkqkfk
mk
ÿ
m“1 ˜nk
ÿ
i“1
1tmk,i“ muRk,i`ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq˘pWk,m´ Ak,mq¸2
p
ÝÑ 0.
As a result, it is enough to establish convergence of Σk{pnkpkqkfkq, where
Σk“
mk
ÿ
m“1 ˜nk
ÿ
i“1
` pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,i`ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq˘pWk,i´ Ak,mq
1tmk,i“ muRk,ipWk,i´ Wk,mq2¸2
mk
“
ÿ
m“1 ˜nk
ÿ
i“1
nk
`
ÿ
i“1
` pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ mu´Rk,iWk,ipWk,i´ Ak,mq ´ pkqkAk,mp1´ Ak,mq¯ek,ip1q
1tmk,i“ mu´Rk,ip1´ Wk,iqpWk,i´ Ak,mq ` pkqkAk,mp1´ Ak,mq¯ek,ip0q
1tmk,i“ muRk,ipWk,i´ Wk,mq2¸2
.
We will next show that
1
nkpkqkfk
Σk´
fcluster
k
fk
p
ÝÑ 0, (A.13)
where
fcluster
k“
`
1
ErAk,mp1´ Ak,mq2snk
ÿ
nk
i“1
1
ErA2
k,mp1´ Ak,mqsnk
ÿ
nk
i“1
e2
k,ip1q
e2
k,ip0q
28

<!-- page 64 -->
´
1
pkErA2
k,mp1´ Ak,mq2snk
ÿ
pek,ip1q ´ ek,ip0qq2
nk
i“1
` pErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2sqmk
ÿ
m“1
` pkErA2
k,mp1´ Ak,mq2smk
ÿ
m“1
n2
k,m
pτk,m´ τkq2
.
nk
nk,m
nk
pτk,m´ τkq2
Let
Xk,m“
1
nkpkqk ˜nk
ÿ
1tmk,i“ muRk,i`ek,ip0qp1´ Wk,iq
i“1
` ek,ip1qWk,i˘pWk,i´ Ak,mq ` pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Wk,mq2¸2
Using the result in equation (A.8) and results on the moments of the binomial distribution (see
intermediate calculations in section A.7), we obtain
1
ErΣks “mk
ÿ
ErXk,ms
nkpkqk
m“1
“ fcluster
k ` Op1q.
Therefore, to show that equation (A.13) holds, we will show
1
mk
f2
ÿ
ErX2
k,ms ÝÑ 0. (A.14)
k
m“1
Let
θk“ ErpRk,iWk,ipWk,i´ Ak,mq ´ pkAk,mp1´ Ak,mqq2|mk,i“ m,Qk,m“ 1s
“ pk `ErAk,mp1´ Ak,mq2s ´ pkErA2
k,mp1´ Ak,mq2s˘,
and
Let
πk“ ErpRk,iWk,ipWk,i´ Ak,mq ´ pkAk,mp1´ Ak,mqq4|mk,i“ m,Qk,m“ 1s
“ pkErpWk,ipWk,i´ Ak,mq ´ pkAk,mp1´ Ak,mqq4|mk,i“ ms ` p4
kp1´ pkqErA4
k,mp1´ Ak,mq4s.
Xk,m,1 “
“
1
nkpkqk ˜nk
ÿ
i“1
Qk,m
nkpkqk ˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqek,ip1q¸2
1tmk,i“ mupRk,iWk,ipWk,i´ Ak,mq ´ pkAk,mp1´ Ak,mqqek,ip1q¸2
.
29

<!-- page 65 -->
Then,
ErX2
k,m,1s “ qkErX2
k,m,1|Qk,m“ 1s
nk
“
πk
n2
kp2
kqk
ÿ
1tmk,i“ mue4
k,ip1q
i“1
`
6θ2
k
n2
kp2
kqk
nk´1
ÿ
i“1
nk
ÿ
j“i`1
1tmk,i“ mk,j“ mue2
k,ip1qe2
k,j p1q.
Therefore, because nkpkqk Ñ 8 and mkqk Ñ 8, we obtain
mk
ÿ
m“1
ErX2
k,m,1s ď c
nkpkqk ˜1
nk
ˆ ˜1
mk
nk
ÿ
i“1
e4
k,ip1q¸`
c
mkqk
maxm n2
k,m
minm n2
k,m
mk
nk´1
ÿ
m“1
1
maxm n2
k,m
nk
ÿ
ÿ
i“1
j“i`1
1tmk,i“ mk,j“ mue2
k,ip1qe2
k,j p1q¸
ÝÑ 0. (A.15)
Using the same argument, we obtain
mk
ÿ
m“1
ErX2
k,m,2s ÝÑ 0, (A.16)
where
1
Xk,m,2 “
nkpkqk ˜nk
ÿ
i“1
Notice that equations (A.15) and (A.16) imply
1tmk,i“ muRk,ip1´ Wk,iqpWk,i´ Ak,mqek,ip0q¸2
.
1
f2
k
mk
ÿ
m“1
ErX2
k,m,1s ÝÑ 0
and
1
mk
f2
ÿ
ErX2
k,m,2s ÝÑ 0.
k
m“1
Notice that the last two equations hold even if fk is bounded (e.g., when τk,m´ τk“ 0 for all k and
m), as long as fk is bounded away from zero in large samples. In section A.3.3 we derive conditions
so that fk is bounded away from zero in large samples even if τk,m´ τk“ 0 for all k and m. Now,
let
1
Xk,m,3 “
nkpkqk ˜pτk,m´ τkqnk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2
.
Recall that, under the conditions in (A.11) and (A.12), fk Ñ 8 and pk min nk,m{fk is bounded for
large k and, therefore, pk max nk,m{fk is bounded for large k. Then (see intermediate calculations
at the end of this document), for large k,
1
mk
f2
ÿ
ErX2
k,m,3s “ 1
k
m“1
pnkpkqkfkq2
mk
ÿ
m“1
n4
k,mp4
kqkpτk,m´ τkq4 ˆ1 ` Oˆ1
pk minm nk,m ˙˙
30

<!-- page 66 -->
pk maxm n2
k,m
“
mkqkfk minm nk,m ˜pk
mk
n2
fk
ÿ
k,m
nk
m“1
pτk,m´ τkq4¸ ˆ1 ` Oˆ1
pk minm nk,m ˙˙
“ Oˆ1
mkqk ˙ ˆ1 ` Oˆ1
pk minm nk,m ˙˙Ñ 0.
Now, H¨older’s inequality implies that equation (A.14) holds (see intermediate calculations).
Now let,
˜
vcluster
k“ fcluster
k {pµkp1´ µkq ´ σ2
kq2
.
We obtain,
r
Vcluster
˜
vcluster
k
k
“
˜
˜
` Opp1q.
vk
vk
We will next establish the analogous result for the heteroskedaticity-robust variance estimator. Let
r
Σrobust
k“
nk
ÿ
i“1
Ă
Rk,i
W2
r
U2
k,i
k,i.
Then, the heteroskedasticity-robust estimator of the variance of ?Nkpp
τfixed
k´ τkq is
r
Vrobust
r
k“ Nk
Q´1
r
Σrobust
r
k
k
Q´1
k.
As we have established before,
r
Uk,i“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´ τkqpWk,i´ Wk,mq
´ pp
τfixed
k´ τkqpWk,i´ Wk,mq ´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m.
For mk,i“ m and Nk,m,0Nk,m,1 ě 1, let
Uk,i“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´ τkqpWk,i´ Wk,mq,
and let Uk,i“ 0 for mk,i“ mand Nk,m,0Nk,m,1 “ 0. Then, for mk,i“ mand Nk,m,0Nk,m,1 ě 1, we
have
and
r
Uk,i´ Uk,i “ ´pp
τfixed
k´ τkqpWk,i´ Wk,mq ´ pp
αk,m´ αk,mq ´ pp
τk,m´ τk,mqWk,m,
1
nkpkqk
nk
ÿ
i“1
1
nk
Ă
r
Rk,i
W2
U2
k,i
k,i“
nkpkqk
ÿ
Ă
Rk,i
W2
k,i´Uk,i ` ` r
Uk,i´ Uk,i˘¯2
. (A.17)
i“1
Focusing on the part of the right hand side of last equation that depends on the first term of
r
Uk,i´ Uk,i, we obtain
1
nkpkqk
nk
ÿ
i“1
Ă
Rk,i
W4
k,ipp
τfixed
k´ τkq2 ď pp
τfixed
k´ τkq2 1
nkpkqk
nk
ÿ
i“1
Ă
Rk,i
W2
k,i
p
ÝÑ 0.
We will focus now on the part of the right-hand side of equation (A.17) that that depends on the
second term ofr
Uk,i´ Uk,i,
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
Ă
1tmk,i“ muRk,i
W2
k,ipp
αk,m´ αk,mq2
.
31

<!-- page 67 -->
Using the formula for the variance of a sample mean under sampling without replacement [e.g., in
the supplement of Abadie et al., 2020], we obtain for 1 ď nď nk,m´ 1,
E«pp
nk
αk,m´ αk,mq2
ÿ
Ă
1tmk,i“ muRk,i
W2
k,i
ˇ ˇ ˇ
i“1
Nk,m,0 “ nff
“ E«pp
αk,m´ αk,mq2Nk,mWk,mp1´ Wk,mqˇ ˇ ˇ
Nk,m,0 “ nff
ď E”npp
αk,m´ αk,mq2ˇ ˇNk,m,0 “ nı
“ nvarpp
αk,m|Nk,m,0 “ nq
“ s2
k,m,0´1´
n
nk,m ¯, (A.18)
where
1
s2
k,m,0 “
nk,m´ 1
nk
ÿ
i“1
1tmk,i“ mupyk,ip0q ´ αk,mq2
.
Because s2
k,m,0 is bounded, so is the right-hand side of equation (A.18). As a result
E«1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
Ă
1tmk,i“ muRk,i
W2
k,ipp
αk,m´ αk,mq2ffď c
mk
nkpk
ÝÑ 0.
An analogous derivation applies to the part of the right-hand side of equation (A.17) that depends
on the third term ofr
Uk,i´ Uk,i. (Notice that Wk,m ď 1 and thatp
τk,m´ τk,m is equal to minus the
difference betweenp
αk,m´ αk,m and the analogous difference for the treated.
Therefore, we will study the behavior of
1
nkpkqk
nk
ÿ
i“1
Ă
Rk,i
W2
k,iU2
k,i. (A.19)
First, notice that
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i
ˇ ˇ ˇpWk,i´ Wk,mq2 ´ pWk,i´ Ak,mq2ˇ ˇ ˇ
Wk,ie2
k,ip1q
1
ď c
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i
ˇ ˇ ˇpWk,i´ Wk,mq ` pWk,i´ Ak,mqˇ ˇ ˇ
ˇ ˇWk,m´ Ak,mˇ ˇWk,i
ď c˜1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i´pWk,i´ Wk,mq ` pWk,i´ Ak,mq¯2
Wk,i¸1{2
ˆ ˜1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i`Wk,m´ Ak,m˘2¸1{2
. (A.20)
The inside of the first square root in equation (A.20) is bounded by a constant times
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i,
32

<!-- page 68 -->
which converges in probability to one. The expectation of the inside of the second square root in
equation (A.20) is
1
nkpkqk
mk
ÿ
m“1
E“Nk,m`Wk,m´ Ak,m˘2‰ ď c
mk
ÝÑ 0.
nkpk
As a result, the right-hand side of equation (A.20) converges to zero in probability. The derivation
with p1´ Wk,iqe2
k,ip0q replacing Wk,ie2
k,ip1q in equation (A.20) is analogous. Now, notice that
pWk,i´ Wk,mq4 ´ pWk,i´ Ak,mq4
“ ´`pWk,i´ Wk,mq2 ` pWk,i´ Ak,mq2˘`pWk,i´ Wk,mq ` pWk,i´ Ak,mq˘pWk,m´ Ak,mq.
Because the first factor of the expression above is bounded, we obtain
1
mk
ÿ
nkpkqk
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i
ˇ ˇ ˇpWk,i´ Wk,mq4 ´ pWk,i´ Ak,mq4ˇ ˇ ˇpτk,m´ τkq2
ď c˜1
nkpkqk
ˆ ˜1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,i¸1{2
1tmk,i“ muRk,i`Wk,m´ Ak,m˘2¸1{2
. (A.21)
Now, the right-hand side of equation (A.21) converges to zero in probability by the same argument
as for equation (A.20). Cauchy-Schwarz inequality implies,
1
nkpkqk
nk
ÿ
i“1
Ă
Rk,i
W2
k,iU2
1
k,i“
nkpkqk
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq2˘
U2
k,i ` Opp1q,
where
˘
Uk,i“ ek,ip1qWk,i ` ek,ip0qp1´ Wk,iq ` pτk,m´ τkqpWk,i´ Ak,mq, ˘
(A.22)
for mk,i“ m and Nk,m,0Nk,m,1 ě 1, and
the behavior of
Uk,i“ 0 for Nk,m,0Nk,m,1 ě 0. Therefore, we will study
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq2˘
U2
k,i.
We know,
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq2Wk,ie2
k,ip1q
´ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
i“1
e2
k,ip1q p
ÝÑ 0,
and
1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq2p1´ Wk,iqe2
k,ip0q
33

<!-- page 69 -->
´ ErA2
k,mp1´ Ak,mqs 1
nk
nk
ÿ
i“1
e2
k,ip0q p
ÝÑ 0.
Now, notice that
ErpWk,i´ Ak,mq4|mk,i“ m,Rk,i“ 1,Ak,m“ as “ p1´ aq4a` a4p1´ aq
“ ap1´ aqrp1´ aq3 ` a3s
“ ap1´ aqr1´ 3ap1´ aqs,
which implies
E«nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq4pτk,m´ τkq2ff
“ nk,mpkqkErAk,mp1´ Ak,mqp1´ 3Ak,mp1´ Ak,mqqspτk,m´ τkq2
,
and
E«1
nkpkqk
mk
ÿ
m“1
nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq4pτk,m´ τkq2ff
“ ErAk,mp1´ Ak,mqp1´ 3Ak,mp1´ Ak,mqqsmk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
.
Notice now that
1
pnkpkqkq2
mk
ÿ
m“1
E«˜nk
ÿ
i“1
1tmk,i“ muRk,ipWk,i´ Ak,mq4pτk,m´ τkq2¸2ff
1
mk
ď c
pnkpkqkq2
ÿ
m“1
E«˜nk
ÿ
i“1
1tmk,i“ muRk,i¸2ff
mk
qk
ď c
pnkpkqkq2
ÿ
pnk,mpk ` n2
k,mp2
kq
m“1
“ c˜1
`
nkpkqk
maxm nk,m
minm nk,m
1
mkqk ¸p
ÝÑ 0.
Notice also that expectations of the sums of products of the terms on the right-hand side of equation
(A.22) are equal to zero. Then,
1
r
Σrobust
k´ frobust
k
p
ÝÑ 0,
nkpkqk
where
frobust
k“ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
i“1
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
nk
ÿ
i“1
e2
k,ip0q
34

<!-- page 70 -->
Now let,
We obtain,
` ErAk,mp1´ Ak,mqp1´ 3Ak,mp1´ Ak,mqqsmk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
.
˜
vrobust
k“ frobust
k {pµkp1´ µkq ´ σ2
kq2
.
r
Vrobust
k“
˜
vrobust
k ` Opp1q.
A.3.3. Large k results the fixed effects case under homogeneous average
treatment effects across clusters
We will now study the Lyapounov’s condition for the case τk,m“ τk for all k and m“ 1,...,mk,
so
fk“
mk
ÿ
m“1
Erψ2
k,ms.
Notice that
mk
ÿ
m“1
Erψ2
k,ms ě 1
nk
`
´
“
`
ErAk,mp1´ Ak,mq2snk
ÿ
i“1
1
ErA2
k,mp1´ Ak,mqsnk
ÿ
nk
i“1
1
ErA2
k,mp1´ Ak,mq2snk
ÿ
nk
i“1
1
nk
ErAk,mp1´ Ak,mq3snk
ÿ
i“1
1
ErA3
k,mp1´ Ak,mqsnk
ÿ
nk
i“1
ErA2
k,mp1´ Ak,mq2snk
ÿ
i“1
1tmk,i“ mue2
k,ip1q
1tmk,i“ mue2
k,ip0q
1tmk,i“ mupek,ip1q ´ ek,ip0qq2
1tmk,i“ mue2
k,ip1q
1tmk,i“ mue2
k,ip0q
2
`
nk
“ E«1
nk
1tmk,i“ muek,ip1qek,ip0q
mk
ÿ
m“1
A3
k,mp1´ Ak,mq3
nk
ÿ
i“1
1tmk,i“ mu ˆek,ip1q
Ak,m
`
ek,ip0q
1´ Ak,m ˙2ff.
Therefore,
lim inf
kÑ8
E«1
nk
mk
ÿ
m“1
A3
k,mp1´ Ak,mq3
nk
ÿ
i“1
1tmk,i“ mu ˆek,ip1q
Ak,m
ek,ip0q
`
1´ Ak,m ˙2ffą 0
is sufficient for lim infkÑ8 fk ą 0 (even if condition (A.11) does not hold). Given our assumption
that the supports of the cluster probabilities, Ak,m, are bounded away from zero and one (uniformly
in k and m), then
lim inf
kÑ8
E«1
nk
mk
nk
ÿ
ÿ
m“1
i“1
1tmk,i“ mu ˆek,ip1q
Ak,m
`
ek,ip0q
1´ Ak,m ˙2ffą 0 (A.23)
35

<!-- page 71 -->
is sufficient for lim infkÑ8 fk ą 0. Assume that (A.23) holds, so lim infkÑ8 fk ą 0. We now obtain,
E«ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mqek,ip1q
ˇ ˇ ˇ ˇ ˇ
4
ˇ ˇ ˇ Qk,m“ 1,Ak,mff
“ E«p1´ Wk,mq4
ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,iWk,iek,ip1q
ˇ ˇ ˇ ˇ ˇ
4
ˇ ˇ ˇ Qk,m“ 1,Ak,mff
ď E«ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,iWk,iek,ip1q
ˇ ˇ ˇ ˇ ˇ
4
ˇ ˇ ˇ Qk,m“ 1,Ak,mff,
and
E«ˇ ˇ ˇ ˇ ˇ
nk
ÿ
i“1
1tmk,i“ muRk,iWk,iek,ip1q
ˇ ˇ ˇ ˇ ˇ
4
ˇ ˇ ˇ Qk,m“ 1,Ak,mff
“ E«ˇ ˇ ˇ ˇ ˇ
nk
ÿ
1tmk,i“ mupRk,iWk,i´ pkAk,mqek,ip1q
i“1
ˇ ˇ ˇ ˇ ˇ
4
ˇ ˇ ˇ Qk,m“ 1,Ak,mff
“ nk,mErpRk,iWk,i´ pkAk,mq4|Qk,m“ 1,Ak,ms
` 3nk,mpnk,m´ 1qpErpRk,iWk,i´ pkAk,mq2|Qk,m“ 1,Ak,msq2
.
The first equality holds because the terms ek,ip1q sum to zero within clusters. The second equality
holds because, if mk,i“ mk,j“ m, with i ‰ j, then Rk,iWk,i and Rk,iWk,i are independent
conditional on Qk,m“ 1,Ak,m, and ErRk,iWk,i´ pkAk,m|Qk,m“ 1,Ak,ms “ 0. Notice that
ErpRk,iWk,i´ pkAk,mq2|Qk,m“ 1,Ak,ms “ pkAk,mp1´ pkAk,mq ď pk,
which also implies ErpRk,iWk,i´ pkAk,mq4|Qk,m“ 1,Ak,ms ď pk. As a result,
mk
ÿ
m“1
E«ˇ ˇ ˇ ˇ ˇ
1
?nkpkqk
nk
ÿ
1tmk,i“ muRk,iWk,iek,ip1q
i“1
ˇ ˇ ˇ ˇ ˇ
4ff
1
ď
` 3
nkpkqk
maxm nk,m
minm nk,m
1
Ñ 0.
mkqk
A.4. Derivations of the variance estimators
In this section, we derive the adjustments in the CCV variance. (We do this under the assumption
that the Zi are independent. In our simulations we actually use a slightly different sampling scheme
for the Zi where the average Zk,m is identical and fixed in each cluster.) To derive the CCV variance
of the least squares estimator, consider first a variance estimator of the form
˜n
ÿ
i“1
Vi¸2
.
We aim, however, to design an estimator based on a subsample consisting of units with Zi “ 1,
where Zi P t0,1u is i.i.d. binary with PrpZi “ 1q “ pZ and independent of Vi. First, notice that
E» –˜n
ÿ
i“1
Vi¸2fi fl“
n
ÿ
i“1
ErV2
i s ` 2
n´1
ÿ
i“1
n
ÿ
j“i`1
ErViVj s,
36

<!-- page 72 -->
and
E» –˜n
ÿ
i“1
ZiVi¸2fi fl“ pZ
n
ÿ
i“1
ErV2
i s ` 2p2
Z
n´1
ÿ
i“1
n
ÿ
j“i`1
ErViVj s.
Therefore,
E» –1
pZ ˜n
ÿ
i“1
ZiVi¸2fi fl“
n
ÿ
i“1
ErV2
i s ` 2pZ
n´1
ÿ
i“1
n
ÿ
j“i`1
ErViVj s,
and
p1´ pZ q
p2
Z
¨ ˝E» –˜n
ÿ
i“1
Adding the last two equations,
ZiVi¸2fi fl´ pZ
n
ÿ
i“1
ErV2
i s˛ ‚“ 2p1´ pZ qn´1
ÿ
i“1
n
ÿ
j“i`1
ErViVj s.
E» –˜n
ÿ
i“1
Vi¸2fi fl“
1
p2
Z
“
1
p2
Z
E» –˜n
ÿ
i“1
E» –˜n
ÿ
i“1
ZiVi¸2fi fl´
ZiVi¸2fi fl´
p1´ pZ q
pZ
n
ÿ
i“1
ErV2
i s
p1´ pZ q
p2
Z
n
ÿ
i“1
ErZiV2
i s. (A.24)
The first term of the CCV variance estimator for least squares is based on the sample counterpart of
the right-hand side of equation (A.24), with 1tmk,i“ muRk,ippWk,i´ Wkqp
Uk,i ´ pp
τk,m´
p
τkqWkp1´
Wkqq in the role of Vi.
To derive the CCV variance estimator for the fixed effect case, consider
λk“ 1´ qk
pErAk,mp1´ Ak,mqsq2
ErA2
k,mp1´ Ak,mq2s,
and let fCCV
k“ λkfcluster
k ` p1´ λkqfrobust
k . This transformation is designed to reproduce the terms
in fk with factor
mk
ÿ
n2
k,m
nk
pτk,m´ τkq2
.
m“1
These terms dominate fk as k increases. It also reproduces several lower order terms.
Notice that
frobust
k“ ErAk,mp1´ Ak,mq2s 1
nk
nk
ÿ
i“1
e2
k,ip1q ` ErA2
k,mp1´ Ak,mqs 1
nk
nk
ÿ
i“1
e2
k,ip0q
` ´ErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2s¯mk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
` p2 ` pkqErA2
k,mp1´ Ak,mq2smk
ÿ
m“1
nk,m
nk
pτk,m´ τkq2
.
37

<!-- page 73 -->
Then,
fCCV
k´ fk “ p1´ λkqpkErA2
ÿ
k,mp1´ Ak,mq2s ˜mk
m“1
ÿ
“ pkqkpErAk,mp1´ Ak,mqsq2 ˜mk
nk,m
nk
m“1
nk,m
nk
pτk,m´ τkq2 `
1
pτk,m´ τkq2 `
nk
1
nk
ÿ
nk
i“1
pek,ip1q ´ ek,ip0qq2¸
nk
ÿ
i“1
pek,ip1q ´ ek,ip0qq2¸.
For ˜ vCCV
k“ fCCV
k {pµkp1´ µkq ´ σ2
kq2, we obtain,
˜
vCCV
k´
˜
vk“ pkqk
mk
ÿ
m“1
nk,m
nk
1
pτk,m´ τkq2 ` pkqk
nk
nk
ÿ
i“1
pek,ip1q ´ ek,ip0qq2
. (A.25)
The difference ˜ vCCV
˜
k´
vk is non-negative and of smaller order than ˜ vk. Therefore, ˜ vCCV
k {˜
vk Ñ 1
(even if ˜ vCCV
˜
k´
vk is bounded away from zero). The first term on the right-hand side of (A.25)
could be estimated to further correct the difference between the CCV estimator and the variance
ofp
τfixed
k.
A.5. Limit results
Let Xk,m be an infinite array of random variables, with rows indexed by k“ 1,2,..., and the
columns of the k-th row indexed by m“ 1,...,mk. Let
Sk“
mk
ÿ
m“1
Xk,m,
and ak“ ErSks.
A Weak Law of Large Numbers for Arrays: For each k“ 1,2,..., suppose that Xk,1,...,Xk,mk are
independent and have finite second moments. In addition, let bk be a sequence of positive constants
such that
1
b2
k
mk
ÿ
m“1
ErX2
k,ms ÝÑ 0.
Then,
Sk´ ak
bk
p
ÝÑ 0.
Proof: By Chebyshev’s inequality, for any εą 0
Pr ˆˇ ˇ ˇ ˇ
Sk´ ak
bk
ˇ ˇ ˇ ˇ
ą ε˙ď
“
ď
1
b2
kε2 varpSkq
1
mk
b2
ÿ
kε2
m“1
1
b2
kε2
mk
ÿ
m“1
varpXk,mq
ErX2
k,ms ÝÑ 0.
38

<!-- page 74 -->
A Central Limit Theorem for Arrays: For each k“ 1,2,... , suppose that Xk,1,..., Xk,mk are
independent, with zero means, ErXk,ms “ 0, and finite variances, σ2
k,m“ ErX2
k,ms, for m “
1,...,mk. Let
s2
k“
mk
ÿ
m“1
σ2
k,m.
Assume also that Lyapounov’s condition holds,
lim
kÑ8
1
s2`δ
k
mk
ÿ
m“1
Er|Xk,m|2`δ s “ 0,
for some δą 0. Then,
Sk
sk
d
ÝÑ Np0,1q.
Proof: ?, Chapter 27.
A.6. Intermediate calculations for Section A.2
The calculation of vk uses the following results.
ErpRk,iWk,i´ pkqkµkq2s “ pkqkµkp1´ pkqkµkq,
ErpRk,ip1´ Wk,iq ´ pkqkp1´ µkqq2s “ pkqkp1´ µkqp1´ pkqkp1´ µkqq,
ErpRk,iWk,i´ pkqkµkqpRk,ip1´ Wk,iq ´ pkqkp1´ µkqqs “ ´p2
kq2
kµkp1´ µkq,
ErRk,iWk,iRk,j Wk,j |mk,i“ mk,j s “ Erp2
kqkA2
k,ms “ p2
kqkpσ2
k ` µ2
kq,
and
ErpRk,iWk,i´ pkqkµkqpRk,j Wk,j´ pkqkµkq|mk,i“ mk,j s “ p2
kqkpσ2
k ` µ2
kq ´ ppkqkµkq2
“ p2
kqkpσ2
k ` p1´ qkqµ2
kq.
Similarly,
ErpRk,ip1´ Wk,iq ´ pkqkp1´ µkqqpRk,j p1´ Wk,j q ´ pkqkp1´ µkqq|mk,i“ mk,j s
“ p2
kqkpσ2
k ` p1´ qkqp1´ µkq2q.
Notice also that
ErRk,iWk,iRk,j p1´ Wk,j q|mk,i“ mk,j s “ Erp2
kqkAk,mp1´ Ak,mqs
“ p2
kqkpµkp1´ µkq ´ σ2
kq,
and
ErpRk,iWk,i´ pkqkµkqpRk,j p1´ Wk,j q ´ pkqkp1´ µkqq|mk,i“ mk,j s
“ p2
kqkpµkp1´ µkq ´ σ2
kq ´ p2
kq2
kµkp1´ µkq
“ p2
kqkpµkp1´ µkqp1´ qkq ´ σ2
kq.
39

<!-- page 75 -->
The following bounds are useful to prove Lyapunov’s condition.
Er|Rk,iWk,i´ pkqkµk|3s “ p1´ pkqkµkq3pkqkµk ` ppkqkµkq3p1´ pkqkµkq
ď cpkqk.
Let Qk,m be a binary indicator that takes value one if cluster m of population k is sampled.
E“|Rk,iWk,i´ pkqkµk|2|Rk,j Wk,j´ pkqkµk|ˇ ˇmk,i“ mk,j“ m‰
“ E“`p1´ pkqkµkq2pkAk,m ` ppkqkµkq2p1´ pkAk,mq˘
ˆ `p1´ pkqkµkqpkAk,m ` ppkqkµkqp1´ pkAk,mq˘ˇ ˇmk,i“ mk,j“ m,Qk,m“ 1‰qk
` E“`pkqkµk˘3ˇ ˇmk,i“ mk,j“ m,Qk,m“ 0‰p1´ qkq
ď cp2
kqk.
E“|Rk,iWk,i´ pkqkµk||Rk,j Wk,j´ pkqkµk||Rk,tWk,t´ pkqkµk|ˇ ˇmk,i“ mk,j“ mk,t“ m‰
“ E“`p1´ pkqkµkqpkAk,m ` ppkqkµkqp1´ pkAk,mq˘3ˇ ˇmk,i“ mk,j“ mk,t“ m,Qk,m“ 1ıqk
` E“`pkqkµk˘3ˇ ˇmk,i“ mk,j“ mk,t“ m,Qk,m“ 1ıp1´ qkq
ď cp3
kqk.
Other useful intermediate calculations.
For the moments of treatment indicators, notice that ErpWk,i´ µkq2Wk,is “ µkp1´ µkq2, and
ErpWk,i´ µkq2p1´ Wk,iqs “ p1´ µkqµ2
k. In addition,
ErWk,iWk,j |mk,i“ mk,j s “ ErA2
k,ms (for mP t1,...,mku)
“ σ2
k ` µ2
k.
Similarly, Erp1´Wk,iqp1´Wk,j q|mk,i“ mk,j s “ σ2
k `p1´µk q2. Therefore, ErpWk,i´µkqWk,j |mk,i“
mk,j s “ σ2
k and ErpWk,i´ µkqp1´ Wk,j q|mk,i“ mk,j s “ ´σ2
k. In addition,
ErpWk,i´ µkqpWk,j´ µkqWk,iWk,j |mk,i“ mk,j s
“ ErA2
k,msp1´ µkq2 (for mP t1,...,mku)
“ pσ2
k ` µ2
kqp1´ µkq2
.
Similarly,
ErpWk,i´ µkqpWk,j´ µkqp1´ Wk,iqp1´ Wk,j q|mk,i“ mk,j s “ pσ2
k ` p1´ µkq2qµ2
k,
and
ErpWk,i´ µkqpWk,j´ µkqWk,ip1´ Wk,j q|mk,i“ mk,j s “ µkp1´ µkqpσ2
k´ µkp1´ µkqq.
40

<!-- page 76 -->
varpRk,iWk,iq “ pkqkµkp1´ pk qkµkq, varpRk,ip1´ Wk,iqq “ pkqkp1´ µkqp1´ pk qkp1´ µk qq. Moreover,
covpRk,iWk,i,Rk,ip1´ Wk,iqq “ ErRk,iWk,iRk,ip1´ Wk,iqs ´ ErRk,iWk,isErRk,ip1´ Wk,iqs
“ ´p2
kq2
kµkp1´ µkq.
Recall that ErWk,iWk,j |mk,i“ mk,j s “ σ2
k ` µ2
k. Therefore, covpWk,i,Wk,j |mk,i“ mk,j q “ σ2
k. Also,
ErWk,ip1´ Wk,j q|mk,i“ mk,j s “ µkp1´ µkq ´ σ2
k.
ErRk,iWk,iRk,j Wk,j |mk,i“ mk,j s “ ErRk,iRk,j |mk,i“ mk,j sErWk,iWk,j |mk,i“ mk,j s
“ p2
kqkpσ2
k ` µ2
kq.
Similarly,
Therefore,
ErRk,ip1´ Wk,iqRk,j p1´ Wk,j q|mk,i“ mk,j s “ p2
kqkpσ2
k ` p1´ µkq2q.
and
covpRk,iWk,i,Rk,j Wk,j |mk,i“ mk,j q “ p2
kqkpσ2
k ` µ2
kq ´ p2
kq2
kµ2
k
“ p2
kqkpσ2
k ` µ2
kp1´ qkqq,
covpRk,ip1´ Wk,iq,Rk,j p1´ Wk,j q|mk,i“ mk,j q “ p2
kqkpσ2
k ` p1´ µkq2q ´ p2
kq2
kp1´ µkq2
“ p2
kqkpσ2
k ` p1´ µkq2p1´ qkqq.
In addition,
covpRk,iWk,i,Rk,j p1´ Wk,j q|mk,i“ mk,j q “ ErRk,iWk,iRk,j p1´ Wk,j q|mk,i“ mk,j s
´ ErRk,iWk,i|mk,i“ mk,j sErRk,j p1´ Wk,j q|mk,i“ mk,j s
“ ErRk,iRk,j |mk,i“ mk,j sErWk,ip1´ Wk,j q|mk,i“ mk,j s
´ ErRk,iWk,i|mk,i“ mk,j sErRk,j p1´ Wk,j q|mk,i“ mk,j s
“ p2
kqkpµkp1´ µkq ´ σ2
kq ´ p2
kq2
kµkp1´ µkq
“ p2
kqkpµkp1´ µkqp1´ qkq ´ σ2
kq.
A.7. Intermediate calculations for Section A.3
ErRk,iWk,ipWk,i´ Ak,mq|Ak,m,Qk,m“ 1,mk,i“ ms “ pkAk,mp1´ Ak,mq.
This implies
Therefore,
ErRk,iWk,ipWk,i´ Ak,mq|mk,i“ ms “ pkqkErAk,mp1´ Ak,mqs.
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Ak,mqff“ nk,mpkqkErAk,mp1´ Ak,mqs.
41

<!-- page 77 -->
For ně 1,
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqˇ ˇ ˇ
Nk,m“ nff
1
“
n
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,i˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,i´ nAk,m¸ˇ ˇ ˇ
Nk,m“ nff
“ ErAk,mp1´ Ak,mqs.
Therefore,
E«nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,m´ Ak,mqff“ ErAk,mp1´ Ak,mqs PrpNk,m ě 1q
“ qkErAk,mp1´ Ak,mqsp1 ´ p1´ pkqnk,mq.
For ně 1
ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ m,Nk,m“ n,Rk,i“ 1s
ď ErpWk,m´ Ak,mq2|mk,i“ m,Nk,m“ n,Rk,i“ 1s
ErAk,mp1´ Ak,mqs
ď
.
n
Because PrpRk,i“ 1|Nk,m“ n,mk,i“ mq “ n{nk,m, we obtain
ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ m,Nk,m“ ns ď ErAk,mp1´ Ak,mqs
nk,m
which implies
ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ m,Nk,m ě 1s ď ErAk,mp1´ Ak,mqs
,
.
nk,m
Therefore,
ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ ms
“ ErRk,iWk,ipWk,m´ Ak,mq2|mk,i“ m,Nk,m ě 1s PrpNk,m ě 1|mk,i“ mq
ErAk,mp1´ Ak,mqs
ď qk
.
nk,m
Conditional on Nk,m“ nand Ak,m, the variable Nk,m,1 has a binomial distribution with parameters
pn,Ak,mq. Then, using the formulas for the moments of a binomial distribution, we find that for
any integer n, such that 1 ď nď nk,m,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2
ˇ ˇ ˇ
Ak,m“ a,Nk,m“ nff
42

<!-- page 78 -->
“ ErpNk,m,1´ N2
k,m,1{nq2|Ak,m“ a,Nk,m“ ns
“ n2a2p1´ aq2 ` nap1´ aqp1´ 6a` 6a2q ` r1paq ` r2paq{n,
where |r1paq| and |r2paq| are uniformly bounded in aP r0,1s. Therefore,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2
ˇ ˇ ˇ
Nk,m“ nff
“ n2ErA2
k,mp1´ Ak,mq2s ` nErAk,mp1´ Ak,mqp1´ 6Ak,m ` 6A2
k,mqs
` Err1pAk,mqs ` Err2pAk,mqs{n.
It follows that
ÿ
E«mk
m“1
pτk,m´ τkq2˜nk
ÿ
i“1
“ ˜mk
ÿ
m“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2ff
pτk,m´ τkq2pnk,mpnk,m´ 1qp2
kqk ` nk,mpkqkq¸ErA2
k,mp1´ Ak,mq2s
mk
`
ÿ
pτk,m´ τkq2nk,mpkqkErAk,mp1´ Ak,mqp1´ 6Ak,mp1´ Ak,mqqs ` Opmkqkq.
m“1
Therefore,
1
nkpkqk
ÿ
E«mk
m“1
pτk,m´ τkq2˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸2ff
ÝÑpErAk,mp1´ Ak,mqs ´ p5 ` pkqErA2
k,mp1´ Ak,mq2sqmk
ÿ
m“1
` pkErA2
k,mp1´ Ak,mq2smk
ÿ
m“1
n2
k,m
pτk,m´ τkq2
.
nk
nk,m
nk
pτk,m´ τkq2
Notice that,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸4
ˇ ˇ ˇ
Ak,m“ a,Nk,m“ nff
“ ErpNk,m,1p1´ Nk,m,1{nqq4|Ak,m“ a,Nk,m“ ns
ď ErN4
k,m,1|Ak,m“ a,Nk,m“ ns
ď n4
,
Therefore,
E«˜nk
ÿ
i“1
1tmk,i“ muRk,iWk,ipWk,i´ Wk,mq¸4ff“ n4
k,mp4
kqk ˆ1 ` Oˆ1
pk minm nk,m ˙˙,
43

<!-- page 79 -->
uniformly in m.
Suppose Xk,m “ pZk,m,1 ` Zk,m,2q2. Let Xk,m,1 “ Z2
k,m,1 and Xk,m,2 “ Z2
k,m,2. Now suppose,
ErX2
k,m,1s ÝÑ 0,
mk
ÿ
m“1
and
mk
ÿ
m“1
ErX2
k,m,2s ÝÑ 0.
Using the binomial theorem and H¨older’s inequality, we obtain
mk
ÿ
ErX2
k,ms “mk
4
ÿ
ÿ
m“1
m“1
p“0
mk
4
ď c
ÿ
ÿ
m“1
p“0
mk
4
ď c
ÿ
ÿ
m“1
p“0
4
ď c
ÿ
ÿ
p“0 ˜mk
m“1
cpErZp
k,m,1Zp4´pq
k,m,2 s
Er|Zk,m,1|p|Zk,m,2|p4´pqs
pErX2
k,m,1sqp{4pErX2
k,m,2sqp4´pq{4
ErX2
k,m,1s¸p{4 ˜mk
ÿ
m“1
ErX2
k,m,2s¸p4´pq{4
ÝÑ 0.
44
