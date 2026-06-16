---
name: presales-effort-estimation-guide
keywords: [presales, effort estimation, costing, man-day, rate card, uoc luong, chi phi]
description: Bảng benchmark man-day cho các hạng mục triển khai/customization Odoo phổ biến, giúp PreSale tự ước lượng effort/chi phí mà không cần hỏi dev mỗi lần.
odoo_versions: [all]
related_skills: [presales-fit-gap-analysis-guide, presales-proposal-sow-templates, odoo-licensing-deployment-guide, presales-data-migration-scoping-guide]
---

# Presales Effort Estimation Guide

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  EFFORT ESTIMATION BENCHMARK                                                  ║
║  Bảng Fit-Gap → Man-day → Rate Card → Giá báo khách                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này cung cấp **benchmark man-day** cho các hạng mục triển khai/customization Odoo phổ biến nhất, giúp PreSale tự điền nhanh cột "Effort" trong bảng Fit-Gap (`presales-fit-gap-analysis-guide.md`) mà không cần hỏi Technical Lead/Dev cho từng dòng — chỉ cần escalate khi gặp hạng mục nằm ngoài bảng hoặc có độ phức tạp bất thường.

> ⚠️ **Đây là benchmark tham khảo, KHÔNG phải số liệu cố định.** Mỗi công ty/team có năng suất khác nhau (kinh nghiệm, codebase nội bộ sẵn có, mức độ tái sử dụng module). Dùng số liệu này làm điểm khởi đầu, sau đó **điều chỉnh theo dữ liệu thực tế** của team (xem Mục 1) — và luôn để Technical Lead xác nhận lại trước khi chốt giá trong Proposal/SOW.

---

## 1. Cách dùng bảng benchmark này

- **Đơn vị "man-day"**: 1 man-day = 1 ngày làm việc (8 giờ) của **1 Functional Consultant hoặc Developer** ở mức năng suất trung bình. Không tính thời gian chờ (khách phản hồi chậm, chờ duyệt...) — phần này xử lý ở Mục 6 và 8.
- **Khi nào dùng**: ngay sau buổi Fit-Gap Workshop, với mỗi dòng được đánh giá là 🔧 Partial, 🛠️ Gap-Custom hoặc 🔌 Gap-Integration — tra bảng tương ứng (Mục 2-5) để điền range vào cột "Effort (man-day)" của bảng Fit-Gap.
- **Range vs số cụ thể**: ở giai đoạn Fit-Gap, luôn dùng **range** (vd "2-4 man-day"), không chốt số lẻ. Số cụ thể chỉ chốt sau khi Technical Lead review lại scope chi tiết.
- **Calibrate theo team thực tế**: sau mỗi dự án, so sánh effort benchmark vs effort thực tế đã log (timesheet) → điều chỉnh dần bảng này cho phù hợp với năng suất team mình. Một team có sẵn nhiều module/library tái sử dụng có thể nhanh hơn benchmark 20-30%; một team mới làm Odoo lần đầu có thể chậm hơn 20-30%.
- **Không cộng dồn máy móc**: tổng effort của 1 dự án không phải lúc nào cũng = tổng effort từng dòng cộng lại — một số hạng mục có thể làm song song (nhiều consultant), một số có dependency (phải xong cấu hình mới custom được). Dùng số tổng để **ước lượng chi phí**, nhưng timeline thực tế cần lập kế hoạch (planning) riêng.

---

## 2. Cấu hình & Setup (Configuration)

Các hạng mục **không cần viết code**, chỉ cấu hình qua giao diện Odoo (Settings, Studio nếu có Enterprise).

| Hạng mục | Man-day | Ghi chú |
|---|---|---|
| Setup công ty, users, phân quyền cơ bản | 1-2 | Tạo company, users, groups, basic access rights |
| Cấu hình 1 module chuẩn (Sales/Purchase/Inventory/Project cơ bản) | 2-5 mỗi module | Tùy số lượng quy trình con cần cấu hình (vd Inventory với nhiều warehouse/route sẽ ở mức cao của range) |
| Cấu hình kế toán (CoA, thuế, ngân hàng, phương thức thanh toán) | 3-7 | Bao gồm setup Chart of Accounts theo `l10n` VN, thuế GTGT, journal, phương thức thanh toán |
| Import master data (KH/NCC/SP) qua file Excel chuẩn, dữ liệu sạch | 1-3 | Giả định khách đã chuẩn hóa data theo template import của Odoo — nếu data chưa sạch, xem Mục 5 (Data Migration) |
| Cấu hình bảng giá/chiết khấu nhiều cấp | 1-3 | Pricelist theo nhóm KH, chiết khấu theo số lượng (bậc thang) |
| Setup multi-company (mỗi công ty thêm) | 1-2 | Tính thêm cho mỗi company **bổ sung** sau company đầu tiên — bao gồm intercompany rules cơ bản nếu cần (`multi-company-patterns.md`) |

