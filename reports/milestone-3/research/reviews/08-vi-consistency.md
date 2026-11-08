# Consistency pass – Vietnamese twins of milestone-3 (2026-11-08)

Stage 5, first part (build-report reference.md section 4.3): whole-report consistency read after the group reviews
A–D. Scope: every `reports/milestone-3/report/*.vi.md`, read in file order (front matter, Parts 1–10, references,
Appendices I–VI). English files and glossary files untouched.

## Commands and results

| Step | Command | Before | After |
| :---- | :---- | :---- | :---- |
| 1 | `check_parity.py --report reports/milestone-3/report --lang vi` | 21 errors, 14 warnings | 0 errors, 14 warnings |
| 2 | `check_abbreviations.py --report reports/milestone-3/report --lang vi` | 3 violations | 0 violations |
| 3 | `glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report` | 19 drifting | 17 drifting (all checked: false positives, see below) |
| 3 | cross-reference comparison (Section/Table/Figure/Appendix/Part vs Mục/Bảng/Hình/Phụ lục/Phần, per file pair; scratch script `xref.py`) | 11 differences | 0 real differences (all were "Cấu trúc của Mục N" announcements, "Phụ lục I, Bảng A.5" regex artefacts, or the English prompt in 12-05) |
| 4 | `glossary.py --lang vi lint` | – | 25 files, 1818 terms, 0 errors |
| 5 | `translation_status.py --report … --lang vi --mark` (20 edited files) | – | 20 recorded; 41 sections, 0 to translate, 0 orphans |

The 14 remaining parity warnings are all in 12-05 lines 25–36 and 59–70: the two verbatim English AI prompts (block
quotes), which stay in English by design ("Section 4", "test", untranslated lines).

## What drifted and what changed

### Step 1 – parity errors (Replaces forms from the settled glossary rows)

| File:line | Before | After |
| :---- | :---- | :---- |
| 00-2:20 | mỗi kỳ mở được giữ lại một lần | lần lượt từng kỳ mở được tách ra để đánh giá |
| 05-00:21 | dùng … làm biến dự báo | dùng … làm đặc trưng |
| 06-02:21 | không dùng làm biến dự báo | không dùng làm đặc trưng |
| 07-02:3 (×2) | biến dự báo; một danh sách biến dự báo | đặc trưng; một danh sách đặc trưng |
| 09-00:10 (×2) | hạn chế dùng chúng làm biến dự báo; … là một biến dự báo | hạn chế dùng chúng làm đặc trưng; … được dùng làm đặc trưng |
| 09-00:12 | vào nhóm biến dự báo | vào nhóm đặc trưng |
| 12-01:129 | sáu điểm không nhất quán | sáu loại không nhất quán |
| 12-01:144 (×2) | **Điểm số và khối lượng học.** … Khối lượng học lên tới 655 tín chỉ | **Điểm số và số tín chỉ đang học.** … Số tín chỉ đang học lên tới 655 |
| 12-01:160 | số tín chỉ này đo khối lượng học | số tín chỉ này phản ánh tổng lượng học tập trên mọi module sinh viên đang theo học (avoids the tautology "số tín chỉ đo số tín chỉ đang học") |
| 12-03:36, 45, 113 | biến dự báo của AQ3; AQ3 (khối lượng học); khối lượng học | đặc trưng của AQ3; AQ3 (số tín chỉ đang học); số tín chỉ đang học |
| 12-04:31 | không phải biến dự báo trong AQ3 | không phải đặc trưng của AQ3 |
| 12-05:13, 45, 52, 79, 81, 86 (×2) | lọt vào biến dự báo; không làm/không bao giờ là biến dự báo; biến dự báo mở rộng; danh sách biến dự báo | lọt vào nhóm đặc trưng; không làm/không bao giờ là đặc trưng; đặc trưng mở rộng; danh sách đặc trưng |

### Step 2 – abbreviations defined twice

| File:line | Before | After |
| :---- | :---- | :---- |
| 02-03:3 | ở mọi xứ thuộc Vương quốc Anh | ở mọi xứ thuộc UK (UK defined in 02-01) |
| 03-05:3 | tác động đến các câu hỏi phân tích | tác động đến các AQ (AQ defined in 01-01) |
| 04-00:3 | từng câu hỏi phân tích (AQ) | từng AQ |

