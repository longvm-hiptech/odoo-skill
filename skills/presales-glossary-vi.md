---
name: presales-glossary-vi
keywords: [presales, glossary, tu dien, thuat ngu, terminology, song ngu, anh viet]
description: Từ điển song ngữ Anh-Việt các thuật ngữ Odoo/ERP thường dùng khi tư vấn, giúp giải thích cho khách không rành kỹ thuật và giữ nhất quán thuật ngữ trong tài liệu.
odoo_versions: [all]
related_skills: [odoo-app-feature-matrix, presales-discovery-questionnaire, presales-fit-gap-analysis-guide, presales-proposal-sow-templates]
---

# Từ Điển Thuật Ngữ PreSale Song Ngữ (Anh-Việt)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  PRESALES GLOSSARY (EN-VI)                                                    ║
║  Giữ thuật ngữ NHẤT QUÁN xuyên suốt Discovery → Fit-Gap → Proposal → Demo     ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Đây là tài liệu tra cứu nhanh: mỗi thuật ngữ tiếng Anh thường gặp khi làm presales Odoo, kèm nghĩa tiếng Việt / giải thích ngắn gọn. Mục tiêu là tránh tình trạng mỗi tài liệu (Discovery Notes, Fit-Gap, Proposal, slide demo) dịch một kiểu khác nhau, gây nhầm lẫn cho khách hàng.

---

## 1. Cách dùng

- **Mục tiêu:** giữ thuật ngữ **NHẤT QUÁN** giữa Discovery Notes, Fit-Gap, Proposal, Demo — tránh mỗi tài liệu dịch 1 kiểu gây nhầm lẫn cho khách.
- **Khi giải thích cho khách không rành kỹ thuật:** ưu tiên dùng cột "Nghĩa tiếng Việt / Giải thích ngắn" — diễn đạt bằng ngôn ngữ nghiệp vụ, tránh thuật ngữ kỹ thuật Odoo (model, field...).
- **Khi viết tài liệu kỹ thuật / trao đổi với Dev:** giữ nguyên thuật ngữ tiếng Anh, vì đó là tên field/model/menu **thật** xuất hiện trên giao diện Odoo (UI tiếng Anh) — dịch sang tiếng Việt trong tài liệu kỹ thuật dễ gây hiểu lầm khi đối chiếu với hệ thống thực tế.
- Một thuật ngữ có thể có nhiều cách dịch tùy ngữ cảnh — bảng dưới đây chọn cách dịch **khuyến nghị** để dùng thống nhất; nếu khách hàng đã quen với một cách gọi khác, có thể ghi chú thêm cách gọi đó trong ngoặc ở lần xuất hiện đầu tiên.
- Với các thuật ngữ đã có định nghĩa chi tiết ở skill khác (vd Fit/Gap/MoSCoW trong `presales-fit-gap-analysis-guide.md`), bảng này chỉ tóm tắt ngắn và trỏ link — **không định nghĩa lại** để tránh mâu thuẫn.

---

