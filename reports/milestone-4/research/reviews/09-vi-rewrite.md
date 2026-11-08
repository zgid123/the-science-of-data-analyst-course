# Vietnamese rewrite after reader test 1 – Milestone 4, 2026-11-08

Stage 5 (second part) of build-report reference.md section 4.3: every passage flagged by reader test 1 (103 flags, files 01-00 to 08-00, reader-test file `m4-reader-test-1.md` in the session scratchpad) was rewritten from the English source, checked against the English for meaning and numbers, and logged below. In the same pass the twins of the English files that changed after translation were brought in line (section "English changes"). Paths are relative to `reports/milestone-4/report/`; line numbers are those of the reader test (the twins before this pass).

Edits were applied by exact-match scripts (`rewrite-2026-11-08-scripts/apply.py` with one edit file per twin in `edits/`; each before-string must occur exactly once or the run aborts). The 03-03 paragraph rewrite, the 03-02 paragraph join, nine comma fixes and the appendix term alignments were made by short inline scripts with the same exact-match rule; `rewrite-2026-11-08-scripts/twins.diff` holds the full before/after diff of all 27 edited twins. The term decisions of the consistency pass (`consistency-2026-11-08.md`) were kept: one English gloss per document, "biến dự báo chính / bộ biến dự báo mở rộng", "dấu cảnh báo", "… của tập kiểm thử", "sai số chuẩn vững", "kỳ mở có cặp".

## Result

| Outcome | Count | Flags |
| :---- | :---- | :---- |
| Fixed | 97 | all others |
| Glossary term – decision for the native user (sentence reworded or the term defined in place; term itself unchanged) | 4 | 6, 12, 21, 65 |
| Rejected with reason | 2 | 82, 86 |

## Checks

| Command | Result |
| :---- | :---- |
| `check_parity.py --report reports/milestone-4/report --lang vi` | 0 errors, 24 warnings: 23 in the verbatim English prompts of 10-06, 1 loanword warning on the English term on the terms page (00-2:37). Nine comma-before-"và/hoặc" warnings introduced by the rewrite were fixed before the final run. |
| `check_abbreviations.py --report reports/milestone-4/report --lang vi` | 17 abbreviations, 0 violations (UK now defined in 05-00 Bảng 5.1, used bare in 05-01 and 10-05) |
| `translation_status.py --report reports/milestone-4/report --lang vi --mark <27 English paths>` | recorded 27 files |
| `translation_status.py --report reports/milestone-4/report --lang vi` | 34 sections, 0 need translation |
| `glossary.py --lang vi --task milestone-4 coverage --report reports/milestone-4/report` | 23 drifting; new ones caused by this pass are listed under "Glossary rows to settle" |

The console output with UTC timestamp and exit codes is in `rewrite-2026-11-08-scripts/checks.log`.

## English changes brought into the twins

| English file | Change in the English | Vietnamese now |
| :---- | :---- | :---- |
| 03-02 | AQ2 uses robust standard errors without clustering, because every run is observed rather than sampled | "Ở đây, mọi kỳ mở đều được quan sát đầy đủ chứ không phải được lấy mẫu, nên mô hình dùng sai số chuẩn vững và không tính sai số chuẩn theo cụm." |
| 03-02 | Partial effects explained: the gap linked to one sign with the others held equal, smaller than the sign's own gap, not the share it explains; both shown side by side | "Mỗi hiệu ứng riêng phần cho thấy chênh lệch gắn với một dấu hiệu khi các dấu hiệu khác được giữ như nhau. Chênh lệch này nhỏ hơn chênh lệch mà dấu hiệu đó cho thấy khi xét riêng; chênh lệch này cũng không phải là phần tình trạng không hoàn thành do dấu hiệu đó giải thích. Vì vậy, báo cáo trình bày hai loại chênh lệch cạnh nhau." |
| 03-03 | Module and start month enter as several terms each, 23 parameters in all | "Module và tháng bắt đầu đều đi vào mô hình dưới dạng nhiều số hạng, nên mô hình có tổng cộng 23 tham số." |
| 03-03 | Banked results defined | "kết quả bảo lưu, tức kết quả bài đánh giá được chuyển sang từ một kỳ mở trước của cùng module" |
| 03-03 | De-duplicated clicks described | "số lượt nhấp đếm lại sau khi mỗi bản ghi lặp lại hoàn toàn chỉ được tính một lần" (same wording in the AQ2 error-analysis cell of 04-01) |
| 04-00 | Discrimination measured on the ROC curve by ROC-AUC and on the precision–recall curve by PR-AUC | "Chỉ số thứ nhất được tính trên đường cong đặc trưng hoạt động của bộ thu (ROC), là diện tích dưới đường cong ROC (ROC-AUC). Chỉ số thứ hai được tính trên đường cong độ chính xác–tỷ lệ phát hiện, là diện tích dưới đường cong độ chính xác–tỷ lệ phát hiện (PR-AUC)." |
| 04-01 | Secondary metric: unweighted mean of the per-run differences between model and rule | "trung bình không trọng số của các chênh lệch giữa mô hình và quy tắc dấu hiệu sớm, tính theo từng kỳ mở" |
| 04-03 | Several gates or populations would let one pass by chance, so one gate and one population | "Ngoài ra, nếu mô hình được đánh giá theo nhiều điều kiện đạt hoặc trên nhiều phạm vi dữ liệu, một trong số đó có thể đạt chỉ do ngẫu nhiên. Vì vậy, thiết kế chỉ đặt một điều kiện đạt duy nhất trên một phạm vi dữ liệu duy nhất." |
| 05-00 / 05-01 | "United Kingdom (UK)" defined in Table 5.1, "UK" in 5.1 | Bảng 5.1: "tại Vương quốc Anh (UK)"; Mục 5.1: "tại UK" |
| 05-02 | Deferred: the choice of which contact to make and any ranking by expected benefit; the list itself (D1) is what AQ4 provides | "Vì vậy, việc chọn hình thức liên hệ và mọi cách xếp hạng theo lợi ích kỳ vọng của việc liên hệ vẫn được hoãn; AQ4 chỉ cung cấp danh sách cho biết nên liên hệ sinh viên nào trước (D1)." |