### Step 3 – cross-file drift found in the read

| File:line | Drift | Change |
| :---- | :---- | :---- |
| 04-01:11; 12-02:14; 12-03:10, 79, 98; 05-00:11 | "lượt đang đăng ký học vào ngày d" (lượt + đăng ký học twice) beside the glossary form "lượt đăng ký học còn hiệu lực tại ngày d" | "lượt (đăng ký học) còn hiệu lực tại ngày d"; "sinh viên đang đăng ký học vào ngày d" kept where the subject is a student, and the defined condition "đang đăng ký học vào ngày d" (terms page, C09) kept |
| 08-02:17; 12-06:32 | "đang đăng ký học tại ngày 13" | "vào ngày 13" (the form of 03-03 and the terms page) |
| 12-04:42, 76 | "còn hiệu lực vào ngày 14" | "còn hiệu lực tại ngày 14" |
| 12-01:75; 12-04:29 (×3), 56, 59; 12-05:46; 12-06:32 | rule "kích hoạt" (appendices) while the body says "đánh dấu được sinh viên" (glossary "(a rule) fires") | rewritten with "đánh dấu (được) sinh viên"; firing rate → "tỷ lệ sinh viên được quy tắc / từng thành phần đánh dấu" |
| 12-01:138 | "Không điểm nào … mỗi điểm nhận" (refers back to the six inconsistencies, now "loại") | "Không loại nào … mỗi loại nhận" |
| 12-02:129 (×2) | held-out run as "kỳ mở được để riêng" | "tách riêng một kỳ mở để đánh giá"; "kỳ mở được tách ra để đánh giá" |
| 12-04:73, 82 | headings "…, trình bày đầy đủ" (calque of "in full") | "Chi tiết về các thay đổi từ Milestone 2."; "Chi tiết về chính sách dữ liệu giả lập." |
| 12-03:18 | lineage header "Tệp nguồn / trường … Cửa sổ thời gian / bộ lọc" vs 07-02 for the same brief template | "Tệp / trường nguồn … Khoảng thời gian / điều kiện lọc" |
| 12-05:15, 51, 104 | window as "cửa sổ (cố định) trước ngày bắt đầu"; elsewhere "khoảng thời gian" | "khoảng thời gian (cố định) trước ngày bắt đầu" |
| 12-03:79 | "mức trung bình của kỳ mở module" | "mức trung bình của kỳ mở" (glossary; 12-03:111) |
| 05-00:15; 12-01:73 | heavy users as "người dùng hoạt động nhiều" | "sinh viên dùng nền tảng rất nhiều" (glossary; 03-03, 12-01:142) |
| 12-05:100 | fact as "thông tin" | "thông tin làm căn cứ" (glossary "fact") |
| 10-00:35 | bare "AI phản biện" | "AI phản biện quy trình chuẩn bị" (role name) |
| 02-01:3 | "nhóm tác giả bộ dữ liệu" (clashes with "nhóm tác giả" = the team) | "các tác giả của bộ dữ liệu" |
| 08-01:12 | "bổ sung thời điểm chốt dữ liệu thứ hai tại ngày 13" (reads as a contradiction: day 13 is called the first cut-off in 03-04 and 12-01) | "bổ sung thêm một thời điểm chốt dữ liệu tại ngày 13" (English: "add a second cut-off at day 13") |
| 12-06:34 | "trước và sau xử lý" | "trước và sau chuẩn bị" (title of 7.1 and Table 7.1) |
| 04-01:14 | concurrent enrolment as "lượt đăng ký học diễn ra đồng thời ở hai kỳ mở" | glossary first-use form "lượt đăng ký học đồng thời (diễn ra cùng lúc ở hai kỳ mở)" |
| 00-2:14 | "bài đến hạn tính đến thời điểm chốt dữ liệu" | "tính đến hết thời điểm chốt dữ liệu" (body form, 04-01:14) |
| 00-2:27 | Precision "trượt hoặc rút học phần" | "trượt hoặc rút khỏi module" (form of 04-01:14, the section it points to) |
| 00-1:13 | IMD row "mức khó khăn theo khu vực" | "mức khó khăn của khu vực" (glossary short form) |