## 2. Thuật ngữ ERP & Quản lý dự án chung

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Master Data** | Dữ liệu nền/dữ liệu danh mục — thông tin ít thay đổi, dùng làm nền cho các giao dịch (vd: danh mục khách hàng, sản phẩm, NCC, kho, tài khoản kế toán). |
| **Transactional Data** | Dữ liệu giao dịch — phát sinh hàng ngày theo hoạt động kinh doanh (vd: đơn hàng, hóa đơn, phiếu xuất kho). Khác với Master Data ở chỗ số lượng lớn và liên tục thay đổi. |
| **Workflow** | Quy trình làm việc / luồng xử lý — chuỗi các bước/trạng thái mà một chứng từ (đơn hàng, phiếu yêu cầu...) đi qua từ khi tạo đến khi hoàn tất. |
| **Approval** | Phê duyệt — bước yêu cầu một người có thẩm quyền (cấp trên, kế toán trưởng...) xác nhận trước khi chứng từ được tiếp tục xử lý. |
| **Dashboard** | Bảng điều khiển / màn hình tổng quan — tổng hợp số liệu, biểu đồ quan trọng để theo dõi nhanh tình hình kinh doanh. |
| **KPI** | Chỉ số đo lường hiệu quả (Key Performance Indicator) — số liệu dùng để đánh giá hiệu suất công việc/phòng ban (vd: doanh số/tháng, tỷ lệ giao hàng đúng hạn). |
| **Audit Trail** | Lịch sử thay đổi / dấu vết kiểm tra — ghi lại ai đã tạo/sửa/xóa gì, khi nào, để phục vụ kiểm tra/đối chiếu sau này. Trong Odoo thể hiện qua Chatter (log hoạt động) và mail.tracking trên field. |
| **Multi-company** | Đa công ty — một hệ thống Odoo quản lý nhiều pháp nhân/công ty con, có thể chia sẻ hoặc tách biệt dữ liệu tùy cấu hình. Xem thêm `multi-company-patterns.md`. |
| **Role / Permission** | Vai trò / quyền hạn — xác định một người dùng được xem/tạo/sửa/xóa những gì trong hệ thống. Trong Odoo cấu hình qua Groups (nhóm quyền) và Access Rights. |
| **Module** | Phân hệ / module — gói chức năng có thể cài thêm vào Odoo (vd: module Sales, module Kế toán). Tương đương "App" khi nói với khách không rành kỹ thuật. |
| **Configuration** | Cấu hình — thiết lập hệ thống bằng các tùy chọn có sẵn (bật/tắt tính năng, thiết lập thông số), **không cần viết code**. Rẻ và nhanh hơn Customization rất nhiều. |
| **Customization** | Tùy biến / lập trình thêm — viết code mới (module, field, report, logic) để đáp ứng yêu cầu mà cấu hình chuẩn không làm được. Xem thêm phân loại Gap trong `presales-fit-gap-analysis-guide.md`. |
| **Go-live** | Ngày vận hành chính thức — thời điểm hệ thống mới chính thức được dùng thay cho hệ thống/quy trình cũ trong môi trường thực tế (Production). |
| **UAT (User Acceptance Testing)** | Kiểm thử nghiệm thu — giai đoạn người dùng cuối phía khách hàng tự tay kiểm tra hệ thống theo kịch bản thực tế trước khi đồng ý go-live. |
| **Sandbox / Staging** | Môi trường thử nghiệm — bản sao của hệ thống dùng để test, demo, đào tạo mà không ảnh hưởng đến dữ liệu thật. |
| **Production** | Môi trường vận hành chính thức — hệ thống thật đang được công ty khách hàng sử dụng hàng ngày, dữ liệu là dữ liệu thật. |
| **Cutover** | Chuyển đổi/chuyển giao hệ thống — giai đoạn ngắn (thường vài ngày) chuyển từ hệ thống cũ sang hệ thống mới: khóa sổ hệ thống cũ, nhập liệu số dư đầu kỳ, chuyển dữ liệu, và go-live. |
| **SLA (Service Level Agreement)** | Cam kết mức độ dịch vụ — thỏa thuận về thời gian phản hồi/xử lý sự cố, thời gian bảo hành, uptime hệ thống... |
| **Subscription** | Thuê bao / hợp đồng định kỳ — mô hình thu phí lặp lại theo chu kỳ (tháng/năm), thường dùng cho phí license Odoo Enterprise hoặc dịch vụ bảo trì. |
| **On-premise** | Tự lưu trữ tại chỗ — hệ thống cài đặt và chạy trên server riêng của công ty khách hàng (tự quản lý hạ tầng). |
| **Cloud (SaaS / Hosting)** | Trên nền tảng đám mây — hệ thống chạy trên server do Odoo hoặc bên thứ ba quản lý, khách hàng truy cập qua Internet, không cần tự quản lý hạ tầng. |

---

