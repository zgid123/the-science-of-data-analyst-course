# S207 – Howard (arXiv 2025): ouladFormat R package

## Summary in my own words

Emma Howard (Trinity College Dublin) presents the ouladFormat R package, which loads, cleans and reshapes OULAD into one row per student. The paper documents data handling choices that matter for Milestone 3: students who unregistered before the start (for example on day −8) have no assessment rows, so student counts differ by table; repeat students (students in more than one presentation) need a keep-or-remove decision; withdrawn students should be removed only if they withdrew up to the analysis week; missing assessment submissions are treated as NA and replaced by 0 or dropped. Its code uses the final_result level "Withdrawn", not the descriptor's "Withdrawal". It confirms B = February and J = October starts and shows a module (DDD-2013J) with six tutor-marked continuous assessments.

## Key facts

- Counts differ by table – "Student 3733 unregistered on day -8 (eight days before the start of the teaching semester), and therefore, there are no assessment data available for student 3733."
- B and J – "(B indicates a February start date and J indicates an October start date)"
- Repeat students – "The repeat_\_students parameter indicates whether repeat students should be removed or kept."
- Withdrawn by week – "it removes students who withdrew from the module up to and including the week indicated by the week_\_end argument"
- Label used in data – the package code sets the final_result levels `Distinction, Pass, Fail, Withdrawn` (crawl line 645), and the text lists the results as "(withdrawn, fail, pass and distinction)"
- Missing submissions – "For this calculation, the NAs may be excluded or replaced by 0 (default) through using the na.rm parameter."
- Exam excluded – "Any (end-of-semester) examination data is not included in the calculation."
- DDD-2013J – "For DDD-2013J, there were six continuous assessments; all marked by a tutor."
- Drousiotis E. et al. (2021; not in sources.md) predicted final results early from first assessment mark, clicks and registration date – "Drousiotis et al. ((2021)) aimed to identify at-risk students by predicting students’ final results"
- Treuiller C. & Boyer A. (2021; not in sources.md) define reactivity as the delay between submission and deadline – "Treuiller & Boyer ((2021)) define reactivity for the OULAD as the delay between the date the assessment is returned and the deadline (in days)."
- Kuzilek J., Hlosta M. & Zdrahal Z. (Scientific Data 2017; S002) is the descriptor the package relies on.

## Used in

03-01-shape-keys-joins.md (per-table counts, repeat students), 03-02-missingness-validity.md (missing submissions, Withdrawn label), 02-02-outcome-time-measures.md (withdrawal up to a week).

## Against reference.md

Extends the outline's Section 3 items "missingness, duplicates and keys". Conflict with the descriptor S002, not the outline: S002 says unregistered students "have Withdrawal as the value of the final_result", S207's code uses "Withdrawn".

## Reliability

Secondary for OULAD facts (third-party preprint, not the data publisher); arXiv 2501.08366v2 (stat.CO), 16 January 2025, CC BY 4.0; the package is on CRAN. Not peer-reviewed as far as the crawl shows; citation traction not checked (metadata lookup failed, as of 2026-11-06).

## Open questions

The paper does not quantify duplicate rows in studentVle or missing `imd_band`; those must be counted from the data (Part 3 profiling). The label "Withdrawn" should be confirmed by counting `final_result` values in studentInfo.csv.
