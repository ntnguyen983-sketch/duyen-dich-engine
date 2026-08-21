# SOURCE_CONFLICTS — External enrichment

## CONFLICT-1 — Binary string orientation (hexagram tables)

| Side | Claim | Source |
|---|---|---|
| A | Bit 0 = bottom line (line 1); KW#1 Qian binary integer 63 | arXiv 2601.07175 |
| B | Binary column published without stating top/bottom | Wikibooks 64 Hexagrams table |
| C | DD engine: `root_bits[0]` = line 6 (MSB of `root_code`) | runtime/v31/engine.py |

**Resolution in library:** Keep **both** candidate `root_code` fields on each external hexagram record. Do not silently pick one. CORE identity continues to use engine indexing only.

## CONFLICT-2 — English hexagram titles

| Side | Example (hex 7 師) | Source |
|---|---|---|
| Huang / Wikibooks | Multitude | Wikibooks note |
| Wilhelm/Baynes | The Army | traditional EN translation |
| Legge | The Army | classical EN |

**Resolution:** Store Wikibooks/Huang string as `name_en_huang_wikibooks`. Do not claim a single English title is universal.

## CONFLICT-3 — Wuxing assignment to trigrams

Correlative cosmology maps (Metal/Wood/…) vary by school (Pre-Heaven vs Post-Heaven applications). Secondary web tables differ in emphasis.

**Resolution:** Mark all wuxing fields `REFERENCE_SECONDARY`. Not used as CORE fact.

## CONFLICT-4 — Correct position (正位)

Secondary rule “yang on odd lines, yin on even” is common in later commentary pedagogy but is not a single locked Zhouyi CORE table in this repository or a unique primary edition cited here.

**Resolution:** One REFERENCE profile only; confidence 0.5; not elevated.

## No conflict recorded for

- Chinese King Wen names (乾, 坤, …) — stable across Wikipedia / Wikibooks.
- Eight trigram Chinese names and symbols.
- NxNxspace — absent everywhere searched.
