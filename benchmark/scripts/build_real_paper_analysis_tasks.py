#!/usr/bin/env python3
"""Build a 50-item full-chain real-paper psychology analysis task dataset."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "real_paper_candidates" / "real_paper_tasks.jsonl"
OUT = ROOT / "real_paper_analysis_tasks"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "_", value, flags=re.I)
    value = re.sub(r"_+", "_", value).strip("_")
    return value[:80] or "task"


def load_candidates() -> list[dict]:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_real_paper_task_pool.py")],
        cwd=ROOT.parent,
        check=True,
    )
    rows = []
    for line in CANDIDATES.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def get(row: dict, key: str, default: str = "") -> str:
    value = row.get(key, default)
    if value is None:
        return default
    return str(value)


def task_status(row: dict) -> str:
    status = row["verification_status"]
    if status == "verified":
        return "ready_for_source_linked_run"
    if status == "partial":
        return "needs_result_freezing"
    return "needs_file_verification"


def expected_deliverables(row: dict) -> list[str]:
    deliverables = [
        "Research question reconstructed from the paper context.",
        "Article hypotheses or a clear statement that the hypothesis must be extracted from the paper.",
        "Experimental design summary: sample, factors, within/between-subject structure, measures, exclusions.",
        "Variable mapping from repository data/scripts to outcome, predictors, covariates, and participant IDs.",
        "Statistical method choice with assumptions and a note on whether Pingouin is in scope.",
        "Executable Python/Pingouin analysis code or a precise reason why the original method is outside Pingouin scope.",
        "APA-style or Chinese psychology-style result report.",
        "Interpretation tied back to the research question, with caveats and no unsupported causal claims.",
    ]
    if row["verification_status"] != "verified":
        deliverables.insert(
            0,
            "Repository verification note: identify what data/script evidence is present and what remains missing.",
        )
    return deliverables


def known_failure_modes(row: dict) -> list[str]:
    failures = [
        "Analyzing a convenient variable instead of the paper's focal dependent variable.",
        "Ignoring repeated-measures, participant IDs, item IDs, or nested trial structure.",
        "Using an independent-samples test for paired/repeated observations.",
        "Omitting assumption checks, effect sizes, confidence intervals, or multiple-comparison correction.",
        "Reporting numeric results that were not computed from the referenced data/script.",
        "Interpreting a significant p value without linking it to the hypothesis.",
        "Making causal claims from correlational or cross-sectional data.",
    ]
    if row["source_language"] == "Chinese":
        failures.append("Misreading Chinese variable names, paper hypotheses, or psychology reporting conventions.")
    if row["pingouin_route"] == "pingouin-stat-router":
        failures.append("Forcing the task into Pingouin when the original model may require mixed-effects or specialized software.")
    return failures


def scoring_rubric() -> list[dict]:
    return [
        {"criterion": "research_question_and_hypotheses", "points": 15},
        {"criterion": "experimental_design_reconstruction", "points": 20},
        {"criterion": "variable_mapping_and_preprocessing", "points": 15},
        {"criterion": "method_choice_assumptions_and_pingouin_scope", "points": 20},
        {"criterion": "analysis_code_or_reproduction_plan", "points": 10},
        {"criterion": "result_reporting_and_interpretation", "points": 15},
        {"criterion": "limitations_and_no_overclaiming", "points": 5},
    ]


def make_task(row: dict, index: int) -> dict:
    tid = f"rp_{index:03d}_{slug(row['id'])}"
    return {
        "id": tid,
        "source_candidate_id": row["id"],
        "source": "Real-paper psychology full-chain benchmark",
        "source_language": get(row, "source_language", "English"),
        "paper_title": get(row, "paper_title"),
        "authors": get(row, "authors"),
        "year": get(row, "year"),
        "journal": get(row, "journal"),
        "doi": get(row, "doi"),
        "paper_url": get(row, "paper_url"),
        "repository_platform": get(row, "repository_platform"),
        "repository_url": get(row, "repository_url"),
        "data_evidence": get(row, "data_evidence"),
        "script_evidence": get(row, "script_evidence"),
        "verification_status": get(row, "verification_status", "needs_manual_check"),
        "task_status": task_status(row),
        "benchmark_level": "T3_full_chain",
        "research_question": get(row, "research_question", "Extract from the paper before final scoring."),
        "article_hypotheses": get(row, "article_hypotheses", "Extract from the paper before final scoring."),
        "experimental_design": get(row, "experimental_design", "Extract from Methods before final scoring."),
        "analysis_type": get(row, "analysis_type", "reproduce main inferential result"),
        "data_analysis_plan": get(row, "data_analysis_plan", "Use scripts/codebook to identify the target analysis."),
        "result_interpretation_target": get(row, "result_interpretation_target", "Interpret the reproduced result against the paper claim."),
        "variables_needed": get(row, "variables_needed", "Extract from data/codebook/script."),
        "pingouin_route": get(row, "pingouin_route", "pingouin-stat-router"),
        "expected_deliverables": expected_deliverables(row),
        "known_failure_modes": known_failure_modes(row),
        "scoring": {
            "type": "rubric_full_chain",
            "max_points": 100,
            "rubric": scoring_rubric(),
            "critical_failures": [
                "fabricated statistics, variables, sample sizes, citations, or repository contents",
                "wrong design family, especially repeated-measures treated as independent",
                "no attempt to connect analysis result to the article hypothesis",
                "unsupported causal interpretation",
            ],
        },
        "notes": get(row, "notes"),
    }


def md_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def task_markdown(task: dict) -> str:
    return f"""# {task['id']}: {task['paper_title']}