## 3. Sales & CRM

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Lead** | Đầu mối / khách hàng tiềm năng (sơ cấp) — thông tin liên hệ ban đầu, chưa xác định rõ nhu cầu/khả năng mua hàng. Trong CRM, Lead có thể được "convert" (chuyển đổi) thành Opportunity. |
| **Opportunity** | Cơ hội bán hàng — Lead đã được xác nhận có nhu cầu thực sự và đang trong quá trình theo đuổi để chốt deal, gắn với giai đoạn (stage) trong Pipeline. |
| **Pipeline** | Phễu bán hàng — toàn bộ các Opportunity được sắp xếp theo các giai đoạn (Mới → Đủ điều kiện → Đề xuất → Đàm phán → Chốt), thường hiển thị dạng Kanban. |
| **Quotation** | Báo giá — chứng từ gửi cho khách hàng đề xuất giá bán cho sản phẩm/dịch vụ, chưa phải là đơn hàng chính thức. |
| **Sales Order (SO)** | Đơn hàng bán — Quotation sau khi được khách hàng xác nhận (đồng ý mua), trở thành cam kết bán hàng chính thức và có thể tiếp tục giao hàng/xuất hóa đơn. |
| **Quotation Template** | Mẫu báo giá — bộ khung báo giá soạn sẵn (sản phẩm, điều khoản, ghi chú) để tạo báo giá nhanh cho các trường hợp lặp lại. |
| **Sales Team** | Đội bán hàng — nhóm nhân viên kinh doanh được tổ chức theo khu vực/dòng sản phẩm/kênh bán, mỗi đội có thể có mục tiêu doanh số riêng. |
| **Customer / Contact** | Khách hàng / Liên hệ — thực thể (cá nhân hoặc tổ chức) mà công ty giao dịch. Trong Odoo, dùng chung 1 model `res.partner` cho cả khách hàng, NCC, nhân viên... |
| **Price List (Bảng giá)** | Bảng giá — bộ quy tắc xác định giá bán áp dụng cho từng nhóm khách hàng/sản phẩm, có thể có nhiều bảng giá khác nhau (vd: giá đại lý, giá lẻ, giá theo khu vực). |
| **Discount** | Chiết khấu / giảm giá — phần trăm hoặc số tiền giảm trừ trên giá bán, có thể áp dụng theo dòng sản phẩm hoặc toàn bộ đơn hàng. |
| **Down Payment** | Tiền đặt cọc / tạm ứng — khoản khách hàng thanh toán trước một phần giá trị đơn hàng, thường xuất hóa đơn riêng trước khi giao hàng đầy đủ. |
| **Recurring Revenue / Subscription (Sales)** | Doanh thu định kỳ / hợp đồng thuê bao — mô hình bán hàng thu tiền lặp lại theo chu kỳ (vd: phí dịch vụ hàng tháng), Odoo hỗ trợ qua app Subscriptions (Enterprise). |

---

## 4. Purchase

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **RFQ (Request for Quotation)** | Yêu cầu báo giá (phía mua hàng) — chứng từ công ty gửi cho NCC để hỏi giá, **chưa phải** đơn đặt hàng chính thức. *(Lưu ý: khác với "RFQ" trong ngữ cảnh đấu thầu/procurement của khách hàng — xem Mục 10.)* |
| **Purchase Order (PO)** | Đơn đặt hàng (mua) — RFQ sau khi NCC xác nhận giá và công ty đồng ý đặt hàng, trở thành cam kết mua hàng chính thức. |
| **Vendor** | Nhà cung cấp (NCC) — đối tác cung cấp hàng hóa/dịch vụ cho công ty. |
| **Vendor Bill** | Hóa đơn mua hàng / hóa đơn từ NCC — chứng từ NCC gửi yêu cầu thanh toán, đối chiếu với PO và phiếu nhập kho (3-way matching). |
| **Purchase Agreement** | Thỏa thuận mua hàng / hợp đồng khung mua hàng — cam kết giá/điều khoản với NCC trong một khoảng thời gian, dùng làm cơ sở tạo các PO sau này. |
| **Replenishment / Reordering Rule** | Bổ sung hàng tự động / Quy tắc đặt hàng lại — quy tắc tự động tạo đề xuất mua hàng hoặc sản xuất khi tồn kho xuống dưới mức tối thiểu. |
| **Drop-shipping** | Giao hàng thẳng từ NCC — NCC giao hàng trực tiếp đến khách hàng cuối, công ty không cần nhập hàng vào kho của mình. |

