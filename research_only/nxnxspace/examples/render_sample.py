from __future__ import annotations

import json
from pathlib import Path

from research_only.nxnxspace import compute


snapshot_path = Path(__file__).with_name("sample_snapshot.json")
snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
print(json.dumps(compute(snapshot), ensure_ascii=False, indent=2, sort_keys=True))
