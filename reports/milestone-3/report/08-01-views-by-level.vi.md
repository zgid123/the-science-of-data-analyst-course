## 8.1. Các bảng dữ liệu đã chuẩn bị theo mức phân tích

Mỗi mức phân tích có bảng dữ liệu đã chuẩn bị riêng; bảng của mỗi mức dựa trên bảng của mức trước và bổ sung thêm thông tin. Đề bài đặt ra
một yêu cầu kiểm tra cho từng mức trước khi bước vào Milestone 4: bảng mô tả phải cho số liệu tổng hợp không đếm trùng và
không bị lệch do phép nối bảng; bảng chẩn đoán phải tính mối liên hệ từ dữ liệu thật, có nhóm so sánh; bảng dự báo phải có
biến mục tiêu, thời điểm dự báo, các đặc trưng lấy từ trước thời điểm đó, cách chia dữ liệu và đủ số trường hợp ở mỗi
lớp nhãn; bảng chỉ định cần dữ liệu về hành động, ràng buộc, chi phí và kết quả [1]. Với từng mức, Phụ lục III (Bảng A.11)
nêu bảng dữ liệu đã chuẩn bị, các lượt đăng ký học được xét, đơn vị của mỗi dòng (grain), yêu cầu kiểm tra của đề bài và kết quả kiểm tra;
các đoạn dưới đây trình bày lại những nội dung đó.

Các bảng mô tả, gồm enrolment, assessment_due và student_week, tính tỷ lệ trên đúng mẫu số, vì mỗi lượt đăng ký học chỉ xuất hiện một lần và các nhóm lượt đăng ký học theo quy tắc của Mục 4.1 chỉ được ghi thành cột cờ, không dùng để lọc bỏ dòng. Ngoài ra, khóa của các bảng này không trùng lặp, mọi phép nối bảng đều giữ nguyên số dòng và số lượt nhấp khớp với nhật ký gốc. Bảng chẩn đoán là features_d27, dùng kèm bảng enrolment. Bảng này bổ sung các dấu hiệu tại ngày 27 cho 27.535 lượt đăng ký học còn hiệu lực tại ngày đó, nhờ đó mối liên hệ giữa các dấu hiệu này và việc không hoàn thành được so sánh riêng trong từng module (OULAD có bảy module).
Các bảng dự báo, gồm features_d13, features_d27 và các ma trận sẵn sàng cho mô hình, bổ sung thêm một thời điểm chốt dữ
liệu tại ngày 13, cách chia dữ liệu theo thời gian thành 9 kỳ mở huấn luyện và 13 kỳ mở của tập kiểm thử, cùng các phép biến đổi có tham số ước lượng (fit) trên các kỳ mở huấn luyện. Ở mọi kỳ mở, lớp thiểu số (lớp có ít lượt đăng ký học hơn) có ít nhất 92 lượt đăng ký học.
Bảng chỉ định capacity_by_run chỉ cung cấp độ dài danh sách theo các giả định về năng lực liên hệ mỗi
tuần. Lý do là dữ liệu không ghi nhận hành động, chi phí hoặc kết quả nào sau khi liên hệ, đồng thời đề bài không cho phép
biến một kết quả dự báo thành kết quả của phân tích chỉ định chỉ bằng cách kèm thêm lời khuyên [1].
