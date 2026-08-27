#!/usr/bin/env python3
"""Regression tests for discovery-run scaffolding and validation."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INIT_SCRIPT = SCRIPT_DIR / "init_discovery_run.py"
VALIDATE_SCRIPT = SCRIPT_DIR / "validate_discovery_run.py"


def create_run(run_dir: Path) -> None:
    subprocess.run(
        [
            sys.executable,
            str(INIT_SCRIPT),
            "--out",
            str(run_dir),
            "--topic",
            "test topic",
        ],
        check=True,
        capture_output=True,
        text=True,
    )


class DiscoveryRunTest(unittest.TestCase):
    def test_init_contains_current_prior_art_audit_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir) / "run"
            create_run(run_dir)

            audit = (run_dir / "08-collision-and-field-audit.md").read_text(
                encoding="utf-8"
            )
            for heading in (
                "## Search cutoff and sources",
                "## arXiv categories and recent-venue surfaces",
                "## Exact query ledger",
                "## Closest-work matrix",
                "## Novelty decision",
            ):
                self.assertIn(heading, audit)

    def test_complete_validation_rejects_missing_novelty_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir) / "run"
            create_run(run_dir)

            for path in run_dir.glob("*.md"):
                text = path.read_text(encoding="utf-8")
                text = re.sub(r"\[FILL[^]]*\]", "completed", text)
                path.write_text(text, encoding="utf-8")

            corpus = run_dir / "01-corpus.md"
            corpus.write_text(
                corpus.read_text(encoding="utf-8")
                + "\nhttps://example.com/source\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(VALIDATE_SCRIPT), str(run_dir)],
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("novelty decision", result.stdout.lower())
            self.assertIn("arxiv full-text", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