---

## 5. Inventory & Logistics

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Pick-Pack-Ship** | Lấy hàng - Đóng gói - Giao hàng — quy trình xử lý đơn hàng xuất kho theo 3 bước riêng biệt (thường dùng ở kho lớn để chia việc cho nhiều người). |
| **Putaway Rule** | Quy tắc cất hàng — quy tắc tự động xác định vị trí lưu trữ (location) cho hàng hóa khi nhập kho, dựa trên loại sản phẩm/khu vực. |
| **Removal Strategy (FIFO/LIFO/FEFO)** | Chiến lược xuất hàng — quy tắc xác định lô hàng nào được xuất trước: **FIFO** (nhập trước xuất trước), **LIFO** (nhập sau xuất trước), **FEFO** (hết hạn trước xuất trước — quan trọng với hàng có hạn sử dụng). |
| **Lot / Serial Number** | Số lô / Số seri — mã định danh để truy xuất nguồn gốc một nhóm hàng (Lot) hoặc một sản phẩm đơn lẻ (Serial). Dùng cho truy xuất, bảo hành, hạn sử dụng. |
| **Landed Cost** | Chi phí phát sinh thêm (chi phí nhập hàng) — các chi phí ngoài giá mua (vận chuyển, bảo hiểm, thuế nhập khẩu...) được phân bổ vào giá vốn sản phẩm. |
| **Stock Move** | Dịch chuyển kho — bản ghi thể hiện một lần hàng hóa di chuyển từ vị trí này sang vị trí khác (nhập, xuất, chuyển kho nội bộ), là đơn vị nhỏ nhất trong Odoo Inventory. |
| **Inventory Adjustment** | Kiểm kê / Điều chỉnh tồn kho — quá trình đối chiếu số liệu tồn kho thực tế với số liệu trên hệ thống và điều chỉnh cho khớp. |
| **Warehouse / Location** | Kho / Vị trí kho — Warehouse là một kho vật lý (vd: Kho Hà Nội, Kho HCM); Location là vị trí cụ thể bên trong kho (vd: Khu A, Kệ 1, Tầng 2) hoặc vị trí ảo (Khách hàng, NCC, Hao hụt). |
| **Delivery Order (DO)** | Phiếu giao hàng / Phiếu xuất kho — chứng từ ghi nhận việc xuất hàng từ kho để giao cho khách hàng. |
| **Receipt** | Phiếu nhập kho — chứng từ ghi nhận việc nhận hàng vào kho (từ NCC hoặc từ kho khác). |
| **Internal Transfer** | Chuyển kho nội bộ — di chuyển hàng hóa giữa các vị trí/kho trong cùng công ty. |
| **Barcode** | Mã vạch — dùng máy quét để thao tác nhanh trên các phiếu kho (nhập/xuất/kiểm kê) thay vì nhập tay, giảm sai sót. |

---

