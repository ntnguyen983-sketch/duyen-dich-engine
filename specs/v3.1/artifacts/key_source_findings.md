# Key source findings for complete v3.1 rewrite

## Sources read

1. `v2_5_3_engine_spec` — Google Doc `1T_VN8r5g2uKzT7vgL3Us4Fp-w2V_NNYRMTfA6PTHKsQ`.
2. `v2_5_6_master_b` — Google Doc `15TXjkKCeZx3hqLj1_vm_uzp6pc-jk95mFWUlbDSqacA`.
3. `bec_unified_logic` — Google Doc `112YN7bwAHHebKLa5Amd_fFtVkQ5079Z-AZQk3XzVHBM`.
4. `engine_v2_9` — Google Doc `1Bdh5FzTSKPE-7DEGq8Eep3h2yVysKdh3ttnjOsPDSTE`.
5. The complete source corpus is stored under `/home/ubuntu/dd_v31_source_docs_text/` and the comparison report is `/home/ubuntu/dd_v31_source_comparison.md`.

## v2.5 theory/runtime evidence

The v2.5.3 and v2.5.6 documents define `Ψ` as the primitive Configuration Potential and derive `E = ||Ψ||²`, `F = -∇Ψ`, and a potential surface `U = -∫G Ψ`. They define a 13-layer architecture with space, force, field, potential, interaction, evolution, state evaluation, prediction, Bellman strategy and feedback. v2.5.6 adds the dynamic distinction `F0` (five non-moving channels) and `ΔF` (moving-line impulse), the six force channels `C1...C6`, and a 12-phase operator sequence:

`P1 Birth Impulse → P2 Acceleration → P3 Growth → P4 Expansion → P5 Peak → P6 Transmission → P7 Interaction → P8 Transformation → P9 Decay → P10 Collapse → P11 Residual → P12 Reset`.

v2.5.6 gives a deterministic pipeline for `F0`, `ΔF`, phase propagation, field `Φ`, energy/potential, interaction tensor `K`, and SDE evolution. It also includes a C++ runtime example with `ENGINE_NORM_BASE=38.138`, `DEFAULT_R_BASE=10.0`, `SPEED_BASE=25.0`, speed bounds 20–50, a 12-element Chi ring, and helper functions for Chi channel allocation and final speed. These constants and C++ examples are implementation evidence, not automatically v3.1 Core invariants.

## v2.8.7 BEC/SL-DIF evidence

The BEC Unified document defines Frozen Core, Reflection, Motion, No-self, Traceability, Condition-dependence and Model Separation. It defines A0–A12 axioms, including external injection/decay, Vector Khí as geometry rather than causal evidence, semantic independence, calibration labels, tick-only state transition, Observer Rule, uncertainty disclosure, read/write separation and separate qualitative/quantitative fields.

Its pipeline is `S00 Raw Input → S01 Canonical Core/Lock → S02 Structural State → S03 Topology → S04 Firewalls/Gates → S05 DWL/Force → S06 L2-RGS → S07 DPKE/Spacetime → S08 Emergence → S09 BEC Observation → S10 Knowledge Mapping → S11 Reporting`.

It defines six-bit operators `M_k` flip, `P` reverse, `C` complement and `H` nuclear extraction. It defines `V_Khi = [S,D,I,F,T]^T`; SIE is a registry and must not invent numeric values without an official profile. The DWL candidate formula is `W_ij = B_ij * (1 + αP_ij + β A_ij/(A_max+ε)) * F_norm` with `α=0.15`, `β=0.20`, `ε=1e-6`, plus quarantine on denominator risk. Force is `F_field_raw = Σ(W_ij D_ij)` and `F_norm = ||F_field_raw||/(4.0 N_edges+ε)`. L2-RGS uses Procrustes and emits `RIGID_FIT`/warning.

The DPKE candidate is `v_base = v_final/50`, `v_raw = v_base + α f_net - β w_resist`, `v_i=Round(Clamp(v_raw,0.1,2.0),6)` and `delay_i=Clamp(Round(Σ(1+μ_topology,i)/v_i),0,12)`. It gives `T_real=t0+Δt_base+delay_i±σ_time` and half-open azimuth sectors with 315° assigned to the next sector. BEC candidate states include `NO_EMERGENCE`, `STABLE_EMERGENCE`, and an H1 Drain/Reserve hypothesis with `D(t)=D0 exp(γ Ω_Force)(1+η FD_drag)`, `R(t+1)=max(0,R(t)-D(t)Δt)`, and a circuit breaker.

