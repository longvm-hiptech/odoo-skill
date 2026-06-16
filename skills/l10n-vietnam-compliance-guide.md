---
name: l10n-vietnam-compliance-guide
keywords: [presales, vietnam, l10n_vn, hoa don dien tu, e-invoice, TT200, TT133, thue, compliance]
description: Tổng hợp yêu cầu pháp lý kế toán/thuế/hóa đơn điện tử tại Việt Nam và mức độ đáp ứng của module l10n_vn trong Odoo. Câu hỏi gần như luôn gặp trong mọi deal tại VN.
odoo_versions: [all]
related_skills: [odoo-app-feature-matrix, vietnam-integration-landscape, odoo-licensing-deployment-guide, presales-to-implementation-handoff-guide, github-verification-guide]
---

# Vietnam Localization Compliance Guide (l10n_vn) — PreSale

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  VIETNAM COMPLIANCE: KẾ TOÁN — THUẾ — HÓA ĐƠN ĐIỆN TỬ                         ║
║  "Odoo có đáp ứng quy định VN không?" — câu hỏi #1 trong mọi deal VN          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

> ⚠️ **Disclaimer quan trọng:** Tài liệu này tổng hợp các quy định **mang tính tham khảo cho PreSale** để định hướng trao đổi với khách hàng — **KHÔNG phải tư vấn pháp lý/thuế**. Quy định pháp luật VN thay đổi thường xuyên; với mỗi deal, PreSale cần:
> 1. Xác nhận lại văn bản pháp luật hiện hành tại thời điểm triển khai.
> 2. Verify mức độ hỗ trợ thực tế của module `l10n_vn` cho **đúng version Odoo** của khách bằng `skills/github-verification-guide.md` (đọc trực tiếp source `addons/l10n_vn` trên GitHub Odoo cho version đó).
> 3. Khuyến nghị khách có kế toán trưởng/đơn vị tư vấn thuế tham gia review trước khi cam kết hợp đồng.

---

## 1. Vì sao đây là chủ đề "sống còn" trong PreSale tại VN

Hầu hết khách hàng VN — đặc biệt là chủ DN/kế toán trưởng — sẽ hỏi ngay từ buổi gặp đầu: *"Phần mềm nước ngoài này có làm được hóa đơn điện tử/báo cáo thuế VN không?"*. Trả lời mơ hồ ở đây dễ làm mất uy tín ngay từ đầu, dù phần còn lại của giải pháp rất phù hợp.

**Nguyên tắc trả lời:**
- Phần **kế toán nền tảng** (Chart of Accounts theo TT200/TT133, sổ sách, báo cáo tài chính cơ bản) → Odoo + `l10n_vn` đáp ứng tốt, đây là phần "Fit".
- Phần **hóa đơn điện tử kết nối nhà cung cấp + một số báo cáo thuế theo mẫu cứng** → thường là "Gap (Integration)" cần tích hợp thêm, **không phải Odoo không làm được**, mà là cần kết nối với hệ sinh thái HĐĐT của VN.

---

## 2. Chuẩn mực kế toán VN & Chart of Accounts

| Quy định | Đối tượng áp dụng | Ghi chú cho Odoo |
|---|---|---|
| **Thông tư 200/2014/TT-BTC** | Doanh nghiệp lớn, mọi loại hình | Hệ thống tài khoản kế toán đầy đủ (Group 1-9) |
| **Thông tư 133/2016/TT-BTC** | Doanh nghiệp vừa và nhỏ (SME) | Hệ thống tài khoản rút gọn |

