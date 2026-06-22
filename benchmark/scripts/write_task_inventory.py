#!/usr/bin/env python3
"""Write a readable inventory of benchmark tasks."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    tasks = [json.loads(line) for line in (ROOT / "tasks" / "tasks.jsonl").read_text(encoding="utf-8").splitlines()]
    lines = ["# Benchmark Task Inventory", ""]
    lines.append(f"Total tasks: {len(tasks)}")
    lines.append("")
    lines.append("## Counts")
    for source, count in Counter(task["source"] for task in tasks).items():
        lines.append(f"- {source}: {count}")
    tag_counts = Counter(tag for task in tasks for tag in task.get("tags", []))
    for tag, count in tag_counts.most_common():
        lines.append(f"- {tag}: {count}")
    lines.append("")
    lines.append("## Tasks")
    lines.append("")
    lines.append("| ID | Source | Tags | Dataset | Prompt |")
    lines.append("| --- | --- | --- | --- | --- |")
    for task in tasks:
        prompt = " ".join(task["problem"].split())
        if len(prompt) > 180:
            prompt = prompt[:177] + "..."
        lines.append(
            f"| `{task['id']}` | {task['source']} | {', '.join(task.get('tags', []))} | `{task['dataset']}` | {prompt} |"
        )
    (ROOT / "TASK_INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(ROOT / "TASK_INVENTORY.md")


if __name__ == "__main__":
    main()

