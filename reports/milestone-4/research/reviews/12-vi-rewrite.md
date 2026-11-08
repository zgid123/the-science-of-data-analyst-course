# Vietnamese rewrite after reader test 2 – Milestone 4, 2026-11-08

Stage 5 of build-report reference.md section 4.3: every flag of `reader-test-2.md` (112 passages; the reader saw only the Vietnamese) was checked against the current twin, then fixed from the English source or rejected with a reason. The reader read while the fidelity review (`fidelity-2026-11-08.md`) was still editing, so each quote was first compared with the current text. In the same pass the twins of the three English files changed today were synced (04-01, 10-04, 10-05), and two settled terms were applied in every twin: "biến đại diện (proxy)" for proxy (no "biến thay thế" left) and "tính điểm rủi ro" for model scoring (no "chấm điểm" left outside graded assessments).

Method: every twin was copied to the session scratchpad before editing (`m4-rewrite2/`). Edits were applied by `rewrite-2-2026-11-08-scripts/apply.py`, one edit file per twin in `edits/`, plus three follow-up files (`edits2-fixwarn*.py` for two parity warnings and one read-aloud fix, `edits3-abbrev*.py` for three abbreviation violations); each before-string must occur exactly once or the run aborts before writing. `show.py STEM LINE…` prints the English and Vietnamese units side by side; every rewritten sentence was compared with its English unit for meaning, numbers, conditions, hedges, citations and cross-references. `twins.diff` holds the before/after diff of the 27 edited twins. Paths below are relative to `reports/milestone-4/report/`; line numbers are those of the reader test.

## Result

| Status | Count | Flags |
| :---- | :---- | :---- |
| Fixed | 108 | all others |
| Already fixed (by the fidelity review before this pass) | 1 | 35 |
| For the native user (protected term kept; sentence reworded or the English added) | 2 | 4, 45 |
| Rejected with reason | 1 | 77 |

## Flags

