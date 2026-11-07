# 5. Thu thập dữ liệu và nguồn gốc dữ liệu

**Nguyên tắc.** Đề bài yêu cầu dữ liệu gốc được giữ nguyên như khi công bố và bất kỳ ai cũng có thể lặp lại quá trình thu thập [1]. Vì vậy, nhóm thu thập bộ dữ liệu đã chọn bằng một script tải các tệp đã công bố, kiểm tra và lưu các tệp đó nguyên trạng, đồng thời ghi lại mọi thông tin cần thiết để lấy lại các tệp. Hai loại bằng chứng giúp người khác kiểm tra được bản sao này. Mã kiểm tra (checksum) là một chuỗi ngắn được tính từ chính xác các byte của tệp; chỉ cần một byte thay đổi, mã kiểm tra cũng thay đổi. Nhóm ghi hai mã kiểm tra cho mỗi tệp: SHA-256 (Secure Hash Algorithm, 256-bit) là chuẩn dùng để đối chiếu, còn MD5 (Message Digest 5) là mã kiểm tra do chính nhà cung cấp công bố. Các tệp được lưu ở định dạng CSV (comma-separated values), tức là bảng dạng văn bản thuần mà công cụ nào cũng đọc được. Bảng 5.1 là kế hoạch thu thập dữ liệu OULAD theo mẫu của đề bài.

**Bảng 5.1. Kế hoạch thu thập dữ liệu OULAD**

| Hạng mục | Giá trị |
| :---- | :---- |
| Tên bộ dữ liệu | Open University Learning Analytics Dataset (tên chính thức) |
| Nhà cung cấp / tác giả | J. Kuzilek, M. Hlosta và Z. Zdrahal, Knowledge Media Institute, The Open University [3] |
| URL chính thức / DOI | Trang của nhà cung cấp [2]; bài mô tả dữ liệu doi:10.1038/sdata.2017.171 [3]; tệp lưu trên figshare, doi:10.6084/m9.figshare.5081998.v1 [3] |
| Ngày truy cập | 06/11/2026 (giờ Việt Nam, UTC+7) |
| Phiên bản / bản phát hành | figshare phiên bản 1; trang của nhà cung cấp đăng phiên bản mới nhất nhưng không ghi số phiên bản [2] |
| Giấy phép / điều khoản | CC BY 4.0 [2], [12] |
| Phương thức thu thập | Tải trực tiếp một tệp nén zip từ bản lưu trên figshare; đối chiếu kích thước và mã SHA-256 với giá trị tham chiếu ghi sẵn trong script thu thập; giải nén bảy bảng, giữ nguyên nội dung |
| Tệp gốc | anonymisedData.zip (46.750.706 byte), gồm courses, assessments, vle, studentInfo, studentRegistration, studentAssessment và studentVle (CSV; riêng studentVle là 453,8 MB) |
| Bằng chứng về tính toàn vẹn | Mã SHA-256 và MD5 của tệp nén và của từng bảng được ghi trong manifest, tức là danh sách các tệp kèm mã kiểm tra; cả bảy bảng đều khớp giá trị SHA-256 tham chiếu ghi sẵn |
| Trích dẫn | Kuzilek, Hlosta và Zdrahal (2017), *Scientific Data*, 4, 170171 [3] |

**Bản dữ liệu được chọn và lý do.** OULAD được phát hành ở ba nơi: máy chủ riêng của nhà cung cấp, với đường dẫn bị lỗi vào lúc thu thập dữ liệu [2]; bản lưu trên figshare có DOI và số phiên bản, được bài mô tả dữ liệu trích dẫn [3]; và Kho dữ liệu học máy UCI [12]. Nhóm thu thập và trích dẫn bản lưu trên figshare. Khi so sánh từng dòng, nhóm thấy bản của UCI giống hệt bản này, chỉ khác ở cách ghi giá trị thiếu (Phụ lục III).

**Tái lập bằng hai lệnh.** Bất kỳ ai có gói thu thập dữ liệu đều có thể tạo lại bản sao của nhóm bằng hai lệnh. Lệnh thứ nhất (`src/collect.py`) tải tệp nén, kiểm tra kích thước và mã kiểm tra rồi giải nén bảy bảng. Lệnh thứ hai (`src/verify_structure.py`) chạy các bước kiểm tra cấu trúc ban đầu ở Mục 6. Ngoài ra, gói thu thập dữ liệu còn chứa manifest các mã kiểm tra, từ điển dữ liệu sao chép từ bài mô tả dữ liệu, bảng nguồn và giấy phép, thông tin trích dẫn và nhật ký thu thập. Các tệp gốc được giữ nguyên như khi công bố: nhóm không làm sạch, không lọc và không chuyển đổi tệp nào. Phụ lục III trình bày cấu trúc thư mục của gói cùng các bảng nguồn, giấy phép và manifest.
