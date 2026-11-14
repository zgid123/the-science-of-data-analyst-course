# Slide-only reading pass – 15-slide English deck (v3-15)

Deck: `reports/milestone-5/build/N04_Milestone5_Slides-15_EN.pptx`, main slides 1–15. Reader played: a manager who
hears the team's story once, without the reports. Method (build-report `slides.md`, section 1 step 3, section 2
"Every slide reads on its own"): previews from `preview_slides.py --slides 1-15` and the text from
`slidekit.py text --slides-only`, read before the speaker notes. Every item that blocks or slows understanding was
fixed in the slide code; slide functions shared with the full deck (`slides_milestone5_full/part1.py` … `part4.py`)
change the Full and Split decks too. Build and check log: `reports/milestone-5/logs/T40_deck15_reading_pass.log`.

## Pass 1: findings and fixes

| Slide | Finding | Fix |
| :---- | :---- | :---- |
| 1 | None: title, authors, course. | – |
| 2 | None: the timeline has its key (orange band, grey markers) and its basis. | – |
| 3 | "Circular 83/2026" named without saying what it is. | Glossed: "the new national rule for counting withdrawals" (plan 12, `part1.py`). |
| 4 | D1, D2, D3 used in all four cards but defined only in the key at the bottom; AQ3 "built on 2013, applied to 2014" names data years before the data are introduced (Slide 5); AQ4 "fixed capacity" is a term defined only on Slide 9. | Decisions moved to the line above the cards, next to the unit of analysis, and dropped from the key; AQ3 reads "built on one year, tested on the next"; AQ4 reads "a list as long as staff can contact" (plan 16, `part1.py`). |
| 5 | Gate names in the "Gates failed" column (dated outcome, tasks, activity, runs, licence) not defined; "quality feasibility" is a criterion name without meaning. | The intro line lists the six must-have gates in words; "quality feasibility (readable, manageable files)" (plan 24, `part2.py`). |
| 6 | None: High/Medium/Low defined, TMA and CMA spelled out, orange row keyed. | – |
| 7 | None: the three parts are defined, the orange part keyed, cut-offs restated. | – |
| 8 | "Day 0" unexplained on the timeline; "refitted inside each fold" is jargon (fold undefined); "the date-filter check is built so that it can fail" does not say why that matters. | "Day 0: module start"; control reads "Learned on the 2013 training runs only"; lead says "a test shows that the date-filter check would catch a leak", and the box ends "so a leak would show" (plan 45, `part2.py`). |
| 9 | "Precision" (in the Milestone 1 target) and "discrimination, calibration" (Framework) not defined; calibration returns on Slide 13. | "Precision is the share of the list who do not complete"; discrimination and calibration glossed in the Framework line (plan 52, `part3.py`). |
| 10 | Title term "Level 2" undefined; "Gate S1" used without definition (defined only in the key of Slide 14); identifiers B2 and B3 in the table unexplained; normalised recall 0.725 and the column "Share of list not completing" 72.5% look like two different numbers. | Key adds "Level 2 = the brief's optional level: running the model test fixed in Milestone 4"; box reads "Gate S1, the test for replacing the rule, is met: normalised recall (here the last column) …"; rows read "Early-sign rule, ranked by number of signs" and "Model using background only" (plan 59, `part3.py`). |
| 11 | "Prepared views" is internal jargon. | "Prepared and raw counts agree in all 176 outcome cells" (plan 64, `part3.py`). |
| 12 | None: dots, whiskers, dashed line and colours keyed; risk difference and population defined. | – |
| 13 | "Calibration fails" relies on a term the manager may not hold; "rule FR1" and "the three groups fixed in advance" are identifiers without content. | "The predicted risks match the observed rates (calibration) in only 5 of the 13 runs"; FR1 stated as its rule (a group reached more than 10 points less well) with the three groups named (plan 76, `part4.py`). |
| 14 | "The key effect" unclear; "tuning measure" and "log loss" bare; the key defines "Change Log", which no cell uses. | "Duplicates move the early-click effect by ≤ 0.004"; "Log loss chosen and disclosed; both changes in the Change Log"; "Gate S1 met under log loss and under recall" (`slides_milestone5_15/path.py`). |
| 15 | None: three numbered points, each with its evidence line. | – |

## Pass 2: changed slides (3, 4, 5, 8, 9, 10, 11, 13, 14)

| Slide | Finding | Fix |
| :---- | :---- | :---- |
| 3–14 | Every term listed in pass 1 is now defined on the slide where it is used; no new undefined term, overflow or overlap in the previews. | – |
| 5 | First rebuild: check_slides warned "shape off the slide" for the bottom text block. | Gloss shortened to "(readable, manageable files)"; warning cleared. |
| 10 | "Penalised logistic model" stays as the report's method name; the lead and the table make clear it is the model being compared. | Kept; the notes call it "the simple penalised logistic model". |

## Speaker notes

The 15 notes in `speech-script.md` were first rewritten at a middle level; they now walk through each slide end to end (T46): each walks through its visual, states the point
with one or two key numbers and their population, says what happened along the way where the slide is about the
team's path, and hands over to the next slide. Lengths: 143–175 words each, 2,449 words in total, about 19.6 minutes
at 125 words a minute.

## Checks

- `build_slides_milestone5_15.py --lang en`: no `! en` room lines.
- `check_slides.py N04_Milestone5_Slides-15_EN.pptx --lang en --task milestone-5`: 0 errors, 0 warnings.
- `build_slides_milestone5_full.py --layout both`, then `check_slides.py` on `N04_Milestone5_Slides-Full_EN.pptx` and
  `N04_Milestone5_Slides-Split_EN.pptx`: 0 errors, 0 warnings each.
- Still open: the Vietnamese strings of the changed English text (translators' table `slides_milestone5_15_vi.py`).