## 6. Manufacturing (MRP)

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **BOM (Bill of Materials)** | Định mức nguyên vật liệu (Bảng kê vật tư) — danh sách nguyên vật liệu/linh kiện và số lượng cần thiết để sản xuất ra một sản phẩm. |
| **Work Order** | Lệnh công việc / Lệnh sản xuất theo công đoạn — một bước/công đoạn cụ thể trong quá trình sản xuất, gắn với một Work Center. |
| **Routing** | Quy trình công nghệ / Định tuyến sản xuất — chuỗi các công đoạn (Work Order) cần thực hiện theo thứ tự để hoàn thành sản phẩm. |
| **Work Center** | Trung tâm sản xuất / Tổ máy — một máy móc, dây chuyền hoặc tổ đội thực hiện một hoặc nhiều công đoạn sản xuất, có công suất (capacity) và chi phí giờ công riêng. |
| **Manufacturing Order (MO)** | Lệnh sản xuất — chứng từ chính thức ra lệnh sản xuất một số lượng sản phẩm theo một BOM cụ thể. |
| **Component** | Thành phần / Nguyên vật liệu đầu vào — các nguyên vật liệu/bán thành phẩm được tiêu thụ trong quá trình sản xuất theo BOM. |
| **By-product** | Sản phẩm phụ — sản phẩm phát sinh thêm (ngoài sản phẩm chính) trong quá trình sản xuất, có thể bán hoặc tái sử dụng. |
| **Quality Check** | Kiểm tra chất lượng (QC) — bước kiểm tra chất lượng sản phẩm/nguyên vật liệu tại các điểm kiểm soát trong quy trình (nhập kho, sản xuất, xuất kho). |
| **PLM (Product Lifecycle Management)** | Quản lý vòng đời sản phẩm — quản lý các phiên bản của sản phẩm/BOM và các thay đổi kỹ thuật (Engineering Change Order - ECO) theo thời gian. |

---

## 7. Accounting & Finance

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Journal Entry** | Bút toán / Định khoản kế toán — bản ghi kế toán thể hiện một giao dịch theo nguyên tắc Nợ/Có (Debit/Credit), là đơn vị cơ bản của sổ sách kế toán. |
| **Chart of Accounts (COA)** | Hệ thống tài khoản kế toán — danh mục các tài khoản kế toán được tổ chức theo quy định (ở VN tham chiếu TT200/TT133, xem `l10n-vietnam-compliance-guide.md`). |
| **Reconciliation** | Đối soát / Đối chiếu công nợ — quá trình khớp các bút toán với nhau (vd: khớp khoản phải thu với khoản đã thanh toán) để xác định số dư còn lại. |
| **Fiscal Year / Period** | Năm tài chính / Kỳ kế toán — khoảng thời gian dùng để lập báo cáo tài chính (thường 12 tháng), chia nhỏ thành các kỳ (tháng/quý). |
| **Invoice / Bill** | Hóa đơn bán (Invoice) / Hóa đơn mua (Bill) — chứng từ yêu cầu thanh toán: Invoice gửi cho khách hàng (đầu ra), Bill nhận từ NCC (đầu vào). |
| **Credit Note** | Hóa đơn điều chỉnh giảm / Giấy báo có — chứng từ điều chỉnh giảm giá trị của một hóa đơn đã phát hành (vd: do trả hàng, giảm giá sau bán). |
| **Payment Term** | Điều khoản thanh toán — quy định thời hạn và cách thức thanh toán (vd: thanh toán ngay, trả chậm 30 ngày, trả góp theo từng đợt). |
| **Tax** | Thuế — các loại thuế áp dụng lên giao dịch (VAT, thuế nhập khẩu...), được cấu hình để tự động tính trên hóa đơn/đơn hàng. |
| **Asset Depreciation** | Khấu hao tài sản cố định — quá trình phân bổ giá trị của tài sản cố định thành chi phí theo thời gian sử dụng. |
| **Analytic Account / Cost Center** | Tài khoản quản trị / Trung tâm chi phí — dùng để theo dõi doanh thu/chi phí theo dự án, phòng ban, hoặc đối tượng quản trị khác — độc lập với hệ thống tài khoản kế toán chính thức. |
| **Bank Statement** | Sao kê ngân hàng — danh sách các giao dịch phát sinh trên tài khoản ngân hàng, dùng để đối soát (Reconciliation) với sổ sách. |
| **Trial Balance** | Bảng cân đối số phát sinh — báo cáo tổng hợp số dư đầu kỳ, phát sinh trong kỳ, và số dư cuối kỳ của tất cả tài khoản kế toán. |
| **Budget** | Ngân sách — kế hoạch thu/chi dự kiến theo khoảng thời gian, dùng để so sánh với số liệu thực tế (Analytic Account). |

---

