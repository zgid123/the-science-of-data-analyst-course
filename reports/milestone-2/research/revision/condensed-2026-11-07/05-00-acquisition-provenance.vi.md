# 5. Thu thập dữ liệu và nguồn gốc dữ liệu

Nhóm phân tích dữ liệu thu thập bộ dữ liệu đã chọn bằng một script giữ nguyên các tệp đã công bố và ghi lại cách lấy lại các tệp đó, đúng như đề bài yêu cầu [1]. Các nguồn được xác định bằng DOI, còn các tệp được lưu ở định dạng CSV (comma-separated values). Tính toàn vẹn của tệp được kiểm tra bằng hai loại mã kiểm tra (checksum): SHA-256 (Secure Hash Algorithm, 256-bit) và MD5 (Message Digest 5). Bảng 5.1 trình bày kế hoạch thu thập dữ liệu; Phụ lục III mô tả đầy đủ gói thu thập dữ liệu.

**Bảng 5.1. Kế hoạch thu thập dữ liệu OULAD**

| Hạng mục | Giá trị |
| :---- | :---- |
| Tên bộ dữ liệu | Open University Learning Analytics Dataset (tên chính thức) |
| Nhà cung cấp / tác giả | J. Kuzilek, M. Hlosta và Z. Zdrahal, Knowledge Media Institute, The Open University [3] |
| URL chính thức / DOI | Trang của nhà cung cấp [2]; bài mô tả dữ liệu doi:10.1038/sdata.2017.171 [3]; tệp lưu trên figshare, doi:10.6084/m9.figshare.5081998.v1 [3] |
| Ngày truy cập | 06/11/2026 (giờ Việt Nam, UTC+7) |
| Phiên bản / bản phát hành | figshare phiên bản 1; trang của nhà cung cấp đăng phiên bản mới nhất nhưng không ghi số phiên bản [2] |
| Giấy phép / điều khoản | CC BY 4.0 [2], [12] |
| Phương thức thu thập | Tải trực tiếp một tệp nén zip từ figshare; đối chiếu kích thước và mã SHA-256 với giá trị tham chiếu ghi sẵn trong script thu thập; giải nén bảy bảng, giữ nguyên nội dung |
| Tệp gốc | anonymisedData.zip (46.750.706 byte), gồm courses, assessments, vle, studentInfo, studentRegistration, studentAssessment và studentVle (CSV; riêng studentVle là 453,8 MB) |
| Kiểm tra tính toàn vẹn | Mã SHA-256 và MD5 của tệp nén và của từng bảng được ghi trong manifest (danh sách các tệp kèm mã kiểm tra); cả bảy bảng đều khớp giá trị SHA-256 tham chiếu ghi sẵn |
| Trích dẫn | Kuzilek, Hlosta và Zdrahal (2017), *Scientific Data*, 4, 170171 [3] |

OULAD được phát hành ở ba nơi, nên cần ghi rõ bản dữ liệu được lấy từ đâu. Trang của nhà cung cấp dẫn đến một tệp nén trên máy chủ của Open University [2] và yêu cầu người dùng đối chiếu tệp này với mã MD5 [2]; tuy nhiên, vào lúc thu thập dữ liệu, đường dẫn đó trả về lỗi HTTP 404. Bài mô tả dữ liệu trích dẫn bản lưu trên figshare [3]. Bản này có DOI, có số phiên bản và là bản nhóm đã thu thập. Kho dữ liệu học máy UCI lưu bản thứ ba với DOI riêng [12]. Khi đối chiếu bản của UCI với các tệp đã thu thập, nhóm thấy cả bảy bảng đều có cùng các dòng dữ liệu. Khác biệt duy nhất là cách ghi giá trị thiếu ở năm bảng: UCI ghi dấu "?", còn figshare để trống ô (Phụ lục III). Vì vậy, khi phân tích, nhóm coi ô trống là giá trị thiếu và trích dẫn bản trên figshare cùng bài mô tả dữ liệu.

Quá trình thu thập có thể tái lập bằng hai lệnh. Lệnh thứ nhất (`src/collect.py`) tải tệp nén, kiểm tra tệp này và giải nén các bảng; lệnh thứ hai (`src/verify_structure.py`) chạy các bước kiểm tra cấu trúc ban đầu ở Mục 6. Gói thu thập dữ liệu gồm hai script này, tệp manifest chứa các mã kiểm tra, từ điển dữ liệu sao chép từ bài mô tả dữ liệu và nhật ký thu thập. Các tệp gốc được giữ nguyên như khi công bố: nhóm không làm sạch, không lọc và không chuyển đổi tệp nào.
