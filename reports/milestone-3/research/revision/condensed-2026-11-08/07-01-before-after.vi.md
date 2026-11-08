## 7.1. Kiểm tra trước và sau chuẩn bị

Bước chuẩn bị không thay đổi biến kết quả hay số đếm nào nếu không có quy tắc nêu rõ. Bảng 7.1 thể hiện điều này cho
từng phép so sánh mà đề bài yêu cầu. Ở dòng tổng thể, số sinh viên đang học tại ngày 13 lớn hơn tại ngày 14, vì số sinh
viên rút vào ngày 14 nhiều hơn số sinh viên đăng ký thêm vào ngày đó.

**Bảng 7.1. Các phép kiểm tra trước và sau chuẩn bị**

| Phép kiểm tra | Trước (dữ liệu gốc) | Sau (dữ liệu đã chuẩn bị) | Trạng thái |
| :---- | :---- | :---- | :---- |
| Lượt đăng ký học, sinh viên, cơ cấu kết quả | 32.593; 28.785; bốn loại kết quả | giống hệt; không bỏ dòng nào | PASS |
| Tổng thể (C09) | 32.593 lượt đăng ký học | 28.061 tại ngày 14; 28.069 tại ngày 13; 27.535 tại ngày 27 | PASS |
| Lượt nhấp | 39.605.099 | 39.506.354 được giữ + 98.745 sau khi rút | PASS |
| Giá trị thiếu | 1.111 / 45 / 173 | giống hệt, không điền giá trị thiếu | PASS |
| Khóa, miền giá trị, thứ tự thời gian | duy nhất; điểm 0–100; tín chỉ 30–655 | duy nhất trong mọi bảng; cùng miền giá trị; không có tuần nào sau khi rút | PASS |
| Đặc trưng dẫn xuất | – | 6 đặc trưng được tính lại từ dữ liệu gốc cho 55.604 dòng: 0 khác biệt | PASS |
| Rò rỉ thông tin | – | đặc trưng chỉ thay đổi ở 26.755 (ngày 13) và 25.663 (ngày 27) lượt đăng ký học có lượt nhấp sau thời điểm chốt | PASS |

Ngoài việc tính lại mọi dòng đặc trưng, chín kiểm thử đơn vị trên dữ liệu giả lập xác nhận từng công thức. Bên cạnh
đó, một dòng được đếm lại thủ công từ các tệp gốc trùng khớp với bảng dữ liệu đã chuẩn bị: một TMA đến hạn vào ngày 19, được
nộp vào ngày 24, với 168 lượt nhấp trong 10 ngày có hoạt động tính đến hết ngày 27.
