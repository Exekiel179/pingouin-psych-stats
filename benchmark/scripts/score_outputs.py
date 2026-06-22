#!/usr/bin/env python3
"""Score opencode benchmark outputs with lightweight automatic and rubric checks."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_tasks() -> dict[str, dict]:
    tasks = {}
    for line in (ROOT / "tasks" / "tasks.jsonl").read_text(encoding="utf-8").splitlines():
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


def extract_tag(text: str, name: str) -> str | None:
    match = re.search(rf"@{re.escape(name)}\[(.*?)\]", text, flags=re.DOTALL)
    return match.group(1).strip() if match else None


def close_enough(actual: str, expected: str, tolerance: float) -> bool:
    try:
        return abs(float(actual) - float(expected)) <= tolerance
    except ValueError:
        return actual.strip().lower() == expected.strip().lower()


def score_closed_form(text: str, task: dict) -> tuple[float, list[str]]:
    gold = task.get("gold") or []
    if not gold:
        return 0.0, ["missing gold labels"]
    passed = 0
    notes = []
    tolerance = float(task.get("scoring", {}).get("tolerance", 0.02))
    for name, expected in gold:
        actual = extract_tag(text, name)
        if actual is None:
            notes.append(f"missing @{name}[]")
            continue
        if close_enough(actual, expected, tolerance):
            passed += 1
        else:
            notes.append(f"{name}: expected {expected}, got {actual}")
    return passed / len(gold), notes


def score_rubric(text: str) -> tuple[float, list[str]]:
    checks = {
        "method": bool(re.search(r"\b(method|analysis|test|anova|correlation|regression|t-?test|chi)\b", text, re.I)),
        "code": "```python" in text or "import pandas" in text or "import pingouin" in text,
        "data": bool(re.search(r"\.csv|read_csv|dataset|dataframe|df\b", text, re.I)),
        "stats": bool(re.search(r"\bp[- ]?value|CI|confidence|effect|cohen|eta|r\b|F\(|t\(", text, re.I)),
        "caveat": bool(re.search(r"assumption|limitation|missing|caveat|S[0-5]|audit", text, re.I)),
    }
    score = sum(checks.values()) / len(checks)
    notes = [name for name, ok in checks.items() if not ok]
    return score, notes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--condition", choices=["baseline", "plugin_guided", "both"], default="both")
    args = parser.parse_args()

    tasks = load_tasks()
    conditions = ["baseline", "plugin_guided"] if args.condition == "both" else [args.condition]
    rows = []
    for condition in conditions:
        out_dir = ROOT / "outputs" / condition
        for path in sorted(out_dir.glob("*.jsonl")):
            task = tasks.get(path.stem)
            if not task:
                continue
            text = read_output(path)
            if task.get("scoring", {}).get("type") == "closed_form":
                score, notes = score_closed_form(text, task)
            else:
                score, notes = score_rubric(text)
            stderr_path = out_dir / f"{path.stem}.stderr.txt"
            failed = stderr_path.exists() and "error" in stderr_path.read_text(encoding="utf-8", errors="replace").lower()
            rows.append({
                "condition": condition,
                "task": path.stem,
                "source": task["source"],
                "score": round(score, 3),
                "failed": failed,
                "notes": "; ".join(notes[:5]),
            })

    result_path = ROOT / "results" / "scores.csv"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with result_path.open("w", encoding="utf-8", newline="") as f:
        import csv
        writer = csv.DictWriter(f, fieldnames=["condition", "task", "source", "score", "failed", "notes"])
        writer.writeheader()
        writer.writerows(rows)

    summary = {}
    for condition in conditions:
        subset = [row for row in rows if row["condition"] == condition]
        if subset:
            summary[condition] = {
                "n": len(subset),
                "mean_score": round(sum(row["score"] for row in subset) / len(subset), 3),
                "failure_rate": round(sum(bool(row["failed"]) for row in subset) / len(subset), 3),
            }
    (ROOT / "results" / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

