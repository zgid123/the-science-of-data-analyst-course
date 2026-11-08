# Reader test 2 – Vietnamese version of the Milestone 4 report

Reader: a Vietnamese lecturer in data analytics who reads only the `.vi.md` files (main text 01–08, appendices 10-00 to 10-07, abbreviation and terms pages 00-1, 00-2) and has not seen the English source. Date: 2026-11-08.

**Overall judgement.** Yes: after one careful reading, a colleague in the field could explain the document. It sets out four questions, a temporal split (2013 for development, 2014 tested once), penalised logistic regression compared against an early-sign rule, one pre-registered pass condition (S1) on normalised recall of a capacity-limited list, a fairness check on recall, and a risk and legal section. The prose is grammatical, and most paragraphs announce their point before giving the evidence. The difficulty is density, not language. Many sentences carry three or four technical ideas at once, especially in the evaluation cards (Bảng 4.3), the FR1 rule (Bảng 4.5), the fairness sample-size paragraph (Mục 4.4) and the appendix tables. Long coined noun phrases ("tỷ lệ phát hiện trong giới hạn danh sách", "phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013", "mô hình logistic chỉ dùng đặc điểm cá nhân") stand in for compact terms that Vietnamese data scientists normally keep in English (recall@k, top-k, lift, gradient boosting, proxy, challenger). This slows reading without adding clarity. A handful of passages read the wrong way round or seem to contradict another section (10-01:40, 10-05:15, 04-01:47 with S3 before S2, 10-04:9 column header). Some procedural ideas appear before they are defined ("lần chốt thứ hai" in Bảng 4.3, inner and outer folds in Bảng A.5). I could not follow 2 passages at all, I needed to reread 52, and 58 more read as translated. "Kỳ mở" (362 occurrences) is understandable but unusual; after the first page it reads as a project term rather than as Vietnamese.

