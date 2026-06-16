---
name: odoo-app-feature-matrix
keywords: [presales, odoo apps, feature matrix, community, enterprise, solution mapping, fit-gap, modules]
description: Danh mục đầy đủ các Apps của Odoo - vấn đề giải quyết, Community/Enterprise, app liên quan, skill kỹ thuật tương ứng. Tài liệu NỀN TẢNG để map yêu cầu khách hàng sang giải pháp Odoo.
odoo_versions: [all]
related_skills: [odoo-editions, presales-fit-gap-analysis-guide, presales-discovery-questionnaire, presales-industry-solution-templates, presales-effort-estimation-guide]
---

# Odoo App Feature Matrix (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  ODOO APP FEATURE MATRIX                                                      ║
║  "Khách nói X → Odoo App nào giải quyết, Community hay Enterprise?"           ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Đây là tài liệu **nền tảng** cho PreSale: danh mục toàn bộ Apps Odoo, nhóm theo khối nghiệp vụ, kèm Edition (Community/Enterprise), vấn đề giải quyết, và skill kỹ thuật tương ứng (để đội Dev tra khi cần demo sâu hoặc customize).

> **Quy ước Edition:** `C` = có trong Community (miễn phí), `E` = chỉ có ở Enterprise, `C/E` = có ở Community nhưng bản Enterprise có thêm tính năng nâng cao.
>
> **Luôn verify lại** tình trạng Edition/tính năng theo đúng version Odoo của khách (xem `skills/odoo-editions.md` và `skills/odoo-version-knowledge-{version}.md`) — danh sách App của Odoo thay đổi qua từng năm.

---

## 1. Sales & Marketing

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **CRM** | C | Quản lý lead/cơ hội, pipeline bán hàng, dự báo doanh số | Kanban pipeline, lead scoring, activity scheduling, email tích hợp, dự báo (forecast) | Sales, Email Marketing | `sale-crm-patterns.md` |
| **Sales** | C | Báo giá, đơn hàng, hợp đồng bán hàng | Quotation builder, e-signature trên báo giá, upsell/cross-sell, online payment | CRM, Invoicing, Inventory | `sale-crm-patterns.md` |
| **Point of Sale (POS)** | C | Bán lẻ tại quầy, nhà hàng | Giao diện chạm, offline mode, nhiều phương thức thanh toán, kết nối máy in/cân điện tử | Inventory, Accounting, Restaurant | *(chưa có skill riêng)* |
| **Subscriptions** | E | Hợp đồng định kỳ, recurring billing | Tự động gia hạn/billing, MRR/churn dashboard, upsell hợp đồng | Sales, Accounting | *(chưa có skill riêng)* |
| **Rental** | E | Cho thuê sản phẩm/thiết bị theo thời gian | Lịch cho thuê, tính giá theo thời gian, phiếu giao/nhận | Sales, Inventory | *(chưa có skill riêng)* |
| **Email Marketing** | C | Gửi chiến dịch email hàng loạt | Drag-drop email builder, A/B testing, thống kê mở/click | CRM, Marketing Automation | *(chưa có skill riêng)* |
| **SMS Marketing** | E | Gửi SMS hàng loạt | Template SMS, lịch gửi, thống kê | Email Marketing | *(chưa có skill riêng)* |
| **Events** | C | Tổ chức sự kiện, bán vé | Trang sự kiện online, quản lý đăng ký, check-in QR | Website, Email Marketing | *(chưa có skill riêng)* |
| **Marketing Automation** | E | Kịch bản marketing tự động (drip campaign) | Workflow visual theo hành vi KH, target theo segment | CRM, Email/SMS Marketing | *(chưa có skill riêng)* |
| **Social Marketing** | E | Quản lý mạng xã hội (Facebook, Instagram, LinkedIn...) | Lên lịch đăng bài, theo dõi tương tác | Website | *(chưa có skill riêng)* |
| **Surveys** | C | Khảo sát, đánh giá, quiz | Builder kéo-thả, chấm điểm tự động, certification | Email Marketing, Website | *(chưa có skill riêng)* |

---

