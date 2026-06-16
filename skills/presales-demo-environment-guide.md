---
name: presales-demo-environment-guide
keywords: [presales, demo, demo data, kich ban demo, scenario, persona, odoo studio]
description: Hướng dẫn dựng môi trường demo ấn tượng - chuẩn bị dữ liệu mẫu, kịch bản theo persona/ngành, và dùng Studio để "demo customize" trực tiếp trước khách
odoo_versions: [all]
related_skills: [presales-industry-solution-templates, odoo-app-feature-matrix, presales-discovery-questionnaire, presales-fit-gap-analysis-guide]
---

# Demo Environment Guide (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  DEMO ENVIRONMENT GUIDE                                                       ║
║  Dựng demo "đúng người, đúng nghề" → Persona + Ngành → Wow moment            ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Tài liệu này hướng dẫn PreSale/Dev chuẩn bị một **buổi demo Odoo có sức thuyết phục**: dữ liệu mẫu sát với khách hàng, kịch bản theo từng persona tham dự, luồng demo theo ngành (bám theo blueprint ở `presales-industry-solution-templates.md`), và cách tận dụng Odoo Studio để tạo "wow moment" ngay tại chỗ.

---

## 1. Cách dùng

- **Demo database chuẩn của Odoo** (instance dùng thử mặc định, dữ liệu "Azure Interior", "Deco Addict"...) chỉ phù hợp cho: demo nội bộ nhanh, giới thiệu tổng quan Odoo lần đầu cho khách chưa rõ nhu cầu, hoặc training đội sales của chính công ty triển khai.
- **Cần dựng demo riêng** khi:
  - Đã qua ít nhất 1 buổi Discovery (`presales-discovery-questionnaire.md`) và biết rõ ngành + vài đặc điểm nghiệp vụ của khách.
  - Buổi demo có sự tham gia của nhiều stakeholder (CEO, kế toán, kho...) — mỗi người cần thấy "góc của mình".
  - Đây là buổi demo "chốt" trước khi khách quyết định chọn nhà triển khai (so với đối thủ).
- **Nguyên tắc cốt lõi:** Demo tốt = khách **"thấy được mình"** trong hệ thống — đúng tên công ty, đúng tên sản phẩm/dịch vụ họ đang bán, đúng đơn vị tính, đúng quy trình duyệt họ đang làm. Đây **không phải** là buổi liệt kê hết tính năng Odoo có; càng cố nhồi nhiều tính năng không liên quan, khách càng khó hình dung và dễ lạc hướng sang câu hỏi "cái kia có làm được không" thay vì tập trung vào giá trị chính.
- Thời gian đầu tư dựng demo riêng nên tỷ lệ với **độ lớn deal** — với deal nhỏ/khách còn đang khảo sát nhiều nhà cung cấp, có thể chỉ cần Việt hoá nhanh (mục 2) + chỉnh vài sản phẩm/khách hàng mẫu là đủ.

---

## 2. Chuẩn bị dữ liệu demo

### 2.1 Chọn nơi dựng database demo

| Phương án | Ưu điểm | Nhược điểm | Phù hợp khi |
|---|---|---|---|
| **Odoo Online free trial** (1 tháng) | Nhanh, không cần hạ tầng, đủ Apps Enterprise để demo | Tự xoá sau 1 tháng (hoặc downgrade), không tách biệt hẳn với account chính, giới hạn customization sâu | Demo nhanh cho 1 khách, vòng đời ngắn (trong tháng) |
| **Odoo.sh staging branch** | Dùng đúng codebase/customization đang phát triển cho khách (nếu đã có dự án), gần với môi trường production thật | Cần đã có project Odoo.sh + biết thao tác branch, tốn thời gian setup hơn trial | Khách đã ký hoặc đang ở giai đoạn cuối, cần demo đúng bản custom đang làm riêng cho họ |
| **Instance demo dùng chung nội bộ** (1 database "tổng" Việt hoá sẵn, dùng cho nhiều khách) | Setup 1 lần, tái sử dụng nhiều lần, tiết kiệm thời gian | Rủi ro lộ dữ liệu khách khác nếu không dọn dẹp kỹ giữa các lần demo (xem mục 2.4) | Công ty triển khai làm nhiều demo/tuần, cần một bộ "khung" sẵn theo từng ngành |