## Source

- Journal: {task['journal']}
- Paper URL/DOI: {task['paper_url'] or task['doi'] or 'not recorded'}
- Repository: {task['repository_url']}
- Repository platform: {task['repository_platform']}
- Source language: {task['source_language']}
- Verification status: `{task['verification_status']}`
- Task status: `{task['task_status']}`

## Research Context

- Research question: {task['research_question']}
- Article hypotheses: {task['article_hypotheses']}
- Experimental design: {task['experimental_design']}
- Analysis type: {task['analysis_type']}
- Variables needed: {task['variables_needed']}
- Planned Pingouin route: `{task['pingouin_route']}`

## Repository Evidence

- Data evidence: {task['data_evidence'] or 'not recorded'}
- Script evidence: {task['script_evidence'] or 'not recorded'}

## Benchmark Task

Starting from the research question, reconstruct the study design, identify the target hypothesis and variables, then produce a defensible analysis plan and result interpretation. Use the repository data/scripts when available. If file-level evidence is incomplete, explicitly state what must be verified before numeric reproduction.

## Expected Deliverables

{md_list(task['expected_deliverables'])}

## Known Failure Modes

{md_list(task['known_failure_modes'])}
"""


def context_markdown(task: dict) -> str:
    return f"""# Context

This is a real-paper psychology benchmark task. The goal is to evaluate whether an agent can move from research question to design reconstruction, analysis routing, reproducible analysis, and interpretation.

Do not invent inaccessible facts. Use the paper URL, repository URL, data evidence, and script evidence as source anchors. If a needed paper section, dataset file, or script is not accessible, mark it as a verification gap instead of hallucinating details.

Paper: {task['paper_title']}
Repository: {task['repository_url']}
Paper URL: {task['paper_url'] or task['doi'] or 'not recorded'}
"""


def gold_rubric_markdown(task: dict) -> str:
    rows = "\n".join(f"- {r['criterion']}: {r['points']} points" for r in task["scoring"]["rubric"])
    critical = md_list(task["scoring"]["critical_failures"])
    return f"""# Gold Rubric

Max score: 100

{rows}

## Critical Failures

{critical}

## Expected Route

- Pingouin route: `{task['pingouin_route']}`
- Analysis type: {task['analysis_type']}
- Benchmark level: `{task['benchmark_level']}`
- Task status: `{task['task_status']}`
"""


def prompt_common(task: dict) -> str:
    deliverables = md_list(task["expected_deliverables"])
    failures = md_list(task["known_failure_modes"])
    return f"""You are completing a real-paper psychology analysis benchmark task.

Paper: {task['paper_title']}
Journal: {task['journal']}
Paper URL/DOI: {task['paper_url'] or task['doi'] or 'not recorded'}
Repository: {task['repository_url']}
Repository platform: {task['repository_platform']}
Source language: {task['source_language']}
Verification status: {task['verification_status']}

Research question:
{task['research_question']}

Article hypotheses:
{task['article_hypotheses']}

Experimental design:
{task['experimental_design']}

Data/script evidence:
- Data: {task['data_evidence'] or 'not recorded'}
- Script: {task['script_evidence'] or 'not recorded'}

Requested task:
Starting from the research question, reconstruct the experimental design, identify the hypothesis and variables, route to the appropriate analysis, provide Python/Pingouin code when in scope, and interpret the result in relation to the paper's claim. If data/scripts are not fully accessible, provide a precise verification gap and a reproducible analysis plan instead of inventing numbers.

Expected deliverables:
{deliverables}

Known failure modes to avoid:
{failures}

Return format:
1. Source verification.
2. Research question and hypotheses.
3. Experimental design and variable map.
4. Analysis route and assumptions.
5. Python/Pingouin code or justified out-of-scope note.
6. Result reporting template or reproduced result if available.
7. Interpretation and limitations.
"""


def prompt_plugin(task: dict) -> str:
    return f"""Use `$pingouin-stat` for this task. Follow its workflow:
1. clarify only if necessary,
2. route to the smallest Pingouin workflow,
3. analyze with Pingouin where in scope,
4. run `$pg-analysis-approval` checks before interpretation,
5. report concisely.

