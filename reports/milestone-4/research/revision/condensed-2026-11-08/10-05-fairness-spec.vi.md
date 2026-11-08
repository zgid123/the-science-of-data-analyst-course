## Phụ lục V – Đặc tả phân tích lỗi và công bằng

Chỉ số gộp có thể che khuất khác biệt giữa các nhóm. Vì vậy, mô hình đã chốt được đánh giá riêng cho từng nhóm cần kiểm tra công bằng trong các kỳ mở kiểm thử; cách làm này gọi là phân tích theo từng nhóm con (slicing analysis) [34]. Giới tính, tình trạng khuyết tật do sinh viên tự khai, mức khó khăn kinh tế – xã hội của khu vực cư trú và nhóm tuổi không được dùng làm biến dự báo mà chỉ phục vụ việc kiểm tra công bằng. Bỏ các thuộc tính này ra khỏi mô hình không làm mô hình "mù" với chúng, vì hoạt động học tập, số lần học trước hoặc số tín chỉ có thể mang cùng thông tin [36]. Bảng A.15 trình bày quy mô của từng nhóm trong các bảng dữ liệu đã chuẩn bị và cách xử lý nhóm đó. Số liệu về kết quả lấy từ các kỳ mở huấn luyện năm 2013; quy mô tập kiểm thử chỉ tính số lượt đăng ký học. Điều kiện để một nhóm được đưa vào kiểm định khẳng định (phép kiểm định chính, ấn định trước) được chốt trong bản đề xuất này dựa trên số lượt đăng ký học, trước khi mở bất kỳ kết quả kiểm thử nào.

**Bảng A.15. Các nhóm cần kiểm tra công bằng tại ngày 27**

| Nhóm | Lượt đăng ký học huấn luyện / sinh viên không hoàn thành | Lượt đăng ký học kiểm thử | Kỳ mở kiểm thử nhỏ nhất | Cách xử lý |
| :---- | :---- | :---- | :---- | :---- |
| Nữ / nam | Nữ: 5.697 / 2.488; nam: 6.114 / 2.757 | Nữ: 6.666; nam: 9.058 | Nữ: 66; nam: 139 | Mô tả, theo từng kỳ mở và gộp |
| Có tình trạng khuyết tật do sinh viên tự khai | 1.123 / 602 | 1.488 | 18 | Kiểm định khẳng định, gộp qua các kỳ mở |
| Mức khó khăn của khu vực 0–10% (10% khu vực khó khăn nhất) | 1.163 / 699 | 1.486 | 17 | Kiểm định khẳng định, gộp qua các kỳ mở |
| Thiếu mức khó khăn của khu vực | 418 / 118 | 610 | 1 | Kiểm định khẳng định, gộp qua các kỳ mở; xét như một nhóm riêng, không bao giờ gộp vào một mức khác |
| Từ 55 tuổi trở lên | 75 / 18 | 118 | 1 | Dưới quy mô đủ điều kiện: chỉ báo cáo ước lượng điểm của chênh lệch, ghi "không đủ dữ liệu, chưa được xác nhận đạt" |

Các tiêu chí công bằng không thể cùng thỏa mãn khi tỷ lệ không hoàn thành khác nhau giữa các nhóm. Một điểm rủi ro có giá trị dự báo dương ngang nhau giữa các nhóm thì không thể đồng thời có tỷ lệ lỗi ngang nhau [35]; ngoài ra, hiệu chuẩn trong từng nhóm và tỷ lệ lỗi cân bằng mâu thuẫn với nhau, trừ các trường hợp suy biến [53]. Do đó, phép kiểm tra công bằng chọn một tiêu chí chính là tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation): ở mọi nhóm, danh sách phải phát hiện được một tỷ lệ sinh viên không hoàn thành ngang nhau. Tiêu chí này phù hợp với hoạt động liên hệ hỗ trợ, vì với hoạt động này, tác hại chính là bỏ sót một sinh viên đang gặp khó khăn [36]. Bảng A.16 liệt kê các phép kiểm tra; chỉ dòng đầu tiên là kiểm định khẳng định, mọi dòng còn lại mang tính mô tả.

**Bảng A.16. Các phép kiểm tra công bằng và lỗi**

