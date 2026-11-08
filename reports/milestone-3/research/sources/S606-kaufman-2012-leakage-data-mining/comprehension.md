# S606 – Leakage in data mining: formulation, detection, and avoidance

## Summary in my own words

Kaufman, Rosset, Perlich (KDD 2011) and Stitelman (extended in ACM TKDD 2012) define leakage as the introduction of information about the target that should not legitimately be available to mine from. Leakage is usually unintentional, introduced during data collection, aggregation and preparation, and at minimum inflates estimated performance. They separate leakage in features from leakage in training examples, name the "no-time-machine requirement" (features may only use information from before the target's time), and propose avoidance by tagging every observation with legitimacy tags (time-stamps) and enforcing a learn-predict separation, which in the time case is a cut at a point in time between training and evaluation examples. The crawl holds the TKDD 2012 record and abstract (OpenAlex) plus the full text of the KDD 2011 conference version (three authors), because the TKDD full text is behind the ACM login.

## Key facts

- Definition (TKDD abstract) – "leakage is the introduction of information about the data mining target that should not be legitimately available to mine from"
- Leakage is usually unintentional and comes from preparation – "the introduction of this illegitimate information is unintentional, and facilitated by the data collection, aggregation and preparation process"
- Consequence – "At the very least leakage leads to overestimation of the model‟s performance."
- No-time-machine requirement – "it is implicitly required that a legitimate model only build on features with information from a time earlier (or sometimes, no later) than that of the target"
- Avoidance method – "We show that it is possible to avoid leakage with a simple specific approach to data management followed by what we call a learn-predict separation"
- Time case: tags are time-stamps and the separation is a time cut – "Learn-predict separation is implemented by a cut at some point in time that segments training from"
- Two leakage types – "leakage in features (2) and in training examples (9)"
- Missing time-stamps break separation – "Updates to database records are usually not timestamped and not stored separately"
- Nisbet R., Elder J. & Miner G. (2009, Academic Press; not in sources.md) are cited [7] as calling leakage one of the top ten data mining mistakes – "Handbook of Statistical Analysis and Data Mining Applications"
- Rosset S. et al. (2010, Data Mining and Knowledge Discovery; not in sources.md) give the intuitive definition – "The unintentional introduction of predictive information about the target by"
- Kohavi R. et al. (2000, SIGKDD Explorations; not in sources.md) describe giveaway attributes downstream of the target – "giveaway attributes that predict the target because"
- Citation traction – "cited_by_count (OpenAlex): 912"

## Used in

06-03-split-leakage.md (definition of leakage; only pre-cut-off features; time cut between training and test).

## Against reference.md

Confirms the outline's predictive-readiness rule "only pre-cut-off features, entity and time split": the cut-off rule is Kaufman's no-time-machine requirement and the time split is their learn-predict separation by time. Extends it: leakage can also enter through training examples, not only features, and records without time-stamps (in OULAD, e.g. registration fields such as date_unregistration that are filled after the cut-off) are the typical source.

## Reliability

Primary, peer-reviewed: ACM Transactions on Knowledge Discovery from Data 6(4), Article 15 (2012), DOI 10.1145/2382577.2382579; conference version KDD '11, pp. 556–563. Authors from Tel Aviv University and Media6Degrees. 912 citations in OpenAlex as of 2026-11-06 (TKDD version). The quotes from the body come from the KDD 2011 version (a course-hosted copy at cs.umb.edu); the TKDD version adds Stitelman and a causal-graph view.

## Open questions

The TKDD 2012 full text was not readable (ACM 403); claims quoting the body should cite the KDD 2011 version's wording or be checked against TKDD. The cited Nisbet (2009), Rosset (2010) and Kohavi (2000) works are not registered.
