---
name: presales-industry-solution-templates
keywords: [presales, industry, nganh, blueprint, distribution, manufacturing, retail, construction, services, logistics]
description: Blueprint giải pháp dựng sẵn theo từng ngành phổ biến tại VN - combo Apps đề xuất, quy trình điển hình, customization thường gặp - giúp PreSale demo nhanh và định hướng phạm vi
odoo_versions: [all]
related_skills: [odoo-app-feature-matrix, presales-competitor-comparison-guide, presales-demo-environment-guide, vietnam-integration-landscape]
---

# Industry Solution Templates (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  INDUSTRY SOLUTION TEMPLATES                                                  ║
║  Ngành của khách → Combo Apps + Quy trình mẫu → Điểm khởi đầu Demo/Fit-Gap    ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này tổng hợp các **blueprint giải pháp dựng sẵn** cho những ngành phổ biến mà các đối tác triển khai Odoo tại Việt Nam thường gặp: combo Apps đề xuất, quy trình mẫu (sample flow), các customization/Gap thường lặp lại, và đối thủ cạnh tranh thường gặp trong ngành.

---

## 0. Cách dùng

- Mỗi blueprint dưới đây là **điểm khởi đầu** (starting point) cho buổi Discovery và Demo đầu tiên — giúp PreSale chuẩn bị nhanh combo Apps phù hợp và kịch bản demo theo đúng "ngôn ngữ nghiệp vụ" của ngành, thay vì demo Odoo từ con số 0.
- Blueprint **KHÔNG thay thế** Fit-Gap Analysis (`presales-fit-gap-analysis-guide.md`) — vẫn **bắt buộc khảo sát riêng** cho từng khách hàng cụ thể bằng `presales-discovery-questionnaire.md`, vì:
  - Mỗi công ty có quy trình đặc thù riêng dù cùng ngành (vd 2 doanh nghiệp phân phối cùng ngành hàng nhưng chính sách công nợ/chiết khấu hoàn toàn khác nhau).
  - Một khách hàng có thể thuộc **nhiều ngành cùng lúc** (vd vừa sản xuất vừa phân phối) → cần kết hợp nhiều blueprint.
  - Edition (Community/Enterprise) của các App tham chiếu trong bảng "Combo Apps đề xuất" lấy từ `odoo-app-feature-matrix.md` — **luôn verify lại** theo đúng version Odoo của khách trước khi cam kết.
- Mục "Customization thường gặp" liệt kê các **Gap điển hình** của ngành — dùng để PreSale chủ động hỏi đúng trọng tâm trong Discovery, và đưa thẳng vào bảng Fit-Gap khi khảo sát thực tế (không tự động coi là Gap bắt buộc của mọi khách).
- Mục "Đối thủ thường gặp" chỉ liệt kê tên — chi tiết so sánh tính năng/giá xem `presales-competitor-comparison-guide.md`.
- Sau khi chọn blueprint phù hợp, bước tiếp theo: chuẩn bị môi trường demo theo `presales-demo-environment-guide.md`.

---

## 1. Phân phối / Bán buôn (Distribution & Wholesale)

### Đặc điểm nghiệp vụ điển hình
- Danh mục nhiều SKU (hàng nghìn mã), thường tổ chức theo nhóm/category nhiều cấp.
- Nhiều kho/chi nhánh — hàng hóa luân chuyển liên tục giữa kho tổng và kho chi nhánh/showroom.
- Công nợ khách hàng và nhà cung cấp lớn, cần kiểm soát hạn mức tín dụng (credit limit) chặt chẽ.
- Chính sách giá phức tạp: chiết khấu theo bậc thang số lượng, theo nhóm khách hàng (đại lý cấp 1/2, khách lẻ), theo khu vực.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Sales** | Báo giá, đơn bán, chính sách giá theo nhóm khách | C |
| **Purchase** | Đặt hàng nhà cung cấp, bổ sung tồn kho | C |
| **Inventory** | Quản lý đa kho/chi nhánh, chuyển kho nội bộ, FIFO/FEFO | C/E |
| **Accounting** (hoặc Invoicing nếu chưa cần đầy đủ) | Công nợ KH/NCC, hóa đơn, đối chiếu thanh toán | E (C cho Invoicing) |
| **CRM** | Quản lý khách hàng/đại lý, theo dõi cơ hội mở rộng kênh | C |
| *Optional:* **eCommerce** | Cổng đặt hàng B2B cho đại lý, đồng bộ tồn kho/giá | C/E |
| *Optional:* **Barcode** | Quét mã vạch khi nhập/xuất/kiểm kê đa kho | E |
| *Optional:* **Subscriptions** | Hợp đồng cung cấp định kỳ (vd hợp đồng cung ứng VPP, vật tư hàng tháng) | E |

