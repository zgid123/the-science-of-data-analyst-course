---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# P2 · 10.01% người mua tạo 60.21% net có ID

<BriefEvidence kind="p2" />
<div class="note">Mẫu số: £8,269,399.91 của 4,334 người mua có ID. 15.41% net toàn kỳ thiếu CustomerID; phân nhóm chưa phải RFM hay B2B/B2C.</div>

<!--
Khoảng 70 giây.

Mục tiêu: Giải thích mức độ tập trung doanh số mà không nhầm nó với việc khách hàng đang rời bỏ.

"Slide này trả lời câu hỏi: doanh số có đang phụ thuộc quá nhiều vào một nhóm khách hàng nhỏ hay không?

Nhìn vào biểu đồ bên trái, dữ liệu có 4.334 người mua có mã nhận diện. Con số 434 được xác định bằng cách lấy 10% của 4.334, tức 433,4 người, rồi làm tròn lên để không bỏ dở một khách. Nhóm xếp 4.334 người mua theo doanh số sau hủy từ cao xuống thấp và chọn 434 người đứng đầu. Nếu hai người có cùng doanh số, nhóm xếp CustomerID tăng dần để kết quả có thể tái lập.

Nhóm 434 người này chiếm 10,01% số người mua có ID, nhưng tạo ra 60,21% doanh số sau hủy của quần thể đó. Trong khi đó, 3.900 người còn lại, tương đương gần 90% số người mua, chỉ tạo khoảng 39,79% doanh số.

Điều này cho thấy doanh nghiệp phụ thuộc đáng kể vào một nhóm khách hàng lớn. Nếu một vài khách lớn giảm mua, tổng doanh số có thể bị ảnh hưởng mạnh.

Phần bên phải mô tả thay đổi từ tháng 1 đến tháng 11. Số người mua hoạt động tăng từ 739 lên 1.660 và số hóa đơn trung bình trên mỗi người tăng từ 1,33 lên 1,59. Tuy nhiên, doanh số trước hủy trên mỗi người hoạt động giảm từ 761 xuống 685 bảng.

Chúng ta không nên kết luận rằng từng khách đang chi tiêu ít đi, vì nhóm khách xuất hiện ở mỗi tháng không hoàn toàn giống nhau. Slide này chỉ chứng minh mức độ tập trung doanh số; nó chưa chứng minh 434 khách lớn đang rời bỏ."

Cách giải thích phần bên phải, từ trên xuống:
- Giai đoạn so sánh là tháng 1/2011 với tháng 11/2011.
- "Người mua có ID: 739 → 1.660, tăng 124,6%" nghĩa là số khách có mã nhận diện và phát sinh ít nhất một hóa đơn trong tháng 11 cao hơn tháng 1. Đây là số khách hoạt động trong từng tháng, không nhất thiết là khách mới.
- "Hóa đơn/người mua: 1,33 → 1,59, tăng 19,5%" nghĩa là mỗi khách hoạt động tạo trung bình 1,33 hóa đơn trong tháng 1 và 1,59 hóa đơn trong tháng 11. Đây là tần suất mua trung bình trong tháng.
- "Gross/người mua hoạt động: £761 → £685, giảm 10,1%" nghĩa là doanh số trước hủy trung bình trên mỗi khách hoạt động thấp hơn vào tháng 11. Đây là doanh số, không phải lợi nhuận.
- Ba dòng trên không theo dõi cùng một nhóm khách cố định. Khách của tháng 1 và tháng 11 có thể khác nhau, nên chưa thể kết luận một khách cụ thể mua thường xuyên hơn nhưng chi ít tiền hơn.
- Dòng "chưa phải cohort" nhắc rằng muốn đo sự thay đổi hành vi của cùng một nhóm khách, doanh nghiệp phải chọn một nhóm khách cố định rồi theo dõi chính nhóm đó qua nhiều tháng.

