# Native review of the per-milestone restructure and the Milestone 5 Level 2 update

Reviewer: native Vietnamese reviewer (fresh reader, not the translator), 2026-11-13. Group: 01-00, 02-00, 03-00, 03-01, 03-02 (`*.vi.md`). Three passes per file (review.md section 2); criterion cells of Appendix II left verbatim.

Glossary coverage before the passes (`glossary.py --lang vi --task self-assessment coverage`): 14 drifting concepts. Real drift fixed: single test ("một lần kiểm tra duy nhất" → "kiểm tra một lần duy nhất"), feature ("biến" → "đặc trưng"), AQ Revision Log, data profiling ("lập hồ sơ" → "khảo sát dữ liệu (profiling)"), tuning ("tinh chỉnh" → "tinh chỉnh siêu tham số"). Accepted as false positives: enrolment (OULAD row "lượt đăng ký học" applies), measure (here a metric, "thước đo"), predictors ("biến dự báo" per the running-text row), NIST verbs, PASS/FAIL, Before/After, Validation, gap, fact, main text ("phần chính" after first use, as the glossary allows), contact list ("danh sách sinh viên cần liên hệ"). After: 12 drifting, all of the accepted kind.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 01-00 | 11 | Voice with intent | Năm bên liên quan được phỏng vấn, do AI tạo sinh mô phỏng | Phỏng vấn năm bên liên quan, do AI tạo sinh mô phỏng |
| 2 | 01-00 | 11 | Abbreviations | bốn câu hỏi phân tích từ mô tả đến chỉ định | bốn câu hỏi phân tích (AQ) từ mô tả đến chỉ định (AQ is used later in the table and in "Nhật ký điều chỉnh AQ") |
| 3 | 01-00 | 11 | No empty words | Các cuộc phỏng vấn là phỏng vấn mô phỏng | Các cuộc phỏng vấn đều được mô phỏng |
| 4 | 01-00 | 13 | Glossary forms (data profiling) | Toàn bộ 10,9 triệu dòng được lập hồ sơ dữ liệu | Khảo sát dữ liệu (profiling) trên toàn bộ 10,9 triệu dòng |
| 5 | 01-00 | 13 | Glossary forms (leakage auditor) | tám lỗi do đợt kiểm tra rò rỉ thông tin của AI phát hiện đều đã được sửa | tám lỗi do AI kiểm tra rò rỉ thông tin phát hiện, tất cả đều đã được sửa |
| 6 | 01-00 | 13 | One clear actor | bộ dữ liệu … nằm trong Gói dữ liệu đã chuẩn bị … và cho kết quả giống hệt khi chạy lại | … đóng gói trong Gói dữ liệu đã chuẩn bị (Prepared Data Package); gói này cho kết quả giống hệt khi chạy lại |
| 7 | 01-00 | 14 | Glossary forms | bản mô tả yêu cầu mô hình hóa (AQ Modeling Brief) | AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa của từng AQ) |
| 8 | 01-00 | 14 | Glossary forms (single test) | một lần kiểm tra duy nhất trên các kỳ mở năm 2014 | kiểm tra một lần duy nhất trên các kỳ mở năm 2014 |
| 9 | 01-00 | 14 | Complete sentence | đặc tả của nguyên mẫu (prototype) Level 2 tùy chọn, được chạy ở Milestone 5 | đặc tả nguyên mẫu (prototype) Level 2 tùy chọn; nguyên mẫu này được chạy ở Milestone 5 |
| 10 | 01-00 | 15 | Plain action / meaning | lần liên hệ đầu tiên gặp đúng sinh viên không hoàn thành học phần trong 92,4% trường hợp | sinh viên được liên hệ đầu tiên là người về sau không hoàn thành học phần trong 92,4% trường hợp |
| 11 | 01-00 | 15 | Glossary forms (tuning) | Thước đo dùng để tinh chỉnh mô hình | Thước đo dùng để tinh chỉnh siêu tham số của mô hình ("tinh chỉnh" alone is fine-tuning) |
| 12 | 01-00 | 15 | Meaning complete (tutors) | nguy cơ dự báo … ở 5 trong 13 kỳ mở kiểm tra, nên cán bộ chỉ xem thứ hạng | nguy cơ do mô hình dự báo … ở 5 trong 13 kỳ mở kiểm thử, nên giảng viên hướng dẫn chỉ được xem thứ hạng |
| 13 | 01-00 | 21 | Glossary forms | Nhật ký điều chỉnh câu hỏi phân tích (AQ Revision Log) | Nhật ký điều chỉnh AQ (AQ Revision Log) |
| 14 | 01-00 | 22 | Head nouns present | Milestone 2 đến Milestone 4 đều mở đầu bằng việc kiểm tra các cam kết của milestone trước | Báo cáo của Milestone 2 đến Milestone 4 đều mở đầu bằng bước kiểm tra các cam kết của milestone liền trước |
| 15 | 01-00 | 24 | Glossary forms (tuning, AQ Revision Log) | thước đo dùng để tinh chỉnh mô hình …; Nhật ký điều chỉnh câu hỏi phân tích; thước đo tinh chỉnh | thước đo dùng để tinh chỉnh siêu tham số của mô hình …; Nhật ký điều chỉnh AQ; thước đo tinh chỉnh siêu tham số |
| 16 | 01-00 | 26 | Written connectives | tức ở Milestone 1, 4 và 5 | cụ thể là ở Milestone 1, 4 và 5 |
| 17 | 01-00 | 28 | Light function words (của chain) | là nội dung của phần nhận xét của nhóm ở Mục 2 | được trình bày trong phần nhận xét của nhóm ở Mục 2 |
| 18 | 02-00 | 3 | No empty words; collocation | diễn ra ra sao …: các vấn đề nhóm gặp phải, cách nhóm vượt qua, các bài học nhóm rút ra và đánh giá chung của nhóm | diễn ra như thế nào …: các vấn đề phát sinh, cách nhóm vượt qua các vấn đề này, bài học rút ra và đánh giá chung về dự án |
| 19 | 02-00 | 14 | Glossary forms (feature) | mỗi biến về lượt nhấp | mỗi đặc trưng về lượt nhấp |
| 20 | 02-00 | 17 | Written connectives | (precision, tức tỷ lệ … | (precision, là tỷ lệ … |
| 21 | 02-00 | 17 | Meaning complete; final state only | Danh sách liên hệ nay chỉ dài bằng số sinh viên Phòng Đào tạo liên hệ được. Thước đo mới là tỷ lệ phát hiện (recall) … | Danh sách liên hệ được đánh giá theo tỷ lệ sinh viên về sau không hoàn thành học phần mà danh sách phát hiện được, trong giới hạn số sinh viên Phòng Đào tạo liên hệ được (matches the English; drops "nay", "mới") |
| 22 | 02-00 | 17 | Glossary forms (single test) | bằng một lần kiểm tra duy nhất | bằng phép kiểm tra một lần duy nhất |
| 23 | 02-00 | 19 | Written connectives | …, tức kiểm tra để bảo đảm … | …, nghĩa là kiểm tra để bảo đảm … |
| 24 | 02-00 | 19 | Glossary forms (feature) | không ảnh hưởng đến các biến đầu vào | không ảnh hưởng đến các đặc trưng |
| 25 | 02-00 | 21 | Glossary forms (tuning) | tinh chỉnh mô hình bằng kiểm định chéo lồng nhau | tinh chỉnh siêu tham số của mô hình bằng kiểm định chéo lồng nhau |
| 26 | 02-00 | 21 | Who speaks (meaning) | gói dữ liệu bản nháp của Milestone 4 | gói bản nháp mà nhóm lập ở Milestone 4 ("our … draft package") |
| 27 | 02-00 | 21 | Glossary forms (tuning) | Nhóm tinh chỉnh mô hình theo log loss | Nhóm tinh chỉnh siêu tham số theo log loss |
| 28 | 02-00 | 21 | Complete sentence (misreading) | … và điều kiện đạt được giữ đúng như Milestone 4 đã cố định (reads "điều kiện đạt được") | … và điều kiện đạt vẫn giữ nguyên như Milestone 4 đã cố định |
| 29 | 02-00 | 21 | Glossary forms (single test) | trước lần kiểm tra duy nhất | trước phép kiểm tra một lần duy nhất |
| 30 | 02-00 | 21 | Meaning complete ("confirms") | phép kiểm tra đánh giá đúng thiết kế đã được cố định từ trước | phép kiểm tra đánh giá một thiết kế đã cố định từ trước nên mang tính khẳng định ("xác nhận" is a replaced glossary form) |
| 31 | 02-00 | 31 | Punctuation (enumeration) | mọi tiêu chí … đạt phần lớn, bốn câu hỏi … được trả lời đúng ở mức … | mọi tiêu chí … đạt phần lớn; bốn câu hỏi … được trả lời ở mức … |
| 32 | 02-00 | 31 | One term per concept | hình thức đào tạo từ xa | hình thức học từ xa (as in Table 2.1) |
| 33 | 02-00 | 31 | Punctuation (enumeration) | xác nhận lại …, tính lại … và đo tác động | xác nhận lại …; tính lại …; đo tác động |
| 34 | 03-00 | 3 | Established words; repetition | chi tiết làm cơ sở cho Bảng 1.1: cơ sở đánh giá …; … và hạn chế còn lại | chi tiết bổ sung cho Bảng 1.1: cơ sở đánh giá …; … và hạn chế tương ứng |
| 35 | 03-01 | 3 | Meaning ("results"); của chain | cơ sở của phần tự đánh giá sơ bộ của nhóm đối với các sản phẩm đã nộp | cơ sở cho phần tự đánh giá sơ bộ của nhóm về kết quả đã nộp |
| 36 | 03-01 | 16 | Written connectives | tức ở Milestone 1, 4 và 5 | cụ thể là ở Milestone 1, 4 và 5 |
| 37 | 03-02 | 16 | Meaning complete (dropped list) | theo năm yêu cầu chất lượng mà đề bài nêu | theo năm yêu cầu chất lượng: rõ ràng, cụ thể, có phạm vi, hướng tới dữ liệu và trả lời được |
| 38 | 03-02 | 55 | Glossary forms (feature, feature view) | sáu biến dẫn xuất … dòng của bảng biến đầu vào | sáu đặc trưng dẫn xuất … dòng của bảng đặc trưng |
| 39 | 03-02 | 83 | Glossary forms | Nhật ký điều chỉnh câu hỏi phân tích | Nhật ký điều chỉnh AQ (AQ Revision Log) |
| 40 | 03-02 | 84 | Meaning complete (added, stale) | trạng thái của từng câu hỏi (đã trả lời, trả lời một phần hoặc hoãn) | trạng thái của từng câu hỏi (no question is deferred now; the English lists no states) |
| 41 | 03-02 | 88 | One clear actor; glossary (Final Project Package first use) | các bước trong gói nộp cuối kỳ chạy lại được mọi kết quả, được đối chiếu từng byte | các bước trong Gói nộp cuối kỳ (Final Project Package); các bước này chạy lại được mọi kết quả và đã được đối chiếu từng byte |
| 42 | 03-02 | 88 | Glossary forms (tuning) | thước đo dùng để tinh chỉnh mô hình | thước đo dùng để tinh chỉnh siêu tham số |
| 43 | 03-02 | 89 | Glossary forms (single test) | danh sách xếp hạng của lần kiểm tra duy nhất năm 2014 | danh sách xếp hạng từ phép kiểm tra một lần duy nhất trên dữ liệu năm 2014 |

Two trial edits were withdrawn because they added numbers absent from the English (check_pairs.py): "(AQ1–AQ4)" became "(AQ)", and "điều kiện đạt S1" in Table 2.1 became "điều kiện đạt".

English source, reported not edited: 01-00 uses "AQ1"–"AQ4" and "AQ Revision Log" without ever defining "AQ" (analytical question) in Section 1; the Vietnamese now gives "(AQ)" at the first mention.

Glossary questions: (1) "coherence" (the brief's "tính kết dính") has no row; (2) "tutor" in the Milestone 5 sense of who sees the ranked list (giảng viên hướng dẫn vs cán bộ) should be settled; (3) "tinh chỉnh" alone for hyperparameter tuning is common in the Milestone 5 twins although the common glossary reserves it for fine-tuning.

Checks: `check_parity.py --report reports/self-assessment/report --lang vi` → 0 errors, 1 warning ('datasets' in the verbatim brief criterion of Table A.3, accepted); `translation_status.py --mark` recorded for all five files; `code/check_pairs.py` → "pairs with differences: 0".

- 01-00-assessment-by-milestone.vi.md: reviewed, 17 findings fixed, parity 0 errors.
- 02-00-team-comments.vi.md: reviewed, 16 findings fixed, parity 0 errors.
- 03-00-appendices.vi.md: reviewed, 1 finding fixed, parity 0 errors.
- 03-01-basis-overview.vi.md: reviewed, 2 findings fixed, parity 0 errors.
- 03-02-assessment-by-criterion.vi.md: reviewed, 7 findings fixed, parity 0 errors, 1 accepted warning.