### Quy trình mẫu (luồng ngắn)

```
Lead/Khách đặt hàng (CRM/Sales) → Báo giá theo bảng giá nhóm KH (Sales)
  → Đơn bán (Sales) → Xuất kho theo route (Inventory)
  → Hóa đơn (Accounting) → Theo dõi công nợ & thu tiền (Accounting)
```

### Customization thường gặp
- Chiết khấu/giá đặc thù theo hợp đồng từng khách hàng (không chỉ theo bảng giá chuẩn của Sales).
- Kiểm soát công nợ theo hạn mức tín dụng (credit limit) — cảnh báo/khóa đơn khi khách vượt hạn mức.
- Chương trình khuyến mãi phức tạp (mua X tặng Y, chiết khấu lũy tiến theo doanh số tích lũy).
- Đối chiếu công nợ định kỳ với đại lý (statement of account) theo mẫu riêng.
- Phân quyền xem giá/tồn kho theo từng nhóm đại lý trên cổng B2B.

### Đối thủ thường gặp
- Misa AMIS
- Fast Business
- SAP Business One

---

## 2. Sản xuất (Manufacturing)

### Đặc điểm nghiệp vụ điển hình
- BOM (định mức nguyên vật liệu) nhiều cấp: NVL → bán thành phẩm → thành phẩm.
- Quản lý song song 3 nhóm tồn kho: nguyên vật liệu, bán thành phẩm (WIP), thành phẩm.
- Tính giá thành sản phẩm là bài toán trọng tâm — ảnh hưởng trực tiếp đến báo cáo lãi/lỗ theo sản phẩm.
- Thường có công đoạn sản xuất (routing/work center) và yêu cầu kiểm tra chất lượng tại các điểm dừng.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Manufacturing (MRP)** | BOM nhiều cấp, lệnh sản xuất (Manufacturing Order), routing theo công đoạn | C/E |
| **Inventory** | Quản lý NVL/bán thành phẩm/thành phẩm, nhiều kho | C/E |
| **Purchase** | Mua NVL, quản lý NCC | C |
| **Sales** | Đơn bán thành phẩm, Make-to-Order | C |
| **Accounting** | Tính giá vốn, giá thành, báo cáo lãi/lỗ theo sản phẩm | E |
| *Optional:* **Quality** | Kiểm tra chất lượng (QC) tại các công đoạn/nhập kho | E |
| *Optional:* **PLM** | Quản lý version BOM, thay đổi kỹ thuật (ECO) — cần nếu khách thay đổi thiết kế thường xuyên | E |
| *Optional:* **Maintenance** | Bảo trì máy móc/thiết bị sản xuất | C |
| *Optional:* **Barcode** | Quét mã khi xuất NVL/nhập thành phẩm tại xưởng | E |

### Quy trình mẫu (luồng ngắn)

```
Đơn bán (Sales) → MO - Manufacturing Order (MRP)
  → Xuất NVL / Nhập thành phẩm (Inventory)
  → Tính giá thành → Xuất kho bán → Hóa đơn (Accounting)
```

