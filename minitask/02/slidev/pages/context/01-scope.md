---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# Bối cảnh và phạm vi dữ liệu

<div class="lead">541,909 dòng hàng hóa đơn · 01/12/2010 - 09/12/2011</div>
<div class="sales-bridge">
  <div class="bridge-label"><span>Gross sales</span><b>£10,247,219.32</b></div>
  <div class="bridge-bar"><div style="width:95.356%">Net £9.77m</div><span style="width:4.644%"></span></div>
  <div class="bridge-caption"><span>Net £9,771,318.16</span><b>Giá trị hủy £475,901.16</b></div>
</div>
<div class="story-stat-row compact">
<div><strong>19,773</strong><span>hóa đơn mua hợp lệ</span></div>
<div><strong>£518.24</strong><span>Gross AOV (Average Order Value - Giá trị hóa đơn trung bình)</span></div>
<div><strong>£302.20</strong><span>MOV (Median Order Value - Giá trị hóa đơn trung vị)</span></div>
</div>

<!--
Khoảng 60 giây.

Mục tiêu: Giải thích phạm vi dữ liệu, cách đi từ doanh số trước hủy đến doanh số sau hủy, và vì sao cần nhìn cả trung bình lẫn trung vị.

Ghi chú dữ liệu: Mỗi dòng dữ liệu tương ứng với một sản phẩm trong một hóa đơn, không phải toàn bộ hóa đơn. Trước khi tính các chỉ số như doanh số và giá trị trung bình mỗi hóa đơn, nhóm đã loại các dòng bị ghi lặp và những mã chỉ dùng để ghi nhận phí, chiết khấu hoặc điều chỉnh thay vì sản phẩm. Dữ liệu tháng 12/2011 gồm tám ngày đầy đủ và một phần ngày 09/12 nên không thể so sánh trực tiếp với một tháng đầy đủ.

"Bộ dữ liệu có 541.909 dòng, từ ngày 1 tháng 12 năm 2010 đến ngày 9 tháng 12 năm 2011. Một dòng là một mặt hàng trong hóa đơn, không phải một đơn hàng. Nhóm loại 5.268 dòng trùng hoàn toàn, chuẩn hóa mã sản phẩm và tách các mã không đại diện sản phẩm trước khi tính các chỉ số.

Gross sales là doanh số trước khi trừ giao dịch hủy. Sau khi trừ 475.901 bảng giá trị hủy, net sales, tức doanh số sau hủy, còn 9,771 triệu bảng. AOV là giá trị trung bình mỗi hóa đơn; Gross AOV 518 bảng được tính trước khi trừ hủy. Con số này cao hơn trung vị 302 bảng, nghĩa là một nửa số hóa đơn có giá trị dưới 302 bảng. Chênh lệch đó cho thấy một số hóa đơn lớn đang kéo trung bình lên. Tháng 12 năm 2011 chỉ có tám ngày đầy đủ và một phần ngày thứ chín, nên không so trực tiếp với tháng đầy đủ."

Thông điệp chính: Bộ dữ liệu đủ lớn để tìm tín hiệu kinh doanh, nhưng các chỉ số chỉ có ý nghĩa khi dùng đúng phạm vi và đúng định nghĩa.

Chuyển: "Từ phạm vi dữ liệu này, nhóm xác định ba câu hỏi kinh doanh cần trả lời trước khi đề xuất hành động."

Thuật ngữ:
- Dòng hàng: một mặt hàng trong hóa đơn; một hóa đơn có thể gồm nhiều dòng.
- Gross sales: tổng giá trị bán trước khi trừ các giao dịch hủy.
- Giá trị hủy: giá trị của các dòng giao dịch bị hủy, được ghi âm trong dữ liệu.
- Net sales: doanh số còn lại sau khi trừ giá trị hủy; không đồng nghĩa với lợi nhuận.
- AOV (Average Order Value): giá trị trung bình của một hóa đơn. Gross AOV = gross sales / số hóa đơn mua hợp lệ.
- Giá trị hóa đơn trung vị (Median Order Value): mốc ở giữa; 50% hóa đơn có giá trị thấp hơn và 50% cao hơn mốc này.
- KPI: chỉ số dùng để đo lường kết quả hoặc hiệu quả hoạt động.
- Mã phi hàng hóa: mã ghi nhận phí, chiết khấu hoặc điều chỉnh, không đại diện cho một sản phẩm bán ra.
- CustomerID: mã nhận diện khách hàng. Dòng thiếu mã vẫn được tính vào tổng doanh số nhưng không dùng để phân tích theo người mua.

Giải thích chi tiết các con số:
- 541.909 dòng: quy mô tệp nguồn trước khi làm sạch. Tệp có 8 trường. Một dòng là một mặt hàng trong hóa đơn, vì vậy số dòng lớn hơn nhiều số hóa đơn.
- 5.268 dòng trùng: các dòng giống nhau hoàn toàn trên cả 8 trường gốc. Tỷ lệ là 5.268 / 541.909 = 0,97%. Sau bước này còn 536.641 dòng.
- 135.037 dòng thiếu CustomerID: bằng 135.037 / 536.641 = 25,16% số dòng sau loại trùng. Các dòng này vẫn được giữ khi tính doanh số tổng thể.
- 533.697 dòng: số dòng còn lại sau khi chuẩn hóa StockCode và loại các mã phi hàng hóa như POST, DOT, M và BANK CHARGES.
- 522.537 dòng mua hợp lệ: Quantity > 0, UnitPrice > 0 và InvoiceNo không bắt đầu bằng C.
- 19.773 hóa đơn mua hợp lệ: số InvoiceNo khác nhau trong 522.537 dòng mua. Đây là mẫu số của Gross AOV và phân tích giỏ hàng.
- 8.668 dòng hủy hợp lệ: InvoiceNo bắt đầu bằng C, Quantity < 0 và UnitPrice > 0.
- 2.492 dòng điều chỉnh khác: không thỏa điều kiện mua hoặc hủy, nên được tách khỏi KPI thay vì coi mọi dòng âm là trả hàng.
- £10.247.219,32 gross sales: tổng Quantity × UnitPrice của các dòng mua hợp lệ.
- £475.901,16 giá trị hủy: trị tuyệt đối của tổng Quantity × UnitPrice trên các dòng hủy hợp lệ.
- £9.771.318,16 net sales: £10.247.219,32 - £475.901,16. Phép đối soát này phải khớp khi tổng hợp theo tháng, quốc gia và tình trạng CustomerID.
- 4,64% giá trị hủy trên gross: £475.901,16 / £10.247.219,32 = 4,6442%, làm tròn thành 4,64%.
- £518,24 Gross AOV: £10.247.219,32 / 19.773 = £518,243, làm tròn thành £518,24.
- £302,20 trung vị hóa đơn: sau khi cộng giá trị các dòng theo từng InvoiceNo, sắp xếp 19.773 giá trị hóa đơn và lấy mốc giữa. Đây không phải £9.771.318,16 / 19.773 và không phải lợi nhuận.
- Khoảng thời gian 01/12/2010 - 09/12/2011: dữ liệu kết thúc lúc 12:50 ngày 09/12/2011. Vì vậy tháng 12/2011 là tháng chưa đầy đủ.

Q&A: CustomerID là mã nhận diện khách hàng. Dòng thiếu mã vẫn được giữ khi tính tổng doanh số, nhưng không dùng trong phân tích theo người mua. Net sales chưa phải lợi nhuận hay doanh thu kế toán đã kiểm toán.
Nguồn: final-report-revised.docx, mục 2.1-2.3 và 4.1, Bảng 2-4, 7.
-->
