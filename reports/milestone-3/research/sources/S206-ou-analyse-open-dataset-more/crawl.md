---
id: S206
url: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/
requested: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/
fetched: 2026-11-06T08:27+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T05
part: 2
raw: none
conversion: html-text of https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ (unreadable, 1212 words)
---
No readable copy was found. Attempts:
- L1 https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/: unreadable (exploded layout (36% of lines have ≤2 characters))
- L3 https://web.archive.org/web/2id_/https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/: error (HTTP 404)

<!-- fetch 2: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ | WebFetch (L5) | 2026-11-06T08:27+07:00 | partial -->
tool: WebFetch
fetch_prompt: "For each of these fields, copy the exact single sentence (or bullet line) from the page that describes it, word for word, in quotation marks, one per line: code_presentation, length, date (assessments), weight, the sentence about missing exam date, date_unregistration, is_banked, score, the sentence about missing submissions, sum_click, date (studentVle), activity_type, week_from, week_to, imd_band, studied_credits, final_result, and the sentence recommending analysing B and J presentations separately. Do not paraphrase."

- code_presentation: "code name of the presentation. It consists of the year and “B” for the presentation starting in February"
- length: "length of the module-presentation in days."
- date (assessments): "information about the final submission date of the assessment calculated as the number of days since the start"
- weight: "weight of the assessment in %."
- Missing exam date: "If the information about the final exam date is missing, it is at the end of the last presentation week."
- date_unregistration: "the student’s unregistered date from the module presentation, this is the number of days measured relative to the start"
- is_banked: "a status flag indicating that the assessment result has been transferred from a previous presentation."
- score: "the student’s score in this assessment. The range is from 0 to 100."
- Missing submissions: "If the student does not submit the assessment, no result is recorded."
- sum_click: "the number of times a student interacts with the material in that day."
- date (studentVle): "the date of student’s interaction with the material measured as the number of days since the start"
- activity_type: "the role associated with the module material."
- week_from: "the week from which the material is planned to be used."
- week_to: "week until which the material is planned to be used."
- imd_band: "specifies the Index of Multiple Depravation band of the place where the student lived during the module-presentation."
- studied_credits: "the total number of credits for the modules the student is currently studying."
- final_result: "student’s final result in the module-presentation."
- B/J recommendation: "it is good practice to analyse the B and J presentations separately."

Several quotes are shortened to exact fragments to stay within the 125-character limit. The page also contains "Depravation," which is the original spelling.