Expected route hint: `{task['pingouin_route']}`.

{prompt_common(task)}
"""


def write_inventory(tasks: list[dict]) -> None:
    lines = [
        "# Real-Paper Analysis Task Dataset",
        "",
        f"Total tasks: {len(tasks)}",
        "",
        "This dataset evaluates full-chain psychology analysis: research question -> hypotheses -> design -> analysis -> interpretation.",
        "",
        "## Counts",
        "",
    ]
    for key in ("task_status", "verification_status", "source_language", "repository_platform"):
        counts: dict[str, int] = {}
        for task in tasks:
            counts[task[key]] = counts.get(task[key], 0) + 1
        lines.append(f"### {key}")
        lines.extend(f"- {name}: {count}" for name, count in sorted(counts.items()))
        lines.append("")

    lines.extend([
        "## Tasks",
        "",
        "| ID | Status | Language | Journal | Paper | Route |",
        "| --- | --- | --- | --- | --- | --- |",
    ])
    for task in tasks:
        lines.append(
            f"| `{task['id']}` | `{task['task_status']}` | {task['source_language']} | {task['journal']} | {task['paper_title']} | `{task['pingouin_route']}` |"
        )
    (OUT / "TASKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme() -> None:
    text = """# Real-Paper Psychology Analysis Tasks

This dataset contains 50 full-chain psychology benchmark tasks built from real paper candidates.

The task is not only "run a statistical test." Each item asks the model to reconstruct:

1. research question
2. article hypotheses
3. experimental design
4. variable mapping and analysis route
5. Pingouin-compatible analysis or justified out-of-scope note
6. result interpretation and limitations

## Files

- `tasks.jsonl`: machine-readable task metadata.
- `TASKS.md`: human-readable inventory.
- `tasks/<task_id>/task.md`: full task specification.
- `tasks/<task_id>/context.md`: benchmark context and anti-hallucination rule.
- `tasks/<task_id>/gold_rubric.md`: scoring rubric.
- `prompts/baseline/*.md`: baseline prompts.
- `prompts/plugin_guided/*.md`: prompts requiring `$pingouin-stat` and `$pg-analysis-approval`.

## Task Status

- `ready_for_source_linked_run`: data/script availability is verified by source table or repository evidence; can be used for source-linked benchmark runs.
- `needs_result_freezing`: data/script evidence exists but the exact target result/table/figure still needs to be frozen before strict numeric scoring.
- `needs_file_verification`: promising paper/data candidate, but file-level data and script evidence must be checked before formal scoring.

## Run

Smoke test two tasks:

```powershell
benchmark\\run_real_paper_benchmark.bat both 2
```

Run plugin-guided only:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\\scripts\\run_real_paper_benchmark.ps1 -Condition plugin_guided -Limit 5
python benchmark\\scripts\\score_real_paper_outputs.py --condition plugin_guided
```

Run all:

```powershell
benchmark\\run_real_paper_benchmark.bat both
```

## Interpretation

The automatic scorer is a lightweight coverage rubric. It checks whether the answer includes source verification, research question/hypotheses, design reconstruction, variable mapping, method/assumption reasoning, code or reproduction plan, and interpretation/limitations.

It is not a substitute for human scoring. For publication-grade evaluation, freeze a target result for each task and create numeric gold labels.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "tasks").mkdir(parents=True)
    (OUT / "prompts" / "baseline").mkdir(parents=True)
    (OUT / "prompts" / "plugin_guided").mkdir(parents=True)
    (OUT / "outputs" / "baseline").mkdir(parents=True)
    (OUT / "outputs" / "plugin_guided").mkdir(parents=True)
    (OUT / "results").mkdir(parents=True)

    tasks = [make_task(row, i) for i, row in enumerate(load_candidates(), start=1)]
    with (OUT / "tasks.jsonl").open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task, ensure_ascii=False) + "\n")

    for task in tasks:
        tdir = OUT / "tasks" / task["id"]
        tdir.mkdir(parents=True)
        (tdir / "task.md").write_text(task_markdown(task), encoding="utf-8")
        (tdir / "context.md").write_text(context_markdown(task), encoding="utf-8")
        (tdir / "gold_rubric.md").write_text(gold_rubric_markdown(task), encoding="utf-8")
        (OUT / "prompts" / "baseline" / f"{task['id']}.md").write_text(prompt_common(task), encoding="utf-8")
        (OUT / "prompts" / "plugin_guided" / f"{task['id']}.md").write_text(prompt_plugin(task), encoding="utf-8")

    write_inventory(tasks)
    write_readme()
    print(json.dumps({
        "count": len(tasks),
        "out": str(OUT),
        "prompt_dirs": [
            str(OUT / "prompts" / "baseline"),
            str(OUT / "prompts" / "plugin_guided"),
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()