> Gợi ý: với khách quan trọng/deal lớn, kết hợp cả 2 — dùng 1 database Odoo Online trial Việt hoá + dữ liệu riêng cho buổi demo, sau đó nếu khách ký thì migrate sang Odoo.sh chính thức.

### 2.2 Việt hoá nhanh môi trường

Trước khi nhập dữ liệu mẫu theo ngành, làm sạch các yếu tố "rõ ràng là demo nước ngoài":

- **Thông tin công ty:** đổi tên công ty (Settings → Companies) thành tên gần giống/đặt theo tên ngành của khách (vd "Công ty TNHH Thương mại ABC"), upload logo (có thể dùng logo placeholder nếu chưa có logo thật của khách), địa chỉ tại Việt Nam.
- **Currency:** chuyển default currency sang **VND**, kiểm tra định dạng số (dấu phân cách hàng nghìn) hiển thị đúng quy ước VN.
- **Ngôn ngữ:** cài đặt và set **Tiếng Việt** làm ngôn ngữ mặc định cho user demo (Settings → Translations → Languages), nhưng vẫn nên biết cách chuyển nhanh sang English nếu trong buổi demo có người nước ngoài tham dự.
- **Chart of Accounts:** cài package kế toán theo `l10n_vn` (Thông tư 200 hoặc Thông tư 133 tuỳ quy mô khách — xem `l10n-vietnam-compliance-guide.md`) thay vì Chart of Accounts mặc định (Mỹ/chung). Đây là điểm khách kế toán sẽ để ý **đầu tiên**.
- **Múi giờ & định dạng ngày:** set timezone Asia/Ho_Chi_Minh, định dạng ngày dd/mm/yyyy.

### 2.3 Tạo dữ liệu mẫu theo ngành

- **Sản phẩm/dịch vụ:** dùng đúng nhóm sản phẩm khách đang bán (vd nếu khách phân phối vật liệu xây dựng → tạo "Xi măng Hà Tiên PCB40", "Thép Hoà Phát phi 10", thay vì để "Office Chair", "Customizable Desk").
- **Khách hàng/NCC mẫu:** đặt tên công ty Việt Nam giả định nhưng hợp lý theo ngành (vd "Công ty CP Xây dựng Phương Nam", "Đại lý VLXD Minh Phát") — **không** để mặc định "Azure Interior", "Deco Addict", "Gemini Furniture".
- **Đơn vị tính (UoM):** thêm/kiểm tra các đơn vị tính phổ biến tại VN theo ngành (thùng, hộp, cây, cuộn, m², m³, tấn, kg) thay vì chỉ "Units"/"Dozens".
- **Số liệu thực tế hợp lý:** giá bán, số lượng tồn kho, giá trị đơn hàng nên ở **mặt bằng giá VND hợp lý** với ngành của khách (vd đơn hàng phân phối VLXD vài chục triệu, không để giá kiểu "$1,500.00" hoặc số quá tròn/giả tạo như "100" cho mọi sản phẩm).
- **Số lượng dữ liệu vừa đủ:** không cần hàng nghìn record — khoảng 15-30 sản phẩm, 10-15 khách hàng/NCC, vài chục giao dịch (đơn bán/mua/hoá đơn) ở các trạng thái khác nhau (draft, confirmed, done) là đủ để demo mượt mà mà vẫn có dữ liệu cho dashboard/báo cáo.

### 2.4 Lưu ý bảo mật dữ liệu

