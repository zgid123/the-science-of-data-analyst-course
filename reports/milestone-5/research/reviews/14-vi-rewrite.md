# Decisions on the reader re-test flags of the 15-slide deck

Decisions on the 34 flags of the Vietnamese reader re-test (13-vi-reader-test.md). Each fix was made in English first
(slide code in `slides_milestone5_full/part*.py` and `slides_milestone5_15/path.py`, notes in
`presentation/v3-15/speech-script.md`), then carried into `slides_milestone5_15_vi.py` after `slidekit.py sync`; rows
marked (VI) changed only the Vietnamese. Facts follow the Milestone 5 report. Build and checks:
`logs/T43_reader_fixes2.log`.

| # | Decision | Change or reason |
| :-- | :-- | :-- |
| 1 | Fixed | Title slide carries no appendix pointer (`owners()` skips plan 1); subtitle reads "from the problem to the answers and the decisions they support". |
| 2 | Fixed (VI) | Unit line defines "kỳ mở" as one offering of a module; OULAD not named before slide 5. |
| 3 | Rejected | UCI 697, 320, 856 are the public repository names of the candidate datasets, each given with its label ("bỏ học" …); the ids let a reader find the set, and the scores carry the comparison. |
| 4 | Fixed | The six gates are listed one by one: dated outcome, dated tasks, dated activity, ≥ 3 runs in time order, open licence, anonymised ID. |
| 5 | Fixed | Note split in two sentences: scores count only what the documentation states, so OULAD gets 12; chosen on three conditions its files confirmed. |
| 6 | Fixed | "rated against the four analytical questions". |
| 7 | Fixed | "7 of 9 have one due by day 27" ("đến hạn"). |
| 8 | Fixed | Cell states what is computed: "Means and scales set on all runs, test year included" (VI "Trung bình, độ lệch để chuẩn hóa tính cả năm kiểm thử"). |
| 9 | Fixed (VI) | "Giữ như thực tế; kiểm tra thêm khi loại" in the row of the 1,586 enrolments, so the object is the row's own count. |
| 10 | Fixed | Lead defines leakage and says the date check catches it; proof box says only enrolments with later clicks change when the filter is off, so a leak would show. |
| 11 | Fixed | Ceiling tied to the example: "a list of k holds at most k non-completers. In the example the best is 5 of 9; across the training runs …". |
| 12 | Fixed | Gate line: normalised recall 0.725 equals the last column; the model ranks, the rule (97% of its hits) is the fallback; notes explain why the two figures are equal. |
| 13 | Fixed | "still registered at day 14" named in the line with 28,061. |
| 14 | Fixed | "Wilson" removed; key reads "Intervals = 95% confidence intervals". |
| 15 | Fixed | "the same direction (more non-completion with the sign)". |
| 16 | Fixed | Groups separated: students with a declared disability; in the most deprived band; with no deprivation band recorded. |
| 17 | Fixed | 0.004 dropped from slide 14; the cell says duplicates leave the early-click comparison the same. |
| 18 | Fixed | "all 22 data checks pass". |
| 19 | Fixed | "the test set grew from 9 runs of 2014 (those with a 2013 match) to 13". |
| 20 | Fixed | "Watch for inactivity, not only missed tasks" on slide 15 and in the take-home line. |
| 21 | Fixed (VI) | Notes: "không còn truy cập học phần". |
| 22 | Fixed (VI) | Notes: day 13 and day 27 each given with its week in separate clauses. |
| 23 | Fixed | Transition sentence rewritten to name what the files held. |
| 24 | Fixed | Long sentence split in two. |
| 25 | Fixed | "We count assignments and quizzes only, not exams." |
| 26 | Fixed | 0.004 removed from the notes. |
| 27 | Fixed | Notes give the reasoning: only enrolments with later clicks change, so the filter is what keeps later data out. |
| 28 | Fixed | Slide 9 notes state S1: a model's list must find more non-completers than the rule's on the 13 test runs of 2014, by more than chance. |
| 29 | Fixed | Slide 10 notes say which list to use: the model's ranking, with the rule as the fallback. |
| 30 | Fixed (VI) | Repetition removed from the inactivity-sign sentence. |
| 31 | Fixed | Slide 13 shows the sixth contact (55.2%); notes give 92.4 / 57.6 / 55.2 / ≤ 47.3 against a base rate of 44.0, hence 5–6 per 20. |
| 32 | Fixed | Notes name log loss as the second measure. |
| 33 | Rejected | The legal classification is the report's next step (Section 12.1) and belongs to the close as a condition for scaling; the slide states the action ("prove that contact works before scaling") and the notes give the reason. |
| 34 | Fixed (VI) | "kịch bản" → "trường đại học giả định trong đề bài". |

Fit fixes made with the Vietnamese pass (no change of meaning): slide 8 proof label, key and control cell; slide 10 gate
line; slide 14 key, each shortened to clear the room checks.