### Customization thường gặp
- Tính giá thành theo phương pháp riêng (định mức/thực tế/hệ số phân bổ chi phí chung — overhead allocation) khác chuẩn MRP/Accounting mặc định.
- Quản lý hao hụt/phế phẩm theo định mức (% hao hụt cho phép, vượt định mức cần phê duyệt).
- Gia công ngoài (subcontracting) phức tạp — nhiều bước, nhiều NCC gia công cho cùng 1 thành phẩm.
- Lập lịch sản xuất (scheduling) theo công suất máy/work center thực tế, có ràng buộc ưu tiên đơn hàng.
- Báo cáo định mức tiêu hao thực tế vs kế hoạch theo từng lệnh sản xuất.

### Đối thủ thường gặp
- SAP Business One
- 1C
- Các phần mềm MES chuyên ngành

---

## 3. Bán lẻ & F&B (Retail & Food/Beverage)

### Đặc điểm nghiệp vụ điển hình
- Nhiều điểm bán (cửa hàng/chi nhánh), giao dịch nhanh, khối lượng lớn theo ca.
- Khuyến mãi thay đổi thường xuyên (theo ngày/giờ/combo/dịp lễ).
- Với F&B: cần quản lý công thức chế biến (recipe) — bản chất tương đương BOM trong sản xuất.
- Bán đa kênh: tại quầy, online, qua sàn TMĐT, qua app giao đồ ăn.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Point of Sale (POS)** | Bán hàng tại quầy/nhà hàng, nhiều phương thức thanh toán | C |
| **Inventory** | Tồn kho theo từng điểm bán, chuyển hàng giữa kho/cửa hàng | C/E |
| **Accounting** (hoặc Invoicing) | Doanh thu, đối soát ca, hóa đơn | E (C cho Invoicing) |
| **CRM** | Quản lý khách hàng thân thiết (loyalty cơ bản) | C |
| *Optional:* **eCommerce** | Bán hàng online song song với cửa hàng | C/E |
| *Optional:* **Website** | Trang giới thiệu/menu/đặt hàng online | C |
| *Optional:* **Email/SMS Marketing** | Chương trình khuyến mãi, nhắc nhở khách quay lại | C/E |
| *Optional:* **Manufacturing (MRP)** | Quản lý công thức chế biến (recipe = BOM) cho F&B | C/E |

### Quy trình mẫu (luồng ngắn)

```
Khách chọn món/hàng (POS) → Thanh toán (POS, nhiều phương thức)
  → Trừ tồn kho theo công thức/SKU (Inventory)
  → Đối soát doanh thu cuối ca → Hạch toán doanh thu (Accounting)
```

### Customization thường gặp
- Tích hợp máy POS/máy in bill/cân điện tử với phần cứng sẵn có của khách (không thuộc danh sách driver chuẩn).
- Chương trình loyalty/tích điểm riêng (quy tắc tích/đổi điểm phức tạp hơn loyalty chuẩn của POS).
- Đồng bộ đa kênh với sàn TMĐT (Shopee/Lazada/TikTok Shop) và Zalo — đơn hàng, tồn kho, giá 2 chiều.
- Quản lý combo/set món với công thức tính giá và trừ kho riêng cho từng thành phần.
- Báo cáo doanh thu theo ca/nhân viên thu ngân theo mẫu riêng của khách.

### Đối thủ thường gặp
- KiotViet
- Sapo
- Misa AMIS Bán hàng

---

## 4. Xây dựng & Quản lý Dự án (Construction & Project-based)

### Đặc điểm nghiệp vụ điển hình
- Quản lý theo từng công trình/dự án — mỗi công trình là 1 đơn vị theo dõi chi phí/doanh thu riêng.
- Chi phí dự án gồm 3 nhóm chính: nhân công (timesheet), vật tư (mua hàng + xuất kho), và thầu phụ.
- Nghiệm thu và xuất hóa đơn thường theo khối lượng hoàn thành hoặc theo giai đoạn (milestone), không phải theo đơn hàng 1 lần.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Project** | Quản lý công trình/dự án, task, ngân sách dự án | C |
| **Timesheets** | Ghi nhận giờ công nhân công theo từng công trình | C |
| **Sales** | Hợp đồng xây dựng, lập hóa đơn theo tiến độ | C |
| **Purchase** | Mua vật tư công trình, làm việc với NCC/thầu phụ | C |
| **Inventory** | Quản lý vật tư công trình, xuất kho theo công trình | C/E |
| **Accounting** | Theo dõi chi phí/doanh thu theo từng dự án (analytic accounting) | E |
| *Optional:* **Field Service** | Quản lý đội thi công hiện trường, báo cáo công việc + chữ ký nghiệm thu | E |
| *Optional:* **Planning** | Lập lịch phân bổ nhân sự/đội thi công cho nhiều công trình | E |

