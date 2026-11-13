# Native review of Appendix IV (work allocation)

Reviewer: native Vietnamese reviewer (agent, not the translator), 2026-11-13. Scope: `report/02-04-work-allocation.vi.md` (new), the Appendix IV sentence of `report/01-00-team-comments.vi.md` (paragraph "Tóm lại,") and of `report/02-00-appendices.vi.md`. Three passes (reader, fidelity, checklist) per build-report `languages/vi/review.md`.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 02-04-work-allocation.vi.md | 1 | 3.5 Head nouns present | Phụ lục IV – Phân công và đóng góp | Phụ lục IV – Phân công công việc và mức đóng góp |
| 2 | 02-04-work-allocation.vi.md | 3 | 3.6 Meaning complete ("the tasks of its brief") | các nhiệm vụ trong đề bài được chia | các nhiệm vụ trong đề bài của milestone đó được chia |
| 3 | 02-04-work-allocation.vi.md | 3 | 3.6 Meaning complete ("contributed to") | thành viên nào cũng tham gia cả năm milestone | thành viên nào cũng đóng góp cho cả năm milestone |
| 4 | 02-04-work-allocation.vi.md | 9 | 3.6 Orthography (same-cell consistency with "nhật ký tìm kiếm") | và Nhật ký vấn đề chất lượng dữ liệu (Data Quality Issue Log) | và nhật ký vấn đề chất lượng dữ liệu (Data Quality Issue Log) |
| 5 | 02-04-work-allocation.vi.md | 9 | 3.5 Head nouns present ("findings of the questions") | kết quả của câu hỏi mô tả | kết quả trả lời câu hỏi mô tả |
| 6 | 02-04-work-allocation.vi.md | 10 | 3.5 Established words ("selection rationale") | lập luận chọn bộ dữ liệu | lý do chọn bộ dữ liệu |
| 7 | 02-04-work-allocation.vi.md | 10 | 3.1 Complete (bare "báo cáo" reads as the verb "report", three times) | … và báo cáo. | … và bản báo cáo. |
| 8 | 02-04-work-allocation.vi.md | 10 | 3.1 Collocations | các quyết định chuẩn bị dữ liệu | các quyết định về chuẩn bị dữ liệu |
| 9 | 02-04-work-allocation.vi.md | 10 | 3.3 One term per concept ("bảng" is the table word, Bảng A.10) | bảng tự đánh giá này | bản tự đánh giá này |
| 10 | 02-04-work-allocation.vi.md | 11 | 3.3 One term per concept (01-00 writes "bộ slide thuyết trình") | và bộ slide. | và bộ slide thuyết trình. |
| 11 | 02-04-work-allocation.vi.md | 13 | 3.2 Every sentence linked; 3.1 Collocations | Tỷ lệ của ba thành viên được làm tròn … và cộng lại là toàn bộ khối lượng công việc. | Ba tỷ lệ này được làm tròn … và cộng lại thành toàn bộ khối lượng công việc. |
| 12 | 01-00-team-comments.vi.md | 5 | 3.5 Plain wording ("work allocation of the three members") | Phụ lục IV trình bày phân công công việc của ba thành viên. | Phụ lục IV trình bày cách phân công công việc giữa ba thành viên. |

Checked and kept: deliverable names in the brief's English with their gloss (Search Log, Data Quality Issue Log, AQ Modeling Brief, Candidate Solution Matrix, Prepared Data Package, Final Project Package) as in 02-01 and 02-03; "gói thu thập dữ liệu", "khảo sát dữ liệu (profiling)", "kiểm tra dữ liệu đã chuẩn bị", "câu hỏi dự báo/chỉ định", "nguyên mẫu Level 2" match the glossary and the sibling twins; decimal comma 33,3; no comma before "và"/"hoặc"; voice "nhóm"; members named by ID and name as in the English. The 02-00-appendices.vi.md sentence reads naturally and is faithful; no edit.

English fault (reported, not edited): `report/02-00-appendices.md` line 3 enumerates with "and" twice: "… (Appendix II); and the rating of every grading criterion … (Appendix III); and the work allocation … (Appendix IV)". The "and" before "the rating" should go, leaving "… (Appendix II); the rating … (Appendix III); and the work allocation … (Appendix IV)". The Vietnamese twin already has the corrected form.

- 02-04-work-allocation.vi.md: reviewed, 11 findings fixed, check_parity PASS (5 headings/captions/rows, 4 table rows).
- 01-00-team-comments.vi.md: Appendix IV sentence reviewed, 1 finding fixed, check_parity 0 errors.
- 02-00-appendices.vi.md: Appendix IV clause reviewed, no finding, check_parity 0 errors.
- Whole report: `check_parity.py --report reports/self-assessment/report --lang vi` → 7 pairs, 0 errors, 1 warning (accepted 'datasets' in 02-03 line 33); `translation_status.py --mark` recorded for 02-04-work-allocation.md, 01-00-team-comments.md and 02-00-appendices.md; `code/check_pairs.py` → "pairs with differences: 0".
