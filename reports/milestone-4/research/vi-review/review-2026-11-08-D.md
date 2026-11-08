# Vietnamese native review – group D (references and appendices)

Reviewer: native-review agent D (not the translator), 2026-11-08. Protocol: `.claude/skills/build-report/languages/vi/review.md`, three passes per file (reader, fidelity, checklist). Files: `09-references.vi.md` (heading and introduction only), `10-00-appendices.vi.md` to `10-07-traceability-full.vi.md`. Paths below are relative to `reports/milestone-4/report/`; line numbers are those of the twin before the edit.

Glossary coverage before the passes (`glossary.py --lang vi --task milestone-4 coverage --report reports/milestone-4/report`): 18 drifting concepts report-wide. Those touching this group: scaling / encoding (fitted) → "phép chuẩn hóa thang đo / phép mã hóa" (10-03 step 3 aligned); flag (noun) → "nhãn bị đánh dấu" (10-05 R14 aligned); fact → "thông tin làm căn cứ" (10-06 aligned); Before / After → "Nội dung cũ / Nội dung mới" (10-07 Table A.13 already aligned); predictor → "biến dự báo" (the Milestone 4 form, already used throughout); recall at capacity, deprivation band, capacity, primary / extended predictors: already in the Milestone 4 forms ("tỷ lệ phát hiện trong giới hạn danh sách", "mức khó khăn của khu vực", "hạn mức liên hệ", "nhóm biến chính / nhóm mở rộng"); programme, tutor (teaching assistant), enrolment / admission, reviewer / sparring partner, retention, measure: not present in this group, or present in the OULAD sense the glossary gives ("giảng viên hướng dẫn", "lượt đăng ký học").

