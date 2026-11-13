# 8. Chiến lược mô hình hóa và phân tích

Chiến lược mô hình hóa gắn mỗi câu hỏi với một loại phân tích, một bài toán kỹ thuật, một
phương pháp cơ sở (baseline), các phương pháp ứng viên và một phương pháp chính được đề xuất. Nhóm chúng em thiết kế
chiến lược này ở Milestone 4 theo Level 1 (mức bắt buộc của đề bài) và chưa huấn luyện mô hình nào. Sau đó, chúng em
chạy AQ1 và AQ2 đúng như đặc tả trên các kỳ mở năm 2013, rồi chạy lại trên các kỳ mở năm 2014. Trong khi đó, AQ3 và AQ4 được chạy dưới dạng nguyên mẫu Level 2 (Mục 10).
Mục đích của mỗi câu hỏi quyết định cách đọc kết quả của câu hỏi đó. Mô hình hóa dự báo nhằm dự báo các quan sát mới;
ngược lại, một mô hình hồi quy chỉ dùng để nắm bắt mối liên hệ thuộc loại mô tả [10]. Ngoài ra, khả năng giải thích tốt
không kéo theo khả năng dự báo tốt [10]. Do đó, kết quả AQ2 không được đọc như quan hệ nhân quả, còn AQ3 và AQ4 phải được
đánh giá trên các kỳ mở chưa dùng đến. Danh sách liên hệ phải được xếp hạng, vì quy tắc dấu hiệu sớm đánh dấu 28,8% số
lượt đăng ký học tại ngày 27, trong khi một danh sách chỉ chứa được 15% hoặc 25% số lượt đăng ký học của một kỳ mở; bên
cạnh đó, không có dữ liệu nào ghi lại một lần liên hệ hay kết quả của lần liên hệ đó. Từ bản mô tả yêu cầu mô hình hóa
(Modeling Brief) của từng AQ (Bảng A.22, Phụ lục VIII), chúng em xác định bốn bài toán: tổng hợp cho AQ1; đo mối liên hệ
trong cùng kỳ mở module cho AQ2; phân loại nhị phân tại ngày 13 và ngày 27 cho AQ3; xếp hạng theo hạn mức liên hệ cố
định cho AQ4.