## Passages that stopped me

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 00-2-glossary.vi.md:12 | "Hệ số của log-odds của điểm rủi ro trong mô hình logistic hiệu chuẩn lại" | Two stacked "của"; I had to parse which model is refitted and on what | 2 |
| 2 | 00-2-glossary.vi.md:14 | "với log-odds của điểm rủi ro làm offset" | "offset" is left untranslated and unexplained here (it is explained only in Bảng A.4) | 2 |
| 3 | 00-2-glossary.vi.md:23 | "Labels-available variant – Phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013" | The English term (labels available) and the Vietnamese name (train on February runs) describe different things; the link is not stated | 2 |
| 4 | 00-2-glossary.vi.md:33 | "Precision at capacity – Độ chính xác của danh sách dài k" | "độ chính xác" is the usual word for accuracy; for precision a reader expects "độ chính xác dương" or just precision@k | 3 |
| 5 | 00-2-glossary.vi.md:37 | "ước lượng tần suất xuất hiện các chênh lệch theo từng kỳ mở có lợi ít nhất bằng mức quan sát được, nếu dấu của chênh lệch ở mỗi kỳ mở là ngẫu nhiên" | Head noun lost: is "có lợi" describing the differences or the runs? Reads as an English relative clause | 2 |
| 6 | 01-01-goal-decisions-aqs.vi.md:7 | "Đồng thời, các thay đổi này điều chỉnh cách đo của hai câu hỏi như trình bày dưới đây." | Which two questions? The table below does not mark them | 2 |
| 7 | 01-01-goal-decisions-aqs.vi.md:16 | "D2; lý do hiển thị cạnh từng tên trong danh sách của D1" | Compressed table cell; I understood only after reading AQ2's brief | 3 |
| 8 | 01-01-goal-decisions-aqs.vi.md:20 | "Chỉ số thứ hai so danh sách với tỷ lệ nền của kỳ mở" | Compares what in the list with the base rate? The share of non-completers comes only in the next sentence | 3 |
| 9 | 01-02-prepared-data-entry-gate.vi.md:3 | "12.080 lượt đăng ký học với 5.519 sinh viên không hoàn thành" | Unit switches from enrolments to students in the same count | 3 |
| 10 | 01-02-prepared-data-entry-gate.vi.md:13 | "các phép biến đổi chỉ được ước lượng trên các kỳ mở năm 2013" | "Phép biến đổi được ước lượng" is a calque (fitted transformations) | 3 |
| 11 | 02-00-aq-task-mapping.vi.md:3 | "bốn bản mô tả AQ Modeling Brief" | Vietnamese and English name stacked; redundant | 3 |
| 12 | 02-01-modeling-briefs.vi.md:3 | "có thể được báo cáo dưới dạng lớp, xác suất hoặc thứ hạng" | "lớp" (class label) is unclear on its own; "nhãn lớp" would be clearer | 3 |
| 13 | 02-01-modeling-briefs.vi.md:46 | "Phương án thay thế là bộ biến dự báo mở rộng: thêm 10 biến dự báo khác, cộng với số lượt nhấp của từng tuần (2 biến tại ngày 13, 4 biến tại ngày 27)" | Alternative to what? Unclear whether the 10 variables replace or add to the 19 | 2 |
| 14 | 02-01-modeling-briefs.vi.md:48 | "Rò rỉ thông tin và khả năng áp dụng cho kỳ mở diễn ra sau" | Translated phrase for temporal transportability; "khả năng tổng quát hóa sang kỳ sau" is more usual | 3 |
| 15 | 02-01-modeling-briefs.vi.md:65 | "với số tên bằng mức mà hạn mức liên hệ cho phép" | "mức mà hạn mức" is redundant and awkward | 3 |
| 16 | 02-02-technical-tasks.vi.md:3 | "còn một mô hình hồi quy chỉ dùng để đo mối liên hệ ... thuộc loại mô hình mô tả theo cách phân loại của Shmueli ... AQ2 vẫn thuộc loại phân tích chẩn đoán" | Too many ideas at once; "mô tả" and "chẩn đoán" collide and I had to reread to see that one is Shmueli's term and the other is the brief's | 2 |
| 17 | 02-02-technical-tasks.vi.md:10 | "Mô hình sống sót thời gian rời rạc có thể cho biết thêm thời điểm sinh viên rời khỏi module" | Understood, but "mô hình sống sót" sounds translated; colleagues say "phân tích sống sót (survival)" | 3 |
| 18 | 03-01-criteria-matrix.vi.md:13 | "tỷ lệ tính lại theo mẫu số thứ hai" | "Mẫu số thứ hai" is used before it is explained (the explanation follows in brackets) | 3 |
| 19 | 03-01-criteria-matrix.vi.md:14 | "Mọi kỳ mở của các module đều có trong dữ liệu, nên hiệu ứng cố định là phù hợp" | The reasoning (full population, not a sample, so fixed effects) is not given here; it reads as a non sequitur | 2 |
| 20 | 03-01-criteria-matrix.vi.md:15 | "Ứng viên 1 với các biến dự báo chính, trừ khi Ứng viên 2 hoặc bộ biến dự báo mở rộng vượt ít nhất một khoảng chênh lệch ấn định trước" | Dense cell; "khoảng chênh lệch ấn định trước" is unclear until Mục 4.2 | 2 |
| 21 | 03-01-criteria-matrix.vi.md:15 | "số sự kiện trên mỗi tham số cao" | Field term (EPV), but terse in a table cell | 3 |
| 22 | 03-02-descriptive-diagnostic.vi.md:5 | "Cách xác định phạm vi dữ liệu chính là nguồn chủ yếu khiến một tỷ lệ mô tả có thể gây hiểu sai." | Repeats the previous sentence's phrase; sounds translated | 3 |
| 23 | 03-02-descriptive-diagnostic.vi.md:9 | "Hiệu ứng cố định phù hợp với thiết kế trong đó mọi kỳ mở của các module được nghiên cứu đều có trong dữ liệu." | Same unexplained logic as #19; it becomes clear only three sentences later | 2 |
| 24 | 03-02-descriptive-diagnostic.vi.md:9 | "Chênh lệch này nhỏ hơn chênh lệch mà dấu hiệu đó cho thấy khi xét riêng; chênh lệch này cũng không phải là phần tình trạng không hoàn thành do dấu hiệu đó giải thích." | Three "chênh lệch" in two clauses; the second clause's point (not an attributable fraction) is hard to catch | 2 |
| 25 | 03-02-descriptive-diagnostic.vi.md:9 | "mô hình cho kết quả tất định" | "Tất định" is correct but rare; the point (rerunning gives the same result) is only explained in Bảng A.1 | 3 |
| 26 | 03-03-predictive.vi.md:5 | "khi bằng số dấu hiệu, sinh viên có tỷ lệ hoạt động thấp hơn được xếp trước" | "Khi bằng số dấu hiệu" (on ties) is awkward; "nếu cùng số dấu hiệu" would read better | 3 |
| 27 | 03-03-predictive.vi.md:7 | "Module và tháng bắt đầu đều đi vào mô hình dưới dạng nhiều số hạng, nên mô hình có tổng cộng 23 tham số." | Dummy coding is implied, not stated; I had to count to see how 19 becomes 23 | 2 |
| 28 | 03-03-predictive.vi.md:7 | "số lượt nhấp đếm lại sau khi mỗi bản ghi lặp lại hoàn toàn chỉ được tính một lần" | Long periphrasis for "click count after de-duplication" | 2 |
| 29 | 03-03-predictive.vi.md:7 | (whole paragraph) "Các biến dự báo chính chia thành bốn nhóm ... bộ này được thử như một phương án thay thế (Bảng 2.3)." | Too many ideas in one paragraph (4 groups, 10 extended variables, weekly clicks); I lost track of what is primary and what is extended | 2 |
| 30 | 03-03-predictive.vi.md:9 | "hai lớp nhãn có cỡ gần nhau" | Calque of "classes are balanced" | 3 |
| 31 | 03-03-predictive.vi.md:13 | "nghiên cứu so sánh (benchmark) cho kết quả này đã loại những bộ dữ liệu mà ở đó hồi quy logistic chỉ kém mô hình tốt nhất không quá 5%" | The logic of the caveat (selection of hard datasets) needs rereading; the sentence order follows the English | 2 |
| 32 | 03-03-predictive.vi.md:13 | "Hiệu chỉnh phạt chỉ cải thiện hiệu chuẩn ở mức trung bình, không chắc chắn trong từng trường hợp cụ thể" | "Ở mức trung bình" is ambiguous (on average vs moderately) | 2 |
| 33 | 03-04-ranking-capacity.vi.md:3 | "nhóm thứ nhất gồm 3 sinh viên đứng đầu trên mỗi 20 sinh viên, nhóm thứ hai gồm 2 sinh viên kế tiếp trên mỗi 20" | "trên mỗi 20" sounds translated (per 20) | 3 |
| 34 | 03-04-ranking-capacity.vi.md:7 | "để ước lượng mức tác động của một can thiệp thay đổi thế nào giữa các cá nhân, cần dữ liệu về can thiệp được phân bổ ngẫu nhiên hoặc dữ liệu mà yếu tố gây nhiễu không làm sai lệch ước lượng" | English sentence order (purpose clause with an embedded question); missing subject | 2 |
| 35 | 04-00-evaluation-design.vi.md:3 | "Chỉ số thứ nhất được tính trên đường cong đặc trưng hoạt động của bộ thu (ROC), là diện tích dưới đường cong ROC (ROC-AUC)." | The literal expansion "đặc trưng hoạt động của bộ thu" is never used by colleagues, and "được tính trên ..., là ..." is an odd structure | 3 |
| 36 | 04-00-evaluation-design.vi.md:3 | "Hướng dẫn báo cáo minh bạch mô hình dự báo đa biến cho tiên lượng hoặc chẩn đoán cá nhân, phiên bản cập nhật cho AI (TRIPOD+AI)" | A 20-word name inside a running sentence; it breaks the flow | 3 |
| 37 | 04-01-evaluation-cards.vi.md:14 | "Theo từng tuần, tỷ lệ cộng dồn các lượt đăng ký học đã bỏ lỡ ít nhất một bài được chấm điểm, tách theo kết quả" | Word order follows the English; "tách theo kết quả" is unclear (by final outcome) | 3 |
| 38 | 04-01-evaluation-cards.vi.md:16 | "138 lượt đăng ký học có cờ chất lượng dữ liệu" | "Cờ" (flag) is a programmer's word; "được đánh dấu lỗi dữ liệu" would be clearer | 3 |
| 39 | 04-01-evaluation-cards.vi.md:31 | "Phần dư trung bình theo khoảng giá trị dự báo (binned residuals), xét theo kỳ mở và theo mức hoạt động. Tương quan giữa các dấu hiệu dựa trên lượt nhấp." | Fragments without verbs; the second is unclear (correlation computed from clicks, or between click-based signs?) | 2 |
| 40 | 04-01-evaluation-cards.vi.md:41 | "Kết quả gộp bằng tổng số sinh viên không hoàn thành có tên trong các danh sách, chia cho tổng mức tối đa mà các danh sách đó có thể đạt" | "Tổng mức tối đa" (the sum of the maximum possible hits) is vague; I needed Bảng A.4 | 2 |
| 41 | 04-01-evaluation-cards.vi.md:42 | "(khi k cố định, ba chỉ số này là các cách biểu diễn khác của cùng số dương tính thật)" | Too many ideas in one cell (8 metrics, two caveats); "số dương tính thật" unexplained here | 2 |
| 42 | 04-01-evaluation-cards.vi.md:42 | "lợi ích ròng (net benefit), chỉ dùng làm bối cảnh, vì chỉ số này mô tả chính sách liên hệ mọi sinh viên có nguy cơ vượt một ngưỡng" | Understood, but "chỉ dùng làm bối cảnh" sounds translated (for context only) | 3 |
| 43 | 04-01-evaluation-cards.vi.md:43 | "sau lần chốt thứ hai, tức lần chốt mô hình cuối cùng" | "Lần chốt thứ hai" is used before any first freeze has been introduced (Mục 4.2 comes later) | 2 |
| 44 | 04-01-evaluation-cards.vi.md:45 | "độ ổn định của danh sách quanh hạng k khi lấy mẫu lại bằng bootstrap" | "Quanh hạng k" is cryptic; the meaning is only explained in Bảng A.8 | 2 |
| 45 | 04-01-evaluation-cards.vi.md:46 | "Kiểm định khẳng định, tức kiểm định chính thức trên các nhóm đã ấn định trước" | "Kiểm định khẳng định" is an invented calque of confirmatory test; it sounds like "a test that affirms" | 2 |
| 46 | 04-01-evaluation-cards.vi.md:47 | "S3 (điều kiện để hiển thị xác suất)" | S3 appears without S2; the reader wonders whether S2 was omitted (S2 appears only in Bảng 4.5) | 2 |
| 47 | 04-01-evaluation-cards.vi.md:47 | "cả hai đều xét trên giá trị ước lượng của dữ liệu gộp mọi kỳ mở" | Calque (on the pooled estimate) | 3 |
| 48 | 04-01-evaluation-cards.vi.md:47 | "Các phạm vi dữ liệu, thời điểm chốt dữ liệu và hạn mức liên hệ khác đều là phân tích độ nhạy và không thể thay đổi kết luận" | A sensitivity analysis "cannot change the conclusion" sounds odd in Vietnamese; the meaning is "has no say in the S1 verdict" | 3 |
| 49 | 04-01-evaluation-cards.vi.md:59 | "Các kỳ mở mà các vị trí trong danh sách bị dùng cho những sinh viên về sau vẫn hoàn thành." | Translated phrasing for "slots wasted on completers" | 3 |
| 50 | 04-01-evaluation-cards.vi.md:61 | "nếu kiểm định này nêu tên nhóm nào, nhóm đó phải được xem xét" | "Kiểm định nêu tên nhóm" is a personified calque (flags a group) | 2 |
| 51 | 04-02-validation-strategy.vi.md:3 | "tập kiểm thử có 1.586 lượt đăng ký học của sinh viên đã có mặt năm 2013. Giống như khi sử dụng thực tế, các lượt này vẫn nằm trong tập kiểm thử" | Why these matter (repeat students, possible leakage) is not said; I understood after reaching Bảng A.5 step 7 | 2 |
| 52 | 04-02-validation-strategy.vi.md:6 | "Nếu một sinh viên có mặt cả trong kỳ mở được tách ra để đánh giá, sinh viên đó bị loại khỏi dữ liệu huấn luyện của fold đó" | "Có mặt cả trong" is missing its second term (both in the held-out run and in the training runs) | 2 |
| 53 | 04-02-validation-strategy.vi.md:6 | "điểm kiểm định chéo sau khi tinh chỉnh lạc quan hơn đáng kể so với thực tế" | Understood, but "điểm ... lạc quan" sounds translated | 3 |
| 54 | 04-02-validation-strategy.vi.md:10 | "Giao thức áp dụng quy trình chốt hai bước được đề xuất cho mô hình dự báo" | Proposed by whom? Reads as translated passive voice | 3 |
| 55 | 04-02-validation-strategy.vi.md:12 | "Các kỳ mở J năm 2013 kéo dài 261–268 ngày, nên khi các kỳ mở B năm 2014 đến thời điểm chốt dữ liệu, kết quả của các kỳ mở J này vẫn chưa có." | I had to calculate the months myself (October + 265 days = July, after February) to accept the claim | 2 |
| 56 | 04-02-validation-strategy.vi.md:12 | "những kỳ mở duy nhất mà một trường đại học đã có kết quả vào thời điểm đó" | "Một trường đại học" is vague (which university? the hypothetical user) | 2 |
| 57 | 04-02-validation-strategy.vi.md:16 | "kiểm định tính xem các chênh lệch có lợi cho mô hình ở mức bằng hoặc hơn mức quan sát được sẽ xuất hiện thường xuyên đến đâu" | Long embedded question; the definition of the p-value is hard to follow | 2 |
| 58 | 04-02-validation-strategy.vi.md:18 | "Tiêu chí thứ ba là nguy cơ chung được ước lượng với sai số không quá 0,05." | "Nguy cơ chung" is unclear (overall outcome proportion) | 3 |
| 59 | 04-03-metrics-success.vi.md:7 | "ước lượng một mô hình hiệu chuẩn lại (recalibration model) với độ dốc được giữ cố định, rồi lấy hệ số chặn" | Understood, but it presumes the reader knows the offset trick | 3 |
| 60 | 04-03-metrics-success.vi.md:9 | "trên một dải xác suất ngưỡng" | Calque (over a range of threshold probabilities) | 3 |
| 61 | 04-03-metrics-success.vi.md:20 | "khoảng tin cậy bootstrap một phía 95% của chênh lệch nằm hoàn toàn dưới 0; khoảng này đã được hiệu chỉnh Holm trên ba nhóm, tức phép hiệu chỉnh giữ xác suất có ít nhất một nhóm bị nêu tên nhầm ở mức 5%" | Too many ideas in one cell (one-sided interval, Holm correction, FWER explanation); I had to reread twice | 2 |
| 62 | 04-03-metrics-success.vi.md:22 | "giới hạn độ dốc từ 0,8 đến 1,2 cho phép độ phân tán của nguy cơ dự báo rộng quá hoặc hẹp quá 20%" | "Rộng quá hoặc hẹp quá 20%" is ambiguous (by up to 20%?) | 2 |
| 63 | 04-04-error-fairness.vi.md:3 | "bỏ các thuộc tính này khỏi mô hình không làm mô hình mất khả năng nhận ra các thuộc tính đó" | Understood; Bảng A.7's "mù" is clearer | 3 |
| 64 | 04-04-error-fairness.vi.md:5 | "trừ các trường hợp suy biến" | Mathematical jargon left without an example | 3 |
| 65 | 04-04-error-fairness.vi.md:7 | "Ngưỡng 400 lượt và mốc 100 sinh viên không hoàn thành dựa trên cùng một phép tính." | The paragraph runs in reverse order (conclusion, then the calculation, then "ngoài ra" with the arithmetic); which calculation is meant is unclear | 2 |
| 66 | 04-04-error-fairness.vi.md:7 | "Số sinh viên còn lại lớn hơn nhóm nhiều lần, nên sai số chuẩn này là nguồn bất định chính của chênh lệch." | "Sai số chuẩn này" is an unclear reference; the statistical step is implicit | 2 |
| 67 | 04-04-error-fairness.vi.md:9 | "đồng thời thiên lệch đối với sinh viên tự khai có khuyết tật biến động thất thường" | Head noun unclear: does the bias fluctuate, or do the students? Needed rereading (Phụ lục IV phrases it better) | 2 |
| 68 | 04-04-error-fairness.vi.md:9 | "chênh lệch không phụ thuộc ngưỡng" | Compressed label for ABROCA in a list | 3 |
| 69 | 05-00-risk-ethics.vi.md:3 | "bốn chức năng là quản trị, lập bản đồ, đo lường và quản lý" | "Lập bản đồ" for NIST "Map" is literal; Vietnamese readers expect "nhận diện (map)" | 3 |
| 70 | 05-00-risk-ethics.vi.md:12 | "chọn phương án đánh giá cho kết quả thuận lợi trên tập kiểm thử" | Ambiguous: choosing a variant because it gives favourable results | 3 |
| 71 | 05-00-risk-ethics.vi.md:16 | "sinh viên chỉ được đánh dấu đến khi kỳ mở kết thúc" | Reads as "students are only flagged until the run ends" (as if flagging were a reward); the meaning is "the flag expires" | 2 |
| 72 | 05-01-leakage-interpretability.vi.md:3 | "Người xây dựng mô hình không được thấy thông tin nằm sau điểm phân tách giữa dữ liệu huấn luyện và dữ liệu kiểm thử" | "Nằm sau điểm phân tách" is a translated spatial metaphor | 3 |
| 73 | 05-01-leakage-interpretability.vi.md:3 | "phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 kiểm tra lại điều kiện đó" | A training variant "checks a condition"; the role is unclear without Mục 4.2 | 3 |
| 74 | 05-01-leakage-interpretability.vi.md:7 | "Do hệ số của một mô hình chỉ là một trong nhiều cách mô tả dữ liệu tốt như nhau, báo cáo không diễn giải hệ số nào thành nguyên nhân." | The logic leap (Rashomon effect leads to no causal reading) needs rereading | 3 |
| 75 | 05-02-causal-fairness-use.vi.md:3 | "Thời điểm gốc (time zero) của đợt thí điểm, tức mốc bắt đầu theo dõi chung cho mọi sinh viên, là thời điểm chốt dữ liệu, khi sinh viên bắt đầu đủ điều kiện vào danh sách" | Three appositions in one sentence; target-trial jargon unexplained | 2 |
| 76 | 05-02-causal-fairness-use.vi.md:5 | "Quy định này bảo đảm sinh viên bị đánh dấu có cơ hội chứng minh dự báo là sai" | Understood, but it sounds translated | 3 |
| 77 | 05-02-causal-fairness-use.vi.md:9 | "hiệu ứng dự báo tự tác động (performative prediction)" | Invented term; colleagues would say "dự báo tự ảnh hưởng" or keep the English | 3 |
| 78 | 06-00-genai-usage.vi.md:3 | "AI phản biện lựa chọn mô hình ... AI rà soát thiết kế đánh giá" | Role names used as proper nouns; this reads oddly throughout Phần 6 and Phụ lục VI | 3 |
| 79 | 06-00-genai-usage.vi.md:12 | "không dùng lập luận về dữ liệu mất cân bằng để ưu tiên đường cong độ chính xác – tỷ lệ phát hiện" | Negated decision inside a long cell; understood on the second pass | 3 |
| 80 | 06-00-genai-usage.vi.md:15 | "cách suy luận cho S1, căn cứ của S2, nhóm lượt đăng ký học dùng cho đánh giá chính, định nghĩa hiệu chuẩn, cách gộp kết quả khi chọn mô hình" | List of fragments that mean little without Bảng A.11 | 2 |
| 81 | 06-00-genai-usage.vi.md:19 | "giả sử tiêu chí thành công chỉ đòi hỏi mô hình vượt quy tắc dấu hiệu sớm ở ít nhất 9 trên 13 kỳ mở ..., thì tiêu chí đó vẫn được đáp ứng chỉ do ngẫu nhiên trong khoảng 13% trường hợp" | A counterfactual inside a "lesson"; I had to reread to see that it argues against a rejected criterion | 3 |
| 82 | 08-00-traceability.vi.md:3 | "cùng các ma trận sẵn sàng cho mô hình được lập từ hai bảng này, tức ma trận đầu vào có thể đưa thẳng vào mô hình" | Calque of "model-ready matrices"; the apposition only repeats the idea | 3 |
| 83 | 08-00-traceability.vi.md:14 | "qua câu hỏi cùng loại phân tích và bài toán kỹ thuật của câu hỏi" | "cùng" reads as "same" rather than "together with" | 2 |
| 84 | 10-01-candidate-comparison.vi.md:15 | "coi hiệu ứng của mỗi module là giá trị lấy từ phân phối chung của các module" | Understood, but it sounds translated | 3 |
| 85 | 10-01-candidate-comparison.vi.md:16 | "các nhánh chia thay đổi giữa các mẫu" | "Nhánh chia" for tree splits is unusual | 3 |
| 86 | 10-01-candidate-comparison.vi.md:17 | "dữ liệu có đủ mọi kỳ mở của các module này, nên hiệu ứng cố định phù hợp với thiết kế" | Same unexplained causal link as #19 | 2 |
| 87 | 10-01-candidate-comparison.vi.md:32 | "Kiểm duyệt không mang thông tin (non-informative censoring)" | "Kiểm duyệt" means censorship of content; for survival data colleagues say "dữ liệu bị chặn/bị cắt (censoring)" or keep the English | 2 |
| 88 | 10-01-candidate-comparison.vi.md:34 | "sự phụ thuộc chằng chịt giữa các thành phần (entanglement)" | Colourful, translated | 3 |
| 89 | 10-01-candidate-comparison.vi.md:40 | "Mô hình chỉ dùng đặc điểm cá nhân cho biết bao nhiêu phần của thứ hạng đến từ mức tham gia học tập, chứ không phải từ module và lịch sử học tập." | Reads backwards: a model with no activity data is said to show how much ranking comes from activity. It conflicts with Mục 3.3 ("phụ thuộc đến mức nào vào đặc điểm cá nhân"); I could not settle which is meant without the main text | 1 |
| 90 | 10-01-candidate-comparison.vi.md:50 | "Can thiệp được phân bổ ngẫu nhiên hoặc không bị gây nhiễu" | "Can thiệp ... không bị gây nhiễu" is a compressed calque (unconfounded) | 3 |
| 91 | 10-02-metric-definitions.vi.md:3 | "L là danh sách gồm k điểm rủi ro cao nhất" | A list of scores rather than of enrolments (4.1:63 says enrolments) | 3 |
| 92 | 10-03-validation-protocol.vi.md:14 | "ở cả vòng kiểm định chéo ngoài lẫn vòng trong" | Outer and inner loops appear here for the first time without introduction | 2 |
| 93 | 10-03-validation-protocol.vi.md:15 | "được tinh chỉnh bằng một vòng loại trừ từng kỳ mở bên trong" | Nested CV described in 8 words; I had to reread with the next row | 2 |
| 94 | 10-03-validation-protocol.vi.md:16 | "chênh lệch nằm trong biến thiên do lấy mẫu ít có ý nghĩa thực tế" | Missing a relative marker ("chênh lệch [mà] nằm trong ...") | 3 |
| 95 | 10-03-validation-protocol.vi.md:46 | "cũng vì lý do này, mô hình riêng cho từng module vẫn không phải lựa chọn tốt, do phép co hệ số không khắc phục được mẫu nhỏ" | "Lý do này" points back to transportability, but the reason given is small samples; the reference is unclear | 2 |
| 96 | 10-04-fairness-spec.vi.md:7 | "Kỳ mở nhỏ nhất của tập kiểm thử" (column) with "Nữ: 66; nam: 139" | The header suggests run size, but the values seem to be the group's count in the run where it is smallest; I had to guess | 2 |
| 97 | 10-04-fairness-spec.vi.md:22 | "Tỷ lệ của từng nhóm trong danh sách so với tỷ lệ của nhóm đó trong số sinh viên không hoàn thành" | Two "tỷ lệ của nhóm"; understood after rereading | 3 |
| 98 | 10-04-fairness-spec.vi.md:25 | "kèm giá trị tham chiếu, tức ABROCA khi nhãn nhóm được hoán vị ngẫu nhiên trong từng kỳ mở" | Permutation reference value in one clause; unclear on first pass | 2 |
| 99 | 10-04-fairness-spec.vi.md:25 | "riêng chỉ số này không bao giờ dẫn đến việc xem xét" | Means "this metric alone never triggers a review"; the word order makes it read as "this metric never leads to consideration" | 2 |
| 100 | 10-04-fairness-spec.vi.md:30 | "Cho thấy vị trí cắt tại hạng k tùy ý đến mức nào" | "Tùy ý đến mức nào" (how arbitrary) is translated and unclear | 2 |
| 101 | 10-05-risk-register.vi.md:12 | "các cờ suy ra từ biến mục tiêu nằm ngoài danh sách biến dự báo" | "Cờ" again; translated | 3 |
| 102 | 10-05-risk-register.vi.md:14 | "Điểm theo fold của cấu hình được chọn mang tính lạc quan" | Calque | 3 |
| 103 | 10-05-risk-register.vi.md:15 | "mô hình được hiệu chuẩn lại trên một kỳ mở sau" | Seems to contradict 4.3:22 ("không bao giờ được hiệu chuẩn lại trên các kỳ mở năm 2014"); "kỳ mở sau" is undefined (a later 2015 run?) | 1 |
| 104 | 10-05-risk-register.vi.md:16 | "Trung bình với CCC" | Terse residual-risk cell | 3 |
| 105 | 10-05-risk-register.vi.md:20 | "Quy tắc diễn đạt theo mối liên hệ, kèm rà soát văn bản" | Compressed; meaning (wording rule) only guessable | 3 |
| 106 | 10-05-risk-register.vi.md:27 | "Đánh giá sự phù hợp trước khi sử dụng" | Legal term (conformity assessment) with no gloss | 3 |
| 107 | 10-06-ai-critiques.vi.md:10 | "để chấm điểm các kỳ mở B năm 2014" | In an education text "chấm điểm" means grading; here it means scoring with the model | 2 |
| 108 | 10-06-ai-critiques.vi.md:15 | "Fail không phải kết quả dạng thời gian đến sự kiện; kiểm duyệt không mang thông tin được nêu là một giả định" | Two survival-analysis ideas in a table cell, with "kiểm duyệt" again | 2 |
| 109 | 10-06-ai-critiques.vi.md:33 | "Hiệu chuẩn tổng thể có offset; ngưỡng áp dụng cho ước lượng gộp; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở sau" | Fragments; "có offset" untranslated | 2 |
| 110 | 10-06-ai-critiques.vi.md:34 | "loại ở mọi vòng" | Too terse (exclude what, in which loops?) | 3 |
| 111 | 10-07-traceability-full.vi.md:9 | "enrolment, assessment_due" | Raw table names in a Vietnamese table, never explained | 3 |
| 112 | 10-07-traceability-full.vi.md:11–12 | "model_ready", "capacity_by_run" | Raw table names never introduced anywhere in the Vietnamese text | 2 |

