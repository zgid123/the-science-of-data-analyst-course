# S404 – The precision-recall plot is more informative than the ROC plot on imbalanced datasets (Saito & Rehmsmeier, PLOS ONE 2015)

## Summary in my own words

Using a confusion-matrix example, simulations and a literature review, the paper shows that ROC plots, whose baseline is fixed at the diagonal, can look reassuring on strongly imbalanced data because specificity is computed over the large negative class. Precision (positive predictive value) depends on the class ratio, so the precision–recall (PRC) plot and its area move with prevalence: the random baseline of AUC-PR equals P/(P+N). The authors recommend PRC plots as the most informative visual tool for imbalanced data, and they note that early-retrieval performance – the quality of a limited number of top-ranked instances – matters when examining every positive prediction is costly. For OULAD, where non-completion is about 44–45% of enrolments, the imbalance argument is weak, but the early-retrieval argument applies directly to contacting only 3–5 students per group of about 20.

## Key facts

- Main finding – "the visual interpretability of ROC plots in the context of imbalanced datasets can be deceptive with respect to conclusions about the reliability of classification performance, owing to an intuitive but wrong interpretation of specificity."
- PRC advantage – "PRC plots, on the other hand, can provide the viewer with an accurate prediction of future classification performance due to the fact that they evaluate the fraction of true positives among positive predictions."
- ROC baseline – "AUC is 0.5 for random and 1.0 for perfect classifiers"
- PRC baseline moves – "the baseline of PRC is determined by the ratio of positives (P) and negatives (N) as y = P / (P + N)."
- AUC-PR of a random classifier – "the AUC (PRC) of random classifiers is 0.5 only for balanced class distributions, whereas it is P / (P + N) for the general case"
- Only some measures react to imbalance – "Only precision, MMC, and the three Fβ scores vary between the two datasets, while the majority of measures stay unchanged"
- Early retrieval – "it is practical to check the performance of the early retrievals, which only examines a limited number of top-scoring instances."
- Choose measures for the target class distribution – "it is important to consider the class distribution of the data at hand or to be analysed in future applications and to select appropriate measures for meaningful performance evaluations."
- Interpolation – "the interpolation methods for PRC and ROC curves differ—ROC analysis uses linear and PRC analysis uses non-linear interpolation"
- Recommendation – "The results of our study strongly recommend PRC plots as the most informative visual analysis tool."
- Cites Davis J. & Goadrich M. (ICML 2006) for the one-to-one ROC–PRC relation – "A PRC curve has a one-to-one relationship with a corresponding ROC curve"

## Used in

04-03-metrics-success.md

## Against reference.md

Extends the outline's metrics bullet "gain over base rate and recall at capacity, discrimination": the paper supports reporting precision against its base-rate baseline (P/(P+N)) and judging top-ranked (early-retrieval) performance, which matches "gain over base rate" and "recall at capacity". Partly qualifies the card's framing "precision–recall versus ROC under imbalance": with non-completion near 44–45% the OULAD target is close to balanced, so the paper's core imbalance argument applies weakly; its argument for top-k evaluation still applies because the contact capacity (3–5 of about 20) flags 15–25% of a group.

## Reliability

Primary; peer-reviewed article by Saito T. and Rehmsmeier M. (University of Bergen); PLOS ONE 10(3):e0118432 (2015); open access. Citation traction: 5206 Crossref / 5790 OpenAlex citations as of 2026-11-06. Current as of November 2026 (single version; the evidence is from bioinformatics simulations and transfers by analogy).

## Open questions

Precision and recall at a fixed top-k per tutor group (rather than a global threshold) are not discussed; the report must define them itself.
