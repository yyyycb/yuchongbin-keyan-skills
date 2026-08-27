#!/usr/bin/env python3
"""Create a non-destructive research idea discovery run directory."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ARTIFACTS = {
    "00-intake.md": """# Discovery Brief

## Topic
[FILL]

## Operating mode
[FILL: full discovery | taste study | defect mining | reframe]

## Target community and paper shape
[FILL]

## Resources
- Compute: [FILL]
- Data access: [FILL]
- Team and expertise: [FILL]
- Time: [FILL]

## Quality thresholds
- Open-source requirement: [FILL]
- Star rule: [FILL]
- Citation/recognition rule: [FILL]

## Exclusions and non-goals
[FILL]
""",
    "01-corpus.md": """# Verified Quality Corpus

## Retrieval provenance
- Search date: [FILL]
- Sources/indexes: [FILL]
- Normalization and caveats: [FILL]

## Corpus

| ID | Title | Year | Venue | Recognition | Citation evidence | Official repo | Stars | License | Role | Caveat |
|---|---|---:|---|---|---|---|---:|---|---|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Coverage gaps
[FILL]
""",
    "02-genealogy-cards.md": """# Idea Genealogy Cards

## Genealogy 1: [FILL]

### Verified position
[FILL]

### Before the paper
[FILL]

### Generative evidence
[FILL]

### Intellectual move
[FILL]

### Method derivation
[FILL]

### Evidence design
[FILL]

### Later inheritance
[FILL]

### Transferable taste lesson and boundary
[FILL]
""",
    "03-taste-ledger.md": """# Research Taste Ledger

## [FILL: date and case]
- Decision made before outcome: [FILL]
- Confidence: [FILL]
- Evidence used: [FILL]
- Outcome or revealed paper: [FILL]
- Error type: [FILL]
- Missed factor: [FILL]
- Updated scoped judgment: [FILL]
- Where the update does not apply: [FILL]
- Next discriminating test: [FILL]
""",
    "04-defect-cards.md": """# Defect Cards

## Defect 1: [FILL]
- Anchor and commit/release: [FILL]
- Expected behavior: [FILL]
- Observed failure: [FILL]
- Protocol and independent unit: [FILL]
- Recurrence: [FILL]
- Evidence level D0-D4: [FILL]
- Current metric visibility: [FILL]
- Stakeholder consequence: [FILL]
- Alternative explanations: [FILL]
- Cheapest next test: [FILL]
- Evidence links: [FILL]
""",
    "05-causal-diagnoses.md": """# Causal Diagnoses

## Phenomenon: [FILL]

| Explanation | Causal path | Distinct prediction | Discriminating intervention | Cost | Result/status |
|---|---|---|---|---|---|
| Implementation/tuning | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Data/evaluation artifact | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
| Structural explanation | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Current conclusion, confidence, and ambiguity
[FILL]
""",
    "06-transfer-matrix.md": """# Requirement Derivation and Structural Transfer

## Diagnosis-to-method derivation

| Diagnosis | Requirement | Mechanism component | New prediction | Test |
|---|---|---|---|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Structural transfer matrix

| Target causal relation | Donor causal relation | Preserved structure | Broken assumption | Required adaptation | New prediction |
|---|---|---|---|---|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Rejected surface analogies
[FILL]
""",
    "07-candidate-portfolio.md": """# Paper-shaped Candidate Portfolio

## Candidate 1: Field-shaping problem/task — [FILL]
- Two-sentence field claim: [FILL]
- FACT: [FILL]
- OBSERVATION: [FILL]
- INFERENCE: [FILL]
- HYPOTHESIS: [FILL]
- Problem independent of method: [FILL]
- Causal insight: [FILL]
- Method derivation: [FILL]
- Field contribution and durable fallback: [FILL]
- Prior-art search cutoff and sources: [FILL]
- Closest full-text works: [FILL]
- Load-bearing novelty axis: [FILL]
- New prediction absent from closest work: [FILL]
- Novelty decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Figure 1: [FILL]
- First kill gate: [FILL]
- Resource fit and leverage: [FILL]

