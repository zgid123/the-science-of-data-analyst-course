# Vietnamese native review – group G3 (Sections 5–8)

Reviewer: native-review agent (fresh reader; not the translator). Protocol: `build-report/languages/vi/review.md`, three passes per file. Glossary coverage before the passes (`glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report`): 10 drifting concepts; those touching G3 are enrolment (settled as "lượt đăng ký học"), coverage, scaling / encoding (fitted), deprivation band, declared disability and aggregate. G3 files already use the settled or glossary forms for them, so no edit was needed for drift.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 05-00-preparation-plan | 3 | 3.1 Voice with intent (actor) | Trước khi bất kỳ bản ghi nào được thay đổi, mỗi vấn đề … đều có một quyết định | Trước khi thay đổi bất kỳ bản ghi nào, nhóm tác giả đã đưa ra cho mỗi vấn đề … một quyết định |
| 2 | 05-00-preparation-plan | 7 | 3.5 No empty words | các phép kiểm tra V01–V15 là các phép kiểm tra của Mục 7 | các phép kiểm tra V01–V15 được trình bày ở Mục 7 |
| 3 | 05-00-preparation-plan | 19 | 3.3 Glossary forms (settled: rút khỏi module) | Hoạt động sau khi rút | Hoạt động sau khi rút khỏi module |
| 4 | 05-00-preparation-plan | 25 | 3.6 Meaning complete ("Later-run claim") | Nhận định hướng đến các lượt mở về sau | Kết luận cần đúng cho các lượt mở về sau |
| 5 | 06-01-pipeline-steps | 5 | 3.3 Keep English (glossary: checksum) | mã kiểm tra (checksum) | checksum |
| 6 | 06-01-pipeline-steps | 6 | 3.3 Glossary forms (rút khỏi module) | lượt nhấp sau khi rút | lượt nhấp sau khi rút khỏi module |
| 7 | 06-01-pipeline-steps | 10 | 3.5 Head nouns present | tám giai đoạn có script | tám giai đoạn đã viết thành script |
| 8 | 06-02-integration-features | 22 | 3.1 Complete (subject of the clause) | cho thấy bổ sung các thuộc tính này … | cho thấy việc bổ sung các thuộc tính này … |
| 9 | 06-03-split-leakage | 3 | 3.1 Complete | làm hiệu năng ước lượng cao hơn thực tế | làm hiệu năng ước lượng được cao hơn thực tế |
| 10–14 | 06-03-split-leakage | 11–15 | 3.3 English only where Vietnamese engineers keep it | Target / Train–test contamination / Student / Temporal / Augmentation leakage | Rò rỉ biến mục tiêu (target leakage); Lẫn dữ liệu giữa tập huấn luyện và tập kiểm thử; Rò rỉ theo sinh viên (student leakage); Rò rỉ theo thời gian (temporal leakage); Rò rỉ do tăng cường dữ liệu (augmentation leakage) |
| 15 | 06-03-split-leakage | 13 | 3.6 Meaning complete ("on one side" of the split) | giữ mỗi sinh viên ở cùng một phía | giữ mỗi sinh viên ở cùng một phía của phép chia |
| 16 | 06-03-split-leakage | 17 | 3.1 Light function words (theo … theo) | theo thời gian theo đúng thực tiễn của OU | theo thời gian dựa trên thực tiễn của OU |
| 17 | 06-03-split-leakage | 18 | 3.5 Established words; 3.1 Vietnamese order | tuân theo nguyên tắc đánh giá dữ liệu phụ thuộc thời gian trên các quan sát tương lai | áp dụng nguyên tắc dữ liệu phụ thuộc thời gian phải được đánh giá trên các quan sát tương lai |
| 18 | 06-03-split-leakage | 19 | 3.1 Complete (verb object) | được khớp trên dữ liệu chỉ học từ các lượt mở huấn luyện; … mọi dòng kiểm thử | … chỉ học tham số từ các lượt mở huấn luyện; … toàn bộ dòng kiểm thử |
| 19 | 06-03-split-leakage | 21 | 3.3 Glossary (tinh chỉnh = fine-tuning) | bước tinh chỉnh tham số | bước tinh chỉnh siêu tham số |
| 20 | 07-00-prepared-validation | 3 | 3.3 Register (who "the team" is) | Đề bài yêu cầu nhóm chứng minh | Đề bài yêu cầu nhóm tác giả chứng minh |
| 21 | 07-00-prepared-validation | 5 | 3.3 Glossary (settled: data profiling) | kết quả lập hồ sơ dữ liệu | kết quả khảo sát dữ liệu (profiling) |
| 22 | 07-01-before-after | 16 | 3.1 Collocation ("đúng ở" read as "correct at") | khác với kết quả đếm lại không lọc đúng ở 26.755 và 25.663 | khác với lần đếm lại không lọc ở đúng 26.755 và 25.663 |
| 23 | 07-02-lineage-dictionary | 4 | 3.5 No empty words (sẽ) | Bước kiểm tra sẽ báo lỗi | Bước kiểm tra báo lỗi |
| 24 | 07-02-lineage-dictionary | 5 | 3.3 Glossary (settled: lineage at first use) | Bảng dòng dõi dữ liệu theo mẫu | Bảng dòng dõi dữ liệu (lineage) theo mẫu |
| 25 | 07-03-residual-risks | 3 | 3.1 Voice (actor); 3.5 "đo lường" | Năm vấn đề được chủ động giữ lại …; đánh dấu và đo lường | Nhóm tác giả chủ động giữ lại năm vấn đề …; đánh dấu và đo mức ảnh hưởng |
| 26 | 07-03-residual-risks | 5 | 3.6 Meaning ("bound their effect at" = upper bound) | giới hạn ảnh hưởng của các dòng này ở mức 3,19% | cho thấy ảnh hưởng của các dòng này không vượt quá 3,19% |
| 27 | 07-03-residual-risks | 6 | 3.6 Meaning ("on record") | chính sách chấm điểm của OU hiện có lại ban hành năm 2025 | … hiện có trong tài liệu lại ban hành năm 2025 |
| 28 | 07-03-residual-risks | 8 | 3.6 Meaning ("10% coverage") | thấp hơn mức 10% | thấp hơn mức bao phủ 10% |
| 29 | 07-03-residual-risks | 12 | 3.3 Glossary (OULAD withdrawal) | với rút học phần | với rút khỏi module |
| 30 | 07-03-residual-risks | 14 | 3.3 Glossary (settled: tutor group) | phụ trách một nhóm khoảng 20 sinh viên | phụ trách một nhóm hướng dẫn khoảng 20 sinh viên |
| 31 | 08-01-views-by-level | 4 | 3.1 Complete (verb) | cho các tỷ lệ trên đúng mẫu số | cho phép tính tỷ lệ trên đúng mẫu số |
| 32 | 08-01-views-by-level | 7 | 3.3 Term reads as "classroom" | ở lớp nhỏ hơn | ở lớp nhãn ít mẫu hơn |
| 33 | 08-02-readiness-matrix | 3 | 3.1 Vietnamese order (topic first) | Bảng 8.1 nêu, cho từng câu hỏi, bảng dữ liệu … | Với từng câu hỏi phân tích, Bảng 8.1 nêu bảng dữ liệu … |
| 34 | 08-02-readiness-matrix | 13 | 3.3 Glossary (recall: first use with English) | tỷ lệ phát hiện đạt được | tỷ lệ phát hiện (recall) đạt được |
| 35 | 08-02-readiness-matrix | 17 | 3.1 Light function words | Việc chọn cách liên hệ và hiệu quả của liên hệ | Cách liên hệ được chọn và hiệu quả của việc liên hệ |
| 36 | 08-02-readiness-matrix | 20 | 3.1 Complete (parallel list items) | cách chia dữ liệu xác định, kiểm soát rò rỉ thông tin | cách chia dữ liệu đã được xác định, biện pháp kiểm soát rò rỉ thông tin |

