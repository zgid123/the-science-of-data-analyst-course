## Phụ lục III – Kế hoạch thu thập dữ liệu và gói thu thập dữ liệu

Gói thu thập dữ liệu tạo lại chính xác bản OULAD mà nhóm phân tích dữ liệu đã thu thập. Các tệp gốc do script thu thập tạo ra và được giữ nguyên, không chỉnh sửa. Cấu trúc của gói như sau:

```text
package/
  README.md
  data/raw/        published files, unchanged
  metadata/        source.md, citation.bib, data_dictionary.md, raw_manifest.csv,
                   collection_log.txt, structure_report.md, structure_results.json
  src/             collect.py (download, verify, extract), verify_structure.py (Task 6)
```

Bảng A.3 ghi nguồn và giấy phép của bộ dữ liệu trong gói.

**Bảng A.3. Nguồn, giấy phép và trích dẫn**

| Hạng mục | Giá trị |
| :---- | :---- |
| Tên bộ dữ liệu | Open University Learning Analytics Dataset (tên chính thức) |
| Nhà cung cấp / tác giả | Jakub Kuzilek, Martin Hlosta, Zdenek Zdrahal; Knowledge Media Institute, The Open University (UK) |
| Trang chính thức | Trang của nhà cung cấp: https://research.stem.open.ac.uk/ouanalyse/dataset/ ; bài mô tả dữ liệu: https://doi.org/10.1038/sdata.2017.171 |
| Bản đã thu thập | Bản lưu trên figshare mà bài mô tả dữ liệu trích dẫn, DOI https://doi.org/10.6084/m9.figshare.5081998.v1 (phiên bản 1), tệp https://ndownloader.figshare.com/files/8606371 |
| Nơi phát hành khác | Kho dữ liệu học máy UCI, DOI https://doi.org/10.24432/C5KK69 (cùng dữ liệu; giá trị thiếu được ghi là "?" thay vì để trống); đường dẫn trên trang của nhà cung cấp http://schools.stem.open.ac.uk/cdn/files/anonymisedData.zip trả về lỗi HTTP 404 vào ngày 05/11/2026 |
| Ngày truy cập | 06/11/2026 (UTC+7; `metadata/collection_log.txt` ghi 2026-11-05 18:24 UTC) |
| Phiên bản | Phiên bản 1 trên figshare (trang của nhà cung cấp ghi "phiên bản mới nhất" nhưng không nêu số phiên bản) |
| Giấy phép | Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ |
| Phương thức thu thập | Tải trực tiếp một tệp nén zip, đối chiếu với các giá trị SHA-256 tham chiếu ghi sẵn, rồi giải nén và giữ nguyên nội dung (`src/collect.py`) |
| Kiểm tra tính toàn vẹn | `metadata/raw_manifest.csv` (số byte, SHA-256, MD5 và số dòng dữ liệu của từng tệp); `metadata/collection_log.txt` |
| Trích dẫn | Kuzilek, Hlosta và Zdrahal (2017), *Scientific Data*, 4, Article 170171, https://doi.org/10.1038/sdata.2017.171 (thông tin đầy đủ trong citation.bib) |

Bảng A.4 là manifest của các tệp gốc: với mỗi tệp đã thu thập, bảng ghi dung lượng, mã kiểm tra (checksum) và số dòng dữ liệu. Mỗi bảng dữ liệu đều khớp với giá trị SHA-256 tham chiếu ghi sẵn.

**Bảng A.4. Manifest của các tệp gốc**

| Tệp | Số byte | SHA-256 | MD5 | Số dòng dữ liệu | Kết quả đối chiếu |
| :---- | :---- | :---- | :---- | :---- | :---- |
| anonymisedData.zip | 46.750.706 | 90dda45037939953f979072fa70a809ebe07e90ec783c408762af7698a3825ec | 7412686fd77cf0e0ee1e8c3e9b354308 |  | Khớp |
| courses.csv | 526 | 4f16eee7454b15e109b0a21a0e43be820e6846ed6f9301bb7feb5ab5ad737a75 | 4c3df8a42a98a0d26b22f507007c31a8 | 22 | Khớp |
| assessments.csv | 8.200 | 8cc738fb88ad760571d6f2a23059bfee0ffcae3bcd830514c9cbd5c6d5a046f1 | 6126f9d435767bcc70134b46f21c2a90 | 206 | Khớp |
| vle.csv | 260.126 | d1b28303dea802ad87b4484e1196e878e06824850b9a4fe8aa34693439fe87e9 | 0e7ef38c483daca42900ca426b66f8da | 6.364 | Khớp |
| studentInfo.csv | 3.461.652 | 7e6f3e474a5eee00639d2a414a6c7e928745823c2d2c2563ca1780145f99b0d6 | ead11d001fe8b7aed1469daa643a812c | 32.593 | Khớp |
| studentRegistration.csv | 1.109.984 | 0d32676285372aaf2e7a80304e5b274b4fba24313e2ca4c04317225e1ec90170 | ef06e3d5784dc7dffe06ef911c5b190c | 32.593 | Khớp |
| studentAssessment.csv | 5.690.310 | fd5320786328d05af841ee7dd4b5871b9dada3b9fe9d6a3642b2f42635510a6e | 9ceb38acaeb26fbc15c98b563290c1db | 173.912 | Khớp |
| studentVle.csv | 453.836.331 | 52668253d876c5becbcb72185977152700cecab2942aca807fecc3dd54b937f0 | b8aae6f4ffd1523319aeb56d66b17f72 | 10.655.280 | Khớp |

Bảng A.5 so sánh bản OULAD trên UCI với các tệp đã thu thập từ figshare, theo từng bảng.

**Bảng A.5. So sánh bản trên UCI với các tệp đã thu thập**

| Bảng | Số byte trên figshare | Số byte trên UCI | Cùng SHA-256 | Ký tự xuống dòng (figshare / UCI) | Số dòng (figshare / UCI) | Cùng nội dung dòng |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| assessments.csv | 8.200 | 8.211 | Không | CRLF / CRLF | 206 / 206 | chỉ khác ở giá trị thiếu: UCI ghi '?', figshare để trống (11 dòng) |
| courses.csv | 526 | 526 | Có | CRLF / CRLF | 22 / 22 | Có |
| studentAssessment.csv | 5.690.310 | 5.690.483 | Không | CRLF / CRLF | 173.912 / 173.912 | chỉ khác ở giá trị thiếu: UCI ghi '?', figshare để trống (173 dòng) |
| studentInfo.csv | 3.461.652 | 3.462.763 | Không | CRLF / CRLF | 32.593 / 32.593 | chỉ khác ở giá trị thiếu: UCI ghi '?', figshare để trống (1.111 dòng) |
| studentRegistration.csv | 1.109.984 | 1.132.550 | Không | CRLF / CRLF | 32.593 / 32.593 | chỉ khác ở giá trị thiếu: UCI ghi '?', figshare để trống (22.560 dòng) |
| studentVle.csv | 453.836.331 | 453.836.331 | Có | CRLF / CRLF | 10.655.280 / 10.655.280 | Có |
| vle.csv | 260.126 | 270.612 | Không | CRLF / CRLF | 6.364 / 6.364 | chỉ khác ở giá trị thiếu: UCI ghi '?', figshare để trống (5.243 dòng) |
