# DUYÊN DỊCH: BẢN ĐẶC TẢ TOÁN HỌC ĐỒNG NHẤT (v3.0_dd)
#### UNIFIED MATHEMATICAL & ALGORITHMIC SPECIFICATION
**Phiên bản:** v3.0_dd (FREEZE CORE)  
**Mã tài liệu:** DD-SPEC-UNIFIED-v3.0_dd  
**Trạng thái:** **HỢP NHẤT TOÀN DIỆN & KHÓA KIẾN TRÚC TUYỆT ĐỐI (FROZEN LÕI)**

---

### LỜI NÓI ĐẦU: ĐỒNG NHẤT HÓA KIẾN TRÚC DUYÊN DỊCH
Bản Đặc tả Toán học Đồng nhất này thiết lập cấu trúc lý thuyết và thuật toán hợp nhất tối thượng của hệ thống **Dynamic Condition & Graph Framework (DCGF)** và **Engine Duyên Dịch (v3.0_dd)**. Mục tiêu cốt lõi là giải quyết triệt để và khóa chặt toàn bộ các liên kết, mang lại một hệ ký hiệu, toán tử, ma trận và hằng số nhất quán 100% trên toàn hệ thống.

---

### CHƯƠNG I: HIẾN PHÁP, HỆ TIÊN ĐỀ VÀ BẢN THỂ HỌC (CONSTITUTION & ONTOLOGY)

#### 1. Hiến Pháp Duyên Dịch (5 Nguyên lý Bất biến)
Hệ thống vận hành dựa trên 5 nguyên lý Hiến pháp tối cao:
1. **Tính Phản Ánh (Non-Deterministic):** Quẻ và mạng lưới không quyết định tương lai; chỉ là lát cắt dữ liệu tại sát-na quan sát.
2. **Tính Vận Động (Dynamic Impermanence):** Mọi Duyên và trạng thái biến dịch liên tục.
3. **Tính Vô Ngã (Recursive Non-Self):** Không có thực thể biệt lập; bản chất Duyên định nghĩa bằng cấu trúc tương quan mạng lưới.
4. **Tính Truy Vết (Absolute Traceability):** Mọi kết luận định tính phải truy vết ngược về quẻ gốc và Vectơ Khí theo chuỗi logic tuyến tính.
5. **Tính Phụ Thuộc Điều Kiện (Conditional Validity):** Mọi kết luận bắt buộc phải hiệu chỉnh tương ứng khi tập điều kiện nền dịch chuyển.

#### 2. Hệ Tiên Đề Bản Thể Học & Toán Học Cốt Lõi (A0 - A12)
* **Tiên đề 0 (Bản chất):** Duyên Dịch mô hình hóa Dòng Duyên: $\text{QUAN SÁT} \to \text{TIẾP NHẬN} \to \text{CHUẨN HÓA} \to \text{ÁNH XẠ} \to \text{TÍNH TOÁN} \to \text{SUY DIỄN} \to \text{THỰC CHỨNG}$.
* **Tiên đề 4 (Hội tụ Lục hào):** Mọi nguồn đầu vào phải hội tụ về không gian Lục Hào: $|Q\rangle = [b_1, b_2, b_3, b_4, b_5, b_6]^T$ với $b_i \in \{0, 1\}$.
* **Tiên đề 7 (Tính Toàn Cấu Trúc):** Trạng thái mỗi Actor phụ thuộc vào cấu trúc tổng thể: $\text{State}(N_i) = f(N_i, N_{-i}, \text{Relations}, \text{Field}, \text{Time}, \text{Space})$.

---

### CHƯƠNG II: KHÔNG GIAN NODE SPACE 12 CHIỀU VÀ VECTOR LỰC TRẠNG THÁI