## 2. Operations / Supply Chain

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Inventory** | C/E | Quản lý kho, xuất nhập tồn, vận chuyển nội bộ | Multi-warehouse, routes (push/pull), nhiều bước giao nhận, FIFO/FEFO | Sales, Purchase, MRP | `stock-inventory-patterns.md` |
| **Barcode** | E | Thao tác kho bằng máy quét mã vạch | Giao diện quét cho nhập/xuất/kiểm kê, hoạt động trên mobile | Inventory, MRP | `stock-inventory-patterns.md` (1 phần) |
| **Purchase** | C | Mua hàng, RFQ, so sánh báo giá NCC | Purchase agreement, 3-way matching (PO/Receipt/Invoice), lead time NCC | Inventory, Accounting | `purchase-procurement-patterns.md` |
| **Lot/Serial Tracking** | C (trong Inventory) | Truy xuất nguồn gốc theo lô/số seri, hạn sử dụng (FEFO) | Traceability report, expiration alerts | Inventory, MRP, Quality | `lot-serial-patterns.md` |
| **Maintenance** | C | Bảo trì thiết bị/máy móc | Lịch bảo trì định kỳ, yêu cầu sửa chữa, kanban trạng thái thiết bị | Manufacturing, Fleet | *(chưa có skill riêng)* |
| **Repairs** | C | Quản lý sửa chữa sản phẩm trả về | Phiếu sửa chữa, link với bảo hành | Inventory, Sales | *(chưa có skill riêng)* |
| **Field Service** | E | Quản lý đội kỹ thuật hiện trường | Lịch điều phối, app mobile cho kỹ thuật viên, báo cáo công việc + chữ ký KH | Project, Inventory, Sales | *(chưa có skill riêng)* |

---

## 3. Manufacturing

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Manufacturing (MRP)** | C/E | Sản xuất theo BOM, lệnh sản xuất | Multi-level BOM, work orders, sản xuất theo công đoạn (routing) | Inventory, Quality, PLM | `stock-inventory-patterns.md` (liên quan), *(MRP riêng: chưa có)* |
| **PLM** | E | Quản lý vòng đời sản phẩm, thay đổi kỹ thuật (ECO) | Version BOM, Engineering Change Orders, so sánh phiên bản | Manufacturing | *(chưa có skill riêng)* |
| **Quality** | E | Kiểm tra chất lượng (QC) trong sản xuất/nhập kho | Quality checkpoints, phiếu kiểm tra, biểu đồ kiểm soát (SPC) | Manufacturing, Inventory | *(chưa có skill riêng)* |
| **Subcontracting** | C/E (trong MRP) | Gia công ngoài (đưa NVL cho NCC gia công) | Tự động tạo phiếu giao NVL + nhận thành phẩm | Manufacturing, Purchase | *(chưa có skill riêng)* |

---

## 4. Finance

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Invoicing** | C | Xuất hóa đơn, theo dõi công nợ cơ bản | Hóa đơn bán/mua, thanh toán online, nhắc nợ | Sales, Purchase | `accounting-patterns.md` |
| **Accounting** | E | Kế toán đầy đủ (sổ cái, BCTC, ngân hàng, tài sản) | Bank reconciliation tự động, multi-currency, consolidation, asset/budget | Invoicing, Sales, Purchase, HR | `accounting-patterns.md`, `tax-fiscal-patterns.md` |
| **Expenses** | C | Quản lý chi phí nhân viên | Quét hóa đơn (OCR), workflow duyệt, hoàn ứng | Accounting, HR | *(chưa có skill riêng)* |
| **Documents** | E | Quản lý tài liệu/chứng từ tập trung | Workflow duyệt tài liệu, OCR, tích hợp với mọi module (hóa đơn, hợp đồng, hồ sơ NV) | Accounting, Sign, HR | `attachment-binary-patterns.md` |
| **Sign** | E | Ký điện tử hợp đồng/tài liệu | Gửi ký nhiều bên, audit trail, template chữ ký | Sales, Documents, HR | *(chưa có skill riêng)* |
| **Spreadsheet / Dashboards** | E | BI nội bộ, báo cáo động dạng spreadsheet | Pivot/Chart kết nối live data, dashboard tổng hợp nhiều app | Tất cả | `dashboard-kpi-patterns.md` |

> 💡 **Lưu ý VN:** Phần kế toán/thuế VN (chart of accounts TT200/TT133, hóa đơn điện tử) xem chi tiết tại `l10n-vietnam-compliance-guide.md`.

---

