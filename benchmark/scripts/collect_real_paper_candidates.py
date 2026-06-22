#!/usr/bin/env python3
"""Collect real-paper psychology benchmark candidates from open repositories.

The script is intentionally conservative: it records evidence and verification
signals instead of pretending that every discovered item is fully validated.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import requests


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "real_paper_candidates"

TOP_JOURNALS = [
    "Nature Human Behaviour",
    "Psychological Science",
    "Journal of Experimental Psychology: General",
    "Journal of Personality and Social Psychology",
    "Cognition",
    "Clinical Psychological Science",
    "Developmental Science",
    "Perspectives on Psychological Science",
    "PNAS",
    "Proceedings of the National Academy of Sciences",
    "Nature Communications",
    "Behavior Research Methods",
    "Psychological Methods",
]

DATA_EXT = {
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
    ".sav",
    ".dta",
    ".rds",
    ".rda",
    ".json",
    ".parquet",
    ".txt",
}

SCRIPT_EXT = {
    ".r",
    ".rmd",
    ".qmd",
    ".py",
    ".ipynb",
    ".sps",
    ".do",
    ".sas",
    ".m",
}


@dataclass
class Candidate:
    id: str
    paper_title: str
    authors: str
    year: str
    journal: str
    journal_tier_reason: str
    doi: str
    paper_url: str
    repository_platform: str
    repository_url: str
    data_evidence: str
    script_evidence: str
    analysis_type: str
    candidate_task: str
    variables_needed: str
    pingouin_route: str
    verification_status: str
    notes: str


def get_json(url: str, params: dict | None = None, retries: int = 2) -> dict | None:
    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=15,
                headers={"User-Agent": "pingouin-psych-stats-benchmark/0.1"},
            )
            if response.status_code == 200:
                return response.json()
            if response.status_code in {429, 500, 502, 503, 504}:
                time.sleep(1.5 * (attempt + 1))
                continue
            return None
        except requests.RequestException:
            time.sleep(1.5 * (attempt + 1))
    return None


def norm_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(norm_text(v) for v in value)
    return re.sub(r"\s+", " ", str(value)).strip()


def file_ext(name: str) -> str:
    return Path(name.lower()).suffix


def infer_analysis(text: str, files: Iterable[str]) -> tuple[str, str]:
    hay = (text + " " + " ".join(files)).lower()
    rules = [
        ("mixed", "mixed anova", "pg-anova"),
        ("repeated", "repeated-measures ANOVA", "pg-anova"),
        ("anova", "ANOVA", "pg-anova"),
        ("t-test", "mean comparison", "pg-mean-tests"),
        ("ttest", "mean comparison", "pg-mean-tests"),
        ("correlation", "correlation", "pg-correlations"),
        ("regression", "linear/logistic regression", "pg-regression-mediation"),
        ("mediation", "mediation", "pg-regression-mediation"),
        ("cronbach", "reliability", "pg-reliability"),
        ("icc", "inter-rater reliability", "pg-reliability"),
    ]
    for needle, analysis, route in rules:
        if needle in hay:
            return analysis, route
    return "needs manual mapping", "pingouin-stat-router"


def osf_node_file_names(node_id: str, max_children: int = 5, max_files: int = 80) -> list[str]:
    names: list[str] = []

    def add_files_for_node(nid: str) -> None:
        providers = get_json(f"https://api.osf.io/v2/nodes/{nid}/files/")
        if not providers:
            return
        for provider in providers.get("data", []):
            if len(names) >= max_files:
                break
            file_url = (
                provider.get("relationships", {})
                .get("files", {})
                .get("links", {})
                .get("related", {})
                .get("href")
            )
            if not file_url:
                continue
            page = get_json(file_url, {"page[size]": 100})
            while page:
                for item in page.get("data", []):
                    if len(names) >= max_files:
                        break
                    attrs = item.get("attributes", {})
                    name = attrs.get("name") or attrs.get("path") or ""
                    kind = attrs.get("kind") or item.get("type") or ""
                    if name:
                        names.append(name)
                    # OSF folder children are represented by a files relationship.
                    child_url = (
                        item.get("relationships", {})
                        .get("files", {})
                        .get("links", {})
                        .get("related", {})
                        .get("href")
                    )
                    if child_url and ("folder" in kind.lower() or attrs.get("kind") == "folder"):
                        child_page = get_json(child_url, {"page[size]": 100})
                        if child_page:
                            for child in child_page.get("data", []):
                                cname = child.get("attributes", {}).get("name") or ""
                                if cname:
                                    names.append(cname)
                                if len(names) >= max_files:
                                    break
                if len(names) >= max_files:
                    break
                next_url = page.get("links", {}).get("next")
                page = get_json(next_url) if next_url and len(names) < max_files else None

    add_files_for_node(node_id)
    children = get_json(f"https://api.osf.io/v2/nodes/{node_id}/children/", {"page[size]": max_children})
    if children:
        for child in children.get("data", [])[:max_children]:
            if len(names) >= max_files:
                break
            cid = child.get("id")
            if cid:
                add_files_for_node(cid)
    return sorted(set(names), key=str.lower)


def osf_search(query: str, page_size: int = 10, pages: int = 1) -> list[dict]:
    out: list[dict] = []
    url = "https://api.osf.io/v2/search/"
    params = {"q": query, "page[size]": page_size}
    for _ in range(pages):
        payload = get_json(url, params)
        if not payload:
            break
        for item in payload.get("data", []):
            if item:
                out.append(item)
        next_url = payload.get("links", {}).get("next")
        if not next_url:
            break
        url = next_url
        params = None
    return out


def osf_item_to_candidate(item: dict, query: str, verify_files: bool = True) -> Candidate | None:
    item_type = item.get("type", "")
    if item_type not in {"nodes", "registrations"}:
        return None
    item_id = item.get("id", "")
    attrs = item.get("attributes", {})
    title = norm_text(attrs.get("title"))
    desc = norm_text(attrs.get("description"))
    text = f"{title} {desc}"
    journal = next((j for j in TOP_JOURNALS if j.lower() in text.lower()), "")
    if not journal:
        journal = next((j for j in TOP_JOURNALS if j.lower() in query.lower()), "")
    if not item_id or not title or not journal:
        return None

    if item_type == "registrations":
        node_url = f"https://api.osf.io/v2/registrations/{item_id}/"
        repo_url = f"https://osf.io/{item_id}/"
        # File traversal for registrations is not as consistent; keep metadata.
        files: list[str] = []
    else:
        node_url = f"https://api.osf.io/v2/nodes/{item_id}/"
        repo_url = f"https://osf.io/{item_id}/"
        files = osf_node_file_names(item_id) if verify_files else []

    data_files = [f for f in files if file_ext(f) in DATA_EXT or "data" in f.lower()]
    script_files = [
        f
        for f in files
        if file_ext(f) in SCRIPT_EXT
        or "script" in f.lower()
        or "analysis" in f.lower()
        or "code" in f.lower()
    ]
    has_data = bool(data_files)
    has_script = bool(script_files)
    if not (has_data or has_script or any(k in text.lower() for k in ["data", "code", "script", "analysis"])):
        return None

    analysis_type, route = infer_analysis(text, files)
    status = "verified" if has_data and has_script else "partial"
    notes = f"Discovered by OSF query: {query}. API: {node_url}"
    if item_type == "registrations":
        status = "needs_manual_check"
        notes += " Registration item; file evidence not traversed by this script."

    return Candidate(
        id=f"osf_{item_id}",
        paper_title=title,
        authors="",
        year="",
        journal=journal,
        journal_tier_reason="Target high-impact psychology/behavioral science journal list.",
        doi="",
        paper_url="",
        repository_platform="OSF",
        repository_url=repo_url,
        data_evidence="; ".join(data_files[:8]),
        script_evidence="; ".join(script_files[:8]),
        analysis_type=analysis_type,
        candidate_task=f"Use the open dataset and scripts to reproduce one core {analysis_type} result from the paper.",
        variables_needed="Read codebook/script; select dependent variable, predictors/factors, and subject ID as applicable.",
        pingouin_route=route,
        verification_status=status,
        notes=notes,
    )


def seed_candidates() -> list[Candidate]:
    """Hand-seeded candidates already encountered during development."""
    seeds = [
        Candidate(
            id="osf_wjr7u",
            paper_title="Object-based encoding constrains storage in visual working memory",
            authors="",
            year="",
            journal="Journal of Experimental Psychology: General",
            journal_tier_reason="APA flagship experimental psychology journal.",
            doi="",
            paper_url="",
            repository_platform="OSF",
            repository_url="https://osf.io/wjr7u/",
            data_evidence="OSF project description says open data and code; file evidence should be verified with OSF file listing.",
            script_evidence="OSF project description says open data and code; file evidence should be verified with OSF file listing.",
            analysis_type="needs manual mapping",
            candidate_task="Reproduce a core visual working memory analysis using the open data and code.",
            variables_needed="Visual working-memory outcome, condition/grouping variables, participant ID.",
            pingouin_route="pingouin-stat-router",
            verification_status="partial",
            notes="Confirmed via OSF API node metadata.",
        ),
        Candidate(
            id="osf_2ur8f",
            paper_title="Interactivity fosters Bayesian reasoning without instruction",
            authors="Vallee-Tourangeau, Abadie, & Vallee-Tourangeau",
            year="2015",
            journal="Journal of Experimental Psychology: General",
            journal_tier_reason="APA flagship experimental psychology journal.",
            doi="10.1037/a0039161",
            paper_url="https://doi.org/10.1037/a0039161",
            repository_platform="OSF",
            repository_url="https://osf.io/2ur8f/",
            data_evidence="OSF metadata says data set and code book.",
            script_evidence="No analysis script confirmed in seed metadata.",
            analysis_type="ANOVA / mean comparison likely",
            candidate_task="Reproduce the main group/condition comparison for Bayesian reasoning performance.",
            variables_needed="Performance outcome, condition/interactivity factor, participant ID.",
            pingouin_route="pg-anova",
            verification_status="partial",
            notes="Useful candidate if analysis scripts are found in parent/root project.",
        ),
    ]
    return seeds


def collect(limit: int) -> list[Candidate]:
    queries = []
    for journal in TOP_JOURNALS:
        queries.extend(
            [
                f'"{journal}" "open data" "analysis code"',
                f'"{journal}" "data" "scripts"',
                f'"{journal}" "OSF" "R script"',
            ]
        )

    seen: set[str] = set()
    candidates: list[Candidate] = []
    for seed in seed_candidates():
        seen.add(seed.id)
        candidates.append(seed)

    for query in queries:
        for item in osf_search(query):
            cand = osf_item_to_candidate(item, query, verify_files=True)
            if not cand or cand.id in seen:
                continue
            seen.add(cand.id)
            candidates.append(cand)
            if len(candidates) >= limit:
                return candidates
    return candidates


def write_outputs(candidates: list[Candidate]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jsonl = OUT_DIR / "real_paper_tasks.jsonl"
    csv_path = OUT_DIR / "real_paper_tasks.csv"
    md_path = OUT_DIR / "REAL_PAPER_50_TASKS.md"

    with jsonl.open("w", encoding="utf-8") as f:
        for cand in candidates:
            f.write(json.dumps(asdict(cand), ensure_ascii=False) + "\n")

    fields = list(asdict(candidates[0]).keys()) if candidates else [f.name for f in Candidate.__dataclass_fields__.values()]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for cand in candidates:
            writer.writerow(asdict(cand))

    lines = [
        "# Real-Paper Psychology Benchmark Candidates",
        "",
        "Scope: published psychology or behavioral-science papers in high-impact journals with open repository evidence.",
        "",
        "Verification labels:",
        "- `verified`: script found both data-like and script-like files in the repository listing.",
        "- `partial`: metadata indicates data/code or only one evidence type was found.",
        "- `needs_manual_check`: promising item, but repository file evidence needs manual inspection.",
        "",
        f"Total candidates: {len(candidates)}",
        "",
        "| # | Status | Journal | Paper / Repository | Candidate task | Route | Evidence |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for i, cand in enumerate(candidates, 1):
        evidence = f"data: {cand.data_evidence or 'n/a'}; scripts: {cand.script_evidence or 'n/a'}"
        paper = f"[{cand.paper_title}]({cand.repository_url})"
        lines.append(
            "| {i} | `{status}` | {journal} | {paper} | {task} | `{route}` | {evidence} |".format(
                i=i,
                status=cand.verification_status,
                journal=cand.journal.replace("|", "/"),
                paper=paper.replace("|", "/"),
                task=cand.candidate_task.replace("|", "/"),
                route=cand.pingouin_route,
                evidence=evidence.replace("|", "/"),
            )
        )

    lines.extend(
        [
            "",
            "## Use In Benchmark",
            "",
            "For each candidate, manually inspect the repository and convert one core published analysis into a task prompt.",
            "Keep the repository evidence in the prompt so baseline and plugin-guided conditions receive identical data access.",
            "",
            "Recommended task conversion fields:",
            "- `dataset_path_or_url`",
            "- `script_path_or_url`",
            "- `target_result`",
            "- `allowed_methods`",
            "- `expected_reporting_items`",
            "- `known_failure_modes`",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()
    candidates = collect(args.limit)
    write_outputs(candidates)
    counts: dict[str, int] = {}
    for cand in candidates:
        counts[cand.verification_status] = counts.get(cand.verification_status, 0) + 1
    print(json.dumps({"count": len(candidates), "status_counts": counts, "out_dir": str(OUT_DIR)}, indent=2))


if __name__ == "__main__":
    main()
