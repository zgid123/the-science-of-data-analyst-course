FILE = "05-01-leakage-interpretability.vi.md"
PAIRS = [
("""Rò rỉ thông tin gồm ba dạng sai sót quan trọng trong dự án này: tách dữ liệu huấn luyện và dữ liệu kiểm thử không triệt để, kể cả trường hợp bước tiền xử lý được ước lượng trên toàn bộ bộ dữ liệu; biến dự báo thực chất là biến đại diện của biến kết quả; và rò rỉ theo thời gian hoặc sự phụ thuộc giữa mẫu huấn luyện và mẫu kiểm thử [22].""",
 """Rò rỉ thông tin gồm ba dạng sai sót quan trọng trong dự án này. Dạng thứ nhất là tách dữ liệu huấn luyện và dữ liệu kiểm thử không triệt để, kể cả trường hợp bước tiền xử lý được ước lượng trên toàn bộ bộ dữ liệu. Dạng thứ hai là biến dự báo thực chất chỉ là biến thay thế cho biến kết quả. Dạng thứ ba là thông tin của thời điểm sau lọt vào dữ liệu huấn luyện, hoặc mẫu huấn luyện và mẫu kiểm thử phụ thuộc lẫn nhau [22]."""),
("""Vì vậy, kết quả của các kỳ mở năm 2014 được giữ kín cho đến khi tập kiểm thử được chấm điểm đúng một lần; AQ2 cũng chờ đến sau lần chấm điểm đó""",
 """Vì vậy, kết quả của các kỳ mở năm 2014 được giữ kín cho đến lần kiểm tra duy nhất trên tập kiểm thử; AQ2 cũng chờ đến sau lần kiểm tra đó"""),
("""Nhiều mô hình khác nhau có thể mô tả dữ liệu tốt gần như ngang nhau [5], vì vậy, báo cáo không diễn giải hệ số nào thành nguyên nhân. Với AQ2, các ước lượng thu được khi đưa mọi dấu hiệu cùng lúc vào mô hình được trình bày bên cạnh các chênh lệch chưa hiệu chỉnh.""",
 """Nhiều mô hình khác nhau, với các hệ số khác nhau, có thể mô tả dữ liệu tốt gần như ngang nhau [5]. Do hệ số của một mô hình chỉ là một trong nhiều cách mô tả dữ liệu tốt như nhau, báo cáo không diễn giải hệ số nào thành nguyên nhân. Với AQ2, các ước lượng đã hiệu chỉnh lẫn nhau (hiệu ứng riêng phần) được trình bày bên cạnh các chênh lệch chưa hiệu chỉnh."""),
("""dữ liệu đến từ đào tạo từ xa tại Vương quốc Anh (UK) giai đoạn 2013–2014.""", """dữ liệu đến từ đào tạo từ xa tại UK giai đoạn 2013–2014."""),
]
