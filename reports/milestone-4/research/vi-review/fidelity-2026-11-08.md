# Vietnamese fidelity review of the rewrite – Milestone 4, 2026-11-08

Stage 4/5 of build-report reference.md section 4.3: every passage changed by the rewrite after reader test 1 (`rewrite-2026-11-08-scripts/twins.diff`, 27 twins) was read again by a reviewer who did not write it, against the English source file of the same name, sentence by sentence (meaning, numbers, hedges, conditions, attributions, citations, cross-references), then checked against the review.md section 3 checklist and the task glossary. The English edits the lead made after the rewrite (04-01 secondary metric, 05-02 deferred contact choice, 08-00 and 10-07 "choice of contact deferred") were compared with the current twins too.

Method: `fidelity-2026-11-08-scripts/pairs.py` splits each English file and its twin into aligned units (paragraphs; one unit per table row) and prints, for every unit that holds a line added by the rewrite, the English unit beside the current Vietnamese unit (101 passages in 27 twins). Fixes were applied by exact-match scripts (`fix.py`, `fix2.py`; each before-string must occur exactly once). Paths are relative to `reports/milestone-4/report/`; line numbers are those of the current twins.

## Findings

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 01-01 | 5 | 3.6 Meaning complete (D2 is *where* the time goes) | "Quyết định D2 xác định cách Trưởng chương trình đào tạo phân bổ thời gian … trong mỗi học kỳ." | "Quyết định D2 xác định Trưởng chương trình đào tạo dành thời gian … cho những việc nào trong mỗi học kỳ." |
| 2 | 01-01 | 7 | 3.3 Glossary forms ("year of study → năm theo học"; "năm học" is the academic year) | "theo năm học của sinh viên" | "theo năm theo học của sinh viên" |
| 3 | 01-01 | 20 | 3.1 Sentences (dangling "là" apposition) | "tỷ lệ nền của kỳ mở, là tỷ lệ sinh viên không hoàn thành" | "tỷ lệ nền của kỳ mở, tức tỷ lệ sinh viên không hoàn thành" |
| 4 | 01-02 | 17 | 3.6 Meaning complete ("đã qua lần kiểm tra" reads as "passed the test"; English: after the test took place) | "sau khi mô hình AQ3 đã qua lần kiểm tra duy nhất trên tập kiểm thử" | "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử" |
| 5 | 03-02 | 11 | 3.6 Meaning complete (same as #4) | "sau khi mô hình AQ3 đã qua lần kiểm tra trên tập kiểm thử (C14)" | "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử (C14)" |
| 6 | 08-00 | 16 | 3.6 Meaning complete (same as #4) | "sau khi mô hình AQ3 đã qua lần kiểm tra trên tập kiểm thử," | "sau lần kiểm tra duy nhất của mô hình AQ3 trên tập kiểm thử," |
| 7 | 03-02 | 9 | 3.6 Meaning complete (added claim: English only walks through the remaining criteria) | "Mô hình cũng đáp ứng các tiêu chí còn lại trong tám tiêu chí của Mục 3.1." | "Các tiêu chí còn lại trong tám tiêu chí của Mục 3.1 được xét như sau." |
| 8 | 04-00 | 3 | 3.1 Sentences ("được tính trên …, là …" left the index without a verb); 3.6 Abbreviations (ROC-AUC defined beside its full form) | "Chỉ số thứ nhất được tính trên đường cong đặc trưng hoạt động của bộ thu (ROC), là diện tích dưới đường cong ROC (ROC-AUC). Chỉ số thứ hai được tính trên đường cong độ chính xác–tỷ lệ phát hiện, là diện tích dưới …(PR-AUC)." | "Chỉ số thứ nhất dựa trên đường cong đặc trưng hoạt động của bộ thu (ROC): đó là diện tích dưới đường cong ROC (ROC-AUC). Chỉ số thứ hai là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện (PR-AUC)." |
| 9 | 04-01 | 45 | 3.3 Glossary forms ("reachable non-completer → sinh viên không hoàn thành còn liên hệ được") | "những sinh viên không hoàn thành mà cán bộ còn kịp liên hệ" | "những sinh viên không hoàn thành còn liên hệ được" |
| 10 | 04-01 | 61 | 3.6 Meaning complete (condition changed: English "passes **or** its flags are reviewed before use"; the twin required both) | "kiểm định khẳng định về công bằng ở Mục 4.4 phải đạt; nếu kiểm định này nêu tên nhóm nào, nhóm đó phải được xem xét trước khi đưa danh sách vào sử dụng;" | "kiểm định khẳng định về công bằng ở Mục 4.4 đạt hoặc mọi nhóm mà kiểm định này nêu tên đều được xem xét lại trước khi đưa danh sách vào sử dụng;" |
| 11 | 05-02 | 5 | 3.6 Meaning complete (hedge: English gives the purpose, "should be able to", "must not"; "bảo đảm" claimed a guarantee) | "Quy định này bảo đảm sinh viên bị đánh dấu có cơ hội chứng minh dự báo là sai [45], đồng thời nhãn …" | "Quy định này nhằm để sinh viên bị đánh dấu có cơ hội chứng minh dự báo là sai [45] và để nhãn …" |

Defects by kind: meaning or condition changed 6 (#1, #4–#6, #10, #11 – #4 to #6 are one wording repeated in three files); added claim 1 (#7); glossary form 2 (#2, #9); sentence form 2 (#3, #8).

## Accepted as written

- 03-03 "Primary approach": three Vietnamese paragraphs for one English paragraph. `check_parity.py` accepts it (0 errors), and the three paragraphs carry every English sentence, number and citation ([11], [14], [6], [15], [16], [17], [18]) in the English order; kept as split.
- Defining or explanatory clauses added by the rewrite that state facts the English gives elsewhere, kept: 03-01 AQ2 rationale "nên hiệu ứng cố định là phù hợp" (03-02 states it); 04-01 pooled normalised recall formula (Bảng A.4 in 10-02); 05-01 why the labels-available variant checks timing (glossary first-use rule); 06-00 Reflection "để không dùng đến dữ liệu của tập kiểm thử" (04-02 gives this reason for counting outcomes on 2013 runs only); 03-03 "không chắc chắn trong từng trường hợp cụ thể" after "chỉ ở mức trung bình".
- Lead's later English changes: 04-01 secondary metric ("trung bình không trọng số của các chênh lệch giữa mô hình và quy tắc dấu hiệu sớm, tính theo từng kỳ mở"), 05-02 deferred choice and ranking by expected benefit with AQ4 supplying only the list (D1), 08-00 and 10-07 "D1; việc chọn hình thức liên hệ được hoãn": the twins match the current English.

## Checks

| Command | Result |
| :---- | :---- |
| `check_parity.py --report reports/milestone-4/report --lang vi` | 0 errors, 24 warnings (23 in the verbatim English prompts of 10-06, 1 loanword on the English term of the terms page 00-2:37); a comma-before-"hoặc" warning from fix #10 was fixed by `fix2.py` before the final run |
| `check_abbreviations.py --report reports/milestone-4/report --lang vi` | 17 abbreviations, 0 violations (first run after `fix.py`: 1 violation, ROC-AUC without its full form, fixed by `fix2.py`) |
| `translation_status.py --report reports/milestone-4/report --lang vi --mark` 01-01, 01-02, 03-02, 04-00, 04-01, 05-02, 08-00 | recorded 7 files |
| `translation_status.py --report reports/milestone-4/report --lang vi` | 34 sections, 0 need translation, 0 orphaned |

Console output with UTC timestamps and exit codes: `fidelity-2026-11-08-scripts/checks.log`.

## Per file

| File | Passages checked | Findings fixed | Parity |
| :---- | :---- | :---- | :---- |
| 00-2 | 1 | 0 | 0 errors |
| 01-00 | 2 | 0 | 0 errors |
| 01-01 | 6 | 3 | 0 errors |
| 01-02 | 4 | 1 | 0 errors |
| 02-00 | 1 | 0 | 0 errors |
| 02-01 | 7 | 0 | 0 errors |
| 02-02 | 3 | 0 | 0 errors |
| 03-00 | 1 | 0 | 0 errors |
| 03-01 | 7 | 0 | 0 errors |
| 03-02 | 4 | 2 | 0 errors |
| 03-03 | 4 | 0 | 0 errors |
| 03-04 | 2 | 0 | 0 errors |
| 04-00 | 1 | 1 | 0 errors |
| 04-01 | 15 | 2 | 0 errors |
| 04-02 | 7 | 0 | 0 errors |
| 04-03 | 6 | 0 | 0 errors |
| 04-04 | 3 | 0 | 0 errors |
| 05-00 | 2 | 0 | 0 errors |
| 05-01 | 3 | 0 | 0 errors |
| 05-02 | 2 | 1 | 0 errors |
| 06-00 | 5 | 0 | 0 errors |
| 07-00 | 2 | 0 | 0 errors |
| 08-00 | 5 | 1 | 0 errors |
| 10-03 | 2 | 0 | 0 errors |
| 10-05 | 3 | 0 | 0 errors |
| 10-06 | 2 | 0 | 0 errors |
| 10-07 | 1 (+ AQ4 row of the lead's change) | 0 | 0 errors |

## Open

- No English sentence was found wrong.
- Glossary: "reachable non-completer" now appears in its glossary form; the rows listed under "Glossary rows to settle" in `rewrite-2026-11-08.md` are still open (no glossary file edited here).
- A second reader test on the rewritten twins (reference.md section 4.3, stage 5) has not been run.