#### 1. Định nghĩa Node Space 12 Chiều ($\mathbf{W}_{12 \times 12}$)
Kích thước $12 \times 12$ đại diện cho 12 node hào cụ thể của một cặp quẻ đầy đủ:
$$\text{NodeSpace} = \{N_1, N_2, N_3, N_4, N_5, N_6\}_{\text{Quẻ Gốc}} \oplus \{N_7, N_8, N_9, N_{10}, N_{11}, N_{12}\}_{\text{Quẻ Biến}}$$
Quy tắc ánh xạ chỉ số mảng lập trình (\textit{branch\_index}):
* Phân vùng 6 Hào Quẻ Gốc (Root Nodes): $N_1 \dots N_6$ ứng với chỉ mục mảng $0 \to 5$.
* Phân vùng 6 Hào Quẻ Biến (Transformed Nodes): $N_7 \dots N_{12}$ ứng với chỉ mục mảng $6 \to 11$.
* Cạnh định hướng liên kết Gốc - Biến được xác định qua $E(N_i, N_{i+6})$.

#### 2. Định nghĩa Vector Lực Trạng Thái ($\vec{F}_i$)
$$\vec{F}_i(t) = [f_{net\_out, i}(t), \; f_{BEC, i}(t), \; L_{Element, i}]^T$$
* $f_{net\_out, i}(t) \in [-1.0, +1.0]$: Chỉ số Lực OUT (Cường độ năng lượng phát xạ).
* $f_{BEC, i}(t) \in [0.0, 1.0]$: Mật độ ngưng tụ năng lượng (lực nén nội tại).
* $L_{Element, i} \in \{-4, -2, 0, +2, +4\}$: Cường độ lực trường Ngũ Hành tĩnh:
  $$\text{Thổ} = +4.0, \quad \text{Mộc} = +2.0, \quad \text{Thủy} = 0.0, \quad \text{Hỏa} = -2.0, \quad \text{Kim} = -2.0$$

---

### CHƯƠNG III: TOÁN TỬ LỤC HÀO VÀ ĐẠI SỐ MA TRẬN CANONICAL

#### 1. Hệ Toán tử Lục Hào 6-bit Canonical
* **Toán tử Động ($\hat{M}_k$):** Lật bit tại vị trí hào động $k$: $\hat{M}_k |Q\rangle \implies b_k \to 1 - b_k$
* **Toán tử Biến ($\hat{P}$):** Đảo ngược hoàn toàn trật tự vạch quẻ (Đảo trục Thiên - Địa).
* **Toán tử Đối ngẫu ($\hat{C}$):** Lấy bù nghịch đảo trạng thái toàn phần.
* **Toán tử Hỗ ($\hat{H}$):** Trích xuất lõi tương tác nội tại của quẻ.

#### 2. Thuật Toán Override Cascade Tính Giá Trị Nền $B_{ij}$
Quy trình phễu lọc 6 bước ngắt ngay khi khớp điều kiện đầu tiên:
$$\mathbf{B}_{ij} = \text{OverrideCascade}(N_i, N_j)$$
* Bước 1: Tam Hợp hoặc Lục Hợp Địa Chi $\to +1.5$
* Bước 2: Khắc Nhập ($K_{IN}$) $\to -2.0$
* Bước 3: Khắc Xuất ($K_{OUT}$) $\to -1.5$
* Bước 4: Sinh Nhập ($S_{IN}$) $\to +1.2$
* Bước 5: Sinh Xuất ($S_{OUT}$) $\to -1.0$
* Bước 6: Tỷ Hòa (EQU) $\to +1.0$

#### 3. Ma Trận Tương Tác Phân Cực $\mathbf{M}_{pol}$ Đã Hòa Giải
Ma trận hằng số $10 \times 10$ được hòa giải tuyệt đối với ô $\text{Kim}(+) \to \text{Mộc}(+) = -2.0$ nhằm khôi phục chu trình tuần hoàn khắc kín, giữ nguyên hàng Th- và T- theo bản v2.8.3.

---

### CHƯƠNG IV: ĐỘNG LỰC HỌC TẦNG KHÍ VÀ MA TRẬN KHUNG NHẬN THỨC