- Module `l10n_vn` cung cấp **Chart of Accounts (CoA) mẫu** theo các thông tư trên — khi cài đặt công ty mới với country = Vietnam, Odoo có thể nạp sẵn CoA tiếng Việt.
- **Cần verify:** phiên bản CoA đi kèm `l10n_vn` có cập nhật theo thông tư mới nhất chưa (các thông tư có thể được sửa đổi/thay thế theo thời gian) — kiểm tra file `data/account_chart_template_data.xml` (hoặc tương đương) trong `addons/l10n_vn` của version Odoo cụ thể.
- Thực tế triển khai: nhiều đối tác VN vẫn **tùy chỉnh lại CoA** theo thói quen của kế toán trưởng (số hiệu tài khoản chi tiết cấp 2/3) — đây là công việc **cấu hình** (Partial Fit), không phải custom code.

---

## 3. Hóa đơn điện tử (HĐĐT) — chủ đề quan trọng nhất

### 3.1 Khung pháp lý

| Văn bản | Nội dung chính |
|---|---|
| **Nghị định 123/2020/NĐ-CP** | Quy định về hóa đơn, chứng từ — bắt buộc chuyển đổi sang HĐĐT |
| **Thông tư 78/2021/TT-BTC** | Hướng dẫn thực hiện NĐ 123 — định dạng dữ liệu HĐĐT, lộ trình áp dụng |
| **Luật Quản lý thuế 2019 (38/2019/QH14)** | Cơ sở pháp lý chung |

**Điểm mấu chốt:** Từ 01/07/2022, hóa đơn điện tử là **bắt buộc** với hầu hết doanh nghiệp tại VN — không còn hóa đơn giấy (trừ một số trường hợp đặc thù).

### 3.2 Hai loại hóa đơn điện tử

| Loại | Mô tả | Đối tượng |
|---|---|---|
| **HĐĐT có mã của Cơ quan thuế (CQT)** | Hóa đơn được CQT cấp mã xác thực trước khi gửi khách hàng | Đa số doanh nghiệp |
| **HĐĐT không có mã** | DN tự phát hành, gửi dữ liệu cho CQT theo bảng tổng hợp định kỳ | DN đủ điều kiện theo quy định (rủi ro thấp về thuế, hạ tầng CNTT đáp ứng...) |

### 3.3 Các nhà cung cấp HĐĐT phổ biến tại VN

| Nhà cung cấp | Tên thương mại | Ghi chú |
|---|---|---|
| MISA | meInvoice | Phổ biến nhất với SME, thường đi kèm hệ sinh thái MISA AMIS |
| Viettel | S-Invoice / vInvoice | Mạnh ở DN vừa-lớn, có hạ tầng viễn thông |
| VNPT | VNPT Invoice | Phổ biến ở DN có quan hệ với VNPT (viễn thông, điện...) |
| BKAV | eHoadon | |
| FPT | FPT eInvoice | |
| Softdreams/CMC/T-VAN khác | EasyInvoice, Sinvoice, ... | Nhiều nhà cung cấp T-VAN nhỏ hơn theo từng vùng |

### 3.4 Hiện trạng tích hợp Odoo ↔ HĐĐT VN

> 🔍 **Đây là phần BẮT BUỘC verify riêng cho mỗi version/deal**, vì thay đổi nhanh theo thời gian và theo bản Community/Enterprise.

Khung đánh giá gợi ý khi verify:

1. **Kiểm tra `addons/l10n_vn` (Community)** — thường chỉ gồm CoA + báo cáo thuế cơ bản, **hiếm khi có sẵn connector tới nhà cung cấp HĐĐT cụ thể**.
2. **Kiểm tra `enterprise/l10n_vn_*`** (nếu khách có Enterprise) — một số bản Odoo Enterprise có thêm module hóa đơn điện tử cho 1 số quốc gia, cần kiểm tra VN có nằm trong danh sách không, và **nhà cung cấp nào** được hỗ trợ sẵn.
3. **Kiểm tra OCA** (`https://github.com/OCA/l10n-vietnam` hoặc tương tự nếu tồn tại) — cộng đồng OCA đôi khi có module bổ sung cho HĐĐT VN.
4. **Mặc định coi là Gap (Integration)** nếu không tìm thấy module xác nhận — báo giá tích hợp HĐĐT như một hạng mục riêng (xem `presales-effort-estimation-guide.md`, mục tích hợp).