Counts: clarity 1 = 2; clarity 2 = 52; clarity 3 = 58; total 112.

## Recurring terms that feel invented or unnatural

| Term in the report | Count | What it seems to mean | Plainer word a colleague would use |
| :-- | :-- | :-- | :-- |
| kỳ mở (module run) | 362 | one offering of a module | "đợt mở lớp", "khóa (presentation)" or "lớp học phần"; at minimum use "kỳ" alone after the first mention |
| lượt đăng ký học | 85 | enrolment record (student × run) | "lượt ghi danh" or "bản ghi đăng ký"; many colleagues just say "sinh viên" once the unit is defined |
| hạn mức liên hệ | 37 | contact capacity | "năng lực liên hệ" or "số sinh viên liên hệ được (k)" |
| kiểm định khẳng định | 19 | confirmatory (pre-registered) test | "kiểm định xác nhận" or "kiểm định chính (đã đăng ký trước)" |
| tỷ lệ phát hiện chuẩn hóa / tỷ lệ phát hiện trong giới hạn danh sách | 18 / 13 | normalised recall@k / recall@k | "recall@k (chuẩn hóa)"; "độ nhạy tại k" |
| danh sách dài k | 17 | top-k list | "danh sách top-k" or "k sinh viên đứng đầu" |
| độ chính xác của danh sách | 17 | precision@k | "precision@k" or "độ chính xác dương tại k"; "độ chính xác" alone means accuracy |
| điều kiện đạt | 16 | pass criterion | "tiêu chí đạt" or "ngưỡng chấp nhận" |
| cây tăng cường độ dốc | 13 | gradient boosting | "gradient boosting" (kept in English by almost everyone) |
| mô hình đối sánh | 12 | challenger model | "mô hình thách thức (challenger)" or "mô hình so sánh" |
| biến thay thế | 10 | proxy variable | "biến đại diện (proxy)"; "biến thay thế" suggests a substitute or imputed variable |
| hiệu chỉnh phạt (hồi quy logistic có ~) | 9 | penalised / regularised logistic regression | "hồi quy logistic có điều chuẩn (regularization)" |
| mức vượt tỷ lệ nền | 8 | lift | "lift" or "hệ số nâng" |
| phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 | 5 | labels-available sensitivity variant | a short name such as "phương án B-2013" after the first definition |
| kiểm duyệt (không mang thông tin) | 2 | censoring | "dữ liệu bị chặn (censoring)" or keep "censoring" |
| dự báo tự tác động | 2 | performative prediction | "dự báo tự ảnh hưởng" or keep the English |
| lập bản đồ (NIST Map) | 2 | identify context and risks | "nhận diện (Map)" |

The five terms that hurt most: "kỳ mở" (sheer frequency, 362), "kiểm định khẳng định" (misleading calque), "độ chính xác của danh sách" (clashes with accuracy), "tỷ lệ phát hiện trong giới hạn danh sách / chuẩn hóa" (long and heavy where recall@k is the norm), "biến thay thế" (suggests the wrong concept).