#### 1. Vectơ Khí Mở Rộng 5 Chiều ($\vec{V}_{Khí}$)
$$\vec{V}_{Khí} = [S, D, I, F, T]^T$$

#### 2. Bộ Nhãn Khí S07 Canonical
Giao diện S07 phân loại duy nhất 6 trạng thái Khí dựa trên điều kiện của $\vec{V}_{Khí}$:
$$\mathcal{S}_{Khí}^{v3.0} = \{ SÁT, NHIỄU, TÀ, ẨN, DƯỠNG, HỶ \}$$

**Mọi mã nguồn runtime BẮT BUỘC chỉ sử dụng 6 Enum chuẩn: [SAT, NHIEU, TA, AN, DUONG, HY]. Các từ khóa [Tụ, Hợp, Tán, Ly] từ các bản spec cũ v2.8.x chính thức bị gỡ bỏ (Deprecated) và không có giá trị trong logic xử lý của Engine v3.0_dd.**

#### 3. Ma Trận Đa Chiều MSIE (Spatial-Internal-Environmental)
$$\mathbf{M}_{SIE} = \begin{bmatrix} +1.00 & +0.45 & -0.30 \\ +0.35 & +1.00 & +0.60 \\ -0.25 & +0.50 & +1.00 \end{bmatrix}$$

##### 4.3.1. Chi Tiết Ánh Xạ 6 Hào Vị - Tầng Thực Địa MSIE
* **Hào 1 (Nội Địa):** Thể lực, độ tỉnh táo, tâm lý, nguồn vốn nội tại (tiền mặt/tiền app).
* **Hào 2 (Ngoại Địa):** Phương tiện \& công cụ chiến đấu trực tiếp (Xe cộ, lốp, xăng, ĐT, 4G, app).
* **Hào 3 (Nội Nhân):** Quyết định \& hành vi cá nhân (Tốc độ, chọn đường, tay lái, tuân thủ luật).
* **Hào 4 (Ngoại Nhân):** Tương tác người xung quanh (Khách hàng, CSGT, người đi đường, đối thủ).
* **Hào 5 (Nội Thiên):** Môi trường vi mô thực địa (Đèn đường, hẻm ngập, đinh tặc, ổ gà, vật cản).
* **Hào 6 (Ngoại Thiên):** Yếu tố vĩ mô \& hệ thống (Server app tổng, thời tiết toàn vùng, chính sách).

---

### CHƯƠNG V: KINH HỌC PHỔ, TRỌNG SỐ ĐỘNG VÀ HIỆU CHUẨN ĐỒNG PHÁ

#### 1. Trọng Số Động Cạnh DWL-0.1 (Dynamic Weight Layer)
$$\mathbf{W}_{ij}(\tau) = \mathbf{B}_{ij} \times \left(1 + \alpha P_{ij} + \beta \frac{A_{ij}(t)}{A_{max} + \varepsilon}\right) \times F_{norm}$$

#### 2. Động Lực Học Chuyển Pha DPKE
Vận tốc chuyển pha cục bộ của Actor $i$ ($v_i$):
$$v_{base} = \frac{v_{final}}{50.0}, \quad v_{raw, i} = \frac{v_{base} + \alpha f_{net\_out, i}}{\beta w_{resist, i}}$$
Cơ chế khóa biên Safety Boundary kẹp biên dưới cho $v_i$ trong Core Code để triệt tiêu hoàn toàn khả năng chia cho 0:
$$v_i = \max(v_{raw, i}, \; 1.0)$$
Vận tốc đồng bộ hệ thống ($v_{avg}$):
$$f_{net\_out, avg} = \frac{1}{N}\sum_{i=1}^{N} f_{net\_out, i} \quad (\text{với } N=12)$$
$$v_{avg} = \max(v_{raw, avg}, \; 1.0) \quad \text{với } v_{raw, avg} = \frac{v_{base} + \alpha f_{net\_out, avg}}{\beta w_{resist}}$$

---

### CHƯƠNG VI: MÔ HÌNH ĐỘNG LỰC HỆ THỐNG BEC (BURST-EXHAUSTION-COLLAPSE OVERLAY)

