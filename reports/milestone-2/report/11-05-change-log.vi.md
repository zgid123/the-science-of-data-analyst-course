## Phụ lục V – Nhật ký thay đổi có kiểm soát và ma trận truy vết đầy đủ

Nhóm phân tích dữ liệu chốt phiên bản cơ sở của Milestone 1 trước khi tìm kiếm bộ dữ liệu. Bảng A.8 liệt kê các tệp của bản đề xuất đã được sao chép vào phiên bản cơ sở, kèm giá trị SHA-256 của từng tệp, nhờ đó mọi chỉnh sửa về sau trên các tệp này đều có thể bị phát hiện. Bảng A.9 ghi lại mọi thay đổi so với phiên bản cơ sở, kèm bằng chứng dữ liệu, theo mẫu ở mục 3.1 của đề bài.

**Bảng A.8. Các tệp Milestone 1 đã chốt**

| Tệp | SHA-256 |
| :---- | :---- |
| 03-01-business-goal.md | f99753ab586754e3c6f416c34b669db647d93dc20920db59fb964c3aef0bab23 |
| 03-02-smart-goal.md | d7b32a609f5b39a24630713b3ca631dca9328404e18a42e0737fa8311caa6087 |
| 03-03-kpis.md | 7698548222c8f9431f16f36bb0a7f6ec5de11221e15b645f8f4d3f5391b8710a |
| 04-01-four-level-questions.md | 300389d938bb7457192bf10790fffa432849c67460df2df379add184c9a05993 |
| 05-00-analytic-approach.md | 98a36dc7d86271d00cd5e5432164e547e7d945f28880e3811c80d35e13439753 |
| 06-01-data-requirements.md | 07d212a4cbaa800221a699bf91db387e7f27e59cac53522108bca7ad06293cf1 |
| 07-00-decision-value.md | 19086def5d5cabde135c1ecd68e6d6223170d6908b3a0d9f068dd8fe65870e68 |
| 09-00-traceability-matrix.md | d74c013921ccb95da9511facaf04b781499012a061d5cb71ae4724e5ec1cdd2d |

Với mỗi thay đổi, Bảng A.9 nêu nội dung cũ, nội dung mới, bằng chứng dữ liệu và tác động đến các AQ, KPI và quyết định.

**Bảng A.9. Nhật ký thay đổi có kiểm soát**

| ID | Nội dung cũ (Milestone 1) | Nội dung mới | Lý do (bằng chứng dữ liệu) | Tác động đến AQ / KPI / quyết định |
| :---- | :---- | :---- | :---- | :---- |
| C01 | Các học phần trực tuyến và học phần kết hợp của chương trình đào tạo tại một trường đại học Việt Nam | Các kỳ mở module của OULAD (Open University, UK, đào tạo từ xa, 2013–2014) là bộ dữ liệu mở thay thế để phân tích; đợt thí điểm vẫn dùng dữ liệu của chính trường | Nhóm không tìm thấy bộ dữ liệu mở nào về các học phần ở Việt Nam; OULAD là ứng viên duy nhất đạt các điều kiện bắt buộc | Mọi AQ được trả lời trên bộ dữ liệu thay thế. Kết quả chỉ mô tả OULAD và phải được kiểm tra lại trên dữ liệu của trường trước khi đưa ra các quyết định D1–D3 |
| C02 | Học phần và học kỳ; tuần 1–5 của học kỳ (Milestone 1 chưa cố định độ dài học kỳ) | Kỳ mở module (`code_presentation`), dài tám đến chín tháng; ngày được đếm từ ngày 0 của kỳ mở; tuần n gồm các ngày từ 7(n−1) đến 7n−1 | Ngày trong OULAD là số ngày tính từ ngày bắt đầu kỳ mở; các kỳ mở kéo dài 234–269 ngày | Thời điểm dự báo là ngày 13 cho danh sách tuần 3 và ngày 27 cho danh sách tuần 5; chênh lệch về độ dài học kỳ được nêu rõ là một hạn chế |
| C03 | Mẫu số: sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần; thôi học theo Thông tư 83/2026 | Các lượt đăng ký học còn hiệu lực tại ngày 14 (thời hạn đăng ký kết thúc hai tuần sau ngày bắt đầu); không phân biệt được tạm ngừng học với chuyển chương trình đào tạo | Có `date_registration` và `date_unregistration`; không có cột nào ghi tình trạng tạm ngừng học hoặc chuyển chương trình đào tạo | KPI chính chỉ là chỉ số đại diện (proxy), tính trên 28.119 lượt đăng ký học; điểm khác so với quy định của Thông tư 83 được ghi nhận |
| C04 | So sánh theo hình thức học và năm theo học; giới hạn của AQ4 về chênh lệch tỷ lệ phát hiện (recall) giữa sinh viên năm nhất và sinh viên các năm trên | So sánh theo module và kỳ mở; giới hạn về tính công bằng được kiểm tra theo mức khó khăn kinh tế – xã hội của khu vực cư trú và tình trạng khuyết tật | Không có cột hình thức học hoặc năm theo học; mọi module đều theo hình thức đào tạo từ xa | Phạm vi của AQ1–AQ3 được thu hẹp; giới hạn của AQ4 được diễn đạt lại theo các nhóm có trong dữ liệu |
| C05 | Dấu hiệu của AQ2: chuyên cần ở các buổi học trên lớp (học phần kết hợp) | Bỏ dấu hiệu này | OULAD không có buổi học trên lớp và không có dữ liệu chuyên cần | AQ2 dùng bài bị bỏ lỡ, bài nộp trễ, mức hoạt động và các kỳ mở mà sinh viên học cùng lúc |
| C06 | Danh sách tuần 3 của AQ3 dựa trên dấu hiệu về bài được chấm điểm và dấu hiệu về hoạt động | Danh sách tuần 3 (thời điểm dự báo là ngày 13) chỉ dựa trên hoạt động; dấu hiệu về bài được chấm điểm bắt đầu được dùng từ danh sách tuần 5 | 1 trong 22 kỳ mở có bài không phải bài thi đến hạn tính đến hết ngày 13; tính đến hết ngày 27 là 16 kỳ mở | KPI phụ 1: chỉ 1 trong 22 kỳ mở có hai bài được chấm điểm đến hạn tính đến hết ngày 27, nên trên OULAD, phần dấu hiệu của KPI này tính một bài bị bỏ lỡ hoặc nộp trễ ở 16 kỳ mở có bài đến hạn tính đến hết ngày 27; quy tắc hai bài vẫn được giữ cho dữ liệu của trường |
| C07 | AQ3 được đánh giá trên một học kỳ sau của chính các học phần thí điểm | Huấn luyện trên các kỳ mở năm 2013, đánh giá trên các kỳ mở năm 2014 của cùng module và cùng tháng bắt đầu (9 cặp kỳ mở); CCC, EEE-B và GGG-B chỉ dùng làm kỳ mở muộn hơn để đánh giá | Các kỳ mở tháng 2 (B) và tháng 10 (J) nên được phân tích riêng; mỗi module có nhiều nhất hai kỳ mở cùng tháng bắt đầu | Đánh giá trên kỳ mở muộn hơn (huấn luyện trên các kỳ mở sớm hơn) là khả thi, nhưng mỗi cặp chỉ có một kỳ mở sớm hơn |
| C08 | Hành động và kết quả của AQ4; KPI phụ 2 và phần liên hệ của KPI phụ 1 được đo từ sổ theo dõi liên hệ | Vẫn là yêu cầu cho quyết định trong tương lai; AQ4 chỉ còn phần xếp hạng, với giả định về số sinh viên cán bộ liên hệ được mỗi tuần | Không ứng viên nào có dữ liệu về liên hệ, về số sinh viên cán bộ liên hệ được mỗi tuần hoặc về can thiệp | Báo cáo không đưa ra nhận định mang tính chỉ định hoặc nhân quả; phần liên hệ của KPI phụ 1 và KPI phụ 2 chỉ được đo trong đợt thí điểm |

