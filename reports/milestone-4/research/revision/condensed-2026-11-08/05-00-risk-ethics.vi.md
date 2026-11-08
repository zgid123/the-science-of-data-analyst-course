# 5. Rủi ro, đạo đức và hạn chế

Thiết kế đánh giá ở Phần 4 đo mức độ hiệu quả của các phương pháp; những sai sót có thể xảy ra khi xây dựng và sử dụng các phương pháp này cần được ghi nhận riêng. Các rủi ro được sắp xếp theo Khung quản lý rủi ro AI của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST), gồm bốn chức năng: quản trị (govern), lập bản đồ (map), đo lường (measure) và quản lý (manage) [38]. Bên cạnh đó, đề bài nêu năm rủi ro cần rà soát: rò rỉ thông tin, quá khớp, kết luận nhân quả quá mức, thiếu công bằng và tự động hóa các quyết định hệ trọng [1]. Bảng 5.1 trình bày Risk and Ethics Notes (ghi chú về rủi ro và đạo đức). Danh mục rủi ro đầy đủ gồm mười sáu rủi ro, mỗi rủi ro kèm biện pháp kiểm soát, cách kiểm tra và mức rủi ro còn lại (Phụ lục VI, Bảng A.17).

**Bảng 5.1. Risk and Ethics Notes**

| Lĩnh vực | Rủi ro chính trong dự án | Biện pháp kiểm soát | Mục |
| :---- | :---- | :---- | :---- |
| Rò rỉ thông tin | Thông tin sau thời điểm chốt dữ liệu hoặc từ các kỳ mở kiểm thử lọt vào mô hình | Biến dự báo có ghi ngày; ước lượng lại bên trong từng fold; kiểm thử một lần duy nhất, có ghi nhật ký | Mục 5.1 |
| Quá khớp và dùng lại tập kiểm thử | Điểm đánh giá trên các fold lạc quan quá mức; sau khi xem kết quả, người phân tích chọn phương án kiểm thử cho kết quả tốt nhất | Tinh chỉnh lồng nhau; mức chênh lệch tối thiểu chốt trước; một điều kiện đạt duy nhất được công bố trước | Mục 5.1 |
| Khả năng diễn giải | Lý do hiển thị cho giảng viên hướng dẫn không khớp với thứ hạng; người đọc hiểu tác động riêng phần của một dấu hiệu như trọng số riêng của dấu hiệu đó | Lý do lấy từ chính mô hình chấm điểm; trình bày ước lượng đã hiệu chỉnh cùng ước lượng chưa hiệu chỉnh | Mục 5.1 |
| Giới hạn về nhân quả | Hiểu danh sách như bằng chứng rằng liên hệ có ích | Không đưa ra nhận định về tác động; chỉ xếp hạng theo lợi ích can thiệp sau khi đã có một đợt thí điểm ngẫu nhiên hóa | Mục 5.2 |
| Tính công bằng | Tỷ lệ phát hiện thấp hơn ở sinh viên khuyết tật hoặc sinh viên ở khu vực khó khăn; biến thay thế | Tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation) làm tiêu chí chính; kiểm định khẳng định; kiểm tra biến thay thế (proxy) | Mục 5.2 |
| Sử dụng trong bối cảnh hệ trọng | Thiên kiến tự động hóa (automation bias): người dùng làm theo danh sách mà không tự đánh giá; gắn nhãn sinh viên; nghĩa vụ pháp lý của trường đại học | Giảng viên hướng dẫn quyết định và có thể bác bỏ bất kỳ tên nào trong danh sách; việc đánh dấu một sinh viên hết hiệu lực khi kỳ mở kết thúc; phân loại rủi ro theo luật AI của Việt Nam trước khi thí điểm | Mục 5.2 |
| Ràng buộc dữ liệu | Chỉ có 9 kỳ mở huấn luyện; module CCC không có trong dữ liệu huấn luyện; đào tạo từ xa tại Anh giai đoạn 2013–2014 | Chia dữ liệu theo kỳ mở; báo cáo riêng module CCC; kiểm định trên dữ liệu của trường trước khi sử dụng | Mục 5.1 |
