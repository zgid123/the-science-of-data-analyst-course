# Common glossary: data and databases

Data engineering, storage, data quality and data governance. Loaded for every report.

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| data | dữ liệu | | |
| Data Warehouse | kho dữ liệu (Data Warehouse) | First use with English | |
| Data Lake | hồ dữ liệu (Data Lake) | First use with English | |
| lakehouse | lakehouse | Keep English | |
| data lifecycle | vòng đời dữ liệu | | |
| Generation / Collection / Ingestion | Phát sinh / Thu thập / Nạp | Lifecycle stage names | |
| Transformation / Serving / Storage | Biến đổi / Phục vụ / Lưu trữ | Lifecycle stage names | |
| data consumers | đối tượng sử dụng dữ liệu | | |
| data source | nguồn dữ liệu | | |
| collector | bộ thu thập | | |
| ETL / ELT | ETL / ELT | Keep English | |
| structured / semi-structured / unstructured | có cấu trúc / bán cấu trúc / phi cấu trúc | | |
| database / relational database | cơ sở dữ liệu / cơ sở dữ liệu quan hệ | | |
| table / view / materialized view | bảng / view / materialized view | Keep "view", "materialized view" | |
| query / query engine | truy vấn / Query Engine | | |
| SQL-on-lake | SQL-on-lake | Keep English | |
| index / indexing | chỉ mục / lập chỉ mục | | |
| derived index | chỉ mục phái sinh | | |
| partition | phân vùng | | |
| dimensional model / fact table / dimension | mô hình chiều (dimensional model) / bảng sự kiện / chiều | | |
| metadata | metadata | Keep English; "siêu dữ liệu" only when the reader needs the gloss | |
| data quality / quality gate | chất lượng dữ liệu / Data Quality Gate | | |
| validation | kiểm định | | |
| lineage / provenance | dòng dõi dữ liệu / nguồn gốc | | |
| traceability | khả năng truy vết | | |
| freshness | độ mới | | độ tươi, tính tươi |
| authoritative (source) | có thẩm quyền | | |
| fact / evidence | dữ kiện (fact) / bằng chứng (evidence) | | |
| append-only / immutable | chỉ ghi thêm (append-only) / bất biến (immutable) | | |
| synchronisation / publication | đồng bộ / công bố | | |
| propagation delay | độ trễ lan truyền | | |
| deletion propagation | xóa lan truyền | | |
| audit store | kho lưu trữ kiểm toán (audit store) | | |
| backup / restore | sao lưu / khôi phục | | |
| retention | lưu giữ | "thời hạn lưu giữ" | |
| data governance | quản trị dữ liệu | | |
| personal data | dữ liệu cá nhân | | |
| pseudonymised / anonymised / de-identified | giả danh hóa / ẩn danh / khử định danh | | |
| business intelligence (BI) | trí tuệ kinh doanh (BI) | Keep "BI" after first use | |
| dashboard | bảng điều khiển (dashboard) | | |
| report (BI) | báo cáo | | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| subject–predicate–object triple | bộ ba chủ ngữ – vị từ – tân ngữ | "bộ ba" after first use | |
| self-loop (of a triple) | bộ ba tự lặp (self-loop) | Subject equals object | |
| data integrity | tính toàn vẹn dữ liệu | | |
| tuple | bộ giá trị | | |
| matching function | hàm so khớp | | |
| notification (LISTEN/NOTIFY) | thông báo | | |
| trigger (database) | trigger | Keep English for the database object | |
| database transaction | giao tác | "giao dịch" stays for a purchase or a payment | |
| commit (of a transaction) | commit | "khi giao tác được commit"; first use may gloss "xác nhận (commit)" | |
| predicate | vị từ | | |
| advisory lock / connection pool | khóa tư vấn (advisory lock) / nhóm kết nối | | |
| conjunction / disjunction | phép hội / phép tuyển | | |

## Tables, keys and data preparation

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| data dictionary | từ điển dữ liệu |  |  |
| granularity | độ chi tiết | | |
| imputation / impute | điền giá trị thiếu | avoid: "quy nạp", "nội suy" (interpolation is a different method) | quy nạp giá trị |
| inner join | nối trong (inner join) |  |  |
| join (of tables); left join | phép nối bảng; nối trái (left join) |  |  |
| many to one / one to one (table relationship) | nhiều – một / một – một | | |
| parent table | bảng cha | a table that keys refer to; "bảng gốc" stays for a raw source table | |
| primary key / foreign key | khóa chính / khóa ngoại |  |  |
