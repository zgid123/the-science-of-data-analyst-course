# Decisions on the round-4 re-test flags

Flags from `12-vi-reader-test.md` (11: clarity 1/2/3 = 0/7/4). Numbers and limitations confirmed consistent by the reader except Level 2 in Table A.2 (flag 6). Every flag fixed; "EN+VI" = fixed in the English source and the twin.

| # | Decision | Change |
| :-- | :-- | :-- |
| 1 | Fixed EN+VI | Conclusion stated: duplicates do not affect the result; "at most 0.004 in any module". |
| 2 | Fixed EN+VI | "counting the quizzes dated after their deadline as late submissions". |
| 3 | Fixed EN+VI | Leakage audit defined (information from after the prediction date or from the test runs); solution phrased as "choices learned from the data … made on the training data only". |
| 4 | Fixed EN+VI | Problem renamed "deliverables consistent and usable", so the Word compatibility point belongs to it. |
| 5 | Fixed EN+VI | Deck status checked against `reports/milestone-5/build/`: the 30-slide deck exists in English and Vietnamese; the full deck with appendix slides is English only and follows once the slide count is settled (open user decision). |
| 6 | Fixed EN+VI | Table A.2 Milestone 4: Level 2 removed from the limitation column (optional; the assigned task already says Level 1); length measured against the 6–12 pages the Milestone 1–3 briefs recommend. |
| 7 | Fixed EN+VI | Closing paragraph states the Milestone 4 benchmark. The recurring-length sentence kept: it states the cross-milestone pattern, the new sentence its effect on ratings. |
| 8 | Fixed VI | "số giả định cho trường đại học trong tình huống mà đề bài đặt ra". |
| 9 | Fixed EN+VI | "five further sources that those searches led to, rejected sources included". |
| 10 | Fixed EN+VI | Milestone 4 presentation limitation names its benchmark (6–12 pages). |
| 11 | Fixed EN+VI | "day 14 defines the population of the completion indicator; days 13 and 27 are the dates on which the contact lists are drawn up". |

Checks: parity 0 errors, 1 accepted warning; `check_pairs.py` 0 pairs with differences; twins marked. Flag counts by round: 46 → 40 → 13 → 11, clarity-1 passages 0 → 0 → 1 → 0.
