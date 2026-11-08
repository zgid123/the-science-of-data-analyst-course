# 10. Sử dụng AI tạo sinh và phản tư của nhóm

Trí tuệ nhân tạo (AI) tạo sinh hỗ trợ milestone này trong năm vai trò mà đề bài cho phép. Đúng như đề bài yêu cầu, mọi
phát hiện về dữ liệu đều được xác nhận bằng mã, số liệu thống kê, tài liệu hoặc kiểm tra trực tiếp trên bộ dữ liệu [1];
AI không bao giờ được xem là nguồn dữ liệu [1]. Trong mỗi lượt rà soát, cả bên soạn thảo lẫn bên phản biện đều là tác tử AI (agent), còn thành viên
nhóm kiểm chứng các quyết định; Phụ lục V trình bày Nhật ký quyết định về AI (AI Decision Log), các prompt và mọi quyết định.

Trong vai trò AI diễn giải từ điển dữ liệu (Data dictionary interpreter), các tác tử nghiên cứu đọc bài mô tả dữ liệu, chính sách đánh giá của OU và
tài liệu về IMD; mỗi thông tin chỉ được giữ lại khi có đoạn trích nguyên văn. Quy định năm 2025 rằng CMA không được nộp
trễ đã được đối chiếu với dữ liệu; vì dữ liệu 2013–2014 có nhiều CMA nộp trễ, nhóm tác giả không áp dụng quy định này. Trong vai trò trợ lý viết mã (Code assistant), AI soạn thảo mọi script của gói
dữ liệu. Các script này được kiểm chứng bằng bốn cách: 13 con số trùng khớp với một lần đếm lại độc lập; chín kiểm thử đơn vị;
sáu đặc trưng được tính lại cho từng dòng mà không lệch dòng nào; một dòng được đếm lại thủ công. Trong vai trò AI
phản biện quy trình chuẩn bị (Preparation critic), một tác tử chạy trong phiên riêng nêu 12 nhận xét; nhóm chấp nhận 9 nhận xét và chấp nhận một phần 3 nhận xét.
Trong vai trò AI kiểm tra rò rỉ thông tin (leakage auditor), tác tử thứ hai nêu 8 phát hiện, đều được chấp nhận; tác tử này không tìm thấy trường
hợp nào dùng dữ liệu sau thời điểm chốt. Trong vai trò trợ lý viết tài liệu (Documentation assistant) và trợ lý tạo dữ liệu giả lập (Synthetic-data assistant), AI soạn thảo từ
điển dữ liệu, bảng truy vết nguồn gốc dữ liệu (lineage), hướng dẫn sử dụng gói và một số bản ghi giả lập nhỏ dùng để kiểm thử; các bản ghi này
không bao giờ đi vào bảng dữ liệu đã chuẩn bị nào.

Các lượt rà soát định hình những quy tắc mà quy trình chuẩn bị dữ liệu (pipeline) áp dụng. Danh sách của AQ4 được đánh giá theo mức vượt so với một danh sách chọn
ngẫu nhiên (C13). Tình trạng nộp trễ CMA (gặp ở 47,2% số bài nộp CMA) không được đưa vào quy tắc dấu hiệu sớm (C10). Một
bài chỉ bị tính là bỏ lỡ khi có ngày đến hạn trùng hoặc sau ngày đăng ký. Ngoài ra, bước kiểm tra rò rỉ thông tin thực sự có khả năng phát hiện lỗi: nếu một đặc trưng dùng dữ liệu sau thời điểm chốt, phép kiểm tra sẽ báo không đạt.
Một đề nghị chỉ được chấp nhận một phần: nhóm đếm các lượt đăng ký học trong tập kiểm thử của sinh viên đã có mặt năm 2013, nhưng không báo cáo tỷ lệ kết quả của nhóm này trước khi lập mô hình, vì báo cáo như vậy sẽ
làm lộ kết quả của tập kiểm thử ngay trong giai đoạn chuẩn bị, điều mà đề bài không cho phép [1].
