#!/usr/bin/env python3
"""Create a timestamped, privacy-conscious analysis archive run."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from workflow_engine import environment_snapshot


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive" / "analysis-runs"


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return value or "analysis"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Short study slug, e.g. rm-anxiety")
    parser.add_argument("--input", dest="input_ref", default="", help="Input path or dataframe identifier (not copied)")
    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d-%H%M%S")
    run_dir = ARCHIVE / f"{timestamp}-{slugify(args.slug)}"
    if run_dir.exists():
        raise SystemExit(f"run already exists: {run_dir}")

    for name in ("results", "reports", "figures"):
        (run_dir / name).mkdir(parents=True, exist_ok=False)

    manifest = {
        "schema": "pingouin-analysis-run/v1",
        "run_id": run_dir.name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_reference": args.input_ref,
        "raw_data_copied": False,
        "status": "initialized",
        "history": [{"from": None, "to": "initialized", "at": datetime.now(timezone.utc).isoformat()}],
        "environment": environment_snapshot(),
        "plugin_root": str(ROOT),
    }
    (run_dir / "analysis.py").write_text("# Add the exact reproducible Pingouin analysis code here.\n", encoding="utf-8")
    (run_dir / "screening.json").write_text("{}\n", encoding="utf-8")
    (run_dir / "audit.md").write_text("# Audit\n\nDecision: PENDING\n\nAudit: S0 pending; S1 pending; S2 pending; S3 pending; S4 pending; S5 pending.\n", encoding="utf-8")
    (run_dir / "run-manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(run_dir)


if __name__ == "__main__":
    main()
