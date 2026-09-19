---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# P3 · Hai cặp mua kèm cần kiểm chứng

<StoryEvidence kind="bundles" />
<div class="note">Lift đo mức đồng xuất hiện so với kỳ vọng độc lập, không đo doanh số tăng do bundle.</div>

<!--
Khoảng 60 giây.

Mục tiêu: Giải thích vì sao hai cặp sản phẩm đáng thử bán kèm, đồng thời tránh hiểu sai rằng lift là mức tăng doanh số.

"Cơ hội tăng trưởng đầu tiên đến từ những sản phẩm thường xuất hiện trong cùng một hóa đơn. Phân tích này dùng 19.773 hóa đơn mua hợp lệ. Mỗi hóa đơn được xem như một giỏ hàng và mỗi SKU chỉ được đếm một lần trong một giỏ, dù khách mua nhiều đơn vị của SKU đó.

Trước hết là cặp túi Jumbo. SKU 85099B, Jumbo Bag Red Retrospot, xuất hiện trong 2.089 hóa đơn. SKU 22386, Jumbo Bag Pink Polkadot, xuất hiện trong 1.218 hóa đơn. Có 825 hóa đơn chứa đồng thời cả hai SKU.

Con số kỳ vọng 128,7 được tính trong trường hợp giả định hai sản phẩm được mua độc lập. Công thức là 2.089 nhân 1.218 rồi chia cho tổng 19.773 hóa đơn, bằng 128,68 và làm tròn thành 128,7. Đây là giá trị kỳ vọng theo mô hình nên có thể là số thập phân, không phải số hóa đơn quan sát thực tế.

Support của cặp túi là 825 chia 19.773, bằng 4,17%. Nghĩa là cứ 100 hóa đơn mua thì có khoảng 4,17 hóa đơn chứa cả hai sản phẩm. Confidence theo chiều từ 85099B sang 22386 là 825 chia 2.089, bằng 39,49%. Nghĩa là trong các hóa đơn có túi đỏ, khoảng 39,49% cũng có túi hồng. Nếu đọc theo chiều ngược lại, confidence là 825 chia 1.218, bằng 67,73%, nên phải nói rõ chiều khi giải thích confidence.

Lift được tính bằng số đồng xuất hiện quan sát chia cho số kỳ vọng: 825 chia 128,68 bằng 6,41. Có thể viết tương đương là 825 nhân 19.773, rồi chia cho 2.089 nhân 1.218. Lift 6,41 nghĩa là hai SKU xuất hiện cùng nhau nhiều gấp 6,41 lần mức kỳ vọng nếu việc mua hai sản phẩm độc lập.

Tiếp theo là cặp tách Regency. SKU 22699 xuất hiện trong 1.065 hóa đơn, SKU 22697 xuất hiện trong 1.013 hóa đơn và có 767 hóa đơn chứa cả hai. Mức kỳ vọng độc lập là 1.065 nhân 1.013 chia 19.773, bằng 54,56 và làm tròn thành 54,6.

Support của cặp tách là 767 chia 19.773, bằng 3,88%. Confidence theo chiều từ 22699 sang 22697 là 767 chia 1.065, bằng 72,02%. Theo chiều ngược lại, confidence là 767 chia 1.013, bằng 75,72%. Lift là 767 chia 54,56, bằng 14,06. Nghĩa là cặp tách xuất hiện cùng nhau nhiều gấp khoảng 14 lần mức kỳ vọng độc lập.

Chỉ số này được gọi là lift. Lift cao cho thấy hai sản phẩm có mối liên hệ mua kèm mạnh hơn ngẫu nhiên. Tuy nhiên, lift 14 không có nghĩa doanh số sẽ tăng 14 lần nếu tạo một gói sản phẩm. Dữ liệu mới chỉ cho thấy khách đã có xu hướng mua chúng cùng nhau; chưa cho biết giá gói, lợi nhuận, tồn kho hay phản ứng của khách khi doanh nghiệp chủ động đề xuất.

Vì vậy, hai cặp này là ứng viên tốt để thử nghiệm ở quy mô nhỏ, chưa phải đề xuất bán gói trên toàn hệ thống."

Giải thích khi được hỏi:
- SKU: mã dùng để nhận diện một sản phẩm cụ thể.
- Bundle hoặc bán kèm: đề xuất hai sản phẩm như một bộ hoặc gợi ý mua cùng nhau.
- 19.773: tổng số hóa đơn mua hợp lệ dùng làm số giỏ hàng N trong mọi công thức.
- 2.089 và 1.218: số hóa đơn chứa từng SKU của cặp túi. 825 là giao của hai tập hóa đơn này.
- 1.065 và 1.013: số hóa đơn chứa từng SKU của cặp tách. 767 là giao của hai tập hóa đơn này.
- 128,7 và 54,6: số hóa đơn mua kèm kỳ vọng nếu hai SKU trong từng cặp được mua độc lập. Đây là kết quả tính toán nên có thể là số thập phân.
- 825 và 767: số hóa đơn quan sát thực tế có cả hai SKU trong từng cặp.
- Trục 0-900 hóa đơn: thang đo chung của hai biểu đồ để so sánh độ dài thanh, không phải tổng số hóa đơn trong dữ liệu.
- Support: tỷ lệ toàn bộ hóa đơn chứa đồng thời cả hai sản phẩm. Công thức là n(A∩B) / N.
- Confidence: trong các hóa đơn có sản phẩm A, tỷ lệ cũng có sản phẩm B. Công thức là n(A∩B) / n(A). Chỉ số này có hướng nên đổi A và B sẽ cho kết quả khác.
- Lift: số lần hai sản phẩm thực sự xuất hiện cùng nhau chia cho số lần kỳ vọng nếu chúng được mua độc lập. Công thức là n(A∩B) × N / [n(A) × n(B)]. Lift không có hướng.
- Lift bằng 1: mức đồng xuất hiện đúng bằng kỳ vọng độc lập. Lift lớn hơn 1: hai sản phẩm xuất hiện cùng nhau nhiều hơn kỳ vọng. Lift nhỏ hơn 1: hai sản phẩm xuất hiện cùng nhau ít hơn kỳ vọng.
- Ngưỡng chọn ứng viên: mỗi SKU xuất hiện trong ít nhất 300 hóa đơn, cặp xuất hiện cùng nhau trong ít nhất 150 hóa đơn và lift lớn hơn 1,2. Hai cặp trên vượt cả ba điều kiện.

Chuyển: "Ngoài cơ hội bán kèm, dữ liệu còn gợi ý hai thị trường quốc tế đáng thử, nhưng chúng ta phải đọc AOV cùng với số lượng khách hàng."

Q&A dữ liệu: Mỗi SKU chỉ được đếm một lần trong mỗi hóa đơn. Phân tích giỏ hàng gồm cả khách có và thiếu CustomerID. Giao dịch hủy chưa được nối với đơn gốc nên chưa thể loại chính xác theo từng giỏ. Các số liệu mô tả sự đồng xuất hiện lịch sử, chưa chứng minh một gợi ý mua kèm sẽ làm doanh số hoặc lợi nhuận tăng.
Nguồn: final-report-revised.docx, mục 4.4 và Bảng 14.
-->