**Cách tích hợp phổ biến khi phải làm Gap (Integration):**
- Hầu hết nhà cung cấp HĐĐT (MISA, Viettel, VNPT...) đều có **API/Web Service** để: (1) gửi dữ liệu hóa đơn từ Odoo → tạo HĐĐT, (2) nhận lại số hóa đơn + mã CQT + link tra cứu → ghi ngược vào `account.move` trong Odoo.
- Effort phụ thuộc vào: chất lượng tài liệu API của NCC, có SDK Python sẵn không, số loại hóa đơn cần hỗ trợ (bán hàng, điều chỉnh, thay thế, hủy).
- Pattern kỹ thuật tham khảo: `external-api-patterns.md`.

### 3.5 Câu trả lời mẫu cho khách hàng

> *"Odoo đáp ứng tốt phần kế toán nền tảng theo chuẩn VN (sổ sách, hạch toán, báo cáo tài chính). Với hóa đơn điện tử, chúng tôi sẽ tích hợp Odoo với nhà cung cấp HĐĐT mà công ty đang sử dụng (ví dụ MISA/Viettel/VNPT) — đây là hạng mục tích hợp được báo giá riêng trong đề xuất, đảm bảo công ty không cần đổi nhà cung cấp HĐĐT đang dùng."*

---

## 4. Báo cáo thuế

| Loại thuế | Mẫu tờ khai phổ biến | Hiện trạng Odoo |
|---|---|---|
| **GTGT (VAT)** — phương pháp khấu trừ | Mẫu 01/GTGT | Cần verify report `l10n_vn` cho version cụ thể; nhiều trường hợp cần custom report theo mẫu mới nhất của Tổng cục Thuế |
| **GTGT** — phương pháp trực tiếp | Mẫu 04/GTGT | Thường ít được hỗ trợ sẵn — khả năng cao là Gap |
| **TNDN (thuế TNDN tạm tính/quyết toán)** | Mẫu 03/TNDN | Thường cần custom report dựa trên dữ liệu kế toán |
| **TNCN (thuế TNCN từ lương)** | Tờ khai khấu trừ TNCN | Liên quan Payroll — xem `odoo-app-feature-matrix.md` mục HR (Payroll thường cần custom cho VN) |
| **Báo cáo tình hình sử dụng hóa đơn** | Mẫu BC26/HĐĐT (qua hệ thống HĐĐT, không qua Odoo) | Thường do nhà cung cấp HĐĐT tự nộp thay |

**Khuyến nghị PreSale:** Liệt kê **đúng các mẫu báo cáo thuế khách thực sự cần nộp định kỳ** trong Discovery (`presales-discovery-questionnaire.md` mục 2.5), sau đó xác nhận mẫu nào Odoo có sẵn vs cần custom report (`report-patterns.md`) — đưa vào bảng Fit-Gap như các dòng riêng biệt.

---

## 5. Lưu trữ chứng từ điện tử & Chữ ký số

- **Luật Kế toán 2015**: quy định thời hạn lưu trữ chứng từ kế toán (tối thiểu 5 năm, 10 năm, hoặc vĩnh viễn tùy loại tài liệu).
- **Chữ ký số**: theo khung pháp lý về chữ ký số và dịch vụ chứng thực chữ ký số — hóa đơn điện tử và một số chứng từ cần ký số hợp lệ. Việc ký số thường do **hệ thống HĐĐT** xử lý (không phải Odoo) — Odoo chỉ cần lưu trữ/tham chiếu file đã ký.
- App `Documents` (Enterprise) hoặc `attachment-binary-patterns.md` (Community) có thể dùng để lưu trữ chứng từ điện tử có cấu trúc, gắn với từng giao dịch kế toán.

---

## 6. Bảo vệ dữ liệu cá nhân (liên quan khi tư vấn Cloud/Hosting)