### Quy trình mẫu (luồng ngắn)

```
Hợp đồng (Sales) → Dự toán/Phân bổ ngân sách (Project budget)
  → Mua vật tư (Purchase) → Ghi nhận chi phí theo dự án (Project/Accounting)
  → Nghiệm thu theo giai đoạn → Xuất hóa đơn theo % hoàn thành (milestone billing)
```

### Customization thường gặp
- Nghiệm thu theo khối lượng/QS (quantity surveying) — chưa có module chuẩn trong Odoo, thường cần custom model + báo cáo.
- Phân bổ chi phí chung (overhead công ty) cho nhiều công trình theo tiêu chí riêng (doanh thu, nhân công, diện tích...).
- Quản lý thầu phụ: hợp đồng khoán, tạm ứng, đối chiếu khối lượng thực hiện vs hợp đồng.
- Báo cáo lãi/lỗ theo từng công trình (project P&L) theo mẫu quản trị riêng của khách.
- Quản lý bảo hành công trình sau bàn giao (theo dõi khiếu nại/bảo trì theo từng hạng mục).

### Đối thủ thường gặp
- Phần mềm dự toán xây dựng chuyên dụng (Eta, G8, Acitt)
- Excel-based vẫn phổ biến

---

## 5. Dịch vụ chuyên nghiệp (Professional Services)

### Đặc điểm nghiệp vụ điển hình
- Bán theo giờ (time & material) hoặc theo gói dịch vụ trọn gói (fixed price).
- Billing dựa trên timesheet thực tế hoặc theo hợp đồng định kỳ (retainer).
- Đội ngũ tư vấn/chuyên gia có nhiều cấp bậc với rate khác nhau — ảnh hưởng trực tiếp đến giá billing và chi phí.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Project** | Quản lý dự án/công việc tư vấn theo từng khách hàng | C |
| **Timesheets** | Ghi nhận giờ làm việc theo dự án, làm cơ sở billing | C |
| **Sales** | Hợp đồng dịch vụ, báo giá gói dịch vụ | C |
| **Accounting** | Xuất hóa đơn theo timesheet/hợp đồng, theo dõi công nợ | E |
| **CRM** | Quản lý pipeline khách hàng/dự án tiềm năng | C |
| *Optional:* **Helpdesk** | Hỗ trợ sau bán (vd hỗ trợ kỹ thuật sau triển khai) | E |
| *Optional:* **Subscriptions** | Hợp đồng dịch vụ định kỳ (bảo trì/support hàng tháng) | E |
| *Optional:* **Knowledge** | Lưu trữ tài liệu/SOP nội bộ cho đội tư vấn | E |
| *Optional:* **Planning** | Phân bổ nhân sự tư vấn cho nhiều dự án song song | E |

### Quy trình mẫu (luồng ngắn)

```
Cơ hội (CRM) → Báo giá gói dịch vụ (Sales)
  → Thực hiện & ghi nhận timesheet (Project/Timesheets)
  → Xuất hóa đơn theo giờ/giai đoạn (Sales → Accounting)
```

### Customization thường gặp
- Billing rate khác nhau theo nhân sự/cấp bậc (junior/senior/manager) áp cho cùng 1 dự án.
- Hợp đồng retainer: khách trả trước 1 khoản, hệ thống trừ dần theo giờ sử dụng thực tế và cảnh báo khi gần hết.
- Báo cáo hiệu suất/utilization của từng tư vấn viên (tỷ lệ giờ billable vs non-billable).
- Quy trình duyệt timesheet nhiều cấp trước khi xuất hóa đơn cho khách.

