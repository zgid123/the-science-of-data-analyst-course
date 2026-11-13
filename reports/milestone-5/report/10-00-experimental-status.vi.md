# 10. Triển khai thực nghiệm và kết quả

Dự án đã hoàn thành Level 1 (mức bắt buộc), gồm chiến lược mô hình hóa ở Mục 8 và thiết kế đánh giá ở Mục 9. Nhóm cũng đã chạy nguyên mẫu (prototype) Level 2 tự chọn cho AQ3 và AQ4, tức là giao thức đã chốt ở Milestone 4 (Phụ lục
X), được cài đặt bằng Python với polars, scikit-learn và statsmodels thành các bước 19 đến 23 của gói nộp cuối kỳ. Các
mô hình được phát triển trên 9 kỳ mở năm 2013 với các fold loại trừ từng kỳ mở (leave-one-run-out), được chốt bằng mã
băm của từng mô hình đã ước lượng, rồi được kiểm tra một lần duy nhất trên 13 kỳ mở năm 2014 (15.724 lượt đăng ký học
chưa rút tại ngày 27, trong đó 6.911 lượt không hoàn thành học phần). Kế hoạch không quy định thước đo để tinh chỉnh mức
điều chuẩn, nên trong các fold bên trong, nhóm chọn mức điều chuẩn cho log loss nhỏ nhất; lựa chọn này được đưa ra sau khi đã biết kết quả tinh chỉnh theo cả hai thước đo (C18). Các phân tích AQ1 và
AQ2 ở Mục 11 là phân tích mô tả và chẩn đoán, không phải nguyên mẫu này: hai phân tích đó không huấn luyện mô hình dự
báo nào.

**Lựa chọn mô hình.** Trong giai đoạn phát triển, không mô hình đối sánh (challenger) nào vượt được mức chênh lệch đã ấn
định trước: cây tăng cường độ dốc (gradient-boosted trees) và bộ biến dự báo mở rộng chỉ làm tỷ lệ phát hiện chuẩn hóa
(normalised recall) gộp thay đổi từ −0,001 đến −0,002 so với mô hình hồi quy logistic có điều chuẩn (penalised). Do đó,
phương pháp chính của Level 1 được giữ nguyên. Bảng 10.1 trình bày mọi danh sách trên các kỳ mở của tập kiểm thử tại
thiết lập chính.

**Bảng 10.1. Các danh sách 5 trên 20 sinh viên tại ngày 27 trên 13 kỳ mở năm 2014 của tập kiểm thử**

| Danh sách | Số sinh viên không hoàn thành có trong danh sách | Tỷ lệ trên tổng số sinh viên không hoàn thành | Tỷ lệ không hoàn thành trong danh sách |
| :---- | :---- | :---- | :---- |
| Mô hình logistic có điều chuẩn (mô hình chính) | 2.868 | 41,5% | 72,5% |
| Danh sách xếp theo quy tắc dấu hiệu sớm (B2) | 2.786 | 40,3% | 70,4% |
| Mô hình chỉ dùng đặc điểm cá nhân (B3) | 2.244 | 32,5% | 56,7% |
| Danh sách ngẫu nhiên (giá trị kỳ vọng) | 1.738 | 25,1% | 43,9% |

**Điều kiện đạt S1 được đáp ứng.** Tỷ lệ phát hiện chuẩn hóa gộp của mô hình là 0,725, so với 0,704 của danh sách xếp
theo quy tắc dấu hiệu sớm, tức tăng +0,021 (khoảng bootstrap hai tầng, so trên cùng các mẫu lấy lại: +0,006 đến +0,036;
kiểm định hoán vị đổi dấu: p = 0,0035); mô hình dẫn trước ở 11 trong 13 kỳ mở. Mức tăng này có thật nhưng nhỏ: danh sách
của mô hình chỉ có thêm 82 sinh viên không hoàn thành trên 3.955 vị trí, nên riêng quy tắc đã tìm được 97% số sinh viên
mà mô hình tìm được, đúng như Level 1 đã dự liệu rằng một phương pháp cơ sở có thể đạt gần mô hình. Mọi phép kiểm tra độ
nhạy đều cho kết quả cùng chiều (Bảng A.37).

**Hiệu chuẩn và lỗi.** Nguy cơ dự báo gộp đáp ứng điều kiện S3 (hiệu chuẩn tổng thể (calibration-in-the-large) 0,117,
độ dốc hiệu chuẩn 0,886), nhưng chỉ 5 trong 13 kỳ mở đáp ứng điều kiện này khi xét riêng từng kỳ mở, nên cán bộ chỉ thấy
thứ hạng và lý do, không thấy xác suất. Phân tích lỗi chỉ ra một nhóm mà danh sách hầu như bỏ sót: 4.193 trong 6.911
sinh viên không hoàn thành (60,7%) vẫn hoạt động bình thường tại ngày 27 nhưng các danh sách chỉ chứa 19,1% số sinh viên
này. Như vậy, danh sách lập ở tuần 4 chủ yếu xác nhận tình trạng giảm tham gia học tập đã bắt đầu. Quy tắc công bằng FR1
không đánh dấu nhóm nào (Mục 11.4).

**So với kỳ vọng của Level 1.** Nguyên mẫu ủng hộ mọi lựa chọn của Level 1: mô hình chính, các phương pháp cơ sở và điều
kiện đạt duy nhất. Kèm theo đó là hai lưu ý: xác suất vẫn không được hiển thị và mức tăng so với quy tắc đủ nhỏ để quy
tắc là phương án thay thế đáng tin cậy. Một bản cài đặt độc lập của cùng giao thức, là bản nháp ở Milestone 4
của nhóm, cho cùng các kết luận, với số sinh viên không hoàn thành có trong danh sách chênh nhau không quá 4. Các kỳ mở năm 2014 đã được mô tả cho AQ1
và AQ2 trước lần kiểm tra này (C15). Tuy vậy, các biến dự báo, cấu hình ứng viên, quy tắc chọn cấu hình và điều kiện đạt
vẫn giữ nguyên như Milestone 4 đã cố định trên dữ liệu năm 2013, nên lần kiểm tra này vẫn xác nhận một thiết kế
đã cố định từ trước, dù không phải là lần đầu tiên nhóm xem dữ liệu năm 2014. Gói nộp cuối kỳ chạy lại mọi bước từ
dữ liệu đã công bố với một giá trị khởi tạo ngẫu nhiên (seed) duy nhất; các tệp kết quả được đối chiếu đến từng byte.