| Phép kiểm tra | Thước đo | Quy tắc |
| :---- | :---- | :---- |
| Kiểm định khẳng định về công bằng (separation) | Tỷ lệ phát hiện trong giới hạn danh sách của từng nhóm đủ điều kiện (ít nhất 400 lượt đăng ký học kiểm thử), trừ đi tỷ lệ này ở các sinh viên còn lại; tính tại ngày 27 với k = 5 trên 20; so sánh trong từng kỳ mở rồi gộp qua các kỳ mở | Một nhóm bị đánh dấu để xem xét khi thỏa cả hai điều kiện: tỷ lệ phát hiện của nhóm thấp hơn của các sinh viên còn lại quá 10 điểm phần trăm; khoảng bootstrap 95% một phía của chênh lệch nằm hoàn toàn dưới 0, sau khi hiệu chỉnh Holm cho ba nhóm của kiểm định khẳng định. Nhóm có dưới 400 lượt đăng ký học kiểm thử chỉ được xem xét theo ước lượng điểm của chênh lệch và được báo cáo là chưa được xác nhận đạt |
| Tỷ lệ được chọn | Tỷ lệ của từng nhóm trong danh sách so với tỷ lệ của nhóm đó trong số sinh viên không hoàn thành | Mô tả |
| Độ chính xác theo nhóm | Độ chính xác của danh sách dài k, tính riêng cho từng nhóm | Mô tả; khi tỷ lệ nền khác nhau, độ chính xác khác nhau giữa các nhóm là điều đã biết trước [35] |
| Hiệu chuẩn theo nhóm | Hiệu chuẩn tổng thể và độ dốc hiệu chuẩn; chỉ vẽ đường cong khi có khoảng 200 sự kiện và 200 trường hợp không có sự kiện [31] | Mô tả, kèm khoảng tin cậy |
| Chênh lệch không phụ thuộc ngưỡng | ABROCA tính trong từng kỳ mở rồi gộp lại; kèm dấu của chênh lệch về khả năng phân biệt (cho biết nhóm nào được phân biệt tốt hơn); kèm giá trị tham chiếu, tức ABROCA khi nhãn nhóm được hoán vị ngẫu nhiên trong từng kỳ mở [34] | Mô tả; riêng chỉ số này không bao giờ dẫn đến việc xem xét |
| Kiểm tra biến thay thế (proxy) | Phân phối điểm rủi ro và trung bình các biến dự báo theo nhóm | Mô tả; cho thấy biến dự báo nào mang thông tin về nhóm |
| Lỗi theo kỳ mở và module | Sinh viên không hoàn thành bị bỏ sót và sinh viên hoàn thành có trong danh sách theo từng kỳ mở; module CCC được báo cáo riêng | Xem xét các kỳ mở có kết quả kém hơn quy tắc |
| Lỗi theo hoạt động và lịch sử học tập | Không hoạt động, hoạt động thấp và bình thường; số lần học trước; đăng ký muộn | Cho thấy mô hình có giá trị gì ngoài việc nhận ra sinh viên không hoạt động |
| Lỗi theo loại kết quả và khả năng liên hệ | Fail và Withdrawn trong số sinh viên không hoàn thành bị bỏ sót và có trong danh sách; việc rút khỏi module trong vòng 7 ngày sau thời điểm chốt dữ liệu | Cho thấy danh sách bỏ sót loại không hoàn thành nào và không liên hệ kịp với ai |
| Độ ổn định của danh sách | Tỷ lệ mẫu bootstrap trong đó một sinh viên gần hạng k vẫn ở trong danh sách | Cho thấy việc một sinh viên gần hạng k có tên trong danh sách hay không phụ thuộc vào ngẫu nhiên đến mức nào |

Một nghiên cứu trước đây trên OULAD ghi nhận hai hiện tượng. Thứ nhất, có một chênh lệch có lợi cho sinh viên nam; phần lớn mô hình dự báo sinh viên có nguy cơ đều tái tạo và khuếch đại nhẹ chênh lệch này. Thứ hai, sai lệch đối với nhóm sinh viên khai báo khuyết tật, vốn chiếm tỷ lệ nhỏ trong dữ liệu, biến động thất thường. Vì vậy, các nhóm nhỏ được gộp qua các kỳ mở và được báo cáo kèm khoảng tin cậy [37].
