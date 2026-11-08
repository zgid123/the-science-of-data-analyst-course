## Phụ lục IV – Đặc tả phân tích lỗi và công bằng

Chỉ số gộp có thể che khuất khác biệt giữa các nhóm. Vì vậy, mô hình đã chốt được đánh giá riêng cho từng nhóm cần kiểm tra công bằng trong các kỳ mở của tập kiểm thử; cách làm này gọi là phân tích theo từng nhóm con [34]. Giới tính, tình trạng khuyết tật do sinh viên tự khai, mức khó khăn kinh tế – xã hội của khu vực cư trú và nhóm tuổi không được dùng làm biến dự báo mà chỉ phục vụ việc kiểm tra công bằng. Bỏ các thuộc tính này ra khỏi mô hình không làm mô hình "mù" với các thuộc tính đó, vì hoạt động học tập, số lần học trước hoặc số tín chỉ có thể mang cùng thông tin [35]. Bảng A.7 trình bày quy mô của từng nhóm trong các bảng dữ liệu đã chuẩn bị và cách xử lý nhóm đó. Số liệu về kết quả lấy từ các kỳ mở huấn luyện năm 2013; quy mô tập kiểm thử chỉ tính số lượt đăng ký học. Điều kiện để một nhóm được đưa vào kiểm định khẳng định được chốt trong bản đề xuất này dựa trên số lượt đăng ký học, trước khi mở bất kỳ kết quả nào của tập kiểm thử.

**Bảng A.7. Các nhóm cần kiểm tra công bằng tại ngày 27**

| Nhóm | Lượt đăng ký học huấn luyện / sinh viên không hoàn thành | Lượt đăng ký học trong tập kiểm thử | Số lượt đăng ký học ít nhất của nhóm trong một kỳ mở của tập kiểm thử | Cách xử lý |
| :---- | :---- | :---- | :---- | :---- |
| Nữ / nam | Nữ: 5.697 / 2.488; nam: 6.114 / 2.757 | Nữ: 6.666; nam: 9.058 | Nữ: 66; nam: 139 | Mô tả, theo từng kỳ mở và gộp |
| Có tình trạng khuyết tật do sinh viên tự khai | 1.123 / 602 | 1.488 | 18 | Kiểm định khẳng định, gộp qua các kỳ mở |
| Mức khó khăn của khu vực 0–10% (10% khu vực khó khăn nhất) | 1.163 / 699 | 1.486 | 17 | Kiểm định khẳng định, gộp qua các kỳ mở |
| Thiếu mức khó khăn của khu vực | 418 / 118 | 610 | 1 | Kiểm định khẳng định, gộp qua các kỳ mở; xét như một nhóm riêng, không bao giờ gộp vào một mức khác |
| Từ 55 tuổi trở lên | 75 / 18 | 118 | 1 | Dưới quy mô tối thiểu để đủ điều kiện: chỉ báo cáo ước lượng điểm của chênh lệch, ghi "không đủ dữ liệu, chưa được xác nhận đạt" |

Các tiêu chí công bằng không thể cùng thỏa mãn khi tỷ lệ không hoàn thành khác nhau giữa các nhóm. Một điểm rủi ro có giá trị dự báo dương ngang nhau giữa các nhóm thì không thể đồng thời có tỷ lệ lỗi ngang nhau [36]; ngoài ra, hiệu chuẩn trong từng nhóm và tỷ lệ lỗi cân bằng mâu thuẫn với nhau, trừ các trường hợp suy biến [37]. Do đó, phép kiểm tra công bằng chọn một tiêu chí chính: tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm, đo bằng tỷ lệ phát hiện trong giới hạn danh sách ngang nhau giữa các nhóm. Tiêu chí này phù hợp với hoạt động liên hệ hỗ trợ, vì với hoạt động này, tác hại chính là bỏ sót một sinh viên đang gặp khó khăn [35]. Bảng A.8 liệt kê các phép kiểm tra; chỉ dòng đầu tiên là kiểm định khẳng định, mọi dòng còn lại mang tính mô tả.

**Bảng A.8. Các phép kiểm tra công bằng và lỗi**