---

## 3. Customization — Code mới

Các hạng mục **cần viết code** (Python/XML/JS/QWeb). Effort giả định đã có **Functional Spec rõ ràng** từ bảng Fit-Gap — nếu yêu cầu còn mơ hồ, áp thêm hệ số ở Mục 7.

| Hạng mục | Man-day | Ghi chú |
|---|---|---|
| Thêm field đơn giản + hiển thị trên view | 0.25-0.5 | 1 field, không có logic onchange/compute phức tạp |
| Custom view (form/list/kanban) phức tạp, nhiều logic invisible/readonly | 0.5-1.5 | Nhiều điều kiện `invisible`/`readonly` theo state, custom button với logic |
| Custom QWeb report đơn giản (1 bảng, ít tính toán) | 1-2 | Vd: phiếu xuất kho, đơn hàng — 1 layout, không có subtotal nhiều cấp |
| Custom QWeb report phức tạp (nhiều bảng, subtotal, đa cấp) | 3-5 | Vd: báo cáo công nợ theo tuổi nợ, báo cáo tổng hợp nhiều dòng/nhóm với subtotal |
| Model mới đơn giản (1-2 field, basic CRUD, 1 view) | 2-4 | Bao gồm security (`ir.model.access.csv`), 1 menu, 1 view cơ bản |
| Model mới phức tạp (nhiều quan hệ, computed fields, constraints, full views+security) | 5-10 | Nhiều `One2many`/`Many2many`, computed fields có dependency phức tạp, constraints, đầy đủ form/list/search view + security groups |
| Custom workflow/state machine + approval nhiều cấp | 3-7 | State machine với nhiều transition, mỗi cấp duyệt có logic/permission riêng (`workflow-state-patterns.md`) |
| Automated email/notification template | 0.5-1 | Mail template + automation rule trigger gửi email |
| Dashboard/KPI tùy chỉnh (Spreadsheet/Studio hoặc custom) | 2-5 | Phụ thuộc số lượng KPI, độ phức tạp truy vấn data, custom widget nếu cần (`dashboard-kpi-patterns.md`) |
| Cron job / scheduled action | 1-2 | Bao gồm xử lý logic, logging, error handling cơ bản |
| OWL component/widget tùy chỉnh | 3-6 | Component JS/OWL có state riêng, tương tác 2 chiều với form (`odoo-owl-components-{version}.md`) |

---

## 4. Tích hợp 3rd-party (Integration)

Effort phụ thuộc rất nhiều vào **chất lượng tài liệu API của bên thứ 3** và **độ đồng bộ 2 chiều**. Đây là nhóm hạng mục có rủi ro vượt effort cao nhất — luôn dành buffer riêng (xem Mục 8).

| Mức độ | Man-day | Đặc điểm |
|---|---|---|
| Đơn giản | 5-8 | REST API tài liệu tốt, 1 chiều, ít loại dữ liệu (vd gửi email/SMS qua API) |
| Trung bình | 10-15 | 2 chiều, mapping data nhiều field, có lỗi/edge case cần xử lý (vd đồng bộ đơn hàng sàn TMĐT) |
| Phức tạp | 20-40+ | Không có API chuẩn, cần middleware, real-time sync, hoặc đối tác chậm phản hồi tài liệu (vd 1 số ngân hàng, ERP legacy) |
| Hóa đơn điện tử VN (theo `l10n-vietnam-compliance-guide.md`) | 8-15 | Tùy nhà cung cấp (MISA/Viettel/VNPT...) và số loại hóa đơn (bán, điều chỉnh, thay thế, hủy) |

> **Tham chiếu**: dùng `vietnam-integration-landscape.md` để tra danh sách tích hợp phổ biến tại VN (sàn TMĐT, e-invoice, ngân hàng, Zalo...) và tier độ phức tạp tương ứng — giúp xác định nhanh nên xếp 1 yêu cầu tích hợp vào mức nào trong bảng trên.

---

## 5. Data Migration

| Khối lượng / Độ phức tạp | Man-day |
|---|---|
| < 5,000 bản ghi, 1 nguồn, dữ liệu sạch | 2-3 |
| 5,000-50,000 bản ghi hoặc 2-3 nguồn cần merge | 5-10 |
| > 50,000 bản ghi, hoặc nhiều nguồn không đồng nhất, dữ liệu cần làm sạch nhiều | 15-30+ |

> **Tham chiếu chi tiết**: `presales-data-migration-scoping-guide.md` — đặc biệt với các trường hợp cần merge nhiều nguồn (vd Excel + Misa + phần mềm bán hàng cũ) hoặc dữ liệu lịch sử (giao dịch, công nợ) cần đối chiếu số dư.

---

## 6. Testing, Training, Project Management (overhead)

