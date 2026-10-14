# Nhóm 4 — Milestone 2 Data Collection Package

Ngày lập: 14/10/2026. Dataset: OULAD. Phạm vi yêu cầu M1: BBB-2014J, chốt cuối ngày 60. Báo cáo đi kèm: `../N04_Milestone2.docx` và `../N04_Milestone2.pdf`.

## Nội dung

- Raw dùng chung tại `../../../datasets/oulad/anonymisedData.zip`, chứa 7 CSV. Bản sao raw và ZIP đóng gói đã bỏ để tránh trùng dữ liệu khi push code; các manifest và bằng chứng kiểm tra được giữ nguyên. Dataset không nằm trong Git; máy mới cần chuẩn bị archive tại đường dẫn này hoặc truyền `--archive`.
- `metadata/raw_manifest.csv`: tên, số byte, SHA-256 và CRC32 từng CSV trong archive.
- `metadata/table_inventory.csv`: số dòng/cột, khóa hoặc nhóm định danh, null keys và dòng dư theo nhóm.
- `metadata/schema_checks.csv`: tất cả 43 cột, kiểu suy ban đầu, missing và min/max số; không xử lý dữ liệu.
- `metadata/structural_summary.json`: hash archive, count của BBB-2014J, outcome distribution, lịch bài và 5 kiểm tra tham chiếu.
- `metadata/local_source_checks.json`: cả 7 file local đã giải nén khớp byte với member raw đóng gói.
- `metadata/baseline.json`: khóa SHA-256 của M1 và scope; không có ngày duyệt được cung cấp.
- `metadata/aq_requirements.csv`, `search_log.csv`, `selection_matrix.csv`, `updated_traceability.csv`, `controlled_change_log.csv`: yêu cầu, lựa chọn và truy xuất bằng chứng của báo cáo.
- `metadata/*-uci.html`, `source_access.json`, `source-notes.md`: bằng chứng nguồn/license/citation và giới hạn truy cập.
- `metadata/ai_usage.md`: prompt có thật, hoạt động AI và trạng thái quyết định.
- `src/verify_collection.py`: kiểm tra cấu trúc chỉ đọc.

## Chạy lại kiểm tra

Yêu cầu Python 3.11+; khoảng 1 GB chỗ trống tạm. DuckDB giới hạn bộ nhớ 512 MB, 2 threads, được phép spill vào thư mục tạm. Không cần notebook, model hoặc dashboard. Từ thư mục package (môi trường ảo đặt ngoài repository):

```bash
python3 -m venv /tmp/milestone2-env
/tmp/milestone2-env/bin/python -m pip install -r requirements.txt
/tmp/milestone2-env/bin/python src/verify_collection.py
```

Hoặc từ vị trí bất kỳ:

```bash
python3 /path/to/data-collection/src/verify_collection.py --archive /path/to/anonymisedData.zip
```

Script giải nén vào thư mục tạm và xóa thư mục đó khi xong; không ghi đè raw. Nó cập nhật metadata kiểm tra (timestamp thay đổi, số đếm/hash phải khớp). Chạy lại trên archive gốc 7 CSV, không phải wrapper ZIP tải từ repository nếu wrapper có thêm nội dung. Không xóa missing, impute, tạo đặc trưng, cân bằng lớp hoặc fit model.

## Tái thu thập khi không còn raw local

1. Mở trang chính thức UCI: https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset . Xác nhận nguồn, CC BY 4.0 và citation.
2. Nhấn Download. Endpoint được trang liên kết tại ngày truy cập: https://archive.ics.uci.edu/static/public/349/open+university+learning+analytics+dataset.zip . HEAD được kiểm HTTP 200 ngày 14/10/2026; package này không tải lại endpoint hoặc khẳng định byte giống archive local.
3. Giữ file vừa tải nguyên gốc trong thư mục raw riêng. Lưu ngày giờ, URL cuối, tên file, dung lượng và SHA-256 mới. Nếu nội dung/bao gói khác, không ghi đè bản đã khóa và không đổi tên để giả là cùng version.
4. Nếu download là wrapper ZIP, đọc danh sách member trước; chọn archive OULAD 7 CSV nếu có. Nếu chỉ có CSV, cần kiểm schema và tạo manifest cho bản thu thập mới; không dùng script dành cho archive 7 CSV mà bỏ qua kiểm tra lỗi.
5. So cấu trúc với dictionary OU và kiểm hash từng CSV với `raw_manifest.csv`. Chỉ gọi cùng bản khi hash thật khớp. Khác hash phải ghi version/change log; ngày tải cũ không suy ngược từ ngày tải mới.

## Nguồn, license và citation

The Open University; Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal. CC BY 4.0: https://creativecommons.org/licenses/by/4.0/ . Khi chia sẻ hoặc tái sử dụng, ghi tác giả, nguồn, license và thay đổi nếu có. Package giữ raw nguyên gốc; metadata và report do nhóm/AI biên soạn riêng.

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2015). *Open University Learning Analytics dataset* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5KK69 .

Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. https://doi.org/10.1038/sdata.2017.171 .

Dictionary: https://research.stem.open.ac.uk/ouanalyse/open-dataset-more/ . Truy cập nguồn ngày 14/10/2026; ngày tải gốc archive local và release version chưa có bằng chứng. Link tải OU trả 404, link MD5 cũ chuyển về trang chủ; không có checksum nhà cung cấp hiện hành để so. Xem source-notes.md.

## Giới hạn cần giữ

`studentVle` có nhóm student–resource–day lặp; cột `key` của bảng này trong inventory là nhóm kiểm tra, không phải PK. Không dedup raw. Thiếu `date_unregistration` có thể biểu thị không rút học phần. `score` không có ngày công bố. `final_result` là outcome, cấm làm predictor. Sensitive attributes không bắt buộc cho dự báo. Không đăng dòng cá nhân trong report hoặc cố nhận diện sinh viên.

Có dữ liệu để bắt đầu Data Understanding của cốt lõi hồi cứu; khả thi cảnh báo thật chưa xác minh. Không có action/consent/capacity/post-action outcome để chứng minh AQ4 can thiệp. Các revision/selection trong báo cáo là bản biên soạn cần nhóm rà soát; không tuyên bố phê duyệt của nhóm hay giảng viên.
