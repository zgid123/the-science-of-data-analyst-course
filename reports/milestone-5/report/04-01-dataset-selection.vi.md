## 4.1. Lựa chọn bộ dữ liệu, nguồn gốc dữ liệu và giấy phép

Ở Milestone 2, nhóm tìm kiếm trên các kho dữ liệu, trong đó có Kho dữ liệu học máy của Đại học California tại Irvine (UCI), bằng các từ khóa rút ra từ yêu cầu dữ liệu và sàng lọc bảy bộ dữ liệu ứng viên. Mỗi ứng viên được cho
điểm từ 0 đến 2 theo mười tiêu chí của đề bài, trong đó các điều kiện bắt buộc được xét trước (Bảng 4.2; điểm chi tiết
ở Bảng A.10, Phụ lục IV). OULAD là ứng viên duy nhất ghi nhận ngày rút khỏi module, ngày nộp bài và số lượt nhấp theo
ngày, nên được chọn vì phù hợp với các câu hỏi chứ không phải vì dễ truy cập. OULAD chỉ được chọn với điều kiện các tệp dữ liệu
xác nhận ba điều: giá trị kết quả tách được đạt với không đạt (G1), mỗi module có đủ kỳ mở để kiểm tra mô hình (G3) và
mã sinh viên không đổi giữa các kỳ mở (G5). Bước kiểm tra cấu trúc đã xác nhận G1 và G5; riêng G3 chỉ đạt ở 5 trong 7
module, là các module có ba hoặc bốn kỳ mở. Bản dữ liệu của nhóm là phiên bản 1 trên figshare (doi:10.6084/m9.figshare.5081998.v1), truy
cập ngày 06/11/2026, kèm mã kiểm tra (checksum) SHA-256 (thuật toán băm an toàn 256 bit) ghi sẵn làm giá trị tham chiếu
(Bảng A.11). Bộ dữ liệu được mô tả trong bài mô tả dữ liệu của Kuzilek, Hlosta và Zdrahal và được phát hành ở dạng ẩn
danh theo giấy phép CC BY 4.0 [5]; nhóm không thực hiện bất kỳ thao tác tái định danh nào.

**Bảng 4.2. Ma trận lựa chọn bộ dữ liệu**

| Ứng viên | Tổng điểm (trên 20) | Điều kiện bắt buộc không đạt | Quyết định |
| :---- | :---- | :---- | :---- |
| A OULAD | 12 | Không có | Được chọn với điều kiện tệp dữ liệu xác nhận ba điều (G1, G3, G5) |
| B UCI 697; C UCI 320; D UCI 856 | 10; 6; 7 | G1, G2a, G2b (C và D không đạt thêm G3) | Bị loại |
| E XuetangX; F HarvardX | 8; 8 | G1, G2a, G4 (F không đạt thêm G2b, G3) | Bị loại |
| G xAPI-Edu-Data | 4 | G1, G2a, G2b, G3 | Bị loại |
