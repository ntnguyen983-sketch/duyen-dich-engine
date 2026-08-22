# Independent review: OpenAI proxy retry

Model: `gpt-5.5`

## 1. Strongest contribution

The strongest contribution of the corpus is that it correctly reframes `NxNxN / Kính Chiếu Yêu` as an **open recursive observation architecture**, not as a finite matrix, prediction engine, or binary true/false classifier.

Key strengths:

1. **Open Field is preserved**  
   `N` is not treated as one fixed cardinality. The corpus distinguishes Actor count, Relation count, Background count, topology, and emergence levels.

2. **Projection and Composition are separated**  
   `Π(X) = (Tượng, Lượng, Tính)` is clearly a projection operation, while `Combine` is a relational/topological operation. This prevents the common error of reducing Duyên Dịch to feature extraction plus scoring.

3. **18×18 is correctly bounded**  
   The proposal properly states that `18×18` is only a deployment slice for six hào × three diện per side, not the whole `NxNxN` space.

4. **Emergence is recursive, not automatic**  
   A combination only becomes a higher-level entity when it has recognizable identity, boundary, and internal structure. This is important and should be retained.

5. **Tính is kept distinct from current State**  
   The corpus correctly preserves `Tính` as rule/constraint structure, not as the current observed state.

6. **Snapshot / Dynamics / Transition / Emergence are separated**  
   This is essential for Duyên Dịch because the system observes operation, trace, accumulation, and phase change rather than issuing direct prediction.

7. **Traceability is explicitly included**  
   The requirement to preserve provenance, uncertainty, source, timestamp, layer, and λ-level aligns with Duyên Dịch governance and should be made mandatory in `DD_3a_rs`.

---

## 2. Critical ambiguities

### 2.1. `K` notation remains risky

The latest proposal uses:

```text
Π(X) = (T(X), L(X), K(X))
```

with `K = Tính`.

This is conceptually understandable, but operationally risky because `K` can be confused with:

- number of background conditions;
- kernel;
- constant;
- calibration key;
- graph degree notation;
- other mathematical variables.

**Correction:** In `DD_3a_rs`, prefer:

```text
Π(X) = (Tuong(X), Luong(X), Tinh(X))
```

or abbreviated:

```text
Π(X) = (Tg(X), Lg(X), Ti(X))
```

If `K` is retained for legacy prose, define once:

```text
K in this document means Tính only; it is not Kernel, not cardinality, and not state.
```

---

### 2.2. `Q ≥ Θ` is useful but must stay conceptual

The proposal writes:

```text
Q(X,t) ≥ Θ(K,Topology,Context)
```

This is a good conceptual expression, but it can be mistaken as an implemented threshold formula.

**Correction:** Mark it explicitly:

```text
CONCEPTUAL ONLY / RESEARCH PLACEHOLDER:
Q_eff(X,t) ≥ Θ_config(Tinh, Topology, Context, Flow)
```

No numeric threshold, weighting, decay, calibration, or transition rule should be implied.

---

### 2.3. `State = f(...)` may look like a runtime formula

The statement:

```text
State = f(T,L,K,Topology,Context,t)
```

is conceptually valid, but should not enter `DD_3a_rs` as a computational formula.

**Correction:** Use prose or tag it as non-operational:

```text
State is observed as a configuration-dependent expression of Tượng, Lượng, Tính, Topology, Context, and time.
```

If formula notation is kept:

```text
State_observed := conceptual_expression(Tuong, Luong, Tinh, Topology, Context, t)
```

and mark:

```text
Not a calibrated runtime function.
```

---

### 2.4. Emergence criteria need sharper non-numeric language

The latest proposal says a higher-level entity requires:

```text
Identity + Boundary + Internal Structure
```

This is strong, but `Boundary` and `Internal Structure` can be vague.

**Correction:** Lock a minimal qualitative test:

A combination may be promoted to `X^(λ+1)` only if all are observable:

1. **Identity:** it can be referred to as one unit across at least one observation window.
2. **Boundary:** it has a distinguishable inside/outside relative to the surrounding graph.
3. **Internal structure:** its internal relations are not reducible to isolated pairwise links.
4. **Role or effect:** it changes relation flow, accumulation, threshold condition, or interpretation at its level.

The fourth criterion is useful because a passive cluster with no role may be visually grouped but not yet emergent.

---

### 2.5. `λ` examples must remain illustrative

The list:

