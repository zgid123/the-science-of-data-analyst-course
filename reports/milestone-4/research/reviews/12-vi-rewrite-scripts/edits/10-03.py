FILE = "10-03-validation-protocol.vi.md"
PAIRS = [
# flag 92
("các dòng của những sinh viên này bị loại khỏi dữ liệu huấn luyện của fold đó, ở cả vòng kiểm định chéo ngoài lẫn vòng trong |",
 "các dòng của những sinh viên này bị loại khỏi dữ liệu huấn luyện của fold đó, ở cả vòng ngoài (vòng kiểm định chéo dùng để đánh giá và chọn mô hình) lẫn vòng trong (vòng kiểm định chéo chạy bên trong mỗi fold huấn luyện để tinh chỉnh siêu tham số, bước 3) |"),
# flag 93
("được tinh chỉnh bằng một vòng loại trừ từng kỳ mở bên trong;",
 "được tinh chỉnh bằng kiểm định chéo lồng nhau: bên trong mỗi fold huấn luyện, một vòng loại trừ từng kỳ mở nữa (vòng trong) được chạy trên các kỳ mở huấn luyện của fold đó;"),
# flag 94
("chênh lệch nằm trong biến thiên do lấy mẫu ít có ý nghĩa thực tế [31], [53] |",
 "những chênh lệch không vượt quá biến thiên do lấy mẫu thì ít có ý nghĩa thực tế [31], [53] |"),
# flag 95
("Khả năng áp dụng mô hình cho một kỳ mở mới là vấn đề khác, vì bằng chứng cho khả năng này chỉ đến từ 9 kỳ mở huấn luyện. Do đó, nhóm tác giả kiểm tra khả năng áp dụng trực tiếp bằng cách chia dữ liệu theo kỳ mở thay vì suy ra từ cỡ mẫu; cũng vì lý do này, mô hình riêng cho từng module vẫn không phải lựa chọn tốt, do phép co hệ số không khắc phục được mẫu nhỏ [17].",
 "Khả năng áp dụng mô hình cho một kỳ mở mới là vấn đề khác, vì bằng chứng cho khả năng này chỉ đến từ 9 kỳ mở huấn luyện. Do chỉ có 9 kỳ mở, nhóm tác giả kiểm tra khả năng áp dụng trực tiếp bằng cách chia dữ liệu theo kỳ mở thay vì suy ra từ cỡ mẫu. Cũng vì số kỳ mở ít, mô hình riêng cho từng module không phải lựa chọn tốt: dữ liệu của từng module nhỏ, mà phép co hệ số không khắc phục được mẫu nhỏ [17]."),
]
