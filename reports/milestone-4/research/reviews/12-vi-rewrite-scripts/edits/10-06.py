FILE = "10-06-ai-critiques.vi.md"
PAIRS = [
# flag 107 (settled: model scoring → tính điểm rủi ro)
("phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 để chấm điểm các kỳ mở B năm 2014 |",
 "phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 để tính điểm rủi ro cho các kỳ mở B năm 2014 |"),
# flag 108 (established term kept, defined in place)
("| Fail không phải kết quả dạng thời gian đến sự kiện; kiểm duyệt không mang thông tin được nêu là một giả định |",
 "| Fail không phải kết quả dạng thời gian đến sự kiện. Kiểm duyệt không mang thông tin (non-informative censoring) được nêu rõ là một giả định: khi một sinh viên bị kiểm duyệt (censored), tức thời điểm rút khỏi module không được quan sát vì việc theo dõi đã dừng, lý do dừng theo dõi được giả định không liên quan đến nguy cơ rút khỏi module |"),
# proxy → biến đại diện
("kiểm tra biến thay thế;", "kiểm tra biến đại diện (proxy check);"),
# flag 109
("| Hiệu chuẩn tổng thể có offset; ngưỡng áp dụng cho ước lượng gộp; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở sau |",
 "| Hiệu chuẩn tổng thể được định nghĩa là hệ số chặn khi log-odds của điểm rủi ro được đưa vào làm offset (hệ số cố định bằng 1); các ngưỡng hiệu chuẩn áp dụng cho ước lượng gộp mọi kỳ mở; chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở diễn ra sau |"),
# flag 110
("ngưỡng chênh lệch khoảng 89 sinh viên; loại ở mọi vòng |",
 "ngưỡng chênh lệch khoảng 89 sinh viên; loại các sinh viên này ở mọi vòng, cả vòng ngoài lẫn vòng trong |"),
]