| # | Flag | Status | Change or reason |
| :-- | :-- | :-- | :-- |
| 1 | 00-2:12 two stacked "của" in calibration slope | Fixed | "Hệ số đứng trước log-odds của điểm rủi ro khi hiệu chuẩn lại bằng mô hình logistic, tức hồi quy logistic biến kết quả theo log-odds đó" |
| 2 | 00-2:14 "offset" unexplained | Fixed | "log-odds của điểm rủi ro được đưa vào làm offset (số hạng có hệ số cố định bằng 1)", as in Bảng A.4 |
| 3 | 00-2:23 labels-available name vs meaning | Fixed | Glossary name kept; cell adds the link: "vì đây là các kỳ mở đã có kết quả (nhãn) vào thời điểm đó" (glossary Usage: first use adds why) |
| 4 | 00-2:33 "độ chính xác của danh sách dài k" read as accuracy | For native user | Protected metric name kept; the terms-page row already opens with the English "Precision at capacity". Reader proposes "precision@k" or "độ chính xác dương tại k" |
| 5 | 00-2:37 sign-flip test, head noun lost | Fixed | "Kiểm định giả sử dấu của chênh lệch ở mỗi kỳ mở là ngẫu nhiên, rồi ước lượng tần suất thu được một tập chênh lệch theo kỳ mở có lợi không kém tập chênh lệch quan sát được" |
| 6 | 01-01:7 "hai câu hỏi" unnamed | Fixed | "điều chỉnh cách đo của hai câu hỏi AQ3 và AQ4, qua hai định nghĩa trình bày ở cuối mục này" (the two are C10, AQ3's comparison rule, and C13, AQ4's list measure; see "For the lead") |
| 7 | 01-01:16 compressed AQ2 decision cell | Fixed | "D2 và lý do cụ thể hiển thị cạnh từng tên trong danh sách liên hệ (D1)" |
| 8 | 01-01:20 "so danh sách với tỷ lệ nền" | Fixed | "so tỷ lệ sinh viên không hoàn thành trong danh sách với tỷ lệ nền của kỳ mở, tức tỷ lệ … trong toàn kỳ mở" |
| 9 | 01-02:3 enrolments then students in one count | Fixed | "các kỳ mở phát triển có 12.080 lượt đăng ký học, trong đó 5.519 lượt không hoàn thành; tập kiểm thử có 15.989 lượt đăng ký học" |
| 10 | 01-02:13 "phép biến đổi được ước lượng" | Fixed | "tham số của các phép biến đổi dữ liệu chỉ được ước lượng từ các kỳ mở năm 2013" (glossary "fitted transform") |
| 11 | 02-00:3 "bản mô tả AQ Modeling Brief" | Fixed | "bốn AQ Modeling Brief" |
| 12 | 02-01:3 "lớp" | Fixed | "nhãn lớp" |
| 13 | 02-01:46 alternative to what | Fixed | "Ngoài ra, bộ biến dự báo mở rộng được thử làm phương án thay thế: bộ này bổ sung vào các biến dự báo chính 10 biến … và số lượt nhấp của từng tuần" (03-03: "the extended set adds") |
| 14 | 02-01:48 transportability | Fixed | "khả năng tổng quát hóa sang kỳ mở diễn ra sau" |
| 15 | 02-01:65 "mức mà hạn mức" | Fixed | "với số tên đúng bằng hạn mức liên hệ" (protected term kept) |
| 16 | 02-02:3 Shmueli vs brief | Fixed | Third purpose in its own sentence; "theo cách phân loại của Shmueli, … là mô hình mô tả [3]. Đề bài dùng một cách xếp loại khác: …; Vì vậy, theo cách xếp loại của đề bài, AQ2 vẫn là câu hỏi chẩn đoán" |
| 17 | 02-02:10 "mô hình sống sót" | Fixed | Glossary term kept with an anchor: "Mô hình sống sót thời gian rời rạc, một dạng phân tích sống sót (survival analysis)" |
| 18 | 03-01:13 "mẫu số thứ hai" before its meaning | Fixed | "tỷ lệ tính lại trên mọi lượt đăng ký học, không chỉ các lượt còn hiệu lực tại ngày 14 (mẫu số thứ hai)" |
| 19 | 03-01:14 fixed-effects reasoning missing | Fixed | "…, tức các kỳ mở được quan sát đầy đủ chứ không phải được lấy mẫu, nên hiệu ứng cố định là phù hợp" (03-02 states the reason) |
| 20 | 03-01:15 dense choice cell | Fixed | Two sentences: "Ứng viên 1 với các biến dự báo chính. Ứng viên 2 hoặc bộ biến dự báo mở rộng chỉ được chọn khi vượt Ứng viên 1 ít nhất một mức chênh lệch đã ấn định trước" |
| 21 | 03-01:15 events per parameter terse | Fixed | "số sự kiện trên mỗi tham số cao, tức mỗi tham số ứng với nhiều sinh viên không hoàn thành" |
| 22 | 03-02:5 repeated phrase | Fixed | Joined: "…phụ thuộc vào cách xác định phạm vi dữ liệu; đây là nguyên nhân chủ yếu khiến một tỷ lệ mô tả có thể gây hiểu sai" |
| 23 | 03-02:9 fixed-effects logic late | Fixed | Reason first: "Dữ liệu có mọi kỳ mở …, tức các kỳ mở được quan sát đầy đủ chứ không phải được lấy mẫu; hiệu ứng cố định phù hợp với thiết kế như vậy." and "Vì các kỳ mở không được lấy mẫu, mô hình dùng sai số chuẩn vững …" |
| 24 | 03-02:9 three "chênh lệch" | Fixed | "Hiệu ứng riêng phần nhỏ hơn chênh lệch đo được khi xét riêng dấu hiệu đó. Ngoài ra, hiệu ứng riêng phần không phải là tỷ trọng của tình trạng không hoàn thành mà dấu hiệu đó giải thích được." |
| 25 | 03-02:9 "tất định" rare | Fixed | Glossary term kept with a gloss: "tất định (chạy lại luôn cho cùng kết quả)" |
| 26 | 03-03:5 "khi bằng số dấu hiệu" | Fixed | "nếu hai sinh viên có cùng số dấu hiệu, sinh viên có tỷ lệ hoạt động thấp hơn được xếp trước" |
| 27 | 03-03:7 19 → 23 parameters | Fixed | "Module và tháng bắt đầu là biến phân loại, nên mỗi biến đi vào mô hình dưới dạng nhiều số hạng (biến giả); vì vậy, 19 biến dự báo tương ứng với tổng cộng 23 tham số" |
| 28 | 03-03:7 de-duplicated clicks periphrasis | Fixed | "số lượt nhấp sau khi loại các bản ghi trùng lặp hoàn toàn" (same wording in the AQ2 error-analysis cell of 04-01) |
| 29 | 03-03:7 paragraph overloaded | Fixed | Extended set moved to its own paragraph: "Ngoài bộ biến dự báo chính, nhóm tác giả thử một phương án thay thế là bộ biến dự báo mở rộng (Bảng 2.3). Bộ này giữ các biến dự báo chính và bổ sung 10 biến: …" |
| 30 | 03-03:9 "hai lớp nhãn có cỡ gần nhau" | Fixed | "số lượt hoàn thành và số lượt không hoàn thành gần cân bằng: 44–46% lượt đăng ký học không hoàn thành" |
| 31 | 03-03:13 benchmark caveat order | Fixed | "nghiên cứu so sánh (benchmark) đưa ra kết quả này đã loại bỏ trước những bộ dữ liệu mà trên đó hồi quy logistic chỉ kém mô hình tốt nhất không quá 5%. Do các bộ dữ liệu có lợi cho hồi quy logistic đã bị loại, nghiên cứu đó không chứng minh …" |
| 32 | 03-03:13 "ở mức trung bình" ambiguous | Fixed | "chỉ cải thiện hiệu chuẩn khi tính trung bình trên nhiều trường hợp, chứ không chắc chắn trong từng trường hợp cụ thể" |
| 33 | 03-04:3 "trên mỗi 20" | Fixed | "trong mỗi 20 sinh viên, nhóm thứ nhất gồm 3 sinh viên có nguy cơ cao nhất, nhóm thứ hai gồm 2 sinh viên kế tiếp" |
| 34 | 03-04:7 purpose clause, no subject | Fixed | "muốn ước lượng tác động của can thiệp khác nhau thế nào giữa các cá nhân, nhà phân tích cần dữ liệu về can thiệp được phân bổ ngẫu nhiên hoặc dữ liệu không bị yếu tố gây nhiễu làm sai lệch [9]" |
| 35 | 04-00:3 "được tính trên …, là …" | Already fixed | Fidelity review #8 rewrote it ("dựa trên đường cong … (ROC): đó là …"). "Đường cong đặc trưng hoạt động của bộ thu" stays: it is the standard Vietnamese name and the abbreviation check requires the full form of ROC |
| 36 | 04-00:3 20-word name mid-sentence | Fixed | Name moved to the end of a shorter sentence: "Với các mô hình dự báo xây dựng bằng hồi quy hoặc học máy, chuẩn báo cáo hiện hành là Hướng dẫn … (TRIPOD+AI)"; the full form stays (abbreviation rule) |
| 37 | 04-01:14 word order, "tách theo kết quả" | Fixed | "Tỷ lệ cộng dồn các lượt đăng ký học đã bỏ lỡ bài được chấm điểm đầu tiên, tính đến từng tuần và tách theo kết quả cuối cùng" |
| 38 | 04-01:16 "cờ" | Fixed | "138 lượt đăng ký học bị đánh dấu thiếu ngày rút khỏi module hoặc thiếu ngày đăng ký" (also in the error-analysis cell) |
| 39 | 04-01:31 fragments without verbs | Fixed | "Tính phần dư trung bình theo khoảng giá trị dự báo (binned residuals) cho từng kỳ mở và từng mức hoạt động. Đo tương quan giữa các dấu hiệu được tính từ lượt nhấp." |
| 40 | 04-01:41 "tổng mức tối đa" | Fixed | "chia cho tổng số sinh viên không hoàn thành mà các danh sách đó có thể chứa nhiều nhất; mỗi danh sách chứa được nhiều nhất k … (hoặc toàn bộ … nếu số này nhỏ hơn k)" = Σ min(k, \|Y\|) of Bảng A.4 |
| 41 | 04-01:42 "số dương tính thật" | Fixed | "cả ba chỉ số đều được tính từ cùng một con số: số sinh viên không hoàn thành có tên trong danh sách" |
| 42 | 04-01:42 "chỉ dùng làm bối cảnh" | Fixed | "chỉ dùng để tham khảo" |
| 43 | 04-01:43 second freeze before the first | Fixed | Synced to the English: "sau lần chốt thứ hai, là lần chốt mô hình cuối cùng trước khi mở bất kỳ kết quả nào của tập kiểm thử (Mục 4.2)" |
| 44 | 04-01:45 "quanh hạng k" | Fixed | "độ ổn định của danh sách khi lấy mẫu lại bằng bootstrap, tức sinh viên xếp gần hạng k có còn trong danh sách hay không" |
| 45 | 04-01:46 "kiểm định khẳng định" calque | For native user | Protected term kept; English added at first use in the file: "Kiểm định khẳng định (confirmatory test), tức kiểm định chính thức trên các nhóm đã ấn định trước". Reader proposes "kiểm định xác nhận" or "kiểm định chính (đã đăng ký trước)" |
| 46 | 04-01:47 S3 without S2 | Fixed | Synced to the English: "S2 là độ chính xác của danh sách dài k; chỉ số này được báo cáo nhưng không phải điều kiện đạt (Bảng 4.5)." before S3 |
| 47 | 04-01:47 "giá trị ước lượng của dữ liệu gộp" | Fixed | "cả hai đều tính trên ước lượng điểm gộp chung cho mọi kỳ mở" |
| 48 | 04-01:47 "không thể thay đổi kết luận" | Fixed | "chỉ là phân tích độ nhạy và không được dùng để thay đổi kết luận về S1"; same wording in 04-03:22 and 10-05 R7 |
| 49 | 04-01:59 slots on completers | Fixed | "Các kỳ mở mà hạn mức liên hệ của danh sách bị dùng cho những sinh viên về sau vẫn hoàn thành" |
| 50 | 04-01:61 test "nêu tên" a group | Fixed | "mọi nhóm bị kiểm định này đánh dấu"; the same verb in 04-03 FR1 and 04-04 ("đánh dấu", glossary "flag") |
| 51 | 04-02:3 why repeat students matter | Fixed | "của những sinh viên đã có mặt trong dữ liệu năm 2013, tức dữ liệu dùng để phát triển mô hình" |
| 52 | 04-02:6 "có mặt cả trong" missing a term | Fixed | "Những sinh viên có mặt cả trong các kỳ mở huấn luyện lẫn trong kỳ mở được tách ra để đánh giá bị loại …" |
| 53 | 04-02:6 "điểm … lạc quan" | Fixed | "kết quả kiểm định chéo của một mô hình đã tinh chỉnh siêu tham số cao hơn đáng kể so với hiệu năng thực tế [30]" |
| 54 | 04-02:10 "được đề xuất" by whom | Fixed | "quy trình chốt hai bước dành cho mô hình dự báo" (the source stays [26]) |
| 55 | 04-02:12 reader had to compute dates | Fixed | "Các kỳ mở J năm 2013 bắt đầu vào tháng 10 năm 2013 và kéo dài 261–268 ngày, tức kết thúc vào khoảng giữa năm 2014. Trong khi đó, các kỳ mở B năm 2014 bắt đầu vào tháng 2 năm 2014 và đến thời điểm chốt dữ liệu chỉ vài tuần sau đó" |
| 56 | 04-02:12 "một trường đại học" vague | Fixed | "mà một trường đại học áp dụng mô hình đã có kết quả vào thời điểm đó" |
| 57 | 04-02:16 p-value as embedded question | Fixed | "kiểm định ước lượng tần suất thu được một tập chênh lệch có lợi cho mô hình không kém tập chênh lệch quan sát được" |
| 58 | 04-02:18 "nguy cơ chung" | Fixed | "nguy cơ chung, tức tỷ lệ không hoàn thành tính trên toàn bộ dữ liệu" |
| 59 | 04-03:7 offset assumed known | Fixed | "tức hồi quy logistic biến kết quả theo log-odds của điểm rủi ro, với độ dốc được giữ cố định bằng 1; hệ số chặn của mô hình này là hiệu chuẩn tổng thể" (slope 1 as in Bảng A.4) |
| 60 | 04-03:9 "dải xác suất ngưỡng" | Fixed | "tại nhiều mức xác suất ngưỡng khác nhau" |
| 61 | 04-03:20 FR1 cell overloaded | Fixed | Holm part split: "Khoảng tin cậy này được hiệu chỉnh Holm trên ba nhóm. Phép hiệu chỉnh Holm giữ xác suất đánh dấu nhầm ít nhất một trong ba nhóm ở mức 5%." |
| 62 | 04-03:22 "rộng quá hoặc hẹp quá 20%" | Fixed | "rộng hơn hoặc hẹp hơn mức đúng tối đa 20%" |
| 63 | 04-04:3 "không làm mô hình mất khả năng nhận ra" | Fixed | "khi không có các thuộc tính này, mô hình vẫn có thể gián tiếp nhận ra chúng" |
| 64 | 04-04:5 "trường hợp suy biến" | Fixed | "(mô hình dự báo hoàn hảo hoặc các nhóm có cùng tỷ lệ nền)", the two degenerate cases of the cited result [37] |
| 65 | 04-04:7 calculation in reverse order | Fixed | "Hai con số này (ngưỡng 400 … và mốc 100 …) được rút ra từ cùng một phép tính, gồm hai bước. Bước thứ nhất: … Bước thứ hai: với tỷ lệ … 28%, nhóm có 400 lượt … sẽ có khoảng 112 sinh viên không hoàn thành (400 × 28%), tức vượt mốc 100" |
| 66 | 04-04:7 "sai số chuẩn này" | Fixed | Step stated: "tỷ lệ phát hiện ở phần sinh viên còn lại có sai số chuẩn nhỏ hơn nhiều; vì vậy, sai số chuẩn 5 điểm của nhóm là nguồn bất định chính …" |
| 67 | 04-04:9 what fluctuates | Fixed | Own sentence: "Ngoài ra, mức thiên lệch của các mô hình này đối với nhóm có tình trạng khuyết tật do sinh viên tự khai thay đổi thất thường" |
| 68 | 04-04:9 "chênh lệch không phụ thuộc ngưỡng" | Fixed | "chênh lệch về khả năng phân biệt không phụ thuộc ngưỡng (ABROCA)" |
| 69 | 05-00:3 "lập bản đồ" | Fixed | Glossary form kept with the NIST names: "quản trị (govern), lập bản đồ (map), đo lường (measure) và quản lý (manage)"; the sentence already explains each. Reader's "nhận diện (map)" passed to the lead |
| 70 | 05-00:12 favourable variant | Fixed | "chọn một phương án đánh giá sau khi thấy phương án đó cho kết quả thuận lợi trên tập kiểm thử"; "Kết quả đánh giá trên các fold cao hơn hiệu năng thực tế" |
| 71 | 05-00:16 "chỉ được đánh dấu đến khi" | Fixed | "dấu cảnh báo hết hiệu lực khi kỳ mở kết thúc" |
| 72 | 05-01:3 spatial metaphor | Fixed | "không được thấy bất kỳ thông tin nào thuộc phần dữ liệu kiểm thử, tức phần nằm sau mốc tách dữ liệu huấn luyện với dữ liệu kiểm thử [40]" |
| 73 | 05-01:3 a variant "checks" | Fixed | "phân tích độ nhạy với phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 được dùng để kiểm tra lại điều kiện này" |
| 74 | 05-01:7 Rashomon leap | Fixed | "Như vậy, bộ hệ số của mô hình được chọn chỉ là một trong nhiều bộ hệ số phù hợp với dữ liệu, nên báo cáo không diễn giải hệ số nào thành nguyên nhân" |
| 75 | 05-02:3 three appositions | Fixed | "Thời điểm gốc (time zero) là mốc mà từ đó mọi sinh viên trong đợt thí điểm bắt đầu được theo dõi. Trong đợt thí điểm này, thời điểm gốc là thời điểm chốt dữ liệu, tức lúc sinh viên bắt đầu đủ điều kiện để có tên trong danh sách [44]." |
| 76 | 05-02:5 sounds translated | Fixed | Fidelity #11 had replaced "bảo đảm"; now "Mục đích của quy định này là để sinh viên bị đánh dấu có cơ hội cho thấy dự báo về mình là sai [45], đồng thời để nhãn …" |
| 77 | 05-02:9 "dự báo tự tác động" invented | Rejected | Glossary term (early-warning-evaluation, "performative prediction"), already given with the English and defined in the same sentence; changing it here alone would create drift. Reader's "dự báo tự ảnh hưởng" passed to the lead |
| 78 | 06-00:3 role names as proper nouns | Fixed | Glossary role names kept, each introduced as a role: "AI phản biện lựa chọn mô hình (model-selection critic), tức một AI đóng vai người phản biện, …; AI rà soát thiết kế đánh giá (evaluation reviewer), tức một AI đóng vai người rà soát, …" |
| 79 | 06-00:12 negated decision | Fixed | "Chấp nhận; riêng lập luận rằng dữ liệu mất cân bằng nên cần ưu tiên đường cong … thì không được dùng, vì tỷ lệ không hoàn thành là 44–46%, tức dữ liệu không mất cân bằng" |
| 80 | 06-00:15 fragment list | Fixed | Head nouns added: "cách suy luận thống kê cho điều kiện đạt S1, căn cứ của tiêu chí S2, phạm vi lượt đăng ký học dùng cho đánh giá chính, …, cách gộp kết quả các fold khi chọn mô hình" |
| 81 | 06-00:19 counterfactual | Fixed | "Phép tính này cho thấy một tiêu chí chỉ đếm số kỳ mở thắng dễ được đáp ứng do ngẫu nhiên: nếu … thì … khoảng 13% trường hợp" |
| 82 | 08-00:3 redundant apposition | Fixed | Apposition removed: "cùng các ma trận sẵn sàng cho mô hình được lập từ hai bảng này" |
| 83 | 08-00:14 "cùng" read as "same" | Fixed | "qua AQ tương ứng, loại phân tích và bài toán kỹ thuật của AQ đó" (also in the 10-07 introduction; "AQ" because the abbreviation is defined) |
| 84 | 10-01:15 random effects sound translated | Fixed | "coi các module là một mẫu lấy từ một tổng thể module lớn hơn, nên hiệu ứng của từng module được ước lượng như một hiệu ứng ngẫu nhiên" (03-02 wording) |
| 85 | 10-01:16 "nhánh chia" | Fixed | "cách cây chia nhánh thay đổi giữa các mẫu"; row 17 "cách chia nhánh không ổn định" |
| 86 | 10-01:17 fixed-effects link | Fixed | "tức các kỳ mở được quan sát đầy đủ chứ không phải được lấy mẫu, nên hiệu ứng cố định phù hợp với thiết kế [12]" |
| 87 | 10-01:32 "kiểm duyệt" | Fixed | Established term kept and defined in place: "khi một sinh viên bị kiểm duyệt (censored), tức thời điểm rút khỏi module không được quan sát vì việc theo dõi đã dừng, lý do dừng theo dõi được giả định không liên quan đến nguy cơ rút khỏi module". Reader's "dữ liệu bị chặn" not adopted (task decision: the biostatistics term stays) |
| 88 | 10-01:34 "chằng chịt" | Fixed | "sự phụ thuộc lẫn nhau giữa các thành phần của hệ thống (entanglement)" |
| 89 | 10-01:40 background-only model reads backwards | Fixed | "Khi so với mô hình chính, mô hình chỉ dùng đặc điểm cá nhân (không có dữ liệu hoạt động) cho biết bao nhiêu phần của thứ hạng đến từ mức tham gia học tập …"; English wording reported below |
| 90 | 10-01:50 "không bị gây nhiễu" | Fixed | "Cần dữ liệu về can thiệp được phân bổ ngẫu nhiên hoặc không bị yếu tố gây nhiễu làm sai lệch [9]" |
| 91 | 10-02:3 list of scores | Fixed | "L là danh sách gồm k lượt đăng ký học có điểm rủi ro cao nhất" |
| 92 | 10-03:14 outer/inner loops undefined | Fixed | "ở cả vòng ngoài (vòng kiểm định chéo dùng để đánh giá và chọn mô hình) lẫn vòng trong (vòng kiểm định chéo chạy bên trong mỗi fold huấn luyện để tinh chỉnh siêu tham số, bước 3)" |
| 93 | 10-03:15 nested CV in eight words | Fixed | "được tinh chỉnh bằng kiểm định chéo lồng nhau: bên trong mỗi fold huấn luyện, một vòng loại trừ từng kỳ mở nữa (vòng trong) được chạy trên các kỳ mở huấn luyện của fold đó" |
| 94 | 10-03:16 missing relative marker | Fixed | "những chênh lệch không vượt quá biến thiên do lấy mẫu thì ít có ý nghĩa thực tế" |
| 95 | 10-03:46 "lý do này" unclear | Fixed | "Do chỉ có 9 kỳ mở, nhóm tác giả kiểm tra … Cũng vì số kỳ mở ít, mô hình riêng cho từng module không phải lựa chọn tốt: dữ liệu của từng module nhỏ, mà phép co hệ số không khắc phục được mẫu nhỏ [17]" |
| 96 | 10-04:7 column header vs values | Fixed | Header synced and stated as the data define it: "Số lượt đăng ký học ít nhất của nhóm trong một kỳ mở của tập kiểm thử" (`code/design_facts.py`, `test_rows_min_per_run`; see "For the lead") |
| 97 | 10-04:22 two "tỷ lệ của nhóm" | Fixed | "Phần trăm danh sách mà mỗi nhóm chiếm, so với phần trăm nhóm đó chiếm trong số sinh viên không hoàn thành" |
| 98 | 10-04:25 permutation reference | Fixed | "kèm giá trị tham chiếu: ABROCA tính lại sau khi hoán vị ngẫu nhiên nhãn nhóm trong từng kỳ mở, tức mức ABROCA có thể có chỉ do ngẫu nhiên [34]" |
| 99 | 10-04:25 "không bao giờ dẫn đến việc xem xét" | Fixed | "chỉ số này không tự mình kích hoạt việc xem xét lại một nhóm" |
| 100 | 10-04:30 "tùy ý đến mức nào" | Fixed | "Cho thấy điểm cắt tại hạng k phụ thuộc vào biến động ngẫu nhiên đến mức nào" |
| 101 | 10-05:12 "cờ" | Fixed | "các cột đánh dấu được suy ra từ biến mục tiêu không nằm trong danh sách biến dự báo" |
| 102 | 10-05:14 "điểm theo fold … lạc quan" | Fixed | "Kết quả theo fold của cấu hình được chọn cao hơn hiệu năng thực tế" |
| 103 | 10-05:15 recalibration contradicts 4.3 | Fixed | Synced to the English R4: "mô hình chỉ được hiệu chuẩn lại trên một kỳ mở diễn ra sau các kỳ mở năm 2014 của tập kiểm thử [33]" |
| 104 | 10-05:16 "Trung bình với CCC" | Fixed | "Trung bình (riêng với module CCC)" |
| 105 | 10-05:20 wording rule compressed | Fixed | "Quy tắc chỉ diễn đạt kết quả dưới dạng mối liên hệ, không dùng từ ngữ nhân quả, kèm rà soát câu chữ" |
| 106 | 10-05:27 conformity assessment unglossed | Fixed | "Đánh giá sự phù hợp (conformity assessment), tức thủ tục đánh giá hệ thống trí tuệ nhân tạo có rủi ro cao trước khi đưa vào sử dụng [49]" |
| 107 | 10-06:10 "chấm điểm" for model scoring | Fixed | Settled term: "để tính điểm rủi ro cho các kỳ mở B năm 2014" |
| 108 | 10-06:15 survival ideas, "kiểm duyệt" | Fixed | Split into two sentences; "bị kiểm duyệt (censored)" defined in place as in 10-01 |
| 109 | 10-06:33 fragments, "có offset" | Fixed | "Hiệu chuẩn tổng thể được định nghĩa là hệ số chặn khi log-odds của điểm rủi ro được đưa vào làm offset (hệ số cố định bằng 1); các ngưỡng hiệu chuẩn áp dụng cho ước lượng gộp mọi kỳ mở; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở diễn ra sau" |
| 110 | 10-06:34 "loại ở mọi vòng" | Fixed | "loại các sinh viên này ở mọi vòng, cả vòng ngoài lẫn vòng trong" |
| 111 | 10-07:9 raw table names | Fixed | "Bảng theo lượt đăng ký học (enrolment) và bảng theo bài được chấm điểm đến hạn (assessment_due)" (08-00: "the enrolment and task views") |
| 112 | 10-07:11–12 model_ready, capacity_by_run | Fixed | "Hai bảng đặc trưng (features_d13, features_d27) và ma trận sẵn sàng cho mô hình (model_ready)"; "bảng độ dài danh sách theo hạn mức liên hệ của từng kỳ mở (capacity_by_run)" |

