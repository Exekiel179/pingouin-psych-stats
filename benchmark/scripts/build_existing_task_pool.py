#!/usr/bin/env python3
"""Build a small benchmark task pool mostly from existing public benchmarks."""

from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[0]
SOURCES = REPO_ROOT.parent / "_sources"
STATLLM = SOURCES / "StatLLM" / "Statistical_Analysis_Tasks"
DA_AGENT = SOURCES / "InfiAgent" / "examples" / "DA-Agent" / "data"


PINGOUIN_KEYWORDS = {
    "correlation": ["correlation", "pearson", "spearman", "kendall"],
    "mean_tests": ["t-test", "ttest", "paired", "two-sample", "one-sample", "mean difference"],
    "anova": ["anova", "analysis of variance", "factorial", "repeated measures"],
    "regression": ["regression", "linear model", "logistic"],
    "chi_square": ["chi-square", "chisq", "contingency"],
    "screening": ["normal", "shapiro", "kolmogorov", "outlier", "missing"],
    "descriptive": ["mean", "median", "standard deviation", "summary"],
}


SELECTED_STATLLM_IDS = [
    3, 4, 5, 7, 13, 17, 21, 22, 25, 27, 36, 40,
    61, 62, 65, 75, 76, 86, 88, 89, 92, 93, 98,
    101, 105, 115, 117, 119, 120, 123, 155, 157,
    158, 177, 179, 183, 189,
]

SELECTED_DA_IDS = [5, 10, 11, 25, 26, 34, 57, 109, 730, 734, 738, 739]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


def read_csv_dicts(path: Path) -> list[dict[str, str]]:
    for encoding in ("utf-8-sig", "gbk", "latin1"):
        try:
            with path.open(encoding=encoding, newline="") as f:
                return list(csv.DictReader(f))
        except UnicodeDecodeError:
            continue
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def classify(text: str) -> list[str]:
    lowered = text.lower()
    tags = []
    for tag, keywords in PINGOUIN_KEYWORDS.items():
        if any(keyword in lowered for keyword in keywords):
            tags.append(tag)
    return tags or ["other"]


def statllm_records() -> list[dict]:
    summary_path = STATLLM / "Summary.csv"
    rows = read_csv_dicts(summary_path)
    selected = []
    for row in rows:
        task_id = int(row["ID"])
        if task_id not in SELECTED_STATLLM_IDS:
            continue
        pd_id = row["ProblemDescription"]
        dd_id = row["DataDescription"]
        ds_id = row["TaskDatasets"]
        dataset_name = row["DatasetName"]
        problem = read_text(STATLLM / "ProblemDescription" / f"{pd_id}.txt")
        data_description = read_text(STATLLM / "DataDescription" / f"{dd_id}.txt")
        source_dataset = STATLLM / "TaskDatasets" / ds_id / dataset_name
        if not source_dataset.exists():
            continue
        target_dataset = ROOT / "tasks" / "data" / "statllm" / ds_id / dataset_name
        target_dataset.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_dataset, target_dataset)
        selected.append({
            "id": f"statllm_{task_id:04d}",
            "source": "StatLLM",
            "source_task_id": task_id,
            "dataset": str(target_dataset.relative_to(ROOT)).replace("\\", "/"),
            "problem": problem,
            "data_description": data_description,
            "tags": classify(problem + "\n" + data_description),
            "expected_output": "Python code using pandas/scipy/pingouin where appropriate, plus concise answer.",
            "scoring": {
                "type": "rubric",
                "checks": [
                    "chooses an appropriate statistical method",
                    "uses the provided dataset and variable definitions",
                    "runs or provides executable Python code",
                    "reports statistic/p-value/effect size when applicable",
                    "states assumptions or limitations",
                ],
            },
        })
    return selected


def da_records() -> list[dict]:
    questions = {}
    labels = {}
    q_path = DA_AGENT / "da-dev-questions.jsonl"
    l_path = DA_AGENT / "da-dev-labels.jsonl"
    if not q_path.exists() or not l_path.exists():
        return []
    for line in q_path.read_text(encoding="utf-8", errors="replace").splitlines():
        row = json.loads(line)
        if row["id"] in SELECTED_DA_IDS:
            questions[row["id"]] = row
    for line in l_path.read_text(encoding="utf-8", errors="replace").splitlines():
        row = json.loads(line)
        if row["id"] in SELECTED_DA_IDS:
            labels[row["id"]] = row
    selected = []
    for task_id, row in sorted(questions.items()):
        source_dataset = DA_AGENT / "da-dev-tables" / row["file_name"]
        if not source_dataset.exists():
            continue
        target_dataset = ROOT / "tasks" / "data" / "da_agent" / row["file_name"]
        target_dataset.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_dataset, target_dataset)
        selected.append({
            "id": f"da_{task_id:04d}",
            "source": "InfiAgent DA-Agent/DAEval",
            "source_task_id": task_id,
            "dataset": str(target_dataset.relative_to(ROOT)).replace("\\", "/"),
            "problem": row["question"],
            "data_description": f"CSV file: {row['file_name']}. Concepts: {', '.join(row.get('concepts', []))}. Constraints: {row.get('constraints', '')}",
            "tags": classify(row["question"] + "\n" + " ".join(row.get("concepts", []))),
            "expected_output": row.get("format", ""),
            "gold": labels.get(task_id, {}).get("common_answers", []),
            "scoring": {
                "type": "closed_form",
                "format": row.get("format", ""),
                "tolerance": 0.02,
            },
        })
    return selected


def write_prompts(tasks: list[dict]) -> None:
    baseline_dir = ROOT / "prompts" / "baseline"
    plugin_dir = ROOT / "prompts" / "plugin_guided"
    baseline_dir.mkdir(parents=True, exist_ok=True)
    plugin_dir.mkdir(parents=True, exist_ok=True)
    for old in list(baseline_dir.glob("*.md")) + list(plugin_dir.glob("*.md")):
        old.unlink()
    for task in tasks:
        common = f"""You are analyzing a statistical/data-analysis task.

Dataset path: {task['dataset']}

Data description:
{task['data_description']}

Task:
{task['problem']}

Return:
1. Brief method choice.
2. Executable Python code.
3. Final answer in the requested format if any.
4. Any assumptions or limitations.
"""
        (baseline_dir / f"{task['id']}.md").write_text(common, encoding="utf-8")
        guided = f"""Use the local Pingouin plugin guidance at:
F:/plugins/pingouin-psych-stats/skills/pingouin-stat/SKILL.md
F:/plugins/pingouin-psych-stats/skills/pg-analysis-approval/SKILL.md
F:/plugins/pingouin-psych-stats/references/workflow-index.md
F:/plugins/pingouin-psych-stats/references/supervision-gates.md
F:/plugins/pingouin-psych-stats/references/pingouin-api-quickref.md

Apply the $pingouin-stat workflow: intake if needed, route, analyze, run approval, and report. Keep the response concise.

{common}
"""
        (plugin_dir / f"{task['id']}.md").write_text(guided, encoding="utf-8")


def main() -> None:
    data_root = ROOT / "tasks" / "data"
    if data_root.exists():
        shutil.rmtree(data_root)
    data_root.mkdir(parents=True, exist_ok=True)
    tasks = statllm_records() + da_records()
    tasks_path = ROOT / "tasks" / "tasks.jsonl"
    with tasks_path.open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")
    write_prompts(tasks)
    print(f"Wrote {len(tasks)} tasks to {tasks_path}")


if __name__ == "__main__":
    main()
