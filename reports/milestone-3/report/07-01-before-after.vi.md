## 7.1. Kiểm tra trước và sau chuẩn bị

Bước chuẩn bị chỉ thay đổi biến kết quả hoặc số đếm khi có một quy tắc nêu rõ. Bảng 7.1 trình bày từng phép so sánh mà đề bài yêu cầu, gồm giá trị trong dữ liệu gốc, giá trị trong dữ liệu đã chuẩn bị và kết quả kiểm tra.

**Bảng 7.1. Các phép kiểm tra trước và sau chuẩn bị**

| Phép kiểm tra | Trước (dữ liệu gốc) | Sau (dữ liệu đã chuẩn bị) | Trạng thái |
| :---- | :---- | :---- | :---- |
| Lượt đăng ký học, sinh viên, cơ cấu kết quả (V01) | 32.593 lượt đăng ký học; 28.785 sinh viên; 12.361 Pass, 10.156 Withdrawn, 7.052 Fail, 3.024 Distinction | Giống hệt; không bỏ dòng nào | PASS |
| Lượt đăng ký học được xét (V01, C09) | 32.593 lượt đăng ký học | 28.061 tại ngày 14; 28.069 tại ngày 13; 27.535 tại ngày 27, khớp với kết quả khảo sát dữ liệu | PASS |
| Số lượt không hoàn thành trong các bảng đặc trưng (V01) | 12.708 tại ngày 13; 12.156 tại ngày 27 theo kết quả khảo sát dữ liệu | Giống hệt | PASS |
| Lượt nhấp (V04) | 39.605.099 | 39.506.354 lượt được giữ, cộng với 98.745 lượt phát sinh sau khi rút khỏi module, bằng đúng tổng gốc; tổng của bảng theo tuần bằng đúng số lượt được giữ | PASS |
| Giá trị thiếu (V02) | imd_band 1.111; ngày đăng ký 45; điểm 173 | Giống hệt, không điền giá trị thiếu | PASS |
| Khóa (V03) | Không trùng lặp trong sáu bảng có khóa | Không trùng lặp trong mọi bảng dữ liệu đã chuẩn bị | PASS |
| Nhóm giá trị và miền giá trị (V05, V07) | Điểm 0–100; tín chỉ 30–655 | Cùng miền giá trị; mọi nhãn thuộc tập giá trị kỳ vọng | PASS |
| Thứ tự thời gian (V08) | Có hoạt động sau khi rút | Không tuần nào sau tuần rút khỏi module được tính | PASS |
| Phép nối bảng (V09, V10) | – | 25 phép nối, số dòng vào bằng số dòng ra; 3.554 lượt đăng ký học không có dòng lượt nhấp được giữ với giá trị 0 | PASS |
| Đặc trưng dẫn xuất (V11) | – | 6 đặc trưng (lượt nhấp trước và sau ngày 0, số ngày có hoạt động, số tài nguyên học tập, số bài bỏ lỡ và nộp trễ) được tính lại từ dữ liệu gốc bằng mã độc lập cho cả 55.604 dòng đặc trưng: 0 khác biệt | PASS |
| Rò rỉ thông tin (V13) | – | Khi đếm lại các đặc trưng lượt nhấp mà bỏ bộ lọc theo ngày, giá trị chỉ thay đổi ở 26.755 (ngày 13) và 25.663 (ngày 27) lượt đăng ký học có lượt nhấp sau thời điểm chốt dữ liệu, nên bộ lọc theo ngày hoạt động đúng; không bảng nào chứa cột suy ra từ biến mục tiêu | PASS |
| Phép biến đổi có tham số ước lượng từ dữ liệu (V12) | – | Tham số giống hệt khi các dòng của tập kiểm thử bị thay đổi | PASS |
| Tài liệu mô tả và cách chia dữ liệu (V14, V15) | – | Mọi cột đều được mô tả và có vai trò; 9 kỳ mở huấn luyện và 13 kỳ mở của tập kiểm thử, không kỳ mở nào thuộc cả hai | PASS |

Số lượt đăng ký học không có lượt nhấp tăng từ 3.365 lên 3.554, vì 189 sinh viên chỉ có lượt nhấp sau khi hủy đăng ký nay không còn lượt nhấp nào được tính. Bên cạnh đó, phép kiểm tra rò rỉ thông tin được thiết kế để báo lỗi (FAIL) nếu bất kỳ đặc trưng nào dùng một lượt nhấp muộn hơn thời điểm chốt dữ liệu. Ngoài việc tính lại mọi dòng đặc trưng, chín kiểm thử đơn vị chạy trên các bản ghi giả lập xác nhận từng công thức. Đồng thời, một dòng được đếm lại thủ công từ các tệp gốc khớp với bảng dữ liệu đã chuẩn bị; Phụ lục VI giải thích đầy đủ các phép kiểm tra này.