| Phép kiểm tra | Thước đo | Quy tắc |
| :---- | :---- | :---- |
| Kiểm định khẳng định về công bằng (ngang bằng tỷ lệ phát hiện) | Tỷ lệ phát hiện trong giới hạn danh sách của từng nhóm đủ điều kiện (ít nhất 400 lượt đăng ký học trong tập kiểm thử), trừ đi tỷ lệ này ở các sinh viên còn lại; tính tại ngày 27 với k = 5 trên 20; so sánh trong từng kỳ mở rồi gộp qua các kỳ mở | Một nhóm bị đánh dấu để xem xét khi thỏa cả hai điều kiện: tỷ lệ phát hiện của nhóm thấp hơn của các sinh viên còn lại quá 10 điểm phần trăm; khoảng bootstrap 95% một phía của chênh lệch nằm hoàn toàn dưới 0, sau khi hiệu chỉnh Holm cho ba nhóm của kiểm định khẳng định. Nhóm có dưới 400 lượt đăng ký học trong tập kiểm thử chỉ được xem xét theo ước lượng điểm của chênh lệch và được báo cáo là chưa được xác nhận đạt |
| Tỷ lệ được chọn | Phần trăm danh sách mà mỗi nhóm chiếm, so với phần trăm nhóm đó chiếm trong số sinh viên không hoàn thành | Mô tả |
| Độ chính xác theo nhóm | Độ chính xác của danh sách dài k, tính riêng cho từng nhóm | Mô tả; khi tỷ lệ nền khác nhau, chênh lệch độ chính xác giữa các nhóm là điều có thể dự kiến [36] |
| Hiệu chuẩn theo nhóm | Hiệu chuẩn tổng thể và độ dốc hiệu chuẩn; chỉ vẽ đường cong khi có khoảng 200 sự kiện và 200 trường hợp không có sự kiện [33] | Mô tả, kèm khoảng tin cậy |
| Chênh lệch không phụ thuộc ngưỡng | ABROCA tính trong từng kỳ mở rồi gộp lại; kèm dấu của chênh lệch về khả năng phân biệt; kèm giá trị tham chiếu: ABROCA tính lại sau khi hoán vị ngẫu nhiên nhãn nhóm trong từng kỳ mở, tức mức ABROCA có thể có chỉ do ngẫu nhiên [34] | Mô tả; chỉ số này không tự mình kích hoạt việc xem xét lại một nhóm |
| Kiểm tra biến đại diện (proxy check) | Phân phối điểm rủi ro và trung bình các biến dự báo theo nhóm | Mô tả; cho thấy biến dự báo nào mang thông tin về nhóm |
| Lỗi theo kỳ mở và module | Sinh viên không hoàn thành bị bỏ sót và sinh viên hoàn thành có trong danh sách theo từng kỳ mở; module CCC được báo cáo riêng | Xem xét các kỳ mở có kết quả kém hơn quy tắc |
| Lỗi theo hoạt động và lịch sử học tập | Không hoạt động, hoạt động thấp và bình thường; số lần học trước; đăng ký muộn | Cho thấy mô hình có tạo thêm giá trị ngoài việc nhận ra sinh viên không hoạt động hay không |
| Lỗi theo loại kết quả và khả năng liên hệ | Fail và Withdrawn trong số sinh viên không hoàn thành bị bỏ sót và có trong danh sách; việc rút khỏi module trong vòng 7 ngày sau thời điểm chốt dữ liệu | Cho thấy danh sách bỏ sót loại không hoàn thành nào và những sinh viên nào không còn liên hệ được |
| Độ ổn định của danh sách | Tỷ lệ mẫu bootstrap trong đó một sinh viên gần hạng k vẫn ở trong danh sách | Cho thấy điểm cắt tại hạng k phụ thuộc vào biến động ngẫu nhiên đến mức nào |

Một nghiên cứu trước đây trên OULAD ghi nhận hai hiện tượng. Thứ nhất, có một chênh lệch có lợi cho sinh viên nam; phần lớn mô hình dự báo sinh viên có nguy cơ đều tái tạo và khuếch đại nhẹ chênh lệch này. Thứ hai, mức thiên lệch đối với nhóm có tình trạng khuyết tật do sinh viên tự khai, vốn chiếm tỷ lệ nhỏ trong dữ liệu, biến động thất thường. Vì vậy, các nhóm nhỏ được gộp qua các kỳ mở và được báo cáo kèm khoảng tin cậy [38].
