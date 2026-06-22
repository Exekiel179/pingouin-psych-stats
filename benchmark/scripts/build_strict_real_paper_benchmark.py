#!/usr/bin/env python3
"""Promote downloaded real-paper tasks with data+scripts to strict benchmark tasks."""

from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL = ROOT / "real_paper_analysis_tasks"
SOURCES = FULL / "sources"
OUT = ROOT / "strict_real_paper_benchmark"

DATA_EXT = {".csv", ".tsv", ".xlsx", ".xls", ".sav", ".dta", ".rds", ".rda", ".json", ".parquet", ".txt"}
SCRIPT_EXT = {".r", ".rmd", ".qmd", ".py", ".ipynb", ".sps", ".do", ".sas", ".m"}
DOC_EXT = {".md", ".html", ".pdf"}

ANALYSIS_PATTERNS = [
    ("anova", r"\b(aov|anova|ezANOVA|afex|lm\(|Anova|mixed_anova|rm_anova)\b"),
    ("t_test", r"\b(t\.test|ttest|pairwise\.t\.test)\b"),
    ("correlation", r"\b(cor\.test|corr|cor\(|pearson|spearman)\b"),
    ("regression", r"\b(lm\(|glm\(|logit|regression)\b"),
    ("mediation", r"\b(mediation|mediate|indirect)\b"),
    ("reliability", r"\b(alpha|cronbach|icc)\b"),
    ("nonparametric", r"\b(wilcox|kruskal|friedman|mann)\b"),
]


