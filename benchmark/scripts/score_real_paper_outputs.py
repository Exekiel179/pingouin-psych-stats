#!/usr/bin/env python3
"""Lightweight rubric scoring for real-paper full-chain benchmark outputs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "real_paper_analysis_tasks"


CHECKS = [
    ("source_verification", 10, [r"source verification", r"repository", r"data evidence", r"script evidence", r"verification gap"]),
    ("research_question_hypotheses", 15, [r"research question", r"hypothes", r"研究问题", r"假设"]),
    ("experimental_design", 20, [r"experimental design", r"within", r"between", r"participant", r"sample", r"实验设计", r"被试", r"组内", r"组间"]),
    ("variable_mapping", 15, [r"variable", r"dependent", r"predictor", r"covariate", r"participant id", r"变量", r"因变量", r"自变量"]),
    ("method_assumptions", 20, [r"anova", r"t-?test", r"correlation", r"regression", r"mediation", r"assumption", r"Pingouin", r"假设检验"]),
    ("code_or_reproduction_plan", 10, [r"```python", r"import pingouin", r"pg\.", r"reproducible analysis plan", r"复现"]),
    ("interpretation_limitations", 10, [r"interpret", r"limitation", r"caveat", r"causal", r"overclaim", r"解释", r"局限"]),
]

CRITICAL_PATTERNS = [
    r"cannot (access|verify).*but.*p\s*[<=>]",
    r"assume.*significant",
    r"proves that",
    r"caused by.*correlation",
]


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


def score_text(text: str) -> tuple[int, list[str], list[str]]:
    score = 0
    missing = []
    lower = text.lower()
    for name, points, patterns in CHECKS:
        if any(re.search(pattern, lower, flags=re.I) for pattern in patterns):
            score += points
        else:
            missing.append(name)
    critical = [pattern for pattern in CRITICAL_PATTERNS if re.search(pattern, lower, flags=re.I)]
    if critical:
        score = min(score, 50)
    return score, missing, critical


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
            score, missing, critical = score_text(text)
            stderr_path = out_dir / f"{path.stem}.stderr.txt"
            failed = stderr_path.exists() and "error" in stderr_path.read_text(encoding="utf-8", errors="replace").lower()
            rows.append({
                "condition": condition,
                "task": path.stem,
                "task_status": task["task_status"],
                "verification_status": task["verification_status"],
                "source_language": task["source_language"],
                "journal": task["journal"],
                "score": score,
                "failed": failed,
                "missing": "; ".join(missing),
                "critical": "; ".join(critical),
            })

    result_path = DATASET / "results" / "scores.csv"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with result_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "condition",
                "task",
                "task_status",
                "verification_status",
                "source_language",
                "journal",
                "score",
                "failed",
                "missing",
                "critical",
            ],
        )
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