## English changes brought into the twins

| English file | Change in the English | Vietnamese now |
| :---- | :---- | :---- |
| 04-01 | S1 cell: "S2, precision at capacity, is reported and is not a gate (Table 4.5)" before S3 | "S2 là độ chính xác của danh sách dài k; chỉ số này được báo cáo nhưng không phải điều kiện đạt (Bảng 4.5)." |
| 04-01 | Validation strategy: "after the second freeze, which fixes the final model before any test outcome is opened (Section 4.2)" | "sau lần chốt thứ hai, là lần chốt mô hình cuối cùng trước khi mở bất kỳ kết quả nào của tập kiểm thử (Mục 4.2)" |
| 10-05 | R4: "recalibration only on a run after the 2014 test runs" | "mô hình chỉ được hiệu chuẩn lại trên một kỳ mở diễn ra sau các kỳ mở năm 2014 của tập kiểm thử" |
| 10-04 | Table A.7 header "Enrolments in the smallest test run" | "Số lượt đăng ký học ít nhất của nhóm trong một kỳ mở của tập kiểm thử" (the meaning of the values; see below) |

## Settled terms applied

| Term | Before | After | Files |
| :---- | :---- | :---- | :---- |
| proxy | biến thay thế; kiểm tra biến thay thế | biến đại diện (proxy) at first use in each file; kiểm tra biến đại diện (proxy check) | 04-04, 05-00, 05-01, 10-01, 10-04, 10-05, 10-06 (no "biến thay thế" left) |
| score (model) | chấm điểm các kỳ mở | tính điểm rủi ro cho các kỳ mở | 10-06 (no other non-grading "chấm điểm" found) |
| censored | kiểm duyệt (undefined) | bị kiểm duyệt (censored), defined in place | 10-01, 10-06 |