## 5. Human Resources

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Employees** | C | Hồ sơ nhân viên, sơ đồ tổ chức | Org chart, hợp đồng lao động, tài liệu nhân sự | Recruitment, Time Off, Payroll | `hr-employee-patterns.md` |
| **Recruitment** | C | Tuyển dụng | Kanban ứng viên theo vòng phỏng vấn, đăng tin tuyển dụng lên website | Employees, Website | `hr-employee-patterns.md` |
| **Time Off** | C | Quản lý nghỉ phép | Workflow duyệt, quy tắc phép theo thâm niên, lịch nghỉ team | Employees, Attendances | `hr-employee-patterns.md` |
| **Attendances** | C | Chấm công | Check-in/out qua kiosk, mobile, hoặc thiết bị (qua IoT) | Employees, Payroll | `hr-employee-patterns.md` |
| **Appraisals** | E | Đánh giá hiệu suất nhân viên | Chu kỳ đánh giá, 360-degree feedback, mục tiêu (goals) | Employees | `hr-employee-patterns.md` |
| **Referrals** | C | Chương trình giới thiệu nhân viên | Gamification, theo dõi điểm thưởng | Recruitment | *(chưa có skill riêng)* |
| **Fleet** | C | Quản lý đội xe công ty | Chi phí xe, bảo hiểm/đăng kiểm, gán xe cho nhân viên | Maintenance, Expenses | *(chưa có skill riêng)* |
| **Payroll** | E (theo quốc gia) | Tính lương | Quy tắc lương theo luật từng nước (cần kiểm tra `l10n` cho VN) | Employees, Accounting | *(chưa có skill riêng — VN payroll thường cần custom, xem F1)* |
| **Approvals** | C | Quy trình phê duyệt nội bộ chung (không chỉ HR) | Tạo loại đơn phê duyệt tùy ý (mua sắm, công tác...), nhiều cấp duyệt | Tất cả | `workflow-state-patterns.md` |

---

## 6. Services & Project

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Project** | C | Quản lý dự án, công việc | Kanban/Gantt, milestone, dự án con, cộng tác qua chatter | Timesheets, Sales, HR | `project-task-patterns.md` |
| **Timesheets** | C | Chấm công theo dự án/task | Ghi nhận giờ làm, đối chiếu với hợp đồng (billable) | Project, HR, Sales (invoicing theo timesheet) | `project-task-patterns.md` |
| **Helpdesk** | E | Quản lý ticket hỗ trợ khách hàng | SLA policy, knowledge base, đa kênh (email/portal/live chat) | Project, Field Service | *(chưa có skill riêng)* |
| **Planning** | E | Lập lịch/phân ca nhân sự | Kéo-thả lịch làm việc, gửi lịch cho nhân viên, theo template tuần | HR, Project, Field Service | *(chưa có skill riêng)* |
| **Knowledge** | E | Wiki nội bộ, SOP | Editor dạng Notion, nhúng vào các record khác | Project, Helpdesk | *(chưa có skill riêng)* |

---

## 7. Productivity & Website

| App | Edition | Vấn đề giải quyết | Tính năng nổi bật | App liên quan | Skill kỹ thuật |
|---|---|---|---|---|---|
| **Website** | C | Website công ty, landing page | Page builder kéo-thả, SEO, multi-website, multi-ngôn ngữ | eCommerce, Blog, CRM (form liên hệ → lead) | `website-integration-patterns.md` |
| **eCommerce** | C/E | Bán hàng online | Giỏ hàng, khuyến mãi, tích hợp Inventory/Accounting | Website, Sales, Inventory | `website-integration-patterns.md` |
| **Blog / Forum / eLearning / Live Chat** | C | Nội dung, cộng đồng, hỗ trợ trực tuyến trên web | Tích hợp sẵn với Website | Website | `website-integration-patterns.md` |
| **Discuss** | C | Chat nội bộ + email gateway | Kênh chat, video call, tích hợp thông báo từ mọi module | Tất cả | `mail-notification-patterns.md` |
| **Contacts** | C | Sổ địa chỉ KH/NCC/nhân viên dùng chung | 360-degree view 1 đối tác, phân loại tag | Tất cả | *(core - res.partner)* |
| **Calendar** | C | Lịch dùng chung, đặt lịch hẹn | Đồng bộ Google/Outlook, đặt lịch online (appointment) | CRM, Project, HR | *(chưa có skill riêng)* |
| **Studio** | E | Tùy biến không cần code | Tạo field/view/automation/report bằng kéo-thả | Tất cả | xem `odoo-editions.md` |
| **Sign** | E | (xem mục Finance) | | | |
| **IoT** | E | Kết nối thiết bị phần cứng (máy in, cân, đầu đọc thẻ...) | IoT Box, driver cho thiết bị phổ biến | POS, Inventory, Manufacturing | *(chưa có skill riêng)* |
| **VoIP** | E | Gọi điện trực tiếp từ Odoo | Click-to-call, ghi log cuộc gọi vào CRM | CRM, Helpdesk | *(chưa có skill riêng)* |
| **WhatsApp** | E | Nhắn tin/thông báo qua WhatsApp Business API | Template message, 2 chiều với khách hàng | CRM, Sales, Helpdesk | *(chưa có skill riêng — với VN thường thay bằng Zalo, xem `vietnam-integration-landscape.md`)* |

