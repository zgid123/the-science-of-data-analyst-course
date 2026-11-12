# 7. Chuẩn bị dữ liệu và dữ liệu sẵn sàng cho phân tích

Trên cơ sở các vấn đề chất lượng dữ liệu đã nêu, trong Milestone 3, nhóm đã xây dựng quy trình chuẩn bị dữ liệu (pipeline) để chuyển bảy bảng dữ liệu gốc thành
các bảng dữ liệu đã chuẩn bị, sẵn sàng cho phân tích; mọi phân tích trong báo cáo đều đọc dữ liệu từ các bảng này. Trước
khi thay đổi bất kỳ bản ghi nào, nhóm ghi cho mỗi vấn đề một quyết định xử lý kèm lý do. Mỗi quyết định có một phép
kiểm tra tự động, đánh mã từ V01 đến V15: phép kiểm tra chạy trên dữ liệu sau xử lý và báo lỗi khi quyết định chưa được
thực hiện đúng. Ba quyết định chi phối kết quả: các bảng giữ nguyên mọi dữ
liệu đã ghi nhận, không xóa dòng nào và không điền giá trị thiếu; mọi đặc trưng chỉ dùng các sự kiện có mốc thời gian tính đến hết thời điểm chốt dữ liệu
của đặc trưng đó; mọi tham số ước lượng từ dữ liệu chỉ lấy từ các kỳ mở huấn luyện. Bảng 7.1 là Ma trận quyết định chuẩn
bị dữ liệu (Preparation Decision Matrix), còn Bảng A.17 (Phụ lục VII) bổ sung lý do của từng quyết định; Phụ lục VII
cũng trình bày mười bước xử lý bằng mã của pipeline cùng số liệu của từng bước.

**Bảng 7.1. Ma trận quyết định chuẩn bị dữ liệu**

| Nhu cầu | Quyết định | Phép kiểm tra |
| :---- | :---- | :---- |
| Phạm vi dữ liệu | Mỗi lượt đăng ký học có cờ cho biết sinh viên còn đăng ký học (chưa rút) tại ngày 13, 14 và 27 hay không (C09); các bảng đặc trưng chỉ giữ lượt đăng ký học chưa rút tại thời điểm chốt dữ liệu | V01 |
| Giá trị thiếu | Nhóm giá trị "Missing" hoặc biến chỉ báo giá trị thiếu; không điền giá trị thiếu | V02, V12 |
| Dòng trùng lặp, khóa, tích hợp bảng | Giữ mọi dòng; cộng số lượt nhấp theo ngày; nối trái (left join) từ bảng lượt đăng ký học | V03, V04, V09, V10 |
| Giá trị không hợp lệ, giá trị ngoại lai | Sửa nhãn ghi sai của mức khó khăn của khu vực; kết quả bảo lưu (chuyển từ kỳ mở trước) không dùng để xác định thời điểm; giữ mọi giá trị | V05–V07 |
| Hoạt động sau khi rút khỏi module | Cắt tại ngày hủy đăng ký | V08 |
| Đặc trưng dẫn xuất | Bài TMA và CMA; quy tắc dấu hiệu sớm (C10); hoạt động so với trung vị của kỳ mở | V11 |
| Thời gian, mã hóa | Thời điểm chốt dữ liệu ở ngày 13 và ngày 27; phép biến đổi được ước lượng trên các dòng huấn luyện | V12, V13 |
| Thuộc tính nhạy cảm, cách chia dữ liệu | Cột phục vụ kiểm tra công bằng nằm ngoài các biến dự báo; huấn luyện trên năm 2013, kiểm tra trên năm 2014 | V14, V15 |
