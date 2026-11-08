# Domain glossary: card payments in Vietnam: Terms settled during the first translation (2026-10-10); Shared terms from report vocabularies (2026-10-28)

Card acceptance at the point of sale, acquiring, clearing and settlement, disputes, fees and statements, card security, anti-money laundering, POS e-invoices and the engineering of payment systems. Select it for reports on card payments, acquiring or payment-system design in Vietnam. Terms that Vietnamese law regulates take the wording of the Vietnamese original text, cited in Usage: Thông tư 18/2024/TT-NHNN as amended by Thông tư 45/2025/TT-NHNN (TT 18/2024), Nghị định 52/2024/NĐ-CP (NĐ 52/2024), Nghị định 123/2020/NĐ-CP as amended by Nghị định 70/2025/NĐ-CP (NĐ 70/2025), Thông tư 09/2020/TT-NHNN (TT 09/2020), Nghị định 13/2023/NĐ-CP (NĐ 13/2023) and Luật Phòng, chống rửa tiền số 14/2022/QH15 (Luật PCRT 2022). Engineering terms follow established Vietnamese IT usage and keep the English where Vietnamese engineers write it.

## Terms settled during the first translation (2026-10-10)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| operational resilience | khả năng phục hồi hoạt động | First use "khả năng phục hồi hoạt động (operational resilience)"; BCBS and PRA texts | khả năng chống chịu trong hoạt động |
| impact tolerance | ngưỡng chịu đựng tác động | PRA SS1/21 | |
| cascading failure | sự cố dây chuyền | | lỗi xếp tầng |
| retry storm / thundering herd | bão thử lại / hiện tượng dồn dập | First use with the English in parentheses | đám đông dồn dập |
| tail latency | độ trễ đuôi | First use "độ trễ đuôi (tail latency)" | |
| hot partition | phân vùng nóng | "shard" stays English | |
| dual write | ghi kép | First use "ghi kép (dual write)" | |
| silent data corruption | hỏng dữ liệu âm thầm | | |
| alert fatigue | quá tải cảnh báo | | |
| ransomware | mã độc tống tiền | First use "mã độc tống tiền (ransomware)" | |
| core banking system | hệ thống ngân hàng lõi | | |
| chaos engineering / fault injection / game day | kỹ thuật hỗn loạn / thí nghiệm chèn lỗi / ngày diễn tập sự cố | First use with the English in parentheses | |
| error budget | quỹ lỗi | SRE | ngân sách lỗi |
| graceful degradation | suy giảm có kiểm soát | | |
| single point of failure | điểm lỗi đơn lẻ | | |
| fail-open / fail-closed | tiếp tục khi lỗi / dừng khi lỗi | First use with the English in parentheses | mở khi lỗi, đóng khi lỗi |
| liability shift | chuyển dịch trách nhiệm | First use "chuyển dịch trách nhiệm (liability shift)" | |
| technical fallback | chuyển sang dải từ do lỗi kỹ thuật | First use with the English in parentheses | |
| key entry (of the card number) | nhập tay số thẻ | | |
| preauthorisation | cấp phép trước | | |
| netting | xác định số ròng phải thu, phải trả | Distinct from "bù trừ" (clearing) | |
| rolling reserve | ký quỹ cuốn chiếu | | |
| pricing plan / volume tier / true-up | biểu phí / bậc phí / khoản điều chỉnh bù chênh | | |
| settlement bank | ngân hàng quyết toán | | |
| advice (ISO 8583 message) | thông báo | "thông báo đảo giao dịch" for a reversal advice | |
| dual-message | mô hình hai thông điệp | | |
| deadline propagation | lan truyền thời hạn | | lan truyền hạn chót |
| static stability | ổn định tĩnh | AWS | |
| home site | trung tâm dữ liệu chủ quản | | |
| compensation (saga step) | thao tác bù | | |
| pivot transaction (saga) | giao dịch bản lề | First use "giao dịch bản lề (pivot transaction)" | giao dịch then chốt |
| network partition | chia cắt mạng | First use "chia cắt mạng (network partition)"; "phân vùng" stays for data partitions | phân mảnh mạng, phân tách mạng, phân vùng mạng |
| availability zone | vùng khả dụng | Cloud zones; "vùng" alone is a pipeline zone | vùng sẵn sàng |
| terminal intercept | thành phần trung gian chuyển thông điệp | First use "thành phần trung gian chuyển thông điệp từ máy POS (terminal intercept)" | |
| incremental authorisation / final authorisation | cấp phép bổ sung / cấp phép cuối cùng | | |
| data element (ISO 8583) | phần tử dữ liệu | "phần tử dữ liệu 11" | |
| billing currency | đồng tiền ghi nợ | Currency of the cardholder's statement | |
| payment allocation (of a repayment) | thứ tự thu hồi nợ | Order in which a repayment settles balances | phân bổ thanh toán |
| Financial Action Task Force (FATF) | Lực lượng Đặc nhiệm Tài chính về chống rửa tiền | Written in full; the English text does not abbreviate it | |
| job instance (batch) | thực thể tác vụ | Spring Batch | phiên bản tác vụ, thực thể job |
| Prudential Regulation Authority (United Kingdom) | Cơ quan Quản lý Thận trọng của Vương quốc Anh | Written in full | |
| partition mode (CAP) | chế độ vận hành khi chia cắt mạng | Brewer | |
| legal hold (on records) | giữ nguyên hồ sơ theo yêu cầu pháp lý | "phong tỏa" stays for frozen funds and accounts | |
| network token (EMV payment tokenisation) | token do tổ chức thẻ cấp | First use "token do tổ chức thẻ cấp (network token)" | token mạng lưới |
| goodput | goodput | Keep English; first use "goodput (lưu lượng được xử lý thành công)" | |
| Principles for Financial Market Infrastructures (PFMI) | Bộ nguyên tắc về hạ tầng thị trường tài chính | CPMI-IOSCO; written in full, in every part, also where English writes it in lower case | nguyên tắc dành cho hạ tầng thị trường tài chính |
| Basel Core Principles | Bộ nguyên tắc cốt lõi Basel | | |
| set off (a merchant's negative balance against future sales) | cấn trừ | "bù trừ" stays for clearing | |
| currency minor unit | đơn vị lẻ của đồng tiền | | đơn vị tiền tệ nhỏ nhất |
| processor (payment processor, an organisation) | đơn vị xử lý | "bộ xử lý" only for software that consumes events ("các bộ xử lý sự kiện") | |
| terminal fleet / fleet | đội thiết bị đầu cuối / đội thiết bị | Full form in headings and at first mention; "đội thiết bị" in running text, as in C5.B7.1 and C5.B8.1 | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| terminal journal | nhật ký giao dịch trên máy POS | | tạp chí thiết bị đầu cuối |