> **KHÔNG** đưa dữ liệu thật của bất kỳ khách hàng nào (tên khách hàng/NCC thật, số điện thoại, địa chỉ, số liệu tài chính/doanh thu thật...) vào một môi trường demo **dùng chung hoặc public** (vd 1 database demo dùng để demo cho nhiều khách khác nhau, hoặc 1 link demo public không yêu cầu đăng nhập). Nếu cần dùng số liệu thật để minh hoạ tính thuyết phục (vd import thử file Excel thật của khách để demo migration), chỉ làm trên **database riêng biệt cho khách đó**, xoá ngay sau buổi demo, và không chia sẻ lại cho khách khác.

---

## 3. Kịch bản demo theo Persona

Mỗi buổi demo thường có nhiều người tham dự với mối quan tâm khác nhau. Chuẩn bị sẵn 1-2 "điểm nhấn" (wow moment) riêng cho từng persona — kể cả khi không phải trọng tâm chính của buổi demo, dành 5-10 phút cho mỗi persona quan trọng có mặt sẽ giúp họ cảm thấy được "nói chuyện trực tiếp" thay vì chỉ ngồi nghe.

| Persona | Quan tâm gì | Tính năng nên demo | "Wow moment" |
|---|---|---|---|
| **CEO / Director** | Bức tranh tổng quan toàn công ty, ra quyết định nhanh, kiểm soát từ xa | Dashboard tổng hợp đa phòng ban (Spreadsheet/Dashboards), báo cáo doanh thu/lợi nhuận theo thời gian thực, mobile app | Mở điện thoại, vào mobile app, xem doanh số "hôm nay" cập nhật ngay khi 1 đơn hàng vừa được xác nhận trên máy demo trước mặt CEO |
| **Kế toán trưởng / CFO** | Độ tin cậy số liệu, giảm thao tác thủ công, tuân thủ quy định VN | Tự động hạch toán bút toán từ đơn bán/mua (Invoicing → Accounting), đối soát ngân hàng (bank reconciliation) bán tự động, báo cáo tài chính (P&L, Balance Sheet) real-time, hoá đơn điện tử theo `l10n_vn` | Click 1 nút "Reconcile" và thấy hệ thống tự match giao dịch ngân hàng với hoá đơn — việc trước đây làm thủ công hàng giờ trên Excel |
| **Trưởng kho / Operations** | Tồn kho chính xác real-time, giảm sai sót thao tác tay | Quét barcode để nhận hàng/xuất hàng, quy trình pick-pack-ship nhiều bước, xem tồn kho cập nhật ngay sau khi quét | Quét 1 mã vạch trên điện thoại/máy quét → tồn kho trên dashboard giảm ngay lập tức trước mắt khách |
| **Sales Manager** | Đội sales làm việc hiệu quả, không bỏ sót cơ hội, chốt đơn nhanh | Pipeline Kanban kéo-thả qua các giai đoạn, tạo báo giá từ template trong vài click, gửi báo giá kèm e-signature cho khách ký online | Kéo 1 deal từ "Qualified" sang "Won" → hệ thống tự tạo báo giá nháp, gửi email kèm link ký điện tử ngay trong buổi demo |
| **IT Admin / Owner** | Khả năng tự quản trị hệ thống, không phụ thuộc vendor cho mọi thay đổi nhỏ | Phân quyền theo nhóm (groups/access rights), thiết lập multi-company, demo Studio thêm field/sửa view không cần code (xem mục 6) | Thêm ngay 1 field mới vào form theo yêu cầu tức thời của chính IT Admin trong buổi demo — chứng minh "không phải lúc nào cũng cần gọi vendor" |

---

## 4. Kịch bản demo theo ngành

Mỗi luồng demo dưới đây bám theo **Combo Apps đề xuất** và **Quy trình mẫu** đã định nghĩa trong `presales-industry-solution-templates.md` — chỉ trình bày lại dưới dạng **luồng thao tác demo end-to-end (15-20 phút)**, không lặp lại chi tiết App/Edition/Customization (xem file đó để biết đầy đủ).

### 4.1 Phân phối / Bán buôn

