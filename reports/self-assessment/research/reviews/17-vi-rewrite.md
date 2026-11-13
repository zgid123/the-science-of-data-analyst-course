# Decisions on the reader-test flags of the per-milestone restructure

Flags from `16-vi-reader-test.md` (26: clarity 1/2/3 = 0/15/11). "EN+VI" = fixed in the English source and the twin.

| Flag | Decision | Change |
| :-- | :-- | :-- |
| 1 stakeholder rating (01-00:11, 03-02:13) | Fixed EN+VI | What is missing stated: the requirements still need confirming with real university staff. |
| 2 "tám lỗi do AI…" | Fixed EN+VI | "eight errors in our code found by an AI audit for leakage (information from after the prediction date reaching the analysis)". |
| 3 Milestone 4 metric | Fixed EN+VI | Primary metric defined: share of later non-completers on a list as long as the contact capacity. |
| 4 baseline scope, term pair | Fixed EN+VI | "a baseline for every question"; one Vietnamese term "nhóm kỹ thuật dự kiến" in Table 1.1 and Table A.5. |
| 5 day 14 vs 13/27 | Fixed EN+VI | AQ1 names day 14 as the reference day of the completion indicator. |
| 6 AQ3 sentence | Fixed EN+VI | Split; "lists of 5 students in every 20"; the gain called small but beyond chance in a paired test (Milestone 5 Section 10: interval +0.006 to +0.036, p = 0.0035). |
| 7 group of 20 | Fixed EN+VI | "tutor group of 20 students (the students one tutor supports)". |
| 8 calibration limit | Fixed EN+VI | Stated as a limit of the result, not of the report; "staff" / "cán bộ" for who sees the list. Kept out of Table A.6: it is a finding the report interprets correctly, not a shortfall of a criterion. |
| 9 tuning measure timing | Fixed EN+VI | Checked against Change Log C18 (Milestone 5 package): log loss chosen after the 2014 test result of the Milestone 4 draft (recall tuning, S3 failed) was known; gate S1 met under both measures, so only calibration depends on it. Stated in Table 1.1, Table 1.2, Table 2.1 and Table A.6. |
| 10 one definition vs changes | Fixed EN+VI | One definition within each report; changes between milestones logged and later reports use the new one. |
| 11 93 withdrawals, Cliff's delta | Fixed EN+VI | Missing withdrawal day kept empty with an indicator (Milestone 3 decision); Cliff's delta sentence already split. |
| 12 "lựa chọn học từ dữ liệu" | Fixed EN+VI | "every value the preparation learns from the data … learned from the training data only"; one term for the indicator column. |
| 13 why the two facts are problems | Fixed EN+VI | Two implementations could disagree; seeing the 2014 runs could have shaped the model. |
| 14 Appendix I repetition, 6–12 | Fixed EN+VI | Duplicate length sentence removed; "6–10 or 8–12 pages" everywhere. |
| 15 limitations row | Fixed VI | Two cases named after a colon. |
| Clarity 3 fixed | Fixed | "51 câu trích dẫn lời các bên liên quan" (EN+VI); "phiên bản mã" for implementation; "phát hiện nhóm sinh viên nào bị bất lợi" for the fairness rule (EN+VI); "mang tính khẳng định" removed. |
| Clarity 3 kept | Kept | "câu chuyện", "tính kết dính" (the team's reference form; glossary row added for coherence); "mắt xích" (Milestone 5's own term for its eleven-link chain); "người dịch và người rà soát" (AI use reported per milestone); "nêu đúng ở mức bằng chứng" (the brief's own criterion wording); "đối chiếu từng byte" (precise); "điều kiện về hiệu chuẩn" (glossary S3 sense). |

Checks: parity 0 errors, 1 accepted warning; `check_pairs.py` 0 differences; four twins marked.