## For the native user

Protected terms were kept everywhere; the reader's proposals, from the flags and from the recurring-terms table of `reader-test-2.md`, are listed for the decision.

| Term in the twins | Flags | Reader's proposal |
| :---- | :---- | :---- |
| độ chính xác của danh sách (dài k) | 4; table (17 uses) | "precision@k" or "độ chính xác dương tại k"; "độ chính xác" alone reads as accuracy |
| kiểm định khẳng định | 45; table (19 uses) | "kiểm định xác nhận" or "kiểm định chính (đã đăng ký trước)"; English "(confirmatory test)" now given at first use in 04-01 |
| kỳ mở | table (362 uses) | "đợt mở lớp", "khóa (presentation)"; at least "kỳ" alone after the first mention |
| lượt đăng ký học (còn hiệu lực) | table (85 uses) | "lượt ghi danh", "bản ghi đăng ký" |
| hạn mức liên hệ | 15 (sentence only); table (37 uses) | "năng lực liên hệ", "số sinh viên liên hệ được (k)" |
| tỷ lệ phát hiện (chuẩn hóa) trong giới hạn danh sách | table (18 / 13 uses) | "recall@k (chuẩn hóa)", "độ nhạy tại k" |
| điều kiện đạt | table (16 uses) | "tiêu chí đạt", "ngưỡng chấp nhận" |

