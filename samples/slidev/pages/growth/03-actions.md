---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# P3 · Hai pilot riêng, một cổng quyết định

<div class="repurchase-line"><b>89.71%</b><span>Trong 2,829 khách mua từ 2 lần trở lên, 2,538 khách đã mua lại ít nhất một sản phẩm</span><small>Không phải hai sản phẩm trong cùng đơn.</small></div>
<div class="pilot-grid">
<div><span>PILOT A · MUA KÈM</span><b>Một cặp, một can thiệp</b><p>CRM · ngày 61-120<br />Kiểm tra tồn kho, giá vốn, cỡ mẫu và nhóm đối chứng.</p></div>
<div><span>PILOT B · QUỐC TẾ</span><b>Danh mục Đức, Pháp</b><p>Marketing + logistics · ngày 121-180<br />Chốt chi phí giao hàng, biên lợi nhuận và năng lực phục vụ.</p></div>
</div>
<div class="decision-gate"><b>MỞ RỘNG</b><span>khi lợi nhuận tăng thêm dương, hiệu quả đủ rõ và hủy không vượt guardrail đã chốt</span></div>

<!--
Khoảng 70 giây.

Mục tiêu: Giải thích cách biến hai tín hiệu tăng trưởng thành hai thử nghiệm có thể đo lường và có điều kiện dừng rõ ràng.

"Đầu tiên, chúng ta chỉ xét 2.829 khách đã mua hàng từ hai lần trở lên, vì phải có ít nhất hai hóa đơn mới có thể quan sát việc mua lại. Trong nhóm này, 2.538 khách đã mua lại ít nhất một sản phẩm mà họ từng mua trước đó. Lấy 2.538 chia cho 2.829 được 89,71%.

Ví dụ, nếu một khách mua một chiếc cốc trong hóa đơn đầu và mua lại đúng chiếc cốc đó trong hóa đơn sau, khách này được tính là mua lại. Nếu khách mua cốc và đĩa trong cùng một hóa đơn, đó là mua kèm và không phải điều mà tỷ lệ 89,71% đang đo.

Con số này cho thấy việc quay lại mua ít nhất một sản phẩm cũ khá phổ biến trong nhóm khách đã có nhiều hóa đơn. Nó không có nghĩa là 89,71% của toàn bộ khách hàng quay lại, và cũng không dự báo tỷ lệ giữ chân trong tương lai.

Pilot A kiểm tra cơ hội bán kèm trong ngày 61 đến 120. Nhóm chỉ chọn một cặp sản phẩm và một cách tác động rõ ràng, chẳng hạn gợi ý mua cùng nhau. Một nhóm khách nhìn thấy đề xuất, nhóm đối chứng không nhìn thấy. Trước khi chạy, phải đảm bảo đủ tồn kho, biết giá vốn và có đủ khách để so sánh.

Pilot B kiểm tra một danh mục sản phẩm tại Đức và Pháp trong ngày 121 đến 180. Trước khi chạy, nhóm phải biết chi phí giao hàng, lợi nhuận trên mỗi đơn và liệu đội vận hành có phục vụ thêm đơn quốc tế hay không.

Hai thử nghiệm cần tách nhóm hoặc tách thời gian để kết quả của thử nghiệm này không làm sai kết quả của thử nghiệm kia. Doanh nghiệp chỉ mở rộng khi lợi nhuận tăng thêm là dương, kết quả đủ rõ và tỷ lệ hủy không vượt mức giới hạn đã thống nhất. Nếu không đạt, doanh nghiệp điều chỉnh hoặc dừng."

Giải thích khi được hỏi:
- 2.829 người: số người mua có ít nhất hai hóa đơn mua hợp lệ. Điều kiện ít nhất hai hóa đơn tạo cơ hội quan sát một lần mua sau lần mua đầu.
- 2.538 người: trong 2.829 người trên, số người từng mua lại ít nhất một StockCode ở một hóa đơn mua khác.
- 89,71%: 2.538 / 2.829 = 89,7137%, làm tròn thành 89,71%. Mẫu số không phải toàn bộ 4.334 người mua có ID.
- Một khách chỉ được tính một lần trong 2.538 người, dù họ mua lại một hay nhiều SKU và dù họ mua lại nhiều lần.
- 59.497 / 266.221 = 22,35%: trong tất cả cặp CustomerID-StockCode có thể theo dõi, 59.497 cặp có mua lặp. Đây là tỷ lệ ở cấp cặp khách-sản phẩm, khác tỷ lệ 89,71% ở cấp người mua.
- 58,85% gross sales: tỷ trọng gross sales của các dòng mua có CustomerID thuộc những cặp khách-SKU từng lặp lại. Con số này gồm cả lần mua đầu nên không phải doanh số chỉ từ các lần mua lại.
- Mua lại cùng SKU: cùng một người mua mua lại một SKU ở hóa đơn khác. Mua kèm: hai SKU xuất hiện trong cùng một hóa đơn. Hai hành vi dùng mẫu số và câu hỏi khác nhau.
- Ngày 61-120 và 121-180: lịch triển khai đề xuất, không phải thời điểm được phát hiện từ dữ liệu lịch sử.
- Một cặp, một can thiệp: mỗi pilot chỉ thay đổi một đề xuất bán kèm rõ ràng để có thể quy chênh lệch kết quả cho can thiệp đó.
- Lợi nhuận tăng thêm dương: lợi nhuận sau chi phí của nhóm thử nghiệm cao hơn nhóm đối chứng. Net sales tăng nhưng chi phí tăng nhiều hơn vẫn không đạt điều kiện này.
- Guardrail hủy: giới hạn bảo vệ được chốt trước pilot. Báo cáo dùng mức tăng không quá 0,5 điểm phần trăm so với đối chứng như ngưỡng minh họa, chưa phải cam kết đã được phê duyệt.
- 0,5 điểm phần trăm khác 0,5% tương đối. Ví dụ, tỷ lệ hủy đối chứng 2,0% thì guardrail 0,5 điểm phần trăm cho phép tối đa 2,5%.
- Cỡ mẫu: báo cáo chưa có phương sai và mức tác động tối thiểu nên chưa tính được số khách hoặc số đơn cần thiết. Phải chốt trước khi chạy pilot.
- Pilot: thử nghiệm quy mô nhỏ trước khi triển khai rộng.
- Can thiệp: thay đổi cụ thể mà doanh nghiệp muốn kiểm tra, ví dụ hiển thị gợi ý mua kèm.
- Cỡ mẫu: số khách hoặc số đơn tối thiểu cần có để so sánh kết quả đáng tin cậy.
- Guardrail: chỉ số giới hạn để bảo vệ doanh nghiệp; ở đây là mức tỷ lệ hủy không được vượt quá.
- Hiệu quả đủ rõ: chênh lệch giữa hai nhóm đủ lớn và ổn định để không dễ bị giải thích bởi dao động ngẫu nhiên.

Chuyển: "Tiếp theo, chúng ta ghép các hành động này thành một lộ trình 180 ngày với người phụ trách và điều kiện chuyển bước."
Nguồn: final-report-revised.docx, mục 3.2-3.3, 4.4, 4.6 và Bảng 5, 6, 13, 16.
-->
