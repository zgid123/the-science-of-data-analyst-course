# 13. Sử dụng AI tạo sinh và bài học rút ra

Xuyên suốt dự án, nhóm chúng em sử dụng AI tạo sinh trong vai bên liên quan mô phỏng, trợ lý tìm tài liệu, trợ lý viết mã, người phản biện
và người cùng viết. Ở mọi vai trò, chúng em áp dụng một nguyên tắc: AI không phải là nguồn của dữ liệu, số liệu thống
kê, thông tin giấy phép hay kết quả; mọi thông tin do AI đưa ra đều được đối chiếu với một nguồn đã lưu, với các tệp dữ
liệu hoặc với mã mà chúng em đã chạy.

## 13.1. Nhật ký quyết định về AI, Milestone 1–5

Bảng A.43 (Phụ lục XVI) trình bày Nhật ký quyết định về AI (AI Decision Log) theo các cột của đề bài, với một hàng cho mỗi
milestone trước và bốn hàng cho bước tích hợp cuối cùng. Với Milestone 1 đến Milestone 4, nhật ký ghi lại cách AI đóng
vai các bên liên quan mô phỏng, trợ lý tìm tài liệu, người phản biện và trợ lý viết mã, cách nhóm chúng em kiểm tra từng
đầu ra cùng những ý kiến phản biện được chấp nhận hoặc bác bỏ. Ở Milestone 5, các tác tử AI đảm nhận ba việc. Thứ nhất,
AI trích xuất 369 nhận định từ các nguồn tài liệu đã lưu; mỗi nhận định được tự động đối chiếu với một trích dẫn
nguyên văn trong chính nguồn đó. Thứ hai, AI viết
mã cho AQ1 và AQ2; chúng em chỉ chấp nhận kết quả sau khi các phép kiểm tra tính nhất quán tự động cho kết quả PASS, một
lần chạy lại cho kết quả giống hệt đến từng byte và một lần tính lại độc lập. Thứ ba, AI rà soát toàn bộ bản thảo và nêu
66 ý kiến phản biện; chúng em đối chiếu từng ý kiến với dữ liệu: 42 ý kiến được chấp nhận, 14 ý kiến được chấp nhận một
phần, 10 ý kiến được xử lý trong các bước hoàn thiện báo cáo sau đó và không ý kiến nào bị bác bỏ. Không tác tử AI nào tạo ra giá trị
chỉ số, ngưỡng hoặc kết quả.

## 13.2. Bài học về AI trong vai người cùng lập luận và cùng viết

Vai trò của AI thay đổi qua các milestone, nhưng nguyên tắc vẫn giữ nguyên: đầu ra của AI là một đề xuất để nhóm chúng em
kiểm chứng, không phải là một phát hiện. Nguyên tắc này phù hợp với hướng dẫn của Tổ chức Giáo dục, Khoa học và Văn hóa Liên Hợp Quốc (UNESCO) về AI tạo sinh trong giáo dục và nghiên cứu. Theo hướng dẫn này, không thể tin rằng AI tạo
sinh luôn chính xác [20]; người học và nhà nghiên cứu không nên chấp nhận thông tin của AI mà không kiểm tra
[20]. Cách kiểm chứng được chọn theo loại sai sót có thể xảy ra: các câu trích từ phỏng vấn được đối chiếu với bản ghi
hội thoại; tài liệu được đối chiếu với bản sao đã lưu kèm trích dẫn nguyên văn; mã được đối chiếu với dữ liệu kiểm thử
cố định (fixture) và các lần đếm lại độc lập; AI đóng vai trò phản biện chỉ được dựa vào đề bài và dữ liệu. Các lần rà soát hữu ích
nhất là khi AI đóng vai trò phản biện phải lập luận từ dữ liệu. Ví dụ, ở Milestone 3, AI kiểm tra rò rỉ thông tin đã phát hiện các
bài đến hạn trước ngày đăng ký bị tính là bỏ lỡ, cùng một phép kiểm tra rò rỉ thông tin không thể báo lỗi (luôn cho kết quả PASS). Các
quyết định vẫn thuộc về chúng em: giữ kín các kỳ mở năm 2014, giữ một quy tắc dấu hiệu sớm duy nhất, trình bày AQ3 và
AQ4 dưới dạng thiết kế và nêu mọi mối liên hệ đúng là mối liên hệ. Như vậy, AI hỗ trợ quá trình lập luận của chúng em
bằng cách phản biện và đẩy nhanh các công việc thường lệ, còn bằng chứng đến từ dữ liệu, các nguồn tài liệu và mã mà
chúng em đã chạy.