Giải thích chi tiết các phép tính:
- 4.334 người mua có ID: CustomerID có ít nhất một hóa đơn mua hợp lệ. Đây là quần thể dùng để xếp hạng chi tiêu.
- 28 khách chỉ có bản ghi hủy: có CustomerID nhưng không có hóa đơn mua hợp lệ. Họ được dùng để đối soát net sales, nhưng không nằm trong quần thể người mua để chăm sóc.
- 4.362 khách có ID: 4.334 người mua + 28 khách chỉ có hủy. Không dùng con số này làm mẫu số của nhóm top 10%.
- 434 người dẫn đầu: ceil(10% × 4.334) = ceil(433,4) = 434.
- 10,01%: 434 / 4.334 = 10,0138%, làm tròn thành 10,01%.
- 3.900 người còn lại: 4.334 - 434 = 3.900.
- 89,99%: 3.900 / 4.334 = 89,9862%, làm tròn thành 89,99%.
- £8.269.399,91: tổng net sales của 4.334 người mua có ID. Đây là mẫu số cho tỷ trọng 60,21% và 39,79%.
- 60,21% và 39,79%: hai tỷ trọng net sales của nhóm 434 và nhóm 3.900 trong £8.269.399,91. Hai tỷ trọng cộng thành 100% sau làm tròn.
- £1.505.841,23 thiếu CustomerID: bằng 15,4108% của £9.771.318,16 net sales toàn kỳ, làm tròn thành 15,41%.
- 25,16% và 15,41% dùng mẫu số khác nhau: 25,16% là tỷ lệ dòng thiếu CustomerID sau loại trùng, còn 15,41% là tỷ lệ net sales thiếu CustomerID.
- 739 và 1.660: số người mua có ID hoạt động trong tháng 01/2011 và 11/2011. Một người có thể xuất hiện ở cả hai tháng.
- 124,6%: (1.660 / 739 - 1) × 100 = 124,63%, làm tròn thành 124,6%.
- 1,33 và 1,59 hóa đơn/người: số hóa đơn mua trong tháng chia số người mua có ID hoạt động trong tháng.
- 19,5%: (1,59 / 1,33 - 1) × 100 = 19,55%, làm tròn thành 19,5%.
- £761,41 và £684,66 gross/người hoạt động: gross sales trong tháng chia số người mua có ID hoạt động của tháng đó.
- -10,1%: (£684,66 / £761,41 - 1) × 100 = -10,08%, làm tròn thành -10,1%.

Giới hạn cần nói rõ: 15,41% doanh số sau hủy không có CustomerID. Vì vậy, kết luận về mức độ tập trung chỉ áp dụng cho phần doanh số có thể xác định người mua.

Giải thích khi được hỏi:
- Khách có ID: khách có mã CustomerID để nhóm các hóa đơn thuộc cùng một người mua.
- Vì sao là 434 người: 10% × 4.334 = 433,4. Nhóm làm tròn lên thành 434 người, rồi chọn theo net sales giảm dần.
- Vì sao không dùng 4.362 khách có ID: 4.362 gồm 4.334 người mua và 28 khách chỉ có bản ghi hủy. Phân nhóm này nhằm chọn người mua để chăm sóc, nên mẫu số là 4.334.
- Net sales có ID: doanh số sau hủy chỉ của các giao dịch có CustomerID.
- Người mua hoạt động: khách có ít nhất một hóa đơn trong tháng đó.
- Cohort: một nhóm khách cố định được theo dõi qua thời gian. Biểu đồ này chưa phải phân tích cohort vì tập khách thay đổi theo tháng.
- RFM (Recency, Frequency, Monetary Value): cách phân nhóm khách theo thời gian kể từ lần mua gần nhất, tần suất mua và tổng giá trị mua; slide này mới chỉ xếp hạng theo doanh số nên chưa phải phân tích RFM đầy đủ.
- B2B/B2C: bán cho doanh nghiệp và bán cho người tiêu dùng cá nhân. Dữ liệu chưa cho biết chắc mỗi CustomerID thuộc loại nào.

Chuyển: "Vì doanh số tập trung vào một nhóm nhỏ, doanh nghiệp cần hiểu rõ từng tài khoản và kiểm chứng cách chăm sóc trước khi triển khai ưu đãi rộng."

Q&A đối soát: £8.269.399,91 của người mua có ID - £3.922,98 của 28 khách chỉ có hủy + £1.505.841,23 của giao dịch thiếu ID = £9.771.318,16 net sales toàn kỳ.
Nguồn: final-report-revised.docx, mục 4.5, Bảng 15, Hình 5-6.
-->
