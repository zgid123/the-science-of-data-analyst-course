## Phụ lục II – Định nghĩa các chỉ số

Các Evaluation Design Card ở Mục 4.1 dùng các chỉ số định nghĩa trong Bảng A.4; Mục 4.1 giải thích bằng lời các chỉ số chính. Các ký hiệu xét một kỳ mở r có n lượt đăng ký học: Y là tập sinh viên không hoàn thành của kỳ mở đó, b = |Y|/n là tỷ lệ nền và L là danh sách gồm k lượt đăng ký học có điểm rủi ro cao nhất.

**Bảng A.4. Định nghĩa các chỉ số**

| Chỉ số | Định nghĩa | Cách đọc |
| :---- | :---- | :---- |
| Tỷ lệ phát hiện trong giới hạn danh sách | \|L ∩ Y\| / \|Y\| | Tỷ lệ sinh viên không hoàn thành của kỳ mở có trong danh sách |
| Tỷ lệ phát hiện tối đa có thể đạt | min(k, \|Y\|) / \|Y\| | Mức cao nhất mà danh sách dài k có thể đạt |
| Tỷ lệ phát hiện chuẩn hóa | tỷ lệ phát hiện / tỷ lệ phát hiện tối đa có thể đạt | 1 = mức tốt nhất có thể đạt; bằng độ chính xác của danh sách khi \|Y\| ≥ k |
| Tỷ lệ phát hiện chuẩn hóa gộp | Σ\|L ∩ Y\| / Σ min(k, \|Y\|) qua các kỳ mở | Mỗi kỳ mở giữ danh sách và giá trị k riêng |
| Độ chính xác của danh sách dài k | \|L ∩ Y\| / k | Tỷ lệ sinh viên trong danh sách không hoàn thành học phần |
| Mức vượt tỷ lệ nền | độ chính xác của danh sách / b | 1 = ngang ngẫu nhiên; danh sách ngẫu nhiên có tỷ lệ phát hiện kỳ vọng k/n |
| ROC-AUC (trong kỳ mở) | Xác suất để một sinh viên không hoàn thành có điểm rủi ro cao hơn một sinh viên hoàn thành của cùng kỳ mở | Khả năng phân biệt không chịu ảnh hưởng của khác biệt giữa các kỳ mở |
| PR-AUC (trong kỳ mở) | Diện tích dưới đường cong độ chính xác – tỷ lệ phát hiện của một kỳ mở | Đọc so với mức ngẫu nhiên b [24] |
| Hiệu chuẩn tổng thể | Hệ số chặn của mô hình logistic cho biến kết quả, trong đó log-odds của điểm rủi ro được đưa vào làm offset (số hạng có hệ số cố định bằng 1) | Mục tiêu bằng 0 [33] |
| Độ dốc hiệu chuẩn | Hệ số của log-odds của điểm rủi ro trong mô hình logistic hiệu chuẩn lại | Mục tiêu bằng 1; dưới 1 nghĩa là nguy cơ dự báo quá cực đoan [33] |
| Điểm Brier | Trung bình bình phương chênh lệch giữa nguy cơ dự báo và kết quả | Chất lượng tổng thể của xác suất dự báo |
| Lợi ích ròng | số dương tính thật/n − số dương tính giả/n × pt/(1 − pt) tại xác suất ngưỡng pt | Bối cảnh: so với liên hệ tất cả, không liên hệ ai và quy tắc [25] |
| ABROCA | Diện tích tuyệt đối giữa đường ROC của một nhóm và đường ROC của phần còn lại | Chênh lệch khả năng phân biệt không phụ thuộc ngưỡng [34] |
