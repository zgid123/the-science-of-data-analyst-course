# 9. Ethics, Bias and Limitations

**Sensitive attributes kept for audit.** The prepared data keep gender, age band, declared disability, deprivation
band and region in every view, outside the primary predictor set, because a fairness audit needs them. Algorithmic
bias in education is a model that performs substantially better or worse for one group of students than for another;
it can arise through proxies even when no demographic attribute is an input, and a dataset without group membership
cannot be audited at all [14]. Removing the attributes would therefore hide bias rather than prevent it. The brief
likewise allows sensitive attributes to be kept for auditing while restricting their use as predictors [1]. Highest
education, the sixth attribute listed in Section 2.3, is a predictor, because prior qualifications describe a student's
preparation for the module; it stays in every view, so its groups can be audited as well. Whether the five audit
attributes should also be predictors is a policy choice, which Milestone 4 examines by comparing models with and
without them.

**What earlier work on OULAD shows.** A study of fairness on OULAD found students with a declared disability strongly
under-represented, a disparity of five to six points in favour of male students reproduced by most models, little
gain in fairness from leaving the attributes out, and disabled students in some cases predicted to fail with a higher
probability [15]. The audit of this project is designed with these findings in mind. The audit groups have known
sizes, 3,164 enrolments with a declared disability and 216 aged 55 or over, so small groups are audited across runs
rather than run by run. The "Missing" deprivation group is reported on its own, because its students succeed more
often (Section 3.2), and merging it into a band would distort that band's rate.

**Privacy.** Privacy rules apply at two levels. OULAD was anonymised with k-anonymity, k = 5, meaning that every
combination of the attributes that could identify a student is shared by at least five students [2]. Under Vietnam's Personal Data
Protection Law No. 91/2025/QH15, de-identified data fall outside the definition of personal data, and re-identifying
them is prohibited [16], so OULAD is never linked to any other source. For the pilot on the university's own records,
the rules are stricter: health information, such as a declared disability, is an example of sensitive personal data
[17], processing must keep to a specific purpose [17], and the law names no general exemption from consent for
research [16], so the pilot needs its own legal basis before any student record is prepared.

**Limits of the claims.** Four limits follow from the data. Results describe UK distance-learning modules of 2013–2014
and must be checked on the university's records before they inform a decision. The associations of AQ2 are not
causes: a sign that goes with non-completion may be a symptom of the same difficulty rather than its source. No
effect of contacting a student can be drawn from OULAD, because it records no contact. And deprivation bands are not
pooled across the nations of the UK, since each nation uses its own index [6].
