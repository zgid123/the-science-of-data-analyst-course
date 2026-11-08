FILE = "04-03-metrics-success.vi.md"
PAIRS = [
# flag 59
("Để tính con số này, nhóm tác giả ước lượng một mô hình hiệu chuẩn lại (recalibration model) với độ dốc được giữ cố định, rồi lấy hệ số chặn của mô hình đó.",
 "Để tính con số này, nhóm tác giả ước lượng một mô hình hiệu chuẩn lại (recalibration model), tức hồi quy logistic biến kết quả theo log-odds của điểm rủi ro, với độ dốc được giữ cố định bằng 1; hệ số chặn của mô hình này là hiệu chuẩn tổng thể."),
# flag 60
("trên một dải xác suất ngưỡng [25].",
 "tại nhiều mức xác suất ngưỡng khác nhau [25]."),
# flag 61
("Điều kiện thứ hai: khoảng tin cậy bootstrap một phía 95% của chênh lệch nằm hoàn toàn dưới 0; khoảng này đã được hiệu chỉnh Holm trên ba nhóm, tức phép hiệu chỉnh giữ xác suất có ít nhất một nhóm bị nêu tên nhầm ở mức 5%. Nhóm thỏa cả hai điều kiện được nêu tên để xem xét lại | Như trên; ba nhóm của kiểm định khẳng định (Mục 4.4) | Điều kiện để đưa vào sử dụng; nhóm được nêu tên sẽ được xem xét lại |",
 "Điều kiện thứ hai: khoảng tin cậy bootstrap một phía 95% của chênh lệch nằm hoàn toàn dưới 0. Khoảng tin cậy này được hiệu chỉnh Holm trên ba nhóm. Phép hiệu chỉnh Holm giữ xác suất đánh dấu nhầm ít nhất một trong ba nhóm ở mức 5%. Nhóm thỏa cả hai điều kiện bị đánh dấu để xem xét lại | Như trên; ba nhóm của kiểm định khẳng định (Mục 4.4) | Điều kiện để đưa vào sử dụng; nhóm bị đánh dấu sẽ được xem xét lại |"),
# flag 48 (same wording as 04-01)
("Mọi phạm vi dữ liệu, thời điểm chốt dữ liệu và hạn mức liên hệ khác đều là phân tích độ nhạy và không thể thay đổi kết luận.",
 "Mọi phạm vi dữ liệu, thời điểm chốt dữ liệu và hạn mức liên hệ khác chỉ là phân tích độ nhạy và không được dùng để thay đổi kết luận về S1."),
# flag 62
("còn giới hạn độ dốc từ 0,8 đến 1,2 cho phép độ phân tán của nguy cơ dự báo rộng quá hoặc hẹp quá 20%.",
 "còn giới hạn độ dốc từ 0,8 đến 1,2 cho phép độ phân tán của nguy cơ dự báo rộng hơn hoặc hẹp hơn mức đúng tối đa 20%."),
]
