---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# P2 · Chăm sóc có chọn lọc và có đối chứng

<div class="customer-stats">
<div><span>Trung vị / khách</span><b>£646.84</b></div>
<div><span>Trung bình / khách</span><b>£1,908.03</b></div>
<div><span>Khách dẫn đầu #14646</span><b>£278,778</b></div>
</div>
<div class="three-actions">
<div><span>01 · RÀ SOÁT</span><p>Xác minh loại tài khoản, chu kỳ mua và lợi nhuận của 434 người mua.</p></div>
<div><span>02 · PILOT CRM</span><p>Chốt khách đủ điều kiện, rồi phân ngẫu nhiên trước khi tiếp cận.</p></div>
<div><span>03 · QUYẾT ĐỊNH</span><p>So net/khách sau 60 ngày, lợi nhuận tăng thêm và tỷ lệ hủy.</p></div>
</div>
<div class="note">Tính cả khách không mua. Không giảm giá đại trà; theo dõi duy trì riêng đủ 180 ngày từ ngày phân nhóm.</div>

<!--
Khoảng 70 giây.

Mục tiêu: Giải thích cách chăm sóc khách hàng lớn mà vẫn đo được chương trình có thực sự tạo thêm lợi nhuận hay không.

"Ba con số ở trên cho thấy mức chi tiêu giữa các khách hàng rất không đồng đều. Một khách trung bình tạo 1.908 bảng, nhưng giá trị trung vị chỉ là 647 bảng. Nghĩa là một nửa số khách tạo không quá khoảng 647 bảng, còn mức trung bình bị kéo lên bởi một số khách rất lớn. Riêng khách 14646 tạo gần 279 nghìn bảng.

434 người mua này là nhóm 10% đứng đầu trong 4.334 người mua có CustomerID. Cụ thể, 10% nhân 4.334 bằng 433,4 nên nhóm làm tròn lên thành 434, sau đó xếp người mua theo net sales từ cao xuống thấp. 28 khách chỉ có bản ghi hủy không nằm trong quần thể này vì họ không phải người mua để đưa vào chương trình chăm sóc.

Vì vậy, đề xuất không phải là giảm giá cho tất cả 434 khách hàng dẫn đầu. Bước một là rà soát từng tài khoản: đây là khách cá nhân hay doanh nghiệp, họ thường mua theo chu kỳ nào và doanh nghiệp thực sự kiếm được bao nhiêu lợi nhuận từ họ.

Bước hai là chạy một Pilot CRM. CRM là Customer Relationship Management, tức quản lý quan hệ khách hàng. Pilot là một thử nghiệm nhỏ trước khi áp dụng cho toàn bộ nhóm khách. Sau khi rà soát 434 người mua dẫn đầu, doanh nghiệp chốt những khách đủ điều kiện và phân ngẫu nhiên họ thành hai nhóm trước khi liên hệ.

Nhóm thử nghiệm nhận đúng một hình thức chăm sóc đã xác định trước, chẳng hạn lời nhắc mua lại theo chu kỳ. Nhóm đối chứng tiếp tục nhận cách chăm sóc hiện tại. Hai nhóm cần được theo dõi trong cùng khoảng thời gian để phần chênh lệch phản ánh tác động của chương trình rõ hơn, thay vì khác biệt sẵn có giữa các khách hàng.

Bước ba là đánh giá sau 60 ngày. Chỉ số chính là net sales bình quân trên mỗi khách đã được phân nhóm. Khách không mua vẫn được tính với giá trị bằng 0. Sau đó, nhóm kiểm tra lợi nhuận tăng thêm sau chi phí chương trình và tỷ lệ hủy của hai nhóm. Nếu chỉ tính những người đã mua, kết quả sẽ bị lệch theo hướng tích cực.

Chỉ mở rộng chương trình khi nhóm được chăm sóc tạo thêm lợi nhuận mà không làm tỷ lệ hủy tăng. Việc khách có tiếp tục mua trong 180 ngày hay không được theo dõi riêng và có thể kết thúc sau lịch triển khai chung."

Giải thích khi được hỏi:
- £1.908,03 trung bình/khách: £8.269.399,91 net sales của 4.334 người mua có ID chia 4.334 = £1.908,0295, làm tròn thành £1.908,03.
- £646,84 trung vị/khách: sắp xếp net sales của 4.334 người mua và lấy mốc giữa. 50% người mua có net sales không cao hơn khoảng £646,84 và 50% không thấp hơn mức này.
- £296,78-£1.600,84: khoảng tứ phân vị trong báo cáo. 50% người mua ở giữa nằm trong khoảng này. Trung bình £1.908,03 cao hơn cả tứ phân vị trên, cho thấy phân phối lệch phải mạnh.
- 2 hóa đơn: trung vị số hóa đơn của một người mua có ID trong cả kỳ. Đây không phải số hóa đơn trung bình mỗi tháng.
- CustomerID 14646: mã nhận diện của người mua đứng đầu theo net sales, không phải khách xếp hạng thứ 14.646.
- £278.778,02 của khách 14646: net sales trong kỳ của riêng CustomerID này. Con số bằng khoảng 3,37% của £8.269.399,91 net sales người mua có ID và 2,85% của £9.771.318,16 net sales toàn kỳ.
- 434 người mua: 10% của 4.334 người mua có ID bằng 433,4. Nhóm làm tròn lên thành 434 và chọn theo net sales giảm dần.
- 28 khách chỉ có hủy: dùng để đối soát doanh số nhưng không đưa vào nhóm người mua mục tiêu của Pilot CRM.
- 60 ngày: cửa sổ đo chỉ số chính được đề xuất. Đây là thời gian tính từ ngày phân nhóm của từng khách, không phải số liệu lịch sử.
- Net sales/khách: tổng net sales của mỗi nhóm chia cho toàn bộ khách đã được phân vào nhóm đó. Khách không mua được ghi nhận bằng 0 để giữ nguyên mẫu số.
- Lợi nhuận tăng thêm: lợi nhuận của nhóm thử nghiệm trừ lợi nhuận ước tính từ nhóm đối chứng, sau khi trừ chi phí của chương trình CRM.
- 180 ngày: cửa sổ theo dõi duy trì riêng tính từ ngày phân nhóm. Nếu phân nhóm sau ngày 1 của lộ trình, kết quả 180 ngày có thể hoàn thành sau ngày 180 của kế hoạch.
- Pilot CRM: thử một hoạt động quản lý quan hệ khách hàng trên quy mô nhỏ trước khi quyết định mở rộng.
- Ví dụ can thiệp: nhóm thử nghiệm nhận lời nhắc mua lại theo chu kỳ; nhóm đối chứng tiếp tục nhận cách chăm sóc hiện tại.
- Nhóm đối chứng: nhóm tương tự nhưng không nhận chương trình, dùng để biết điều gì sẽ xảy ra nếu doanh nghiệp không can thiệp.
- Lợi nhuận tăng thêm: phần lợi nhuận của nhóm nhận chương trình cao hơn nhóm đối chứng, sau khi trừ chi phí chương trình.
- Phân ngẫu nhiên: chia khách bằng phương pháp ngẫu nhiên để hai nhóm có thể so sánh công bằng hơn.

Chuyển: "Sau khi xác định cách bảo vệ nguồn doanh số hiện tại, chúng ta chuyển sang các cơ hội tăng trưởng từ sản phẩm và thị trường."
Nguồn: final-report-revised.docx, mục 3.3, 4.5 và 4.6.
-->
