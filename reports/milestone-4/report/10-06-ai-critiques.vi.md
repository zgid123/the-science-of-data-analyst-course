## Phụ lục VI – Quyết định về các nhận xét của AI và các prompt

Nhật ký quyết định về AI ở Phần 6 (Bảng 6.1) ghi lại các đóng góp quan trọng của AI; phụ lục này trình bày quyết định của nhóm chúng em về từng nhận xét của hai AI rà soát. Bảng A.10 trình bày 12 nhận xét của AI phản biện lựa chọn mô hình và Bảng A.11 trình bày 12 nhận xét của AI rà soát thiết kế đánh giá, mỗi nhận xét kèm bằng chứng dùng để kiểm chứng và tác động của nhận xét đó đến bản đề xuất.

**Bảng A.10. Quyết định về các nhận xét của AI phản biện lựa chọn mô hình**

| # | Nhận xét (tóm tắt) | Quyết định | Nơi xử lý |
| :---- | :---- | :---- | :---- |
| 1 | Chỉ số gộp có thể cho kết quả cao chỉ vì mô hình tách được kỳ mở có tỷ lệ cao khỏi kỳ mở có tỷ lệ thấp | Chấp nhận | Danh sách và tỷ lệ phát hiện chuẩn hóa theo từng kỳ mở; ROC-AUC và PR-AUC trong từng kỳ mở; phương pháp cơ sở chỉ dùng đặc điểm cá nhân |
| 2 | Chưa nêu cách chia fold; có module không có trong dữ liệu huấn luyện; kết quả của kỳ mở tháng 10 năm 2013 chưa có vào tháng 2 năm 2014 | Chấp nhận | Nêu rõ các fold loại trừ từng kỳ mở; số hạng module mã hóa dưới dạng độ lệch, CCC được xét riêng; phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 để tính điểm rủi ro cho các kỳ mở B năm 2014 |
| 3 | Một tập kiểm thử phải phân xử nhiều phép so sánh | Chấp nhận | Một phép so sánh chính (S1); mọi biến thể là phân tích độ nhạy |
| 4 | AQ2 cho mối liên hệ gộp, không theo từng module; các số đếm đã dùng không lấy từ 9 kỳ mở huấn luyện | Chấp nhận | Số hạng tương tác dấu hiệu × module; nêu mức phù hợp với dữ liệu theo đúng 9 kỳ mở và 6 module; dấu hiệu về bài được chấm điểm chỉ xét khi có bài đến hạn |
| 5 | Lý do lấy từ AQ2 có thể mâu thuẫn với điểm rủi ro của AQ3; ước lượng đã hiệu chỉnh chỉ là hiệu ứng riêng phần | Chấp nhận | Lý do lấy từ mô hình tính điểm rủi ro; ước lượng chưa hiệu chỉnh và đã hiệu chỉnh đặt cạnh nhau; kiểm tra tương quan |
| 6 | Lựa chọn dựa nhiều vào tài liệu; chưa có quy tắc chuyển mô hình | Chấp nhận một phần | Quy tắc chuyển mô hình ở Bảng A.5, bước 4; lập luận xuất phát từ các ràng buộc của dự án (Mục 3.3) |
| 7 | Phương án phân tích sống sót bị loại dựa trên một giả định phát biểu sai | Chấp nhận | Fail không phải kết quả dạng thời gian đến sự kiện. Kiểm duyệt không mang thông tin (non-informative censoring) được nêu rõ là một giả định: khi một sinh viên bị kiểm duyệt (censored), tức thời điểm rút khỏi module không được quan sát vì việc theo dõi đã dừng, lý do dừng theo dõi được giả định không liên quan đến nguy cơ rút khỏi module |
| 8 | Cỡ mẫu không cho biết gì về khả năng áp dụng cho kỳ mở mới; chưa nêu nguồn của R² dự kiến | Chấp nhận | Khả năng áp dụng được kiểm tra bằng cách chia theo kỳ mở; trích dẫn giá trị mặc định của Riley; cỡ mẫu tối thiểu cho từng thời điểm chốt dữ liệu |
| 9 | Chưa quyết định giảng viên hướng dẫn thấy thứ hạng hay xác suất | Chấp nhận | Thứ hạng và lý do; chỉ hiển thị xác suất nếu đạt S3; các nhóm mức nguy cơ được cố định theo hạn mức liên hệ |
| 10 | Phép kiểm tra công bằng thiếu lực kiểm định; chỉ bỏ các thuộc tính nhạy cảm ra khỏi mô hình là chưa đủ | Chấp nhận | Gộp qua các kỳ mở cho các nhóm của kiểm định khẳng định; kiểm tra biến đại diện (proxy check); nêu rõ tiêu chí chính là tiêu chí ngang bằng tỷ lệ phát hiện |
| 11 | Thứ tự nguy cơ được mặc nhiên coi là trùng với nhu cầu hỗ trợ; tỷ lệ phát hiện có mức trần | Chấp nhận | Nêu rõ giả định là chưa được kiểm chứng; tỷ lệ phát hiện chuẩn hóa; tách Fail và Withdrawn |
| 12 | Ngày rút khỏi module không xác định và sinh viên học lại có thể gây rò rỉ | Chấp nhận một phần | Các phân tích độ nhạy ở Bảng A.5, bước 7; số lần học trước được ghi nhận khi đăng ký nên vẫn hợp lệ |

