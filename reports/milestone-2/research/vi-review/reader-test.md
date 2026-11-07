# Reader test – Vietnamese version of the Milestone 2 report

Reader: Vietnamese-native data-analytics lecturer marking the report, who has never seen the source-language version.
Files read (in file-name order): `00-1-abbreviations.vi.md`, `00-2-glossary.vi.md`, `01-00` to `09-00` `*.vi.md` in
`reports/milestone-2/report/`. Evidence codes and citations in square brackets were ignored. No other file was opened.
Date: 2026-11-06.

## Overall judgement

Yes, a reader of the field could explain the document afterwards: what the four questions need, why OULAD was chosen
over six other candidates, how it was collected and checked, and which parts of each question it cannot answer. The
Vietnamese is grammatical and mostly fluent; the argument holds together section by section. What costs the reader time
is not grammar but density and a handful of invented or overloaded terms. The hardest stretches are the leakage table
(Bảng 2.3, last row), the structural-verification paragraph that turns counts into gate decisions (06-00:19), and the
short G3 limitation in 7.2, where module/start-month/training-run logic is packed into one clause. Three term problems
recur: "học phần" is used both for the Vietnamese university course and for the OULAD module (the glossary even has to
warn about it), "tổng hợp" means "aggregated" in Sections 3–4 but "synthetic" in Section 9, and "độ chính xác" stands
for both precision and accuracy. The phrase "số sinh viên cán bộ liên hệ được (mỗi tuần)" is repeated nine times where
one defined word ("năng lực liên hệ", "sức liên hệ") would do. The writing also uses English sentence frames in places
("chính các câu hỏi, chứ không phải dữ liệu, quyết định…", "Đặt hai mục này cạnh nhau cho thấy…"), which read as
translated but rarely block understanding. One content point surfaced while reading: 04-02:19 says the OULAD failure
rate is "nhiều khả năng cao hơn", while 08-00:17–18 states flatly that it "cao hơn"; and 04-01:6 describes G1 as "ngày
ghi nhận kết quả" while 02-01:17 defines G1 as the withdrawal date.

Counts: clarity 1 = 3 passages, clarity 2 = 33 passages, clarity 3 = 26 passages (62 in total).

