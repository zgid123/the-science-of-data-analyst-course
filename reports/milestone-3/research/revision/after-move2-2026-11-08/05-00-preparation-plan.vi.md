# 5. Kế hoạch chuẩn bị dữ liệu

Trước khi thay đổi bất kỳ bản ghi nào, nhóm tác giả đã đưa ra cho mỗi vấn đề trong Bảng 3.1 một quyết định kèm lý do,
cách thực hiện và cách kiểm tra, đúng như đề bài yêu cầu [1]. Các quyết định này tránh những cách làm mà đề bài nêu rõ: điền mọi giá
trị thiếu bằng giá trị trung bình, xóa mọi dòng trùng lặp, xóa mọi giá trị nằm ngoài khoảng tứ phân vị, dùng dữ liệu
tương lai để tạo đặc trưng cho quá khứ và loại bỏ các thuộc tính nhạy cảm mà bước kiểm tra công bằng cần đến [1].
Bảng 5.1 trình bày Ma trận quyết định chuẩn bị dữ liệu (Preparation Decision Matrix); các phép kiểm tra V01–V15 được
trình bày ở Mục 7, còn toàn bộ ma trận nằm trong tệp `data/metadata/decision_matrix.md`.

**Bảng 5.1. Ma trận quyết định chuẩn bị dữ liệu**

| Vấn đề | Quyết định | Lý do | Cách thực hiện | Kiểm tra |
| :---- | :---- | :---- | :---- | :---- |
| Tổng thể | Gắn cờ mọi lượt đăng ký học; bảng đặc trưng giữ những lượt đang học tại thời điểm chốt | KPI và các danh sách liên hệ chỉ xét sinh viên đang theo học | Quy tắc đang đăng ký học vào ngày d (C09) | V01 |
| Giá trị thiếu | Nhóm "Missing"; biến chỉ báo; không điền giá trị thiếu trong bảng | Giá trị thiếu mang thông tin hoặc chiếm tỷ lệ nhỏ | Riêng ma trận đầu vào của mô hình điền ô thiếu bằng trung vị của tập huấn luyện | V02, V12 |
| Dòng trùng lặp và khóa | Giữ mọi dòng lượt nhấp; cộng theo ngày; thêm phiên bản đã loại dòng trùng | Không xác định được nguyên nhân trùng; giữ đúng mức chi tiết của bản ghi | Tổng hợp số liệu trước khi nối bảng | V03, V04 |
| Nhãn / kiểu không hợp lệ | Sửa nhãn "10-20"; không gán thời điểm cho kết quả bảo lưu | Ngày −1 chỉ là giá trị giữ chỗ | Trạng thái "banked" | V05, V06 |
| Giá trị ngoại lai | Giữ mọi giá trị | Đây là những sinh viên hoạt động nhiều và những bài nộp trễ có thật | Chỉ áp dụng log1p trong các ma trận cho mô hình | V07 |
| Hoạt động sau khi rút | Cắt bỏ từ ngày hủy đăng ký | Hoạt động này không phản ánh mức tham gia khi còn đăng ký học | Lọc theo ngày | V08 |
| Tích hợp bảng | Nối trái; điền số đếm 0 | Phép nối trong (inner join) làm mất 3.365 lượt đăng ký học | Phép nối bảng có kiểm tra | V09, V10 |
| Đặc trưng dẫn xuất | TMA và CMA không trọng số; điểm CMA sau 7 ngày; quy tắc của C10 | Dữ liệu không có kết quả thi và ngày công bố điểm | Bảng 6.1 | V11 |
| Tổng hợp theo thời gian | Tuần 7 ngày; thời điểm chốt ngày 13 và 27 | Đây là các thời điểm dự báo của Milestone 2 | Lọc dữ liệu tính đến hết thời điểm chốt | V13 |
| Mã hóa và chuẩn hóa thang đo | Giữ thang đo gốc trong bảng; ma trận cho mô hình tuyến tính fit trên các kỳ mở 2013 | Không kỳ mở nào của tập kiểm thử ảnh hưởng đến tham số | Mã hóa thứ bậc, one-hot, log1p, chuẩn hóa | V12 |
| Thuộc tính nhạy cảm | Giữ làm cột kiểm tra công bằng | Cần để so sánh kết quả giữa các nhóm sinh viên | Vai trò "audit" | V14 |
| Chia dữ liệu | Huấn luyện 2013, kiểm thử 2014 | Kết luận cần đúng cho các kỳ mở diễn ra sau | Cờ chia dữ liệu | V15 |
