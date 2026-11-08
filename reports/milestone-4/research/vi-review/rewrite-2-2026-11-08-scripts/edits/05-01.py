FILE = "05-01-leakage-interpretability.vi.md"
PAIRS = [
# proxy → biến đại diện (first use in the file)
("Dạng thứ hai là biến dự báo thực chất chỉ là biến thay thế cho biến kết quả.",
 "Dạng thứ hai là biến dự báo thực chất chỉ là biến đại diện (proxy) cho biến kết quả."),
# flag 72
("Người xây dựng mô hình không được thấy thông tin nằm sau điểm phân tách giữa dữ liệu huấn luyện và dữ liệu kiểm thử [40].",
 "Người xây dựng mô hình không được thấy bất kỳ thông tin nào thuộc phần dữ liệu kiểm thử, tức phần nằm sau mốc tách dữ liệu huấn luyện với dữ liệu kiểm thử [40]."),
# flag 73
("Bên cạnh đó, phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 kiểm tra lại điều kiện đó,",
 "Bên cạnh đó, phân tích độ nhạy với phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 được dùng để kiểm tra lại điều kiện này,"),
# flag 74
("Do hệ số của một mô hình chỉ là một trong nhiều cách mô tả dữ liệu tốt như nhau, báo cáo không diễn giải hệ số nào thành nguyên nhân.",
 "Như vậy, bộ hệ số của mô hình được chọn chỉ là một trong nhiều bộ hệ số phù hợp với dữ liệu, nên báo cáo không diễn giải hệ số nào thành nguyên nhân."),
]
