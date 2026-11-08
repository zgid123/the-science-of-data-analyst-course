FILE = "04-02-validation-strategy.vi.md"
PAIRS = [
# flag 51
("Tại ngày 27, tập kiểm thử có 1.586 lượt đăng ký học của sinh viên đã có mặt năm 2013. Giống như khi sử dụng thực tế, các lượt này vẫn nằm trong tập kiểm thử và chỉ bị loại ra trong một phân tích độ nhạy.",
 "Tại ngày 27, tập kiểm thử có 1.586 lượt đăng ký học của những sinh viên đã có mặt trong dữ liệu năm 2013, tức dữ liệu dùng để phát triển mô hình. Giống như khi sử dụng thực tế, các lượt này vẫn nằm trong tập kiểm thử và chỉ bị loại ra trong một phân tích độ nhạy."),
# flag 52
("Nếu một sinh viên có mặt cả trong kỳ mở được tách ra để đánh giá, sinh viên đó bị loại khỏi dữ liệu huấn luyện của fold đó,",
 "Những sinh viên có mặt cả trong các kỳ mở huấn luyện lẫn trong kỳ mở được tách ra để đánh giá bị loại khỏi dữ liệu huấn luyện của fold đó,"),
# flag 53
("Lập luận thứ nhất là điểm kiểm định chéo sau khi tinh chỉnh lạc quan hơn đáng kể so với thực tế [30].",
 "Lập luận thứ nhất là kết quả kiểm định chéo của một mô hình đã tinh chỉnh siêu tham số cao hơn đáng kể so với hiệu năng thực tế [30]."),
# flag 54
("Giao thức áp dụng quy trình chốt hai bước được đề xuất cho mô hình dự báo:",
 "Giao thức áp dụng quy trình chốt hai bước dành cho mô hình dự báo:"),
# flags 55, 56
("Các kỳ mở J năm 2013 kéo dài 261–268 ngày, nên khi các kỳ mở B năm 2014 đến thời điểm chốt dữ liệu, kết quả của các kỳ mở J này vẫn chưa có. Vì vậy, nhóm tác giả bổ sung phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013, những kỳ mở duy nhất mà một trường đại học đã có kết quả vào thời điểm đó;",
 "Các kỳ mở J năm 2013 bắt đầu vào tháng 10 năm 2013 và kéo dài 261–268 ngày, tức kết thúc vào khoảng giữa năm 2014. Trong khi đó, các kỳ mở B năm 2014 bắt đầu vào tháng 2 năm 2014 và đến thời điểm chốt dữ liệu chỉ vài tuần sau đó; vào lúc này, kết quả của các kỳ mở J năm 2013 vẫn chưa có. Vì vậy, nhóm tác giả bổ sung phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013, những kỳ mở duy nhất mà một trường đại học áp dụng mô hình đã có kết quả vào thời điểm đó;"),
# flag 57
("Kiểm định này giả sử dấu của chênh lệch ở từng kỳ mở chỉ là ngẫu nhiên. Với giả sử đó, kiểm định tính xem các chênh lệch có lợi cho mô hình ở mức bằng hoặc hơn mức quan sát được sẽ xuất hiện thường xuyên đến đâu.",
 "Kiểm định này giả sử dấu của chênh lệch ở từng kỳ mở chỉ là ngẫu nhiên. Với giả sử đó, kiểm định ước lượng tần suất thu được một tập chênh lệch có lợi cho mô hình không kém tập chênh lệch quan sát được."),
# flag 58
("Tiêu chí thứ ba là nguy cơ chung được ước lượng với sai số không quá 0,05.",
 "Tiêu chí thứ ba là nguy cơ chung, tức tỷ lệ không hoàn thành tính trên toàn bộ dữ liệu, được ước lượng với sai số không quá 0,05."),
]
