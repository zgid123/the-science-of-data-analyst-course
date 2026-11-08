# S105 – N04 (2026). Prepared Data Package OULAD-N04-prepared-1.0: metadata (team's own package)

## Summary in my own words

This source is the metadata of the Milestone 3 Prepared Data Package: the README with the rebuild command and the steps, the Controlled Change Log C01–C13, the data dictionary, decision matrix, feature and split specifications, lineage, predictor sets, transform parameters, transformation log, validation summary and version manifest. It shows how the prepared dataset is rebuilt from the pinned raw files (figshare DOI, SHA-256 checks), which columns a model may read (20 primary, 10 extended, weekly clicks; the CMA score excluded from Milestone 4), how the 2013/2014 split and the paired subset are defined, and the observed values of every validation check. The version manifest names OULAD-N04-prepared-1.0 with hashes and row counts of each view.

## Key facts

- Rebuild – "Two runs from raw write identical files: the SHA-256 of all eight views is equal across runs."
- Raw download fallback – "Otherwise it downloads the OULAD archive from the"
- Licence – "License of the data: CC BY 4.0; cite Kuzilek, Hlosta and Zdrahal (2017), Scientific Data 4, 170171."
- Model inputs – "identifier, split, evaluation, target, rule and audit columns are never inputs"
- Reporting rule – "Report test results for paired and unpaired runs separately, and with"
- Predictor rule – "the only columns a model may use; everything else in a feature view is id, split, evaluation, target, rule or audit"
- CMA score excluded – "known for fewer than 10% of training rows at both cut-offs"
- Paired subset – "Paired subset: the 9 test runs whose module and start month also ran in 2013"
- Split – "Split by run year: training 2013B, 2013J (9 runs); test 2014B, 2014J (13 runs)"
- De-duplicated clicks – "38,247,422 ≤ 39,506,354"
- Rule rates by run – "[0.0838, 0.4401]"
- Manifest – "2026-11-06T15:24:17Z"
- Change log scope – "None changes the Business Goal or the decisions D1–D3."

## Used in

06-01-quality-findings.md, 07-01-features-leakage.md, 07-02-prepared-dataset.md.

## Against reference.md

Confirms the outline's Part 7 ("final prepared dataset and version; reproducible pipeline") and the baseline note "prepared dataset `OULAD-N04-prepared-1.0`". Confirms the brief's Final Project Package needs (source, provenance/licence, access instructions, data dictionary): the README gives the DOI, licence and rebuild command.

## Reliability

Primary: the team's own package files, copied verbatim from the repository at commit 19d35a4 (17 files). Machine-written files (validation summary, manifest, predictor sets) come directly from the pipeline. No citation traction applies (as of 2026-11-08).

## Open questions

- The README states the run takes "about 15 seconds" while the Milestone 3 report (S103) states about 20 seconds; immaterial, but the report should not quote a run time.
- The manifest records that the package had uncommitted changes when it was created; the Final Project Package should be rebuilt from a committed state and its manifest checked before submission (T21).
