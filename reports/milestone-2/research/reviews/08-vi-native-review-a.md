# Review 2-A – native review of the rewritten twins 00-0 to 04-02

Date: 2026-11-06. Reviewer: a native Vietnamese reviewer (an agent separate from the rewrite-A translator). Scope: `00-0`,
`00-1`, `00-2`, `01-00`, `01-01`, `01-02`, `02-00`, `02-01`, `02-02`, `02-03`, `03-00`, `04-00`, `04-01`, `04-02`
(`*.vi.md` in `reports/milestone-2/report/`). Each file went through the three passes of `review.md`: a reader pass on the
Vietnamese alone, a fidelity pass sentence by sentence against the English, then the checklist. References: `guide.md`,
`lessons.md`, the merged glossary (`glossary.py --lang vi --task milestone-2 show`), `reader-test.md`, `rewrite-A.md`.

## Findings fixed

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 00-0-title-page.vi.md | 24 | 3.6 Numbers (dates) | "Tháng 11/2026" | "Tháng 11 năm 2026" |
| 2 | 00-1-abbreviations.vi.md | 12 | 3.6 Meaning complete (nothing added) | "… do nơi phát hành cung cấp. Nhóm ghi mã này vào manifest, là danh sách …" | "… do nơi phát hành cung cấp và được ghi trong manifest, tức danh sách các tệp đã thu thập kèm mã kiểm tra của từng tệp" (the English sentence, with a short gloss of the kept English term) |
| 3 | 00-2-glossary.vi.md | 9 | 3.6 Meaning complete | "tạo lại bộ dữ liệu đã thu thập" | "tạo lại dữ liệu đã thu thập" ("re-create the collected data") |
| 4 | 00-2-glossary.vi.md | 14 | 3.6 Meaning complete | "Ngày cuối cùng có dữ liệu được dùng để lập danh sách" | "… được phép dùng …" ("may use") |
| 5 | 01-01-frozen-baseline.vi.md | 5 | 3.6 Meaning complete (English now defines KPI 1) | "trong số sinh viên bỏ lỡ hoặc nộp trễ từ hai bài được chấm điểm trở lên tính đến hết tuần 4, bao nhiêu phần trăm …" | "trong số sinh viên có dấu hiệu sớm tính đến tuần 4, bao nhiêu phần trăm được liên hệ trước khi hết tuần 5" (the English defines the denominator as students showing early signs by week 4, not the rule) |
| 6 | 01-01-frozen-baseline.vi.md | 5 | 3.6 Meaning complete | "trong vòng bảy ngày sau khi danh sách được gửi" | "trong vòng bảy ngày kể từ khi có danh sách" ("within seven days of the list") |
| 7 | 01-01-frozen-baseline.vi.md | 14 | 3.6 Meaning complete; 3.1 clear actor | "Chỉ với dữ liệu …, mô hình nhận ra đúng đến mức nào …, khi so với một quy tắc đơn giản dựa trên kết quả các bài được chấm điểm" | "Dữ liệu ghi nhận đến hết tuần 2 và hết tuần 4 dự báo được việc sinh viên không hoàn thành học phần tốt đến mức nào, so với một quy tắc đơn giản dựa trên các bài được chấm điểm bị bỏ lỡ" (the English names the rule "based on missed assessed tasks" and no model) |
| 8 | 01-02-scope-change-log.vi.md | 5 | 3.6 Meaning complete (remove additions) | "(liên hệ ai, liên hệ thế nào và kết quả sau đó) chưa được phân tích ở Milestone này; phần này được giữ …" | "(liên hệ ai và liên hệ theo cách nào) được giữ làm yêu cầu dữ liệu cho đợt thí điểm" |
| 9 | 01-02-scope-change-log.vi.md | 5 | 3.5 Plain wording; 3.5 "hoặc" | "ảnh hưởng đến … hay các quyết định. Các thay đổi này chỉ làm hẹp phần mà mỗi câu hỏi trả lời được bằng dữ liệu mở." | "làm thay đổi … hoặc các quyết định; các thay đổi này chỉ thu hẹp phạm vi trả lời của từng câu hỏi trên dữ liệu mở." |
| 10 | 02-01-aq-data-matrix.vi.md | 4 | 3.1 Vietnamese order | "Bảng 2.1 nêu, cho từng câu hỏi, những gì cần đo" | "Với từng câu hỏi, Bảng 2.1 nêu những gì cần đo" |
| 11 | 02-01-aq-data-matrix.vi.md | 15 | 3.1 Collocations | "phân biệt tạm ngừng học, chuyển chương trình đào tạo với thôi học" | "phân biệt tạm ngừng học, chuyển chương trình đào tạo và thôi học" (three-way distinction) |
| 12 | 02-01-aq-data-matrix.vi.md | 15 | 3.5 No "của chúng"; 3.5 Parentheses | "những phần câu hỏi cần đến chúng … (Partial) (Phụ lục V)" | "những phần câu hỏi cần đến các biến đó … (Partial, Phụ lục V)" |
| 13 | 02-02-requirements-by-level.vi.md | 3, 7 | 3.6 Meaning complete (hedge) | "những gì dữ liệu (đó) cho thấy" | "những gì dữ liệu (đó) có thể cho thấy" ("can show") |
| 14 | 02-02-requirements-by-level.vi.md | 14 | 3.3 One term per concept (reader-test #27: "trường" field vs university) | "trường chưa có sổ theo dõi liên hệ" | "nhà trường chưa có sổ theo dõi liên hệ" |
| 15 | 02-02-requirements-by-level.vi.md | 16 | 3.3 Glossary forms | "mức khó khăn kinh tế – xã hội của khu vực sinh viên cư trú" | "mức khó khăn kinh tế – xã hội của khu vực cư trú" (glossary row "deprivation band") |
| 16 | 02-02-requirements-by-level.vi.md | 16 | 3.5 No "chúng" | "…; chúng không bao giờ là lý do để đưa …" | "…, không bao giờ dùng làm lý do để đưa …" |
| 17 | 02-03-prediction-point-leakage.vi.md | 13 | 3.6 Meaning complete (remove additions) | "…; bài đến hạn sau ngày rút không được tính." / "… cũng không được tính …" | clause removed; "cũng" removed (the English states only the rule) |
| 18 | 03-00-search-strategy.vi.md | 4 | 3.3 One term per concept (as in 00-1) | "Kho dữ liệu học máy của University of California, Irvine (UCI)" | "Kho dữ liệu học máy của Đại học California tại Irvine (UCI)" |
| 19 | 04-01-criteria-gates.vi.md | 3 | 3.5 Parentheses for glosses | "khả năng xử lý chất lượng dữ liệu, tức là các lỗi … hay không;" | "khả năng xử lý chất lượng dữ liệu (các lỗi trong dữ liệu có xử lý được hay không);" |
| 20 | 04-01-criteria-gates.vi.md | 6 | 3.6 Meaning complete | "Điểm số giúp so sánh các bộ dữ liệu" | "Điểm số làm cơ sở cho phần thảo luận" ("support the discussion") |
| 21 | 04-01-criteria-gates.vi.md | 6 | 3.3 One term per concept ("điểm" = score in this section) | "Một số điểm tài liệu chưa làm rõ … Nhóm ghi các điểm này thành điều kiện …" | "Những thông tin mà tài liệu chưa làm rõ nhưng tệp dữ liệu có thể xác nhận được nhóm ghi thành điều kiện …" |
| 22 | 04-02-selection-matrix.vi.md | 3 | 3.1 Sentences | "vì có hai cột mỗi cột ghép hai tiêu chí: biến kết quả / thời điểm và …" | "vì có hai cột ghép đôi tiêu chí: cột biến kết quả / thời điểm và cột tài liệu / giấy phép" |
| 23 | 04-02-selection-matrix.vi.md | 17 | 3.6 Meaning complete (remove additions); 3.5 Punctuation | "…, nên bộ dữ liệu này không có kết quả theo từng học phần; ngoài ra, UCI 697 chỉ có …" | "UCI 697 chỉ gán nhãn cho sinh viên ở cấp chương trình đào tạo vào cuối năm thứ ba hoặc thứ tư; bộ dữ liệu này cũng chỉ có số liệu gộp theo học kỳ [4], [5]." |
| 24 | 04-02-selection-matrix.vi.md | 17 | 3.3 One term per concept ("điểm" = score) | "chưa làm rõ một số điểm … xác nhận những điểm đó" | "chưa làm rõ một số thông tin … xác nhận những thông tin đó" |

## Kept after review (justified)

- 01-01:5 "Dự án theo dõi ba chỉ số đo lường hiệu quả chính (KPI)": the count follows from the English (one primary,
  two secondary KPIs) and gives the abbreviation its full form at first use.
- 01-01:5 "mức cơ sở 70% … mức mục tiêu 75%": glossary terms naming what the two English figures are.
- 01-01:15 "yêu cầu đối xử công bằng giữa các nhóm sinh viên" for "fairness limits": the report checks fairness across
  groups (Section 2.2); the reader test flagged a bare "yêu cầu công bằng" as undefined.
- 03-00:15 "Phiếu khảo sát, mỗi sinh viên một phiếu" for "Questionnaire": the reader test (#34) needed the unit stated.

## Closing lines

- 00-0-title-page: reviewed, 1 finding fixed, parity 0 errors 0 warnings.
- 00-1-abbreviations: reviewed, 1 finding fixed, parity 0 errors 0 warnings.
- 00-2-glossary: reviewed, 2 findings fixed, parity 0 errors 0 warnings.
- 01-00-baseline-scope: reviewed, no finding, parity 0 errors 0 warnings.
- 01-01-frozen-baseline: reviewed, 3 findings fixed, parity 0 errors 0 warnings.
- 01-02-scope-change-log: reviewed, 2 findings fixed, parity 0 errors 0 warnings.
- 02-00-data-requirements: reviewed, no finding, parity 0 errors 0 warnings.
- 02-01-aq-data-matrix: reviewed, 3 findings fixed, parity 0 errors 0 warnings.
- 02-02-requirements-by-level: reviewed, 4 findings fixed, parity 0 errors 0 warnings.
- 02-03-prediction-point-leakage: reviewed, 1 finding fixed, parity 0 errors 0 warnings.
- 03-00-search-strategy: reviewed, 1 finding fixed, parity 0 errors 0 warnings.
- 04-00-evaluation-selection: reviewed, no finding, parity 0 errors 0 warnings.
- 04-01-criteria-gates: reviewed, 3 findings fixed, parity 0 errors 0 warnings.
- 04-02-selection-matrix: reviewed, 3 findings fixed, parity 0 errors 0 warnings (after fixing one comma before "và").

Each file was then recorded with `translation_status.py --report reports/milestone-2/report --lang vi --mark FILE.md`.
A sweep of the 14 twins finds none of the replaced forms ("thiếu thốn", "thông tin nền", "đợt mở học phần", "số sinh
viên cán bộ", "tổng hợp", "kiểm thử"); "độ chính xác" appears only as "độ chính xác của danh sách (precision)" at 02-01:13.