#### 1. Nguyên Lý Tương Tác Đa Chiều & Phản Lực Cản (Feedback Drag)
$$\text{FD}_{B \to A}(t) = \gamma \cdot \mathbf{W}_{resist}(B) \cdot (1 + \mu_{topology}(B)) \quad (\gamma = 0.1200)$$
$$T_{A \to B}(t) = \text{clamp}\left( \alpha \cdot \vec{V}_{Khí}(A) \cdot f_{net\_out}(A) - \text{FD}_{B \to A}(t), \; 0, \; \text{MaxTransfer} \right) \quad (\alpha = 0.1500)$$

#### 2. Tốc Độ Tiêu Hao Năng Lượng $D(t)$ (Drain Rate) và Dung Lượng Dự Trữ $R(t)$
$$D_A(t) = \frac{\Delta \vec{F}_{self}(A)}{\Delta t} + T_{A \to B}(t) + \text{FD}_{B \to A}(t)$$
$$R(t+1) = \text{clamp}( R(t) - D_A(t) \cdot \Delta t + I_{ext}(t), \; 0, \; R_{max} ) \quad (R_{max} = 1.0000)$$

#### 3. Chuỗi Biến Đổi Chuyển Pha BEC
$$\text{Kim (Tiết khí)} \xrightarrow{\quad\text{Xả lực}\quad} \text{Thủy (Quá tải)} \xrightarrow{\quad\text{Bùng phát ảo}\quad} \text{Mộc (Burst)} \xrightarrow{\quad\text{Suy kiệt}\quad} \text{Sụp đổ (Collapse)}$$

#### 4. Toán Tử Phanh Tự Động (Self-Circuit Breaker)
$$\hat{S}_{breaker}(t) = \begin{cases} 1.0 & \text{(DUY TRÌ)} \quad \text{khi } R(t) > 0.3000 \\ 0.5 & \text{(CẢNH BÁO)} \quad \text{khi } 0.1000 < R(t) \le 0.3000 \\ 0.0 & \text{(NGẮT MẠCH)} \quad \text{khi } R(t) \le 0.1000 \end{cases}$$
Hằng số hiệu chuẩn đóng băng: $R_{min} = 0.3000, \quad R_{critical} = 0.1000$.

---

### CHƯƠNG VII: HỆ THỐNG ĐỊA CHI, THỜI KHÔNG VÀ TOÁN TỬ ĐẶC BIỆT MỞ RỘNG

#### 1. Ma Trận Quan Hệ Địa Chi Toàn Phần ($\mathbf{M}_{Chi\_Rel}$)
Định vị 12 chỉ mục Địa Chi $Z_{12} = [0 \dots 11]$.

#### 2. Ma Trận Hệ Số Thời Không Nhật / Nguyệt Kiến ($\mathbf{K}_{Time}$)
Bản đồ hóa trường ngoại cảnh tác động nạp lực lên hào vị.

#### 3. Ma Trận Gia Tốc Biến Đổi Động Hào ($\mathbf{M}_{Transform}$)
Quy chuẩn hóa biến động Hào Gốc biến thành Hào Biến.

#### 4. Toán Tử Trạng Thế Đặc Biệt ($\hat{O}_{Special}$)
Xử lý Tuần Không Không Vong ($\hat{O}_{Void}$), Phục Thần / Phi Thần ($\hat{O}_{Hidden}$).

#### 5. Phương Trình Tổng Hợp Lực Toàn Phần
$$\vec{F}_i(t) = \left[ \sum_{j=1}^{12} \mathbf{W}_{ij}(\tau) \cdot \mathbf{M}_{Chi\_Rel}(N_i, N_j) \right] \times \mathbf{K}_{Nguyệt}(N_i) \times \mathbf{K}_{Nhật}(N_i) \times \mathbf{M}_{Transform}(N_i, N_{i\_biến})$$