1. Mở **CRM**, cho xem 1 cơ hội bán hàng từ đại lý ở giai đoạn "Đàm phán".
2. Chuyển sang **Sales**: tạo báo giá, chọn khách hàng thuộc nhóm "Đại lý cấp 1" → cho thấy bảng giá/chiết khấu tự động áp theo nhóm khách.
3. Xác nhận đơn bán → sang **Inventory**: xem phiếu xuất kho được tạo tự động, chọn kho/chi nhánh tương ứng.
4. Xác nhận giao hàng → quay lại **Sales**, tạo hoá đơn từ đơn bán.
5. Mở **Accounting**: xem hoá đơn vừa tạo xuất hiện trong báo cáo công nợ phải thu, ghi nhận thanh toán.
6. **Kết quả/report cuối:** Dashboard công nợ theo khách hàng + báo cáo doanh số theo nhóm đại lý.

### 4.2 Sản xuất

1. Mở **Sales**: 1 đơn bán thành phẩm đã confirm, có cấu hình Make-to-Order.
2. Sang **Manufacturing (MRP)**: cho xem Manufacturing Order tự động sinh ra, kèm BOM nhiều cấp (thành phẩm → bán thành phẩm → NVL).
3. Mở 1 work order, đánh dấu hoàn thành từng công đoạn (routing) → tồn kho NVL giảm, tồn kho thành phẩm tăng tương ứng.
4. (Nếu có Quality) cho xem 1 điểm kiểm tra chất lượng (quality checkpoint) gắn vào công đoạn cuối.
5. Quay lại **Inventory**: xác nhận nhập kho thành phẩm → xuất kho bán hàng.
6. Mở **Accounting**: xem giá thành sản phẩm được tính toán, ảnh hưởng đến báo cáo lãi/lỗ theo sản phẩm.
7. **Kết quả/report cuối:** Báo cáo giá thành sản phẩm + báo cáo định mức tiêu hao thực tế vs kế hoạch.

### 4.3 Bán lẻ & F&B

1. Mở **Point of Sale**: thực hiện 1 giao dịch bán mẫu (chọn món/sản phẩm, áp khuyến mãi, thanh toán nhiều phương thức — tiền mặt + chuyển khoản).
2. Cho xem hoá đơn/bill in ra (hoặc preview) ngay tại quầy.
3. Sang **Inventory**: xác nhận tồn kho nguyên liệu/sản phẩm tự động trừ theo công thức (recipe = BOM, nếu F&B) hoặc theo SKU (nếu retail thường).
4. (Nếu có eCommerce) mở song song 1 đơn hàng online vừa đặt trên website → cho thấy tồn kho dùng chung giữa kênh online và tại quầy.
5. Cuối ngày: thực hiện thao tác "đóng ca" (close session) trên POS.
6. Mở **Accounting**: xem doanh thu trong ca được hạch toán tự động.
7. **Kết quả/report cuối:** Báo cáo doanh thu theo ca/nhân viên thu ngân + báo cáo sản phẩm bán chạy.

### 4.4 Xây dựng & Quản lý Dự án

1. Mở **Sales**: hợp đồng xây dựng đã ký với khách, cấu hình hoá đơn theo % hoàn thành (milestone billing).
2. Sang **Project**: cho xem công trình tương ứng đã được tạo tự động, với các task/giai đoạn (móng, khung, hoàn thiện...).
3. Mở **Timesheets**: nhập thử giờ công của 1-2 công nhân vào task đang thực hiện.
4. Sang **Purchase**: tạo đơn mua vật tư công trình, gắn vào đúng dự án (analytic account).
5. Quay lại **Project/Accounting**: cho xem chi phí thực tế (nhân công + vật tư) được tổng hợp theo dự án, so với ngân sách ban đầu.
6. Đánh dấu 1 milestone hoàn thành → xuất hoá đơn theo % tương ứng từ **Sales**.
7. **Kết quả/report cuối:** Báo cáo lãi/lỗ theo công trình (project P&L) — chi phí thực tế vs ngân sách vs doanh thu đã xuất hoá đơn.

### 4.5 Dịch vụ chuyên nghiệp

