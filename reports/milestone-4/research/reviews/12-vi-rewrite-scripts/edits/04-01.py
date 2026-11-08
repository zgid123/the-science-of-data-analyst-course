FILE = "04-01-evaluation-cards.vi.md"
PAIRS = [
# flag 37
("| Theo từng tuần, tỷ lệ cộng dồn các lượt đăng ký học đã bỏ lỡ ít nhất một bài được chấm điểm, tách theo kết quả |",
 "| Tỷ lệ cộng dồn các lượt đăng ký học đã bỏ lỡ bài được chấm điểm đầu tiên, tính đến từng tuần và tách theo kết quả cuối cùng |"),
# flag 38
("tỷ lệ khi bỏ 138 lượt đăng ký học có cờ chất lượng dữ liệu do thiếu ngày rút khỏi module hoặc ngày đăng ký |",
 "tỷ lệ khi bỏ 138 lượt đăng ký học bị đánh dấu thiếu ngày rút khỏi module hoặc thiếu ngày đăng ký |"),
# flags 39, 28 (de-duplicated clicks), 38
("| Phần dư trung bình theo khoảng giá trị dự báo (binned residuals), xét theo kỳ mở và theo mức hoạt động. Tương quan giữa các dấu hiệu dựa trên lượt nhấp. Phân tích độ nhạy theo bốn cách: dùng số lượt nhấp đếm lại sau khi mỗi bản ghi lặp lại hoàn toàn chỉ được tính một lần; dùng phiên bản quy tắc dấu hiệu sớm có tính thêm CMA nộp trễ; bỏ 138 lượt đăng ký học có cờ chất lượng dữ liệu; và bỏ các kỳ mở không có bài đến hạn |",
 "| Tính phần dư trung bình theo khoảng giá trị dự báo (binned residuals) cho từng kỳ mở và từng mức hoạt động. Đo tương quan giữa các dấu hiệu được tính từ lượt nhấp. Phân tích độ nhạy theo bốn cách: dùng số lượt nhấp sau khi loại các bản ghi trùng lặp hoàn toàn; dùng phiên bản quy tắc dấu hiệu sớm có tính thêm CMA nộp trễ; bỏ 138 lượt đăng ký học bị đánh dấu thiếu ngày; và bỏ các kỳ mở không có bài đến hạn |"),
# flag 40
("Kết quả gộp bằng tổng số sinh viên không hoàn thành có tên trong các danh sách, chia cho tổng mức tối đa mà các danh sách đó có thể đạt |",
 "Kết quả gộp bằng tổng số sinh viên không hoàn thành có tên trong các danh sách, chia cho tổng số sinh viên không hoàn thành mà các danh sách đó có thể chứa nhiều nhất; mỗi danh sách chứa được nhiều nhất k sinh viên không hoàn thành (hoặc toàn bộ sinh viên không hoàn thành của kỳ mở, nếu số này nhỏ hơn k) |"),
# flags 41, 42
("(khi k cố định, ba chỉ số này là các cách biểu diễn khác của cùng số dương tính thật);",
 "(khi k cố định, cả ba chỉ số đều được tính từ cùng một con số: số sinh viên không hoàn thành có tên trong danh sách);"),
("lợi ích ròng (net benefit), chỉ dùng làm bối cảnh, vì chỉ số này",
 "lợi ích ròng (net benefit), chỉ dùng để tham khảo, vì chỉ số này"),
# flag 43 and the English sync (second freeze defined in place)
("sau lần chốt thứ hai, tức lần chốt mô hình cuối cùng, mô hình tính điểm rủi ro cho 13 kỳ mở năm 2014 đúng một lần và lần chạy này được ghi nhật ký [21], [26] (Mục 4.2; Phụ lục III) |",
 "sau lần chốt thứ hai, là lần chốt mô hình cuối cùng trước khi mở bất kỳ kết quả nào của tập kiểm thử (Mục 4.2), mô hình tính điểm rủi ro cho 13 kỳ mở năm 2014 đúng một lần và lần chạy này được ghi nhật ký [21], [26] (Mục 4.2; Phụ lục III) |"),
# flag 44
("độ ổn định của danh sách quanh hạng k khi lấy mẫu lại bằng bootstrap;",
 "độ ổn định của danh sách khi lấy mẫu lại bằng bootstrap, tức sinh viên xếp gần hạng k có còn trong danh sách hay không;"),
# flag 45 (protected term kept; English added at first use in the file)
("| Kiểm định khẳng định, tức kiểm định chính thức trên các nhóm đã ấn định trước,",
 "| Kiểm định khẳng định (confirmatory test), tức kiểm định chính thức trên các nhóm đã ấn định trước,"),
# flag 46 and the English sync (S2 before S3)
("Ngoài ra, số kỳ mở thắng, hòa và thua được đếm riêng. S3 (điều kiện để hiển thị xác suất):",
 "Ngoài ra, số kỳ mở thắng, hòa và thua được đếm riêng. S2 là độ chính xác của danh sách dài k; chỉ số này được báo cáo nhưng không phải điều kiện đạt (Bảng 4.5). S3 (điều kiện để hiển thị xác suất):"),
# flag 47
("cả hai đều xét trên giá trị ước lượng của dữ liệu gộp mọi kỳ mở;",
 "cả hai đều tính trên ước lượng điểm gộp chung cho mọi kỳ mở;"),
# flag 48
("Các phạm vi dữ liệu, thời điểm chốt dữ liệu và hạn mức liên hệ khác đều là phân tích độ nhạy và không thể thay đổi kết luận |",
 "Các phạm vi dữ liệu, thời điểm chốt dữ liệu và hạn mức liên hệ khác chỉ là phân tích độ nhạy và không được dùng để thay đổi kết luận về S1 |"),
# flag 49
("| Các kỳ mở mà các vị trí trong danh sách bị dùng cho những sinh viên về sau vẫn hoàn thành.",
 "| Các kỳ mở mà hạn mức liên hệ của danh sách bị dùng cho những sinh viên về sau vẫn hoàn thành."),
# flag 50
("kiểm định khẳng định về công bằng ở Mục 4.4 đạt hoặc mọi nhóm mà kiểm định này nêu tên đều được xem xét lại trước khi đưa danh sách vào sử dụng;",
 "kiểm định khẳng định về công bằng ở Mục 4.4 đạt hoặc mọi nhóm bị kiểm định này đánh dấu đều được xem xét lại trước khi đưa danh sách vào sử dụng;"),
]
