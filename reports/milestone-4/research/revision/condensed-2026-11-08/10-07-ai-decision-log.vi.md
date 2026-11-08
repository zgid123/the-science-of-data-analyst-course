## Phụ lục VII – Nhật ký quyết định về AI và các prompt

AI tạo sinh đóng vai trò cộng sự trong mô hình hóa, theo các vai mà đề bài cho phép: giải thích phương pháp, đề xuất và phản biện các nhóm kỹ thuật ứng viên, rà soát thiết kế đánh giá. Các lựa chọn cuối cùng và bằng chứng cho các lựa chọn đó vẫn do nhóm tác giả chịu trách nhiệm [1]. Bảng A.18 là Nhật ký quyết định về AI (AI Decision Log) theo năm cột của đề bài, mỗi dòng ứng với một đóng góp quan trọng của AI.

**Bảng A.18. Nhật ký quyết định về AI**

| Prompt / mục đích | Đề xuất của AI | Quyết định của nhóm | Bằng chứng / cách kiểm chứng | Tác động đến bản đề xuất |
| :---- | :---- | :---- | :---- | :---- |
| Tìm các nguồn uy tín về cách chọn phương pháp cho từng AQ (trợ lý tìm tài liệu) | Phân biệt giải thích với dự báo; ưu tiên quy tắc và phương pháp cơ sở đơn giản trước; dùng mô hình diễn giải được khi sử dụng trong bối cảnh hệ trọng; tiêu chí cỡ mẫu; cách đặt bài toán theo phân tích sống sót và theo xếp hạng | Chấp nhận sau khi đọc từng nguồn | Mọi phát biểu được đối chiếu với bản lưu của nguồn, kèm trích dẫn nguyên văn | Phần 2–3; Phụ lục I–II |
| Tìm nguồn về thiết kế đánh giá (trợ lý tìm tài liệu) | TRIPOD+AI và Công cụ đánh giá nguy cơ sai lệch của mô hình dự báo, phiên bản cho AI (PROBAST+AI); hiệu chuẩn; fold theo nhóm; tinh chỉnh lồng nhau; các loại rò rỉ thông tin; đăng ký trước kế hoạch phân tích; bootstrap hai tầng (hierarchical bootstrap); phân tích theo từng nhóm con | Chấp nhận, trừ một điểm: đường cong độ chính xác – tỷ lệ phát hiện thường được khuyến nghị khi dữ liệu mất cân bằng lớp, nhưng lập luận này không áp dụng ở đây, vì tỷ lệ không hoàn thành là 44–46% | Kiểm chứng như dòng trên | Phần 4; Phụ lục III–V |
| Tìm nguồn về rủi ro, quan hệ nhân quả, công bằng và quy định pháp lý (trợ lý tìm tài liệu) | Thử nghiệm mục tiêu (target trial) và xếp hạng theo lợi ích can thiệp (uplift) đều cần dữ liệu can thiệp; thử nghiệm mục tiêu là thử nghiệm ngẫu nhiên giả định mà một phân tích dữ liệu quan sát cố gắng mô phỏng; các tiêu chí công bằng mâu thuẫn nhau; Đạo luật AI của EU, Luật Trí tuệ nhân tạo của Việt Nam và danh mục hệ thống trí tuệ nhân tạo có rủi ro cao; dự báo tự tác động (performative prediction) | Chấp nhận; Đạo luật của EU được dùng làm chuẩn tham chiếu, luật Việt Nam có hiệu lực ràng buộc đối với đợt thí điểm tại Việt Nam | Văn bản pháp luật được đọc từ bản chính thức khi có; văn bản của EU được đọc từ một bản thứ cấp | Phần 5; Phụ lục VI |
| Rà soát việc chọn mô hình theo góc nhìn của một nhà phân tích hoài nghi (AI phản biện lựa chọn mô hình) | 12 nhận xét: đánh giá trong từng kỳ mở, fold chia theo kỳ mở, một phép so sánh chính trên tập kiểm thử, kết quả AQ2 theo từng module, lý do lấy từ mô hình chấm điểm, quy tắc chuyển sang mô hình đối sánh (challenger), giả định của phân tích sống sót, quan hệ giữa cỡ mẫu và khả năng áp dụng cho kỳ mở mới, nên hiển thị thứ hạng hay xác suất, lực kiểm định của phép kiểm tra công bằng, nguy cơ cao có đồng nghĩa với nhu cầu hỗ trợ hay không, sinh viên học lại | Chấp nhận 10, chấp nhận một phần 2 (Bảng A.19) | Từng nhận xét được đối chiếu với các thông tin của thiết kế và độ dài các kỳ mở | Phụ lục I–II và IV–VI |
| Rà soát thiết kế đánh giá theo góc nhìn của một chuyên gia phương pháp (AI rà soát thiết kế đánh giá) | 12 nhận xét: module không có trong dữ liệu huấn luyện, hạn mức liên hệ tính theo kỳ mở hay theo từng giảng viên hướng dẫn, suy luận cho S1, căn cứ của S2, tổng thể kiểm thử chính, định nghĩa hiệu chuẩn, cách gộp kết quả khi chọn mô hình, điều kiện kiểm tra công bằng, giá trị tham chiếu của ABROCA, thước đo tác động của AQ2, các khoảng trống trong phân tích lỗi, các rủi ro còn thiếu | Chấp nhận 12 (Bảng A.20) | Nhóm tính lại các phép tính trong từng nhận xét | Phụ lục III–VI; S2 (độ chính xác của danh sách dài k) được báo cáo, không dùng làm điều kiện đạt |