## Passages

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 00-1-abbreviations.vi.md:12 | "MD5 \| Message Digest 5 \| Mã kiểm tra do nhà cung cấp đưa ra và được ghi trong manifest" | No Vietnamese expansion (other rows have one); "manifest" untranslated and never explained | 3 |
| 2 | 00-2-glossary.vi.md:12 | "Một lần mở một module của OULAD, … "học phần" chỉ học phần của trường" | The entry for "đợt mở học phần" itself uses "học phần" for the OULAD module, then says "học phần" means the university's course: the term contradicts its own definition | 2 |
| 3 | 01-01-frozen-baseline.vi.md:3 | "vì chính các câu hỏi, chứ không phải dữ liệu, quyết định cần thu thập những gì" | English cleft structure; "quyết định" is used as a noun (D1–D3) everywhere else, so I first read it as a noun here | 2 |
| 4 | 01-01-frozen-baseline.vi.md:5 | "Business Goal (mục tiêu của tổ chức)" | Untranslated head term inside a Vietnamese sentence; the gloss is fine but the English stays as the working term throughout | 3 |
| 5 | 01-01-frozen-baseline.vi.md:5 | "KPI phụ 1 là tỷ lệ liên hệ sinh viên có dấu hiệu sớm; KPI phụ 2 là tỷ lệ liên hệ kịp thời" | Unclear head noun: does "sớm" attach to "dấu hiệu" or to "liên hệ"? Rate of what over what (denominator missing)? I guessed: share of flagged students who are contacted, and share contacted within the deadline | 2 |
| 6 | 01-01-frozen-baseline.vi.md:5 | "giống cách Thông tư 83/2026 của Việt Nam thống kê số sinh viên thôi học" | "của Việt Nam" after a circular number sounds translated; a Vietnamese writer would name the issuing ministry | 3 |
| 7 | 01-01-frozen-baseline.vi.md:13 | "D2; các lý do hiển thị trong D1" | "lý do hiển thị" – reasons displayed where? I guessed: the reasons printed next to each name on the list | 2 |
| 8 | 01-01-frozen-baseline.vi.md:14 | "có thể dự báo đúng đến mức nào …, so với quy tắc đơn giản" | Which simple rule? Never named here or later; I guessed a baseline rule such as "missed a graded assessment" | 2 |
| 9 | 01-01-frozen-baseline.vi.md:15 | "trong giới hạn số sinh viên cán bộ liên hệ được mỗi tuần và yêu cầu công bằng" | Long noun chain standing in for "capacity"; "yêu cầu công bằng" undefined | 3 |
| 10 | 01-02-scope-change-log.vi.md:5 | "Thứ nhất, tổng thể thay đổi:" | "tổng thể" (population) as a bare subject reads abruptly; "tổng thể nghiên cứu" would be natural | 3 |
| 11 | 01-02-scope-change-log.vi.md:5 | "phần hành động của AQ4 vẫn là yêu cầu dành cho đợt thí điểm, vì không bộ dữ liệu mở nào ghi nhận phần này" | "phần hành động" is an invented label; "vẫn là yêu cầu dành cho" means it is deferred, but I worked that out only at 7.2 | 2 |
| 12 | 01-02-scope-change-log.vi.md:5 | "các thay đổi này chỉ thu hẹp mức độ mà từng câu hỏi trả lời được trên dữ liệu mở" | Source-language order; understood | 3 |
| 13 | 02-00-data-requirements.vi.md:3 | "Các yêu cầu được phát biểu bằng khái niệm, không dùng tên cột" | "phát biểu bằng khái niệm" sounds translated ("ở mức khái niệm") | 3 |
| 14 | 02-01-aq-data-matrix.vi.md:10 | "tuần sinh viên lần đầu bỏ lỡ bài được chấm điểm, ở cả hai nhóm" | Which two groups? Never named; I guessed completers vs non-completers. Same at 07-01:10 | 1 |
| 15 | 02-01-aq-data-matrix.vi.md:11 | "Chênh lệch tỷ lệ sinh viên về sau không hoàn thành học phần giữa sinh viên có và không có từng dấu hiệu" | Too many ideas in one noun phrase (difference of rates, later non-completion, with/without each signal) | 2 |
| 16 | 02-01-aq-data-matrix.vi.md:12 | "thông tin nền có tại thời điểm đăng ký" | "thông tin nền" is invented for background/demographic data; first use, not defined | 3 |
| 17 | 02-01-aq-data-matrix.vi.md:13 | "Tỷ lệ phát hiện (recall) và độ chính xác của danh sách (precision)" | "độ chính xác" is precision here but accuracy at 02-02:11 and 02-02:16; the reader cannot tell which metric later sentences mean | 2 |
| 18 | 02-01-aq-data-matrix.vi.md:15 | "những vế câu hỏi dựa vào các biến đó chuyển sang mức đáp ứng một phần (Partial)" | "vế câu hỏi" is unusual; "chuyển sang mức" sounds translated | 3 |
| 19 | 02-01-aq-data-matrix.vi.md:15 | "sáu điều kiện bắt buộc …, từ G1 đến G5, trong đó G2 gồm hai phần" | Six gates numbered one to five; resolved by the next clause but stops the eye | 3 |
| 20 | 02-01-aq-data-matrix.vi.md:20 | "có một đợt muộn hơn để kiểm thử" | "kiểm thử" is software-testing vocabulary; "đánh giá (trên tập kiểm tra)" expected | 3 |
| 21 | 02-02-requirements-by-level.vi.md:10 | "kèm thông tin nền để kiểm tra độ nhất quán giữa các nhóm" | Consistency of what between which groups? I guessed: whether the association holds in each subgroup | 2 |
| 22 | 02-02-requirements-by-level.vi.md:11 | "đủ số học kỳ để đánh giá trên một học kỳ sau" / "Độ chính xác trên một học kỳ sau, với độ dài danh sách cố định" | "một học kỳ sau" (a later, held-out semester) is not explained; "độ chính xác" here is accuracy, not the precision of 02-01:13 | 2 |
| 23 | 02-02-requirements-by-level.vi.md:14 | "thay vì đưa ra một khuyến nghị dưới danh nghĩa phân tích chỉ định" | Understood; "dưới danh nghĩa" sounds translated ("gọi là") | 3 |
| 24 | 02-02-requirements-by-level.vi.md:16 | "chỉ để kiểm tra mức độ liên quan và độ chính xác có giữ được giữa các nhóm hay không" | Fairness check phrased obliquely; "giữ được giữa các nhóm" took a second reading | 2 |
| 25 | 02-02-requirements-by-level.vi.md:16 | "mức thiếu thốn của khu vực sinh viên cư trú" | Invented rendering of the deprivation index; "mức độ khó khăn kinh tế – xã hội của khu vực" is what we say | 3 |
| 26 | 02-02-requirements-by-level.vi.md:16 | "Các dữ liệu này chỉ được dùng để hỗ trợ sinh viên …, không bao giờ dùng để chấm điểm" | "chấm điểm": grading the student, or risk scoring? Ambiguous in a report about scoring models | 2 |
| 27 | 02-03-prediction-point-leakage.vi.md:3 | "những trường nào sẽ làm rò rỉ thông tin từ sau thời điểm chốt dữ liệu" | "trường" (field) vs "trường" (university) both occur in this report; understood from context | 3 |
| 28 | 02-03-prediction-point-leakage.vi.md:11 | "Giá trị trung bình theo học phần, phép chuẩn hóa thang đo và phép mã hóa chỉ được ước lượng trên các học kỳ huấn luyện" | "phép mã hóa" (encoding) and "học kỳ huấn luyện" (training semesters) are invented; three technical ideas in one cell | 2 |
| 29 | 02-03-prediction-point-leakage.vi.md:11 | "được ước lượng trên tất cả các học kỳ hoặc trên toàn bộ học kỳ" | I could not tell "tất cả các học kỳ" from "toàn bộ học kỳ"; presumably "across all semesters incl. test" vs "over the whole semester incl. after the cut-off", but the words do not say so | 1 |
| 30 | 02-03-prediction-point-leakage.vi.md:13 | "bảo đảm lần rút học phần của sinh viên không bị tính thành dấu hiệu báo trước chính lần rút đó" | Circular-sounding; needed rereading to see the point (withdrawal causing "missed" work) | 2 |
| 31 | 02-03-prediction-point-leakage.vi.md:13 | "sinh viên đã rời học phần trước thời điểm chốt dữ liệu không được tính là sinh viên mà danh sách phát hiện được" | Double negative + relative clause; "rời" vs "rút" switch; I read it twice to see they are excluded from recall | 2 |
| 32 | 03-00-search-strategy.vi.md:4 | "loại các bản tải lại không rõ nguồn gốc dữ liệu" | "bản tải lại" (re-upload) sounds like "re-download"; I guessed right from context | 3 |
| 33 | 03-00-search-strategy.vi.md:6 | "bản sao của một bài mô tả dữ liệu nhóm đã có, địa chỉ cũ đã được thay thế, bản tải lại dữ liệu KDD Cup 2015 của bên thứ ba và metadata thứ cấp" | Four excluded categories in one breath; KDD Cup 2015 and "metadata thứ cấp" are not explained | 2 |
| 34 | 03-00-search-strategy.vi.md:15 | "Đơn vị phân tích: Bảng hỏi" | A questionnaire is not a unit of analysis; I guessed "one survey response per student" | 2 |
| 35 | 04-01-criteria-gates.vi.md:3 | "khả năng xử lý chất lượng dữ liệu" | Criterion name is opaque: ability of whom to handle what? I guessed "data-quality issues are manageable" | 2 |
| 36 | 04-01-criteria-gates.vi.md:3 | "mức sẵn có và thời điểm có của các biến giải thích" | "thời điểm có" is a translated frame (when the variable becomes available) | 3 |
| 37 | 04-01-criteria-gates.vi.md:6 | "G1 bảo đảm có biến kết quả và ngày ghi nhận kết quả" | Contradicts 02-01:17, where G1 requires the withdrawal date, not a result date; I had to go back | 2 |
| 38 | 04-02-selection-matrix.vi.md:3 | "Ma trận thể hiện tám trong mười tiêu chí theo các cột của đề bài. Tổng điểm còn gồm hai tiêu chí còn lại là đơn vị phân tích và độ chi tiết cùng phạm vi thời gian" | Table shows six columns, so I had to count split cells to reach eight; "cùng" (= "và") made me read "đơn vị… cùng phạm vi" as one criterion | 2 |
| 39 | 04-02-selection-matrix.vi.md:17 | "UCI 697 gán nhãn tình trạng theo chương trình đào tạo cho sinh viên vào cuối năm thứ ba hoặc thứ tư" | Word order hides the point: the label is a programme-level status recorded only at year 3–4, so there is no course-level outcome | 2 |
| 40 | 04-02-selection-matrix.vi.md:17 | "OULAD được chọn vì đây là bộ dữ liệu ứng viên duy nhất có tài liệu đáp ứng điều kiện về mốc thời gian và giấy phép, đồng thời ghi nhận ngày rút học phần" | Long, translated sentence order; understood | 3 |
| 41 | 05-00-acquisition-provenance.vi.md:15 | "kích thước và mã SHA-256 được đối chiếu với giá trị tham chiếu ghi sẵn" | Recorded beforehand by whom and where? "ghi sẵn" leaves the source of the reference value unclear | 2 |
| 42 | 05-00-acquisition-provenance.vi.md:17 | "được ghi trong manifest" | "manifest" untranslated and undefined (also 00-1:12, 05-00:22) | 3 |
| 43 | 05-00-acquisition-provenance.vi.md:20 | "thấy bảy bảng của hai bản có các dòng dữ liệu giống nhau. Khác biệt duy nhất nằm ở năm bảng" | "all seven identical" then "differences in five" reads as a contradiction until you reach the "?" explanation | 2 |
| 44 | 06-00-structural-verification.vi.md:3 | "Mỗi bảng được đọc ở dạng văn bản để không giá trị nào bị chuyển đổi" | Means "read every column as text/string"; translated phrasing | 3 |
| 45 | 06-00-structural-verification.vi.md:13 | "ngày đăng ký từ −322 đến 167; ngày hủy đăng ký từ −365 đến 444" | Negative days are not explained in this section (only in the glossary and at 7.1); a reader of the table alone is puzzled | 3 |
| 46 | 06-00-structural-verification.vi.md:17 | "thiếu dòng tương ứng ở bảng cha" | "bảng cha" is database jargon; understood | 3 |
| 47 | 06-00-structural-verification.vi.md:19 | "Các giá trị kết quả phân biệt được đạt và đạt loại giỏi với trượt và rút học phần." | "phân biệt được A và B với C và D" parses badly; I first read "đạt và đạt loại giỏi" as being distinguished from each other | 2 |
| 48 | 06-00-structural-verification.vi.md:19 | "Ở cả 1.309 trường hợp học lại cùng một module, số lần học trước đó đều tăng lên, nên mã sinh viên được giữ nguyên" | Logical step skipped: the reader must infer that a rising prior-attempt count proves the same ID is the same person | 2 |
| 49 | 06-00-structural-verification.vi.md:19 | "mỗi module có tối đa một đợt trước và một đợt sau có cùng tháng bắt đầu" | Dense; "trước/sau" relative to what (train/test)? Understood only after 7.2 | 2 |
| 50 | 06-00-structural-verification.vi.md:19 | "3.097 lượt đăng ký học phần kết thúc vào hoặc trước ngày 0, còn 28.119 lượt vẫn duy trì đăng ký đến ngày 14" | Numbers given with no purpose; the link to the KPI denominator appears only at 07-01:18 | 2 |
| 51 | 07-01-traceability.vi.md:1 | "Ma trận truy vết cập nhật" | "cập nhật" after a noun reads as a verb ("update the matrix"); "đã cập nhật" needed | 3 |
| 52 | 07-01-traceability.vi.md:12 | "đánh giá trên các đợt mở năm 2014 của 9 cặp module và tháng bắt đầu (C07)" | "cặp module và tháng bắt đầu" is a new unit introduced inside a table cell; the 9 is not derivable from the text | 2 |
| 53 | 07-01-traceability.vi.md:19 | "theo yêu cầu của sản phẩm bàn giao B trong đề bài [1] (Bảng A.10)" | "sản phẩm bàn giao B" unexplained; "Bảng A.10" does not match the appendix numbering (Phụ lục V) | 2 |
| 54 | 07-02-gaps-revisions.vi.md:5 | "một câu hỏi chỉ định chưa có bằng chứng về hành động được giữ làm yêu cầu cho quyết định trong tương lai; nhận định rút ra từ câu hỏi đó ở mức thận trọng hơn" | Abstract restatement of the brief's rule; subject and what "thận trọng hơn" compares to are unclear | 2 |
| 55 | 07-02-gaps-revisions.vi.md:13 | "mỗi cặp module và tháng bắt đầu có nhiều nhất một đợt mở trước đó để huấn luyện; CCC và các đợt mở tháng 2 của EEE và GGG không có đợt nào" | Too many ideas at once; "không có đợt nào" – no training run? no test run? I could not settle it on the page | 1 |
| 56 | 08-00-risks-ethics.vi.md:4 | "Do đó, nhóm … chỉ sử dụng dữ liệu trong phạm vi các điều kiện về quyền riêng tư và đạo đức; bản thân dữ liệu cũng giới hạn những kết luận có thể rút ra." | "Do đó" does not follow from the previous sentence; two unrelated points joined by a semicolon | 3 |
| 57 | 08-00-risks-ethics.vi.md:12 | "Dữ liệu chỉ được lưu trên máy của các thành viên nhóm theo giấy phép CC BY 4.0" | Reads as if the licence requires local storage; I guessed two separate facts (stored locally; used under CC BY 4.0) | 2 |
| 58 | 08-00-risks-ethics.vi.md:27 | "thay vì được sửa âm thầm" | Translated idiom; "tự ý sửa mà không ghi nhận" is what we say | 3 |
| 59 | 09-00-genai-reflection.vi.md:3 | "hỗ trợ Milestone này ở bốn trong số các vai trò mà đề bài cho phép" | Translated frame; understood | 3 |
| 60 | 09-00-genai-reflection.vi.md:11 | "Một tác tử AI làm việc cho nhóm" | "tác tử" is a rare academic coinage for "agent"; many colleagues would not recognise it | 3 |
| 61 | 09-00-genai-reflection.vi.md:17 | "vẫn có thể vượt qua các điều kiện bắt buộc đầu tiên" | "đầu tiên" – the first gates in the list, or an earlier version of the gates? I guessed the latter | 2 |
| 62 | 09-00-genai-reflection.vi.md:21 | "nhóm chỉ còn dữ liệu tổng hợp (synthetic)" | "tổng hợp" means aggregated in 03-00:13, 03-00:17, 04-02:17; here it means synthetic. Only the English in brackets saved me; plain Vietnamese is "dữ liệu giả lập / mô phỏng" | 2 |

