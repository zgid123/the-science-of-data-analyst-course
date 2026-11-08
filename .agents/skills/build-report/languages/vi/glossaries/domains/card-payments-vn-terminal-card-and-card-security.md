# Domain glossary: card payments in Vietnam: Terminal, card and card security; Fraud, anti-money laundering and data protection; E-invoices; Engineering of payment systems

Card acceptance at the point of sale, acquiring, clearing and settlement, disputes, fees and statements, card security, anti-money laundering, POS e-invoices and the engineering of payment systems. Select it for reports on card payments, acquiring or payment-system design in Vietnam. Terms that Vietnamese law regulates take the wording of the Vietnamese original text, cited in Usage: Thông tư 18/2024/TT-NHNN as amended by Thông tư 45/2025/TT-NHNN (TT 18/2024), Nghị định 52/2024/NĐ-CP (NĐ 52/2024), Nghị định 123/2020/NĐ-CP as amended by Nghị định 70/2025/NĐ-CP (NĐ 70/2025), Thông tư 09/2020/TT-NHNN (TT 09/2020), Nghị định 13/2023/NĐ-CP (NĐ 13/2023) and Luật Phòng, chống rửa tiền số 14/2022/QH15 (Luật PCRT 2022). Engineering terms follow established Vietnamese IT usage and keep the English where Vietnamese engineers write it.

## Terminal, card and card security

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| point-of-sale terminal | thiết bị chấp nhận thẻ tại điểm bán | TT 18/2024, Điều 3 khoản 24 (sửa đổi bởi TT 45/2025, Điều 1). Overrides "máy chấp nhận thẻ" of digital-banking-vn in card reports | máy cà thẻ |
| POS terminal / mPOS | thiết bị POS / mPOS | First use "thiết bị chấp nhận thẻ tại điểm bán (POS)"; then "thiết bị POS" or "máy POS"; keep "mPOS" | |
| cash register | máy tính tiền | NĐ 70/2025, Điều 3 khoản 2 điểm d | máy thu ngân |
| terminal fleet / terminal management system (TMS) | đội thiết bị đầu cuối / hệ thống quản lý thiết bị đầu cuối (TMS) | "thiết bị đầu cuối" as in TT 18/2024, Điều 3 khoản 24 | hạm đội thiết bị |
| floor limit | hạn mức ngoại tuyến | First use "hạn mức ngoại tuyến (floor limit)", the maximum a terminal approves offline | hạn mức sàn, giới hạn sàn |
| online / offline (transaction) | trực tuyến / ngoại tuyến | "phê duyệt ngoại tuyến", "chấp nhận thẻ ngoại tuyến" | |
| store-and-forward | lưu rồi chuyển tiếp | First use "lưu rồi chuyển tiếp (store-and-forward)" | lưu trữ và chuyển đi, lưu và chuyển tiếp |
| stand-in processing (STIP) | xử lý thay thế (STIP) | First use "xử lý thay thế (stand-in processing, STIP)": the network approves within limits set by an unreachable issuer | xử lý dự bị |
| chip / chip card / magnetic stripe | chip / thẻ chip / dải từ | TT 18/2024, Điều 3 khoản 6 ("có gắn chip điện tử") | sọc từ, vạch từ |
| fallback (to magnetic stripe) | chuyển sang dải từ (fallback) | Card sense only; the software sense keeps common "phản hồi dự phòng (fallback)" | |
| contactless | không tiếp xúc | TT 18/2024, Điều 3 khoản 29 ("chip không tiếp xúc") | phi tiếp xúc |
| cardholder verification method (CVM) | phương thức xác minh chủ thẻ (CVM) | Keep "CVM" after first use | phương pháp kiểm chứng chủ thẻ |
| personal identification number (PIN) / PIN block | mã PIN / khối PIN (PIN block) | TT 18/2024, Điều 3 khoản 23 ("Mã số xác định chủ thẻ (PIN)"); later "mã PIN" | số định danh cá nhân |
| cryptogram / application cryptogram (AC) | cryptogram / cryptogram ứng dụng (AC) | Keep English; first use "cryptogram (giá trị mật mã do chip tạo ra cho từng giao dịch)" | mật mã đồ, mật mã học ứng dụng |
| skimming / shimming | skimming / shimming | Keep English; first use "skimming (gắn thiết bị đọc trộm dải từ)", "shimming (chèn thiết bị đọc trộm vào khe chip)" | lướt thẻ, đệm thẻ |
| relay attack | tấn công chuyển tiếp | First use "tấn công chuyển tiếp (relay attack)", e.g. Ghost Tap over NFC | tấn công rơ-le |
| counterfeit card | thẻ giả | TT 18/2024, Điều 3 khoản 11 | thẻ nhái, thẻ làm giả |
| fraudulent or counterfeit card transaction | giao dịch thẻ gian lận, giả mạo | TT 18/2024, Điều 3 khoản 12 | |
| tamper / tamper-responsive | can thiệp trái phép / tự phản ứng khi bị can thiệp | "thiết bị POS bị can thiệp trái phép" | giả mạo thiết bị |
| key injection | nạp khóa | First use "nạp khóa (key injection)" vào thiết bị POS | tiêm khóa, bơm khóa |
| hardware security module (HSM) | mô-đun bảo mật phần cứng (HSM) | Keep "HSM" after first use | mô-đun an ninh phần cứng |
| derived unique key per transaction (DUKPT) | DUKPT | Keep English; first use "DUKPT (khóa riêng suy diễn cho từng giao dịch)" | |
| point-to-point encryption (P2PE) | mã hóa điểm-điểm (P2PE) | Keep "P2PE" after first use | mã hóa điểm-tới-điểm |
| tokenisation / token vault | token hóa / token vault | First use "token hóa (tokenisation)"; keep "token vault" with gloss "kho lưu ánh xạ token – số thẻ" | |
| PCI DSS / cardholder data environment | PCI DSS / môi trường dữ liệu chủ thẻ | Keep "PCI DSS"; "môi trường dữ liệu chủ thẻ (CDE)" | |