Cross-references checked in pass 2 against the English after the renumbering: Phụ lục I–VII, Bảng A.1–A.13, Hình A.1–A.2, Mục 2.1, 2.2, 3.3, 4.1, 4.2, 5.2, Phần 6 (Bảng 6.1), Bảng A.5 bước 4 and bước 7, Bảng A.8 and R8–R13: every pointer matches its English counterpart. Glossary population (Milestone 4) → "phạm vi dữ liệu" also applied in 10-03 and 10-06. Checked and kept: Table A.11 row 1 states the two-thirds rule of AQ2 in full; the rule is the one of success criterion of AQ2 in Table 4.2 (Section 4.1), so the gloss is accurate and helps the row read on its own.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 10-01-candidate-comparison.vi.md | 3 | 3.5 Parentheses for side information | mà câu hỏi đó phục vụ, như Mục 2.2 đã trình bày. | mà câu hỏi đó phục vụ (Mục 2.2). |
| 2 | 10-01-candidate-comparison.vi.md | 7 | 3.5 No empty words | Các thông tin về dữ liệu được lấy từ 9 kỳ mở | Thông tin về dữ liệu lấy từ 9 kỳ mở |
| 3 | 10-01-candidate-comparison.vi.md | 15 | 3.1 Vietnamese order (pooled within-run read as pooled in each run) | Chênh lệch nguy cơ gộp trong từng kỳ mở cho mỗi dấu hiệu, cùng chênh lệch riêng | Chênh lệch nguy cơ của mỗi dấu hiệu, so sánh trong cùng kỳ mở rồi gộp lại, cùng chênh lệch riêng |
| 4 | 10-01-candidate-comparison.vi.md | 15 | 3.5 Head nouns present (outcomes) | Cho thấy tổ hợp dấu hiệu nào phân tách các kết quả | Cho thấy tổ hợp dấu hiệu nào tách sinh viên hoàn thành với sinh viên không hoàn thành |
| 5 | 10-01-candidate-comparison.vi.md | 16 | 3.6 Meaning complete (few, not too few) | 6 module và 9 kỳ mở là quá ít để ước lượng một phương sai | 6 module và 9 kỳ mở là ít để ước lượng một thành phần phương sai |
| 6 | 10-01-candidate-comparison.vi.md | 22 | 3.3 Glossary forms (gap → chênh lệch, not khoảng) | biết độ lớn khoảng chênh lệch của từng dấu hiệu | biết độ lớn chênh lệch của từng dấu hiệu |
| 7 | 10-01-candidate-comparison.vi.md | 39 | 3.1 Collocations (rủi ro này nghiêng về) | rủi ro cần kiểm tra là khả năng áp dụng cho một kỳ mở về sau; rủi ro này nghiêng về một mô hình đơn giản, ổn định [6]. | rủi ro cần kiểm tra là khả năng áp dụng mô hình cho một kỳ mở về sau; với rủi ro này, một mô hình đơn giản, ổn định có lợi thế hơn [6]. |
| 8 | 10-01-candidate-comparison.vi.md | 40 | 3.1 Relational pairs complete | đến từ mức tham gia học tập, chứ không từ module | đến từ mức tham gia học tập, chứ không phải từ module |
| 9 | 10-01-candidate-comparison.vi.md | 48 | 3.3 Glossary forms (activity ratio) | khi bằng nhau thì ưu tiên mức hoạt động tương đối thấp hơn | khi bằng nhau thì ưu tiên sinh viên có tỷ lệ hoạt động thấp hơn |
| 10 | 10-01-candidate-comparison.vi.md | 55 | 3.3 Formal register (Not available) | \| Không khả dụng \| | \| Chưa áp dụng được \| |
| 11 | 10-02-metric-definitions.vi.md | 3 | 3.1 One main idea, one breath (symbols listed after 'cho') | dùng các chỉ số được định nghĩa trong Bảng A.4, cho kỳ mở r có n lượt đăng ký học, tập sinh viên không hoàn thành Y, tỷ lệ nền b = \|Y\|/n và danh sách L gồm k điểm rủi ro cao nhất; Mục 4.1 giải thích bằng lời các chỉ số chính. | dùng các chỉ số định nghĩa trong Bảng A.4; Mục 4.1 giải thích bằng lời các chỉ số chính. Các ký hiệu xét một kỳ mở r có n lượt đăng ký học: Y là tập sinh viên không hoàn thành của kỳ mở đó, b = \|Y\|/n là tỷ lệ nền và L là danh sách gồm k điểm rủi ro cao nhất. |
| 12 | 10-02-metric-definitions.vi.md | 17 | 3.3 English term at first use | \| Hiệu chuẩn tổng thể \| Hệ số chặn của mô hình logistic cho kết quả, | \| Hiệu chuẩn tổng thể (calibration-in-the-large) \| Hệ số chặn của mô hình logistic cho biến kết quả, |
| 13 | 10-03-validation-protocol.vi.md | 3 | 3.5 No empty words (lần kiểm tra một lần) | từ lần chốt thứ nhất đến lần kiểm tra một lần duy nhất trên các kỳ mở năm 2014. | từ lần chốt thứ nhất đến phép kiểm tra một lần duy nhất trên các kỳ mở năm 2014. |
| 14 | 10-03-validation-protocol.vi.md | 5 | 3.5 No empty words (lần kiểm tra một lần), caption | Giao thức kiểm định và kiểm tra, từ lần chốt thứ nhất đến lần kiểm tra một lần duy nhất | Giao thức kiểm định và kiểm tra, từ lần chốt thứ nhất đến phép kiểm tra một lần duy nhất |
| 15 | 10-03-validation-protocol.vi.md | 7 | 3.3 Glossary forms (never a bare kiểm thử) | Lần chốt thứ hai, trước khi kiểm thử, cố định | Lần chốt thứ hai, trước khi chạy trên tập kiểm thử, cố định |
| 16 | 10-03-validation-protocol.vi.md | 13 | 3.3 Glossary forms (population, Milestone 4 → phạm vi dữ liệu) | chốt các AQ, tổng thể, nhóm biến dự báo | chốt các AQ, phạm vi dữ liệu, nhóm biến dự báo |
| 17 | 10-03-validation-protocol.vi.md | 15 | 3.3 Glossary forms (fitted scaling / encoding) | Điền giá trị thiếu, chuẩn hóa thang đo và mã hóa được ước lượng lại trong từng fold | Phép điền giá trị thiếu, phép chuẩn hóa thang đo và phép mã hóa được ước lượng lại trong từng fold |
| 18 | 10-03-validation-protocol.vi.md | 16 | 3.6 Meaning complete (a gain in 7 of 9 folds) | và có mặt ở ít nhất 7 trên 9 fold. | và mức cải thiện xuất hiện ở ít nhất 7 trên 9 fold. |
| 19 | 10-03-validation-protocol.vi.md | 17 | 3.3 Glossary forms (never a bare kiểm thử) | Mô hình cuối cùng được chốt trước khi kiểm thử [26] | Mô hình cuối cùng được chốt trước khi chạy trên tập kiểm thử [26] |
| 20 | 10-03-validation-protocol.vi.md | 18 | 3.3 Glossary forms (kiểm định only for tests and the validation set) | kỳ mở diễn ra sau là một phép kiểm định theo thời gian [27] | kỳ mở diễn ra sau là một phép đánh giá theo thời gian (temporal validation) [27] |
| 21 | 10-03-validation-protocol.vi.md | 20 | 3.5 Head nouns present | \| 8. Lặp lại AQ2 \| | \| 8. Lặp lại phân tích AQ2 \| |
| 22 | 10-03-validation-protocol.vi.md | 22 | 3.3 One term per concept (module terms = số hạng, as in Table A.1) | các hệ số module được mã hóa thành độ lệch | các số hạng module được mã hóa thành độ lệch |
| 23 | 10-03-validation-protocol.vi.md | 22 | 3.3 Glossary forms (never a bare kiểm thử) | Phép kiểm thử chính dùng cách chia theo năm | Phép kiểm tra chính dùng cách chia theo năm |
| 24 | 10-03-validation-protocol.vi.md | 35 | 3.5 Head nouns present | có thể chứa, 9 kỳ mở huấn luyện \| | có thể chứa, tính trên 9 kỳ mở huấn luyện \| |
| 25 | 10-03-validation-protocol.vi.md | 46 | 3.3 Glossary forms (R² Nagelkerke) | độ lạc quan của Nagelkerke R² không quá 0,05 | độ lạc quan của R² Nagelkerke không quá 0,05 |
| 26 | 10-03-validation-protocol.vi.md | 46 | 3.3 Glossary forms (R² Nagelkerke) | là Nagelkerke R² dự kiến bằng 0,15 | là R² Nagelkerke dự kiến bằng 0,15 |
| 27 | 10-03-validation-protocol.vi.md | 46 | 3.1 Voice with intent; 3.2 linking (khả năng này ×3, no actor) | Khả năng áp dụng cho kỳ mở mới lại là vấn đề khác, vì khả năng này chỉ dựa trên 9 kỳ mở huấn luyện. Do đó, khả năng này được kiểm tra trực tiếp bằng cách chia dữ liệu theo kỳ mở thay vì suy ra từ cỡ mẫu; | Khả năng áp dụng mô hình cho một kỳ mở mới là vấn đề khác, vì bằng chứng cho khả năng này chỉ đến từ 9 kỳ mở huấn luyện. Do đó, nhóm tác giả kiểm tra khả năng áp dụng trực tiếp bằng cách chia dữ liệu theo kỳ mở thay vì suy ra từ cỡ mẫu; |
| 28 | 10-04-fairness-spec.vi.md | 3 | 3.5 No empty words (repeat the noun, not chúng) | không làm mô hình "mù" với chúng, vì | không làm mô hình "mù" với các thuộc tính đó, vì |
| 29 | 10-04-fairness-spec.vi.md | 13 | 3.5 Head nouns present | \| Dưới quy mô đủ điều kiện: chỉ báo cáo | \| Dưới quy mô tối thiểu để đủ điều kiện: chỉ báo cáo |
| 30 | 10-04-fairness-spec.vi.md | 15 | 3.5 Punctuation (colon before an explanation; 'là' read as copula) | chọn một tiêu chí chính là tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation), đo bằng | chọn một tiêu chí chính: tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation), đo bằng |
| 31 | 10-04-fairness-spec.vi.md | 23 | 3.6 Meaning complete (expected, not known in advance) | khi tỷ lệ nền khác nhau, độ chính xác khác nhau giữa các nhóm là điều đã biết trước [36] | khi tỷ lệ nền khác nhau, chênh lệch độ chính xác giữa các nhóm là điều có thể dự kiến [36] |
| 32 | 10-04-fairness-spec.vi.md | 28 | 3.6 Meaning complete (whether, a yes/no question) | Cho thấy mô hình có giá trị gì ngoài việc nhận ra sinh viên không hoạt động | Cho thấy mô hình có tạo thêm giá trị ngoài việc nhận ra sinh viên không hoạt động hay không |
| 33 | 10-04-fairness-spec.vi.md | 29 | 3.6 Meaning complete (whom it cannot reach) | loại không hoàn thành nào và không liên hệ kịp với ai | loại không hoàn thành nào và những sinh viên nào không còn liên hệ được |
| 34 | 10-04-fairness-spec.vi.md | 32 | 3.3 Glossary forms (declared disability; bias = thiên lệch) | Thứ hai, sai lệch đối với nhóm sinh viên khai báo khuyết tật, vốn chiếm tỷ lệ nhỏ trong dữ liệu, biến động thất thường. | Thứ hai, mức thiên lệch đối với nhóm có tình trạng khuyết tật do sinh viên tự khai, vốn chiếm tỷ lệ nhỏ trong dữ liệu, biến động thất thường. |
| 35 | 10-05-risk-register.vi.md | 13 | 3.5 Head nouns present | nhìn thấy dòng kiểm định hoặc dòng kiểm thử | nhìn thấy các dòng thuộc tập kiểm định hoặc tập kiểm thử |
| 36 | 10-05-risk-register.vi.md | 14 | 3.3 One term per concept (as in Table A.2) | \| Sai lệch do chọn lọc khi chọn mô hình \| | \| Thiên lệch do lựa chọn mô hình \| |
| 37 | 10-05-risk-register.vi.md | 14 | 3.5 Head nouns present | \| Tinh chỉnh lồng nhau; | \| Tinh chỉnh siêu tham số theo vòng lồng nhau; |
| 38 | 10-05-risk-register.vi.md | 15 | 3.3 Glossary forms (Vương quốc Anh (UK)) | đào tạo từ xa ở UK khác | đào tạo từ xa ở Vương quốc Anh (UK) khác |
| 39 | 10-05-risk-register.vi.md | 15 | 3.3 Glossary forms (never a bare kiểm thử; kiểm định only for tests) | \| Kiểm thử theo thời gian; xét riêng kỳ mở có cặp và kỳ mở không có cặp; kiểm định tại chỗ trước mọi lần sử dụng \| | \| Kiểm tra theo thời gian; xét riêng kỳ mở có cặp và kỳ mở không có cặp; đánh giá lại trên dữ liệu của trường trước mọi lần sử dụng \| |
| 40 | 10-05-risk-register.vi.md | 15 | 3.3 Glossary forms (a failed check: báo lỗi, not không đạt) | nếu không đạt kiểm tra hiệu chuẩn thì danh sách chỉ hiển thị thứ hạng | nếu phép kiểm tra hiệu chuẩn báo lỗi thì danh sách chỉ hiển thị thứ hạng |
| 41 | 10-05-risk-register.vi.md | 16 | 3.3 One term per concept (module terms = số hạng) | \| Biến module được mã hóa thành độ lệch; | \| Số hạng module được mã hóa thành độ lệch; |
| 42 | 10-05-risk-register.vi.md | 17 | 3.3 One term per concept (as in Appendix III) | kèm kiểm định đổi dấu; | kèm kiểm định hoán vị đổi dấu; |
| 43 | 10-05-risk-register.vi.md | 18 | 3.3 Glossary forms (never a bare kiểm thử) | \| Nhiều biến thể kiểm thử \| | \| Nhiều phương án phân tích trên tập kiểm thử \| |
| 44 | 10-05-risk-register.vi.md | 25 | 3.1 Complete (verb missing) | \| Nhãn bị đánh dấu theo sinh viên lâu dài \| | \| Nhãn bị đánh dấu đi theo sinh viên lâu dài \| |
| 45 | 10-05-risk-register.vi.md | 25 | 3.3 Glossary forms (flag, noun); 3.6 no added 'chỉ' | \| Việc đánh dấu chỉ dùng để đưa ra hỗ trợ và hết hiệu lực | \| Nhãn bị đánh dấu dẫn đến hoạt động hỗ trợ và hết hiệu lực |
| 46 | 10-06-ai-critiques.vi.md | 10 | 3.3 One term per concept (module terms = số hạng) | biến module mã hóa dưới dạng độ lệch, CCC được xét riêng | số hạng module mã hóa dưới dạng độ lệch, CCC được xét riêng |
| 47 | 10-06-ai-critiques.vi.md | 12 | 3.3 One term per concept (interaction terms = số hạng) | \| Biến tương tác dấu hiệu × module; | \| Số hạng tương tác dấu hiệu × module; |
| 48 | 10-06-ai-critiques.vi.md | 12 | 3.6 Meaning complete (fit = the 'fit to data' criterion, not model fitting) | nêu rõ mô hình được ước lượng trên 9 kỳ mở và 6 module; | nêu mức phù hợp với dữ liệu theo đúng 9 kỳ mở và 6 module; |
| 49 | 10-06-ai-critiques.vi.md | 18 | 3.5 Head nouns present | bỏ các thuộc tính là chưa đủ \| | chỉ bỏ các thuộc tính nhạy cảm ra khỏi mô hình là chưa đủ \| |
| 50 | 10-06-ai-critiques.vi.md | 19 | 3.1 Complete (critique read as the team's own assumption) | \| Giả định thứ tự nguy cơ trùng với nhu cầu hỗ trợ; | \| Thứ tự nguy cơ được mặc nhiên coi là trùng với nhu cầu hỗ trợ; |
| 51 | 10-06-ai-critiques.vi.md | 29 | 3.6 Meaning complete (no added 'phụ') | các chỉ số phụ chỉ biểu diễn lại cùng một số đếm | các chỉ số chỉ biểu diễn lại cùng một số đếm |
| 52 | 10-06-ai-critiques.vi.md | 30 | 3.3 Glossary forms (bootstrap hai tầng ghép cặp; số kỳ mở thắng, hòa và thua; one term for the sign-flip test) | Bootstrap hai tầng (mô hình và quy tắc được so sánh trên cùng mẫu lặp), có lập lại danh sách trong mỗi mẫu; kiểm định đổi dấu; số kỳ mở mà mô hình hơn, bằng và kém quy tắc | Bootstrap hai tầng ghép cặp (mô hình và quy tắc được so sánh trên cùng mẫu lấy lại), có lập lại danh sách trong mỗi mẫu lấy lại; kiểm định hoán vị đổi dấu; số kỳ mở thắng, hòa và thua |
| 53 | 10-06-ai-critiques.vi.md | 32 | 3.3 Glossary forms (population, Milestone 4 → phạm vi dữ liệu) | \| Chưa có tổng thể kiểm thử chính \| | \| Chưa xác định phạm vi dữ liệu kiểm thử chính \| |
| 54 | 10-06-ai-critiques.vi.md | 33 | 3.3 Glossary forms (a failed check: báo lỗi, not không đạt) | phương án xử lý khi hiệu chuẩn không đạt lại dùng tập kiểm thử lần thứ hai | phương án xử lý khi phép kiểm tra hiệu chuẩn báo lỗi lại dùng tập kiểm thử lần thứ hai |
| 55 | 10-06-ai-critiques.vi.md | 41 | 3.3 Glossary forms (fact → thông tin làm căn cứ) | đối chiếu từng nhận xét với các thông tin của thiết kế trước khi quyết định | đối chiếu từng nhận xét với các thông tin làm căn cứ của thiết kế trước khi quyết định |
| 56 | 10-06-ai-critiques.vi.md | 41 | 3.6 Meaning complete (giữ nguyên contradicts rút gọn) | Các prompt được giữ nguyên bằng tiếng Anh ở dạng rút gọn; | Các prompt được trình bày bằng tiếng Anh, ở dạng rút gọn; |
| 57 | 10-07-traceability-full.vi.md | 1 | 3.6 Orthography (Change Log is a named log: Nhật ký thay đổi) | ## Phụ lục VII – Truy vết đầy đủ và nhật ký thay đổi | ## Phụ lục VII – Truy vết đầy đủ và Nhật ký thay đổi |
| 58 | 10-07-traceability-full.vi.md | 9 | 3.1 Vietnamese order (head noun first) | tuần có bài bị bỏ lỡ đầu tiên theo kết quả \| | tuần đầu tiên có bài bị bỏ lỡ, theo từng loại kết quả \| |
| 59 | 10-07-traceability-full.vi.md | 10 | 3.3 Glossary forms (never a bare kiểm thử) | lặp lại trên năm 2014 sau khi kiểm thử AQ3 \| | lặp lại trên năm 2014 sau phép kiểm tra AQ3 \| |
| 60 | 10-07-traceability-full.vi.md | 21 | 3.3 Glossary forms (never a bare kiểm thử) | phép kiểm thử của AQ3 vẫn độc lập \| | phép kiểm tra AQ3 trên tập kiểm thử vẫn độc lập \| |
| 61 | 10-07-traceability-full.vi.md | 3 | 3.3 One term per concept (Validation column = Cách đánh giá, as in Table 8.1) | chỉ số chính, cách kiểm định và quyết định được hỗ trợ | chỉ số chính, cách đánh giá và quyết định được hỗ trợ |
| 62 | 10-07-traceability-full.vi.md | 7 | 3.3 One term per concept (Validation column = Cách đánh giá, as in Table 8.1) | \| Chỉ số chính \| Kiểm định \| Quyết định \| | \| Chỉ số chính \| Cách đánh giá \| Quyết định \| |

Closing lines (parity: `check_parity.py --report reports/milestone-4/report --lang vi <English file>`; status: `translation_status.py … --mark`):

- 09-references.vi.md: reviewed (heading and introduction read; entries identical to the English), 0 findings; parity 0 errors, 0 warnings; marked.
- 10-00-appendices.vi.md: reviewed, 0 findings (pointers I–VII match the English); parity 0 errors, 0 warnings; marked.
- 10-01-candidate-comparison.vi.md: reviewed, 10 findings fixed; parity 0 errors, 0 warnings; marked.
- 10-02-metric-definitions.vi.md: reviewed, 2 findings fixed; parity 0 errors, 0 warnings; marked.
- 10-03-validation-protocol.vi.md: reviewed, 15 findings fixed; parity 0 errors, 0 warnings; marked.
- 10-04-fairness-spec.vi.md: reviewed, 7 findings fixed; parity 0 errors, 0 warnings; marked.
- 10-05-risk-register.vi.md: reviewed, 11 findings fixed; parity 0 errors, 0 warnings; marked.
- 10-06-ai-critiques.vi.md: reviewed, 11 findings fixed; parity 0 errors, 23 warnings, all on lines 43–68 inside the two verbatim English prompts (kept in English by design); marked.
- 10-07-traceability-full.vi.md: reviewed, 6 findings fixed; parity 0 errors, 0 warnings; marked.

Terms for the glossary to settle:

1. "module terms" / "interaction terms" of a regression → "số hạng module" / "số hạng tương tác" (the twins used "biến module", "hệ số module", "biến tương tác" in turn).
2. "sign-flip permutation test" → "kiểm định hoán vị đổi dấu" (also appeared as "kiểm định đổi dấu").
3. "selection bias in model choice" → "thiên lệch do lựa chọn mô hình" (also appeared as "sai lệch do chọn lọc khi chọn mô hình").
4. "Validation" as a traceability column → "Cách đánh giá" (Table 8.1); "kiểm định" stays for the validation set and statistical tests.
5. "odds ratio": the report writes "tỉ số odds" throughout while every other ratio is "tỷ"; one spelling should be fixed report-wide ("tỷ số odds" suggested).
