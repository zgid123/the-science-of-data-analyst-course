# Kiểm tra mẫu số 28.119 "còn hiệu lực tại ngày 14"

Ngày chạy: 2026-11-13. Dữ liệu: `datasets/oulad/studentRegistration.csv` (32.593 dòng).

## Kết luận

58 lượt đăng ký sau ngày 14 **vẫn nằm trong** 28.119. Phép trừ ở Mục 6 chỉ loại các lượt hủy vào hoặc trước
ngày 14, nên câu "còn hiệu lực tại ngày 14" chưa chính xác với con số này.

## Kết quả đếm

| Điều kiện | Số dòng |
|---|---:|
| Tổng số dòng | 32.593 |
| `date_unregistration` ≤ 0 | 3.097 |
| `date_unregistration` từ 1 đến 14 | 1.377 |
| `date_unregistration` trống hoặc > 14 | **28.119** |
| – trong đó `date_registration` > 14 | **58** |
| – trong đó thiếu `date_registration` | **7** |

- 32.593 − 3.097 − 1.377 = 28.119, khớp với Mục 6.
- Cả 58 lượt đăng ký muộn đều chưa hủy tính đến ngày 14, nên không lượt nào bị phép trừ loại ra.
- Trong 45 lượt thiếu ngày đăng ký, 38 lượt đã bị loại vì hủy vào hoặc trước ngày 14 (35 lượt hủy ≤ ngày 0,
  3 lượt hủy trong ngày 1–14); 7 lượt còn lại vẫn nằm trong 28.119.

## Hai cách sửa

| Cách | Mẫu số | Câu mô tả |
|---|---:|---|
| Giữ số, sửa chữ | 28.119 | "chưa hủy tính đến ngày 14" |
| Giữ chữ, sửa số | 28.061 | "còn hiệu lực tại ngày 14" (đã loại 58 lượt đăng ký muộn) |

Nếu loại thêm 7 lượt thiếu ngày đăng ký, mẫu số là 28.054.

## Chạy lại

```bash
python3 check-result/check_day14_denominator.py
```

Kết quả gốc của lần chạy này ở `output.txt`.