## Fraud, anti-money laundering and data protection

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| fake transaction / POS cash-out | giao dịch thanh toán khống / rút tiền mặt qua POS | TT 18/2024, Điều 3 khoản 9 ("giao dịch thanh toán khống tại đơn vị chấp nhận thẻ"); NĐ 52/2024, Điều 29 | giao dịch ma, giao dịch giả tạo |
| transaction laundering | rửa giao dịch | First use "rửa giao dịch (transaction laundering)": sales of a hidden business pushed through another merchant's terminal | giặt giao dịch |
| money mule | người chuyển tiền thuê | First use "người chuyển tiền thuê (money mule)"; "tài khoản thuê, mượn" for the account | con la tiền, la tiền |
| anti-money laundering (AML) / combating the financing of terrorism (CFT) | phòng, chống rửa tiền / chống tài trợ khủng bố | Luật PCRT 2022; keep "AML/CFT" in tables | chống rửa tiền bẩn |
| know your customer (KYC) | nhận biết khách hàng (KYC) | Luật PCRT 2022, Điều 9 | biết khách hàng của bạn |
| reporting entity | đối tượng báo cáo | Luật PCRT 2022, Điều 4 | |
| suspicious transaction report | báo cáo giao dịch đáng ngờ | Luật PCRT 2022, Điều 26 | báo cáo hoạt động đáng ngờ, báo cáo giao dịch khả nghi |
| large-value transaction | giao dịch có giá trị lớn | Luật PCRT 2022, Điều 25 | |
| sanctions screening / blacklist | sàng lọc danh sách đen / Danh sách đen | Luật PCRT 2022, Điều 3 khoản 9 ("Danh sách đen"); first use "sàng lọc danh sách đen (sanctions screening)" | sàng lọc trừng phạt, rà soát cấm vận |
| sensitive personal data | dữ liệu cá nhân nhạy cảm | NĐ 13/2023, Điều 2 khoản 4 | |
| personal data controller / personal data processor | Bên Kiểm soát dữ liệu cá nhân / Bên Xử lý dữ liệu cá nhân | NĐ 13/2023, Điều 2 khoản 9–10 | bên điều khiển dữ liệu |

## E-invoices

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| e-invoice / POS-generated e-invoice | hóa đơn điện tử / hóa đơn điện tử khởi tạo từ máy tính tiền | NĐ 70/2025 (sửa đổi NĐ 123/2020, Điều 3 khoản 2 điểm c và Điều 11): "hóa đơn điện tử khởi tạo từ máy tính tiền có kết nối chuyển dữ liệu điện tử với cơ quan thuế" | hóa đơn POS, hóa đơn sinh từ máy POS |
| adjustment invoice / replacement invoice | hóa đơn điều chỉnh / hóa đơn thay thế | NĐ 70/2025 (sửa đổi NĐ 123/2020, Điều 19) | hóa đơn sửa đổi, hóa đơn thế chỗ |
| tax authority | cơ quan thuế | NĐ 70/2025 | cơ quan quản lý thuế vụ |
| seller / buyer (invoice) | người bán / người mua | NĐ 70/2025, Điều 11 khoản 3 | |

