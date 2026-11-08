FILE = "04-03-metrics-success.vi.md"
PAIRS = [
("""Con số thứ nhất là hiệu chuẩn tổng thể: hệ số chặn của mô hình hiệu chuẩn lại khi cố định độ dốc.""",
 """Con số thứ nhất là hiệu chuẩn tổng thể. Để tính con số này, nhóm tác giả ước lượng một mô hình hiệu chuẩn lại (recalibration model) với độ dốc được giữ cố định, rồi lấy hệ số chặn của mô hình đó."""),
("""Một chênh lệch nhỏ hơn mức dao động giữa các mẫu ít có ý nghĩa thực tiễn [31]; vì vậy, thiết kế chỉ đặt một điều kiện đạt duy nhất trên một phạm vi dữ liệu duy nhất.""",
 """Một chênh lệch nhỏ hơn mức dao động giữa các mẫu ít có ý nghĩa thực tiễn [31]. Ngoài ra, nếu mô hình được đánh giá theo nhiều điều kiện đạt hoặc trên nhiều phạm vi dữ liệu, một trong số đó có thể đạt chỉ do ngẫu nhiên. Vì vậy, thiết kế chỉ đặt một điều kiện đạt duy nhất trên một phạm vi dữ liệu duy nhất."""),
("""khoảng tin cậy 95% của chênh lệch, tính bằng bootstrap hai tầng ghép cặp, nằm trên 0;""",
 """khoảng tin cậy 95% của chênh lệch, tính bằng bootstrap hai tầng với mô hình và quy tắc được so trên cùng mẫu lấy lại, nằm trên 0;"""),
("""tính trên ước lượng điểm gộp |""", """xét trên giá trị ước lượng của dữ liệu gộp mọi kỳ mở |"""),
("""| Không có nhóm nào của kiểm định khẳng định đồng thời thỏa hai điều kiện: tỷ lệ phát hiện trong giới hạn danh sách thấp hơn của các sinh viên còn lại quá 10 điểm phần trăm; và khoảng tin cậy bootstrap một phía 95% của chênh lệch, đã hiệu chỉnh Holm trên ba nhóm (phép hiệu chỉnh giữ xác suất có ít nhất một nhóm bị đánh dấu nhầm ở mức 5%), nằm hoàn toàn dưới 0. Nhóm thỏa cả hai điều kiện bị đánh dấu để xem xét lại | Như trên; ba nhóm của kiểm định khẳng định (Mục 4.4) | Điều kiện để đưa vào sử dụng; nhóm bị đánh dấu được xem xét lại |""",
 """| Trong ba nhóm của kiểm định khẳng định, không có nhóm nào thỏa đồng thời hai điều kiện sau. Điều kiện thứ nhất: tỷ lệ phát hiện trong giới hạn danh sách của nhóm thấp hơn tỷ lệ này ở các sinh viên còn lại quá 10 điểm phần trăm. Điều kiện thứ hai: khoảng tin cậy bootstrap một phía 95% của chênh lệch nằm hoàn toàn dưới 0; khoảng này đã được hiệu chỉnh Holm trên ba nhóm, tức phép hiệu chỉnh giữ xác suất có ít nhất một nhóm bị nêu tên nhầm ở mức 5%. Nhóm thỏa cả hai điều kiện được nêu tên để xem xét lại | Như trên; ba nhóm của kiểm định khẳng định (Mục 4.4) | Điều kiện để đưa vào sử dụng; nhóm được nêu tên sẽ được xem xét lại |"""),
("""Mức chắc chắn này đến từ bootstrap hai tầng ghép cặp và kiểm định hoán vị đổi dấu ở Mục 4.2.""",
 """Mức chắc chắn này đến từ bootstrap hai tầng và kiểm định hoán vị đổi dấu ở Mục 4.2."""),
("""đồng thời, giới hạn này cho phép độ phân tán của nguy cơ dự báo rộng hơn hoặc hẹp hơn 20%. Nếu mô hình không thỏa điều kiện hiệu chuẩn, đầu ra chỉ gồm thứ hạng và lý do; mô hình không bao giờ được hiệu chuẩn lại trên các kỳ mở năm 2014, vì làm vậy sẽ để dữ liệu kiểm thử định hình mô hình.""",
 """còn giới hạn độ dốc từ 0,8 đến 1,2 cho phép độ phân tán của nguy cơ dự báo rộng quá hoặc hẹp quá 20%. Nếu mô hình không thỏa điều kiện hiệu chuẩn, đầu ra chỉ gồm thứ hạng và lý do; mô hình không bao giờ được hiệu chuẩn lại trên các kỳ mở năm 2014, vì làm vậy sẽ để dữ liệu của tập kiểm thử định hình mô hình."""),
]
