## Phụ lục I – Các AQ Modeling Brief

Nhóm tác giả lập AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa) cho từng AQ trước khi nêu tên bất kỳ phương pháp nào. Nhờ đó, phương pháp xuất phát từ câu hỏi, từ đầu ra mà câu hỏi cần và từ quyết định mà câu hỏi phục vụ [1]. Các bản mô tả dùng bộ dữ liệu đã chuẩn bị OULAD-N04-prepared-1.0. Trong bộ dữ liệu này, một lượt đăng ký học là một sinh viên trong một kỳ mở module; thời điểm chốt dữ liệu là cuối ngày 13 và cuối ngày 27 của kỳ mở; sinh viên được tính là không hoàn thành khi kết quả cuối cùng là Không đạt (Fail) hoặc Rút khỏi module (Withdrawn). Bảng A.1, A.2, A.3 và A.4 trình bày tám thuộc tính của bản mô tả cho từng câu hỏi.

**Bảng A.1. Modeling Brief của AQ1**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ1: tỷ lệ đạt, không đạt và rút khỏi module, phân theo module, kỳ mở, tháng bắt đầu và năm, cùng tuần của bài bị bỏ lỡ đầu tiên |
| Loại phân tích | Mô tả |
| Quyết định được hỗ trợ | D2 (phân bổ thời gian của cố vấn học tập) và D3 (có mở rộng sau thí điểm hay không): các trưởng chương trình đào tạo thấy module và kỳ mở nào mất nhiều sinh viên nhất và bài bị bỏ lỡ đầu tiên xuất hiện sớm đến mức nào |
| Đơn vị phân tích | Lượt đăng ký học, giới hạn ở các lượt còn hiệu lực vào ngày 14 (tổng thể dùng để tính KPI); bài đánh giá khi xét bài bị bỏ lỡ đầu tiên |
| Biến kết quả / biến mục tiêu | Không áp dụng (không có bài toán học có giám sát); các thước đo: tỷ lệ hoàn thành và không hoàn thành, tỷ trọng từng kết quả, tuần của bài đầu tiên đến hạn mà chưa nộp |
| Thông tin đầu vào | Bảng lượt đăng ký học (kết quả, module, kỳ mở, tháng bắt đầu, năm); bảng bài đến hạn (bài, ngày đến hạn, bài nộp); dùng toàn bộ kỳ mở, vì câu hỏi mô tả các kỳ mở đã kết thúc |
| Đầu ra dự kiến | Bảng tỷ lệ kèm khoảng tin cậy 95% theo module, kỳ mở, tháng bắt đầu và năm; phân phối tuần của bài bị bỏ lỡ đầu tiên theo kết quả |
| Ràng buộc chính | Mẫu số đúng (lượt đăng ký học còn hiệu lực vào ngày 14) và lịch bài đánh giá riêng của từng kỳ mở, vốn khác nhau giữa các module; năm module thiếu dữ liệu bài thi |

**Bảng A.2. Modeling Brief của AQ2**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ2: trong từng module, những dấu hiệu nào tính đến hết tuần 4 gắn với khả năng sinh viên về sau không hoàn thành |
| Loại phân tích | Chẩn đoán (mối liên hệ; không đưa ra nhận định nhân quả) |
| Quyết định được hỗ trợ | D2 và các lý do kèm theo mỗi tên trong danh sách D1: giảng viên hướng dẫn nên chú ý đến những dấu hiệu nào |
| Đơn vị phân tích | Lượt đăng ký học còn hiệu lực vào ngày 27 |
| Biến kết quả / biến mục tiêu | non_completion vào cuối kỳ mở, dùng làm biến kết quả của mô hình mối liên hệ, không phải biến cần dự đoán |
| Thông tin đầu vào | Các dấu hiệu tính đến hết ngày 27: bỏ lỡ một bài, nộp trễ một TMA, không có hoạt động trên nền tảng học tập trong bảy ngày gần nhất, mức hoạt động so với trung vị của kỳ mở, hoạt động trước ngày bắt đầu; hiệu chỉnh theo kỳ mở module, số lần học trước và số tín chỉ đang học |
| Đầu ra dự kiến | Chênh lệch nguy cơ tính bằng điểm phần trăm kèm khoảng tin cậy 95%, gồm ước lượng chưa hiệu chỉnh và ước lượng đã hiệu chỉnh theo kỳ mở module (so sánh sinh viên trong cùng kỳ mở); tỉ số odds (odds ratio) đặt bên cạnh; chiều của từng mối liên hệ trong mỗi module |
| Ràng buộc chính | Chỉ là mối liên hệ; bài đến hạn tính đến hết ngày 27 chỉ có ở 16 trên 22 kỳ mở; các dấu hiệu tương quan với nhau; ước lượng trên 9 kỳ mở huấn luyện năm 2013 (6 module) để kết quả của các kỳ mở kiểm thử năm 2014 vẫn được giữ kín |