The same document explicitly says calibration components may evolve but may not mutate Core Identity. These formulas and thresholds need profile/version/test-vector checks before promotion to Core.

## v2.9 engine evidence

The v2.9 engine document defines `DETERMINISTIC_FORWARD_ONLY` and `SEMANTICALLY_ISOLATED_KERNEL`. It states the one-way flow `Reality → Observation → Snapshot(t0) → S00...Topology → DWL → SL-DIF → Vector Khí → State → Decoder → Interpretation → S12 → Audit`. It defines `V_Khi=[S,D,I,F,T]`, with S derived from moving-line groups, D from directional delta, I from actual/max SIE interactions, F as `F_norm`, and T as runtime phase in Z12.

It gives a competing spacetime formula `T_real=t0+τ_trigger*BASE_SCALE(C)*(50/v_final)`, delay `Δt_delay,i=Clamp(Round((W_resist,i/v_final)(1+μ_topology)),0,12)`, and `σ_time=|F_max-F_min|/(F_norm+ε)*(1-v_final/100)`. It lists BEC states `LATENT_ACCUMULATION`, `TRANSIENT_FORCE`, and `NO_EMERGENCE`; its symbolic mapping still contains the legacy `Ân` label and explicitly marks mapping as calibration-required. This is a source conflict that v3.1 must resolve by canonical vocabulary/decoder separation.

## Canonical rewrite implications

- Keep Ψ, F0/ΔF, 12 phase operators, six-bit operators and forward-only pipeline as fully written modules with source provenance.
- Convert the 13-layer v2.5 model into L1 theory/reference and map its executable portions to v3.1 L2/L3; do not run Bellman/feedback by default.
- Use the v2.8.7 12-stage pipeline as the executable staging model, but preserve v3.1 six-layer architecture at the document boundary.
- Keep SIE, S07 mapping and BEC calibration as explicit registries/profiles with full interfaces, validation, failure modes and test vectors. A missing/invalid profile must produce unresolved/quarantine state rather than a guessed label.
- Do not use legacy `Ân` as canonical `AN`; `AN` is the serialize code for canonical `ẨN` only. Legacy labels remain Compatibility-only.
- Do not promote `α`, `β`, `ε`, `γ`, `η`, thresholds, or speed/radius constants to invariants solely because a source states them. They require profile IDs, version, hash, effective domain and test vectors.

## Additional v2.8.6 and v2.9.1_new2 findings

The v2.8.6 master gives the pipeline `S00 Raw Input → S01 Normalize/|Q⟩ → S02 Structural Decode → S03 Topology/12-line grid → S04 Rigid Check Separation → DWL-0.1 → S05 Force/Field → S06 Vector Khí → Gates 1–5 → S07 Emergence → S08 Spacetime/temporal decision → Canonical JSON/SHA-256`. It defines `Q∈Z₂⁶`, upper/lower trigrams, normalized Mai Hoa modulo rules, six-bit operators `D_i`, complement `C`, reverse `P`, nuclear `H`, Node schema, Chi ring mapping with default Step=2, and a 10×10 Mpol matrix.

The v2.8.6 Override Cascade is ordered: Tam Hợp/Lục Hợp `+1.5`, Khắc Nhập `-2.0`, Khắc Xuất `-1.5`, Sinh Nhập `+1.2`, Sinh Xuất `-1.0`, Tỷ Hòa `+1.0`, stopping at first match. It defines DWL components `W_ij=B_ij K_context K_interaction K_time`, domains `B∈[0,1]`, `K_context∈[0,2]`, `K_interaction∈[0,1]`, `K_time∈[0,2]`, hence `W∈[0,4]`; persistence `P_ij=N_active/N_observed` and accumulation `A_ij=ΣW_ij`. It defines `F_field_raw=ΣW_ij D_ij`, theoretical max `4N_edges`, and `F_norm=||F_raw||/(4N_edges)`.

It defines `V_Khi=[S,D,I,F,T]`, with `S∈{0,0.5,1}` from moving-line layer, `D=ΔH·ψ`, `I=actual/max SIE`, `F=F_norm`, and `T∈Z12`. It also gives `v_final=Clamp(SPEED_BASE+5F+R/2,20,50)`, L2-RGS output fields/status, 12 Life-stage topology and spacetime formulas: `T_real=t0+τ_trigger·BASE_SCALE(C)·(50/v_final)`, actor delay `Clamp(Round((W_resist/v_final)(1+μ_topology)),0,12)` with μ=1.5 for Tử/Mộ/Tuyệt, μ=0.8 for Suy/Bệnh, μ=0 otherwise, and `σ_time=|Fmax−Fmin|/(F_norm+ε)(1−v_final/100)`. These are source candidates; profile registration and tests are still required.

