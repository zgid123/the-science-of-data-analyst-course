# Decisions on the reader re-test flags

Flags from `08-vi-reader-test.md` (40: clarity 1/2/3 = 0/20/20). "EN+VI" = fixed in the English source and the twin.

**Rating correction (EN+VI).** The re-test showed that the Milestone 2 and Milestone 3 generative-AI criteria were downgraded for page length, which those criteria do not grade (the Milestone 2 and 3 rubrics have no presentation criterion: `milestones/02/milestone-2.md` line 351, `03` rubric). Under the scale of Table A.1 both are Met. Totals change from 35 met / 9 mostly met to 37 / 7 (M2 8/1/0, M3 10/0/0), in Section 1, Table A.2 and Appendix I; recounted per table by script (both languages agree). Length stays in Table A.2's main-limitation column and in each milestone's introduction. Milestone 4 "Presentation and consistency" keeps length as its limitation; the optional Level 2 no longer downgrades it (the brief: Level 2 is not needed for 100 points).

| Flag (file:line) | Decision | Change |
| :-- | :-- | :-- |
| 01-00:13 contact list, pilot not introduced | Fixed EN+VI | Opening: the project draws up, early in each course, a list of students for the support office to contact. |
| 01-00:14 exam-based outcome | Fixed EN+VI | "exam results". |
| 01-00:14 de-duplicated version purpose | Fixed EN+VI | "…to test whether duplicates change the results". |
| 01-00:14 early clicks undefined | Fixed EN+VI | "clicks in the first four weeks" (OULAD exploration REPORT.md Section 5.2). |
| 01-00:16 list date | Fixed EN+VI | "(day 13 or day 27 after the course start)". |
| 01-00:17 four questions not listed | Fixed EN+VI | Problem cell names the four levels. |
| 01-00:17 whose 50% target | Fixed EN+VI | "The Milestone 1 target". |
| 01-00:18 nested definition | Fixed VI | Definition in brackets. |
| 01-00:19 word order | Fixed VI | Rewritten with the head noun first. |
| 01-00:20 contradiction with predictive not evaluated | Fixed EN+VI | "The evaluation plan reports results … separately". |
| 01-00:22 slide status | Fixed VI | Two sentences; status of the deck stated as a condition. |
| 02-01:14 evidence column | Fixed EN+VI | "the evidence column of the tables in Appendix II". |
| 02-01:26 "dù … vẫn" | Fixed VI | Rewritten as a plain statement. |
| 02-02:32/89 day 13 vs 14 | Fixed EN+VI | Day 14 named as the population of the completion indicator; days 13 and 27 are the list dates. |
| 02-02:33 five entries | Fixed EN+VI | "five entries for the further results they led to". |
| 02-02:34 "ba điểm" | Fixed VI | "ba nội dung". |
| 02-02:38, 57 length under GenAI | Fixed EN+VI | Rating correction above. |
| 02-02:55 "dòng dữ liệu biến" | Fixed VI | "dòng của bảng biến đầu vào". |
| 02-02:73 Level 2 downgrades presentation | Fixed EN+VI | Limitation is length only. |
| 02-02:88 N/A explanation | Fixed EN+VI | "We did not run Level 2, the optional prototype; the report gives only its specification". |
| Clarity 3 fixed | Fixed | 01-00:7 announced column matches header; 01-00:16 repeated "kỳ mở" gloss removed; 01-00:19 "22 phép kiểm tra hợp lệ"; 02-02:13 "no real person" (EN+VI); 02-02:14 "chủ đề yêu cầu"; 02-02:15 "đặt mục tiêu nâng"; 02-02:52 "kiểm chứng"; 02-02:69 "among others" (EN+VI); 02-02:87 fold rendered as "lượt kiểm định chéo". |
| Clarity 3 kept | Kept | Title (form's own title); Phòng Đào tạo (the scenario university's office, named in every milestone report); 01-00:15 column name (detail in the Milestone 2 report); "ở dạng thiết kế", "tập kiểm thử giữ lại", "không báo lỗi" (glossary forms; "không báo lỗi" keeps check results apart from the rating "Đạt"); translator identity (AI use reported per milestone); "khoảng" for page counts (counts are layout estimates); 02-01:24 question levels (now named in Section 1); 02-02:54, 02-02:73 detail in the milestone reports; "Đã giảm thiểu" for a documented mismatch (the checksum and sensitivity analysis mitigate it). |
| Terms "học phần" / "module" | Kept | Glossary: "module" for OULAD units, "học phần" for the university's courses and for completion ("hoàn thành học phần"). |

Checks: `check_parity.py --lang vi` 0 errors, 1 accepted warning; `check_pairs.py` 0 pairs with differences; three twins marked.