1. Mở **CRM**: 1 cơ hội từ khách hàng tổ chức/doanh nghiệp đang ở giai đoạn đề xuất.
2. Sang **Sales**: tạo báo giá gói dịch vụ tư vấn (theo giờ hoặc trọn gói) → gửi kèm e-signature.
3. Khách "ký" (demo nhanh) → đơn hàng confirm, tự động tạo dự án trong **Project**.
4. Mở **Timesheets**: nhập giờ làm việc của 2-3 chuyên gia với rate khác nhau (junior/senior) vào cùng 1 task.
5. Sang **Sales**: tạo hoá đơn dựa trên timesheet thực tế đã ghi nhận → cho thấy hệ thống tự tổng hợp số giờ × rate tương ứng.
6. (Nếu có Helpdesk) mở nhanh 1 ticket hỗ trợ sau triển khai liên kết với cùng khách hàng.
7. **Kết quả/report cuối:** Báo cáo utilization (tỷ lệ giờ billable/non-billable) theo từng tư vấn viên + công nợ theo hợp đồng.

### 4.6 Xuất nhập khẩu & Logistics

1. Mở **Purchase**: đơn mua hàng quốc tế đã confirm, đơn vị tiền tệ là USD/EUR (đa tiền tệ).
2. Sang **Inventory**: xác nhận nhận hàng theo lô/container → cho xem cách phân bổ landed cost (thuế NK, vận chuyển, bảo hiểm) vào giá vốn lô hàng.
3. Mở **Accounting**: xem bút toán chênh lệch tỷ giá phát sinh khi quy đổi USD/EUR sang VND.
4. Sang **Sales**: tạo đơn bán xuất khẩu cho 1 khách nước ngoài, cũng bằng ngoại tệ.
5. Quay lại **Inventory**: xem tồn kho theo lô/container vẫn được theo dõi xuyên suốt từ nhập đến xuất.
6. **Kết quả/report cuối:** Báo cáo giá vốn đã bao gồm landed cost theo lô hàng + báo cáo công nợ đa tiền tệ với chênh lệch tỷ giá.

---

## 5. Checklist chuẩn bị trước demo

- [ ] **Dữ liệu:** đã Việt hoá (công ty, currency VND, Chart of Accounts `l10n_vn`, ngôn ngữ tiếng Việt), đã tạo dữ liệu mẫu theo đúng ngành khách, đã xoá dữ liệu test rác/dữ liệu demo mặc định không liên quan.
- [ ] **User & phân quyền:** đã tạo sẵn user demo riêng cho từng persona (CEO, kế toán, kho, sales...) với phân quyền tương ứng — **không demo bằng tài khoản Admin** cho mọi vai trò (vì Admin thấy mọi menu/tính năng, không phản ánh đúng trải nghiệm thật của user cuối).
- [ ] **Dashboard/KPI:** đã setup sẵn ít nhất 1-2 dashboard chính theo persona quan trọng nhất (vd CEO dashboard), đã test hiển thị đúng số liệu từ dữ liệu mẫu đã tạo.
- [ ] **Mobile app:** đã cài Odoo mobile app và **đăng nhập sẵn** trên điện thoại/tablet demo, đã test load được trang chính trước khi vào phòng demo.
- [ ] **Internet backup:** chuẩn bị 4G hotspot dự phòng — phòng trường hợp wifi của khách chập chờn hoặc chặn truy cập ra ngoài (firewall công ty khách).
- [ ] **Rehearse trình tự:** đã chạy thử toàn bộ kịch bản demo theo đúng thứ tự ít nhất 1 lần trên **đúng môi trường/trình duyệt** sẽ dùng khi demo thật, có chuẩn bị **"Plan B"** (vd ảnh chụp màn hình/video quay sẵn) cho bước nào có rủi ro lỗi cao (tích hợp ngoài, kết nối thiết bị phần cứng, internet...).

---

## 6. Dùng Odoo Studio để "demo customize" trực tiếp