def load_tasks() -> dict[str, dict]:
    return {
        json.loads(line)["id"]: json.loads(line)
        for line in (FULL / "tasks.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def kind(path: str) -> str:
    ext = Path(path.lower()).suffix
    if ext in DATA_EXT:
        return "data"
    if ext in SCRIPT_EXT:
        return "script"
    if ext in DOC_EXT:
        return "doc"
    return "other"


def read_text(path: Path, limit: int = 20000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except Exception:
        return ""


def script_hints(paths: list[Path]) -> dict:
    combined = "\n".join(read_text(p) for p in paths if p.suffix.lower() in SCRIPT_EXT)
    detected = []
    for name, pattern in ANALYSIS_PATTERNS:
        if re.search(pattern, combined, flags=re.I):
            detected.append(name)
    variables = []
    # Useful but intentionally shallow extraction from R/SPSS style formulas.
    for match in re.finditer(r"([A-Za-z_][\w.]*)\s*~\s*([A-Za-z_][\w.:*+\-\s]*)", combined):
        lhs = match.group(1)
        rhs = re.split(r"[:*+\-\s]+", match.group(2))
        variables.extend([lhs, *rhs])
    variables = sorted({v for v in variables if len(v) > 1 and not v.lower().startswith(("data", "df"))})[:30]
    snippets = []
    for line in combined.splitlines():
        if any(re.search(pattern, line, flags=re.I) for _, pattern in ANALYSIS_PATTERNS):
            clean = line.strip()
            if clean and clean not in snippets:
                snippets.append(clean[:240])
        if len(snippets) >= 12:
            break
    return {
        "detected_analysis": detected,
        "candidate_variables": variables,
        "analysis_snippets": snippets,
    }


def data_hints(paths: list[Path]) -> dict:
    hints = {}
    for path in paths[:5]:
        ext = path.suffix.lower()
        if ext in {".csv", ".tsv", ".txt"}:
            delimiter = "\t" if ext == ".tsv" else ","
            try:
                with path.open(encoding="utf-8-sig", errors="replace", newline="") as f:
                    reader = csv.reader(f, delimiter=delimiter)
                    header = next(reader, [])
                    rows = sum(1 for _, _row in zip(range(2000), reader))
                hints[str(path.name)] = {"columns": header[:80], "sample_rows_counted": rows}
            except Exception as exc:
                hints[str(path.name)] = {"error": type(exc).__name__}
        elif ext in {".xlsx", ".xls", ".sav", ".dta", ".rds", ".rda"}:
            hints[str(path.name)] = {"note": f"{ext} file; inspect with pandas/pyreadstat/R as appropriate"}
    return hints


def copy_task_sources(task_id: str, target_dir: Path) -> tuple[list[dict], list[Path], list[Path], list[Path]]:
    manifest = json.loads((SOURCES / task_id / "manifest.json").read_text(encoding="utf-8"))
    copied = []
    data_paths: list[Path] = []
    script_paths: list[Path] = []
    doc_paths: list[Path] = []
    for item in manifest.get("downloaded", []):
        rel = Path(item["path"])
        src = FULL / rel
        if not src.exists():
            continue
        subdir = kind(str(src))
        dst = target_dir / "sources" / subdir / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        entry = {
            "kind": subdir,
            "path": str(dst.relative_to(OUT)).replace("\\", "/"),
            "source_url": item.get("source_url") or item.get("source_url".replace("_", "")) or "",
            "size": dst.stat().st_size,
        }
        copied.append(entry)
        if subdir == "data":
            data_paths.append(dst)
        elif subdir == "script":
            script_paths.append(dst)
        elif subdir == "doc":
            doc_paths.append(dst)
    return copied, data_paths, script_paths, doc_paths


def strict_prompt(task: dict, strict: dict, plugin: bool) -> str:
    prefix = ""
    if plugin:
        prefix = """Use `$pingouin-stat` and `$pg-analysis-approval`.
Route to the smallest applicable Pingouin workflow. If the original script uses a method outside Pingouin scope, state that explicitly and give the closest safe Pingouin subset only if defensible.

"""
    data_files = "\n".join(f"- {f['path']}" for f in strict["files"] if f["kind"] == "data")
    script_files = "\n".join(f"- {f['path']}" for f in strict["files"] if f["kind"] == "script")
    doc_files = "\n".join(f"- {f['path']}" for f in strict["files"] if f["kind"] == "doc") or "- none"
    snippets = "\n".join(f"- `{s}`" for s in strict["script_hints"]["analysis_snippets"]) or "- no statistical snippets detected"
    return f"""{prefix}You are completing a strict real-paper psychology benchmark task.

Paper: {task['paper_title']}
Journal: {task['journal']}
Paper URL/DOI: {task['paper_url'] or task['doi'] or 'not recorded'}
Original repository: {task['repository_url']}

Local data files:
{data_files}

Local script files:
{script_files}

Local document/readme files:
{doc_files}

Detected analysis families from scripts: {', '.join(strict['script_hints']['detected_analysis']) or 'not detected'}
Candidate variables from scripts: {', '.join(strict['script_hints']['candidate_variables']) or 'not extracted'}
Script analysis snippets:
{snippets}

Task:
1. Inspect the local data and script files.
2. Identify one concrete target analysis from the scripts that can be reproduced or safely approximated in Python/Pingouin.
3. State the research question/hypothesis/design as far as supported by the local files and paper metadata.
4. Run or write executable Python code using local file paths.
5. Report the statistic, p value, effect size/CI where possible.
6. Interpret the result against the paper claim with limitations.

Do not invent paper details or numeric results. If a script uses software/features outside Pingouin, mark the limitation and reproduce the closest valid subset only when justified.
"""


def write_task(task: dict, index: int) -> dict | None:
    manifest_path = SOURCES / task["id"] / "manifest.json"
    if not manifest_path.exists():
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    kinds = {kind(item.get("path", "")) for item in manifest.get("downloaded", [])}
    if "data" not in kinds or "script" not in kinds:
        return None

    strict_id = f"strict_{index:03d}_{task['id']}"
    target = OUT / "tasks" / strict_id
    target.mkdir(parents=True, exist_ok=True)
    files, data_paths, script_paths, doc_paths = copy_task_sources(task["id"], target)
    strict = {
        "id": strict_id,
        "source_task_id": task["id"],
        "paper_title": task["paper_title"],
        "journal": task["journal"],
        "paper_url": task["paper_url"],
        "doi": task["doi"],
        "repository_url": task["repository_url"],
        "source_language": task["source_language"],
        "pingouin_route_hint": task["pingouin_route"],
        "files": files,
        "script_hints": script_hints(script_paths),
        "data_hints": data_hints(data_paths),
        "scoring": {
            "type": "strict_real_paper_rubric",
            "max_points": 100,
            "criteria": [
                {"name": "uses_local_data_and_scripts", "points": 15},
                {"name": "identifies_concrete_target_analysis", "points": 15},
                {"name": "correct_design_and_variable_mapping", "points": 15},
                {"name": "appropriate_method_and_assumptions", "points": 20},
                {"name": "executable_python_pingouin_or_valid_scope_note", "points": 15},
                {"name": "numeric_reporting_when_reproducible", "points": 10},
                {"name": "interpretation_and_limitations", "points": 10},
            ],
            "critical_failures": [
                "does not use local files",
                "fabricates numeric results",
                "ignores repeated-measures or nested structure when visible",
                "claims Pingouin supports an unsupported model without caveat",
            ],
        },
    }
    (target / "strict_task.json").write_text(json.dumps(strict, indent=2, ensure_ascii=False), encoding="utf-8")
    (target / "task.md").write_text(strict_prompt(task, strict, plugin=False), encoding="utf-8")
    (target / "gold_checklist.md").write_text(gold_checklist(strict), encoding="utf-8")
    return strict


def gold_checklist(strict: dict) -> str:
    files = "\n".join(f"- `{f['path']}` ({f['kind']}, {f['size']} bytes)" for f in strict["files"])
    snippets = "\n".join(f"- `{s}`" for s in strict["script_hints"]["analysis_snippets"]) or "- none"
    return f"""# Gold Checklist

This is a strict benchmark item because local data and script files are present.

## Required Evidence Use

The answer must use local files under this task directory:

{files}

## Script-Derived Analysis Clues

- Detected analysis families: {', '.join(strict['script_hints']['detected_analysis']) or 'not detected'}
- Candidate variables: {', '.join(strict['script_hints']['candidate_variables']) or 'not extracted'}

Snippets:

{snippets}

## Scoring

- Uses local data and scripts: 15
- Identifies a concrete target analysis from scripts: 15
- Correct design and variable mapping: 15
- Appropriate method and assumptions: 20
- Executable Python/Pingouin or valid out-of-scope note: 15
- Numeric reporting when reproducible: 10
- Interpretation and limitations: 10
"""


def write_outputs(strict_tasks: list[dict], original_tasks: dict[str, dict]) -> None:
    (OUT / "prompts" / "baseline").mkdir(parents=True, exist_ok=True)
    (OUT / "prompts" / "plugin_guided").mkdir(parents=True, exist_ok=True)
    (OUT / "outputs" / "baseline").mkdir(parents=True, exist_ok=True)
    (OUT / "outputs" / "plugin_guided").mkdir(parents=True, exist_ok=True)
    (OUT / "results").mkdir(parents=True, exist_ok=True)

    with (OUT / "tasks.jsonl").open("w", encoding="utf-8") as f:
        for strict in strict_tasks:
            f.write(json.dumps(strict, ensure_ascii=False) + "\n")
            src = original_tasks[strict["source_task_id"]]
            (OUT / "prompts" / "baseline" / f"{strict['id']}.md").write_text(strict_prompt(src, strict, plugin=False), encoding="utf-8")
            (OUT / "prompts" / "plugin_guided" / f"{strict['id']}.md").write_text(strict_prompt(src, strict, plugin=True), encoding="utf-8")

    lines = [
        "# Strict Real-Paper Benchmark",
        "",
        f"Total strict tasks: {len(strict_tasks)}",
        "",
        "These tasks have both local data files and local analysis script files.",
        "",
        "| ID | Source Task | Journal | Data Files | Script Files | Detected Analysis | Paper |",
        "| --- | --- | --- | ---: | ---: | --- | --- |",
    ]
    for strict in strict_tasks:
        data_n = sum(1 for f in strict["files"] if f["kind"] == "data")
        script_n = sum(1 for f in strict["files"] if f["kind"] == "script")
        detected = ", ".join(strict["script_hints"]["detected_analysis"]) or "not detected"
        lines.append(
            f"| `{strict['id']}` | `{strict['source_task_id']}` | {strict['journal']} | {data_n} | {script_n} | {detected} | {strict['paper_title']} |"
        )
    (OUT / "STRICT_TASKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    readme = """# Strict Real-Paper Benchmark

This subset contains tasks that have both downloaded local data files and local analysis scripts.

Run a smoke test:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\\scripts\\run_strict_real_paper_benchmark.ps1 -Condition both -Limit 2
```

Score outputs:

```powershell
python benchmark\\scripts\\score_strict_real_paper_outputs.py --condition both
```

The strict prompts require the model to inspect local files and identify one concrete target analysis from the original scripts. This is stronger than the source-linked candidate benchmark, but numeric gold values still need optional human freezing if publication-grade exact scoring is required.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for sub in ("tasks", "prompts"):
        path = OUT / sub
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)
        path.mkdir(parents=True, exist_ok=True)
    (OUT / "outputs" / "baseline").mkdir(parents=True, exist_ok=True)
    (OUT / "outputs" / "plugin_guided").mkdir(parents=True, exist_ok=True)
    (OUT / "results").mkdir(parents=True, exist_ok=True)

    original_tasks = load_tasks()
    strict_tasks = []
    for task in original_tasks.values():
        strict = write_task(task, len(strict_tasks) + 1)
        if strict:
            strict_tasks.append(strict)
    write_outputs(strict_tasks, original_tasks)
    print(json.dumps({"strict_tasks": len(strict_tasks), "out": str(OUT)}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
