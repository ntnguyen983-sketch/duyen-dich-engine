# Duyên Dịch v3.1

Đây là repository canonical integration cho đặc tả **Duyên Dịch v3.1 — full rewrite**. Sáu phụ lục được hợp nhất theo lớp kiến trúc thay vì gộp tuần tự theo version. Bản release bao gồm định nghĩa, công thức, pseudocode, profile, guards, gates, error behavior, provenance, JSON contract, test vectors và runtime runnable có trạng thái rõ ràng.

## Thành phần

| Thành phần | Đường dẫn | Trạng thái |
|---|---|---|
| Đặc tả hợp nhất đầy đủ | `specs/v3.1/DUYEN_DICH_v3.1.md` | Release candidate / full specification |
| Từ vựng S07 | `specs/v3.1/canonical_vocabulary.json` | CORE enum + compatibility aliases |
| S07 profile | `specs/v3.1/s07_mapping_profile_v31.json` | Profile có rule/vector; `CALIBRATION_REQUIRED` |
| Runtime profiles | `specs/v3.1/runtime_profiles_v31.json` | Matrix, delay, DWL, BEC, topology và provenance |
| Runtime v3.1 | `runtime/v31/` | RUNNABLE / PROVISIONAL |
| Legacy decoder | `specs/v3.1/compatibility/legacy_decoder.json` | COMPATIBILITY; read-only |
| JSON Schema | `specs/v3.1/schemas/canonical_response.schema.json` | CORE data contract |
| Decision log | `specs/v3.1/artifacts/decision_log.md` | Provenance và quyết định review |
| Gemini Vòng 1/2 | `gemini_rewrite_round1.json`, `gemini_rewrite_round2.json` | Review artifacts |
| Source matrix/findings | `specs/v3.1/artifacts/source_matrix_rewrite.md`, `specs/v3.1/artifacts/key_source_findings.md` | Source traceability |
| Release handoff | `RELEASE_HANDOFF.md` | Điều kiện phát hành và giới hạn |
| Runtime CI | `.github/workflows/v31-runtime.yml` | Automated regression |

## Kiến trúc và firewall

Kernel v3.1 chỉ chấp nhận sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`. Nhãn lịch sử chỉ được đọc ở compatibility decoder và không được tự động ép sang mã canonical. Luồng dữ liệu là forward-only từ S00 đến S11. Runtime chỉ phát số liệu và trace; mapping S07 là read-only và không được ghi ngược vào Kernel. Confidence audit bắt buộc loại `f_net_out` khỏi input và phải ghi `f_net_out_found=false`.

Runtime v3.1 chạy L1→L6 end-to-end. Các toán tử field và S07 mapping trong cây runtime được đánh dấu **PROVISIONAL** khi chưa có profile active; provenance và gate luôn ghi rõ trạng thái. Khi có phụ lục hoặc profile được phê duyệt, chỉ thay toán tử tương ứng, không phá contract hoặc regression tests.

`CALIBRATION_REQUIRED` không phải placeholder. Đó là trạng thái có profile, domain, hash, điều kiện kích hoạt, behavior khi chưa active và test vector. S07 activation, RGS normalization, BEC lambda/gamma và threshold profile vẫn cần calibration/approval. Chu kỳ 60 ticks, H1 Drain/Reserve và causal/phase interpretations là `RESEARCH`, không được dùng như CORE hoặc semantic action.

## Kiểm định đặc tả

```bash
cd specs/v3.1
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m json.tool runtime_profiles_v31.json >/dev/null
python3 -m json.tool s07_mapping_profile_v31.json >/dev/null
python3 -m json.tool canonical_vocabulary.json >/dev/null
python3 -m json.tool schemas/canonical_response.schema.json >/dev/null
```

## Kiểm định runtime

```bash
python3 -m unittest discover -s runtime/v31 -p 'test_*.py' -v
```

GitHub Actions tự chạy runtime regression trên push và pull request. Bộ kiểm định đặc tả xác nhận enum canonical, legacy isolation, S07 rule/boundary vectors, profile hash, runtime guards, confidence firewall, complete runtime contract, 60-tick/H1 research classification và decision log.