Bảng A.19 ghi lại quyết định về từng nhận xét trong 12 nhận xét của AI phản biện lựa chọn mô hình.

**Bảng A.19. Quyết định về các nhận xét của AI phản biện lựa chọn mô hình**

| # | Nhận xét (tóm tắt) | Quyết định | Nơi xử lý |
| :---- | :---- | :---- | :---- |
| 1 | Chỉ số gộp có thể cho kết quả cao chỉ vì mô hình tách được kỳ mở có tỷ lệ cao khỏi kỳ mở có tỷ lệ thấp | Chấp nhận | Danh sách và tỷ lệ phát hiện chuẩn hóa theo từng kỳ mở; ROC-AUC và PR-AUC trong từng kỳ mở; phương pháp cơ sở chỉ dùng đặc điểm cá nhân |
| 2 | Chưa nêu cách chia fold; có module không có trong dữ liệu huấn luyện; kết quả của kỳ mở tháng 10 năm 2013 chưa có vào tháng 2 năm 2014 | Chấp nhận | Nêu rõ các fold loại trừ từng kỳ mở; biến module mã hóa dưới dạng độ lệch, CCC được xét riêng; phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 để chấm điểm các kỳ mở B năm 2014 |
| 3 | Một tập kiểm thử phải phân xử nhiều phép so sánh | Chấp nhận | Một phép so sánh chính (S1); mọi biến thể là phân tích độ nhạy |
| 4 | AQ2 cho mối liên hệ gộp, không theo từng module; các số đếm đã dùng không lấy từ 9 kỳ mở huấn luyện | Chấp nhận | Biến tương tác dấu hiệu × module; nêu rõ mô hình được ước lượng trên 9 kỳ mở và 6 module; dấu hiệu về bài được chấm điểm chỉ xét khi có bài đến hạn |
| 5 | Lý do lấy từ AQ2 có thể mâu thuẫn với điểm rủi ro của AQ3; ước lượng đã hiệu chỉnh chỉ là hiệu ứng riêng phần | Chấp nhận | Lý do lấy từ mô hình chấm điểm; ước lượng chưa hiệu chỉnh và đã hiệu chỉnh đặt cạnh nhau; kiểm tra tương quan |
| 6 | Lựa chọn dựa nhiều vào tài liệu; chưa có quy tắc chuyển mô hình | Chấp nhận một phần | Quy tắc chuyển mô hình ở Bảng A.13, bước 4; lập luận xuất phát từ các ràng buộc của dự án (Mục 3.3) |
| 7 | Phương án phân tích sống sót bị loại dựa trên một giả định phát biểu sai | Chấp nhận | Fail không phải kết quả dạng thời gian đến sự kiện; kiểm duyệt không mang thông tin (non-informative censoring) được nêu là một giả định |
| 8 | Cỡ mẫu không cho biết gì về khả năng áp dụng cho kỳ mở mới; chưa nêu nguồn của R² dự kiến | Chấp nhận | Khả năng áp dụng được kiểm tra bằng cách chia theo kỳ mở; trích dẫn giá trị mặc định của Riley; cỡ mẫu tối thiểu cho từng thời điểm chốt dữ liệu |
| 9 | Chưa quyết định giảng viên hướng dẫn thấy thứ hạng hay xác suất | Chấp nhận | Thứ hạng và lý do; chỉ hiển thị xác suất nếu đạt S3; các nhóm mức nguy cơ được cố định theo hạn mức liên hệ |
| 10 | Phép kiểm tra công bằng thiếu lực kiểm định; bỏ các thuộc tính là chưa đủ | Chấp nhận | Gộp qua các kỳ mở cho các nhóm của kiểm định khẳng định; kiểm tra biến thay thế (proxy); nêu rõ tiêu chí chính là ngang bằng tỷ lệ phát hiện (separation) |
| 11 | Giả định thứ tự nguy cơ trùng với nhu cầu hỗ trợ; tỷ lệ phát hiện có mức trần | Chấp nhận | Nêu rõ giả định là chưa được kiểm chứng; tỷ lệ phát hiện chuẩn hóa; tách Fail và Withdrawn |
| 12 | Ngày rút khỏi module không xác định và sinh viên học lại có thể gây rò rỉ | Chấp nhận một phần | Các phân tích độ nhạy ở Bảng A.13, bước 7; số lần học trước được ghi nhận khi đăng ký nên vẫn hợp lệ |

