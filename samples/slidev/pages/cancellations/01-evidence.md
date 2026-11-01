---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# P1 · Hai giao dịch tạo hai đỉnh hủy

<BriefEvidence kind="p1" />
<div class="takeaway compact-takeaway">Hai cặp đảo ngược trong 12-16 phút chiếm 51.62% giá trị hủy.</div>
<div class="note">Phân tích độ nhạy: net giữ nguyên £9,771,318.16. Chưa xác nhận nguyên nhân đảo ngược.</div>

<!--
Khoảng 70 giây.

Mục tiêu: Giúp người nghe hiểu rằng tỷ lệ hủy 4,64% bị ảnh hưởng rất lớn bởi chỉ hai trường hợp đặc biệt.

"Slide này trả lời câu hỏi: tỷ lệ hủy 4,64% có phải là vấn đề xảy ra phổ biến, hay con số đó đang bị kéo lên bởi một vài giao dịch rất lớn?

Trước tiên, nhìn vào biểu đồ bên trái. Hai cột màu cam ở tháng 1 và tháng 12 cao hơn hẳn các tháng còn lại. Tuy nhiên, đây chưa phải bằng chứng cho thấy hủy đơn tăng theo mùa. Mỗi đỉnh chủ yếu đến từ một đơn mua rất lớn, sau đó có một giao dịch hủy với giá trị âm tương ứng. Nói đơn giản, hệ thống ghi nhận đơn mua rồi ghi thêm một giao dịch để hủy đơn đó.

Cụ thể, đơn của khách 12346 trị giá 77.184 bảng bị hủy sau 16 phút. Đơn của khách 16446 trị giá 168.470 bảng bị hủy sau 12 phút. Chỉ hai trường hợp này đã chiếm 51,62% tổng giá trị hủy của cả kỳ.

Phần bên phải cho thấy ảnh hưởng của chúng. Khi tính trên toàn bộ dữ liệu, tỷ lệ hủy là 4,64%. Nếu thử tính lại bằng cách loại đồng thời cả đơn mua và đơn hủy của hai trường hợp đặc biệt, tỷ lệ còn khoảng 2,30%. Phải loại cả hai phía để phép so sánh công bằng; vì vậy doanh số sau hủy vẫn giữ nguyên ở 9,77 triệu bảng.

Điều này không có nghĩa doanh nghiệp đã giảm được hủy đơn. Nó chỉ cho thấy chỉ số 4,64% đang bị hai giao dịch lớn chi phối. Dữ liệu không ghi lý do hủy, nên chúng ta chưa thể kết luận đây là lỗi nhập liệu, khách đổi ý hay vấn đề vận hành."

Giải thích khi được hỏi:
- 13 cột theo tháng: từ 12/2010 đến 12/2011. Giá trị hủy lần lượt là £17.547,86; £91.525,05; £8.335,52; £10.504,30; £33.316,06; £8.948,23; £13.713,84; £11.407,26; £22.926,57; £16.980,64; £41.613,03; £24.991,44 và £174.091,36.
- Dấu * ở 12/2011: dữ liệu tháng này chỉ đến 12:50 ngày 09/12, nên cột £174.091,36 không thể so trực tiếp với một tháng đầy đủ.
- 4,64%: £475.901,16 tổng giá trị hủy / £10.247.219,32 gross sales = 4,6442%, làm tròn thành 4,64%.
- Khách 12346, SKU 23166: mua lúc 10:01 và hủy lúc 10:17 ngày 18/01/2011. Chênh lệch 16 phút, giá trị £77.183,60.
- Khách 16446, SKU 23843: mua lúc 09:15 và hủy lúc 09:27 ngày 09/12/2011. Chênh lệch 12 phút, giá trị £168.469,60.
- £245.653,20: £77.183,60 + £168.469,60.
- 51,62%: £245.653,20 / £475.901,16 = 51,6185%, làm tròn thành 51,62%.
- £230.247,96 giá trị hủy điều chỉnh: £475.901,16 - £245.653,20.
- £10.001.566,12 gross điều chỉnh: £10.247.219,32 - £245.653,20. Nhóm loại cả phần mua và phần hủy để tử số và mẫu số dùng cùng phạm vi.
- 2,30%: £230.247,96 / £10.001.566,12 = 2,3021%, làm tròn thành 2,30%.
- £9.771.318,16 net không đổi: trước điều chỉnh là gross - hủy. Sau điều chỉnh, cùng một giá trị £245.653,20 được trừ khỏi cả gross và hủy nên hiệu số không thay đổi.
- Giao dịch hủy có giá trị âm: một bản ghi được dùng để triệt tiêu giá trị của đơn mua trước đó.
- Phân tích độ nhạy: thử tính lại chỉ số khi thay đổi một giả định hoặc loại một trường hợp đặc biệt để xem kết quả thay đổi bao nhiêu.
- Net sales giữ nguyên: vì cả đơn mua và đơn hủy tương ứng đều được loại khỏi phép tính; hai giá trị vốn triệt tiêu nhau.
- Giới hạn: 2,30% là kết quả phân tích độ nhạy, không phải xác suất khách trả hàng và không phải mức hủy doanh nghiệp đã đạt được sau cải tiến.

Chuyển: "Vì chưa biết lý do của hai đơn hủy lớn này, bước tiếp theo là bổ sung dữ liệu và chuẩn hóa cách theo dõi trước khi đặt mục tiêu giảm hủy."
Nguồn: final-report-revised.docx, mục 4.2, Bảng 8-9 và Hình 2.
-->