The v2.9.1_new2 document is the strongest historical source for a concrete S07 candidate. It defines a 12×12 NodeSpace for root+transformed six-line nodes, node force vector `[f_net_out,f_BEC,L_Element]`, OverrideCascade values and the same DWL formula with `α=0.15, β=0.20, ε=1e−6`, BEC density `f_BEC(t)=sigmoid(λ Σ f_net_out(τ)e^(−γ(t−τ)))` with default `λ=0.35, γ=0.08`, MSIE 3×3 values, MFlux 5×5 values, and a 60-tick synchronization cycle `LCM(12,5,12)=60`. It explicitly gives the six S07 labels and threshold rules:

- `DƯỠNG`: `I≥0.70 ∧ D>0.2 ∧ F≥0.5`
- `HỶ`: `I≥0.60 ∧ D>0.5 ∧ S≥0.5`
- `ẨN`: `I·S<0.30 ∧ F≤0.4`
- `NHIỄU`: `|D|≤0.2 ∧ F>0.6 ∧ I∈[0.3,0.6]`
- `TÀ`: `D<−0.3 ∧ F≥0.7 ∧ S<0.30`
- `SÁT`: `I<0.30 ∧ D<−0.5 ∧ F≥0.6`

It also gives ROM mapping of lines 1–6 to Địa Nội/Địa Ngoại/Nhân Nội/Nhân Ngoại/Thiên Nội/Thiên Ngoại and the actor delay formula with `simulation_ticks/v_i`. This profile is complete enough to be written as a named historical candidate profile, but it lacks an independent profile hash, explicit test-vector suite and formal effective-domain metadata; therefore v3.1 should not silently treat it as a default canonical profile. It can replace a blank placeholder with a fully specified `CALIBRATION_REQUIRED`/`RESEARCH` profile and deterministic unresolved behavior until registered.

## BEC Unified Logic v2.8.7 findings

BEC Unified defines a Frozen Core: reflection, motion, no-self, traceability, condition-dependence and model separation. Rev.A axioms A0–A12 include binary state, existence bounds, closed-system decay with external injection, semantic-free Vector Khí, independent decoder, calibration labeling, kernel-only transitions, observer evidence at t+1, uncertainty disclosure, read/write separation, qualitative/quantitative separation and mandatory calibration for quantitative outputs. Its 12-stage pipeline is S00 Raw Input, S01 Canonical Core/Core Lock, S02 Structural State, S03 Topology, S04 Gates, S05 DWL/Force, S06 L2-RGS, S07 DPKE/Spacetime, S08 Emergence, S09 BEC Observation, S10 Knowledge Mapping, S11 Reporting. `initialize(raw_input)` only establishes identity at initialization; `observe(state,evidence)` appends future evidence without resetting identity; no feedback writes into history.

BEC Unified confirms structural operators Mk/flip, P/reverse, C/complement and H/nuclear extraction, with no semantic result at the structural layer. SIE is a registry, not a place to invent new numeric values. DWL uses `W_ij=B_ij(1+αP_ij+βA_ij/(A_max+ε))F_norm`, α=0.15, β=0.20, ε=1e-6, and quarantines on division-by-zero risk; `F_norm=||F_field_raw||/(4N_edges+ε)`. DPKE uses `v_base=v_final/50`, `v_raw=v_base+αf_net−βw_resist`, `v_i=round(clamp(v_raw,0.1,2.0),6)`; BEC reporting precision is 4 decimals. BEC emergence states include `NO_EMERGENCE` and `STABLE_EMERGENCE`, with threshold variables θI, θF, θP, θA. Drain/reserve H1 is explicitly a hypothesis family: `D(t)=D0 exp(γΩForce)(1+ηFD_drag)`, `R(t+1)=max(0,R(t)−D(t)Δt)`, circuit breaker when `R≤Threshold_stop`; it must not be treated as calibrated CORE without registry evidence.

Important conflict: BEC Unified states a Rev.A delay `Clamp(Round(Σ(1+μ_topology,i)/v_i),0,12)`, while v2.8.6/v2.9 and v2.9.1_new2 state actor-local delay with `W_resist/v_final` plus `simulation_ticks/v_i`. v3.1 must expose these as named formula profiles and select one only through a versioned runtime profile; no silent merge. The BEC document also names Output A structural and Output B BEC/projection branches, canonical JSON sorted keys and SHA-256, and G1–G5 schema/identity/core-lock/research/canonical checks.