Bảng A.20 ghi lại quyết định về từng nhận xét trong 12 nhận xét của AI rà soát thiết kế đánh giá.

**Bảng A.20. Quyết định về các nhận xét của AI rà soát thiết kế đánh giá**

| # | Nhận xét (tóm tắt) | Quyết định | Nơi xử lý |
| :---- | :---- | :---- | :---- |
| 1 | Các kỳ mở năm 2013 gồm 6 module, không phải 7 | Chấp nhận | Tiêu chí của AQ2 tính theo tỷ lệ module: dấu hiệu phải cùng chiều ở ít nhất hai phần ba số module; quy tắc cho module không có trong dữ liệu huấn luyện; CCC được xét riêng |
| 2 | Danh sách theo kỳ mở được dùng thay cho hạn mức liên hệ của từng giảng viên hướng dẫn; các chỉ số phụ chỉ biểu diễn lại cùng một số đếm | Chấp nhận | Nêu giới hạn và rủi ro R8; định nghĩa tỷ lệ phát hiện chuẩn hóa; lợi ích ròng chỉ làm bối cảnh |
| 3 | Suy luận cho S1 chưa được đặc tả đủ với 13 kỳ mở | Chấp nhận | Bootstrap hai tầng (mô hình và quy tắc được so sánh trên cùng mẫu lặp), có lập lại danh sách trong mỗi mẫu; kiểm định đổi dấu; số kỳ mở mà mô hình hơn, bằng và kém quy tắc |
| 4 | S2 mơ hồ và thiếu mốc so sánh | Chấp nhận | S2 được báo cáo, không dùng làm điều kiện đạt |
| 5 | Chưa có tổng thể kiểm thử chính | Chấp nhận | S1 trên cả 13 kỳ mở, mọi lượt đăng ký học đủ điều kiện, ngày 27, k = 5 trên 20 |
| 6 | Hệ số chặn hiệu chuẩn chưa được định nghĩa rõ; phương án xử lý khi hiệu chuẩn không đạt lại dùng tập kiểm thử lần thứ hai | Chấp nhận | Hiệu chuẩn tổng thể có offset; ngưỡng áp dụng cho ước lượng gộp; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở sau |
| 7 | Bước chọn mô hình dùng cách gộp kết quả khác với S1; sinh viên có mặt ở cả kỳ mở huấn luyện lẫn kỳ mở kiểm định chưa được loại ở các fold vòng trong | Chấp nhận | Cùng chỉ số với S1; ngưỡng chênh lệch khoảng 89 sinh viên; loại ở mọi vòng |
| 8 | Điều kiện kiểm định công bằng không phát hiện được vấn đề ở nhóm nhỏ; quy tắc lẫn lộn giữa kiểm định hai phía và một phía | Chấp nhận | Điều kiện đưa nhóm vào kiểm định xác định từ số lượt đăng ký học; kiểm định một phía; hiệu chỉnh Holm; ghi "chưa được xác nhận đạt" cho nhóm nhỏ |
| 9 | ABROCA thiếu giá trị tham chiếu | Chấp nhận | Tính trong từng kỳ mở, giá trị tham chiếu bằng hoán vị, báo cáo dấu, chỉ để mô tả |
| 10 | Ở tỷ lệ nền này, tỉ số odds phóng đại độ lớn của hiệu ứng; ngưỡng quá dễ đạt; AQ2 và AQ3 phụ thuộc nhau | Chấp nhận | Dùng chênh lệch nguy cơ, với hiệu ứng nhỏ nhất có ý nghĩa là 5 điểm phần trăm; quy tắc được chốt trước; kết quả AQ2 năm 2014 không thể thay đổi AQ3 |
| 11 | Phân tích lỗi còn khoảng trống | Chấp nhận | Sinh viên không hoàn thành còn liên hệ được, sinh viên có hoạt động, độ ổn định của danh sách, phân tích theo lịch sử học tập, CCC |
| 12 | Thiếu rủi ro và có biện pháp kiểm soát không khớp với rủi ro | Chấp nhận | Mười sáu rủi ro ở Bảng A.17; biện pháp kiểm soát cho rủi ro hiểu nhầm hệ số là nguyên nhân (R9), khẳng định việc liên hệ có hiệu quả (R10) và thiên kiến tự động hóa (R13) được gắn đúng với rủi ro tương ứng |