```text
λ0 Actor/Hào
λ1 Relation
λ2 Cluster
λ3 Network
λ4 Emergent State
```

is good, but should not become a fixed universal ladder.

**Correction:** State:

```text
The λ ladder is an observation convention for a given analysis profile. It is not a closed ontology and does not define a maximum emergence level.
```

---

### 2.6. `threshold_state` labels could be mistaken for S07 states

The research labels:

```text
PRE, CROSSING, POST, UNKNOWN
```

are acceptable as threshold observation markers, but they must be clearly separated from S07 Khí states.

**Correction:** Use a namespaced field:

```json
"threshold_phase": "PRE_THRESHOLD|THRESHOLD_CROSSING|POST_THRESHOLD|UNKNOWN"
```

and state:

```text
These are not S07 states and do not modify the Kernel S07 enum.
```

---

### 2.7. The document should not imply prediction

Some phrases such as “dự báo”, “phase transition”, or “state mới” could be misread as deterministic forecasting.

**Correction:** Add a canonical guardrail:

```text
DD_3a_rs observes operational configuration, accumulation, transition signals, and traceable emergence. It does not output binary true/false prediction and does not claim deterministic future certainty.
```

---

## 3. Precise corrections

### 3.1. Recommended canonical opening

Use this as the opening classification for `DD_3a_rs`:

```text
Document ID: DD_3a_rs
Title: Kính Chiếu Yêu / NxNxN Research Specification
Status: RESEARCH / CONCEPTUAL_LOCK
Kernel impact: NONE
S07 impact: NONE
Calibration impact: NONE
Runtime status: Non-executable ontology and architecture layer
```

---

### 3.2. Replace shorthand formula

Current:

```text
Π(X)=\big(T(X),L(X),K(X)\big)
```

Recommended:

```text
Π(X) = (Tuong(X), Luong(X), Tinh(X))
```

or:

```text
Π(X) = (Tg(X), Lg(X), Ti(X))
```

with explicit note:

```text
Tinh is the rule/constraint layer. Tinh is not current State.
```

---

### 3.3. Keep 18×18 explanation, but align with Proto v0.3

Recommended wording:

```text
For a six-hào Actor, each hào may be observed through three projection components: Tuong, Luong, Tinh. This gives 18 observable components per Actor.

For two Actors A and B, the relation field may be represented either as:

Q[i,j,a,b] ∈ 6 × 6 × 3 × 3

or flattened as:

R[(i,a),(j,b)] ∈ 18 × 18.

The 3×3 projection-interface is already included in the 18×18 representation. It must not be multiplied again as an independent fourth cardinality block.
```

---

### 3.4. Strengthen relation cell definition

Recommended relation-cell minimum:

```json
{
  "relation_cell_id": "RC-...",
  "level_lambda": null,
  "source_component": null,
  "target_component": null,
  "projection_interface": "TUONG_TUONG|TUONG_LUONG|TUONG_TINH|LUONG_TUONG|LUONG_LUONG|LUONG_TINH|TINH_TUONG|TINH_LUONG|TINH_TINH",
  "relation_type": null,
  "direction": null,
  "tuong_observation": null,
  "luong_observation": null,
  "tinh_rule": null,
  "topology_role": null,
  "context_ids": [],
  "snapshot_id": null,
  "evidence": [],
  "uncertainty": null,
  "provenance": [],
  "classification": "RESEARCH"
}
```

This should remain Research schema, not Kernel schema.

---

### 3.5. Add explicit S07 boundary

Insert in `DD_3a_rs`:

```text
DD_3a_rs does not create, rename, extend, or remap S07 states. The only canonical S07 states remain: SÁT, TÀ, NHIỄU, HỶ, DƯỠNG, ẨN; serialized as SAT, TA, NHIEU, HY, DUONG, AN. Any mapping from a 5D Khí vector to S07 requires a valid S07_MAPPING_PROFILE. Without such a profile, the correct output is MAPPING_UNRESOLVED.
```

---

### 3.6. Add explicit layer boundary

Insert:

```text
DD_3a_rs belongs to Research/Architecture. It may define observation vocabulary, conceptual flow, relation-cell structure, emergence criteria, and traceability requirements. It must not define runtime weights, calibrated formulas, thresholds, decay functions, S07 mapping, confidence conversion, or Kernel invariants.
```

---

### 3.7. Add confidence/uncertainty separation

Insert:

```text
Force, relation intensity, uncertainty, and confidence are separate fields. A force magnitude or network output must not be used directly as confidence_score.
```