## 8. HR & Payroll

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Employee** | Nhân viên — hồ sơ thông tin nhân sự (thông tin cá nhân, vị trí, phòng ban, quản lý trực tiếp...). |
| **Contract** | Hợp đồng lao động — thông tin về điều khoản làm việc của nhân viên (lương, loại hợp đồng, thời hạn), là cơ sở để tính lương (Payroll). |
| **Payroll** | Tính lương / Bảng lương — quá trình tính toán lương, thưởng, các khoản khấu trừ (BHXH, thuế TNCN...) cho nhân viên theo kỳ lương. |
| **Time Off** | Nghỉ phép — quản lý các loại ngày nghỉ (phép năm, nghỉ ốm, nghỉ không lương...) và quy trình xin nghỉ/duyệt nghỉ. |
| **Attendance** | Chấm công — ghi nhận giờ vào/ra làm việc thực tế của nhân viên (qua kiosk, máy chấm công, hoặc app di động). |
| **Appraisal** | Đánh giá hiệu suất — quy trình đánh giá định kỳ kết quả làm việc của nhân viên (theo mục tiêu, 360-degree feedback...). |
| **Recruitment** | Tuyển dụng — quy trình quản lý tin tuyển dụng, hồ sơ ứng viên, và các vòng phỏng vấn (thường dạng Kanban theo từng giai đoạn tuyển dụng). |
| **Department** | Phòng ban — đơn vị tổ chức trong sơ đồ công ty, dùng để nhóm nhân viên và phân quyền/báo cáo theo phòng ban. |
| **Job Position** | Vị trí công việc / Chức danh — định nghĩa một vị trí tuyển dụng/công việc cụ thể trong công ty (vd: Kế toán viên, Trưởng phòng Kinh doanh). |
| **Expense** | Chi phí (nhân viên ứng/chi hộ) — khoản chi nhân viên tự ứng trước (vd: tiếp khách, công tác phí) và đề nghị công ty hoàn lại, theo quy trình duyệt chi. |

---

## 9. Project & Service

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Task** | Công việc / Nhiệm vụ — đơn vị công việc nhỏ nhất trong một dự án, có thể giao cho một hoặc nhiều người phụ trách, có deadline. |
| **Milestone** | Mốc dự án / Cột mốc quan trọng — điểm đánh dấu một giai đoạn quan trọng đã hoàn thành trong dự án (thường gắn với điều kiện thanh toán). |
| **Timesheet** | Bảng chấm công theo dự án / Bảng kê thời gian — ghi nhận số giờ làm việc của nhân viên trên từng task/dự án, có thể dùng để tính billable (xuất hóa đơn theo giờ). |
| **Stage (Kanban)** | Giai đoạn (Kanban) — các cột trong giao diện Kanban thể hiện trạng thái tiến độ của task/cơ hội/lead (vd: To Do → In Progress → Done). |
| **Helpdesk Ticket** | Phiếu hỗ trợ / Ticket — yêu cầu hỗ trợ từ khách hàng (sự cố, câu hỏi, yêu cầu bảo hành) được theo dõi từ lúc tạo đến khi giải quyết xong. |
| **SLA Policy** | Chính sách SLA — quy tắc xác định thời gian phản hồi/xử lý tối đa cho một loại ticket/yêu cầu, dựa trên mức độ ưu tiên. |
| **Field Service** | Dịch vụ hiện trường — quản lý đội kỹ thuật/nhân viên đi làm việc tại địa điểm khách hàng (lắp đặt, bảo trì, sửa chữa tận nơi). |
| **Planning / Shift** | Lập lịch làm việc / Ca làm — phân công lịch làm việc (ca, khung giờ) cho nhân viên, thường dùng cho cửa hàng, nhà máy, đội dịch vụ hiện trường. |

---

## 10. Thuật ngữ riêng của PreSale

