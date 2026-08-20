# Ma trận nguồn viết lại Duyên Dịch v3.1

## Mục tiêu

Bản v3.1 mới phải là một đặc tả viết lại hoàn chỉnh, không chỉ là contract-first skeleton. Tuy nhiên, mọi công thức, enum, mapping và tham số vẫn phải có provenance. Nguồn Google Docs được xem là bản đọc/biên soạn; PDF cùng tên là artifact bất biến dùng để đối chiếu hash và phát hiện sai khác.

## Nguồn ưu tiên theo lớp

| Lớp | Nguồn ưu tiên | Document ID | Dự kiến sử dụng | Trạng thái ban đầu |
|---|---|---|---|---|
| L1 lý thuyết động lực | v2.5.3 Engine Specification | `1T_VN8r5g2uKzT7vgL3Us4Fp-w2V_NNYRMTfA6PTHKsQ` | Ψ, tiên đề Level -1, primitive quantities, SDE/Bellman và phase operators nếu còn nhất quán | cần đối chiếu |
| L1/L2 lực động | v2.5.5 Dynamic Force Propagation | `1f-gwNp8jNrI-RPHXn2Uv-oh-KL1Yt_PwUXepFlxfeys` | dynamic force, propagation, lực và điều kiện vận động | cần đối chiếu |
| L2 runtime/engine | v2.5.6 Master Spec A/B | `1oMqaomdvflTbu6b-tGcKtML5pJmMVtEYESagB2TFbjI`, `15TXjkKCeZx3hqLj1_vm_uzp6pc-jk95mFWUlbDSqacA` | engine contract, operators, pipeline và các khác biệt nội bộ v2.5.6 | đối chiếu xung đột |
| L2/L3 trường | v2.8.6 Master Spec | `1LgvaWOndVxnBpi7p-6OPARZqJZ47TgmhB-Ii-b1losc` | DCGF/SL-DIF, nodes, topology, interaction và pipeline | nguồn chính cần kiểm chứng |
| L2/L3 trường | Tổng quan DCGF & SL-DIF v2.8.6 | `1_qS9DgvaUUyGLIEfIHQCX-nSlqfksTIdbHE1OdIraio` | kiến trúc và ranh giới field | nguồn tóm tắt |
| L2/L3 BEC | BEC Unified Logic & System Dynamics v2.8.7 | `112YN7bwAHHebKLa5Amd_fFtVkQ5079Z-AZQk3XzVHBM` | Frozen Core, 12-stage pipeline, SIE, Vector Khí 5D, DWL, DPKE, BEC | nguồn thuật toán cần audit |
| L2/L3 hợp nhất | v2.8.7 Full Spec | `1lZfkQh1TOeKpixEcqSlj44y-287zepzoQDtEputPhBc` | bản hợp nhất gần nhất trước v2.9 | cần đối chiếu |
| L2/L3 hiệu chỉnh | v2.8.7 Rev.A | `1Ej3_pUFVeIbg2gYg7LgBM5-7WzIV-c4rYa1OM5nUU8M` | precedence, Rev.A axioms, delay và boundary corrections | candidate canonical nếu đủ căn cứ |
| L2/L3 merge history | ghi chú merge v2.8.6 → v2.8.7 | `1mtIV18E4HT6V7LtgdXNJIORG4v6z-nOcxdiNQ3VDYZw` | truy vết thay đổi, không dùng trực tiếp làm Core | provenance |
| L2/L3 v2.9 | SL-DIF summary v2.9 | `1kVh7Ao43C9wmKcXSWB3xDoqUNaqId1Ec2Y19AxXF2UU` | thay đổi kiến trúc động lực học | nguồn kiến trúc |
| L2/L3 v2.9-D | Decoupled Dynamic Field Architecture | `1xAZW_II3kpbeGIY_TRQ8mgUpkU5xGoS56f5RbxmJXlk` | decoupling và dynamic field | phải hòa giải với SL-DIF/BEC |
| L2/L3 v2.9-D | DD-CORE v2.9-D extended | `1VFxfiI7PYIH2JLEM8gYeWmH1xiCnNrDG4Zyv62VHOKI` | mở rộng kiến trúc, kiểm xung đột | research/architecture |
| L3/L4 runtime | engine v2.9 | `1Bdh5FzTSKPE-7DEGq8Eep3h2yVysKdh3ttnjOsPDSTE` | execution core, forward-only, semantic firewall, Vector Khí và state pipeline | implementation contract |
| L3 runtime | Py v2.9.3 | `1nGmMp7Gg5PVc9QeYpmTr7HKIVpGXcBNqDQ52vrO3LX8` | code-like runtime, formulas, guard conditions và edge cases | implementation evidence |
| L3/L4 | v2.9 overview | `1JuxJGg6MQLsn5Jfz3wT4x2BQArtqjsCOzN_by2hNWLo` | tổng hợp runtime và semantics | nguồn phụ |
| L3/L4 | v2.9.1 | `1I5oxn-p8KxY8Fz62_fljBGgcW3u2XRSqTrgDKMrE0OQ` | phiên bản cập nhật runtime/contract | cần đối chiếu |
| L3/L4 | v2.9.1 NEW2 | `180a8LwwV1OH3H2claoO89xih8h55lUY9tdbNgp0vTY0` | patch/alternate runtime | cần đối chiếu |
| L4/L5 mapping | v3.0.0 | `1OaIykatXspd9HlDds6WeBHtQC0P7DAv3DEc93wKi_Dg` | canonical authority hiện hành, S07/vocabulary/schema/gates nếu có | authority mặc định |
| L5 contract | FULL_SPEC | `1BJCioeFBFmM943AT5rlB9-1ej0gLbo9F19WDNM_a8Ig` | hợp nhất cũ để truy vết nội dung và phát hiện phần bị bỏ qua | historical composite |
| L6 interface | Wireframe v3.1_dd | `1JbIawa-_iM2mXF2hDBXwWeV1xFA4krA7evcGslp_mSI` | UI/Operations contract, không chứa compute | interface source |
| L2/L3 bridge | DCGF v2.9/v3.0 SL-DIF integration | `14xJhKrOTsG2hlpbWl2L4x8dqgjByAvbndRJsmkkPwMM` | proposed integration, kiểm tra không nâng research thành Core | integration source |
| research support | Tri thức v2.9-gem | `1E0QxJp2385tBpi7p-6OPARZqJZ47TgmhB-Ii-b1losc` | chỉ dùng để tìm giả thuyết/câu hỏi mở, không làm authority | research only |

