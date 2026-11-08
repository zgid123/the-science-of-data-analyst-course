# S310 – When Should You Adjust Standard Errors for Clustering? (Abadie, Athey, Imbens & Wooldridge, QJE 2023)

## Summary in my own words

The authors argue that whether and how to cluster standard errors is decided by the design — how the sample was drawn from the population and how the "treatment" (here, a student characteristic or module condition) varies across clusters — not by whether residuals are correlated within clusters. When the sample contains a large fraction of the clusters in the population, conventional cluster-robust standard errors can be severely inflated; they propose corrected variance estimators and discuss fixed-effects estimators. For an associational regression on OULAD, which contains all presentations of its seven modules, the choice between module fixed effects, cluster-robust errors and mixed models should be argued from the design.

## Key facts

- Clustered SEs widespread – "Clustered standard errors, with clusters defined by factors such as geography, are widespread in empirical research in economics and many other disciplines."
- Design component – "In addition to the common sampling component, the new framework incorporates a design component that accounts for the variability induced on the estimator by the treatment assignment mechanism."
- Inflation when most clusters are sampled – "when the number of clusters in the sample is a non-negligible fraction of the number of clusters in the population, conventional cluster standard errors can be severely inflated"
- Design decides clustering – "it is the sampling process and the treatment assignment mechanism that solely determine the correct level of clustering"
- Residual correlation alone is not the reason – "the presence of cluster-level unobserved components of the outcome variable becomes irrelevant for the choice of clustering level."
- Fixed effects estimator covered – "We derive the large sample variances for the least squares and fixed effect estimators under our proposed framework"

## Used in

03-02-descriptive-diagnostic.md, 03-01-criteria-matrix.md

## Against reference.md

Extends the outline's Part 3 "explanatory regression within module" for AQ2: module (or module-presentation) fixed effects absorb module differences; cluster-robust errors by module would rest on only 7 clusters, too few for reliable cluster-robust inference, and by this paper are not automatically required when all module runs are observed. The report should state the chosen variance method and its condition.

## Reliability

Primary; peer-reviewed article by A. Abadie, S. Athey, G. W. Imbens and J. M. Wooldridge, *Quarterly Journal of Economics* 138(1), 1–35 (2023), doi:10.1093/qje/qjac038; read from arXiv 1710.02926 (revised author version). OpenAlex cited-by count 1,505 as of 2026-11-06. Econometric framing (treatment effects); applying it to associational education regression is by analogy.

## Open questions

The "few clusters" problem (7 modules) is not a finding of this paper; it needs a source such as Cameron & Miller (2015, Journal of Human Resources), not fetched.