### Đối thủ thường gặp
- Misa AMIS
- Các SaaS quốc tế (Zoho, HubSpot cho mảng CRM)

---

## 6. Xuất nhập khẩu & Logistics (Import-Export & Logistics)

### Đặc điểm nghiệp vụ điển hình
- Nhiều loại chứng từ xuất nhập khẩu đi kèm mỗi lô hàng (tờ khai hải quan, vận đơn, C/O, hợp đồng ngoại thương).
- Giao dịch đa tiền tệ là bắt buộc (mua/bán với đối tác nước ngoài).
- Cần tính landed cost — phân bổ các chi phí phụ (thuế nhập khẩu, vận chuyển quốc tế, bảo hiểm) vào giá vốn hàng hóa.
- Theo dõi hàng hóa theo lô/container trong suốt quá trình vận chuyển.

### Combo Apps đề xuất

| App | Vai trò trong giải pháp | Edition |
|---|---|---|
| **Purchase** | Đặt hàng NCC nước ngoài, theo dõi lead time giao hàng | C |
| **Sales** | Hợp đồng bán hàng xuất khẩu, đa tiền tệ | C |
| **Inventory** | Quản lý tồn kho theo lô/container, nhiều kho (kho ngoại quan, kho nội địa) | C/E |
| **Accounting** | Đa tiền tệ, hạch toán chênh lệch tỷ giá, landed cost | E |
| *Optional:* **Quality** | Kiểm hàng đầu vào trước khi nhập kho | E |
| *Optional:* **Barcode** | Quét mã khi nhận/xuất hàng theo lô/container | E |

### Quy trình mẫu (luồng ngắn)

```
Đơn mua quốc tế (Purchase) → Nhận hàng + tính landed cost (Inventory/Accounting)
  → Nhập kho (đa tiền tệ) → Đơn bán xuất khẩu (Sales)
  → Hóa đơn đa tiền tệ (Accounting)
```

### Customization thường gặp
- Tính landed cost (thuế nhập khẩu, vận chuyển quốc tế, bảo hiểm) phân bổ vào giá vốn theo tiêu chí riêng (theo trọng lượng, giá trị, thể tích).
- Theo dõi chứng từ XNK (tờ khai hải quan, C/O, vận đơn) — chưa có module chuẩn, thường cần custom model + đính kèm (attachment) liên kết với đơn hàng/lô hàng.
- Tích hợp khai báo hải quan điện tử (VNACCS) thường nằm ngoài phạm vi Odoo — cần làm rõ ranh giới tích hợp với hệ thống khai báo hải quan riêng.
- Quản lý lịch trình vận chuyển/container (ETD/ETA) và cảnh báo trễ hàng.
- Đối chiếu công nợ đa tiền tệ với đối tác nước ngoài, theo dõi chênh lệch tỷ giá thực tế vs hạch toán.

### Đối thủ thường gặp
- Phần mềm khai báo hải quan chuyên dụng + Excel
- ECUS

---

## Liên kết

- Danh mục đầy đủ Apps + Edition để tra cứu/điều chỉnh combo: `odoo-app-feature-matrix.md`
- So sánh chi tiết với từng đối thủ liệt kê ở mỗi ngành: `presales-competitor-comparison-guide.md`
- Chuẩn bị môi trường demo theo blueprint đã chọn: `presales-demo-environment-guide.md`
- Đặc thù tích hợp Việt Nam (sàn TMĐT, Zalo, hóa đơn điện tử, hải quan...): `vietnam-integration-landscape.md`
- Bộ câu hỏi khảo sát chi tiết theo từng khối nghiệp vụ: `presales-discovery-questionnaire.md`
- Bước tiếp theo sau khi chọn blueprint và demo: `presales-fit-gap-analysis-guide.md`
