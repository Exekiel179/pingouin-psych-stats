#!/usr/bin/env python3
"""Download source files for real-paper analysis tasks.

The downloader is conservative:
- It creates one `sources/<task_id>/` folder per task.
- It prioritizes data, scripts, README/codebook, and document files.
- It skips large files by default and records every decision in manifests.
- It supports OSF through the public API and saves metadata pages for other
  platforms when direct file APIs are unavailable.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "real_paper_analysis_tasks"
TASKS = DATASET / "tasks.jsonl"
SOURCES = DATASET / "sources"

INTERESTING_EXT = {
    ".csv",
    ".tsv",
    ".txt",
    ".xlsx",
    ".xls",
    ".sav",
    ".dta",
    ".rds",
    ".rda",
    ".json",
    ".parquet",
    ".r",
    ".rmd",
    ".qmd",
    ".py",
    ".ipynb",
    ".sps",
    ".do",
    ".sas",
    ".m",
    ".md",
    ".html",
    ".pdf",
}

INTERESTING_NAME = re.compile(
    r"(readme|codebook|analysis|script|syntax|data|dataset|clean|main|result|table|figure|supplement)",
    flags=re.I,
)


def safe_name(value: str) -> str:
    value = value.replace("\\", "/").split("/")[-1] or "file"
    value = re.sub(r"[^A-Za-z0-9._\-\u4e00-\u9fff]+", "_", value)
    return value[:160] or "file"


def task_rows() -> list[dict]:
    return [json.loads(line) for line in TASKS.read_text(encoding="utf-8").splitlines() if line.strip()]


def get_json(url: str, params: dict | None = None, retries: int = 3) -> dict | None:
    for attempt in range(retries):
        try:
            r = requests.get(
                url,
                params=params,
                timeout=30,
                headers={"User-Agent": "pingouin-psych-stats-source-downloader/0.1"},
            )
            if r.status_code == 200:
                return r.json()
            if r.status_code in {429, 500, 502, 503, 504}:
                time.sleep(1.5 * (attempt + 1))
                continue
            return None
        except requests.RequestException:
            time.sleep(1.5 * (attempt + 1))
    return None


def should_download(name: str, size: int | None, max_mb: float) -> tuple[bool, str]:
    ext = Path(name.lower()).suffix
    if size is not None and size > max_mb * 1024 * 1024:
        return False, f"skip_large>{max_mb}MB"
    if ext in INTERESTING_EXT:
        return True, "interesting_ext"
    if INTERESTING_NAME.search(name):
        return True, "interesting_name"
    return False, "not_interesting"


def download_file(url: str, path: Path, max_mb: float) -> tuple[bool, str, int]:
    try:
        with requests.get(url, stream=True, timeout=60, headers={"User-Agent": "pingouin-psych-stats-source-downloader/0.1"}) as r:
            if r.status_code != 200:
                return False, f"http_{r.status_code}", 0
            total = 0
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 256):
                    if not chunk:
                        continue
                    total += len(chunk)
                    if total > max_mb * 1024 * 1024:
                        path.unlink(missing_ok=True)
                        return False, f"aborted_large>{max_mb}MB", total
                    f.write(chunk)
            return True, "downloaded", total
    except requests.RequestException as exc:
        return False, f"request_error:{type(exc).__name__}", 0


def osf_id_from_url(url: str) -> str | None:
    match = re.search(r"osf\.io/([A-Za-z0-9]+)/?", url)
    return match.group(1) if match else None


def list_osf_files(node_id: str, max_files: int) -> list[dict]:
    files: list[dict] = []

    def visit_file_url(file_url: str) -> None:
        page = get_json(file_url, {"page[size]": 100})
        while page and len(files) < max_files:
            for item in page.get("data", []):
                attrs = item.get("attributes", {})
                name = attrs.get("name") or attrs.get("path") or item.get("id", "file")
                kind = attrs.get("kind", "")
                download = item.get("links", {}).get("download")
                size = attrs.get("size")
                if download:
                    files.append({
                        "name": name,
                        "kind": kind,
                        "size": size,
                        "download_url": download,
                        "provider": attrs.get("provider", ""),
                        "path": attrs.get("materialized_path") or attrs.get("path") or "",
                    })
                child_url = (
                    item.get("relationships", {})
                    .get("files", {})
                    .get("links", {})
                    .get("related", {})
                    .get("href")
                )
                if child_url and len(files) < max_files:
                    visit_file_url(child_url)
                if len(files) >= max_files:
                    break
            next_url = page.get("links", {}).get("next")
            page = get_json(next_url) if next_url and len(files) < max_files else None

    providers = get_json(f"https://api.osf.io/v2/nodes/{node_id}/files/")
    if providers:
        for provider in providers.get("data", []):
            file_url = (
                provider.get("relationships", {})
                .get("files", {})
                .get("links", {})
                .get("related", {})
                .get("href")
            )
            if file_url:
                visit_file_url(file_url)
            if len(files) >= max_files:
                break

    children = get_json(f"https://api.osf.io/v2/nodes/{node_id}/children/", {"page[size]": 100})
    if children:
        for child in children.get("data", []):
            cid = child.get("id")
            if not cid or len(files) >= max_files:
                break
            child_providers = get_json(f"https://api.osf.io/v2/nodes/{cid}/files/")
            if not child_providers:
                continue
            for provider in child_providers.get("data", []):
                file_url = (
                    provider.get("relationships", {})
                    .get("files", {})
                    .get("links", {})
                    .get("related", {})
                    .get("href")
                )
                if file_url:
                    visit_file_url(file_url)
                if len(files) >= max_files:
                    break
    return files[:max_files]


def save_web_snapshot(url: str, out_dir: Path) -> dict:
    if not url:
        return {"status": "no_url"}
    snapshot = out_dir / "repository_page.md"
    jina_url = f"https://r.jina.ai/http://r.jina.ai/http://example.com"
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        jina_url = "https://r.jina.ai/" + url
    try:
        r = requests.get(jina_url, timeout=40, headers={"User-Agent": "pingouin-psych-stats-source-downloader/0.1"})
        snapshot.write_text(r.text, encoding="utf-8", errors="replace")
        return {"status": f"snapshot_http_{r.status_code}", "path": str(snapshot.relative_to(DATASET))}
    except requests.RequestException as exc:
        return {"status": f"snapshot_error:{type(exc).__name__}"}


def download_task(task: dict, max_mb: float, max_files: int) -> dict:
    out_dir = SOURCES / task["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "task_id": task["id"],
        "paper_title": task["paper_title"],
        "repository_platform": task["repository_platform"],
        "repository_url": task["repository_url"],
        "verification_status": task["verification_status"],
        "downloaded": [],
        "skipped": [],
        "errors": [],
    }

    repo = task["repository_url"]
    platform = task["repository_platform"].lower()
    if "osf" in platform or "osf.io" in repo:
        node_id = osf_id_from_url(repo)
        if not node_id:
            manifest["errors"].append({"reason": "could_not_parse_osf_id"})
        else:
            files = list_osf_files(node_id, max_files=max_files)
            (out_dir / "osf_file_listing.json").write_text(json.dumps(files, indent=2, ensure_ascii=False), encoding="utf-8")
            if not files:
                manifest["errors"].append({"reason": "osf_api_returned_no_files"})
                manifest["snapshot"] = save_web_snapshot(repo, out_dir)
            for file in files:
                name = file["name"]
                ok, reason = should_download(name, file.get("size"), max_mb)
                if not ok:
                    manifest["skipped"].append({"name": name, "reason": reason, "size": file.get("size")})
                    continue
                rel = safe_name(file.get("path") or name)
                target = out_dir / rel
                if target.exists():
                    manifest["downloaded"].append({"name": name, "path": str(target.relative_to(DATASET)), "status": "already_exists"})
                    continue
                success, status, size = download_file(file["download_url"], target, max_mb=max_mb)
                entry = {"name": name, "path": str(target.relative_to(DATASET)), "status": status, "size": size, "source_url": file["download_url"]}
                if success:
                    manifest["downloaded"].append(entry)
                else:
                    manifest["skipped"].append(entry)
    elif "zenodo" in platform or "zenodo" in repo:
        manifest["snapshot"] = save_web_snapshot(repo, out_dir)
        manifest["errors"].append({"reason": "zenodo_file_api_not_implemented_yet"})
    else:
        manifest["snapshot"] = save_web_snapshot(repo, out_dir)
        manifest["errors"].append({"reason": "platform_requires_manual_or_custom_downloader"})

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--start", type=int, default=1, help="1-based task index")
    parser.add_argument("--task-id", default="")
    parser.add_argument("--max-mb", type=float, default=25.0)
    parser.add_argument("--max-files", type=int, default=150)
    args = parser.parse_args()

    SOURCES.mkdir(parents=True, exist_ok=True)
    rows = task_rows()
    if args.task_id:
        rows = [row for row in rows if row["id"] == args.task_id]
    else:
        rows = rows[args.start - 1 :]
        if args.limit:
            rows = rows[: args.limit]

    summary = []
    for i, task in enumerate(rows, start=args.start):
        print(f"[{i}] {task['id']} {task['repository_platform']} {task['repository_url']}")
        manifest = download_task(task, max_mb=args.max_mb, max_files=args.max_files)
        summary.append({
            "task_id": task["id"],
            "downloaded": len(manifest["downloaded"]),
            "skipped": len(manifest["skipped"]),
            "errors": len(manifest["errors"]),
        })

    summary_path = SOURCES / "download_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"tasks": len(summary), "summary_path": str(summary_path), "downloaded_files": sum(x["downloaded"] for x in summary)}, indent=2))


if __name__ == "__main__":
    main()