This aligns with governance and prevents `f_net_out`-style mistakes.

---

## 4. What to lock in `DD_3a_rs`

The following should be locked as `RESEARCH / CONCEPTUAL_LOCK`, not as Kernel:

### 4.1. Canonical intent

```text
Duyên Dịch uses Kính Chiếu Yêu / NxNxN to observe operation, relation formation, accumulation, topology, transition conditions, emergence, and traceability. It does not use this layer to produce deterministic binary prediction.
```

### 4.2. Open Field principle

Lock:

```text
NxNxN is an open combinatorial observation field. N is not one fixed cardinality and does not require materializing an infinite matrix.
```

### 4.3. Recursive projection

Lock:

```text
Any observable entity or structure may be projected through Tuong, Luong, Tinh.
```

This includes:

- hào;
- Actor;
- background condition;
- relation;
- cluster;
- network;
- emergent state/entity.

### 4.4. Projection vs Composition

Lock the distinction:

```text
Projection decomposes observation into Tuong/Luong/Tinh.
Composition forms relations, topology, clusters, networks, and possible emergent entities.
```

### 4.5. 18×18 as a slice

Lock:

```text
18×18 is a flattened representation of six hào × three projection components per side. It is a relation-field slice, not the definition of NxNxN.
```

### 4.6. Tính/rule layer distinct from State

Lock:

```text
Tinh represents rule, constraint, relation grammar, and transformation condition. State represents the current observed expression of the system. Tinh is not State.
```

### 4.7. Snapshot/Dynamics/Transition/Emergence separation

Lock:

```text
Snapshot, Dynamics, Transition, and Emergence are separate observation records and must not be collapsed into one conclusion.
```

### 4.8. Emergence promotion criteria

Lock qualitatively:

```text
A combination becomes a higher-level entity only when it has observable identity, boundary, internal structure, and role/effect at its level.
```

### 4.9. Traceability axiom

Lock:

```text
Every projection, relation, topology update, transition marker, and emergence claim must preserve provenance, source/version, timestamp or snapshot reference, λ-level, uncertainty, and classification.
```

### 4.10. Non-impact on Kernel v3.0_dd

Lock:

```text
DD_3a_rs does not modify Kernel v3.0_dd, canonical S07, DPKE safety rules, mapping profiles, or runtime gates.
```

---

## 5. What remains Research / Placeholder

The following must remain `RESEARCH` or `PLACEHOLDER`:

1. Formula for quantifying Tượng.
2. Formula for quantifying Lượng.
3. Formula for quantifying Tính.
4. `Q_eff` definition.
5. `Θ_config` definition.
6. Any threshold number.
7. Any weight between Tượng/Lượng/Tính.
8. Any Combine function.
9. Any topology metric.
10. Any cluster detection algorithm.
11. Any emergence detection algorithm.
12. Any decay, accumulation, persistence, or flow equation.
13. Any mapping from 5D Khí vector to S07.
14. Any confidence calculation from force, relation intensity, or network output.
15. Any prediction rule.
16. Any maximum λ-level.
17. Any calibrated transition rule.
18. Any automatic promotion from relation to cluster or cluster to emergent state.
19. Any runtime JSON replacement for the current canonical schema.
20. Any new S07 state, alias, or enum.

Recommended classification:

```text
Ontology vocabulary: RESEARCH / CONCEPTUAL_LOCK
Observation schema: RESEARCH
Relation cell schema: RESEARCH
Threshold formula: PLACEHOLDER
Weights/calibration: PLACEHOLDER
S07 mapping from vector: MAPPING_UNRESOLVED unless valid profile exists
Kernel change: NOT APPLICABLE
```

---

## 6. Open questions / test vectors

### 6.1. Open questions

1. What minimum observation window is required before something can be called `Dynamics` rather than `Snapshot`?
2. What evidence is sufficient to mark a relation as existing rather than merely hypothesized?
3. What is the difference between a dense relation group and a true emergent cluster?
4. Can an emergent entity be later dissolved, and how is that dissolution recorded without rewriting its previous emergence record?
5. How should contradictory evidence be stored: separate observations, uncertainty update, or competing relation cells?
6. What is the minimal provenance requirement for manually entered interpretation?
7. Are background conditions first-class entities at `λ0`, or do they occupy a parallel background layer with their own projection?
8. When topology changes, is that recorded as a new graph snapshot or as a transition event?
9. Can one relation belong to multiple clusters at different λ-levels?
10. What is the governance path for promoting a Research schema field into a canonical runtime field?