### Coverage warnings checked and left as they are

The 17 remaining coverage warnings were checked one by one; none is a real drift in this report:

- due by / by the cut-off: the body consistently writes "tính đến hết ngày N / tính đến hết thời điểm chốt dữ liệu"; the
  glossary row's "thời điểm dự báo" conflicts with the "data cut-off" row (see open points).
- gate (S1), capacity (Milestone 4), capacity scenarios, profile (AQ1 output), NIST AI RMF verbs: the concept does not
  occur in this report, or occurs under its full first-use form ("kịch bản số sinh viên cán bộ liên hệ được mỗi tuần",
  three times, each in a different file); the matches come from other senses of the English word ("dataset entry gate",
  "profile.json", "measure").
- enrolment: "lượt đăng ký học" is the OULAD unit (correct per the topic row "enrolment (OULAD unit …)").
- flag, gap, coverage, baseline, attendance, measure, scaling, stand-in, fact, deprivation band, non-completion: the
  English word mostly carries another sense here (data-quality flag "cờ", missing-data gap "khoảng trống", temporal
  coverage "phạm vi thời gian", project baseline "phiên bản cơ sở", random-list baseline "mốc so sánh"), and the senses
  the rows cover use the glossary form wherever they occur; deprivation band uses its short form "mức khó khăn của khu
  vực" after the full form.

### Cross-references, front matter, bridges

- Every Mục/Bảng/Hình/Phụ lục/Phần reference matches the English file by file (script comparison above, then read).
- Abbreviation page (00-1): each full form matches its first use in the body (AI 10-00, AQ and KPI 01-01, CMA/TMA 02-00,
  CSV/DOI/SHA-256/OU 01-02, IMD 02-03, OULAD 01-01, UK 02-01, UTC 06-01, EDA 10-00).
- Terms page (00-2): each Vietnamese name matches the body term (after the two fixes above).
- File bridges read naturally in Vietnamese in every consecutive pair; no change needed.

## Edits per file

| File | Edits |
| :---- | :---- |
| 00-1-abbreviations.vi.md | 1 |
| 00-2-glossary.vi.md | 3 |
| 02-01-population-unit-keys.vi.md | 1 |
| 02-03-codes-sensitive.vi.md | 1 |
| 03-05-quality-issue-log.vi.md | 1 |
| 04-00-aq-data-fit.vi.md | 1 |
| 04-01-fit-ratings.vi.md | 2 |
| 05-00-preparation-plan.vi.md | 3 |
| 06-02-integration-features.vi.md | 1 |
| 07-02-lineage-dictionary.vi.md | 2 |
| 08-01-views-by-level.vi.md | 1 |
| 08-02-readiness-matrix.vi.md | 1 |
| 09-00-ethics-limitations.vi.md | 3 |
| 10-00-genai-reflection.vi.md | 1 |
| 12-01-profiling-details.vi.md | 8 |
| 12-02-pipeline-package.vi.md | 3 |
| 12-03-dictionary-lineage.vi.md | 7 |
| 12-04-traceability-change-log.vi.md | 10 |
| 12-05-ai-decision-log.vi.md | 12 |
| 12-06-validation-ledger.vi.md | 3 |
| **Total (20 files)** | **65** |

## Open points (glossary rows to decide; not edited here)

1. `topics/course-completion-early-contact.md`, row "due by day N / by the cut-off": the Vietnamese form ends in "tính
   đến hết thời điểm dự báo", while the row "data cut-off" fixes "thời điểm chốt dữ liệu" and the row "due day" says to
   keep "thời điểm chốt dữ liệu" for days 13 and 27. The report uses "tính đến hết thời điểm chốt dữ liệu" throughout;
   the row should say the same, otherwise coverage keeps flagging it.
2. The row "registered at day d" gives "còn hiệu lực tại ngày d"; the terms page and C09 define "Đang đăng ký học vào ngày
   d". Both now appear by subject (lượt → "còn hiệu lực", sinh viên / the defined condition → "đang đăng ký học"); the
   row's Usage could record this split.
3. The coverage check flags terms whose English word has other senses in this report (flag, gap, coverage, baseline,
   measure, profile); narrowing those rows' English patterns would make the check quieter.
