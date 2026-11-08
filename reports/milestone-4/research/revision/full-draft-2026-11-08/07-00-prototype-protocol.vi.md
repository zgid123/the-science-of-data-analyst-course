# 7. Giao thức chạy nguyên mẫu

Nguyên mẫu (prototype) không bắt buộc của Level 2 kiểm tra tính khả thi của các lựa chọn ở Level 1, không nhằm cạnh tranh để đạt điểm số cao nhất [1]. Trên cơ sở thiết kế đánh giá ở Phần 4, Bảng 7.1 đặc tả cách chạy nguyên mẫu theo từng bước mà đề bài quy định. Do bản đề xuất được chốt trước, nguyên mẫu có thể xác nhận hoặc bác bỏ các lựa chọn nhưng không thể thay đổi các lựa chọn này.

**Bảng 7.1. Giao thức chạy nguyên mẫu**

| Bước của đề bài | Đặc tả |
| :---- | :---- |
| 1. Tái lập dữ liệu đầu vào | Nạp OULAD-N04-prepared-1.0, kiểm tra mã băm (hash) của các tệp, không thay đổi dữ liệu gốc |
| 2. Cài đặt phương pháp cơ sở (baseline) | Danh sách xếp theo quy tắc dấu hiệu sớm, mô hình chỉ dùng đặc điểm cá nhân (background-only model) và danh sách ngẫu nhiên, cài đặt trước mọi phương pháp ứng viên |
| 3. Cài đặt phương pháp ứng viên | Hồi quy logistic có hiệu chỉnh phạt (penalised logistic regression) làm phương pháp chính (primary approach) và cây tăng cường độ dốc (gradient-boosted trees) làm mô hình đối sánh (challenger) (Bảng 3.1) |
| 4. Chia dữ liệu và ước lượng đúng cách | Giao thức ở Mục 4.2 và Phụ lục IV |
| 5. Đánh giá | Các chỉ số và tiêu chí ở Bảng 4.2, kể cả các kết quả không thuận lợi |
| 6. Phân tích lỗi và phân tích theo nhóm con | Phân tích lỗi theo từng nhóm con và kiểm định khẳng định về tính công bằng (Mục 4.4) |
| 7. So sánh với kỳ vọng ở Level 1 | Xem S1 có được thỏa mãn hay không và mô hình đối sánh có vượt phương pháp chính đúng mức chênh lệch đã ấn định hay không; mọi thay đổi được ghi lại kèm lý do |
| 8. Khả năng tái lập | Nhật ký thí nghiệm lưu mã nguồn (script), giá trị khởi tạo ngẫu nhiên (seed), phiên bản gói phần mềm và dữ liệu, các fold (phần chia trong kiểm định chéo) và bản ghi các lần truy cập tập kiểm thử |

Phương pháp cơ sở đạt kết quả ngang bằng phương pháp ứng viên vẫn là một kết quả chấp nhận được, vì một phương pháp cơ sở đơn giản có thể là lựa chọn tốt hơn [1]. Khi đó, quy tắc dấu hiệu sớm hoặc mô hình chỉ dùng đặc điểm cá nhân được giữ lại cho giai đoạn sau, kèm lý do của lựa chọn này.