---

### 6.2. Suggested non-calibrated test vectors

These are not numeric calibration tests. They are structural/governance tests for `DD_3a_rs`.

#### Test Vector 1 — 18×18 flattening

Input condition:

```text
Actor A has 6 hào.
Actor B has 6 hào.
Each hào is projected through Tuong, Luong, Tinh.
```

Expected result:

```text
A has 18 components.
B has 18 components.
Relation field may be represented as 18×18 or 6×6×3×3.
System must not create 18×18×3×3.
```

---

#### Test Vector 2 — Tính is not State

Input condition:

```text
Same Tinh/rule layer across two snapshots.
Luong changes between t0 and t1.
Observed State changes.
```

Expected result:

```text
The system records changed State/Dynamics.
The system does not rewrite Tinh as if the rule layer changed.
```

---

#### Test Vector 3 — Snapshot cannot imply Dynamics

Input condition:

```text
Only one snapshot is available.
```

Expected result:

```text
Snapshot may be recorded.
Dynamics must be UNKNOWN or INSUFFICIENT_DATA.
Transition must not be claimed.
Emergence must not be claimed unless independently evidenced.
```

---

#### Test Vector 4 — Emergence requires structure

Input condition:

```text
Three relations are present but disconnected.
No boundary or internal organization is observed.
```

Expected result:

```text
No X^(λ+1) is promoted.
Relations remain at relation level.
Emergence status remains UNKNOWN or NOT_OBSERVED.
```

---

#### Test Vector 5 — Emergent entity promotion

Input condition:

```text
Multiple relations form a stable cluster with observable identity, boundary, internal structure, and role/effect on flow.
```

Expected result:

```text
Cluster may be recorded as X^(λ+1).
It receives its own projection Π(X^(λ+1)).
Its provenance links back to source relations.
```

---

#### Test Vector 6 — Threshold labels are not S07

Input condition:

```text
A relation cell has threshold_phase = THRESHOLD_CROSSING.
```

Expected result:

```text
System does not treat THRESHOLD_CROSSING as an S07 state.
S07 remains only SAT, TA, NHIEU, HY, DUONG, AN.
```

---

#### Test Vector 7 — Missing S07 mapping profile

Input condition:

```text
A 5D Khí vector is available.
No valid S07_MAPPING_PROFILE is registered.
```

Expected result:

```text
Return MAPPING_UNRESOLVED.
Do not infer SAT/TA/NHIEU/HY/DUONG/AN.
Do not invent a mapping.
```

---

#### Test Vector 8 — Force is not confidence

Input condition:

```text
A relation has high Luong magnitude or high network force output.
```

Expected result:

```text
Relation intensity may be recorded.
confidence_score must not be copied from force magnitude.
Uncertainty/confidence require separate evidence logic.
```

---

#### Test Vector 9 — Background as projected entity

Input condition:

```text
A background condition modifies relation strength or threshold visibility.
```

Expected result:

```text
Background is recorded with its own Tuong/Luong/Tinh projection or equivalent research record.
Relation provenance links to background_ids.
No direct unproven causal certainty is asserted.
```

---

#### Test Vector 10 — Previous snapshot immutability

Input condition:

```text
New evidence arrives at t2 that changes interpretation of t1.
```

Expected result:

```text
t1 snapshot is not overwritten.
A new revision, inference, or interpretation layer is added with provenance.
Traceability is preserved.
```

---

## 7. Final recommendation in 5 sentences

1. `DD_3a_rs` should be accepted as a `RESEARCH / CONCEPTUAL_LOCK` artifact for Kính Chiếu Yêu / NxNxN, with no Kernel v3.0_dd change.  
2. The final version should merge the conceptual clarity of the latest proposal with the governance safeguards of Proto v0.3, especially provenance, uncertainty, layer separation, and S07 boundaries.  
3. All formulas involving `Q`, `Θ`, weights, topology metrics, Combine functions, cluster detection, emergence detection, and 5D vector mapping must remain `RESEARCH` or `PLACEHOLDER` until valid profiles and test vectors exist.  
4. The artifact should explicitly state that Duyên Dịch observes operation, accumulation, topology, transition signals, and traceable emergence, not deterministic true/false prediction.  
5. I recommend locking the ontology, vocabulary, recursive flow, relation-cell concept, emergence criteria, and traceability requirements now, while deferring every numeric or calibrated operational mechanism to later governed research.
