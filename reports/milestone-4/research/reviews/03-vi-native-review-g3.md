## Review G3 – files 06, 07, 08, 09, 10-00, 10-01, 10-02 (native review, 2026-11-07)

Protocol: `.claude/skills/build-report/languages/vi/review.md` (three passes per file). Glossary coverage run first
(`glossary.py --lang vi --task milestone-4 coverage --report reports/milestone-4/report`: 15 drifting concepts); in this
group the drifting concepts present were rule-ranked list, capacity, gate S1 and Change Log entry; all aligned to the
glossary forms. 50 edits in total (49 scripted replacements, 1 punctuation fix after the parity warning).

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 06-00-genai-usage.vi.md | 11 | 3.3 Glossary forms (gate S1) | Một tiêu chí quyết định duy nhất S1 | Điều kiện đạt duy nhất S1 |
| 2 | 06-00-genai-usage.vi.md | 13 | 3.5 Plain wording | những điểm có hệ quả lớn nhất | những điểm có ảnh hưởng lớn nhất đến thiết kế |
| 3 | 06-00-genai-usage.vi.md | 13 | 3.6 Meaning (hedge "would be met by chance about 13% of the time") | sẽ được thỏa mãn do ngẫu nhiên trong khoảng 13% số trường hợp | vẫn có thể được đáp ứng do ngẫu nhiên với xác suất khoảng 13% |
| 4 | 06-00-genai-usage.vi.md | 13 | 3.1 One clear actor (bare "nhóm") | Nhóm đã kiểm chứng; giá trị do nhóm ấn định | Nhóm tác giả đã kiểm chứng; giá trị do nhóm tác giả ấn định |
| 5 | 07-00-prototype-protocol.vi.md | 3 | 3.5 Head noun / plain wording | không nhằm đạt điểm số cao nhất; Trên cơ sở phần đánh giá ở Phần 4 | không nhằm cạnh tranh để đạt điểm số cao nhất; Trên cơ sở thiết kế đánh giá ở Phần 4 |
| 6 | 07-00-prototype-protocol.vi.md | 3 | 3.5 Repeat the noun, not the pronoun | không thể thay đổi chúng | không thể thay đổi các lựa chọn này |
| 7 | 07-00-prototype-protocol.vi.md | 10 | 3.3 Glossary forms (rule-ranked list) | Danh sách xếp hạng theo quy tắc | Danh sách xếp theo quy tắc dấu hiệu sớm |
| 8 | 07-00-prototype-protocol.vi.md | 11 | 3.5 Parentheses for pointers | …, như Bảng 3.1 | … (Bảng 3.1) |
| 9 | 07-00-prototype-protocol.vi.md | 16 | 3.5 Established words | hồ sơ truy cập tập kiểm thử được ghi | bản ghi các lần truy cập tập kiểm thử được lưu |
| 10 | 07-00-prototype-protocol.vi.md | 18 | 3.1 Complete sentence (head noun of the subject) | Kết quả phương pháp cơ sở ngang bằng phương pháp ứng viên vẫn là… | Trường hợp phương pháp cơ sở đạt kết quả ngang bằng phương pháp ứng viên vẫn là… |
| 11 | 08-00-traceability.vi.md | 3, 14 | 3.3 Glossary forms (Change Log entry Cn) | mục C14 của nhật ký thay đổi có kiểm soát | thay đổi C14 trong Nhật ký thay đổi |
| 12 | 08-00-traceability.vi.md | 11, 12 | 3.3 Glossary forms (rule-ranked list) | danh sách xếp hạng theo quy tắc | danh sách xếp theo quy tắc dấu hiệu sớm |
| 13 | 08-00-traceability.vi.md | 12 | 3.3 Glossary forms (capacity) | số sinh viên liên hệ được | số sinh viên cán bộ liên hệ được |
| 14 | 08-00-traceability.vi.md | 12 | 3.6 Meaning ("contact deferred" adds no choice) | D1; lựa chọn cách liên hệ để lại sau | D1; phần liên hệ được hoãn |
| 15 | 08-00-traceability.vi.md | 14 | 3.1 Clear actor ("C14 protects", not purpose) | …, nhằm bảo đảm tính độc lập… | …; thay đổi này bảo đảm tính độc lập… |
| 16 | 10-00-appendices.vi.md | 3 | 3.5 Plain wording / parentheses | thiết kế đứng sau phần nội dung chính; AQ Modeling Brief (…) (Phụ lục I); Evaluation Design Card (…) (Phụ lục III) | thiết kế làm cơ sở cho phần nội dung chính; AQ Modeling Brief, là … (Phụ lục I); Evaluation Design Card, là … (Phụ lục III) – no double parentheses |
| 17 | 10-00-appendices.vi.md | 3 | 3.3 Glossary forms (Change Log entry Cn) | mục C14 của nhật ký thay đổi có kiểm soát | thay đổi C14 trong Nhật ký thay đổi |
| 18 | 10-00-appendices.vi.md | 3 | 3.5 Plain wording | chỉ dùng các lượt mở | chỉ tính trên các lượt mở |
| 19 | 10-01-briefs-full.vi.md | 3 | 3.1 Light function words (double "là") | không hoàn thành nghĩa là kết quả cuối cùng là… | sinh viên được tính là không hoàn thành khi kết quả cuối cùng là… |
| 20 | 10-01-briefs-full.vi.md | 9 | 3.1 Vietnamese order | rút khỏi module theo module | rút khỏi module, phân theo module |
| 21 | 10-01-briefs-full.vi.md | 11 | 3.5 Plain wording | D2 (thời gian của cố vấn học tập được dành cho đâu) | D2 (phân bổ thời gian của cố vấn học tập) |
| 22 | 10-01-briefs-full.vi.md | 12, 22 | 3.5 Plain wording | bài đánh giá đối với…; đi kèm với việc sinh viên… | bài đánh giá khi xét…; gắn với khả năng sinh viên… |
| 23 | 10-01-briefs-full.vi.md | 28 | 3.1 Relational pair / one breath | cả chưa hiệu chỉnh lẫn trong từng lượt mở module, với tỉ số odds … đặt bên cạnh | gồm ước lượng chưa hiệu chỉnh và ước lượng trong từng lượt mở module, kèm tỉ số odds … |
| 24 | 10-01-briefs-full.vi.md | 29 | 3.1 Voice ("bị" for a neutral outcome) | vẫn chưa bị xem | vẫn được giữ kín |
| 25 | 10-01-briefs-full.vi.md | 40 | 3.3 Glossary forms (on or before the cut-off) | có ngày ghi nhận trùng hoặc trước thời điểm chốt; cùng lượt nhấp theo tuần | được ghi nhận tính đến hết thời điểm chốt; có thêm số lượt nhấp theo tuần |
| 26 | 10-01-briefs-full.vi.md | 41 | 3.6 Meaning ("only if calibration holds") | khi mô hình được hiệu chuẩn tốt | khi kết quả hiệu chuẩn đạt yêu cầu |
| 27 | 10-01-briefs-full.vi.md | 48 | 3.6 Meaning (gain over the run's base rate, not over chance) + glossary (lift, capacity) | trong giới hạn số sinh viên giả định liên hệ được …, với mức vượt so với ngẫu nhiên | với số sinh viên cán bộ liên hệ được theo giả định …, với mức vượt tỷ lệ nền (lift) của lượt mở |
| 28 | 10-01-briefs-full.vi.md | 52, 53 | 3.5 Head noun / plain wording | không có kết quả nào của việc liên hệ; các lý do đứng sau | không ghi nhận kết quả của việc liên hệ; các lý do dẫn đến điểm rủi ro đó |
| 29 | 10-01-briefs-full.vi.md | 54, 55 | 3.3 Glossary forms (capacity) | dài đúng mức mà số sinh viên liên hệ được cho phép; Số sinh viên liên hệ được | có độ dài bằng số sinh viên cán bộ liên hệ được; Số sinh viên cán bộ liên hệ được |
| 30 | 10-02-candidate-comparison.vi.md | 3 | 3.1 Complete predicate | Các thông tin về dữ liệu lấy từ | Các thông tin về dữ liệu được lấy từ |
| 31 | 10-02-candidate-comparison.vi.md | 12, 16 | 3.5 Empty words / complete phrase | ước lượng một phương sai; Vấn đề hội tụ và vấn đề có ít cụm | ước lượng phương sai; Dễ gặp vấn đề hội tụ và vấn đề do có ít cụm |
| 32 | 10-02-candidate-comparison.vi.md | 18 | 3.3 One term per concept (gap = rate difference) | khoảng cách (2×) | khoảng chênh lệch; chênh lệch chưa hiệu chỉnh |
| 33 | 10-02-candidate-comparison.vi.md | 24 | 3.6 Form (double parentheses in a header) | …(penalised logistic regression) (phương pháp chính) | Ứng viên 1 (phương pháp chính): … (penalised logistic regression) |
| 34 | 10-02-candidate-comparison.vi.md | 26 | 3.3 Glossary forms (flag) | Gắn cờ khi có… | Đánh dấu sinh viên có… |
| 35 | 10-02-candidate-comparison.vi.md | 27, 33 | 3.5 Complete phrase | chứ không tại một thời điểm; mang lại được bao nhiêu | chứ không gắn với một thời điểm cụ thể; đóng góp được bao nhiêu vào thứ hạng |
| 36 | 10-02-candidate-comparison.vi.md | 35 | 3.1 One idea, one breath (three-reason sentence) | one sentence with three reasons joined by semicolons | "Thứ nhất, …. Thứ hai, …. Thứ ba, …; rủi ro này nghiêng về một mô hình đơn giản, ổn định" |
| 37 | 10-02-candidate-comparison.vi.md | 36 | 3.1 Complete sentence ("vì … thì" without a main clause, unclear actor) | vì một đánh giá chuẩn (benchmark) đã loại … thì không thể cho thấy cây vượt hồi quy logistic [19]; cây chỉ thay thế… | vì kết quả của một benchmark không đủ để cho thấy cây vượt hồi quy logistic khi benchmark đó đã loại … [19]. Cây tăng cường độ dốc chỉ thay thế… |
| 38 | 10-02-candidate-comparison.vi.md | 42 | 3.3 Glossary forms (rule-ranked list) | danh sách xếp hạng theo quy tắc | danh sách xếp theo quy tắc dấu hiệu sớm |
| 39 | 10-02-candidate-comparison.vi.md | 44 | 3.3 Glossary forms (capacity) + head noun | Danh sách theo số dấu hiệu; số sinh viên liên hệ được (2×) | Xếp theo số dấu hiệu; số sinh viên cán bộ liên hệ được |
| 40 | 10-02-candidate-comparison.vi.md | 46 | 3.3 Glossary ("khớp" reads as "match"/fit) | Thứ tự nguy cơ khớp với nhu cầu hỗ trợ | Thứ tự nguy cơ trùng với thứ tự nhu cầu hỗ trợ |
| 41 | 10-02-candidate-comparison.vi.md | 35 | 3.5 Punctuation (parity warning) | về sau, và rủi ro này | về sau; rủi ro này |

Per-file close:

- 06-00-genai-usage.vi.md: reviewed, 4 edits, parity 0 errors, 0 warnings.
- 07-00-prototype-protocol.vi.md: reviewed, 6 edits, parity 0 errors, 0 warnings.
- 08-00-traceability.vi.md: reviewed, 5 edits, parity 0 errors, 0 warnings.
- 09-references.vi.md: reviewed (heading and intro sentence only; entries identical to the English), no findings, parity 0 errors, 0 warnings.
- 10-00-appendices.vi.md: reviewed, 4 edits, parity 0 errors, 0 warnings.
- 10-01-briefs-full.vi.md: reviewed, 14 edits (one meaning error: "mức vượt so với ngẫu nhiên" for gain over the base rate), parity 0 errors, 0 warnings.
- 10-02-candidate-comparison.vi.md: reviewed, 17 edits, parity 0 errors, 0 warnings (after fix 41).
- `translation_status.py --report reports/milestone-4/report --lang vi --mark` on the 7 files: recorded 7 file(s).

Terms for the glossary to settle: (1) "gap" (between rates) → "chênh lệch", never "khoảng cách"; (2) table cell form of
capacity: "số sinh viên cán bộ liên hệ được" (the full row form "… mỗi tuần" is too long for cells and k is per run, not
per week); (3) "contact deferred" (AQ4) → "phần liên hệ được hoãn", as in 01-02; (4) "baseline" of a model comparison →
"phương pháp cơ sở", distinct from KPI "mức cơ sở" (coverage reports it as drift although the use is consistent).
