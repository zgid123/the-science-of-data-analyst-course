## 4.1. Evaluation Design Card

Mỗi AQ có một Evaluation Design Card (thẻ thiết kế đánh giá) gồm bảy nội dung theo đề bài: chỉ số
chính, chỉ số phụ, chiến lược kiểm định, phương pháp cơ sở (baseline), phân tích lỗi, kiểm tra công bằng hoặc kiểm tra
theo nhóm con và tiêu chí thành công [1]. Chỉ số được chọn theo quyết định mà chỉ số đó phục vụ: tỷ lệ phát hiện
(recall) quan trọng khi một lần liên hệ tốn ít chi phí, còn độ chính xác của danh sách (precision) quan trọng khi liên
hệ tốn kém [23]. Bên cạnh đó, khi người dùng chỉ xem xét được một số ít trường hợp đứng đầu bảng xếp hạng, hiệu năng
trong nhóm đầu bảng này là thước đo có ý nghĩa thực tế [24]. Bảng 4.1 tóm tắt năm nội dung của bốn thẻ; bản đầy đủ,
gồm cả chỉ số phụ và phân tích lỗi, nằm ở Phụ lục III (Bảng A.8–A.11).

**Bảng 4.1. Evaluation Design Card (bản tóm tắt)**

| Nội dung | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- |
| Chỉ số chính | Các tỷ lệ kèm khoảng tin cậy 95% | Chênh lệch nguy cơ trong từng kỳ mở, kèm khoảng tin cậy | Tỷ lệ phát hiện chuẩn hóa (normalised recall, tức tỷ lệ phát hiện chia cho mức tối đa mà danh sách cùng độ dài có thể đạt) của danh sách dài k theo hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20); tại ngày 27, k = 5 trên 20 | Tỷ lệ phát hiện chuẩn hóa của danh sách dài k |
| Kiểm định | Tổng hợp theo hai cách độc lập (từ bảng đã chuẩn bị và từ bảng gốc); đối chiếu với các tổng số đã biết (32.593 và 28.061 lượt đăng ký học) | Các kỳ mở năm 2013; lặp lại trên năm 2014 sau lần kiểm thử của AQ3 | Loại trừ từng kỳ mở (leave-one-run-out: mỗi lần để riêng một kỳ mở năm 2013 làm dữ liệu kiểm định); kiểm thử một lần duy nhất trên năm 2014 | Như AQ3 |
| Phương pháp cơ sở | Tỷ lệ gộp; tỷ lệ theo mẫu số thứ hai, tức toàn bộ 32.593 lượt đăng ký học thay vì 28.061 lượt còn hiệu lực tại ngày 14 | Chênh lệch tỷ lệ chưa hiệu chỉnh theo từng dấu hiệu | Danh sách xếp theo quy tắc dấu hiệu sớm; mô hình chỉ dùng đặc điểm cá nhân; danh sách ngẫu nhiên | Danh sách ngẫu nhiên và danh sách xếp theo quy tắc dấu hiệu sớm |
| Công bằng / nhóm con | Tỷ lệ theo nhóm, chỉ mô tả | Mối liên hệ theo nhóm, chỉ mô tả | Kiểm định khẳng định về tỷ lệ phát hiện theo nhóm, với các nhóm và quy tắc ấn định trước (Mục 4.4) | Như AQ3, theo mức khó khăn của khu vực và tình trạng khuyết tật |
| Tiêu chí thành công | Hai cách tổng hợp cho cùng kết quả; mọi tỷ lệ đều kèm khoảng tin cậy | Chênh lệch ít nhất 5 điểm phần trăm; khoảng tin cậy không chứa 0; chênh lệch cùng chiều ở ít nhất hai phần ba số module | Một điều kiện đạt duy nhất (S1): tỷ lệ phát hiện chuẩn hóa gộp của mô hình cao hơn của danh sách xếp theo quy tắc dấu hiệu sớm; khoảng tin cậy của chênh lệch nằm hoàn toàn trên 0 (Mục 4.3) | Danh sách đáp ứng điều kiện S1; kiểm định khẳng định về công bằng đạt; nếu không đạt, nhóm liên quan được xem xét lại (Mục 4.4) |
