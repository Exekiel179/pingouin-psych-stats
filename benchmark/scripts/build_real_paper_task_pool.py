#!/usr/bin/env python3
"""Build a 50-item real-paper candidate pool for the Pingouin benchmark.

Sources are intentionally mixed:
1. A published meta-science dataset on computational reproducibility in
   psychology Registered Reports, which gives DOI, journal, data URL, script
   URL, script language, and reproducibility status for real papers.
2. Curated high-impact OSF/Zenodo candidates discovered during plugin work.

This creates candidates, not final executable tasks. A human should inspect
each repository and convert one core analysis into a benchmark prompt.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd


BENCH_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = BENCH_ROOT / "real_paper_candidates"
SOURCE_XLSX = OUT_DIR / "Data_for_Analysis_of_Open_Data_and_Computational_Reproducibility_in_Registered_Reports_in_Psychology.xlsx"


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
    research_question: str
    article_hypotheses: str
    experimental_design: str
    data_analysis_plan: str
    result_interpretation_target: str
    variables_needed: str
    pingouin_route: str
    source_language: str
    benchmark_level: str
    verification_status: str
    notes: str


def clean(value: object) -> str:
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def year_from_study(study: str) -> str:
    m = re.search(r"(19|20)\d{2}", study)
    return m.group(0) if m else ""


def platform_from_url(url: str) -> str:
    lower = url.lower()
    if "osf.io" in lower:
        return "OSF"
    if "figshare" in lower:
        return "Figshare"
    if "zenodo" in lower:
        return "Zenodo"
    if "dataverse" in lower:
        return "Dataverse"
    if "psycharchives" in lower:
        return "PsychArchives"
    if "icpsr" in lower:
        return "ICPSR"
    if "github" in lower:
        return "GitHub"
    return "Other repository"


def tier_reason(journal: str, source: str) -> str:
    top = {
        "Nature Human Behaviour": "Top multidisciplinary behavioral-science journal.",
        "Psychological Science": "APS flagship empirical psychology journal.",
        "Journal of Experimental Psychology: General": "APA flagship experimental psychology journal.",
        "Journal of Personality and Social Psychology": "APA flagship social/personality psychology journal.",
        "Cognition": "Leading cognitive psychology journal.",
        "Nature Communications": "High-impact multidisciplinary journal.",
        "PNAS": "High-impact multidisciplinary journal with behavioral-science papers.",
        "Psychological Methods": "Top methods journal in psychology.",
        "Behavior Research Methods": "Leading psychology methods and tooling journal.",
    }
    if journal in top:
        return top[journal]
    if source == "registered_reports_reproducibility":
        return "Peer-reviewed psychology Registered Report source table; not all journals are top-tier, but papers have explicit data/script audit fields."
    return "High-impact/target-journal candidate from open repository search; verify journal tier before final benchmark use."


def infer_route(language: str, comments: str) -> tuple[str, str]:
    hay = f"{language} {comments}".lower()
    if any(k in hay for k in ["correlation", "pearson", "spearman"]):
        return "correlation", "pg-correlations"
    if any(k in hay for k in ["anova", "ancova", "interaction"]):
        return "ANOVA / factorial comparison", "pg-anova"
    if any(k in hay for k in ["regression", "logistic"]):
        return "regression", "pg-regression-mediation"
    if any(k in hay for k in ["t-test", "ttest", "mean difference"]):
        return "mean comparison", "pg-mean-tests"
    return "reproduce main inferential result", "pingouin-stat-router"


def from_registered_reports(limit: int = 37) -> list[Candidate]:
    if not SOURCE_XLSX.exists():
        raise FileNotFoundError(
            f"Missing {SOURCE_XLSX}. Run collect_real_paper_candidates.py once or download the OSF source table."
        )
    df = pd.read_excel(SOURCE_XLSX, sheet_name="Data")
    df = df[df["doi"].apply(lambda x: isinstance(x, str) and x.startswith("10."))]
    df = df[(df["availability"] == 1) & (df["analysis_script_included"] == 1)]
    df = df.sort_values(
        by=["reproducible_final", "run_script_final", "journal"],
        ascending=[False, False, True],
        na_position="last",
    )

    candidates: list[Candidate] = []
    for idx, row in df.head(limit).iterrows():
        study = clean(row["study"])
        journal = clean(row["journal"])
        doi = clean(row["doi"])
        data_url = clean(row["url_dataset"])
        script_url = clean(row["url_scripts"]) or data_url
        language = clean(row["programming_language"])
        comments = " ".join(
            clean(row.get(col, ""))
            for col in [
                "comments_on_reproducibility_po",
                "comments_on_reproducibility_dl",
                "comments_on_reproducibility_sg",
                "resolving_disagreements_between_coders",
            ]
        )
        analysis, route = infer_route(language, comments)
        reproducible = clean(row.get("main_reason_not_reproducible", ""))
        status = "verified" if clean(row["run_script_final"]) == "1.0" else "partial"
        if clean(row["reproducible_final"]) != "1.0":
            status = "partial"

        repo = script_url or data_url
        candidates.append(
            Candidate(
                id=f"rr_{len(candidates)+1:03d}",
                paper_title=f"{study} registered report",
                authors=study,
                year=year_from_study(study),
                journal=journal,
                journal_tier_reason=tier_reason(journal, "registered_reports_reproducibility"),
                doi=doi,
                paper_url=f"https://doi.org/{doi}",
                repository_platform=platform_from_url(repo),
                repository_url=repo,
                data_evidence=data_url,
                script_evidence=f"{script_url} ({language})",
                analysis_type=analysis,
                candidate_task=f"Reproduce one main inferential result from the published Registered Report using the shared data and {language or 'analysis'} script.",
                research_question="Extract from the article introduction/registered report rationale before final task release.",
                article_hypotheses="Extract preregistered or stated hypotheses from the article before final task release.",
                experimental_design="Extract participants, design factors, within/between-subject structure, measures, and exclusion rules from Methods.",
                data_analysis_plan=f"Use the shared {language or 'analysis'} script to identify the target model/test; translate to Pingouin where in scope.",
                result_interpretation_target="Compare the reproduced result with the paper's reported conclusion; flag effect direction, uncertainty, and overclaiming.",
                variables_needed="Extract outcome, predictors/factors, covariates, and subject/repeated-measures identifiers from the original script/codebook.",
                pingouin_route=route,
                source_language="English",
                benchmark_level="full_chain_candidate",
                verification_status=status,
                notes=f"From 'Analysis of Open Data and Computational Reproducibility in Registered Reports in Psychology' source table. Reproducibility label: {reproducible or 'not recorded'}.",
            )
        )
    return candidates


def curated_candidates() -> list[Candidate]:
    rows = [
        {
            "id": "curated_osf_wjr7u",
            "paper_title": "Object-based encoding constrains storage in visual working memory",
            "authors": "",
            "year": "",
            "journal": "Journal of Experimental Psychology: General",
            "doi": "",
            "paper_url": "",
            "repository_platform": "OSF",
            "repository_url": "https://osf.io/wjr7u/",
            "data_evidence": "OSF metadata: open data and code for accepted JEP:General paper.",
            "script_evidence": "OSF metadata: open data and code for accepted JEP:General paper.",
            "analysis_type": "visual working-memory group/condition analysis",
            "candidate_task": "Reproduce a core condition effect in visual working memory storage.",
            "research_question": "How does object-based encoding constrain visual working-memory storage?",
            "article_hypotheses": "Extract exact hypothesis statements from the published article before final task release.",
            "experimental_design": "Visual working-memory experiment; inspect methods for condition structure and repeated-measures design.",
            "data_analysis_plan": "Use shared code to identify the reported condition effect; translate ANOVA/mean tests to Pingouin if in scope.",
            "result_interpretation_target": "Explain whether the reproduced condition effect supports object-based storage constraints.",
            "variables_needed": "Outcome accuracy/recall, condition/grouping variables, participant ID.",
            "pingouin_route": "pg-anova",
            "source_language": "English",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "partial",
            "notes": "OSF API metadata verified; file-level evidence requires manual inspection.",
        },
        {
            "id": "curated_osf_2adxj",
            "paper_title": "Nature Human Behaviour Repro - Newson et al. (2025)",
            "authors": "Newson et al.",
            "year": "2025",
            "journal": "Nature Human Behaviour",
            "doi": "",
            "paper_url": "",
            "repository_platform": "OSF",
            "repository_url": "https://osf.io/2adxj/",
            "data_evidence": "Correlation_BonfCorrected.xlsx",
            "script_evidence": "R_codes_v3_Newsonetal.2025.qmd; Syntax-Reproducibility-Robustness.sps",
            "analysis_type": "correlation / robustness analysis",
            "candidate_task": "Reproduce a reported correlation/robustness result from the shared spreadsheet and scripts.",
            "research_question": "Extract exact research question from the Nature Human Behaviour article and robustness report.",
            "article_hypotheses": "Extract focal predictions and robustness claims from the article/script.",
            "experimental_design": "Inspect paper and repository for sample, measures, and correlational or experimental structure.",
            "data_analysis_plan": "Reproduce the correlation/robustness result and check multiple-comparison correction.",
            "result_interpretation_target": "Assess whether the reproduced correlation supports the stated behavioral conclusion.",
            "variables_needed": "Correlation variables and correction family from the script.",
            "pingouin_route": "pg-correlations",
            "source_language": "English",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "verified",
            "notes": "Discovered by OSF API file listing.",
        },
        {
            "id": "curated_osf_7wgv2",
            "paper_title": "Robustness report: Arechar et al. (2023), Nature Human Behaviour",
            "authors": "Arechar et al.",
            "year": "2023",
            "journal": "Nature Human Behaviour",
            "doi": "",
            "paper_url": "",
            "repository_platform": "OSF",
            "repository_url": "https://osf.io/7wgv2/",
            "data_evidence": "CR.csv; m_agg.rds; m_rob-alt.rds; m_rob-rev.rds",
            "script_evidence": "Fig1-rev2.R; REP_supps-rev.Rmd; REP_supps.Rmd",
            "analysis_type": "robustness / model comparison",
            "candidate_task": "Reproduce one robustness comparison using the shared CSV/R scripts.",
            "research_question": "Extract exact research question from Arechar et al. and the robustness report.",
            "article_hypotheses": "Extract focal hypothesis and robustness alternative specifications.",
            "experimental_design": "Inspect paper and repository for participant structure, treatment/condition variables, and outcome.",
            "data_analysis_plan": "Reproduce one reported robustness comparison; route to Pingouin only if the model is ANOVA/correlation/mean-test compatible.",
            "result_interpretation_target": "Explain whether the robustness result preserves or weakens the original claim.",
            "variables_needed": "Outcome and model specification from Fig1 or supplement script.",
            "pingouin_route": "pingouin-stat-router",
            "source_language": "English",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "verified",
            "notes": "Discovered by OSF API file listing.",
        },
        {
            "id": "curated_zenodo_15672966",
            "paper_title": "Protracted development of gaze behavior",
            "authors": "",
            "year": "2025",
            "journal": "Nature Human Behaviour",
            "doi": "10.5281/zenodo.15672966",
            "paper_url": "https://doi.org/10.5281/zenodo.15672966",
            "repository_platform": "Zenodo",
            "repository_url": "https://zenodo.org/records/15672966",
            "data_evidence": "Zenodo record title indicates raw eyetracking data for Nature Human Behaviour paper.",
            "script_evidence": "Script/code evidence not confirmed in quick API search.",
            "analysis_type": "developmental gaze-behavior analysis",
            "candidate_task": "If scripts are present, reproduce one age/development effect in gaze behavior.",
            "research_question": "How does gaze behavior develop across age or developmental stage?",
            "article_hypotheses": "Extract exact developmental predictions from the paper before final task release.",
            "experimental_design": "Developmental eye-tracking dataset; inspect task, age groups, repeated trials, and participant IDs.",
            "data_analysis_plan": "Identify one age/development effect; use ANOVA/correlation/regression depending on paper script.",
            "result_interpretation_target": "Interpret whether the reproduced result supports protracted gaze-behavior development.",
            "variables_needed": "Age/development predictor, gaze outcome, participant/trial identifiers.",
            "pingouin_route": "pg-anova",
            "source_language": "English",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "Zenodo hit found; verify files include analysis scripts before using.",
        },
    ]
    out = []
    for row in rows:
        journal = row["journal"]
        out.append(Candidate(journal_tier_reason=tier_reason(journal, "curated"), **row))
    return out


def chinese_candidates() -> list[Candidate]:
    rows = [
        {
            "id": "cn_psydb_orthographic_wm",
            "paper_title": "汉语发展性阅读障碍儿童的正字法工作记忆加工缺陷",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "group comparison / cognitive-developmental analysis",
            "candidate_task": "从研究问题出发，复原阅读障碍儿童与对照组在正字法工作记忆任务上的核心差异分析。",
            "research_question": "汉语发展性阅读障碍儿童是否存在正字法工作记忆加工缺陷？",
            "article_hypotheses": "提取论文中关于阅读障碍组在正字法工作记忆任务表现较弱的具体假设。",
            "experimental_design": "中文认知/发展心理实验；需核验被试分组、任务条件、因变量和是否有重复测量。",
            "data_analysis_plan": "优先复现组间差异、条件主效应或交互；根据设计路由到 t 检验、ANOVA 或混合 ANOVA。",
            "result_interpretation_target": "解释结果是否支持发展性阅读障碍的正字法工作记忆缺陷解释，并避免因果过度推断。",
            "variables_needed": "组别、任务条件、正确率/反应时/记忆表现、被试 ID。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_belief_perseverance",
            "paper_title": "对立证据和因果关系强度对信念固着的影响",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "factorial experiment / interaction",
            "candidate_task": "根据研究问题重建对立证据和因果关系强度对信念固着的析因实验分析。",
            "research_question": "对立证据与因果关系强度如何影响信念固着？",
            "article_hypotheses": "提取关于对立证据、因果强度及其交互影响信念更新/固着程度的假设。",
            "experimental_design": "可能为多因素实验；需核验因素水平、组间/组内结构、操纵检查和因变量。",
            "data_analysis_plan": "复现核心主效应/交互效应；检查方差齐性、重复测量结构和事后比较。",
            "result_interpretation_target": "解释对立证据与因果强度如何共同影响信念固着，区分统计显著与理论支持。",
            "variables_needed": "对立证据条件、因果强度条件、信念评分/变化量、被试 ID。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_crowdfunding_emotion",
            "paper_title": "公益众筹中如何提高项目吸引力：项目图片情绪效价和内容信息的作用",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "factorial experiment / mediation possible",
            "candidate_task": "复原图片情绪效价和内容信息对公益众筹项目吸引力的核心实验分析。",
            "research_question": "项目图片情绪效价和内容信息如何影响公益众筹项目吸引力？",
            "article_hypotheses": "提取关于情绪效价、内容信息及潜在交互/中介机制的假设。",
            "experimental_design": "社会/消费心理实验；需核验图片情绪效价、内容信息操纵、吸引力评分和样本结构。",
            "data_analysis_plan": "复现主效应/交互；若论文含中介，检查 Pingouin mediation 是否适用。",
            "result_interpretation_target": "解释哪些图片/内容组合提高项目吸引力，并避免把实验情境外推过度。",
            "variables_needed": "情绪效价、内容信息条件、吸引力评分、可能的中介变量、被试 ID。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_sentence_production_eye_tracking",
            "paper_title": "中文句子产生中语义和音韵编码的时间进程及交互作用",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related eye-movement dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "psycholinguistic repeated-measures analysis",
            "candidate_task": "从研究问题出发复原语义/音韵编码时间进程的眼动或行为指标分析。",
            "research_question": "中文句子产生中语义编码与音韵编码的时间进程如何展开，二者是否交互？",
            "article_hypotheses": "提取关于语义效应、音韵效应及其时间进程/交互的假设。",
            "experimental_design": "心理语言学实验；需核验项目/被试双随机结构、时间窗、条件和重复测量因素。",
            "data_analysis_plan": "Pingouin 可用于简化的重复测量 ANOVA/相关分析；若原文为混合效应模型，应标记超出 Pingouin 完整范围。",
            "result_interpretation_target": "解释时间窗效应是否支持语义与音韵编码的顺序或交互模型。",
            "variables_needed": "语义条件、音韵条件、时间窗、眼动/反应指标、被试 ID、项目 ID。",
            "pingouin_route": "pingouin-stat-router",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；心理语言学项目级数据可能需要 mixed models，需标注 Pingouin 范围限制。",
        },
        {
            "id": "cn_psydb_arithmetic_principles",
            "paper_title": "算术原则知识在成人数学认知中的作用",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "cognitive task mean comparison / regression",
            "candidate_task": "复原算术原则知识与成人数学认知表现之间的核心关系或组间差异分析。",
            "research_question": "算术原则知识在成人数学认知表现中起什么作用？",
            "article_hypotheses": "提取关于原则知识预测数学认知表现或调节任务表现的假设。",
            "experimental_design": "数学认知行为实验；需核验任务类型、条件、表现指标和个体差异测量。",
            "data_analysis_plan": "根据论文脚本复现相关、回归或条件比较；检查异常值和测验信度。",
            "result_interpretation_target": "解释算术原则知识与数学认知表现的关联强度及其理论含义。",
            "variables_needed": "原则知识得分、数学认知表现、条件/任务类型、被试 ID。",
            "pingouin_route": "pg-regression-mediation",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_learning_judgment_encoding",
            "paper_title": "编码方式和材料类型对不同年龄组项目再认和联结再认年老化的影响",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "mixed ANOVA / aging cognition",
            "candidate_task": "复原编码方式、材料类型和年龄组对项目/联结再认的核心混合设计分析。",
            "research_question": "编码方式和材料类型如何影响不同年龄组的项目再认与联结再认老化？",
            "article_hypotheses": "提取关于年龄组、编码方式、材料类型及其交互影响记忆表现的假设。",
            "experimental_design": "老化与记忆实验；需核验年龄组为组间因素，编码/材料/再认类型是否为组内因素。",
            "data_analysis_plan": "复现混合 ANOVA；检查被试 ID、长表格式、球形性和事后比较校正。",
            "result_interpretation_target": "解释交互结果是否支持特定编码方式缓解或放大记忆老化差异。",
            "variables_needed": "年龄组、编码方式、材料类型、再认类型、正确率/d-prime、被试 ID。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_social_class_fairness",
            "paper_title": "社会阶层与公平规范的关系：心理权利的中介作用",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates an Acta Psychologica Sinica related dataset.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "mediation / regression",
            "candidate_task": "复原社会阶层、心理权利与公平规范之间的中介分析。",
            "research_question": "心理权利是否中介社会阶层与公平规范之间的关系？",
            "article_hypotheses": "提取关于社会阶层影响心理权利并进一步影响公平规范的中介假设。",
            "experimental_design": "社会心理问卷/实验；需核验横断或实验设计、量表得分和控制变量。",
            "data_analysis_plan": "复现回归/中介分析；检查量表信度、缺失值、协变量和因果语言限制。",
            "result_interpretation_target": "解释中介效应是否支持理论路径，并明确相关/横断数据的因果限制。",
            "variables_needed": "社会阶层、心理权利、公平规范、控制变量、量表条目。",
            "pingouin_route": "pg-regression-mediation",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；需在 ScienceDB/PsyDB 中核验数据文件、代码本和脚本。",
        },
        {
            "id": "cn_psydb_working_memory_training",
            "paper_title": "工作记忆训练迁移效应的边界条件",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB search result indicates possible Acta Psychologica Sinica related dataset; title requires verification.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "pre-post mixed design / training effect",
            "candidate_task": "复原训练组与控制组在前后测迁移任务上的核心交互分析。",
            "research_question": "工作记忆训练在什么条件下产生迁移效应？",
            "article_hypotheses": "提取关于训练组、测量时间和迁移任务类型交互的假设。",
            "experimental_design": "训练干预设计；需核验组别、前后测、任务类型和随机分配情况。",
            "data_analysis_plan": "复现组别 x 时间混合 ANOVA；检查基线差异、缺失/脱落和多重比较。",
            "result_interpretation_target": "解释是否存在训练迁移效应及其边界条件，避免把练习效应误解为广泛迁移。",
            "variables_needed": "组别、时间、任务类型、表现指标、被试 ID。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "中文子集候选；标题需人工确认是否为心理学报论文及对应数据集。",
        },
        {
            "id": "cn_psydb_emotion_attention",
            "paper_title": "情绪刺激对注意捕获或认知控制的影响",
            "authors": "",
            "year": "",
            "journal": "心理学报",
            "doi": "",
            "paper_url": "",
            "repository_platform": "ScienceDB/Psychological Science Data Bank",
            "repository_url": "https://www.scidb.cn/en/psych",
            "data_evidence": "ScienceDB/PsyDB contains multiple Acta Psychologica Sinica cognitive/emotion datasets; exact article requires verification.",
            "script_evidence": "Analysis script not confirmed; inspect dataset files.",
            "analysis_type": "repeated-measures ANOVA / reaction-time analysis",
            "candidate_task": "复原情绪条件对注意或认知控制任务反应时/正确率的核心分析。",
            "research_question": "情绪刺激如何影响注意捕获或认知控制表现？",
            "article_hypotheses": "从具体论文中提取情绪效价/唤醒度影响注意指标的假设。",
            "experimental_design": "情绪认知实验；需核验情绪条件、任务条件、RT 清洗规则和重复测量结构。",
            "data_analysis_plan": "复现重复测量 ANOVA 或配对比较；检查 RT 异常值剔除、正确试次筛选和多重比较。",
            "result_interpretation_target": "解释情绪效应是否支持注意捕获/控制资源理论。",
            "variables_needed": "情绪条件、任务条件、RT/正确率、被试 ID、试次筛选字段。",
            "pingouin_route": "pg-anova",
            "source_language": "Chinese",
            "benchmark_level": "full_chain_candidate",
            "verification_status": "needs_manual_check",
            "notes": "占位中文候选；必须替换为具体 PsyDB 论文/数据集记录后才能进入正式 benchmark。",
        },
    ]
    out = []
    for row in rows:
        out.append(Candidate(journal_tier_reason="Chinese top psychology journal; prioritize ScienceDB/PsyDB linked open data, but verify analysis scripts.", **row))
    return out


def write_outputs(candidates: list[Candidate]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jsonl = OUT_DIR / "real_paper_tasks.jsonl"
    csv_path = OUT_DIR / "real_paper_tasks.csv"
    md_path = OUT_DIR / "REAL_PAPER_50_TASKS.md"

    with jsonl.open("w", encoding="utf-8") as f:
        for cand in candidates:
            f.write(json.dumps(asdict(cand), ensure_ascii=False) + "\n")

    fields = list(asdict(candidates[0]).keys())
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for cand in candidates:
            writer.writerow(asdict(cand))

    lines = [
        "# Real-Paper Psychology Benchmark Candidates",
        "",
        "This file lists real published psychology/behavioral-science paper candidates with open data and analysis-script evidence.",
        "",
        "Important: these are benchmark candidates, not all ready-to-run tasks. Before adding an item to the executable benchmark, inspect the repository and convert one specific result/table/figure into a task with expected outputs.",
        "",
        "## Verification Labels",
        "",
        "- `verified`: source table or repository evidence says data and analysis scripts are available and scripts could be run or files were listed.",
        "- `partial`: data and scripts are indicated, but reproduction failed, was incomplete, or file-level evidence still needs manual inspection.",
        "- `needs_manual_check`: promising high-impact record, but script evidence is not yet confirmed.",
        "",
        "## Source Strategy",
        "",
        "- Main seed: `Analysis of Open Data and Computational Reproducibility in Registered Reports in Psychology` OSF/PsyArXiv project, which audits real psychology Registered Reports and records data/script availability.",
        "- Supplement: curated OSF/Zenodo candidates from high-impact journals such as `Nature Human Behaviour` and `Journal of Experimental Psychology: General`.",
        "- Target repositories: OSF/Open Science Framework, PsychArchives, Dataverse, ICPSR, Zenodo, Figshare. Current automated evidence is strongest for OSF and one Zenodo candidate.",
        "",
        f"Total candidates: {len(candidates)}",
        "",
        "| # | Status | Journal | Paper | Repository | Task | Route |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for i, cand in enumerate(candidates, 1):
        paper = f"[{cand.paper_title}]({cand.paper_url or cand.repository_url})"
        repo = f"[{cand.repository_platform}]({cand.repository_url})"
        lines.append(
            f"| {i} | `{cand.verification_status}` | {cand.journal} | {paper} | {repo} | {cand.candidate_task} | `{cand.pingouin_route}` |"
        )

    lines.extend(
        [
            "",
            "## Full Evidence Fields",
            "",
        ]
    )
    for i, cand in enumerate(candidates, 1):
        lines.extend(
            [
                f"### {i}. {cand.paper_title}",
                "",
                f"- Journal: {cand.journal}",
                f"- DOI/paper: {cand.paper_url or cand.doi or 'not recorded'}",
                f"- Repository: {cand.repository_url}",
                f"- Data evidence: {cand.data_evidence or 'not recorded'}",
                f"- Script evidence: {cand.script_evidence or 'not recorded'}",
                f"- Research question: {cand.research_question}",
                f"- Article hypotheses: {cand.article_hypotheses}",
                f"- Experimental design: {cand.experimental_design}",
                f"- Data analysis plan: {cand.data_analysis_plan}",
                f"- Result interpretation target: {cand.result_interpretation_target}",
                f"- Analysis type: {cand.analysis_type}",
                f"- Pingouin route: `{cand.pingouin_route}`",
                f"- Source language: {cand.source_language}",
                f"- Benchmark level: {cand.benchmark_level}",
                f"- Verification: `{cand.verification_status}`",
                f"- Notes: {cand.notes}",
                "",
            ]
        )

    lines.extend(
        [
            "## Conversion Rule For opencode Benchmark",
            "",
            "For each final executable task, create a prompt that includes:",
            "",
            "- paper citation and repository URL;",
            "- exact dataset file(s) to use;",
            "- exact script/codebook file(s) to inspect;",
            "- one target result, table, or figure to reproduce;",
            "- allowed method family and required assumption checks;",
            "- expected APA-style reporting fields;",
            "- known failure modes, especially repeated-measures structure, multiple comparisons, and unsupported causal claims.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    base = from_registered_reports(limit=37)
    curated = curated_candidates()
    chinese = chinese_candidates()
    seen = {c.doi or c.repository_url or c.id for c in base}
    seen_ids = {c.id for c in base}
    merged = base[:]
    for cand in curated + chinese:
        key = cand.doi or cand.repository_url
        if cand.id in seen_ids:
            continue
        if key in seen and cand.repository_platform != "ScienceDB/Psychological Science Data Bank":
            continue
        merged.append(cand)
        seen.add(key)
        seen_ids.add(cand.id)
    merged = merged[:50]
    write_outputs(merged)
    counts: dict[str, int] = {}
    platforms: dict[str, int] = {}
    for cand in merged:
        counts[cand.verification_status] = counts.get(cand.verification_status, 0) + 1
        platforms[cand.repository_platform] = platforms.get(cand.repository_platform, 0) + 1
    print(json.dumps({"count": len(merged), "status_counts": counts, "platform_counts": platforms}, indent=2))


if __name__ == "__main__":
    main()
