# 5. Rủi ro, đạo đức và hạn chế

Thiết kế đánh giá ở Phần 4 đo mức độ hiệu quả của các phương pháp, còn những sai sót có thể phát sinh khi xây dựng và sử dụng các phương pháp này cần được ghi nhận riêng. Đề bài yêu cầu rà soát năm rủi ro: rò rỉ thông tin, quá khớp, kết luận nhân quả quá mức, thiếu công bằng và tự động hóa các quyết định hệ trọng [1]. Nhóm tác giả sắp xếp các rủi ro này theo Khung quản lý rủi ro AI (AI Risk Management Framework) của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST). Khung này có bốn chức năng là quản trị (govern), lập bản đồ (map), đo lường (measure) và quản lý (manage) [39], lần lượt ứng với việc xác định ai chịu trách nhiệm, xác định rủi ro phát sinh ở đâu, kiểm tra biện pháp kiểm soát có hiệu quả hay không và xử lý phần rủi ro còn lại.

**Risk & Ethics Notes.** Bảng 5.1 trình bày Risk & Ethics Notes (ghi chú về rủi ro và đạo đức) theo yêu cầu của đề bài: với mỗi lĩnh vực, bảng nêu rủi ro chính trong dự án này, biện pháp kiểm soát mà bản đề xuất đã xây dựng sẵn và mục trình bày chi tiết.

**Bảng 5.1. Risk & Ethics Notes**

| Lĩnh vực | Rủi ro chính trong dự án | Biện pháp kiểm soát | Mục |
| :---- | :---- | :---- | :---- |
| Rò rỉ thông tin | Thông tin sau thời điểm chốt dữ liệu hoặc từ các kỳ mở thuộc tập kiểm thử lọt vào mô hình | Biến dự báo có ghi ngày; ước lượng lại bên trong từng fold; kiểm tra một lần duy nhất trên tập kiểm thử, có ghi nhật ký | Mục 5.1 |
| Quá khớp và dùng lại tập kiểm thử | Kết quả đánh giá trên các fold cao hơn hiệu năng thực tế; chọn một phương án đánh giá sau khi thấy phương án đó cho kết quả thuận lợi trên tập kiểm thử | Tinh chỉnh lồng nhau; mức chênh lệch ấn định trước; một điều kiện đạt duy nhất được công bố trước | Mục 5.1 |
| Khả năng diễn giải | Lý do hiển thị không khớp với thứ hạng; hiệu ứng riêng phần của một dấu hiệu (chênh lệch khi giữ các dấu hiệu khác như nhau) bị hiểu nhầm là phần đóng góp riêng của dấu hiệu đó | Lý do lấy từ chính mô hình tính điểm rủi ro; ước lượng đã hiệu chỉnh và chưa hiệu chỉnh được trình bày cùng nhau | Mục 5.1 |
| Giới hạn nhân quả | Coi danh sách là bằng chứng cho thấy liên hệ với sinh viên có ích | Không đưa ra nhận định về tác động; chỉ xếp hạng theo lợi ích can thiệp sau một đợt thí điểm ngẫu nhiên hóa | Mục 5.2 |
| Tính công bằng | Tỷ lệ phát hiện thấp hơn ở sinh viên khuyết tật hoặc sinh viên sống ở khu vực khó khăn; biến đại diện (proxy) | Tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm là tiêu chí chính; kiểm định khẳng định; kiểm tra biến đại diện | Mục 5.2 |
| Sử dụng trong bối cảnh hệ trọng | Thiên kiến tự động hóa (automation bias), tức là người dùng làm theo danh sách mà không tự đánh giá; gắn nhãn sinh viên; nghĩa vụ pháp lý của trường đại học | Giảng viên hướng dẫn quyết định và có thể bác bỏ bất kỳ tên nào; dấu cảnh báo hết hiệu lực khi kỳ mở kết thúc; phân loại rủi ro theo luật trí tuệ nhân tạo của Việt Nam trước khi thí điểm | Mục 5.2 |
| Ràng buộc dữ liệu | Chỉ có 9 kỳ mở huấn luyện; module CCC không có trong dữ liệu huấn luyện; dữ liệu đào tạo từ xa tại Vương quốc Anh (UK) giai đoạn 2013–2014 | Chia dữ liệu theo kỳ mở; báo cáo riêng module CCC; đánh giá lại trên dữ liệu của trường trước khi sử dụng | Mục 5.1 |

**Danh mục rủi ro.** Phụ lục V (Bảng A.9) trình bày đầy đủ danh mục gồm mười sáu rủi ro. Mỗi dòng của danh mục nêu nơi rủi ro phát sinh trong dự án này, biện pháp kiểm soát mà bản đề xuất đã xây dựng sẵn, phép kiểm tra cho biết biện pháp đó có hiệu quả hay không và rủi ro còn lại sau khi áp dụng biện pháp.

Mục 5.1 trình bày các rủi ro đối với tính hợp lệ của kết quả đánh giá; Mục 5.2 trình bày các rủi ro khi dùng danh sách cho sinh viên thật.