## Engineering of payment systems

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| idempotency / idempotent receiver | tính lũy đẳng / bộ tiếp nhận lũy đẳng | Builds on common "lũy đẳng (idempotent)"; first use "bộ tiếp nhận lũy đẳng (idempotent receiver)" | tính bất biến khi lặp |
| idempotency key | idempotency key | Keep English; first use "idempotency key (khóa chống xử lý lặp)" | khóa đồng nhất |
| at-least-once delivery / exactly-once | phân phối ít nhất một lần / đúng một lần | First use with English: "phân phối ít nhất một lần (at-least-once delivery)" | giao hàng ít nhất một lần |
| duplicate (message, transaction) | bản trùng / giao dịch trùng lặp | Builds on common "chống trùng lặp" | bản sao chép trùng |
| in-doubt transaction / unknown outcome | giao dịch chưa rõ kết quả / kết quả chưa rõ | "kết quả chưa rõ sau khi hết thời gian chờ" | giao dịch lơ lửng |
| jitter / retry with backoff and jitter | jitter / thử lại có giãn cách và jitter | Builds on common "thử lại / giãn cách thử lại (backoff)"; keep "jitter" | rung pha |
| circuit breaker | bộ ngắt mạch | First use "bộ ngắt mạch (circuit breaker)" | cầu dao điện |
| bulkhead | bulkhead | Keep English; first use "bulkhead (vách ngăn cô lập tài nguyên)" | vách tàu |
| load shedding | cắt giảm tải | First use "cắt giảm tải (load shedding)" | sa thải tải, rụng tải |
| saga / compensating transaction | saga / giao dịch bù | Keep "saga"; first use "giao dịch bù (compensating transaction)" | giao dịch đền bù |
| transactional outbox / relay | outbox giao dịch / bộ chuyển tiếp | First use "outbox giao dịch (transactional outbox)": a table written in the same database transaction as the state change | |
| event stream / event | luồng sự kiện / sự kiện | First use "luồng sự kiện (event stream)" | dòng chảy sự kiện |
| ledger / double-entry ledger | sổ cái / sổ cái bút toán kép | "sổ cái chỉ ghi thêm" | sổ ghi chép kép |
| journal entry / posting | bút toán / hạch toán | "hạch toán vào tài khoản thẻ" | mục nhật ký, mục ghi sổ |
| control account | tài khoản kiểm soát | | |
| reconciliation / reconciliation break | đối soát / chênh lệch đối soát | First use "đối soát (reconciliation)"; first use "chênh lệch đối soát (break)" | khớp lệnh, điều hòa giao dịch, hòa giải giao dịch, đối chiếu khớp |
| tie-out | đối chiếu cân số | First use "đối chiếu cân số (tie-out)": opening balance plus movements equals closing balance | buộc số |
| maker-checker | người lập – người duyệt | First use "nguyên tắc người lập – người duyệt (maker-checker)"; TT 09/2020 ("vừa khởi tạo vừa phê duyệt") | người làm – người kiểm |
| write-once (storage) | ghi một lần (WORM) | First use "lưu trữ ghi một lần (write-once, WORM)" | viết một lần |
| active-active / active-passive | active-active / active-passive | Keep English; first use "active-active (hai trung tâm cùng xử lý)" | |
| failover / failback | chuyển đổi dự phòng / chuyển về hệ thống chính | TT 09/2020 ("chuyển đổi hoạt động thực tế sang hệ thống dự phòng"); first use "chuyển đổi dự phòng (failover)" | chuyển đổi lỗi |
| disaster recovery / disaster recovery site | dự phòng thảm họa / hệ thống dự phòng thảm họa | TT 09/2020, Điều 50 | khôi phục thảm họa, phục hồi sau thảm họa |
| business continuity | bảo đảm hoạt động liên tục | TT 09/2020 | liên tục kinh doanh |
| recovery time objective (RTO) / recovery point objective (RPO) | mục tiêu thời gian khôi phục (RTO) / mục tiêu điểm khôi phục (RPO) | Keep "RTO", "RPO" after first use | |
| split brain / fencing token | split-brain / fencing token | Keep English; first use "split-brain (hai nút cùng tự nhận là nút chính)", "fencing token (số hiệu tăng dần chặn ghi từ nút cũ)" | não phân tách, mã thông báo hàng rào |
| gray failure | sự cố ngầm | First use "sự cố ngầm (gray failure)": the component passes health checks while serving wrong or slow results | thất bại xám |
| health check | kiểm tra sức khỏe | "kiểm tra sức khỏe dịch vụ (health check)" | |
| observability / trace / distributed tracing | khả năng quan sát / trace / truy vết phân tán | First use "khả năng quan sát (observability)"; keep "trace" | dấu vết phân tán |
| service-level objective (SLO) | mục tiêu mức dịch vụ (SLO) | Keep "SLO" after first use | mục tiêu cấp độ dịch vụ |
| canary release / feature flag | triển khai canary / cờ tính năng | First use "triển khai canary (canary release)", "cờ tính năng (feature flag)" | phát hành chim hoàng yến, phát hành chim yến |
| contract test | kiểm thử hợp đồng | First use "kiểm thử hợp đồng (contract test)" | |
| command and query responsibility segregation (CQRS) | CQRS | Keep English; first use "CQRS (tách luồng ghi và luồng đọc)" | |
| multi-factor authentication for administrators | xác thực đa yếu tố khi truy cập quản trị | TT 09/2020 | |
| information system security | an toàn hệ thống thông tin | TT 09/2020 | an ninh hệ thống thông tin |