Bảng A.10 là ma trận truy vết đầy đủ theo yêu cầu của đề bài (sản phẩm bàn giao B). Mọi dòng của ma trận đều phục vụ Business Goal: nâng tỷ lệ hoàn thành học phần bằng cách nhận ra đủ sớm những sinh viên đang giảm tham gia học tập để kịp hỗ trợ trong học kỳ. Mỗi dòng liên kết KPI, câu hỏi, yêu cầu dữ liệu, tệp, biến thực tế, mức đáp ứng và quyết định tương ứng.

**Bảng A.10. Truy vết đầy đủ từ mục tiêu đến quyết định, kèm mức đáp ứng**

| Business Goal / SMART Goal / KPI | AQ | Loại phân tích | Yêu cầu dữ liệu | Bộ dữ liệu / tệp | Biến thực tế | Mức đáp ứng | Quyết định được hỗ trợ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Tỷ lệ hoàn thành học phần ở các học phần thí điểm, theo giả định tăng từ mức cơ sở 70% lên mức mục tiêu 75% đến cuối năm học 2027–2028 (KPI chính) | AQ1 | Mô tả | Kết quả theo học phần và theo thời gian; bài bị bỏ lỡ đầu tiên | studentInfo, studentRegistration, assessments, studentAssessment | final_result, date_unregistration, assessments.date, date_submitted | Một phần | D2, D3 |
| KPI chính; KPI phụ 1, tỷ lệ liên hệ sinh viên có dấu hiệu sớm (phần dấu hiệu) | AQ2 | Chẩn đoán | Dấu hiệu trong tuần 1–4, đối chiếu với kết quả về sau | + studentVle, vle | sum_click, studentVle.date, date_submitted | Một phần | D2; lý do cụ thể trong D1 |
| KPI phụ 1 (phần dấu hiệu) | AQ3 | Dự báo | Biến cần dự đoán và các đặc trưng tính đến hết thời điểm dự báo; kỳ mở muộn hơn để đánh giá | như AQ2 | như AQ2 + num_of_prev_attempts, studied_credits, imd_band, disability | Một phần | D1 |
| KPI phụ 2, tỷ lệ liên hệ kịp thời; KPI phụ 1 (phần liên hệ) | AQ4 | Chỉ định | Xếp hạng trong giới hạn số sinh viên cán bộ liên hệ được mỗi tuần; sổ theo dõi liên hệ | Kết quả của AQ3 | không có biến về liên hệ | Một phần / Không đáp ứng | D1 |
