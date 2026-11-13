# Decisions on the reader-test flags of the restructured document

Flags from `06-vi-reader-test.md` (46: clarity 1/2/3 = 0/21/25). "EN+VI" = the fault was in the English source too, fixed in both.

| # | Decision | Change |
| :-- | :-- | :-- |
| 1 | Kept | Title is the form's own title given by the user ("…trên nhiệm vụ được giao"). |
| 2 | Kept | Registered project title, copied from the milestone title pages. |
| 3 | Fixed EN+VI | Section 1 and Appendix I: "Of the 45 criteria … one is not applicable …; of the 44 rated criteria, 35 … 9 …". |
| 4 | Fixed VI | "những nội dung mà kết quả đánh giá chưa phản ánh được". |
| 5 | Fixed EN+VI | Column "What happened" / "Điều đã xảy ra". |
| 6 | Fixed EN+VI | "all five simulated stakeholders" / "năm bên liên quan mô phỏng". |
| 7 | Fixed VI | "thí điểm việc dùng danh sách". |
| 8 | Fixed EN+VI | Section 1 opening now names OULAD, its records (enrolments, assessments, daily clicks on the learning platform), 22 runs of seven modules, 2013–2014, and the project aim. |
| 9 | Fixed EN+VI | Effect size named: early clicks of completers vs non-completers. |
| 10, 11 | Fixed VI | "mỗi biến về lượt nhấp được tính thêm một lần…"; "được dùng trong phân tích độ nhạy". |
| 12 | Kept | "kỳ mở (module)" is the glossary form (module run) and a user decision (T8); now defined at first use in the opening paragraph. |
| 13 | Fixed EN+VI | Precision defined; the 45% base rate stated ("about 45% of enrolled students do not complete"). |
| 14 | Kept | "câu hỏi chỉ định" is the brief's own word (glossary), glossed at first use. |
| 15 | Fixed VI | Recall defined in Vietnamese order: "tỷ lệ sinh viên có tên trong danh sách trên tổng số sinh viên về sau không hoàn thành học phần". |
| 16 | Fixed VI | Drift: "dữ liệu kiểm thử giữ riêng" → glossary "tập kiểm thử giữ lại" (3 places). |
| 17 | Fixed EN+VI | Expected benefit explained: how much a contact would change the chance of completing. |
| 18 | Fixed EN+VI | Status states the mitigation: every result stated as an association; adopters recompute on own data. |
| 19 | Fixed EN+VI | "…so it passed whatever the data held". |
| 20 | Fixed EN+VI | Missing-value indicators defined; the leakage link stated; "now"/"nay" removed. |
| 21 | Fixed VI | "hai lần chạy lại tạo ra các tệp giống hệt nhau". |
| 22 | Fixed EN+VI | "set of runs" / "tập kỳ mở nào" (no "nhóm" for runs). |
| 23 | Fixed EN+VI | Change Log introduced: the record of changes kept with the milestone reports. |
| 24 | Fixed VI | "phần chi tiết". |
| 25 | Fixed EN+VI | "longer" deck removed; status: completed once the final slide count is settled. |
| 26 | Kept | Who translated is not needed for the point; generative AI use is reported in each milestone report. |
| 27–29 | Fixed EN+VI | Page counting names both languages; Table A.2 gives EN and VI counts per milestone; Milestone 5 English length (24 pages) stated where the closing sentence needs it. |
| 30 | Kept | Criterion cells copy each brief verbatim (Milestone 1 brief writes them in English). |
| 31 | Fixed VI | "năm yêu cầu chất lượng"; "Mười tiêu chí đánh giá bộ dữ liệu". Line 69 kept: the brief's own "selection criteria". |
| 32 | Kept | Both correct: lists are drawn on days 13 and 27; the completion indicator counts students registered on day 14 (Milestone 5 report). |
| 33 | Fixed EN+VI | Appendices intro and Appendix II intro: numbers in the evidence and limitation columns refer to the milestone report. |
| 34 | Fixed EN+VI | "eleven searches and five further results they led to, rejected results included" (Milestone 2 Section 3). |
| 35 | Fixed VI | Split into two sentences with the three facts as a list; actor "Nhóm chọn". |
| 36 | Fixed VI | "Bước kiểm tra đầu vào … điều kiện kế thừa từ Milestone …" (lines 48, 67). |
| 37 | Kept | YELLOW / RED are the brief's labels (glossary), each glossed in the cell. |
| 38 | Fixed VI | "mỗi lượt (fold) có một kỳ mở được tách ra để đánh giá" (glossary held-out run), lines 54 and 70. |
| 39 | Fixed EN+VI | "the six derived features on all 55,604 feature rows (one per enrolment and list date)" (Milestone 3 Table 7.1, check V11). |
| 40 | Fixed EN+VI | "Thirteen entries in the AI Decision Log". |
| 41 | Fixed VI | Cell split into sentences. |
| 42 | Fixed VI | "chỉ số công bằng … kiểm định thống kê … xác định từ trước". |
| 43 | Fixed VI | "được tính vào phần chất lượng của Level 1". |
| 44 | Kept | Section 1 now states the base rate itself (flag 13). |
| 45 | Fixed EN+VI | Limitation states the shortfall: the brief shows one eleven-column table; the report splits it. |
| 46 | Kept | Reader marked it acceptable. |

Recurring terms: "kỳ mở", "module", "câu hỏi chỉ định", "YELLOW/RED" kept as glossary or brief forms (reasons above); "module" names OULAD units and "học phần" the university's courses, as the glossary row "module (OULAD)" sets. "fold", "dữ liệu kiểm thử giữ riêng", "điều kiện đầu vào kế thừa", "tiêu chí" for non-grading checks and "nhóm" for runs fixed as listed.

Checks after the fixes: `check_parity.py --lang vi` 0 errors, 1 accepted warning ('datasets' in the verbatim Milestone 2 criterion); two long sentences in the Section 1 opening split; `check_pairs.py` 0 pairs with differences; all four twins marked.
