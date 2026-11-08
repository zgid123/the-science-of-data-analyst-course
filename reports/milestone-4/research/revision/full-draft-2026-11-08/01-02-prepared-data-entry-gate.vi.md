## 1.2. Dữ liệu đã chuẩn bị và điều kiện đầu vào

Bộ dữ liệu đã chuẩn bị OULAD-N04-prepared-1.0 gồm một bảng có mỗi dòng ứng với một lượt đăng ký học và hai bảng đặc trưng, mỗi bảng ứng với một thời điểm chốt dữ liệu: hết ngày 13 (tuần 2) và hết ngày 27 (tuần 4). Mỗi bảng đặc trưng chỉ giữ các lượt đăng ký học còn hiệu lực tại thời điểm chốt dữ liệu và chỉ dùng thông tin ghi nhận tính đến hết thời điểm đó. Biến mục tiêu non_completion nhận giá trị dương khi kết quả cuối cùng là Không đạt (Fail) hoặc Rút khỏi module (Withdrawn). Tập huấn luyện gồm 9 kỳ mở năm 2013, với 11.811 lượt đăng ký học và 5.245 sinh viên không hoàn thành (44,4%) tại ngày 27. Tập kiểm thử gồm 13 kỳ mở năm 2014 với 15.724 kết quả tại ngày 27; các kết quả này được giữ kín cho đến lần kiểm thử cuối cùng, chỉ thực hiện một lần (Phụ lục IV, Bảng A.14).

Đề bài chỉ cho một nhóm bước vào mô hình hóa khi đáp ứng đủ năm điều kiện [1]. Bảng 1.2 nêu bằng chứng cho từng điều kiện.

**Bảng 1.2. Điều kiện đầu vào**

| Điều kiện | Bằng chứng từ Milestone 3 | Trạng thái |
| :---- | :---- | :---- |
| Các AQ đã được duyệt | AQ1–AQ3 sẵn sàng; AQ4 ở dạng xếp hạng, phần liên hệ được hoãn (thay đổi C11 và C13 trong Nhật ký thay đổi) | Đạt |
| Bộ dữ liệu đã chuẩn bị | OULAD-N04-prepared-1.0: từ điển dữ liệu, đơn vị phân tích, khóa, biến mục tiêu, khoảng thời gian lấy đặc trưng | Đạt |
| Kiểm soát rò rỉ thông tin | Thời điểm chốt dữ liệu ở ngày 13 và ngày 27; chia dữ liệu theo năm; các phép biến đổi học tham số từ dữ liệu năm 2013; đạt cả 22 trên 22 phép kiểm tra | Đạt |
| Các hạn chế đã biết | 19 vấn đề chất lượng dữ liệu đã ghi nhận (DQ01–DQ19); thuộc tính dùng để kiểm tra công bằng; tính đại diện và bảo vệ dữ liệu | Đạt |
| Truy vết | AQ → yêu cầu dữ liệu → biến gốc và biến đã chuẩn bị | Đạt |

Cả năm điều kiện đều đạt, nên các câu hỏi có thể được mô hình hóa ở dạng hiện hành, còn phần liên hệ của AQ4 tiếp tục được hoãn. Thiết kế đánh giá dẫn đến một thay đổi trong cách đo AQ2; thay đổi này được ghi là thay đổi C14 trong Nhật ký thay đổi (Mục 4.2; Phụ lục VIII).
