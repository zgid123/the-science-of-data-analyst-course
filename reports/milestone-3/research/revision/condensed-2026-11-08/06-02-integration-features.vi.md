## 6.2. Tích hợp bảng và xây dựng đặc trưng

Phép tích hợp bắt đầu từ bảng lượt đăng ký học, rồi thêm từng bảng còn lại bằng phép nối trái (left join) có kiểm tra;
cả 25 phép nối đều giữ nguyên số dòng đầu vào. Lượt nhấp được cộng theo lượt đăng ký học và ngày, sau đó theo tuần,
giống cách chính OU tổng hợp lượt nhấp theo tuần và loại nội dung để cảnh báo sớm [9]. Mỗi đặc trưng chỉ dùng các bản
ghi có ngày tính đến hết thời điểm chốt dữ liệu của đặc trưng đó, vì một mô hình hợp lệ chỉ được dựa trên thông tin
có trước biến mục tiêu [10]. Bên cạnh đó, rò rỉ thông tin thường xảy ra qua những bản ghi được cập nhật về sau mà không
kèm dấu thời gian [10]; ở OULAD, điểm số là ví dụ, vì dữ liệu không ghi ngày công bố điểm. Bảng 6.1 định nghĩa các biến dẫn xuất chính; từ điển dữ liệu (Phụ lục III) liệt kê
đủ 20 biến dự báo chính và 10 biến dự báo mở rộng.

**Bảng 6.1. Các biến dẫn xuất chính**

| Biến | Công thức | Trường nguồn | Quy tắc về khoảng thời gian / thời điểm |
| :---- | :---- | :---- | :---- |
| non_completion (biến mục tiêu) | final_result là Fail hoặc Withdrawn | studentInfo | Cuối kỳ mở; không bao giờ dùng làm đặc trưng |
| clicks_0c, activity_ratio_run | Số lượt nhấp từ ngày 0 đến thời điểm chốt c; (clicks_0c + 1) ÷ (trung vị clicks_0c của các sinh viên đang đăng ký học trong kỳ mở + 1) | studentVle | Cùng kỳ mở, tính đến hết ngày c, không dùng biến kết quả |
| inactive_last7 | Không có lượt nhấp nào từ ngày c − 6 đến ngày c | studentVle | Bảy ngày kết thúc tại c |
| tasks_missed_c | TMA hoặc CMA đến hạn tính đến hết ngày c và sau ngày đăng ký, nhưng chưa được nộp tính đến hết ngày c | assessments, studentAssessment | Tính đến hết ngày c; loại kết quả bảo lưu |
| tma_late_c, cma_late_c | Bài đến hạn tính đến hết ngày c và được nộp sau ngày đến hạn, nhưng vẫn trong phạm vi đến hết ngày c | assessments, studentAssessment | Tính đến hết ngày c |
| early_sign_rule | Bỏ lỡ một bài, nộp trễ một TMA hoặc không hoạt động trong bảy ngày gần nhất | dẫn xuất | Tại c (C10) |

Các thuộc tính nhân khẩu học chủ yếu phục vụ bước kiểm tra công bằng, vì các thực nghiệm trước đây của OU cho thấy việc bổ
sung các thuộc tính này vào dữ liệu hoạt động và dữ liệu bài đánh giá không cải thiện đáng kể khả năng dự báo sinh viên
có nguy cơ [9].