Hai AI rà soát là hai phiên AI tạo sinh riêng biệt; mỗi phiên chỉ được đọc đề bài và các phụ lục nêu trong prompt của phiên đó. Các thành viên nhóm đối chiếu từng nhận xét với các thông tin của thiết kế trước khi quyết định. Các prompt được giữ nguyên bằng tiếng Anh và rút gọn còn phần chỉ dẫn về nhiệm vụ; các tài liệu được gọi theo vị trí trong báo cáo này. AI phản biện lựa chọn mô hình nhận chỉ dẫn sau:

> You act as the "Model selection" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the AQ Modeling Briefs (Appendix I), the candidate comparison (Appendix II) and the
> sample sizes and counts from the prepared data (Appendix IV). Do not search the web, do not open any data file, do
> not invent benchmark results, metric thresholds or performance numbers, and do not choose the model for the team.
> Challenge the model selection as a sceptical senior analyst would: (1) mismatch between each AQ's question, output
> and the chosen method; (2) whether each modeling AQ has a sensible baseline and 2–3 real candidate families, or a
> straw-man baseline; (3) whether the rationale is tied to the data facts and constraints, or rests on algorithm
> reputation; (4) assumptions the team has not checked; (5) causal overclaim or confusion between association,
> prediction and benefit; (6) leakage or test-set exposure risks created by the modeling plan; (7) anything that makes
> the choice hard to act on for tutors (decision D1) or unfair to groups. Write at most 12 numbered critiques, most
> important first, each with the passage, the problem, why it matters and a concrete recommendation.

AI rà soát thiết kế đánh giá nhận chỉ dẫn sau:

> You act as the "Evaluation design" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the Evaluation Design Cards and metric definitions (Appendix III), the validation
> and test protocol (Appendix IV), the error and fairness analysis (Appendix V), the risk register (Appendix VI) and the
> counts from the prepared data. Do not search the web, do not open any data file, do not invent results, benchmarks or
> performance numbers. Review the evaluation design as a sceptical methodologist: (1) whether each metric reflects the
> decision it serves and whether any metric is misleading for this base rate; (2) whether the success criteria are
> fixed in advance, falsifiable, internally consistent, and neither trivially easy nor impossible; (3) validation:
> leakage paths, test reuse, grouping of students across runs and years, nested tuning, the AQ2/AQ3 interaction; (4)
> uncertainty estimation with 9 training and 13 test runs; (5) calibration criteria and what happens when they fail;
> (6) fairness: choice of criterion, small groups, multiple comparisons, interpretation of ABROCA; (7) error analysis
> gaps; (8) risks missing from the register or controls that do not match their risk. Write at most 12 numbered
> critiques, most important first, each with the passage, the problem, why it matters and a concrete recommendation.