## Check results

| Command | Result |
| :---- | :---- |
| `apply.py edits/*.py` | 27 twins, 120 edits applied, exit 0; follow-up files applied 6 more (below and one read-aloud fix in 04-04:7) |
| `check_parity.py --report reports/milestone-4/report --lang vi` (first run) | 0 errors, 26 warnings; 2 introduced by this pass (comma before "và" in 03-02:9, "của họ" in 04-04:7), fixed by `edits2-fixwarn*.py` |
| `check_abbreviations.py --report reports/milestone-4/report --lang vi` (first run) | 17 abbreviations, 3 violations (TRIPOD+AI full form shortened in 04-00; "câu hỏi phân tích" repeated after AQ was defined in 08-00 and 10-07), fixed by `edits3-abbrev*.py` |
| `check_parity.py --report reports/milestone-4/report --lang vi` (final) | 0 errors, 24 warnings: 23 in the verbatim English prompts of 10-06, 1 loanword on the English term of the terms page (00-2:37); the same 24 as before this pass |
| `check_abbreviations.py --report reports/milestone-4/report --lang vi` (final) | 17 abbreviations, 0 violations |
| `translation_status.py --report reports/milestone-4/report --lang vi --mark <27 English paths>` | recorded 27 files (a first call passed the paths as one argument and recorded 1; rerun) |
| `translation_status.py --report reports/milestone-4/report --lang vi` | 34 sections, 0 need translation, 0 orphaned, exit 0 |