---

## 8. Mapping ngược: "Khách nói X → Odoo App nào?"

Dùng bảng này khi PreSale ghi chép Discovery Notes và cần tra nhanh "Odoo có cái này không":

| Khách hàng nói... | Odoo App / Tính năng |
|---|---|
| "Quản lý hàng theo lô, hạn sử dụng (FEFO)" | Inventory + Lot/Serial Tracking |
| "Khách đặt hàng online, đồng bộ tồn kho" | Website + eCommerce + Inventory |
| "Ký hợp đồng online, không cần in giấy" | Sign |
| "Thu tiền theo gói thuê bao hàng tháng" | Subscriptions |
| "Cho thuê thiết bị theo ngày/giờ" | Rental |
| "Đội kỹ thuật đi bảo trì tận nơi, chụp ảnh, khách ký xác nhận" | Field Service |
| "Quản lý ticket bảo hành/hỗ trợ KH" | Helpdesk |
| "Lập kế hoạch ca làm cho nhân viên cửa hàng" | Planning |
| "Wiki/SOP nội bộ cho nhân viên mới" | Knowledge |
| "Chấm công bằng vân tay/khuôn mặt" | Attendances + IoT (kết nối máy chấm công) |
| "Phê duyệt đề nghị tạm ứng/công tác nhiều cấp" | Approvals |
| "Quản lý đội xe giao hàng, bảo hiểm, đăng kiểm" | Fleet |
| "Sản xuất theo định mức NVL (BOM), nhiều công đoạn" | Manufacturing (MRP) |
| "Kiểm tra chất lượng đầu vào/đầu ra" | Quality |
| "Gia công ngoài cho NCC" | Manufacturing — Subcontracting |
| "Theo dõi cơ hội bán hàng theo phễu (pipeline)" | CRM |
| "Bán hàng tại quầy, có máy in bill, máy quẹt thẻ" | Point of Sale |
| "Quét hóa đơn chi phí nhân viên tự động nhập liệu" | Expenses (OCR) |
| "Báo cáo động, dashboard tổng hợp nhiều phòng ban" | Spreadsheet/Dashboards |
| "Khách muốn tự tạo thêm field/báo cáo không cần dev" | Studio (chỉ Enterprise) |
| "Gửi Zalo/SMS marketing cho khách hàng" | SMS Marketing + xem `vietnam-integration-landscape.md` cho Zalo |

---

## 9. Lưu ý theo version & edition

- Danh sách App **thay đổi theo từng năm** — Odoo có thể đổi tên app, gộp/tách app, hoặc chuyển từ Enterprise sang Community (và ngược lại) giữa các version. **Luôn xác nhận lại** với `skills/odoo-version-knowledge-{version}.md` trước khi cam kết với khách.
- Một số app chỉ thực sự "production-ready" từ một version nhất định (vd Field Service, Knowledge ổn định hơn từ v16+). Nếu khách dùng version cũ (14/15), kiểm tra kỹ trước khi đưa vào đề xuất.
- App "chưa có skill kỹ thuật riêng" trong bảng trên **không có nghĩa là Odoo không hỗ trợ** — chỉ có nghĩa là bộ skill kỹ thuật của workspace này chưa có pattern riêng cho app đó. Khi cần demo/customize sâu, dùng `skills/github-verification-guide.md` để tra trực tiếp source code Odoo cho app đó.
- Khi 1 yêu cầu map vào nhiều App, ưu tiên kiểm tra **App liên quan** trong bảng — phần lớn câu hỏi "có làm được combo X+Y không" đều đã có sẵn trong Odoo nếu 2 app đó vốn tích hợp với nhau (vd Sales ↔ Inventory ↔ Accounting là 1 luồng liền mạch).

---

## Liên kết

- Chi tiết Community vs Enterprise, license, cách check tính năng có sẵn theo module đã cài: `skills/odoo-editions.md`
- Bước tiếp theo sau khi map xong Apps: `skills/presales-fit-gap-analysis-guide.md`
- Blueprint theo ngành (combo App đề xuất sẵn): `skills/presales-industry-solution-templates.md`
