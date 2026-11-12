## 7.1. Biến dẫn xuất, mã hóa và kiểm soát rò rỉ thông tin

Mọi đặc trưng chỉ dùng các bản ghi có mốc thời gian tính đến hết thời điểm chốt dữ liệu của đặc trưng đó. Vì vậy, hoạt
động sau thời điểm chốt dữ liệu, ngày rút khỏi module và kết quả cuối cùng không được dùng để tính bất kỳ đặc trưng nào; điểm TMA cũng không
được dùng vì không có ngày công bố điểm. Các biến dẫn xuất gồm số lượt nhấp trước và sau ngày 0, hoạt động so với trung
vị của cùng kỳ mở, tình trạng không có hoạt động trong bảy ngày gần nhất, các bài bị bỏ lỡ hoặc nộp trễ và quy tắc dấu
hiệu sớm (Bảng A.18, Phụ lục VII). Bộ biến dự báo chính gồm 19 biến dự báo dùng được, tương ứng 23 tham số sau khi mã hóa
module và tháng bắt đầu. Mọi phép biến đổi được ước lượng lại trong từng fold phát triển (fold, tức một phần chia của
kiểm định chéo). Các số hạng module được mã hóa theo độ lệch so với trung bình (deviation coding); nhờ cách mã hóa này,
một module chưa có trong dữ liệu huấn luyện được gán hiệu ứng bằng mức trung bình của các module. Rò rỉ thông tin là việc dùng thông tin chưa thể có tại thời điểm dự báo.
Nhóm chặn rò rỉ thông tin bằng bốn biện pháp: quy tắc thời gian nêu trên; chỉ ước lượng tham số trên dữ liệu năm
2013; chia dữ liệu theo năm; đánh dấu 1.586 lượt đăng ký học của tập kiểm thử tại ngày 27 thuộc về các sinh viên đã học
trong năm 2013, vì mô hình có thể đã "biết" những sinh viên này từ dữ liệu huấn luyện (Bảng A.19). Phép kiểm tra bộ lọc
ngày thực sự phát hiện được lỗi: khi bỏ bộ lọc, giá trị đặc trưng thay đổi nhưng chỉ thay đổi ở những lượt đăng ký học
có lượt nhấp sau thời điểm chốt dữ liệu.
