# S604 – OU Analyse website (The Open University)

## Summary in my own words

The OU Analyse website (analyse.kmi.open.ac.uk, now redirected to research.stem.open.ac.uk/ouanalyse/) describes the system in a few sentences. fetch.py could not convert the page (exploded layout), so the readable text comes from a WebFetch extract: OU Analyse uses machine learning for early identification of students at risk of failing, and each student's risk of failing the next assignment is updated weekly for tutors and Student Support Teams. The page is staff-facing and does not describe how models are trained.

## Key facts

- Purpose of the system – "OU Analyse is a system powered by machine learning methods for early identification of students at risk of failing."
- Weekly update, target is the next assignment – "All students with their risk of failure in their next assignment are updated weekly"
- Recipients of the predictions – "made available to the course tutors and the Student Support Teams to consider appropriate support."

## Used in

06-03-split-leakage.md (weekly prediction cadence before the next assessment).

## Against reference.md

Confirms that the OU predicts at weekly points tied to the next assessment, which supports the outline's choice of week-based prediction points (end of week 2 = day 13, end of week 4 = day 27). It does not fix those particular days.

## Reliability

Primary institutional page (The Open University, KMi / STEM Faculty), undated. The text is a WebFetch extract (model-assisted, quotes requested verbatim), so status partial; quotes should be treated as close to, but not guaranteed to be, the page wording.

## Open questions

No date on the page; no training method stated (see S605).
