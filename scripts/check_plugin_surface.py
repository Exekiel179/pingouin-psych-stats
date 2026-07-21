#!/usr/bin/env python3
"""Check the plugin's public surface and progressive-disclosure contracts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = {
    "pg-intake.md": "pingouin-stat",
    "pg-analyze.md": "pingouin-stat",
    "pg-method.md": "pingouin-stat-router",
    "pg-screen.md": "pg-data-screening",
    "pg-report.md": "pg-reporting",
    "pg-approve.md": "pg-analysis-approval",
    "pg-archive.md": "archive-contract.md",
}


def main() -> None:
    required_files = [
        ROOT / "MODE_REGISTRY.md",
        ROOT / "references" / "exposure-policy.md",
        ROOT / "references" / "archive-contract.md",
        ROOT / "references" / "workflow-contract.md",
        ROOT / "references" / "pingouin-optimization.md",
        ROOT / "archive" / "README.md",
        ROOT / "scripts" / "init_analysis_run.py",
        ROOT / "scripts" / "workflow_engine.py",
    ]
    required_dirs = [ROOT / "archive" / "analysis-runs", ROOT / "archive" / "templates"]
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.is_file()]
    missing += [str(path.relative_to(ROOT)) for path in required_dirs if not path.is_dir()]
    if missing:
        raise SystemExit(f"missing surface files: {missing}")

    registry = (ROOT / "MODE_REGISTRY.md").read_text(encoding="utf-8")
    policy = (ROOT / "references" / "exposure-policy.md").read_text(encoding="utf-8")
    for token in ("Public Entry Points", "Specialist Skills", "Command Map", "Loading Policy"):
        if token not in registry:
            raise SystemExit(f"MODE_REGISTRY.md missing section: {token}")
    for token in ("Stage", "Intake", "Screen", "Analyze", "Approve", "Report", "Archive"):
        if token not in (ROOT / "references" / "workflow-contract.md").read_text(encoding="utf-8"):
            raise SystemExit(f"workflow-contract.md missing stage: {token}")
    for token in ("Tier 0", "Tier 1", "Tier 2", "Tier 3", "Non-Disclosure Rules"):
        if token not in policy:
            raise SystemExit(f"exposure-policy.md missing section: {token}")

    manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for key in ("name", "version", "description", "skills", "interface"):
        if key not in manifest:
            raise SystemExit(f"Codex manifest missing key: {key}")

    for filename, skill in COMMANDS.items():
        path = ROOT / "commands" / filename
        if not path.is_file():
            raise SystemExit(f"missing command: commands/{filename}")
        body = path.read_text(encoding="utf-8")
        if not body.startswith("---\n") or "description:" not in body or "model:" not in body:
            raise SystemExit(f"command frontmatter incomplete: commands/{filename}")
        if skill not in body:
            raise SystemExit(f"command dispatch missing {skill}: commands/{filename}")

    print(f"PASS plugin_surface ({len(COMMANDS)} commands, manifest {manifest['version']})")


if __name__ == "__main__":
    main()