Console output with UTC timestamps, commands and exit codes: `rewrite-2-2026-11-08-scripts/checks.log`; full before/after diff: `rewrite-2-2026-11-08-scripts/twins.diff`.

## For the lead

- **10-04 Table A.7, English header.** "Enrolments in the smallest test run" does not match the values: `code/design_facts.py` computes `test_rows_min_per_run`, each group's fewest enrolments in any one test run (female 66 and male 139 come from different runs). Suggested English: "Fewest enrolments of the group in one test run". The twin states this meaning.
- **10-01 paragraph after Table A.2, English wording.** "The background-only model shows how much of the ranking comes from engagement rather than from module and history" reads backwards on its own and seems to contradict 03-03 ("how much of a ranking comes from who the student is"); the two agree only by comparison with the primary model. Suggested: "Compared with the primary model, the background-only model shows …". The twin adds "Khi so với mô hình chính".
- **10-06 Table A.11 row 6** still says "or on a later run"; 10-05 R4 now says "a run after the 2014 test runs". Aligning the two English cells would remove a reader's doubt; the twin keeps "trên một kỳ mở diễn ra sau".
- **01-01 "how two questions are measured"** names neither question; the twin names AQ3 and AQ4 (Change Log C10 and C13, defined at the end of Section 1.1). The English could name them too.
- **Glossary rows to settle (not edited here).** `topics/early-warning-evaluation.md` still has "proxy (for an excluded attribute) → biến thay thế" and "proxy check → kiểm tra biến thay thế", which contradict the settled "biến đại diện (proxy)"; the twins now use "kiểm tra biến đại diện". The reader's alternatives for "lập bản đồ (map)" ("nhận diện (map)") and "dự báo tự tác động" ("dự báo tự ảnh hưởng") are glossary questions too.
- **Content added for clarity, beyond the English words** (each derived from the report or the cited source): the dates of the October 2013 and February 2014 runs (04-02), the two degenerate cases (04-04), dummy terms (03-03), the definitions of outer and inner loops (10-03), of censoring (10-01, 10-06), of conformity assessment (10-05) and of the prepared tables (10-07).
- A third reader test on the rewritten passages has not been run.