## Candidate 2: Mechanism-centered — [FILL]
- Two-sentence field claim: [FILL]
- FACT: [FILL]
- OBSERVATION: [FILL]
- INFERENCE: [FILL]
- HYPOTHESIS: [FILL]
- Problem independent of method: [FILL]
- Causal insight: [FILL]
- Method derivation: [FILL]
- Field contribution and durable fallback: [FILL]
- Prior-art search cutoff and sources: [FILL]
- Closest full-text works: [FILL]
- Load-bearing novelty axis: [FILL]
- New prediction absent from closest work: [FILL]
- Novelty decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Figure 1: [FILL]
- First kill gate: [FILL]
- Resource fit and leverage: [FILL]

## Candidate 3: Benchmark/diagnostic/validity — [FILL]
- Two-sentence field claim: [FILL]
- FACT: [FILL]
- OBSERVATION: [FILL]
- INFERENCE: [FILL]
- HYPOTHESIS: [FILL]
- Problem independent of method: [FILL]
- Causal insight: [FILL]
- Method derivation or justified no-method scope: [FILL]
- Field contribution and durable fallback: [FILL]
- Prior-art search cutoff and sources: [FILL]
- Closest full-text works: [FILL]
- Load-bearing novelty axis: [FILL]
- New prediction absent from closest work: [FILL]
- Novelty decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Figure 1: [FILL]
- First kill gate: [FILL]
- Resource fit and leverage: [FILL]
""",
    "08-collision-and-field-audit.md": """# Novelty and Field-value Audit

## Candidates frozen before search
[FILL: problem, causal claim, mechanism principle, evaluation contract, intended contributions, and new prediction for each candidate]

## Search cutoff and sources
- Searched at (UTC): [FILL: YYYY-MM-DD]
- Sources and coverage caveats: [FILL]

## arXiv categories and recent-venue surfaces
[FILL: relevant categories, latest-90-day and latest-24-month sweeps, full-history search, proceedings/OpenReview where relevant]

## Exact query ledger

| Candidate | Source/category | Exact query | Date filter | Results inspected | Full texts inspected | Caveat |
|---|---|---|---|---:|---:|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Closest-work matrix

| Candidate | Work and URL | Problem/setting | Causal insight | Mechanism principle | Evaluation unit | Shared structure | Load-bearing difference | Candidate-only prediction | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |

## Novelty decisions

### Candidate 1
- Decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Load-bearing novelty axis: [FILL]
- Claim boundary and rerun trigger: [FILL]

### Candidate 2
- Decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Load-bearing novelty axis: [FILL]
- Claim boundary and rerun trigger: [FILL]

### Candidate 3
- Decision: [FILL: PASS | REFRAME | KILL | INCOMPLETE]
- Load-bearing novelty axis: [FILL]
- Claim boundary and rerun trigger: [FILL]

## Naturalness deletion tests
[FILL]

## Durability and field consequence
[FILL]

## Conclusion-to-cost leverage
[FILL]

## Remaining novelty uncertainty and concurrent-work caveat
[FILL]
""",
    "09-pilot-gates.md": """# Frozen Pilot Gates

## Candidate 1
- Load-bearing hypothesis: [FILL]
- Independent unit and sample: [FILL]
- Matched baseline and budget: [FILL]
- Primary endpoint: [FILL]
- PASS/STOP threshold: [FILL]
- Negative controls: [FILL]
- Failure action: [FILL]
- Claims forbidden after PASS: [FILL]

## Candidate 2
[FILL]

## Candidate 3
[FILL]
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the standard artifacts for a research idea discovery run."
    )
    parser.add_argument("--out", required=True, type=Path, help="Absolute run directory")
    parser.add_argument("--topic", required=True, help="Research topic recorded in the manifest")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out = args.out.expanduser()
    if not out.is_absolute():
        raise SystemExit("--out must be an absolute path")
    if out.exists() and any(out.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty directory: {out}")

    out.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": 1,
        "topic": args.topic,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "artifacts": list(ARTIFACTS),
    }
    (out / "run-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for name, body in ARTIFACTS.items():
        (out / name).write_text(body, encoding="utf-8")

    print(f"created discovery run: {out}")
    for name in ["run-manifest.json", *ARTIFACTS]:
        print(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