Note on the English sources: at the time of this pass, `04-01-evaluation-cards.md` still reads "unweighted mean of per-run differences" and `05-02-causal-fairness-use.md` still reads "The contact decision therefore stays deferred"; neither file was stale for `translation_status.py`. The Vietnamese follows the wording given in the task brief, which the English states elsewhere (01-01, 02-02, 04-03); the two English sentences should be updated to match.

## Flags

| # | File:line | Outcome | New wording (or reason) |
| :-- | :-- | :-- | :-- |
| 1 | 01-00:3 | Fixed | "Đề bài chia công việc thành hai mức, gọi là Level 1 và Level 2. Level 1 là bản Đề xuất mô hình hóa và đánh giá (Modeling and Evaluation Proposal) và là phần bắt buộc. … Level 2 là thí nghiệm với nguyên mẫu (prototype) và không bắt buộc"; "Level 1/2" stay English (glossary, brief's own terms) |
| 2 | 01-01:3 | Fixed | "Mục tiêu của tổ chức (Business Goal) là nâng tỷ lệ hoàn thành học phần …"; "Mục tiêu SMART (SMART Goal), tức mục tiêu cụ thể, …, chuyển mục tiêu này thành một mức cần đạt." |
| 3 | 01-01:3 | Fixed | "KPI phụ thứ nhất xét các sinh viên có dấu hiệu sớm của việc giảm tham gia học tập và đo tỷ lệ sinh viên trong nhóm này được liên hệ tính đến hết tuần 5. KPI phụ thứ hai xét các sinh viên có tên trong danh sách liên hệ và đo tỷ lệ sinh viên được liên hệ trong vòng bảy ngày." |
| 4 | 01-01:5 | Fixed | "Quyết định D1 xác định những sinh viên mà giảng viên kiêm cố vấn học tập và phòng hỗ trợ sinh viên sẽ liên hệ ở mỗi đợt lập danh sách. Đợt lập danh sách là thời điểm vào tuần 3 và tuần 5 …" |
| 5 | 01-01:5 | Fixed | "Quyết định D2 xác định cách Trưởng chương trình đào tạo phân bổ thời gian … Quyết định D3 xác định có mở rộng … hay không." |
| 6 | 01-01:7 | Glossary term – decision for the native user | Term "kỳ mở" kept; sentence reworded: "Mỗi lần một module được tổ chức là một kỳ mở module (module run); kỳ mở được đặt tên theo năm và tháng bắt đầu, với B là tháng 2 và J là tháng 10." |
| 7 | 01-01:7 | Fixed | "bỏ phép so sánh theo hình thức học (trực tuyến hoặc kết hợp) và theo năm học của sinh viên, thay bằng phép so sánh theo module và theo kỳ mở" |
| 8 | 01-01:9 | Fixed | "Bước này đối chiếu từng câu hỏi với dữ liệu thực. Nếu một phần của câu hỏi đã bị hoãn, phần đó chỉ được đưa trở lại khi có một thay đổi được ghi vào Nhật ký thay đổi [1]." |
| 9 | 01-01:18 | Fixed | "việc chọn hình thức liên hệ được hoãn đến đợt thí điểm (C11)"; the same phrase replaces "chọn cách liên hệ", "phần liên hệ" and "quyết định liên hệ" in 01-02, 02-01, 02-02, 05-02 and 08-00 |
| 10 | 01-01:20 | Fixed | "Chỉ số thứ nhất là tỷ lệ phát hiện: trong số sinh viên về sau không hoàn thành, bao nhiêu phần trăm có tên trong danh sách." |
| 11 | 01-01:20 | Fixed (term "mức vượt tỷ lệ nền" kept for the user) | "Chỉ số thứ hai so danh sách với tỷ lệ nền của kỳ mở, là tỷ lệ sinh viên không hoàn thành trong kỳ mở đó. Một danh sách chọn ngẫu nhiên cũng có tỷ lệ sinh viên không hoàn thành đúng bằng tỷ lệ nền, nên danh sách tốt phải vượt mức này; chỉ số thứ hai vì vậy gọi là mức vượt tỷ lệ nền (lift)." |
| 12 | 01-02:3 | Glossary term – decision for the native user | "lượt đăng ký học còn hiệu lực" kept and defined in place: "nghĩa là sinh viên chưa rút khỏi module vào ngày đó"; "hai bảng đặc trưng, tức hai bảng chứa biến dự báo cho mô hình"; sentence split in three |
| 13 | 01-02:3 | Fixed | "Nhờ đó, không lựa chọn nào trong bản đề xuất này chịu ảnh hưởng của các kết quả đó." |
| 14 | 01-02:13 | Fixed | "cả 22 phép kiểm tra tính hợp lệ đều đạt" |
| 15 | 01-02:17 | Fixed | "riêng việc chọn hình thức liên hệ của AQ4 vẫn được hoãn" |
| 16 | 01-02:17 | Fixed | "AQ2 được ước lượng trên các kỳ mở năm 2013 và chỉ được lặp lại trên các kỳ mở năm 2014 sau khi mô hình AQ3 đã qua lần kiểm tra duy nhất trên tập kiểm thử. Nhờ vậy, khi chọn mô hình dự báo, nhóm tác giả chưa thấy kết quả nào của tập kiểm thử." (same pattern in 03-02:11) |
| 17 | 02-00:3 | Fixed | "bốn bản mô tả AQ Modeling Brief, mỗi bản cho một câu hỏi" |
| 18 | 02-01:3 | Fixed | "thông tin được phép dùng làm đầu vào và khoảng thời gian được lấy thông tin đó" |
| 19 | 02-01:14 | Fixed | "Lượt đăng ký học, chỉ gồm các lượt còn hiệu lực tại ngày 14 (đây là nhóm tính KPI). Riêng khi xét bài bị bỏ lỡ đầu tiên, đơn vị phân tích là từng bài được chấm điểm" |
| 20 | 02-01:18 | Fixed | "Phải dùng đúng mẫu số (lượt đăng ký học còn hiệu lực tại ngày 14) và đúng lịch bài được chấm điểm của từng kỳ mở, vì lịch này khác nhau giữa các module." |
| 21 | 02-01:32 | Glossary term – decision for the native user | "tỉ số odds" kept with the glossary spelling "tỉ" (paired row "tỉ số nguy cơ"); the reader proposes "tỷ số chênh (OR)". Cell split: "…; tỉ số odds (odds ratio) được báo cáo bên cạnh. Ngoài ra, chiều của từng mối liên hệ được nêu cho từng module" |
| 22 | 02-01:46 | Fixed | "19 biến dự báo chính có thể dùng trong các bảng đặc trưng, … Biến điểm trung bình của bài đánh giá chấm bằng máy (CMA) bị loại, vì dưới 10% số dòng huấn luyện có giá trị này. Phương án thay thế là bộ biến dự báo mở rộng: thêm 10 biến dự báo khác, cộng với số lượt nhấp của từng tuần (2 biến tại ngày 13, 4 biến tại ngày 27)" |
| 23 | 02-01:65 | Fixed | "AQ4 chỉ bổ sung một quy tắc: giữ lại phần đầu của bảng xếp hạng, với số tên bằng mức mà hạn mức liên hệ cho phép." |
| 24 | 02-02:3 | Fixed | "AQ2 vẫn thuộc loại phân tích chẩn đoán, với bài toán kỹ thuật là đo mối liên hệ." |
| 25 | 02-02:6 | Fixed | "Cụ thể, AQ2 xét các sinh viên có một dấu hiệu tính đến ngày 27 và đo xem tỷ lệ không hoàn thành ở nhóm này cao hơn bao nhiêu so với sinh viên tương đương …"; 03-02:7: "AQ2 hỏi: so với sinh viên tương đương không có dấu hiệu, sinh viên có một dấu hiệu tính đến hết ngày 27 có tỷ lệ không hoàn thành cao hơn bao nhiêu?" |
| 26 | 02-02:10 | Fixed | "khi chọn sinh viên được ưu tiên nhận nguồn hỗ trợ khan hiếm, các nghiên cứu đánh giá phần đầu danh sách, vì quyết định được đưa ra ở phần này [7]" |
| 27 | 02-02:10 | Fixed | "Hơn nữa, biến mục tiêu gộp Withdrawn với Fail, mà kết quả Fail chỉ được xác định khi kỳ mở kết thúc. Vì hai điểm này, phân tích sống sót chỉ là phần mở rộng." (same order in 03-03:9) |
| 28 | 03-00:3 | Fixed | "hai hoặc ba nhóm phương pháp ứng viên"; "làm lập luận cho lựa chọn" |
| 29 | 03-01:5 | Fixed | Lead "Các kết luận giúp chọn giữa hai ứng viên ngang nhau."; "nhóm tác giả dựa vào bốn kết luận …; trong phần lớn trường hợp, các kết luận này đủ để chọn được một ứng viên" |
| 30 | 03-01:13 | Fixed | "tỷ lệ tính lại theo mẫu số thứ hai (mọi lượt đăng ký học, không chỉ các lượt còn hiệu lực tại ngày 14)" |
| 31 | 03-01:14 | Fixed | "Mọi kỳ mở của các module đều có trong dữ liệu, nên hiệu ứng cố định là phù hợp" |
| 32 | 03-01:15 | Fixed | "số sự kiện trên mỗi tham số cao (mỗi sự kiện là một sinh viên không hoàn thành)" (glossary term kept, defined) |
| 33 | 03-01:16 | Fixed | "Chia sinh viên thành các nhóm mức nguy cơ, với ranh giới nhóm đặt theo hạn mức liên hệ"; "Ứng viên 1, kèm lý do cho từng sinh viên trong danh sách"; column header and intro "lập luận tóm tắt" (rationale), "lý do" kept only for reasons shown to tutors |
| 34 | 03-02:5 | Fixed | "Phép so sánh hai mẫu số cho thấy những tỷ lệ nào phụ thuộc vào cách xác định phạm vi dữ liệu. Cách xác định phạm vi dữ liệu chính là nguồn chủ yếu khiến một tỷ lệ mô tả có thể gây hiểu sai." |
| 35 | 03-02:9 | Fixed | Heading "AQ2: lập luận cho mô hình này."; decision stated (English change): "… nên mô hình dùng sai số chuẩn vững và không tính sai số chuẩn theo cụm." |
| 36 | 03-02:9 | Fixed | "Khi biến kết quả phổ biến, tỉ số odds cho thấy hiệu ứng lớn hơn so với tỉ số nguy cơ; trong dữ liệu này, 44–46% sinh viên không hoàn thành, nên cần lưu ý điều đó. Bên cạnh đó, giá trị p …" (two ideas in two sentences; "cho thấy hiệu ứng lớn hơn" speaks of magnitude, so it holds for odds ratios below 1) |
| 37 | 03-02:9 | Fixed | English change: "ước lượng của mỗi dấu hiệu đã được hiệu chỉnh theo các dấu hiệu còn lại. Các ước lượng đã hiệu chỉnh lẫn nhau này gọi là hiệu ứng riêng phần. Mỗi hiệu ứng riêng phần cho thấy chênh lệch gắn với một dấu hiệu khi các dấu hiệu khác được giữ như nhau. …" |
| 38 | 03-02:9 | Fixed | "Mô hình cũng đáp ứng các tiêu chí còn lại trong tám tiêu chí của Mục 3.1. Về giả định, mô hình coi phần đóng góp của các dấu hiệu trong một module là cộng được với nhau trên thang log-odds; … Về mức phù hợp với dữ liệu, … Về tính bền vững, …" |
| 39 | 03-02:11 | Fixed | "Phụ lục I (Bảng A.1) đối chiếu chi tiết các phương pháp ứng viên cho AQ2 với tám tiêu chí." (same in 03-03, 03-04) |
| 40 | 03-03:7 | Fixed | English change: "Module và tháng bắt đầu đều đi vào mô hình dưới dạng nhiều số hạng, nên mô hình có tổng cộng 23 tham số." |
| 41 | 03-03:7 | Fixed | English change: "kết quả bảo lưu, tức kết quả bài đánh giá được chuyển sang từ một kỳ mở trước của cùng module" |
| 42 | 03-03:7 | Fixed | English change: "số lượt nhấp đếm lại sau khi mỗi bản ghi lặp lại hoàn toàn chỉ được tính một lần" |
| 43 | 03-03:7 | Fixed | "Với các giả định mặc định, tiêu chí cỡ mẫu tối thiểu của Riley và cộng sự đòi hỏi 1.731 lượt đăng ký học huấn luyện; con số 11.811 lượt tại ngày 27 gấp khoảng bảy lần mức này [14]." |
| 44 | 03-03:7 | Fixed | "… thay vì xây cho mỗi module một mô hình riêng. Mỗi mô hình riêng như vậy chỉ có cỡ mẫu nhỏ, trong khi phép co hệ số (shrinkage) không bù được cho cỡ mẫu nhỏ [17]." |
| 45 | 03-03:7 | Fixed | Block split into three paragraphs at its English lead sentences: approach and predictor groups (one sentence per group); "Lập luận cho lựa chọn này xuất phát từ chính dự án." with "Thứ nhất / Thứ hai / Thứ ba"; "Rủi ro cần kiểm tra là khả năng áp dụng mô hình cho kỳ mở diễn ra sau." The English keeps one paragraph; the split is the only paragraph-level difference from the English and was requested for this block |
| 46 | 03-03:9 | Fixed | "nghiên cứu so sánh (benchmark) cho kết quả này đã loại những bộ dữ liệu mà ở đó hồi quy logistic chỉ kém mô hình tốt nhất không quá 5%. Vì vậy, nghiên cứu đó không chứng minh rằng cây vượt hồi quy logistic [19]." |
| 47 | 03-03:9 | Fixed | "Hiệu chỉnh phạt chỉ cải thiện hiệu chuẩn ở mức trung bình, không chắc chắn trong từng trường hợp cụ thể [17]" |
| 48 | 03-04:3 | Fixed | "Các tiêu chí còn lại của Mục 3.1 được xét như sau. … Danh sách dựa trên một giả định chưa được kiểm chứng: sinh viên có nguy cơ cao hơn cũng là sinh viên cần hỗ trợ hơn, tức thứ tự theo nguy cơ trùng với thứ tự theo mức cần hỗ trợ." |
| 49 | 03-04:7 | Fixed | "Lập luận thứ nhất là để ước lượng mức tác động của một can thiệp thay đổi thế nào giữa các cá nhân, cần dữ liệu về can thiệp được phân bổ ngẫu nhiên hoặc dữ liệu mà yếu tố gây nhiễu không làm sai lệch ước lượng [9]." |
| 50 | 04-00:3 | Fixed | "Chuẩn này chia việc đánh giá thành ba khía cạnh; mỗi chỉ số đo phải được nêu kèm lập luận cho lựa chọn [21]." |
| 51 | 04-00:3 | Fixed | English change: two indices on two curves (see "English changes") |
| 52 | 04-01:5 | Fixed | "Thiết lập chính của báo cáo là danh sách 5 trên 20 tại ngày 27. Thiết lập này được chọn vì danh sách tương ứng được giao cho giảng viên hướng dẫn vào tuần 5, đồng thời tỷ lệ 25% của danh sách gần với tỷ lệ sinh viên bị quy tắc dấu hiệu sớm đánh dấu tại ngày 27." ("thiết lập chính" is the glossary form of "operating point"; listed for the user below) |
| 53 | 04-01:5 | Fixed | "Báo cáo dùng ba chỉ số này thay vì điểm F1, vì độ dài danh sách do hạn mức liên hệ quyết định chứ không được chọn để cân bằng hai loại lỗi." |
| 54 | 04-01:16 | Fixed | "138 lượt đăng ký học có cờ chất lượng dữ liệu do thiếu ngày rút khỏi module hoặc ngày đăng ký" ("cờ" only for data-quality flags, as the glossary row says; same in the AQ2 error-analysis cell) |
| 55 | 04-01:17 | Fixed | "Các kỳ mở mà tỷ lệ tính theo hai mẫu số chênh nhau nhiều hơn độ rộng khoảng tin cậy của tỷ lệ" |
| 56 | 04-01:29 | Fixed | "chỉ sau khi mô hình AQ3 đã được chốt và đã tính điểm rủi ro cho các kỳ mở năm 2014" |
| 57 | 04-01:31 | Fixed | Three sentences; "Phân tích độ nhạy theo bốn cách: dùng số lượt nhấp đếm lại …; dùng phiên bản quy tắc dấu hiệu sớm có tính thêm CMA nộp trễ; bỏ 138 lượt đăng ký học có cờ chất lượng dữ liệu; và bỏ các kỳ mở không có bài đến hạn" |
| 58 | 04-01:32 | Fixed | "chỉ được mô tả. Mô hình không hiệu chỉnh theo các thuộc tính này, để khác biệt giữa các nhóm không bị che đi" |
| 59 | 04-01:33 | Fixed | "ở ít nhất hai phần ba số module tính được dấu hiệu đó" |
| 60 | 04-01:41 | Fixed | "Mỗi kỳ mở dùng danh sách riêng của kỳ mở đó. Kết quả gộp bằng tổng số sinh viên không hoàn thành có tên trong các danh sách, chia cho tổng mức tối đa mà các danh sách đó có thể đạt" (the formula of Bảng A.4) |
| 61 | 04-01:42 | Fixed | "trung bình không trọng số của các chênh lệch giữa mô hình và quy tắc dấu hiệu sớm, tính theo từng kỳ mở" |
| 62 | 04-01:42 | Fixed | "lợi ích ròng (net benefit), chỉ dùng làm bối cảnh, vì chỉ số này mô tả chính sách liên hệ mọi sinh viên có nguy cơ vượt một ngưỡng, chứ không mô tả danh sách có độ dài cố định theo hạn mức liên hệ [25]" |
| 63 | 04-01:43 | Fixed | "sau lần chốt thứ hai, tức lần chốt mô hình cuối cùng, mô hình tính điểm rủi ro cho 13 kỳ mở năm 2014 đúng một lần và lần chạy này được ghi nhật ký" |
| 64 | 04-01:45 | Fixed | "tỷ lệ phát hiện chỉ tính trên những sinh viên không hoàn thành mà cán bộ còn kịp liên hệ, tức sinh viên chưa rút khỏi module trong vòng 7 ngày sau thời điểm chốt dữ liệu" |
| 65 | 04-01:46 | Glossary term – decision for the native user | "kiểm định khẳng định" and "tỷ lệ phát hiện trong giới hạn danh sách" kept; defined at first use: "Kiểm định khẳng định, tức kiểm định chính thức trên các nhóm đã ấn định trước, về tỷ lệ phát hiện trong giới hạn danh sách của từng nhóm" |
| 66 | 04-01:47 | Fixed | "S1 gồm ba yêu cầu. Thứ nhất, … Thứ hai, khoảng tin cậy 95% của chênh lệch giữa hai tỷ lệ này phải nằm trên 0. Khoảng tin cậy được tính bằng bootstrap hai tầng (lấy mẫu lại kỳ mở, rồi lượt đăng ký học trong từng kỳ mở), trong đó mô hình và quy tắc được so trên cùng một mẫu lấy lại. Thứ ba, …" ("điều kiện đạt" kept) |
| 67 | 04-01:47 | Fixed | "cả hai đều xét trên giá trị ước lượng của dữ liệu gộp mọi kỳ mở" (same in 04-03 Bảng 4.5, S3) |
| 68 | 04-01:59 | Fixed | "Các kỳ mở mà các vị trí trong danh sách bị dùng cho những sinh viên về sau vẫn hoàn thành. Ngoài ra, nhóm sinh viên hoàn toàn không có hoạt động, vốn danh sách nào cũng đưa vào, được tách khỏi …" |
| 69 | 04-01:61 | Fixed | "kiểm định khẳng định về công bằng ở Mục 4.4 phải đạt; nếu kiểm định này nêu tên nhóm nào, nhóm đó phải được xem xét trước khi đưa danh sách vào sử dụng" |
| 70 | 04-02:3 | Fixed | "Kiểm tra trên các kỳ mở mà mô hình chưa thấy." |
| 71 | 04-02:6 | Fixed | "Nếu một sinh viên có mặt cả trong kỳ mở được tách ra để đánh giá, sinh viên đó bị loại khỏi dữ liệu huấn luyện của fold đó" |
| 72 | 04-02:6 | Fixed | "Lập luận thứ hai là chính tiêu chí dùng để chọn mô hình cũng có thể bị quá khớp, tức khớp cả nhiễu của dữ liệu dùng để chọn; khi đó, sai lệch sinh ra …" |
| 73 | 04-02:12 | Fixed | "… độ lệch so với module trung bình (deviation coding). Nhờ cách mã hóa này, một module không có trong dữ liệu huấn luyện nhận mức của module trung bình." |
| 74 | 04-02:16 | Fixed | "Điều kiện đạt S1 xét chênh lệch giữa mô hình và quy tắc; độ bất định của chênh lệch này được ước lượng bằng bootstrap hai tầng." |
| 75 | 04-02:16 | Fixed | "Kiểm định này giả sử dấu của chênh lệch ở từng kỳ mở chỉ là ngẫu nhiên. Với giả sử đó, kiểm định tính xem các chênh lệch có lợi cho mô hình ở mức bằng hoặc hơn mức quan sát được sẽ xuất hiện thường xuyên đến đâu." |
| 76 | 04-02:18 | Fixed | "Tiêu chí thứ hai là mức lạc quan của R² Nagelkerke không quá 0,05. Mức lạc quan là phần R² trên dữ liệu phát triển cao hơn R² trên dữ liệu mới, …" |
| 77 | 04-03:7 | Fixed | "Để tính con số này, nhóm tác giả ước lượng một mô hình hiệu chuẩn lại (recalibration model) với độ dốc được giữ cố định, rồi lấy hệ số chặn của mô hình đó." |
| 78 | 04-03:11 | Fixed | English change: missing step added (see "English changes") |
| 79 | 04-03:20 | Fixed | "Trong ba nhóm của kiểm định khẳng định, không có nhóm nào thỏa đồng thời hai điều kiện sau. Điều kiện thứ nhất: tỷ lệ phát hiện trong giới hạn danh sách của nhóm thấp hơn tỷ lệ này ở các sinh viên còn lại quá 10 điểm phần trăm. Điều kiện thứ hai: … Nhóm thỏa cả hai điều kiện được nêu tên để xem xét lại" |
| 80 | 04-03:22 | Fixed | "còn giới hạn độ dốc từ 0,8 đến 1,2 cho phép độ phân tán của nguy cơ dự báo rộng quá hoặc hẹp quá 20%" |
| 81 | 04-04:5 | Fixed | "Cụ thể, nếu điểm rủi ro có giá trị dự báo dương ngang nhau giữa các nhóm thì điểm đó không thể đồng thời có tỷ lệ lỗi ngang nhau [36]. Tương tự, hiệu chuẩn trong từng nhóm và tỷ lệ lỗi cân bằng giữa các nhóm mâu thuẫn với nhau, trừ các trường hợp suy biến [37]." |
| 82 | 04-04:5 | Rejected | The English report itself defines separation for this audit as "equal recall at capacity across groups" (04-04), and the glossary row names the criterion after that definition; the Vietnamese name follows the report, not the general textbook definition |
| 83 | 04-04:7 | Fixed | "Với khoảng 100 sinh viên không hoàn thành trong một nhóm và tỷ lệ phát hiện ở mức khoảng 0,5, sai số chuẩn của tỷ lệ phát hiện của nhóm là khoảng 5 điểm phần trăm. Số sinh viên còn lại lớn hơn nhóm nhiều lần, nên sai số chuẩn này là nguồn bất định chính của chênh lệch. Do đó, chênh lệch 10 điểm trong quy tắc FR1 tương đương khoảng hai lần sai số chuẩn …" |
| 84 | 04-04:9 | Fixed | "… thiên lệch đối với sinh viên tự khai có khuyết tật biến động thất thường … [38]. Vì kết quả ở các nhóm ít sinh viên có thể dao động thất thường như vậy, báo cáo này gộp các nhóm nhỏ qua các kỳ mở và báo cáo kèm khoảng tin cậy." Also "Quy tắc FR1 … nêu tên một nhóm để xem xét lại" |
| 85 | 04-04:9 | Fixed | One name "biến thay thế" (settled glossary): 05-01 "biến đại diện của biến kết quả" → "biến thay thế cho biến kết quả" |
| 86 | 05-00:3 | Rejected | The reader marked it fine because the sentence explains each NIST function; "lập bản đồ" is the glossary row for "map" |
| 87 | 05-00:13 | Fixed | "hiệu ứng riêng phần của một dấu hiệu (chênh lệch khi giữ các dấu hiệu khác như nhau) bị hiểu nhầm là phần đóng góp riêng của dấu hiệu đó"; "mô hình tính điểm rủi ro" |
| 88 | 05-01:3 | Fixed | "Dạng thứ nhất là … Dạng thứ hai là biến dự báo thực chất chỉ là biến thay thế cho biến kết quả. Dạng thứ ba là rò rỉ theo thời gian (thông tin của thời điểm sau lọt vào dữ liệu huấn luyện) hoặc sự phụ thuộc giữa mẫu huấn luyện và mẫu kiểm thử [22]." |
| 89 | 05-01:7 | Fixed | "Nhiều mô hình khác nhau, với các hệ số khác nhau, có thể mô tả dữ liệu tốt gần như ngang nhau [5]. Do hệ số của một mô hình chỉ là một trong nhiều cách mô tả dữ liệu tốt như nhau, báo cáo không diễn giải hệ số nào thành nguyên nhân." |
| 90 | 05-02:3 | Fixed | "mức nguy cơ và lợi ích nhận được từ can thiệp có thể không đi cùng nhau: người có nguy cơ cao nhất chưa chắc được lợi nhiều nhất" |
| 91 | 05-02:3 | Fixed | English change: "việc chọn hình thức liên hệ và mọi cách xếp hạng theo lợi ích kỳ vọng của việc liên hệ vẫn được hoãn; AQ4 chỉ cung cấp danh sách cho biết nên liên hệ sinh viên nào trước (D1)" (see the note on the English file above) |
| 92 | 05-02:3 | Fixed | "Bước tiếp theo là một đợt thí điểm ngẫu nhiên hóa. Thời điểm gốc (time zero) của đợt thí điểm, tức mốc bắt đầu theo dõi chung cho mọi sinh viên, là thời điểm chốt dữ liệu, …" |
| 93 | 05-02:5 | Fixed | "Đối với từng sinh viên trong danh sách, dấu cảnh báo chỉ dẫn đến hoạt động hỗ trợ và hết hiệu lực khi kỳ mở kết thúc. Quy định này bảo đảm …" |
| 94 | 06-00:3 | Fixed | "trong những vai trò mà đề bài cho phép khi AI hỗ trợ việc mô hình hóa"; "các nhóm phương pháp ứng viên" |
| 95 | 06-00:12 | Fixed | "bootstrap hai tầng (hierarchical bootstrap)"; one name "bootstrap hai tầng" also in 04-02, 04-03, 10-03, 10-05, 10-06 (pairing described in words where it matters) |
| 96 | 06-00:13 | Fixed | "Thử nghiệm mục tiêu (target trial, tức thực nghiệm ngẫu nhiên hóa mà dữ liệu quan sát cố gắng mô phỏng) và xếp hạng theo lợi ích can thiệp đều cần dữ liệu về can thiệp" |
| 97 | 06-00:14 | Fixed | "đối chiếu với các dữ kiện của thiết kế đánh giá và với độ dài các kỳ mở" |
| 98 | 06-00:19 | Fixed | "mọi số đếm phải lấy từ 6 module của các kỳ mở huấn luyện, để không dùng đến dữ liệu của tập kiểm thử" (the reason 04-02 gives for counting outcomes on the 2013 runs only) |
| 99 | 06-00:19 | Fixed | "Phép tính này cho thấy một điều: giả sử tiêu chí thành công chỉ đòi hỏi mô hình vượt quy tắc dấu hiệu sớm ở ít nhất 9 trên 13 kỳ mở của tập kiểm thử, thì tiêu chí đó vẫn được đáp ứng chỉ do ngẫu nhiên trong khoảng 13% trường hợp." |
| 100 | 07-00:20 | Fixed | "Nếu phương pháp cơ sở đạt kết quả ngang bằng phương pháp ứng viên, kết quả đó vẫn được chấp nhận." |
| 101 | 08-00:3 | Fixed | "cùng các ma trận sẵn sàng cho mô hình được lập từ hai bảng này, tức ma trận đầu vào có thể đưa thẳng vào mô hình" |
| 102 | 08-00:11 | Fixed | "Kiểm định chéo loại trừ từng kỳ mở trên các kỳ mở năm 2013" |
| 103 | 08-00:12 | Fixed | "D1; việc chọn hình thức liên hệ được hoãn" |

## Term alignments made in the same pass

- Rationale for a choice → "lập luận" (01-00, 01-01 Change Log, 02-02, 03-00, 03-01 header, 03-02 heading, 03-03, 03-04, 04-00, 04-02, 06-00, 07-00); "lý do" now appears in the main text only for the reasons shown to tutors with each student.
- A model scoring runs → "tính điểm rủi ro" in 04-01, 04-02, 05-00 and 06-00 ("lần kiểm tra … trên tập kiểm thử" in 01-02, 03-02, 05-01 and 08-00, where the English means the single test) and, for consistency, 00-2 (row 23), 10-03, 10-05 (two rows), 10-06 and 10-07; "chấm điểm" remains only for marked assignments ("bài được chấm điểm").
- Data-quality flags → "cờ chất lượng dữ liệu"; groups named by FR1 → "nêu tên … để xem xét lại" (04-01, 04-03, 04-04), so "đánh dấu" stays for students on the list.

## Glossary rows to settle (no glossary file was edited)

- `topics/early-warning-evaluation.md`, "contact deferred (AQ4) → phần liên hệ được hoãn": the reader could not tell what "phần liên hệ" meant (#15, #91, #103); the twins now say "việc chọn hình thức liên hệ được hoãn". Suggest changing the row and adding the old form to Replaces.
- "paired two-level bootstrap → bootstrap hai tầng ghép cặp" and "hierarchical (two-level) bootstrap → bootstrap phân tầng": the twins now use the single name "bootstrap hai tầng", with the pairing stated in words; coverage reports the paired row at 0%.
- "proxy variable → biến đại diện": the one remaining use (05-01) now reads "biến thay thế", the settled form for proxy.
- "single test (on the 2014 runs)" Usage still quotes "chấm điểm các kỳ mở năm 2014 đúng một lần", which the newer "score → tính điểm rủi ro" row overrides.
- "exact duplicate row; de-duplicated twin → bản đối chiếu đã loại trùng" (Milestone 4 tables): the English now describes the twin in words, and the twins follow the English.

## Decisions for the native user

The reader judged these terms invented or unnatural; they were kept as the glossary requires and the sentences around them reworded or the term defined in place:

| Term | Reader's count | Reader's proposal |
| :---- | :---- | :---- |
| kỳ mở (module run) | 191 | lớp học phần / đợt học / khóa học phần |
| lượt đăng ký học | 48 | lượt ghi danh; or "sinh viên" where the unit is obvious |
| còn hiệu lực | 11 | còn đang theo học |
| tỷ lệ phát hiện trong giới hạn danh sách | 4 | recall tại k |
| tỷ lệ phát hiện chuẩn hóa | 9 | recall chuẩn hóa |
| mức vượt tỷ lệ nền (lift) | 6 | hệ số nâng (lift) / lift |
| độ chính xác của danh sách | 11 | precision tại k |
| kiểm định khẳng định | 7 | kiểm định xác nhận (chính thức) |
| điều kiện đạt | 12 | tiêu chí đạt / ngưỡng đạt |
| tỉ số odds | 5 | tỷ số chênh (OR) |

Two further glossary forms the reader questioned are not on that list and were also kept: "thiết lập chính" (operating point; reader: cấu hình chính / kịch bản chính) and "hạn mức liên hệ" (capacity; reader: năng lực liên hệ).

## Left open

- The English `04-01-evaluation-cards.md` (secondary metric) and `05-02-causal-fairness-use.md` (what stays deferred) do not yet contain the wording the twins now carry; update the English or confirm the twins.
- 03-03 has three paragraphs where the English "Primary approach" paragraph has one (flag #45).
- A second reader test on the rewritten twins (reference.md section 4.3, stage 5) has not been run.
