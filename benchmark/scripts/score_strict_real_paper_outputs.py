#!/usr/bin/env python3
"""Score strict real-paper benchmark outputs with a file-use rubric."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "strict_real_paper_benchmark"


def load_tasks() -> dict[str, dict]:
    tasks = {}
    for line in (DATASET / "tasks.jsonl").read_text(encoding="utf-8").splitlines():
        task = json.loads(line)
        tasks[task["id"]] = task
    return tasks


def read_output(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    chunks = []
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            chunks.append(line)
            continue
        for key in ("message", "text", "content", "output"):
            value = event.get(key)
            if isinstance(value, str):
                chunks.append(value)
        if isinstance(event.get("parts"), list):
            for part in event["parts"]:
                if isinstance(part, dict) and isinstance(part.get("text"), str):
                    chunks.append(part["text"])
    return "\n".join(chunks) or text


def score(text: str, task: dict) -> tuple[int, list[str], list[str]]:
    lower = text.lower()
    points = 0
    missing = []

    local_file_names = [Path(f["path"]).name.lower() for f in task["files"]]
    used_local = any(name in lower for name in local_file_names)
    if used_local:
        points += 15
    else:
        missing.append("uses_local_data_and_scripts")

    snippets = task["script_hints"].get("analysis_snippets", [])
    detected = task["script_hints"].get("detected_analysis", [])
    if any(d in lower for d in detected) or any(s[:40].lower() in lower for s in snippets if len(s) > 40):
        points += 15
    else:
        missing.append("identifies_concrete_target_analysis")

    if re.search(r"variable|dependent|predictor|factor|within|between|participant|subject|变量|因变量|自变量|被试|组内|组间", lower):
        points += 15
    else:
        missing.append("correct_design_and_variable_mapping")

    if re.search(r"assumption|normal|homogeneity|sphericity|multiple|correction|effect size|pingouin|anova|t-?test|correlation|regression|假设|效应量", lower):
        points += 20
    else:
        missing.append("appropriate_method_and_assumptions")

    if "```python" in lower or "import pingouin" in lower or re.search(r"\bpg\.", lower) or "out of scope" in lower or "outside pingouin" in lower:
        points += 15
    else:
        missing.append("executable_python_pingouin_or_valid_scope_note")

    if re.search(r"\bp\s*[<=>]|p-value|ci\b|confidence interval|cohen|eta|r\s*=|t\(|f\(|χ|chi|统计量|置信区间", lower):
        points += 10
    else:
        missing.append("numeric_reporting_when_reproducible")

    if re.search(r"interpret|limitation|caveat|claim|causal|overclaim|解释|局限|不能.*因果", lower):
        points += 10
    else:
        missing.append("interpretation_and_limitations")

    critical = []
    critical_patterns = {
        "fabricated_numeric_without_file_use": r"(p\s*[<=>]\s*0\.\d+|t\(|f\(|r\s*=).{0,200}$",
        "unsupported_causality": r"proves that|caused by.*correlation|证明.*因果",
    }
    for name, pattern in critical_patterns.items():
        if re.search(pattern, lower, flags=re.S) and not used_local:
            critical.append(name)
    if critical:
        points = min(points, 50)
    return points, missing, critical


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--condition", choices=["baseline", "plugin_guided", "both"], default="both")
    args = parser.parse_args()

    tasks = load_tasks()
    conditions = ["baseline", "plugin_guided"] if args.condition == "both" else [args.condition]
    rows = []
    for condition in conditions:
        out_dir = DATASET / "outputs" / condition
        for path in sorted(out_dir.glob("*.jsonl")):
            task = tasks.get(path.stem)
            if not task:
                continue
            text = read_output(path)
            points, missing, critical = score(text, task)
            stderr_path = out_dir / f"{path.stem}.stderr.txt"
            failed = stderr_path.exists() and "error" in stderr_path.read_text(encoding="utf-8", errors="replace").lower()
            rows.append({
                "condition": condition,
                "task": path.stem,
                "source_task_id": task["source_task_id"],
                "journal": task["journal"],
                "score": points,
                "failed": failed,
                "missing": "; ".join(missing),
                "critical": "; ".join(critical),
            })

    result_path = DATASET / "results" / "scores.csv"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with result_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["condition", "task", "source_task_id", "journal", "score", "failed", "missing", "critical"])
        writer.writeheader()
        writer.writerows(rows)

    summary = {}
    for condition in conditions:
        subset = [row for row in rows if row["condition"] == condition]
        if subset:
            summary[condition] = {
                "n": len(subset),
                "mean_score": round(sum(row["score"] for row in subset) / len(subset), 2),
                "failure_rate": round(sum(bool(row["failed"]) for row in subset) / len(subset), 3),
            }
    (DATASET / "results" / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
