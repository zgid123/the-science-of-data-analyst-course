# Reader test – Vietnamese Milestone 4 report (stage 5, reference.md section 4.3)

Reader: a lecturer in data analytics at a Vietnamese university who reads Vietnamese natively. Read cold, in
file-name order: `00-1`, `00-2`, `01-*` to `08-*`, `10-*` (`*.vi.md` only; English prompt lines starting with `>` in
`10-07` skipped; evidence codes and citations ignored). No English source file and no other research file was opened.

**Overall judgement.** A reader of the field can explain the document afterwards at the level of its skeleton: four
questions (AQ1–AQ4), a descriptive and a diagnostic question answered without machine learning, a penalised logistic
regression that must beat the early-sign rule on the 2014 runs, tested once, with a ranked contact list of fixed
length, a fairness check on three groups, and a deferred contact decision pending a randomised pilot. Chapters 1, 2,
5, 6, 7 and 8 read well. The reader cannot, however, explain the success criteria and the evaluation details with
confidence. Sections 4.3–4.4 and Appendices III–V pack several conditions into one sentence or table cell, and they
rest on coined terms that are never said in plain words ("số sinh viên cán bộ liên hệ được", "tỷ lệ phát hiện chuẩn
hóa trong giới hạn danh sách", "kiểm tra xác nhận", "phương án chỉ dùng kết quả đã biết"). Two terms are never defined
anywhere the reader can see ("mẫu số thứ hai", "lượt mở ghép cặp"). One number in the main text contradicts
the reader's model until the appendix explains it (03-03:5). The prose is grammatical and mostly natural, but a
large share of sentences keep English clause order (long subject, verb at the end; "X so với Y mô tả Z") and read as
translated. The glossary resolves several invented terms, but only for a reader who stops to look them up.

Clarity: 1 = I could not work out the meaning; 2 = I understood after rereading; 3 = I understood but it sounds translated.

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 01-01:3 | "Business Goal (mục tiêu của tổ chức) là nâng tỷ lệ…" | English label opens a Vietnamese sentence; the same holds for "SMART Goal" | 3 |
| 2 | 01-01:3 | "nâng tỷ lệ hoàn thành học phần của sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần từ mức cơ sở giả định 70% lên 75%" | Long noun chain; "từ… lên…" sits far from "nâng", so I had to find what rises from 70% | 2 |
| 3 | 01-01:5 | "chỉ những câu hỏi phân tích (AQ) còn hiệu lực sau bước đánh giá mức phù hợp giữa AQ và dữ liệu" | Heavy noun phrase; "đánh giá mức phù hợp giữa AQ và dữ liệu" is a calque of "AQ–data fit assessment" | 3 |
| 4 | 01-01:12 | "D2, lý do kèm các tên trong danh sách D1" | Fragment: what is "lý do kèm các tên"? Guessed: AQ2 supplies the reasons shown next to each name | 2 |
| 5 | 01-01:14 | "Lượt đăng ký học nào được xếp đầu với số sinh viên cán bộ liên hệ được theo giả định" | First parse: "officials who can be contacted". Only the glossary shows it means contact capacity | 2 |
| 6 | 01-01:14 | "danh sách đạt mức vượt tỷ lệ nền của lượt mở và tỷ lệ phát hiện (recall) bao nhiêu" | "mức vượt tỷ lệ nền" is a coined term for lift; I guessed it from the later "(lift)" | 2 |
| 7 | 01-01:14 | "từng mức khó khăn của khu vực" | Vague; I only learn in 10-01 that it is a socio-economic deprivation index of the home area | 3 |
| 8 | 01-02:13 | "các phép biến đổi được ước lượng trên năm 2013" | "estimated on 2013" calque; Vietnamese would say "học/ước lượng từ dữ liệu năm 2013" | 3 |
| 9 | 01-02:14 | "Các vấn đề chất lượng DQ01–DQ19" | Codes without words; the reader has no idea what the 19 issues are | 3 |
| 10 | 02-00:3 | "mỗi câu hỏi trước hết được mô tả theo những gì câu hỏi đó cần" | Passive, abstract; sounds translated | 3 |
| 11 | 02-00:3 | "các AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa của từng AQ)" | English title used as a Vietnamese noun throughout (8 times) | 3 |
| 12 | 02-01:9 | "(tổng thể của KPI)" | "tổng thể" = population, but "tổng thể của KPI" first read as "the KPI overall" | 2 |
| 13 | 02-01:11 | "bộ biến mở rộng và số lượt nhấp theo tuần là phương án thay thế" | "bộ biến mở rộng" used before it is introduced (03-03) | 2 |
| 14 | 02-01:12 | "nguy cơ cao không đồng nghĩa với lợi ích khi được liên hệ" | Understood; phrasing translated | 3 |
| 15 | 02-01:14 | "Hệ thống cảnh báo sớm của chính OU cũng cung cấp hằng tuần cho giảng viên hướng dẫn một danh sách sinh viên có nguy cơ" | English word order (verb–time–recipient–object) | 3 |
| 16 | 02-02:3 | "Mô hình hóa giải thích kiểm định các giả thuyết nhân quả, mô hình hóa dự báo đưa ra dự báo…; còn mô hình hồi quy chỉ dùng để đo mối liên hệ, không nhằm…, là mô hình mô tả theo cách hiểu của Shmueli" | "giải thích kiểm định" reads as a compound noun; three ideas in one sentence, main verb "là" at the very end | 2 |
| 17 | 02-02:3 | "Đề bài xếp loại phân tích này vào câu hỏi chẩn đoán" | "loại phân tích này" points back to a clause, not a noun; unclear reference | 2 |
| 18 | 02-02:7 | "khi dự báo được dùng để xếp hạng, chất lượng của thứ hạng cuối cùng quan trọng hơn giá trị dự báo" | "thứ hạng cuối cùng" (final rank) vs "giá trị dự báo" (predicted value) – had to reread to see the contrast | 2 |
| 19 | 02-02:7 | "Mô hình sống sót thời gian rời rạc" | Vietnamese statistics usually says "mô hình sống còn" / "phân tích sống còn" | 3 |
| 20 | 02-02:7 | "Xếp hạng theo lợi ích can thiệp (uplift), tức là theo lợi ích kỳ vọng khi liên hệ sinh viên" | Understood; "lợi ích can thiệp" is a coinage | 3 |
| 21 | 03-00:3 | "Candidate Solution Matrix (ma trận các giải pháp ứng viên)" | English heading/term kept | 3 |
| 22 | 03-01:3 | "Bốn kết luận về các hệ thống dự báo giúp phân định phần lớn các trường hợp hai ứng viên ngang nhau." | Whose conclusions? "phân định" for "break ties" is unexpected; only the next sentences explain it | 2 |
| 23 | 03-01:11 | "Tỷ lệ gộp chung; mẫu số thứ hai" | "mẫu số thứ hai" is never defined in the main text; I could not tell which second denominator | 1 |
| 24 | 03-01:12 | "Quan sát được mọi lượt mở của các module" | Reason cell without subject; I guessed it justifies fixed effects | 2 |
| 25 | 03-01:13 | "Hồi quy logistic có hiệu chỉnh phạt" | Colleagues say "hồi quy logistic có phạt" or "có chính quy hóa"; "hiệu chỉnh phạt" sounds invented | 3 |
| 26 | 03-01:13 | "Cây tăng cường độ dốc (gradient-boosted trees)" | Literal "độ dốc" for gradient; most lecturers say "gradient boosting" | 3 |
| 27 | 03-01:13 | "số sự kiện trên mỗi tham số dồi dào" | "sự kiện" (event = non-completion) not defined here | 2 |
| 28 | 03-01:14 | "Các nhóm mức nguy cơ xác định theo số sinh viên cán bộ liên hệ được" | Two coinages stacked; meaning (tiers set by contact capacity) only clear after 03-04 | 2 |
| 29 | 03-02:3 | "tỷ lệ gộp chung, tính thêm theo mẫu số thứ hai; cách so sánh này cho thấy những tỷ lệ nào thay đổi theo mẫu số" | Same undefined "mẫu số thứ hai"; the baseline of AQ1 remains unknown | 1 |
| 30 | 03-02:5 | "Hiệu ứng cố định phù hợp với thiết kế quan sát được mọi lượt mở…, còn việc có tính sai số chuẩn theo cụm hay không phụ thuộc vào cách dữ liệu được lấy mẫu" | Two claims joined by "còn"; "thiết kế quan sát được mọi lượt mở" is opaque | 2 |
| 31 | 03-02:5 | "quá ít để ước lượng một phương sai" | Variance of what? (the random-effect variance) | 2 |
| 32 | 03-02:5 | "tỉ số odds cho giá trị lớn hơn tỉ số nguy cơ" | Logic of why this matters (OR overstates RR when outcome is common) left implicit | 2 |
| 33 | 03-02:5 | "mỗi ước lượng là hiệu ứng riêng phần của một dấu hiệu tương quan với các dấu hiệu khác; … không được đọc như trọng số riêng của từng dấu hiệu" | Dense; "hiệu ứng riêng phần" vs "trọng số riêng" sound like the same thing | 2 |
| 34 | 03-03:3 | "sinh viên có mức hoạt động thấp hơn so với mặt bằng của lượt mở được xếp trước" | Understood; translated order | 3 |
| 35 | 03-03:5 | "trên 19 biến dự báo chính dùng được" | "dùng được" tacked on at the end; sounds translated | 3 |
| 36 | 03-03:5 | "Số lượt nhấp theo tuần (tổng số lượt nhấp đã là một biến dự báo chính) được đưa vào bộ biến mở rộng gồm 10 biến dự báo bổ sung" | Is weekly clicks one of the 10 or an 11th? (10-04 suggests "10 + weekly clicks") | 2 |
| 37 | 03-03:5 | "Các lượt mở huấn luyện có từ 5.245 đến 5.519 sinh viên không hoàn thành" | Read as "each run has 5,245–5,519", impossible with 11,811 enrolments in 9 runs; the range means day 27 vs day 13, which only 10-02:3 explains | 1 |
| 38 | 03-03:5 | "gấp khoảng bảy lần con số 1.731 mà các tiêu chí cỡ mẫu tối thiểu của Riley và cộng sự đòi hỏi theo các giả định mặc định" | Understood; long relative clause in English order | 3 |
| 39 | 03-03:5 | "vì phép co hệ số không khắc phục được cỡ mẫu nhỏ" | "phép co hệ số" (shrinkage) unusual; link to per-module models needs a second read | 2 |
| 40 | 03-03:7 | "benchmark đó đã loại các bộ dữ liệu mà hồi quy logistic đạt kết quả cách các mô hình tốt nhất không quá 5%" | "benchmark đó" has no antecedent; "cách… không quá 5%" is hard to parse | 2 |
| 41 | 03-03:7 | "bằng cùng một phần mềm" | Same software as what? | 2 |
| 42 | 03-03:7 | "Hiệu chỉnh phạt chỉ cải thiện hiệu chuẩn xét trung bình" | "xét trung bình" (on average, across samples) is unclear | 2 |
| 43 | 03-04:3 | "Phương án ứng viên là chia nhóm mức nguy cơ, dành cho giảng viên hướng dẫn muốn liên hệ nhẹ hơn với nhóm thứ hai" | "nhóm thứ hai" not yet introduced when used; "liên hệ nhẹ hơn" vague | 2 |
| 44 | 03-04:5 | "muốn ước lượng tác động của một can thiệp thay đổi ra sao giữa các sinh viên thì cần dữ liệu…" | "thay đổi ra sao" attaches ambiguously (the intervention changes? the effect varies?) | 2 |
| 45 | 03-04:5 | "những khách hàng có nguy cơ dự báo cao nhất" | Sudden switch to "khách hàng" in a student context; the churn study is not named | 2 |
| 46 | 04-00:8 | "nên thiết kế còn quy định rõ ai được xem dữ liệu nào và vào lúc nào" | Understood; translated | 3 |
| 47 | 04-01:15 | "Tỷ lệ phát hiện chuẩn hóa trong giới hạn danh sách, ngày 27, 5 trên 20 sinh viên" | Coined metric name; had to go to the glossary | 2 |
| 48 | 04-01:16 | "Hai cách tổng hợp; đối chiếu với các tổng đã biết" | Which two ways? Which known totals? Only 10-03 explains | 2 |
| 49 | 04-01:17 | "Tỷ lệ gộp; mẫu số thứ hai" | Undefined term again | 1 |
| 50 | 04-01:18 | "Kiểm tra xác nhận tỷ lệ phát hiện theo nhóm" | "kiểm tra xác nhận" (confirmatory test) reads as "verification check" | 2 |
| 51 | 04-01:19 | "kiểm tra xác nhận về công bằng đạt hoặc đã được xem xét lại" | Which is reviewed – the test or the group? | 2 |
| 52 | 04-02:5 | "1.586 lượt đăng ký học trong tập kiểm thử thuộc về sinh viên đã có mặt năm 2013 được loại ra trong một phân tích độ nhạy" | Long subject; verb at the end | 3 |
| 53 | 04-02:13 | "Sinh viên có mặt cả trong lượt mở được tách riêng để kiểm định bị loại khỏi dữ liệu huấn luyện của fold đó" | "có mặt cả trong" – also in what? Missing the second term of "cả… lẫn…" | 2 |
| 54 | 04-02:16 | "còn quá khớp vào tiêu chí lựa chọn có thể làm sai lệch kết quả ngang với chênh lệch giữa các thuật toán" | "quá khớp vào tiêu chí lựa chọn" is a calque; the comparison "ngang với" is hard to follow | 2 |
| 55 | 04-02:17 | "Cây tăng cường độ dốc… hoặc bộ biến mở rộng gồm thêm 10 biến dự báo cùng số lượt nhấp theo tuần… chỉ thay thế lựa chọn chính khi làm tăng… ít nhất 0,03 (…) và tăng ở ít nhất 7 trong 9 fold" | Two subjects, two conditions and a parenthesis in one sentence | 2 |
| 56 | 04-02:25 | "các hệ số theo module được mã hóa thành độ lệch so với module trung bình; module không có trong dữ liệu huấn luyện nhận giá trị trung bình" | "giá trị trung bình" of what? (a zero deviation) | 2 |
| 57 | 04-02:28 | "Vì vậy, phương án chỉ dùng kết quả đã biết chấm điểm các lượt mở B năm 2014…" | First parse: "the option only uses known results to score…"; the noun phrase ends at "đã biết" and "chấm điểm" is the verb | 2 |
| 58 | 04-03:3 | "số sinh viên không hoàn thành có trong danh sách của một lượt mở chia cho số tối đa mà một danh sách cùng độ dài có thể chứa, gộp qua các lượt mở" | Definition in one breath; "gộp qua các lượt mở" attaches unclearly | 2 |
| 59 | 04-03:5 | "so với mức trần do số sinh viên cán bộ liên hệ được quyết định" | Coinage plus passive agent; parse breaks | 2 |
| 60 | 04-03:11 | "để việc tách lượt mở có tỷ lệ cao khỏi lượt mở có tỷ lệ thấp không làm chỉ số này tăng giả tạo" | Needed the A.19 row 1 to understand what "tách" means here | 2 |
| 61 | 04-03:16 | "Lợi ích ròng (net benefit) so với các phương án liên hệ tất cả, không liên hệ ai hoặc liên hệ theo quy tắc [32] mô tả một chính sách dựa trên ngưỡng" | Long subject, verb "mô tả" buried; first read "so với" as the verb | 2 |
| 62 | 04-03:20 | "Một chênh lệch nhỏ hơn biến thiên do lấy mẫu ít có ý nghĩa thực tiễn, nên thiết kế chỉ định một điều kiện đạt duy nhất trên một tổng thể duy nhất" | "nhỏ hơn biến thiên do lấy mẫu" parses badly; the "nên" link is not obvious | 2 |
| 63 | 04-03:25 | "Tổng thể và điểm vận hành" | "điểm vận hành" (operating point) unfamiliar in Vietnamese | 2 |
| 64 | 04-03:27 | "khoảng tin cậy 95% của chênh lệch theo bootstrap hai tầng ghép cặp" | "ghép cặp" here = paired model-vs-rule; later "ghép cặp" means something else (row 121) | 2 |
| 65 | 04-03:27 | "báo cáo số lượt mở thắng, hòa và thua" | Understood; sports metaphor sounds translated | 3 |
| 66 | 04-03:30 | "Không nhóm kiểm tra xác nhận nào vừa có tỷ lệ phát hiện… thấp hơn… quá 10 điểm phần trăm, vừa có khoảng tin cậy bootstrap một phía 95% của chênh lệch, đã hiệu chỉnh Holm cho ba nhóm kiểm tra xác nhận, nằm hoàn toàn dưới 0; nhóm thỏa cả hai điều kiện bị đánh dấu" | Negated "không… nào vừa… vừa…", nested modifiers, two conditions and a consequence in one cell; I could not state the rule after two reads | 1 |
| 67 | 04-03:35 | "Mọi tổng thể, thời điểm chốt dữ liệu và số sinh viên cán bộ liên hệ được khác đều là phân tích độ nhạy" | "khác" at the end must scope over all three nouns; first read as "all populations… are sensitivity analyses" | 2 |
| 68 | 04-04:7 | "tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation), đo bằng mức ngang nhau của tỷ lệ phát hiện" | Circular definition; "separation" is the textbook name, the Vietnamese is coined | 3 |
| 69 | 04-04:9 | "phù hợp với hoạt động liên hệ có tác hại chính là bỏ sót sinh viên đang gặp khó khăn" | Reads as "contact whose main harm is missing students" – needs reread | 2 |
| 70 | 04-04:11 | "Kiểm tra xác nhận bao gồm ba nhóm mà AQ4 nêu tên và có ít nhất 400 lượt đăng ký học trong tập kiểm thử" | "mà AQ4 nêu tên và có…" – AQ4 has 400 enrolments? Subject of "có" ambiguous | 2 |
| 71 | 04-04:12 | "nhóm có mức khó khăn của khu vực cao nhất, 0–10%" | "0–10%" for the most deprived band is counter-intuitive without explanation | 2 |
| 72 | 04-04:13 | "Quy tắc F1 của Bảng 4.2 đánh dấu một nhóm để xem xét lại." | Reads like a result ("flagged one group") in a plan with no results | 2 |
| 73 | 04-04:13 | "Theo tỷ lệ không hoàn thành trong dữ liệu huấn luyện, ngay cả nhóm đủ điều kiện có tỷ lệ thấp nhất… cũng có hơn 100 sinh viên không hoàn thành" | Purpose of the sentence (expected count in the test set) left implicit | 2 |
| 74 | 04-04:19 | "nên một phép kiểm tra biến thay thế so sánh điểm rủi ro và các biến dự báo giữa các nhóm" | "biến thay thế" (proxy) first read as "replacement variable" | 2 |
| 75 | 05-00:7 | "Risk and Ethics Notes (ghi chú về rủi ro và đạo đức)" | English title kept | 3 |
| 76 | 05-00:8 | "sổ đăng ký đầy đủ gồm mười sáu rủi ro" | "sổ đăng ký" sounds like a registry book; "danh mục rủi ro" is usual | 3 |
| 77 | 05-00:16 | "chọn phương án kiểm tra có lợi" | Favourable to whom? | 2 |
| 78 | 05-00:17 | "Lý do không khớp với thứ hạng; hiểu tác động riêng phần như trọng số" | Two compressed risks; had to recall 03-02 | 2 |
| 79 | 05-00:18 | "thí điểm ngẫu nhiên hóa trước mọi xếp hạng theo lợi ích can thiệp" | "trước" = before (in time) or "as a precondition"? | 2 |
| 80 | 05-00:20 | "nhãn bị đánh dấu hết hiệu lực khi lượt mở kết thúc" | "nhãn bị đánh dấu" = "the flagged label"? Calque of "flag" | 2 |
| 81 | 05-01:6 | "Người xây dựng mô hình không được thấy thông tin vượt quá điểm phân tách" | "điểm phân tách" (split point) unclear in time vs data sense | 2 |
| 82 | 05-01:9 | "còn phương án chỉ dùng kết quả đã biết kiểm tra lại điều kiện đó" | Same coinage; same parse break as row 57 | 2 |
| 83 | 05-01:17 | "Nhiều mô hình có mức phù hợp với dữ liệu gần như ngang nhau, nên không hệ số nào được hiểu là nguyên nhân" | Logical step (Rashomon effect) missing; "nên" does not follow for a reader | 2 |
| 84 | 05-01:18 | "các ước lượng đã hiệu chỉnh lẫn nhau của AQ2" | "hiệu chỉnh lẫn nhau" – mutually adjusted; awkward | 2 |
| 85 | 05-02:9 | "một đợt thí điểm ngẫu nhiên hóa có thời điểm gốc (time zero) là thời điểm chốt dữ liệu" | "thời điểm gốc" coinage; why time zero matters is not said | 2 |
| 86 | 05-02:12 | "Mỗi nhãn bị đánh dấu dẫn đến hoạt động hỗ trợ và hết hiệu lực khi lượt mở kết thúc, vì sinh viên bị đánh dấu cần có cơ hội chứng minh dự báo sai và việc gắn nhãn không được làm thiên lệch nhận thức của cán bộ" | Rule and two reasons in one sentence; "nhãn… dẫn đến hoạt động hỗ trợ" is odd | 2 |
| 87 | 05-02:26 | "dự báo tự tác động (performative prediction)" | Understood with the English; coinage | 3 |
| 88 | 05-02:26 | "các lần liên hệ được ghi nhận cùng kết quả trước mọi lần huấn luyện lại" | Recorded together with outcomes, before retraining – order of ideas unclear | 2 |
| 89 | 06-00:13 | "một quy tắc thành công đòi hỏi mô hình vượt quy tắc dấu hiệu sớm ở ít nhất 9 trên 13 lượt mở kiểm thử vẫn có thể được đáp ứng do ngẫu nhiên với xác suất khoảng 13%" | Long subject, two "quy tắc", verb at the end | 2 |
| 90 | 07-00:16 | "Script, seed ngẫu nhiên, phiên bản gói phần mềm" | Untranslated "Script", "seed"; acceptable but foreign | 3 |
| 91 | 08-00:3 | "gắn mỗi câu hỏi với một chuỗi liên kết duy nhất" | Understood; translated | 3 |
| 92 | 08-00:9 | "Tỷ lệ gộp; mẫu số thứ hai" | Undefined term again | 1 |
| 93 | 08-00:10 | "D2; dấu hiệu cho D1" | Fragment; signs for D1? | 2 |
| 94 | 10-00:3 | "các AQ Modeling Brief, là bản mô tả…; các Evaluation Design Card, là thẻ thiết kế đánh giá…" | Eight appendices in one sentence with English titles | 3 |
| 95 | 10-01:28 | "gồm ước lượng chưa hiệu chỉnh và ước lượng trong từng lượt mở module" | Second item lacks "đã hiệu chỉnh"; contrast unclear | 2 |
| 96 | 10-01:40 | "(điểm trung bình bài đánh giá chấm bằng máy (CMA) bị loại vì dưới 10% số dòng huấn luyện có giá trị này)" | Parentheses inside parentheses inside a list | 2 |
| 97 | 10-01:48 | "lượt đăng ký học nào đứng đầu danh sách, với mức vượt tỷ lệ nền (lift) của lượt mở và tỷ lệ phát hiện (recall) ra sao" | "với… ra sao" construction is foreign | 2 |
| 98 | 10-02:11 | "với hiệu ứng module được rút từ một tổng thể các module" | "rút từ một tổng thể" = drawn from a population; literal | 2 |
| 99 | 10-02:16 | "Tất định; sai số chuẩn bền vững" | Telegraphic calques of "deterministic; robust SE" | 3 |
| 100 | 10-02:18 | "Cho D2 biết nên chú ý dấu hiệu nào" | D2 is a decision, not a person who can be told | 2 |
| 101 | 10-02:27 | "23 tham số so với 5.245–5.519 sinh viên… 11.811–12.080 lượt đăng ký học… con số 1.728–1.731" | Three ranges in one cell; the day-27/day-13 meaning is only in the paragraph above | 2 |
| 102 | 10-02:27 | "rất ít lượt đăng ký học bị kiểm duyệt (censored)" | "kiểm duyệt" is used in biostatistics, but many readers will think of censorship | 3 |
| 103 | 10-02:33 | "Bổ sung thông tin về thời điểm, điều mà D1 không dùng khi thời điểm chốt cố định" | "điều mà" reference and the condition are hard to parse | 2 |
| 104 | 10-02:36 | "Mô hình chỉ dùng đặc điểm cá nhân cho thấy bao nhiêu phần của thứ hạng đến từ mức tham gia học tập chứ không phải từ module và lịch sử học tập" | Seems to state the opposite of what a background-only model measures; needed rereading | 2 |
| 105 | 10-02:45 | "Quy tắc biết được tại mỗi thời điểm chốt" | "biết được" – the rule is known? computable? | 2 |
| 106 | 10-03:6 | "Số sinh viên cán bộ liên hệ được k của một lượt mở là 3 hoặc 5 sinh viên được liên hệ trên mỗi nhóm hướng dẫn khoảng 20 sinh viên" | Coinage plus symbol k between noun and modifier | 2 |
| 107 | 10-03:10 | "Điểm vận hành chính là 5 trên 20 tại ngày 27, vì danh sách này phục vụ đợt lập danh sách vào tuần 5" | "danh sách này" – which list? | 2 |
| 108 | 10-03:18 | "Tỷ lệ cộng dồn theo từng tuần của các lượt đăng ký học đã bỏ lỡ bài được chấm điểm lần đầu" | "lần đầu" attaches to "chấm điểm" or "bỏ lỡ"? | 2 |
| 109 | 10-03:20 | "tỷ lệ khi có và khi không có 138 lượt đăng ký học được đánh dấu" | Only hint of what the "second denominator" is, and it does not use that name | 2 |
| 110 | 10-03:21 | "khi đổi giữa hai mẫu số" | Which two? | 2 |
| 111 | 10-03:33 | "độ nhạy đối với lượt nhấp đã loại dòng trùng, đối với biến thể quy tắc có tính cả CMA nộp trễ, đối với 138 lượt…" | Four sensitivity items chained by "đối với" | 2 |
| 112 | 10-03:34 | "được mô tả chứ không bị hiệu chỉnh để loại bỏ" | Adjusted away – what is removed? | 2 |
| 113 | 10-03:42 | "là các cách biểu diễn khác của cùng số dương tính thật khi k cố định; trung bình không trọng số của chênh lệch theo từng lượt mở; …" | Ten secondary metrics in one cell | 2 |
| 114 | 10-03:47 | "S1 (điều kiện đạt duy nhất): trên cả 13 lượt mở kiểm thử, mọi lượt đăng ký học đủ điều kiện, tại ngày 27, k = 5 trên 20, tỷ lệ phát hiện chuẩn hóa gộp… phải cao hơn…" | Four scope qualifiers before the subject | 2 |
| 115 | 10-03:57 | "sinh viên hoàn toàn không có hoạt động, nhóm mà danh sách nào cũng đưa vào, được tách khỏi sinh viên vẫn hoạt động nhưng có nguy cơ" | Appositive inside the subject; verb far away | 2 |
| 116 | 10-03:76 | "với log-odds của điểm rủi ro làm offset" | "offset" untranslated | 3 |
| 117 | 10-04:6 | "mô hình cuối cùng được chốt và lần truy cập tập kiểm thử được ghi lại trước khi kiểm thử" | Logging the access before testing? Order unclear | 2 |
| 118 | 10-04:14 | "các dòng của sinh viên cũng có mặt trong lượt mở kiểm định (121–129 sinh viên, 242–258 dòng) bị loại…, ở cả vòng ngoài lẫn vòng trong" | Long subject with ranges; "vòng ngoài/vòng trong" (nested CV) not introduced | 2 |
| 119 | 10-04:16 | "Cây tăng cường độ dốc chỉ thay thế hồi quy logistic, cũng như nhóm biến mở rộng chỉ thay thế nhóm chính, khi mức cải thiện đạt…" | Interrupted structure "X chỉ…, cũng như Y chỉ…, khi…" | 2 |
| 120 | 10-04:19 | "Các lượt mở ghép cặp (9) và không ghép cặp (4)" | "lượt mở ghép cặp" never defined; guessed a 2014 run whose module also ran in 2013 | 1 |
| 121 | 10-04:28 | "phương án chỉ dùng kết quả đã biết chấm điểm các lượt mở B năm 2014" | Same parse break as row 57 | 2 |
| 122 | 10-04:31 | "các lượt mở được lấy mẫu lại, rồi đến các lượt đăng ký học trong từng lượt mở được chọn; danh sách… được lập lại thành 25%…" | "rồi đến… được chọn" elliptical; "lập lại thành 25%" odd | 2 |
| 123 | 10-04:56 | "9 lượt mở ghép cặp / 4 lượt mở không ghép cặp" | Undefined term in a sample-size table | 1 |
| 124 | 10-04:66 | "mô hình riêng cho từng lượt mở vẫn không phù hợp" | 03-03 says "từng module"; I could not tell whether both are meant | 2 |
| 125 | 10-05:15 | "5.697 / 2.488 và 6.114 / 2.757" | Slash and "và" mix two meanings (enrolments/non-completers, female and male) | 2 |
| 126 | 10-05:17 | "Mức khó khăn của khu vực 0–10%" | Same as row 71 | 2 |
| 127 | 10-05:33 | "trừ đi của phần còn lại, ngày 27, k = 5 trên 20, gộp trong từng lượt mở" | "gộp trong từng" contradicts itself; "trừ đi của" missing head noun | 2 |
| 128 | 10-05:35 | "khác biệt là điều có thể dự liệu trước khi tỷ lệ nền khác nhau" | First read "before base rates differ"; meant "foreseeable when…" | 2 |
| 129 | 10-05:37 | "kèm dấu của chênh lệch về khả năng phân biệt và giá trị tham chiếu tính từ nhãn nhóm được hoán vị ngẫu nhiên trong từng lượt mở" | Long chain of modifiers; reference value of a permutation test not explained | 2 |
| 130 | 10-05:42 | "Cho thấy ngưỡng cắt tại k tùy ý đến mức nào" | "tùy ý" (arbitrary) placed oddly | 2 |
| 131 | 10-05:44 | "chênh lệch có lợi cho sinh viên nam mà phần lớn mô hình… đều tái tạo và khuếch đại nhẹ, cùng với sai lệch thất thường ở nhóm ít người có tình trạng khuyết tật" | Relative clause inverted; "nhóm ít người có…" = few disabled people or the small disabled group? | 2 |
| 132 | 10-06:13 | "rà soát pipeline" | Untranslated | 3 |
| 133 | 10-06:15 | "Dịch chuyển giữa các năm và khi áp dụng cho trường đại học" | "dịch chuyển" (shift) without object; two contexts glued | 2 |
| 134 | 10-06:19 | "Danh sách theo lượt mở so với số sinh viên giảng viên hướng dẫn liên hệ được" | Risk name is a comparison without a verb | 2 |
| 135 | 10-06:22 | "Quy tắc về mức thiếu hụt ở Bảng A.16" | A.16 never calls it a "shortfall rule" | 2 |
| 136 | 10-06:25 | "Nhãn bị đánh dấu dẫn đến hỗ trợ và hết hiệu lực khi lượt mở kết thúc" | Same as row 86 | 2 |
| 137 | 10-07:13 | "không dùng lập luận về mất cân bằng lớp để chọn đường cong độ chính xác – tỷ lệ phát hiện, vì tỷ lệ không hoàn thành là 44–46%" | Negated reasoning about a curve choice; needed rereading | 2 |
| 138 | 10-07:13 | "bootstrap phân tầng" | Elsewhere "bootstrap hai tầng"; are they the same? | 3 |
| 139 | 10-07:14 | "Thử nghiệm mục tiêu (target trial)" | Literal; the usual term is "mô phỏng thử nghiệm đích (target trial emulation)" | 2 |
| 140 | 10-07:16 | "số sinh viên cán bộ liên hệ được tính theo lượt mở so với theo giảng viên hướng dẫn" | Coinage plus "tính theo… so với theo…" | 2 |
| 141 | 10-07:27 | "số liệu không phải của 9 lượt mở huấn luyện" | Fragment; what was wrong is not said | 2 |
| 142 | 10-07:43 | "Quy tắc AQ2 tính theo tỷ lệ số module" | Telegraphic; meaning (two-thirds of modules) only via A.9 | 2 |
| 143 | 10-07:48 | "phương án khi không đạt lại dùng lại tập kiểm thử" | "lại dùng lại" – double "lại"; parse breaks | 2 |
| 144 | 10-07:49 | "Chọn mô hình theo một cách gộp khác" | Different from what? | 2 |
| 145 | 10-07:52 | "Tỉ số odds ở tỷ lệ nền này; ngưỡng quá dễ đạt" | A verbless fragment; I could not reconstruct the criticism | 1 |
| 146 | 10-08:4 | "cấp độ phân tích" | Elsewhere "loại phân tích"; is it the same? | 3 |
| 147 | 10-08:13 | "enrolment, assessment_due" | Raw table names without Vietnamese gloss (also features_d27, capacity_by_run) | 3 |
| 148 | 10-08:13 | "Tỷ lệ gộp; mẫu số thứ hai" | Undefined term again | 1 |

## Recurring terms that feel invented or unnatural

Counts cover `01-*`–`08-*` and `10-*` (`.vi.md`, prompt lines excluded).

| Term in the report | Count | Meaning I inferred | Plainer word a colleague would use |
| :-- | :-- | :-- | :-- |
| số sinh viên cán bộ liên hệ được | 23 | contact capacity | "năng lực liên hệ", "hạn mức liên hệ (k)" |
| tỷ lệ phát hiện chuẩn hóa / … trong giới hạn danh sách | 19 / 22 | normalised recall at k | "recall@k chuẩn hóa", "tỷ lệ phát hiện tại k" |
| kiểm tra xác nhận | 19 | confirmatory (pre-specified) test | "kiểm định khẳng định", "kiểm định chính (định trước)" |
| mẫu số thứ hai | 5 | rate recomputed excluding 138 flagged enrolments (guess) | name the denominator: "mẫu số loại 138 lượt đăng ký thiếu ngày" |
| phương án chỉ dùng kết quả đã biết | 5 | variant trained only on runs whose outcomes were known in time | "phương án huấn luyện chỉ trên các lượt mở B 2013" |
| lượt mở ghép cặp / không ghép cặp | 4 | 2014 runs whose module also ran in 2013 (guess) | define once: "lượt mở có lượt mở cùng module năm 2013" |
| mức vượt tỷ lệ nền | 7 | lift | "lift" / "hệ số nâng" |
| tiêu chí ngang bằng tỷ lệ phát hiện (separation) | 6 | equal recall / equal opportunity | "tiêu chí cơ hội ngang nhau (equal opportunity)" |
| hồi quy logistic có hiệu chỉnh phạt | 8 | penalised logistic regression | "hồi quy logistic có phạt / có chính quy hóa" |
| cây tăng cường độ dốc | 11 | gradient-boosted trees | "gradient boosting (cây tăng cường gradient)" |
| mô hình sống sót | 8 | survival model | "mô hình sống còn", "phân tích sống còn" |
| mô hình đối sánh | 6 | challenger model | "mô hình thách thức", "mô hình so sánh" |
| biến thay thế | 8 | proxy variable | "biến đại diện (proxy)" |
| tổng thể | 22 | analysis population | "quần thể phân tích", "nhóm đối tượng" |
| mức khó khăn (của khu vực) | 14 | IMD band | "chỉ số thiếu thốn khu vực (IMD)" |
| sổ đăng ký rủi ro | 4 | risk register | "danh mục rủi ro", "bảng theo dõi rủi ro" |
| nhãn bị đánh dấu | 3 | the "flagged" status | "trạng thái 'có nguy cơ'" |
| điểm vận hành | 2 | operating point | "mức k chính", "điểm làm việc" |
| lượt mở (module) | 272 | module presentation | acceptable once defined; "đợt mở module" reads more naturally |
| AQ Modeling Brief / Evaluation Design Card / Candidate Solution Matrix / Business Goal | 8 / 12 / 4 / 5 | brief's English template names | keep once in brackets, then use the Vietnamese name |
