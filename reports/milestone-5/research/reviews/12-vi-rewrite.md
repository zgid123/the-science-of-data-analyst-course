# Decisions on the reader-test flags of the 15-slide deck

Flags from `11-vi-reader-test.md` (35: clarity 1/2/3 = 1/18/16). EN+VI = fixed in the English source and the Vietnamese; VI = Vietnamese only.

| # | Decision | Change |
| :-- | :-- | :-- |
| 1 | Fixed EN+VI | Pointer reads "Detail on appendix slides A2–A9" / "Chi tiết ở các slide phụ lục …" (build_slides_milestone5_15.py). |
| 2 | Fixed EN+VI | Slide 2: "(assumed: the university is a case scenario)" / "(số giả định, vì trường đại học là một tình huống giả định của đề bài)". |
| 3 | Fixed VI | Slide 3 title "Mục tiêu của tổ chức (Business Goal) và mục tiêu SMART". |
| 4 | Fixed EN+VI | AQ3 card: "data up to day 13 or 27 (end of week 2 or 4)"; notes say the days count from the run's start. |
| 5 | Fixed VI | Unit line glosses "module là học phần trong OULAD"; glossary kept (module = OULAD unit, học phần = course). |
| 6 | Fixed EN+VI | Slide 4 notes name the decisions and questions in words, without D1–D3 or AQ codes. |
| 7 | Fixed EN+VI | UCI rows labelled: "UCI 697 (dropout)", "UCI 320 (school pupils)", "UCI 856 (one survey)"; notes say where UCI comes from. "Bộ dữ liệu ứng viên" kept (glossary). |
| 8 | Fixed EN+VI | Decision cell "Được chọn, kèm ba điều kiện"; the side text names the three conditions and that the files confirmed them. |
| 9 | Fixed EN+VI | Slide 5 notes state the three conditions and that they were met. |
| 10 | Fixed EN+VI | Medium = "it shifts a number by an amount we can measure" / "làm lệch một con số ở mức đo được". |
| 11 | Fixed EN+VI | "marked, capped or grouped as 'Missing'" / "được đánh dấu, giới hạn hoặc gộp vào nhóm 'Thiếu'". |
| 12 | Fixed EN+VI | Slide 6 notes: the early-click effect is measured on a scale from −1 to 1, so 0.004 is negligible. |
| 13 | Fixed EN+VI | Slide 7: the late-quiz block removed from the slide (detail stays in the appendix and notes). |
| 14 | Fixed EN+VI | "Scales computed on all runs, test year included" / "Thang đo tính trên mọi kỳ mở, kể cả năm kiểm thử". |
| 15 | Fixed EN+VI | "Kept, as in real use; also tested without them" / "Giữ như thực tế; kiểm tra thêm khi bỏ ra". |
| 16 | Fixed EN+VI | Check box gives totals (26,755 of 28,069; 25,663 of 27,535) and its conclusion: a leak would show. |
| 17 | Fixed EN+VI | Notes: "a check that always passed and so could catch nothing". |
| 18 | Fixed EN+VI | Notes say the conclusion aloud: if a leak existed, the date check would show it. |
| 19 | Fixed EN+VI | "so the best possible recall in a training run is 46% to 100%". |
| 20 | Fixed EN+VI | Lift dropped from slide 9 (defined on the appendix slides that use it); TRIPOD+AI line replaced by plain "What else is judged". |
| 21 | Fixed VI | Gate box: "Đạt điều kiện S1 (ngưỡng để mô hình thay quy tắc)"; the notes define S1 as well. |
| 22 | Fixed VI | Gate: "tỷ lệ phát hiện chuẩn hóa 0,725 (= 72,5% ở cột cuối)". |
| 23 | Fixed EN+VI | Notes: "the optional prototype test that the brief calls Level 2"; "more complex model" replaces "challenger". |
| 24 | Fixed EN+VI | Notes name "the third column, the share of all non-completers on the list". |
| 25 | Fixed EN+VI | Slide 11: "two independent counts, from the prepared and the raw data, agree exactly". |
| 26 | Fixed EN+VI | Slide 12 notes: fewer numbers; silence signs "roughly 9 to 16 points each", matching the chart (8.7–15.8). |
| 27 | Fixed EN+VI | "Of the students only the model picks, 59.7% do not complete; of those only the rule picks, 50.6%." |
| 28 | Fixed EN+VI | "FR1" replaced by "the fairness rule" on slide 13 (shared slide, also the full deck). |
| 29 | Fixed EN+VI | Reconciled: lists tested at 5 per 20; the contact curve shows effort pays up to about the sixth name, so 5 to 6 per 20 (slides 13 and 15, notes and take-home line). |
| 30 | Fixed EN+VI | Slide 14 cell: "Duplicates barely matter: the early-click effect moves ≤ 0.004 on a −1 to 1 scale". |
| 31 | Fixed EN+VI | "The plan did not say how to tune the model" / "Kế hoạch chưa nêu cách tinh chỉnh mô hình". |
| 32 | Fixed EN+VI | Notes: "a standard accuracy measure, said openly when we chose it"; log loss stays only in the slide key. |
| 33 | Fixed EN+VI | Slide 15 notes: Vietnamese rules list systems that rank learners among high-risk uses of AI and require a person to keep control of every decision (Milestone 5 report, Appendix XV). |
| 34 | Fixed EN+VI | Thank-you removed from slide 15's notes; slide 16 has its own notes (build script applies v3 notes to the closing slide). |
| 35 | Fixed EN+VI | Slide 16 notes rewritten without English names, "pipeline" or the add-drop rule. |

Checks after the fixes (logs/T42_reader_fixes.log): 15-slide EN and VI check_slides 0 errors, 0 warnings, no room lines, no missing strings; Full and Split EN 0 errors, 0 warnings.
