## 7.2. Truy vết nguồn gốc dữ liệu, từ điển dữ liệu và phiên bản

Mỗi cột đã chuẩn bị đều được mô tả với trường nguồn, phép biến đổi, kiểu dữ liệu, vai trò và mức độ nhạy cảm, đúng như
đề bài yêu cầu [1]. Bước kiểm tra báo lỗi nếu một cột thiếu mô tả hoặc một danh sách biến dự báo chứa cột kiểm tra
công bằng, cột biến mục tiêu hay cột mô tả (V14). Bảng truy vết nguồn gốc dữ liệu (lineage) theo mẫu của đề bài nằm ở Phụ lục III (Bảng A.12); mỗi dòng
của bảng ứng với một biến đã chuẩn bị. Bản kê phiên bản (version manifest) đặt tên bộ dữ liệu đã chuẩn bị là
OULAD-N04-prepared-1.0. Bản kê này ghi lại mã SHA-256 của mọi tệp gốc, script và tệp đã chuẩn bị, số dòng, commit của
kho mã, phiên bản Python (3.12.7) và polars (2.1.0), cùng thời điểm tạo theo giờ phối hợp quốc tế (UTC).