| Thuật ngữ (English) | Nghĩa tiếng Việt / Giải thích ngắn |
|---|---|
| **Discovery** | Khảo sát / Thu thập yêu cầu — giai đoạn đầu tiên, PreSale làm việc với khách hàng để hiểu quy trình hiện tại và nhu cầu. Xem bộ câu hỏi tại `presales-discovery-questionnaire.md`. |
| **Fit-Gap (Fit / Gap)** | Phân tích đáp ứng / khoảng trống — đánh giá từng yêu cầu của khách: Odoo **đáp ứng sẵn (Fit)** hay **cần customize/tích hợp (Gap)**. Xem định nghĩa đầy đủ và các mức phân loại tại `presales-fit-gap-analysis-guide.md` (Mục 3). |
| **MoSCoW** | Khung ưu tiên hóa yêu cầu — viết tắt của **M**ust have / **S**hould have / **C**ould have / **W**on't have, dùng để xếp hạng độ ưu tiên của từng yêu cầu. Xem chi tiết tại `presales-fit-gap-analysis-guide.md` (Mục 6). |
| **SOW (Statement of Work)** | Bản mô tả phạm vi công việc — tài liệu pháp lý mô tả chi tiết phạm vi (scope), deliverable, timeline, chi phí, và trách nhiệm các bên trong dự án. Xem template tại `presales-proposal-sow-templates.md`. |
| **Deliverable** | Sản phẩm bàn giao — kết quả cụ thể, hữu hình mà đội triển khai phải bàn giao cho khách hàng (vd: hệ thống đã cấu hình, tài liệu hướng dẫn, báo cáo tùy chỉnh). |
| **Proposal** | Đề xuất / Báo giá tổng thể — tài liệu trình bày giải pháp đề xuất, phạm vi, chi phí và timeline gửi cho khách hàng để ra quyết định. Gồm Technical Proposal và Commercial Proposal. |
| **RFP / RFQ (Request for Proposal / Request for Quotation — phía khách hàng/đấu thầu)** | Hồ sơ mời thầu / Yêu cầu báo giá (từ khách hàng) — tài liệu khách hàng phát hành để mời các nhà cung cấp (như công ty mình) nộp đề xuất/báo giá. **Lưu ý:** đây là RFQ theo nghĩa **đấu thầu/mua sắm của khách hàng**, khác với "RFQ" trong Odoo Purchase (Mục 4) — RFQ của Odoo Purchase là chứng từ **công ty mình gửi cho NCC của mình**. Hai khái niệm tên giống nhau nhưng vai trò ngược chiều, cần làm rõ khi trao đổi để tránh nhầm lẫn. |
| **Change Request (CR)** | Yêu cầu thay đổi — yêu cầu phát sinh thêm từ khách hàng sau khi SOW đã được thống nhất, cần đánh giá tác động đến effort/chi phí/timeline trước khi thực hiện. |
| **Out of Scope** | Ngoài phạm vi — các hạng mục đã được xác nhận **không** nằm trong phạm vi triển khai hiện tại (có thể đưa vào Phase sau), cần ghi rõ trong SOW để tránh tranh chấp ("scope creep"). |
| **Process Change** | Thay đổi quy trình — khi khách hàng đồng ý điều chỉnh quy trình nghiệp vụ hiện tại theo cách làm chuẩn của Odoo thay vì yêu cầu customize. Thường là hướng xử lý Gap **rẻ nhất**. Xem `presales-fit-gap-analysis-guide.md` (Mục 5). |

---

## Liên kết

- `odoo-app-feature-matrix.md` — Danh mục Apps Odoo, dùng cùng các thuật ngữ ở Mục 3-9 để map yêu cầu khách hàng sang giải pháp.
- `presales-discovery-questionnaire.md` — Bộ câu hỏi khảo sát theo từng khối nghiệp vụ, dùng các thuật ngữ trong Mục 2-9 khi ghi chép.
- `presales-fit-gap-analysis-guide.md` — Định nghĩa đầy đủ Fit/Gap/MoSCoW/Process Change (Mục 10 của file này chỉ tóm tắt và trỏ link).
- `presales-proposal-sow-templates.md` — Sử dụng các thuật ngữ SOW/Deliverable/Out of Scope trong Mục 10 khi soạn Proposal.
