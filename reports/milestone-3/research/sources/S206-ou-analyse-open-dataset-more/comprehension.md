# S206 – OU Analyse: Open University Learning Analytics dataset (dataset page)

## Summary in my own words

This is the current OU Analyse page describing OULAD (the old address analyse.kmi.open.ac.uk/open_dataset now redirects to research.stem.open.ac.uk/ouanalyse/). It gives the column definitions that complement the data descriptor (S002) and is more explicit about time: assessment `date` is the final submission date in days since the presentation start, `date_unregistration` and studentVle `date` are days relative to the start, and `sum_click` counts interactions with a material in that day. It confirms B = February start, recommends analysing B and J presentations separately, places a missing exam date at the end of the last presentation week, and defines `is_banked` as a result transferred from a previous presentation. It spells IMD as "Index of Multiple Depravation" and gives no definition of the bands or of the nations covered.

## Key facts

- B = February – "for the presentation starting in February" (code_presentation is the year plus a letter, B for February)
- Separate B and J – "it is good practice to analyse the B and J presentations separately."
- Assessment date – "information about the final submission date of the assessment calculated as the number of days since the start"
- Weight – "weight of the assessment in %."
- Missing exam date – "If the information about the final exam date is missing, it is at the end of the last presentation week."
- Unregistration – "the student’s unregistered date from the module presentation, this is the number of days measured relative to the start"
- is_banked – "a status flag indicating that the assessment result has been transferred from a previous presentation."
- No submission, no row – "If the student does not submit the assessment, no result is recorded."
- sum_click per day – "the number of times a student interacts with the material in that day."
- VLE date – "the date of student’s interaction with the material measured as the number of days since the start"
- activity_type – "the role associated with the module material."
- week_from / week_to – "the week from which the material is planned to be used." and "week until which the material is planned to be used."
- imd_band – "specifies the Index of Multiple Depravation band of the place where the student lived during the module-presentation."
- studied_credits – "the total number of credits for the modules the student is currently studying."
- Citation – the page asks users to cite Kuzilek J., Hlosta M. & Zdrahal Z. (Scientific Data 2017; S002).

## Used in

02-00-data-understanding.md, 02-01-population-unit-keys.md, 02-02-outcome-time-measures.md, 02-03-codes-sensitive.md, 03-01-shape-keys-joins.md, 03-02-missingness-validity.md.

## Against reference.md

Confirms the outline's Section 2 items (time semantics, measurement semantics, categorical codes) and the descriptor S002. One wording difference against S002: S002 calls assessment `date` "the cut-off day", this page "the final submission date"; both mean the deadline day relative to the presentation start.

## Reliability

Primary: the dataset publisher's own page (OU Analyse, Faculty of STEM, The Open University); no date on the page (as of 2026-11-06). Read through WebFetch with a per-field verbatim prompt because the HTML conversion was unreadable; quotes are WebFetch extracts, status partial.

## Open questions

The page lists no errata or known issues (duplicates, "Withdrawal" vs "Withdrawn"); the WebFetch summary also did not reproduce the final_result category list. Whether day 0 is the "official module start date" is stated only in S002 ("from module start date to module end date").
