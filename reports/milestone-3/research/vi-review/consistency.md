# Consistency read of the Vietnamese twin (stage 5, first half)

Reviewer: consistency reader (agent), 2026-11-06T02:37:51Z. Scope: every `reports/milestone-3/report/*.vi.md` read in file-name order (00-0 … 12-06); long appendix tables checked for prose, captions, headers and spot-checked cells. References: `languages/vi/guide.md`, `review.md`, merged glossary (`glossary.py --lang vi --task milestone-3 show`), `glossary.py … coverage --report`.

Checks across files: (1) one term per concept; (2) abbreviations defined at first use and matching `00-1-abbreviations.vi.md`; (3) file openers linking to what precedes; (4) Mục/Bảng/Hình/Phụ lục pointers; (5) Vietnamese number format.

| # | File:line | Finding | Fix |
| :---- | :---- | :---- | :---- |
| 1 | 01-01-baseline-aqs.vi.md:3 | KPI defined as "KPI chính của dự án (KPI: chỉ số đo lường hiệu quả chính)", not the full-form-then-abbreviation pattern of 00-1 | "Tỷ lệ này là chỉ số đo lường hiệu quả chính (KPI) của dự án." |
| 2 | 09-00-ethics-limitations.vi.md:21 | "Vương quốc Anh" spelled out again after UK is defined (02-01); English writes "UK" | "tại UK" |
| 3 | 09-00-ethics-limitations.vi.md:23 | Same: "các quốc gia thuộc Vương quốc Anh" (03-04 already writes "thuộc UK") | "các quốc gia thuộc UK" |
| 4 | 12-01-profiling-details.vi.md:76 | DQ19 cell spells out "Vương quốc Anh" after definition | "của UK" |
| 5 | 12-05-ai-decision-log.vi.md:10 | A2 cell spells out "Vương quốc Anh" after definition | "các quốc gia khác của UK" |
| 6 | 12-04-traceability-change-log.vi.md:20 | C01 cell spells out "Đại học Mở Anh" after OU is defined (01-02); English "UK Open University" | "(OU, đào tạo từ xa tại UK, 2013–2014)" |
| 7 | 06-02-integration-features.vi.md:6 | "by its cut-off" rendered "không muộn hơn" instead of the settled "chậm nhất vào" | "có ngày chậm nhất vào thời điểm chốt dữ liệu" |
| 8 | 06-02-integration-features.vi.md:18 | Table 6.1 tasks_missed_c: "đến hạn không muộn hơn c" | "đến hạn chậm nhất vào ngày c" |
| 9 | 06-02-integration-features.vi.md:19 | Table 6.1 tma_late_c: "đến hạn không muộn hơn c … vẫn không muộn hơn c" | "đến hạn chậm nhất vào ngày c, … vẫn chậm nhất vào ngày c" |
| 10 | 03-04-temporal-representativeness.vi.md:3 | "ngày rút không muộn hơn thời điểm đó" | "ngày rút chậm nhất vào thời điểm chốt đó" |
| 11 | 12-01-profiling-details.vi.md:75 | DQ18 header "đến hạn tính đến thời điểm chốt"; Bảng 3.1 says "chậm nhất vào thời điểm chốt" | aligned with Bảng 3.1 |
| 12 | 12-02-pipeline-package.vi.md:91, 98 | Bảng A.9 "+ các bài đến hạn tính đến thời điểm chốt" (×2) | "+ các bài đến hạn chậm nhất vào thời điểm chốt" |
| 13 | 12-04-traceability-change-log.vi.md:29 | C10 rule "đến hạn tính đến thời điểm chốt"; glossary row 00-2 and 04-01 use "chậm nhất vào thời điểm chốt" | aligned |
| 14 | 12-03-dictionary-lineage.vi.md:80, 82, 89 | "chậm nhất tại c" (×3) instead of the settled "chậm nhất vào ngày N" | "chậm nhất vào ngày c" |
| 15 | 12-03-dictionary-lineage.vi.md:11 | "Lớp nhỏ hơn" (reads as a classroom) for the smaller target class | "Lớp nhãn ít mẫu hơn" |
| 16 | 12-03-dictionary-lineage.vi.md:3, 5, 7 | Bảng A.11 says "cấp phân tích" while Mục 8 (08-00, 08-01) says "mức phân tích" for the same "analytics level" | "mức phân tích" in prose, caption and header |
| 17 | 06-03-split-leakage.vi.md:13 | First use of "fold" in the report has no gloss (glossary Usage: "fold (phần chia trong kiểm định chéo)") | gloss added at first use |
| 18 | 05-00-preparation-plan.vi.md:6 | "bias audit" rendered "bước kiểm tra thiên lệch"; every other file says "kiểm tra công bằng" for the audit | "bước kiểm tra công bằng" |
| 19 | 12-05-ai-decision-log.vi.md:21 | "Mục 8.3 của đề bài" capitalised while the brief's other sections are "mục 11/13.1/14 của đề bài" (lower case keeps them apart from report sections) | "mục 8.3 của đề bài" |

Checked without change:

- Terms: "học phần" appears only for the university's courses (00-0, 01-01, 07-03, 12-04); OULAD units use lượt đăng ký học, lượt mở (module), rút khỏi module, không hoàn thành; "kiểm định" only in "kiểm định chéo"; khảo sát dữ liệu (profiling), bảng dữ liệu đã chuẩn bị, bảng đặc trưng, thời điểm chốt dữ liệu vs ngày đến hạn, giảng viên hướng dẫn, tinh chỉnh siêu tham số, Chỉ số khó khăn đa chiều (IMD) are used consistently.
- Abbreviations: AI (10-00), AQ (01-01), CMA/TMA (02-00), CSV/DOI/SHA-256/OU (01-02), IMD (02-03), OULAD (01-01), SMART (01-01), UK (02-01), UTC (07-02) are each defined once at first use in document order and match 00-1; section pointers in 00-1 and 00-2 match the English.
- Openers: every file's first sentence mirrors the English bridge.
- Pointers: Bảng 1.1–8.1, Hình 3.1, Bảng/Hình A.1–A.18 and Phụ lục I–VI resolve to the right exhibits.
- Numbers: decimal comma and dot thousands throughout; raw tool output in Bảng A.18 (e.g. "28061", "(Pass, 12361)") and "-1" in Bảng A.5 stay as the English writes them.
- The remaining parity warnings are the two AI prompts quoted verbatim in English in 12-05 (by design, guide section 8).

Commands and results:

- `check_parity.py --report reports/milestone-3/report --lang vi`: 41 pairs, 0 errors, 13 warnings (all in the 12-05 verbatim prompts).
- `translation_status.py --mark` for the 11 edited files: 01-01, 03-04, 05-00, 06-02, 06-03, 09-00, 12-01, 12-02, 12-03, 12-04, 12-05.
- `glossary.py --lang vi lint`: 25 glossary files, 1677 terms, 0 errors.

Per file: all 41 twins read; 11 edited (19 findings fixed); parity 0 errors.