Bảng A.11 ghi lại quyết định về từng nhận xét trong 12 nhận xét của AI rà soát thiết kế đánh giá.

**Bảng A.11. Quyết định về các nhận xét của AI rà soát thiết kế đánh giá**

| # | Nhận xét (tóm tắt) | Quyết định | Nơi xử lý |
| :---- | :---- | :---- | :---- |
| 1 | Các kỳ mở năm 2013 gồm 6 module, không phải 7 | Chấp nhận | Tiêu chí của AQ2 tính theo tỷ lệ module: dấu hiệu phải cùng chiều ở ít nhất hai phần ba số module; quy tắc cho module không có trong dữ liệu huấn luyện; CCC được xét riêng |
| 2 | Danh sách theo kỳ mở được dùng thay cho hạn mức liên hệ của từng giảng viên hướng dẫn; các chỉ số chỉ biểu diễn lại cùng một số đếm | Chấp nhận | Nêu giới hạn và rủi ro R8; định nghĩa tỷ lệ phát hiện chuẩn hóa; lợi ích ròng chỉ làm bối cảnh |
| 3 | Suy luận cho S1 chưa được đặc tả đủ với 13 kỳ mở | Chấp nhận | Bootstrap hai tầng (mô hình và quy tắc được so sánh trên cùng mẫu lấy lại), có lập lại danh sách trong mỗi mẫu lấy lại; kiểm định hoán vị đổi dấu; số kỳ mở thắng, hòa và thua |
| 4 | S2 mơ hồ và thiếu mốc so sánh | Chấp nhận | S2 được báo cáo, không dùng làm điều kiện đạt |
| 5 | Chưa xác định phạm vi dữ liệu kiểm thử chính | Chấp nhận | S1 trên cả 13 kỳ mở, mọi lượt đăng ký học đủ điều kiện, ngày 27, k = 5 trên 20 |
| 6 | Hệ số chặn hiệu chuẩn chưa được định nghĩa rõ; phương án xử lý khi phép kiểm tra hiệu chuẩn báo lỗi lại dùng tập kiểm thử lần thứ hai | Chấp nhận | Hiệu chuẩn tổng thể được định nghĩa là hệ số chặn khi log-odds của điểm rủi ro được đưa vào làm offset (hệ số cố định bằng 1); các ngưỡng hiệu chuẩn áp dụng cho ước lượng gộp mọi kỳ mở; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở diễn ra sau các kỳ mở năm 2014 của tập kiểm thử |
| 7 | Bước chọn mô hình dùng cách gộp kết quả khác với S1; sinh viên có mặt ở cả kỳ mở huấn luyện lẫn kỳ mở kiểm định chưa được loại ở các fold vòng trong | Chấp nhận | Cùng chỉ số với S1; ngưỡng chênh lệch khoảng 89 sinh viên; loại các sinh viên này ở mọi vòng, cả vòng ngoài lẫn vòng trong |
| 8 | Điều kiện kiểm định công bằng không phát hiện được vấn đề ở nhóm nhỏ; quy tắc lẫn lộn giữa kiểm định hai phía và một phía | Chấp nhận | Điều kiện đưa nhóm vào kiểm định xác định từ số lượt đăng ký học; kiểm định một phía; hiệu chỉnh Holm; ghi "chưa được xác nhận đạt" cho nhóm nhỏ |
| 9 | ABROCA thiếu giá trị tham chiếu | Chấp nhận | Tính trong từng kỳ mở, giá trị tham chiếu bằng hoán vị, báo cáo dấu, chỉ để mô tả |
| 10 | Ở tỷ lệ nền này, tỉ số odds phóng đại độ lớn của hiệu ứng; ngưỡng quá dễ đạt; AQ2 và AQ3 phụ thuộc nhau | Chấp nhận | Dùng chênh lệch nguy cơ, với hiệu ứng nhỏ nhất có ý nghĩa là 5 điểm phần trăm; quy tắc được chốt trước; kết quả AQ2 năm 2014 không thể thay đổi AQ3 |
| 11 | Phân tích lỗi còn khoảng trống | Chấp nhận | Sinh viên không hoàn thành còn liên hệ được, sinh viên có hoạt động, độ ổn định của danh sách, phân tích theo lịch sử học tập, CCC |
| 12 | Thiếu rủi ro và có biện pháp kiểm soát không khớp với rủi ro | Chấp nhận | Mười sáu rủi ro ở Bảng A.9; biện pháp kiểm soát cho rủi ro hiểu nhầm hệ số là nguyên nhân (R9), khẳng định việc liên hệ có hiệu quả (R10) và thiên kiến tự động hóa (R13) được gắn đúng với rủi ro tương ứng |

