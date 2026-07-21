#!/usr/bin/env python3
"""Stateful workflow engine for Pingouin analysis archive runs."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATES = {
    "initialized": {"intake_complete"},
    "intake_complete": {"screened"},
    "screened": {"analyzed"},
    "analyzed": {"approved", "approved_with_notes", "revise", "blocked"},
    "revise": {"analyzed"},
    "approved": {"reported"},
    "approved_with_notes": {"reported"},
    "reported": {"complete"},
    "blocked": set(),
    "complete": set(),
}
DECISIONS = {"approved": "APPROVED", "approved_with_notes": "APPROVED_WITH_NOTES"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_manifest(run: Path) -> dict:
    path = run / "run-manifest.json"
    if not path.is_file():
        raise SystemExit(f"missing run manifest: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def write_manifest(run: Path, manifest: dict) -> None:
    (run / "run-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def environment_snapshot() -> dict:
    def version(name: str) -> str | None:
        try:
            return importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            return None

    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    plugin_version = None
    if manifest_path.is_file():
        plugin_version = json.loads(manifest_path.read_text(encoding="utf-8")).get("version")
    return {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "pingouin": version("pingouin"),
        "pandas": version("pandas"),
        "numpy": version("numpy"),
        "plugin": plugin_version,
    }


def artifact_status(run: Path, state: str) -> dict[str, list[str]]:
    checks: dict[str, list[str]] = {}

    def files_under(name: str) -> list[str]:
        directory = run / name
        return [str(path.relative_to(run)) for path in directory.rglob("*") if path.is_file()] if directory.is_dir() else []

    if state in {"screened", "analyzed", "approved", "approved_with_notes", "revise", "reported", "complete"}:
        screening = run / "screening.json"
        checks["screening"] = ["screening.json"] if screening.is_file() and screening.stat().st_size > 2 else []
    if state in {"analyzed", "approved", "approved_with_notes", "revise", "reported", "complete"}:
        code = (run / "analysis.py")
        checks["analysis"] = [] if not code.is_file() or "Add the exact" in code.read_text(encoding="utf-8") else ["analysis.py"]
        checks["results"] = files_under("results")
    if state in {"approved", "approved_with_notes", "reported", "complete"}:
        audit = (run / "audit.md").read_text(encoding="utf-8") if (run / "audit.md").is_file() else ""
        checks["approval"] = ["audit.md"] if any(label in audit for label in DECISIONS.values()) else []
    if state in {"reported", "complete"}:
        checks["reports"] = files_under("reports")
    return checks


def missing_artifacts(run: Path, state: str) -> list[str]:
    checks = artifact_status(run, state)
    return [name for name, found in checks.items() if not found]


def transition(run: Path, target: str) -> dict:
    manifest = read_manifest(run)
    current = manifest.get("status", "initialized")
    if target not in STATES.get(current, set()):
        raise SystemExit(f"invalid transition: {current} -> {target}")
    missing = missing_artifacts(run, current)
    if missing:
        raise SystemExit(f"cannot leave {current}; missing artifacts: {', '.join(missing)}")
    manifest["status"] = target
    manifest["updated_at"] = now()
    manifest.setdefault("history", []).append({"from": current, "to": target, "at": manifest["updated_at"]})
    write_manifest(run, manifest)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "check"):
        command = sub.add_parser(name)
        command.add_argument("run", type=Path)
    advance = sub.add_parser("advance")
    advance.add_argument("run", type=Path)
    advance.add_argument("target", choices=sorted(STATES))
    args = parser.parse_args()
    run = args.run.resolve()
    manifest = read_manifest(run)
    if args.command == "status":
        print(json.dumps({"run_id": manifest.get("run_id"), "status": manifest.get("status"), "history": manifest.get("history", [])}, indent=2, ensure_ascii=False))
    elif args.command == "check":
        missing = missing_artifacts(run, manifest.get("status", "initialized"))
        if missing:
            raise SystemExit("missing artifacts: " + ", ".join(missing))
        print("PASS archive_check", run)
    else:
        updated = transition(run, args.target)
        print(json.dumps({"run_id": updated["run_id"], "status": updated["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
