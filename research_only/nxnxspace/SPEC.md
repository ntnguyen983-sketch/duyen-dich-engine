# NxNxspace Phase 1–2 Specification

**Namespace:** `research_only.nxnxspace`
**Status:** `research_only`
**Version:** `0.1.0-research`

## 1. Mục tiêu

Với một snapshot bất biến gồm `tick_id` và danh sách entity có vector số, prototype tạo ra một ma trận cosine similarity kích thước `N×N`. Mô-đun chỉ tính toán trên snapshot/mock data được truyền trực tiếp vào hàm; không đọc runtime state, canonical store, database, realtime source hoặc bất kỳ output nào của CORE.

## 2. Input snapshot schema

Input tối thiểu:

```json
{
  "tick_id": 42,
  "entities": [
    {"id": "entity_A", "vector": [0.2, 0.8]},
    {"id": "entity_B", "vector": [0.6, 0.4]},
    {"id": "entity_C", "vector": [0.9, 0.1]}
  ]
}
```

`tick_id` là số nguyên không âm. `entities` là mảng có thể rỗng. Mỗi entity có `id` chuỗi không rỗng và `vector` là mảng số thực hữu hạn, không rỗng. Mọi vector trong một snapshot phải có cùng số chiều. ID trùng nhau bị từ chối. Các field ngoài schema được phép tồn tại trong input nhưng bị bỏ qua bởi phép tính và không được đưa vào deterministic input hash.

## 3. Công thức và quy ước số học

Với hai vector `a` và `b`:

```text
cosine(a,b) = dot(a,b) / (||a||₂ × ||b||₂)
```

Nếu một trong hai vector là zero vector, cosine được quy ước là `0.0`. Prototype tính nửa tam giác trên rồi mirror sang nửa còn lại, nên `matrix[i][j] == matrix[j][i]` bằng cả giá trị và biểu diễn sau rounding 12 chữ số. Các giá trị `-0.0` được chuẩn hóa thành `0.0`.

## 4. Output contract

Output thành công có namespace/status riêng:

```json
{
  "namespace": "research_only.nxnxspace",
  "status": "research_only",
  "N": 3,
  "tick_id": 42,
  "timestamp": "2026-08-21T00:00:00Z",
  "deterministic_input_hash": "<sha256>",
  "entity_vectors": [
    {"id": "entity_A", "vector": [0.2, 0.8]},
    {"id": "entity_B", "vector": [0.6, 0.4]},
    {"id": "entity_C", "vector": [0.9, 0.1]}
  ],
  "cosine_similarity_matrix": [[1.0, 0.739940073396, 0.348186529604], [0.739940073396, 1.0, 0.888217643156], [0.348186529604, 0.888217643156, 1.0]],
  "space_state": {
    "kind": "cosine_similarity_snapshot",
    "dimension": 2,
    "zero_vector_count": 0,
    "pairwise_mean": 0.658781415385,
    "pairwise_min": 0.348186529604,
    "pairwise_max": 0.888217643156
  },
  "time_axis": {"kind": "discrete_tick", "tick_id": 42, "unit": "tick"}
}
```

`timestamp` lấy từ input nếu có; nếu không có, runtime gắn UTC timestamp hiện tại cho metadata. Timestamp không ảnh hưởng đến matrix, `space_state` hoặc deterministic input hash.

## 5. Hash canonicalization

Hash input dùng đúng object:

```json
{"entities":[...],"tick_id":42}
```

Object được serialize UTF-8 bằng JSON canonical với sorted keys và separators `(',', ':')`, sau đó SHA-256. Entity order được giữ nguyên vì thứ tự hàng/cột của matrix phụ thuộc snapshot order. Không dùng timestamp tự sinh, không dùng số ngẫu nhiên, không gọi Gemini/API AI và không dùng `f_net_out`.

## 6. Failure behavior và isolation

`compute(snapshot)` ném `NxNxspaceValidationError` cho input sai. `safe_compute(snapshot)` bắt riêng validation error và trả envelope research-only gồm `error`, `error_code`, `namespace` và `status`; nó không import hoặc gọi CORE. Các lỗi ngoài validation không bị nuốt. Vì module không được đăng ký vào bất kỳ pipeline nào, lỗi NxNxspace không làm CORE lỗi và cũng không thể làm CORE thay đổi.

## 7. Bất biến kiểm thử

Prototype phải kiểm tra N=0, N=1, N=3, duplicate entity, invalid vector, zero vector, repeat cùng input cho matrix/state/hash, symmetry của matrix, failure isolation và static boundary không có import/path ghi ngược vào CORE. Không có test nào được phép sửa file ngoài namespace `research_only/nxnxspace/`.