Mỗi AI rà soát là một phiên AI tạo sinh riêng biệt, chỉ được đọc đề bài và các phụ lục nêu trong prompt của phiên đó; chúng em đối chiếu từng nhận xét với các thông tin làm căn cứ của thiết kế trước khi quyết định. Các prompt được trình bày bằng tiếng Anh, ở dạng rút gọn; các tài liệu được gọi theo vị trí trong báo cáo này. AI phản biện lựa chọn mô hình nhận chỉ dẫn sau:

> You act as the "Model selection" reviewer role that the MTH045 Milestone 4 brief allows for generative AI (brief
> section 11). Read only the brief, the AQ Modeling Briefs (Section 2.1), the candidate comparison (Appendix I) and the
> sample sizes and counts from the prepared data (Appendix III). Do not search the web, do not open any data file, do
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
> section 11). Read only the brief, the Evaluation Design Cards and metric definitions (Appendix II), the validation
> and test protocol (Appendix III), the error and fairness analysis (Appendix IV), the risk register (Appendix V) and the
> counts from the prepared data. Do not search the web, do not open any data file, do not invent results, benchmarks or
> performance numbers. Review the evaluation design as a sceptical methodologist: (1) whether each metric reflects the
> decision it serves and whether any metric is misleading for this base rate; (2) whether the success criteria are
> fixed in advance, falsifiable, internally consistent, and neither trivially easy nor impossible; (3) validation:
> leakage paths, test reuse, grouping of students across runs and years, nested tuning, the AQ2/AQ3 interaction; (4)
> uncertainty estimation with 9 training and 13 test runs; (5) calibration criteria and what happens when they fail;
> (6) fairness: choice of criterion, small groups, multiple comparisons, interpretation of ABROCA; (7) error analysis
> gaps; (8) risks missing from the register or controls that do not match their risk. Write at most 12 numbered
> critiques, most important first, each with the passage, the problem, why it matters and a concrete recommendation.
