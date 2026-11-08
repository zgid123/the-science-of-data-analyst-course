FILE = "03-03-predictive.vi.md"
PAIRS = [
# flag 26
("xếp hạng sinh viên theo số dấu hiệu; khi bằng số dấu hiệu, sinh viên có tỷ lệ hoạt động thấp hơn được xếp trước",
 "xếp hạng sinh viên theo số dấu hiệu; nếu hai sinh viên có cùng số dấu hiệu, sinh viên có tỷ lệ hoạt động thấp hơn được xếp trước"),
# flag 27
("Module và tháng bắt đầu đều đi vào mô hình dưới dạng nhiều số hạng, nên mô hình có tổng cộng 23 tham số.",
 "Module và tháng bắt đầu là biến phân loại, nên mỗi biến đi vào mô hình dưới dạng nhiều số hạng (biến giả); vì vậy, 19 biến dự báo tương ứng với tổng cộng 23 tham số."),
# flags 28, 29
(" Bộ biến dự báo mở rộng bổ sung 10 biến: biến chỉ báo thiếu ngày đăng ký, số lượt nhấp đếm lại sau khi mỗi bản ghi lặp lại hoàn toàn chỉ được tính một lần, lượt nhấp trong 14 ngày trước ngày bắt đầu, số ngày kể từ lượt nhấp cuối, xu hướng hoạt động trong tuần cuối, số bài nộp sớm và lượt nhấp trên bốn loại tài nguyên học tập. Ngoài 10 biến này, bộ biến dự báo mở rộng còn gồm số lượt nhấp của từng tuần, 2 biến tại ngày 13 và 4 biến tại ngày 27; bộ này được thử như một phương án thay thế (Bảng 2.3).",
 "\n\nNgoài bộ biến dự báo chính, nhóm tác giả thử một phương án thay thế là bộ biến dự báo mở rộng (Bảng 2.3). Bộ này giữ các biến dự báo chính và bổ sung 10 biến: biến chỉ báo thiếu ngày đăng ký, số lượt nhấp sau khi loại các bản ghi trùng lặp hoàn toàn, lượt nhấp trong 14 ngày trước ngày bắt đầu, số ngày kể từ lượt nhấp cuối, xu hướng hoạt động trong tuần cuối, số bài nộp sớm và lượt nhấp trên bốn loại tài nguyên học tập. Ngoài 10 biến này, bộ mở rộng còn gồm số lượt nhấp của từng tuần: 2 biến tại ngày 13 và 4 biến tại ngày 27."),
# flag 30
("Thứ ba, hai lớp nhãn có cỡ gần nhau, với 44–46% lượt đăng ký học không hoàn thành.",
 "Thứ ba, số lượt hoàn thành và số lượt không hoàn thành gần cân bằng: 44–46% lượt đăng ký học không hoàn thành."),
# flag 31
("Tuy nhiên, nghiên cứu so sánh (benchmark) cho kết quả này đã loại những bộ dữ liệu mà ở đó hồi quy logistic chỉ kém mô hình tốt nhất không quá 5%. Vì vậy, nghiên cứu đó không chứng minh rằng cây vượt hồi quy logistic [19].",
 "Tuy nhiên, nghiên cứu so sánh (benchmark) đưa ra kết quả này đã loại bỏ trước những bộ dữ liệu mà trên đó hồi quy logistic chỉ kém mô hình tốt nhất không quá 5%. Do các bộ dữ liệu có lợi cho hồi quy logistic đã bị loại, nghiên cứu đó không chứng minh rằng cây vượt hồi quy logistic [19]."),
# flag 32
("Hiệu chỉnh phạt chỉ cải thiện hiệu chuẩn ở mức trung bình, không chắc chắn trong từng trường hợp cụ thể [17];",
 "Hiệu chỉnh phạt chỉ cải thiện hiệu chuẩn khi tính trung bình trên nhiều trường hợp, chứ không chắc chắn trong từng trường hợp cụ thể [17];"),
]
