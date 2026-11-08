FILE = "02-01-modeling-briefs.vi.md"
PAIRS = [
("""thông tin được phép dùng làm đầu vào cùng khoảng thời gian của thông tin đó, đầu ra mong đợi""",
 """thông tin được phép dùng làm đầu vào và khoảng thời gian được lấy thông tin đó, đầu ra mong đợi"""),
("""| Lượt đăng ký học, giới hạn ở các lượt còn hiệu lực tại ngày 14 (nhóm tính KPI); bài được chấm điểm, khi xét bài bị bỏ lỡ đầu tiên |""",
 """| Lượt đăng ký học, chỉ gồm các lượt còn hiệu lực tại ngày 14 (đây là nhóm tính KPI). Riêng khi xét bài bị bỏ lỡ đầu tiên, đơn vị phân tích là từng bài được chấm điểm |"""),
("""| Mẫu số đúng (lượt đăng ký học còn hiệu lực tại ngày 14) và lịch bài được chấm điểm của từng kỳ mở, vốn khác nhau giữa các module; 5 module""",
 """| Phải dùng đúng mẫu số (lượt đăng ký học còn hiệu lực tại ngày 14) và đúng lịch bài được chấm điểm của từng kỳ mở, vì lịch này khác nhau giữa các module. Ngoài ra, 5 module"""),
("""| Chênh lệch nguy cơ tính bằng điểm phần trăm kèm khoảng tin cậy 95%, cả dạng chưa hiệu chỉnh và dạng so sánh trong từng kỳ mở module, bên cạnh tỉ số odds (odds ratio); chiều của từng mối liên hệ trong từng module |""",
 """| Chênh lệch nguy cơ tính bằng điểm phần trăm kèm khoảng tin cậy 95%, ở cả dạng chưa hiệu chỉnh và dạng so sánh trong từng kỳ mở module; tỉ số odds (odds ratio) được báo cáo bên cạnh. Ngoài ra, chiều của từng mối liên hệ được nêu cho từng module |"""),
("""| 19 biến dự báo chính dùng được trong các bảng đặc trưng (điểm trung bình của bài đánh giá chấm bằng máy (CMA) bị loại vì dưới 10% số dòng huấn luyện có giá trị này), tất cả đều ghi nhận tính đến hết thời điểm chốt dữ liệu; phương án thay thế là bộ biến dự báo mở rộng, gồm thêm 10 biến cùng số lượt nhấp theo từng tuần (2 biến tại ngày 13, 4 biến tại ngày 27) |""",
 """| 19 biến dự báo chính có thể dùng trong các bảng đặc trưng, tất cả đều ghi nhận tính đến hết thời điểm chốt dữ liệu. Biến điểm trung bình của bài đánh giá chấm bằng máy (CMA) bị loại, vì dưới 10% số dòng huấn luyện có giá trị này. Phương án thay thế là bộ biến dự báo mở rộng: thêm 10 biến dự báo khác, cộng với số lượt nhấp của từng tuần (2 biến tại ngày 13, 4 biến tại ngày 27) |"""),
("""việc chọn cách liên hệ được hoãn |""", """việc chọn hình thức liên hệ được hoãn |"""),
("""nên AQ4 dùng lại điểm rủi ro của AQ3 và chỉ bổ sung quy tắc cắt bảng xếp hạng ở độ dài mà hạn mức liên hệ cho phép; trong khi đó, AQ1 và AQ2""",
 """nên AQ4 dùng lại điểm rủi ro của AQ3. AQ4 chỉ bổ sung một quy tắc: giữ lại phần đầu của bảng xếp hạng, với số tên bằng mức mà hạn mức liên hệ cho phép. Trong khi đó, AQ1 và AQ2"""),
]
