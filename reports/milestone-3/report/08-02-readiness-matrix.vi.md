## 8.2. Ma trận mức sẵn sàng cho mô hình

Bảng 8.1 là Ma trận mức sẵn sàng cho mô hình (Model Readiness Matrix) theo đề bài. Với từng AQ, bảng nêu bảng dữ liệu đã
chuẩn bị, biến mục tiêu hoặc thước đo, bộ đặc trưng hoặc các chiều phân tích, quy tắc chia dữ liệu hoặc quy tắc thời gian
và mức sẵn sàng cho Milestone 4 [1]. Một AQ được xếp Sẵn sàng khi bảng dữ liệu, biến mục tiêu và các quy tắc đã được cố
định và kiểm tra; AQ được xếp Cần điều chỉnh khi một phần của câu hỏi vẫn còn thiếu dữ liệu.

**Bảng 8.1. Ma trận mức sẵn sàng cho mô hình**

| AQ | Loại phân tích | Bảng dữ liệu đã chuẩn bị | Biến mục tiêu / thước đo | Bộ đặc trưng / chiều phân tích | Quy tắc chia dữ liệu / thời gian | Mức sẵn sàng |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Mô tả | enrolment, assessment_due | Tỷ lệ hoàn thành; tuần đầu tiên bỏ lỡ bài được chấm điểm | Module, kỳ mở, tháng bắt đầu, năm | Cả 22 kỳ mở; nhóm tính KPI gồm các lượt đăng ký học còn hiệu lực tại ngày 14 | Sẵn sàng |
| AQ2 | Chẩn đoán | features_d27, enrolment | non_completion | Bài bỏ lỡ, TMA và CMA nộp trễ, không hoạt động trong bảy ngày gần nhất, tỷ lệ hoạt động so với trung vị của kỳ mở; số kỳ mở mà sinh viên học đồng thời, chỉ xét cho năm 2014 | Dấu hiệu tính đến hết ngày 27; dấu hiệu về bài được chấm điểm chỉ có ở 16 kỳ mở có bài đến hạn | Sẵn sàng, chỉ cho phân tích mối liên hệ |
| AQ3 | Dự báo | features_d13, features_d27, model_ready | non_completion tại cuối kỳ mở | 20 đặc trưng chính, 10 đặc trưng mở rộng và số lượt nhấp theo tuần; quy tắc dấu hiệu sớm làm mốc so sánh | Huấn luyện trên năm 2013, đánh giá trên tập kiểm thử (các kỳ mở năm 2014); tinh chỉnh siêu tham số bằng các fold (phần chia trong kiểm định chéo) loại trừ từng kỳ mở (leave-one-run-out) trong năm 2013 | Sẵn sàng; danh sách tại ngày 13 chỉ dựa trên hoạt động, vì tính đến hết ngày 13 chỉ 1 trong 22 kỳ mở có bài đến hạn |
| AQ4 | Chỉ định (xếp hạng) | capacity_by_run kèm điểm rủi ro từ AQ3 | Lift so với tỷ lệ không hoàn thành của kỳ mở; tỷ lệ phát hiện (recall) so với mức tối đa mà danh sách cùng độ dài có thể đạt | Danh sách gồm 3 hoặc 5 sinh viên cho mỗi nhóm hướng dẫn 20 sinh viên hoặc gồm 30 hoặc 40 sinh viên cho mỗi kỳ mở; kiểm tra công bằng theo mức khó khăn của khu vực và tình trạng khuyết tật | Theo từng kỳ mở và thời điểm chốt dữ liệu, chỉ trên các kỳ mở của tập kiểm thử | Cần điều chỉnh: phần xếp hạng đã sẵn sàng; lựa chọn cách liên hệ được hoãn |

**Lý do cần xếp hạng.** Quy tắc dấu hiệu sớm đánh dấu 20,2% số sinh viên đang đăng ký học vào ngày 13 và 28,8% vào ngày
27, trong khi danh sách 3 hoặc 5 sinh viên trên mỗi nhóm 20 sinh viên chỉ chứa được 15% hoặc 25% số sinh viên của nhóm. Với
danh sách 5 sinh viên trên mỗi nhóm 20, quy tắc đánh dấu nhiều sinh viên hơn độ dài danh sách ở 7 trong 22 kỳ mở tại ngày 13 và ở 10 kỳ mở tại
ngày 27; với danh sách 3 sinh viên trên mỗi nhóm 20, con số này là 15 kỳ mở tại ngày 13 và cả 22 kỳ mở tại ngày 27. Vì vậy, cán bộ cần
một thứ tự ưu tiên để biết nên liên hệ ai trước. AQ3 và AQ4 cung cấp thứ tự đó, còn riêng quy tắc dấu hiệu sớm thì không xếp được thứ tự này.

**Những câu hỏi chưa khả thi.** Ba phần của đề xuất không trả lời được bằng OULAD và cần hồ sơ riêng của đợt thí điểm.
Phần thứ nhất là cách liên hệ nào hiệu quả nhất với sinh viên nào (tin nhắn của giảng viên, cuộc gọi từ Phòng Đào tạo hoặc giới thiệu sinh viên đến một đơn vị hỗ trợ khác), cùng tác động của cách liên hệ đó đến việc hoàn thành học phần
(AQ4, C08, C11). Phần thứ hai là các phép so sánh theo năm theo học, theo hình thức học và theo việc điểm danh (C04, C05). Phần thứ
ba là tỷ lệ liên hệ kịp thời (KPI phụ 2) cùng phần liên hệ của KPI phụ 1, tức số sinh viên có dấu hiệu sớm đã được liên hệ (C08).

**Điều kiện để bước vào Milestone 4.** Đề bài đặt ra sáu điều kiện để bắt đầu lập mô hình [1]: các câu hỏi cốt lõi có
bảng dữ liệu đã chuẩn bị và truy vết rõ ràng; biến mục tiêu, đặc trưng và các chiều phân tích đã ổn định; rò rỉ thông tin
và cách chia dữ liệu đã được xác định cho các bài toán dự báo; các vấn đề chất lượng quan trọng đã được xử lý hoặc được
giữ lại có chủ đích; không dùng dữ liệu giả lập làm bằng chứng; dữ liệu đã chuẩn bị tạo lại được từ các tệp gốc. Cả sáu
điều kiện đều được đáp ứng với AQ1 đến AQ3, nên Milestone 4 có thể bắt đầu với ba AQ này. AQ4 bước vào Milestone 4 dưới
dạng câu hỏi xếp hạng, còn phần liên hệ chờ đợt thí điểm. Phụ lục VI (Bảng A.19) nêu tình trạng của từng điều kiện.