Terms for the glossary to settle: (1) the brief's five leakage types (target, train–test contamination, student, temporal, augmentation leakage), rendered here as listed in rows 10–14; (2) "smaller class" (minority class of the target) → "lớp nhãn ít mẫu hơn" (12-01 and others still write "lớp nhỏ hơn"); (3) "tuning" → "tinh chỉnh siêu tham số", since "tinh chỉnh" alone is fine-tuning.

Per file (check_parity.py --lang vi; translation_status.py --mark run on all twelve):

- 05-00-preparation-plan: reviewed, 4 findings fixed, parity 0 errors, 0 warnings.
- 06-00-preparation-pipeline: reviewed, no findings, parity 0 errors, 0 warnings.
- 06-01-pipeline-steps: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 06-02-integration-features: reviewed, 1 finding fixed, parity 0 errors, 0 warnings.
- 06-03-split-leakage: reviewed, 11 findings fixed, parity 0 errors, 0 warnings (an "English loanword: test" warning from the gloss "(train–test contamination)" was resolved by dropping that gloss).
- 07-00-prepared-validation: reviewed, 2 findings fixed, parity 0 errors, 0 warnings.
- 07-01-before-after: reviewed, 1 finding fixed, parity 0 errors, 0 warnings.
- 07-02-lineage-dictionary: reviewed, 2 findings fixed, parity 0 errors, 0 warnings.
- 07-03-residual-risks: reviewed, 6 findings fixed, parity 0 errors, 0 warnings.
- 08-00-readiness: reviewed, no findings, parity 0 errors, 0 warnings.
- 08-01-views-by-level: reviewed, 2 findings fixed, parity 0 errors, 0 warnings.
- 08-02-readiness-matrix: reviewed, 4 findings fixed, parity 0 errors, 0 warnings.
