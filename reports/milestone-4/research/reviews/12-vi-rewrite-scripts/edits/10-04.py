FILE = "10-04-fairness-spec.vi.md"
PAIRS = [
# English sync (column header) and flag 96; the values are the group's fewest enrolments in one test run (code/design_facts.py, test_rows_min_per_run)
("| Lượt đăng ký học trong tập kiểm thử | Kỳ mở nhỏ nhất của tập kiểm thử | Cách xử lý |",
 "| Lượt đăng ký học trong tập kiểm thử | Số lượt đăng ký học ít nhất của nhóm trong một kỳ mở của tập kiểm thử | Cách xử lý |"),
# flag 97
("| Tỷ lệ của từng nhóm trong danh sách so với tỷ lệ của nhóm đó trong số sinh viên không hoàn thành | Mô tả |",
 "| Phần trăm danh sách mà mỗi nhóm chiếm, so với phần trăm nhóm đó chiếm trong số sinh viên không hoàn thành | Mô tả |"),
# flags 98, 99
("kèm giá trị tham chiếu, tức ABROCA khi nhãn nhóm được hoán vị ngẫu nhiên trong từng kỳ mở [34] | Mô tả; riêng chỉ số này không bao giờ dẫn đến việc xem xét |",
 "kèm giá trị tham chiếu: ABROCA tính lại sau khi hoán vị ngẫu nhiên nhãn nhóm trong từng kỳ mở, tức mức ABROCA có thể có chỉ do ngẫu nhiên [34] | Mô tả; chỉ số này không tự mình kích hoạt việc xem xét lại một nhóm |"),
# proxy → biến đại diện (first use in the file)
("| Kiểm tra biến thay thế |", "| Kiểm tra biến đại diện (proxy check) |"),
# flag 100
("| Cho thấy vị trí cắt tại hạng k tùy ý đến mức nào |",
 "| Cho thấy điểm cắt tại hạng k phụ thuộc vào biến động ngẫu nhiên đến mức nào |"),
]