## Recurring terms that feel invented or unnatural

Counts are occurrences across the abbreviation and terms pages plus Sections 1–9 (`grep -o -i`, case-insensitive).

| Term | Count | Problem | Plainer word a colleague would use |
| :-- | :-- | :-- | :-- |
| số sinh viên cán bộ liên hệ được (mỗi tuần) | 9 | Clause used as a noun for "capacity"; heavy every time | năng lực liên hệ (mỗi tuần), số lượt liên hệ tối đa |
| học phần (for the OULAD module) / đợt mở học phần | 27 (đợt mở học phần); "module" 25 | Same word for the university course and the OULAD module; glossary must warn | module / lượt mở module (keep "học phần" for the university only) |
| tổng hợp (aggregated vs synthetic) | 4 | One word, two meanings | số liệu gộp (aggregated); dữ liệu giả lập (synthetic) |
| độ chính xác (precision vs accuracy) | 6 | One word, two metrics | precision → độ chính xác của danh sách / tỷ lệ đúng trong danh sách; accuracy → độ chính xác tổng thể; or keep English |
| bài được chấm điểm | 14 | Passive, long; reads translated | bài đánh giá (tính điểm), bài kiểm tra |
| thông tin nền | 7 | Invented for background/demographics | thông tin nhân khẩu học, đặc điểm cá nhân |
| nhóm phân tích dữ liệu (as "the team") | 15 | Repeated full label where "nhóm" suffices | nhóm |
| mức thiếu thốn (của khu vực cư trú) | 4 | Literal "deprivation" | mức độ khó khăn kinh tế – xã hội của khu vực |
| bài mô tả dữ liệu | 15 | Acceptable but "bài" alone is vague | bài báo mô tả bộ dữ liệu |
| phần hành động (của AQ4) | 2 | Invented label | phần can thiệp / phần về việc liên hệ |
| Business Goal | 4 | Untranslated working term | mục tiêu của đơn vị / mục tiêu kinh doanh |
| manifest | 3 | Untranslated, undefined | tệp kê khai (danh sách tệp và mã kiểm tra) |
| tác tử (AI) | 2 | Rare coinage | AI agent / trợ lý AI |
| kiểm thử | 1 | Software term | đánh giá trên tập kiểm tra |
| cặp module và tháng bắt đầu | 2 | New unit introduced without definition | nhóm module cùng tháng khai giảng |