## Quy tắc xử lý nguồn

1. **v3.0.0 là canonical authority mặc định** cho enum, schema, gates và invariants; các nguồn cũ chỉ được nâng lên Core khi không xung đột và có provenance rõ.
2. **v2.5 là nền lý thuyết**, không được đưa trực tiếp vào runtime nếu v2.8/v2.9 đã thay thế operator hoặc pipeline.
3. **v2.8.6/v2.8.7 là nguồn field/BEC**, nhưng mọi ngưỡng, calibration và công thức phải đối chiếu với runtime v2.9/v2.9.3 trước khi khóa.
4. **v2.9/v2.9.1/v2.9.3 là runtime evidence**, nhưng code-like text không tự động là canonical nếu không tương thích với v3.0.0 contract.
5. **S07 chỉ được khóa khi tìm thấy profile có profile_id/version/hash/effective domain/parameters/test vectors**. Nếu không, tài liệu phải viết đầy đủ cơ chế unresolved, không viết giả mapping.
6. **Gemini chỉ được đề xuất và phản biện**. Quyết định cuối cùng phải ghi trong decision log, có test vector và provenance.

## Khoảng phải truy nguyên khi viết lại

| Khoảng hiện tại | Nguồn cần tìm trong corpus | Điều kiện nâng thành CORE |
|---|---|---|
| Ψ/SDE/Bellman/phase operators | v2.5.3, v2.5.5, v2.5.6 | định nghĩa không mâu thuẫn với field runtime và có test |
| SL-DIF/BEC và SIE | v2.8.6, v2.8.7, BEC Unified, v2.9 | boundary, state transition và input/output rõ |
| matrix/delay/DPKE | BEC Unified, engine v2.9, Py v2.9.3, Rev.A | công thức nhất quán, guard/epsilon/biên rõ |
| S07 semantic mapping | v3.0.0, full specs, Docs có S07/profile | profile version/hash/domain/test vectors |
| canonical JSON | v3.0.0, engine v2.9, current schema | schema và compatibility không mâu thuẫn |
| UI/Operations | wireframe v3.1_dd, v3.0.0 | chỉ gọi API, không chứa compute |

## Ghi chú provenance

Ngày thu thập: 2026-08-20. Các Document ID là định danh Drive; mọi trích dẫn trong đặc tả mới phải giữ `source_document_id`, tiêu đề nguồn, version, thời điểm thu thập và hash nếu là PDF/binary. Markdown được tạo từ Google Docs chỉ là bản trích xuất phân tích, không thay thế artifact nguồn.
