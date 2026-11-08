# 9. Ethics, Bias and Limitations

The prepared data keep gender, age band, disability, deprivation band and region in every view, outside the primary
predictor set, because a fairness audit needs them. Algorithmic bias in education is a model performing substantially
better or worse for one group than for another; it can arise through proxies even when no demographic attribute is an
input, and a data set without group membership cannot be audited at all [14]. The brief likewise allows sensitive
attributes to be kept for auditing while restricting their use as predictors [1]. On OULAD, Riazy et al. found
students with a declared disability strongly under-represented, a 5–6-point disparity in favour of male students
reproduced by most models, little gain in fairness from leaving the attributes out, and disabled students in some
cases predicted to fail with higher probability [15]. The audit groups have known sizes, 3,164 enrolments with a
declared disability and 216 aged 55 or over, so small groups are audited across runs, and the "Missing" deprivation
group is reported on its own.

Privacy rules apply at two levels. OULAD was anonymised with k-anonymity, k = 5 [2], and under Vietnam's Personal
Data Protection Law No. 91/2025/QH15 de-identified data fall outside the definition of personal data and
re-identifying them is prohibited [16], so OULAD is never linked to other sources. For the pilot on the university's
records, health information is an example of sensitive personal data [17], processing must keep to a specific
purpose [17], and the law names no general research exemption from consent [16], so the pilot needs its own legal
basis. Claims stay within the data: results describe UK distance-learning modules of 2013–2014 and must be checked on
the university's records, associations in AQ2 are not causes, no effect of contacting a student can be drawn from
OULAD, and deprivation bands are not pooled across nations [6].
