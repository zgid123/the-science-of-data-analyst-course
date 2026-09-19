# MiniTask 02 - Phân tích Kinh doanh & Giải quyết Vấn đề Bán lẻ Trực tuyến UK

- **Báo cáo hoàn chỉnh (Final Report):** [final-report-revised.docx](final-report-revised.docx)
- **Đề bài môn học:** [minitask-2.pdf](minitask-2.pdf)
- **Dữ liệu giao dịch:** [e-commerce data.csv](e-commerce%20data.csv)
- **Slide thuyết trình Slidev:** [slidev/slides.md](slidev/slides.md)
- **Mã nguồn phân tích (Source Code):**
  - **Jupyter Notebook:** [`minitask_02_analysis.ipynb`](minitask_02_analysis.ipynb) (Định dạng chuẩn Jupyter với Markdown, Code Pandas, Biểu đồ Matplotlib/Seaborn và kết quả đầu ra trực quan).
  - **Python Script:** [`minitask_02_analysis.py`](minitask_02_analysis.py) (Script độc lập tái lập 100% các bảng số liệu Bảng 7 đến Bảng 16, không phụ thuộc thư viện ngoài).

---

## Hướng dẫn chạy Mã nguồn (Execution Guide)

### 1. Chạy với Python Script độc lập (Zero Dependency)
Script được thiết kế để chạy trực tiếp trên bất kỳ môi trường Python 3 nào mà không yêu cầu cài đặt thêm thư viện ngoài:
```bash
python3 minitask_02_analysis.py
```
Toàn bộ quy trình từ làm sạch dữ liệu nguồn, loại trùng 5,268 dòng, lọc mã phi hàng hóa, đến đối soát Gross - Cancellation = Net và xuất các Bảng 7, 8, 9, 10, 13, 14, 15, 16 sẽ được in ra định dạng bảng chi tiết.

### 2. Mở và chạy trên Jupyter Notebook / Google Colab / VS Code
Mở tệp [`minitask_02_analysis.ipynb`](minitask_02_analysis.ipynb) trong VS Code, JupyterLab hoặc tải lên Google Colab:
- Sử dụng stack tiêu chuẩn: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- Các cell code được chia theo từng chương của Báo cáo, kèm diễn giải phương pháp và đồ thị trực quan (Hình 1, Hình 2, Hình 3, Hình 4, Hình 6).
- Kết quả đầu ra đã được tính toán và định dạng sẵn, giúp giảng viên và người đọc có thể xem ngay lập tức mà không bắt buộc phải tính toán lại từ đầu.