- **Ý tưởng:** trong lúc demo, nếu khách bất chợt hỏi "vậy nếu em cần thêm 1 trường X / đổi tên cột Y / ẩn bớt cột Z thì sao?" — đây là cơ hội vàng. Mở **Studio** ngay tại chỗ, thêm field/đổi label/ẩn hiện cột theo đúng yêu cầu vừa nêu, rồi quay lại record vừa demo để cho khách thấy thay đổi có hiệu lực ngay lập tức. Đây thường là **"wow moment"** lớn nhất của cả buổi — đặc biệt với persona IT Admin/Owner (mục 3) — vì thể hiện trực quan tính linh hoạt "no-code" của Odoo Enterprise mà các phần mềm đóng gói khác (Misa, Fast, KiotViet...) khó làm được ngay tại chỗ.
- **Lưu ý:** chỉ nên thực hiện với những thay đổi **đơn giản và đã luyện tập trước** (thêm field text/số/ngày, đổi label, ẩn/hiện cột trong list view, sắp xếp lại field trên form). **Không** thử nghiệm điều gì chưa từng làm trên môi trường demo — Studio thao tác trực tiếp lên schema, một thay đổi sai có thể làm hỏng view hoặc gây lỗi hiển thị giữa buổi demo, rất khó xử lý gọn trước mặt khách.
- **Cảnh báo Edition:** Studio là tính năng **Enterprise**. Nếu khách đã xác định/có khả năng cao sẽ dùng **Community**, **không nên** demo bước này — hoặc nếu vẫn muốn cho khách thấy khả năng này tồn tại, phải nói rõ ngay từ đầu: "đây là tính năng của gói Enterprise, không có sẵn trong Community" — tránh để khách hiểu nhầm rồi thất vọng khi biết phải trả thêm phí license mới có Studio.

---

## 7. Lỗi thường gặp khi demo (pitfalls)

- **Demo quá nhiều tính năng không liên quan đến nhu cầu khách** — mỗi tính năng "thêm cho vui" kéo dài thời gian và làm loãng thông điệp chính, khiến khách khó nhớ điều quan trọng nhất.
- **Để lộ dữ liệu/tên khách hàng khác** trong môi trường demo dùng chung — vô tình mở 1 record/báo cáo còn chứa tên công ty/số liệu của khách trước đó là một sự cố nghiêm trọng về bảo mật và uy tín.
- **Không test trước trên đúng môi trường/trình duyệt** sẽ dùng khi demo thật — lỗi về độ phân giải màn hình, trình duyệt không hỗ trợ, hoặc mất kết nối với hệ thống bên thứ 3 (email server, payment gateway demo...) thường chỉ lộ ra khi đã ở trước mặt khách.
- **Trả lời "cái này làm được hết" cho mọi câu hỏi mà chưa verify** — câu trả lời này tạo kỳ vọng sai và có thể trở thành cam kết ngầm trong mắt khách. Thay vào đó, ghi nhận lại câu hỏi để xử lý kỹ hơn trong buổi Fit-Gap workshop (`presales-fit-gap-analysis-guide.md`), trả lời kiểu "đây là yêu cầu hay, để team kỹ thuật xác nhận chi tiết và phản hồi sau buổi này".

---

## Liên kết

- Blueprint theo ngành (combo App + quy trình mẫu mà các luồng demo ở mục 4 bám theo): `presales-industry-solution-templates.md`
- Tra cứu App/tính năng tương ứng khi khách hỏi thêm trong lúc demo: `odoo-app-feature-matrix.md`
- Thông tin đã thu thập trước demo (ngành, quy mô, pain points) để cá nhân hoá kịch bản: `presales-discovery-questionnaire.md`
- Bước tiếp theo sau demo — xử lý các câu hỏi/yêu cầu chưa verify thành Gap chính thức: `presales-fit-gap-analysis-guide.md`
- Chart of Accounts/hoá đơn điện tử theo `l10n_vn` khi Việt hoá dữ liệu kế toán: `l10n-vietnam-compliance-guide.md`
- Chi tiết Community vs Enterprise (đặc biệt cho mục 6 — Studio): `odoo-editions.md`
