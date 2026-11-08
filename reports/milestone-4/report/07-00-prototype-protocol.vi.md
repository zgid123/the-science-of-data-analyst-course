# 7. Giao thức chạy nguyên mẫu

**Mục đích.** Nguyên mẫu không bắt buộc của Level 2 kiểm tra xem các lựa chọn ở Level 1 có khả thi hay không và cho thấy ưu điểm và hạn chế của từng lựa chọn; nguyên mẫu không nhằm cạnh tranh để đạt điểm số cao nhất và không đòi hỏi tinh chỉnh siêu tham số trên quy mô lớn [1]. Báo cáo này không chạy nguyên mẫu nên không nêu hiệu năng của bất kỳ mô hình nào. Thay vào đó, báo cáo đặc tả cách chạy nguyên mẫu để bất kỳ ai chạy nguyên mẫu cũng tuân theo thiết kế đánh giá đã chốt ở Phần 4.

**Các bước.** Bảng 7.1 trình bày từng bước mà đề bài quy định và cách nguyên mẫu thực hiện bước đó. Do bản đề xuất được chốt trước, nguyên mẫu có thể xác nhận hoặc bác bỏ các lựa chọn ở Level 1 nhưng không thể điều chỉnh các lựa chọn này sau khi đã thấy kết quả.

**Bảng 7.1. Giao thức chạy nguyên mẫu**

| Bước của đề bài | Đặc tả |
| :---- | :---- |
| 1. Tái lập dữ liệu đầu vào | Nạp OULAD-N04-prepared-1.0, kiểm tra mã băm của các tệp, không thay đổi dữ liệu gốc |
| 2. Cài đặt phương pháp cơ sở | Danh sách xếp theo quy tắc dấu hiệu sớm, mô hình chỉ dùng đặc điểm cá nhân và danh sách ngẫu nhiên, cài đặt trước mọi phương pháp ứng viên |
| 3. Cài đặt phương pháp ứng viên | Hồi quy logistic có hiệu chỉnh phạt làm phương pháp chính và cây tăng cường độ dốc làm mô hình đối sánh, như ở Bảng 3.1 |
| 4. Chia dữ liệu và ước lượng đúng cách | Giao thức ở Mục 4.2 và Phụ lục III |
| 5. Đánh giá | Các chỉ số trong các Evaluation Design Card (Bảng 4.1–4.4) và các tiêu chí ở Bảng 4.5, kể cả các kết quả không thuận lợi |
| 6. Phân tích lỗi và phân tích theo nhóm con | Phân tích lỗi theo từng nhóm con và kiểm định khẳng định về tính công bằng ở Mục 4.4 |
| 7. So sánh với kỳ vọng ở Level 1 | Điều kiện đạt S1 có được đáp ứng hay không; mô hình đối sánh có vượt mức chênh lệch đã ấn định hay không; mọi thay đổi được ghi lại kèm lập luận |
| 8. Khả năng tái lập | Nhật ký thực nghiệm lưu script, giá trị khởi tạo ngẫu nhiên (seed), phiên bản gói phần mềm và dữ liệu, các fold và bản ghi các lần truy cập tập kiểm thử |

**Phương pháp cơ sở có thể được chọn.** Nếu phương pháp cơ sở đạt kết quả ngang bằng phương pháp ứng viên, kết quả đó vẫn được chấp nhận. Đề bài lưu ý rằng một phương pháp cơ sở đơn giản có thể là lựa chọn tốt hơn khi mô hình phức tạp chỉ cải thiện ít mà lại khó diễn giải hơn [1]. Khi đó, quy tắc dấu hiệu sớm hoặc mô hình chỉ dùng đặc điểm cá nhân được giữ lại cho giai đoạn sau kèm lập luận; thay đổi này được ghi vào nhật ký thực nghiệm.
