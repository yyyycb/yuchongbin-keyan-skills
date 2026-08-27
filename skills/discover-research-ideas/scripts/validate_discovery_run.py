#!/usr/bin/env python3
"""Validate structure and completion signals for a discovery run."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED = {
    "00-intake.md": ["# Discovery Brief", "## Resources", "## Quality thresholds"],
    "01-corpus.md": ["# Verified Quality Corpus", "## Retrieval provenance", "## Corpus"],
    "02-genealogy-cards.md": ["# Idea Genealogy Cards", "### Intellectual move", "### Later inheritance"],
    "03-taste-ledger.md": ["# Research Taste Ledger", "Updated scoped judgment"],
    "04-defect-cards.md": ["# Defect Cards", "Evidence level D0-D4", "Alternative explanations"],
    "05-causal-diagnoses.md": ["# Causal Diagnoses", "Discriminating intervention", "Structural explanation"],
    "06-transfer-matrix.md": ["# Requirement Derivation and Structural Transfer", "New prediction"],
    "07-candidate-portfolio.md": ["# Paper-shaped Candidate Portfolio", "FACT", "HYPOTHESIS"],
    "08-collision-and-field-audit.md": [
        "# Novelty and Field-value Audit",
        "## Search cutoff and sources",
        "## arXiv categories and recent-venue surfaces",
        "## Exact query ledger",
        "## Closest-work matrix",
        "## Novelty decisions",
        "## Naturalness deletion tests",
    ],
    "09-pilot-gates.md": ["# Frozen Pilot Gates", "PASS/STOP threshold", "Claims forbidden after PASS"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a research idea discovery run.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument(
        "--structure-only",
        action="store_true",
        help="Check the scaffold and headings while allowing [FILL] placeholders.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results.")
    return parser.parse_args()


def validate(run_dir: Path, structure_only: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    manifest_path = run_dir / "run-manifest.json"
    if not manifest_path.is_file():
        errors.append("missing run-manifest.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("schema_version") != 1:
                errors.append("run-manifest.json has unsupported schema_version")
            if not str(manifest.get("topic", "")).strip():
                errors.append("run-manifest.json has no topic")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid run-manifest.json: {exc}")

    contents: dict[str, str] = {}
    for name, required_fragments in REQUIRED.items():
        path = run_dir / name
        if not path.is_file():
            errors.append(f"missing {name}")
            continue
        text = path.read_text(encoding="utf-8")
        contents[name] = text
        for fragment in required_fragments:
            if fragment not in text:
                errors.append(f"{name}: missing required section/field: {fragment}")
        if not structure_only and "[FILL" in text:
            errors.append(f"{name}: contains unresolved [FILL] placeholders")

    portfolio = contents.get("07-candidate-portfolio.md", "")
    candidate_count = len(re.findall(r"^## Candidate\s+\d+", portfolio, flags=re.MULTILINE))
    if candidate_count < 3:
        warnings.append(
            f"07-candidate-portfolio.md contains {candidate_count} candidates; default contract expects 3"
        )

    corpus = contents.get("01-corpus.md", "")
    source_markers = len(re.findall(r"https?://", corpus))
    if not structure_only and source_markers == 0:
        errors.append("01-corpus.md: no source URLs found")

    defects = contents.get("04-defect-cards.md", "")
    if not structure_only and not re.search(r"\bD[2-4]\b", defects):
        warnings.append("04-defect-cards.md: no D2-D4 verified defect marker found")

    novelty_audit = contents.get("08-collision-and-field-audit.md", "")
    if not structure_only:
        decisions = re.findall(
            r"(?im)^-\s*Decision:\s*(PASS|REFRAME|KILL|INCOMPLETE)\s*$",
            novelty_audit,
        )
        if len(decisions) < 3:
            errors.append(
                "08-collision-and-field-audit.md: novelty decision missing for one or more candidates"
            )

        if not re.search(r"\b20\d{2}-\d{2}-\d{2}\b", novelty_audit):
            errors.append(
                "08-collision-and-field-audit.md: no dated search cutoff found"
            )

        arxiv_full_text_urls = re.findall(
            r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/[^\s)>|]+",
            novelty_audit,
            flags=re.IGNORECASE,
        )
        if len(set(arxiv_full_text_urls)) < 3:
            errors.append(
                "08-collision-and-field-audit.md: fewer than 3 arXiv full-text URLs found"
            )

    return errors, warnings


def main() -> int:
    args = parse_args()
    run_dir = args.run_dir.expanduser()
    if not run_dir.is_absolute():
        raise SystemExit("run_dir must be an absolute path")
    if not run_dir.is_dir():
        raise SystemExit(f"not a directory: {run_dir}")

    errors, warnings = validate(run_dir, args.structure_only)
    result = {
        "run_dir": str(run_dir),
        "mode": "structure-only" if args.structure_only else "complete",
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"validation: {'PASS' if result['ok'] else 'FAIL'}")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARN: {item}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
