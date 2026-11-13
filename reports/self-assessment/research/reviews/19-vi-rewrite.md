# Decisions on the reader re-test flags (per-milestone restructure)

Flags from `18-vi-reader-test.md` (14: clarity 1/2/3 = 1/12/1). "EN+VI" = fixed in the English source and the twin.

**Rating correction (EN+VI).** Flags 10 and 13 led to Change Log entry C16 (Milestone 5 package): the plan (C07) tested on the 9 paired runs of 2014; Milestone 3 kept all 13 runs without a Change Log entry ("3–4, recorded in 5"). The Milestone 3 criterion "Link with Milestones 1–2, scope consistency and Change Log" is therefore Mostly met. Totals 37 met / 8 mostly met of 45 (M3 9/1), recounted by script in both languages.

| # | Decision | Change |
| :-- | :-- | :-- |
| 1 "kể lại mục tiêu" | Kept | The team's reference form uses "kể một câu chuyện liền mạch". |
| 2, 12 why the M2 table limits the rating | Fixed EN+VI | The brief grades the table by analytics level; it sits in an appendix with only a summary in the main text; length lowers no rating for Milestone 2. |
| 3, 14 recall reads as precision | Fixed VI | "tỷ lệ phát hiện (recall), tức phần trăm sinh viên về sau không hoàn thành học phần được danh sách gọi tên" in Table 1.1 and Table A.5. |
| 4 day 14 | Fixed EN+VI | AQ1 states that the lists themselves are drawn up on days 13 and 27. |
| 5 "nhóm hướng dẫn" | Fixed VI | "cứ mỗi 20 sinh viên do một giảng viên hướng dẫn phụ trách" (no "nhóm"). |
| 6 "three limitations" with five clauses | Fixed EN+VI | Numbered (1)–(3), each a sentence. |
| 7 (clarity 1) other measure never named | Fixed EN+VI | Named as recall at capacity, used by the Milestone 4 draft, in Table 1.1, Table 2.1 and Table A.6. |
| 8 test-set extension unexplained in Table 1.2 | Fixed EN+VI | "from 9 to 13 runs of 2014". |
| 9 "rút ra" twice | Fixed VI | Rewritten with one verb. |
| 10, 13 test-set story | Fixed EN+VI | Planned 9 paired runs, grown in Milestone 3 to 13; rating correction above. |
| 11 calibration condition undefined | Fixed EN+VI | "log loss also rewards predicted risks that match the observed rates, the calibration condition S3". |

Checks: parity 0 errors, 1 accepted warning; `check_pairs.py` 0 differences (one VI repeat of "14" caught and fixed); twins marked.