- **Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân** (hiệu lực từ 01/07/2023) — ảnh hưởng đến cách lưu trữ/xử lý dữ liệu cá nhân của khách hàng, nhân viên (HR module), đối tác.
- Khi tư vấn **Odoo Online/Odoo.sh** (hosting nước ngoài) cho khách hàng có dữ liệu nhạy cảm (HR, khách hàng cá nhân), cần lưu ý:
  - Một số ngành/khách hàng (đặc biệt khối tài chính, y tế, hoặc DNNN) có thể yêu cầu **lưu trữ dữ liệu trong lãnh thổ VN** → ảnh hưởng đến lựa chọn **on-premise/private cloud tại VN** thay vì Odoo Online/Odoo.sh.
  - Xem thêm `odoo-licensing-deployment-guide.md` mục về data residency.
- Đây không phải vấn đề riêng của Odoo — áp dụng cho mọi giải pháp SaaS nước ngoài, nhưng PreSale nên **chủ động nêu** để xây dựng niềm tin.

---

## 7. FAQ thường gặp & gợi ý trả lời

| Câu hỏi của khách | Gợi ý trả lời |
|---|---|
| "Odoo có xuất hóa đơn điện tử theo chuẩn VN không?" | "Odoo sẽ được tích hợp với nhà cung cấp HĐĐT [MISA/Viettel/VNPT...] mà công ty đang dùng — đảm bảo tuân thủ NĐ123/TT78." |
| "Hệ thống tài khoản có đúng theo TT200 không?" | "Có, Odoo có sẵn Chart of Accounts theo TT200/TT133 cho VN, và có thể tùy chỉnh thêm theo thói quen của kế toán." |
| "Báo cáo thuế GTGT có tự động không?" | "Cần xác nhận mẫu báo cáo cụ thể — phần lớn dữ liệu lấy tự động từ sổ sách Odoo, nhưng layout theo mẫu mới nhất của Tổng cục Thuế có thể cần custom report (đã đưa vào báo giá nếu có)." |
| "Dữ liệu công ty có lưu ở VN không?" | Tùy phương án triển khai — xem `odoo-licensing-deployment-guide.md`. On-premise/private cloud VN có thể đáp ứng yêu cầu lưu trữ nội địa. |
| "Phần mềm nước ngoài, có ai support tiếng Việt không?" | Trả lời theo năng lực thực tế của đối tác triển khai (đội ngũ local support) — không phải câu hỏi về Odoo mà về đối tác. |

---

## 8. Checklist xác minh kỹ thuật trước khi cam kết

- [ ] Đã xác nhận `l10n_vn` cho **đúng version Odoo** của khách có CoA theo TT200/TT133 cập nhật (qua `github-verification-guide.md`)
- [ ] Đã liệt kê **nhà cung cấp HĐĐT hiện tại của khách** và xác nhận chưa có/đã có connector sẵn (Community/Enterprise/OCA)
- [ ] Đã liệt kê **các mẫu báo cáo thuế** khách bắt buộc nộp định kỳ và đối chiếu với report có sẵn trong `l10n_vn`
- [ ] Đã hỏi khách về **yêu cầu data residency** (nếu là DNNN/tài chính/y tế) → ảnh hưởng lựa chọn hosting
- [ ] Đã ghi rõ trong Proposal: phần nào là **Fit (kế toán nền tảng)**, phần nào là **Gap-Integration (HĐĐT, báo cáo thuế đặc thù)** với effort riêng

---

## Liên kết

- Tích hợp HĐĐT, ngân hàng, thanh toán, vận chuyển: `skills/vietnam-integration-landscape.md`
- Hosting & data residency: `skills/odoo-licensing-deployment-guide.md`
- Cách verify source code Odoo theo version: `skills/github-verification-guide.md`
- Đưa vào Fit-Gap: `skills/presales-fit-gap-analysis-guide.md`
- Pattern kỹ thuật accounting/tax: `skills/accounting-patterns.md`, `skills/tax-fiscal-patterns.md`