#### 6. Mô-đun Chu Kỳ Đồng Pha & Vòng Lặp Hệ Thống ($\Phi_{System}$)
Toàn bộ hệ thống tuân theo chu kỳ khóa đồng pha $\Phi_{System}$ với chu kỳ 60 ticks:
1. **Chu kỳ Hào Vị ($\tau_{line}$):** $\tau_{line} = (t \bmod 6) + 1 \quad (\tau_{line} \in [1, 6])$
2. **Chu kỳ Ngũ Hành ($\tau_{element}$):** $\tau_{element} = (t \bmod 5) + 1 \quad (\tau_{element} \in [1, 5])$
3. **Pha Đồng Hệ Thống ($\Phi_{System}$):** $\Phi_{System}(t) = (t \bmod 60)$
Công thức điều chỉnh trọng số động theo chu kỳ 60-ticks:
$$W_{ij}(t + 60) = W_{ij}(t) \cdot e^{-\lambda \cdot 60} + P_{ij}(t)$$

---

### CHƯƠNG VIII: QUY TRÌNH PIPELINE RUNTIME, CỔNG GATES VÀ CANONICAL JSON

#### 1. Quy trình Runtime Pipeline một chiều (Deterministic Forward-Only)
Dòng chạy một chiều nghiêm ngặt: $S00 \to S01 \to S02 \to \text{Step 1} \to \text{Step 2} \to \text{Step 3/BEC} \to \text{Step 4} \to S07 \to S08$.

#### 2. Bộ Sáu Cổng Bảo An Hệ Thống (Testing Gates G1 - G6)
* **Gate G1 (Input Validation):** Kiểm tra định dạng đầu vào.
* **Gate G5 (Output Verification):** Khớp nối kiểm tra tính toàn vẹn đầu ra và băm SHA-256.
* **Gate G6 (Matrix & Logic Consistency Check):** Kiểm tra tính đồng nhất của toàn bộ các ma trận hằng số trước khi băm SHA-256.

#### 3. Bản Thiết Kế Cấu Trúc Canonical Input Query JSON Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "DuyenDich_Unified_Query_Matrix_v3_0",
  "type": "object",
  "required": ["engine_config", "query_variables", "matrix_3x3_nodes"],
  "properties": {
    "engine_config": {
      "type": "object",
      "required": ["spec_version", "matrix_type", "expansion_mode"],
      "properties": {
        "spec_version": { "type": "string", "enum": ["v3.0_dd"] },
        "matrix_type": { "type": "string", "enum": ["3x3_Base_Query"] },
        "expansion_mode": { "type": "string", "enum": ["NxN_Tensor_Chain"] }
      }
    },
    "query_variables": {
      "type": "object",
      "required": ["actor", "target", "qualitative", "quantitative", "structure"],
      "properties": {
        "actor": { "type": "string", "description": "Chủ thể phát lực [A]" },
        "target": { "type": "string", "description": "Đối tượng nhận lực [T]" },
        "qualitative": { "type": "string", "description": "Cát/Hung, Vượng/Suy, Khí S07" },
        "quantitative": { "type": "string", "description": "Biên độ lực F_int, F_trans, f_BEC" },
        "structure": { "type": "string", "description": "Tọa độ Quẻ/Hào vị N1..N12" }
      }
    },
    "matrix_3x3_nodes": {
      "type": "array",
      "minItems": 9,
      "maxItems": 9,
      "items": {
        "type": "object",
        "required": ["node_id", "axis", "template_v3_0"],
        "properties": {
          "node_id": { "type": "string", "pattern": "^O[1-9]$" },
          "axis": { 
            "type": "array", 
            "items": { "type": "string" },
            "minItems": 2, 
            "maxItems": 2 
          },
          "template_v3_0": { "type": "string" }
        }
      }
    }
  }
}
```

#### 4. Bản Thiết Kế Cấu Trúc Canonical Output Payload JSON Schema
Bảo vệ tính toàn vẹn (G5) đối soát SHA-256 của toàn bộ 18 phân hệ thông tin đầu ra canonical băm phẳng.