**Bảng A.3. Modeling Brief của AQ3**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ3: so với quy tắc dấu hiệu sớm, mô hình ước lượng khả năng không hoàn thành tốt đến mức nào khi áp dụng cho một kỳ mở về sau, tại cuối tuần 2 (ngày 13) và cuối tuần 4 (ngày 27) |
| Loại phân tích | Dự báo |
| Quyết định được hỗ trợ | D1 (ai có tên trong danh sách liên hệ) |
| Đơn vị phân tích | Lượt đăng ký học còn hiệu lực tại thời điểm chốt dữ liệu |
| Biến kết quả / biến mục tiêu | non_completion (Fail hoặc Withdrawn) vào cuối kỳ mở, chỉ biết được sau khi kỳ mở kết thúc |
| Thông tin đầu vào | 19 biến dự báo chính của các bảng dữ liệu đã chuẩn bị, tất cả đều được ghi nhận tính đến hết thời điểm chốt; điểm trung bình bài đánh giá chấm bằng máy (CMA) không được dùng, vì dưới 10% số dòng huấn luyện có giá trị này; phương án thay thế là tập mở rộng gồm 10 biến dự báo, cộng thêm số lượt nhấp theo tuần |
| Đầu ra dự kiến | Một điểm rủi ro cho mỗi lượt đăng ký học tại mỗi thời điểm chốt, dùng làm thứ hạng trong kỳ mở; chỉ hiển thị dưới dạng xác suất khi kết quả hiệu chuẩn đạt yêu cầu |
| Ràng buộc chính | Rò rỉ thông tin và khả năng áp dụng cho một kỳ mở về sau; khả năng diễn giải đối với giảng viên hướng dẫn; hiệu chuẩn; huấn luyện trên các kỳ mở năm 2013, kiểm tra một lần trên các kỳ mở năm 2014 |

**Bảng A.4. Modeling Brief của AQ4**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ4: với hạn mức liên hệ giả định (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20), những lượt đăng ký học nào đứng đầu danh sách; danh sách đó đạt mức vượt tỷ lệ nền (lift) của kỳ mở và tỷ lệ phát hiện (recall) bao nhiêu, tính chung và theo mức khó khăn kinh tế – xã hội của khu vực cư trú và tình trạng khuyết tật |
| Loại phân tích | Chỉ định (xếp hạng), ở vai trò hỗ trợ quyết định; lựa chọn cách liên hệ được để lại sau |
| Quyết định được hỗ trợ | D1: giảng viên hướng dẫn nhận một danh sách có thứ tự và quyết định liên hệ với ai |
| Đơn vị phân tích | Lượt đăng ký học trong một kỳ mở module |
| Biến kết quả / biến mục tiêu | Dùng biến mục tiêu của AQ3 để đánh giá danh sách; dữ liệu không ghi nhận kết quả của việc liên hệ |
| Thông tin đầu vào | Điểm rủi ro của AQ3 và các lý do dẫn đến điểm rủi ro đó; độ dài k của danh sách trong mỗi kỳ mở, tính theo 3 hoặc 5 sinh viên được liên hệ trên mỗi nhóm hướng dẫn khoảng 20 sinh viên |
| Đầu ra dự kiến | Mỗi kỳ mở có một danh sách có thứ tự, dài đúng bằng hạn mức liên hệ cho phép; mỗi tên kèm các dấu hiệu giải thích vì sao sinh viên đó có tên |
| Ràng buộc chính | Hạn mức liên hệ cố định; sinh viên có nguy cơ cao chưa chắc là người được lợi nhiều nhất khi được liên hệ; quyết định do con người đưa ra; danh sách phải công bằng giữa các mức khó khăn của khu vực và giữa sinh viên có và không có khuyết tật; báo cáo không khẳng định rằng việc liên hệ có hiệu quả |
