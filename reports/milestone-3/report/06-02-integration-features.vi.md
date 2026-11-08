## 6.2. Tích hợp bảng và xây dựng đặc trưng

**Tích hợp bảng.** Phép tích hợp bắt đầu từ bảng lượt đăng ký học, mỗi dòng ứng với một trong 32.593 lượt đăng ký học, rồi thêm từng bảng còn lại bằng phép nối trái (left join) sau khi cộng bảng đó về mức lượt đăng ký học, nhờ đó không lượt đăng ký học nào bị mất và không dòng nào bị nhân bản. Mỗi phép nối bảng đều được kiểm tra: pipeline xác nhận số dòng sau phép nối bằng số dòng trước phép nối; cả 25 phép nối đều giữ nguyên số dòng đầu vào. Lượt nhấp được cộng theo lượt đăng ký học và ngày, sau đó theo tuần, giống cách chính OU tổng hợp lượt nhấp theo tuần và theo loại nội dung trong công tác cảnh báo sớm [9].

**Quy tắc thời điểm.** Mỗi đặc trưng chỉ dùng các bản ghi có ngày tính đến hết thời điểm chốt dữ liệu của đặc trưng đó. Một mô hình hợp lệ chỉ được dựa trên thông tin đã có trước khi biết giá trị biến mục tiêu. Nói chung, một nguồn rò rỉ phổ biến là các bản ghi được cập nhật về sau nhưng không lưu dấu thời gian của lần cập nhật: giá trị mà mô hình đọc được khi đó có thể đã chứa thông tin phát sinh sau thời điểm dự báo [10]. Hoạt động trước ngày 0 được giữ thành một khoảng thời gian riêng, vì hoạt động này đã được ghi nhận trước khi bắt đầu giảng dạy. Các đặc trưng cần đến điểm chỉ dùng điểm CMA của những bài nộp sớm hơn thời điểm chốt dữ liệu ít nhất bảy ngày, vì điểm CMA dự kiến được công bố trong vòng bảy ngày [3] (quy định năm 2025, được giả định vẫn đúng cho giai đoạn 2013–2014); ngược lại, điểm TMA không có ngày công bố trong dữ liệu.

**Biến dẫn xuất.** Bảng 6.1 định nghĩa các biến dẫn xuất chính cùng công thức, trường nguồn và quy tắc thời điểm của từng biến; c là ngày chốt dữ liệu, bằng 13 hoặc 27.

**Bảng 6.1. Các biến dẫn xuất chính**

| Biến | Công thức | Trường nguồn | Quy tắc về khoảng thời gian / thời điểm |
| :---- | :---- | :---- | :---- |
| non_completion (biến mục tiêu) | final_result là Fail hoặc Withdrawn | studentInfo | Quan sát vào cuối kỳ mở; không bao giờ dùng làm đặc trưng |
| enrolled_d13, enrolled_d14, enrolled_d27 | Đã đăng ký đến ngày d (hoặc không rõ ngày đăng ký) và chưa hủy đăng ký đến ngày d | studentRegistration | Ngày d (C09) |
| clicks_pre | Số lượt nhấp trước ngày 0 | studentVle | Trước ngày bắt đầu |
| clicks_0c, active_days_0c | Số lượt nhấp và số ngày có ít nhất một lượt nhấp, từ ngày 0 đến ngày c | studentVle | Từ ngày 0 đến ngày c |
| activity_ratio_run | (clicks_0c + 1) ÷ (trung vị clicks_0c của các sinh viên đang đăng ký học trong kỳ mở + 1) | studentVle | Cùng kỳ mở, từ ngày 0 đến ngày c; không dùng biến kết quả |
| inactive_last7 | Không có lượt nhấp nào từ ngày c − 6 đến ngày c | studentVle | Bảy ngày kết thúc tại c |
| tasks_missed_c | TMA hoặc CMA đến hạn tính đến hết ngày c, có ngày đến hạn không sớm hơn ngày đăng ký, nhưng chưa được nộp tính đến hết ngày c | assessments, studentAssessment | Bài nộp tính đến hết ngày c; loại kết quả bảo lưu |
| tma_late_c, cma_late_c | Số bài đến hạn tính đến hết ngày c được nộp sau ngày đến hạn nhưng không muộn hơn ngày c, theo từng loại | assessments, studentAssessment | Bài nộp tính đến hết ngày c |
| cma_score_mean_c | Điểm trung bình của các CMA nộp tính đến hết ngày c − 7; để trống nếu không có | studentAssessment | Điểm đã biết tại c; được chuẩn bị nhưng không dùng làm đặc trưng (Mục 7.3) |
| early_sign_rule | Bỏ lỡ một bài, nộp trễ một TMA hoặc không hoạt động trong bảy ngày gần nhất | dẫn xuất | Tại c (C10) |
| early_sign_rule_cma | early_sign_rule hoặc nộp trễ một CMA | dẫn xuất | Tại c; phương án kiểm tra độ nhạy |
| first_missed_week | Tuần của bài đến hạn sớm nhất mà sinh viên chưa nộp; chỉ xét các bài đến hạn trong thời gian sinh viên còn đăng ký học | Bảng dữ liệu đã chuẩn bị assessment_due | Toàn bộ kỳ mở (chỉ dùng cho AQ1) |

Một bài chỉ được tính là bỏ lỡ nếu ngày đến hạn không sớm hơn ngày đăng ký của sinh viên. Ngoài ra, tỷ lệ hoạt động so sánh một sinh viên với trung vị của chính kỳ mở đó tính đến cùng ngày, không dùng đến biến kết quả. Các bảng đặc trưng gồm 20 đặc trưng chính và 10 đặc trưng mở rộng, cùng số lượt nhấp theo tuần; mỗi cột còn lại là mã định danh, biến mục tiêu, cờ phục vụ đánh giá, quy tắc dấu hiệu sớm hoặc thuộc tính dùng để kiểm tra công bằng. Các thuộc tính nhân khẩu học chủ yếu phục vụ bước kiểm tra công bằng, vì tại OU, việc bổ sung các thuộc tính này vào dữ liệu hoạt động và dữ liệu bài được chấm điểm không cải thiện đáng kể khả năng dự báo sinh viên có nguy cơ [9]. Phụ lục III giải thích các lựa chọn này và liệt kê các nhóm đặc trưng.