Các hạng mục này **không nằm trong bảng Fit-Gap theo từng dòng** mà tính trên **tổng effort của cả nhóm Customization + Integration** (Mục 3 + Mục 4):

| Hạng mục | Cách tính |
|---|---|
| UAT support (sau khi build xong) | ~15% tổng effort phần Customization + Integration |
| Đào tạo người dùng | 0.5-1 ngày / nhóm người dùng / module |
| PM, họp, tài liệu | ~10-15% tổng effort toàn dự án |

> Lưu ý: "Đào tạo người dùng" tính theo **nhóm người dùng** (vd nhóm Sales, nhóm Kho, nhóm Kế toán), không tính theo đầu người — 1 buổi đào tạo có thể cho cả nhóm.

---

## 7. Hệ số điều chỉnh (Multipliers)

Sau khi cộng tổng effort từ Mục 2-6, áp các hệ số sau **nếu** dự án rơi vào tình huống tương ứng (có thể áp **nhiều hệ số cùng lúc**, nhân dồn):

| Tình huống | Hệ số |
|---|---|
| Yêu cầu chưa rõ ràng / khả năng thay đổi cao | x1.3-1.5 |
| Version Odoo rất mới (v19+, ít tài liệu/cộng đồng) | x1.1-1.2 |
| Team chưa có kinh nghiệm với domain nghiệp vụ cụ thể (vd ngành dược, GDP/GSP) | x1.2 |
| Khách yêu cầu tài liệu/quy trình bài bản (DNNN, ISO) | x1.1-1.3 |

> **Ví dụ**: 1 hạng mục custom có effort gốc 6 man-day, yêu cầu chưa rõ ràng (x1.4) + khách là DNNN cần tài liệu bài bản (x1.2) → effort điều chỉnh = 6 × 1.4 × 1.2 ≈ **10 man-day**.

---

## 8. Buffer / Risk Contingency

Sau khi đã áp hệ số điều chỉnh ở Mục 7, **cộng thêm 15-20% buffer trên TỔNG effort** của toàn dự án trước khi quy ra giá.

- Buffer này dùng để xử lý các phát sinh không lường trước được (bug phát sinh khi tích hợp, yêu cầu nhỏ phát sinh trong quá trình UAT, thời gian chờ phản hồi...).
- **KHÔNG** thông báo riêng buffer này cho khách hàng — đưa thẳng vào giá tổng (không tách thành 1 dòng "Buffer/Contingency" riêng trong Proposal, vì dễ bị khách yêu cầu cắt bỏ).
- Nếu dự án có nhiều hạng mục Integration phức tạp (Mục 4, mức "Phức tạp") hoặc data migration lớn (Mục 5, > 50,000 bản ghi), cân nhắc lấy buffer ở mức cao của range (20%) do rủi ro vượt effort ở các nhóm này thường cao hơn.

---

## 9. Quy đổi Effort → Giá (Rate Card mẫu)

Sau khi có tổng effort (đã áp hệ số + buffer), quy đổi sang giá bằng rate card theo vai trò. Bảng dưới là **template** — công ty tự điền rate theo thị trường/chính sách giá riêng:

| Vai trò | Rate (VNĐ/man-day hoặc USD/man-day) |
|---|---|
| Functional Consultant (Senior) | {điền theo công ty} |
| Functional Consultant (Junior) | {điền theo công ty} |
| Technical Developer (Senior) | {điền theo công ty} |
| Technical Developer (Junior) | {điền theo công ty} |
| Project Manager | {điền theo công ty} |

**Công thức tổng quát:**

```
Tổng giá = Σ (effort theo từng hạng mục × rate theo vai trò phù hợp) × (1 + buffer%)
```

Trong đó:
- "Effort theo từng hạng mục" lấy từ bảng Fit-Gap đã điền theo Mục 2-6, sau khi áp hệ số Mục 7.
- "Rate theo vai trò phù hợp" — phân loại hạng mục nào do Functional Consultant làm (cấu hình, training, UAT support), hạng mục nào do Developer làm (customization, integration), hạng mục nào do PM phụ trách (overhead PM).
- "Buffer%" lấy từ Mục 8 (15-20%), áp 1 lần trên tổng (không áp lặp lại nếu đã áp ở bước tính effort).

---

## Liên kết

- Nguồn input cho bảng này: `presales-fit-gap-analysis-guide.md` — mỗi dòng Gap/Partial trong Fit-Gap được tra effort tại đây.
- Bước tiếp theo sau khi có tổng effort/giá: `presales-proposal-sow-templates.md`.
- Chi phí license (ảnh hưởng tổng giá ngoài effort): `odoo-licensing-deployment-guide.md`.
- Chi tiết riêng cho hạng mục Data Migration: `presales-data-migration-scoping-guide.md`.
- Tích hợp phổ biến tại VN và tier độ phức tạp: `vietnam-integration-landscape.md`.
