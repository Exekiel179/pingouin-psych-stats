#!/usr/bin/env python3
"""Write a report for downloaded real-paper task sources."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "real_paper_analysis_tasks"
SOURCES = DATASET / "sources"

DATA_EXT = {".csv", ".tsv", ".xlsx", ".xls", ".sav", ".dta", ".rds", ".rda", ".json", ".parquet", ".txt"}
SCRIPT_EXT = {".r", ".rmd", ".qmd", ".py", ".ipynb", ".sps", ".do", ".sas", ".m"}


def load_tasks() -> dict[str, dict]:
    return {
        json.loads(line)["id"]: json.loads(line)
        for line in (DATASET / "tasks.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def file_kind(path: str) -> str:
    ext = Path(path.lower()).suffix
    if ext in DATA_EXT:
        return "data"
    if ext in SCRIPT_EXT:
        return "script"
    if ext in {".md", ".html", ".pdf"}:
        return "doc"
    return "other"


def main() -> None:
    tasks = load_tasks()
    rows = []
    for task_id, task in tasks.items():
        manifest_path = SOURCES / task_id / "manifest.json"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        else:
            manifest = {"downloaded": [], "skipped": [], "errors": [{"reason": "not_processed"}]}
        downloaded = manifest.get("downloaded", [])
        kinds = {}
        for item in downloaded:
            kind = file_kind(item.get("path") or item.get("name", ""))
            kinds[kind] = kinds.get(kind, 0) + 1
        rows.append({
            "task_id": task_id,
            "paper_title": task["paper_title"],
            "platform": task["repository_platform"],
            "task_status": task["task_status"],
            "downloaded": len(downloaded),
            "data_files": kinds.get("data", 0),
            "script_files": kinds.get("script", 0),
            "doc_files": kinds.get("doc", 0),
            "errors": len(manifest.get("errors", [])),
            "error_reasons": "; ".join(e.get("reason", "") for e in manifest.get("errors", [])),
        })

    complete = [r for r in rows if r["data_files"] > 0 and r["script_files"] > 0]
    data_only = [r for r in rows if r["data_files"] > 0 and r["script_files"] == 0]
    script_only = [r for r in rows if r["script_files"] > 0 and r["data_files"] == 0]
    none = [r for r in rows if r["downloaded"] == 0]

    lines = [
        "# Source Download Report",
        "",
        f"Total tasks: {len(rows)}",
        f"Downloaded at least one file: {sum(1 for r in rows if r['downloaded'] > 0)}",
        f"Have data and script files: {len(complete)}",
        f"Have data only: {len(data_only)}",
        f"Have script only: {len(script_only)}",
        f"No downloaded files: {len(none)}",
        "",
        "## Task Status",
        "",
        "| ID | Downloaded | Data | Script | Docs | Platform | Status | Errors | Paper |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
    ]
    for r in rows:
        lines.append(
            f"| `{r['task_id']}` | {r['downloaded']} | {r['data_files']} | {r['script_files']} | {r['doc_files']} | {r['platform']} | `{r['task_status']}` | {r['error_reasons']} | {r['paper_title']} |"
        )

    lines.extend([
        "",
        "## Next Actions",
        "",
        "- Promote tasks with both data and scripts to strict benchmark candidates.",
        "- For data-only or script-only tasks, inspect skipped files and repository pages.",
        "- For ScienceDB/PsyDB tasks, replace the generic community URL with exact dataset detail URLs before retrying downloads.",
        "- For Zenodo and Mannheim, implement platform-specific file API downloaders if those tasks are retained.",
        "",
    ])

    (SOURCES / "SOURCE_DOWNLOAD_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        "tasks": len(rows),
        "downloaded_any": sum(1 for r in rows if r["downloaded"] > 0),
        "data_and_script": len(complete),
        "report": str(SOURCES / "SOURCE_DOWNLOAD_REPORT.md"),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
