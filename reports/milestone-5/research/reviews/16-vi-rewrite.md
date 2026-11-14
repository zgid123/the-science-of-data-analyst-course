# Decisions on the focused reader check of the 15-slide deck

Decisions on the 11 findings of the focused reader check (15-vi-reader-test.md). Each fix was made in English first
(slide code in `slides_milestone5_full/part*.py` and `slides_milestone5_15/path.py`, notes in
`presentation/v3-15/speech-script.md`), then carried into `slides_milestone5_15_vi.py` after `slidekit.py sync`.
Facts follow the Milestone 5 report: the contamination row follows Appendix VII (medians, scales and category levels);
the gain without the students seen in 2013 (+0.020, 0.006 to 0.037) and on the 9 paired runs (+0.024, 0.010 to 0.043)
follow Appendix XIV; the test-set change follows Change Log C16 ("3–4, recorded in 5"). Build and checks:
`logs/T44_reader_fixes3.log`.

| # | Decision | Change or reason |
| :-- | :-- | :-- |
| 1 | Fixed | Slide 8 cell: "2014 test-year medians and scales shape inputs" (VI "Trung vị, độ lệch của năm kiểm thử 2014 định hình biến đầu vào"); notes: computed with 2014, the test year's own values would shape the model's inputs and the test would no longer be unseen. |
| 2 | Fixed | Proof box: "exactly the enrolments with later clicks change, no others"; notes add that most enrolments have later clicks, so most change, and that no other record does. |
| 3 | Fixed | Control cell: "Kept, as in real use; without them the gain holds", in the row naming the 1,586 test enrolments of students seen in 2013; notes name both. |
| 4 | Fixed | Slide 9 definition gives one ceiling: "the most a list of length k can reach, k non-completers (5 in the example, hence 4 of 5)"; "5 of 9" removed. |
| 5 | Fixed | Slide 4 AQ4: "overall and by student group (for the fairness check)". |
| 6 | Fixed | Slide 10 gate shows 72.5% vs 70.4% and says why it equals the last column: each list is shorter than its run's non-completers; Vietnamese header now "Tỷ lệ không hoàn thành trong danh sách". |
| 7 | Fixed | Slide 13 and the notes of slides 13 and 15: "the top-ranked student" / "sinh viên xếp hạng cao nhất", the fifth- and sixth-ranked, from the seventh on. |
| 8 | Fixed | Slide 13: "the fairness check … found none of the three groups fixed in advance disadvantaged"; notes the same; no "rule … flags". |
| 9 | Fixed | Slide 14: "every check shown to catch an error"; notes the same (VI active clause with "nhóm"). |
| 10 | Fixed | Slide 14 row: "the 2014 test set grew from the 9 runs with a 2013 twin to all 13, unrecorded until Milestone 5"; notes add that the 9 runs are still reported apart and the gain holds on them. |
| 11 | Fixed (VI) | Slide 15: "Điểm rủi ro không phải xác suất; chỉ thí điểm ngẫu nhiên cho biết liên hệ có ích không", under the heading "Đọc điểm rủi ro như thứ hạng", matching the notes. |

Fit changes made with this pass (no change of meaning): slide 8 proof box drops "a leak would show" (the label "Proof
the check works" and the lead carry it); slide 10 gate label shortened to "Gate S1 (model replaces rule) met" and the
fallback's 97% kept in the notes.
