#!/usr/bin/env python3
"""Run local quality checks for the Pingouin Psych Stats plugin."""

from __future__ import annotations

import argparse
import inspect
import json
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
import pingouin as pg


PLUGIN_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SIGNATURE_BITS = {
    "ttest": ["alternative", "correction", "confidence"],
    "pairwise_tests": ["padjust", "effsize", "nan_policy"],
    "logistic_regression": ["X", "y", "remove_na"],
    "mediation_analysis": ["n_boot", "seed", "return_dist"],
    "power_ttest": ["alternative"],
    "mwu": ["alternative"],
    "kruskal": ["between", "detailed"],
    "friedman": ["within", "subject"],
    "chi2_independence": ["correction"],
    "power_chi2": ["dof", "w", "power"],
    "bayesfactor_ttest": ["paired", "r"],
    "multivariate_ttest": ["X", "Y", "paired"],
    "box_m": ["dvs", "group"],
    "madmedianrule": ["a"],
}

ROUTING_SCENARIOS = [
    ("pingouin-stat: I need a full psychology analysis and report.", "pingouin-stat"),
    ("I have pre and post anxiety scores for the same participants.", "pg-mean-tests"),
    ("Compare three therapy groups on depression scores.", "pg-anova"),
    ("Analyze time by treatment group with repeated measurements.", "pg-anova"),
    ("Check whether stress and sleep quality are correlated controlling age.", "pg-correlations"),
    ("Predict binary dropout from baseline motivation and age.", "pg-regression-mediation"),
    ("Test whether self-efficacy mediates intervention effect on wellbeing.", "pg-regression-mediation"),
    ("Calculate Cronbach alpha for a five-item scale.", "pg-reliability"),
    ("Compute ICC for ratings from three clinicians.", "pg-reliability"),
    ("How many participants do I need for r = .30?", "pg-power"),
    ("Turn this Pingouin table into APA Chinese prose.", "pg-reporting"),
    ("Approve this analysis before I report it.", "pg-analysis-approval"),
    ("I uploaded data but do not know if it is long or wide.", "pg-data-screening"),
    ("Compare two groups on a skewed outcome with small n using a rank test.", "pg-nonparametric"),
    ("Is therapy type associated with relapse yes or no?", "pg-categorical"),
    ("Give me the Bayes factor for this group difference.", "pg-bayesian"),
    ("Compare two groups on three symptom subscales together.", "pg-multivariate"),
]


def _rng() -> np.random.Generator:
    return np.random.default_rng(20260622)


def _assert_frame(value: object, *, min_rows: int = 1) -> None:
    if not isinstance(value, pd.DataFrame):
        raise AssertionError(f"expected DataFrame, got {type(value).__name__}")
    if len(value) < min_rows:
        raise AssertionError("result DataFrame is empty")


def _assert_finite(value: object) -> None:
    arr = np.asarray(value, dtype=float)
    if not np.isfinite(arr).all():
        raise AssertionError(f"non-finite value: {value}")


def test_signatures() -> None:
    for fn_name, expected_bits in EXPECTED_SIGNATURE_BITS.items():
        sig = str(inspect.signature(getattr(pg, fn_name)))
        missing = [bit for bit in expected_bits if bit not in sig]
        if missing:
            raise AssertionError(f"{fn_name} signature missing {missing}: {sig}")


def test_mean_tests() -> None:
    rng = _rng()
    x = rng.normal(0.2, 1.0, 35)
    y = rng.normal(0.7, 1.1, 35)
    _assert_frame(pg.ttest(x, y, correction="auto"))

    df = pd.DataFrame({
        "score": np.r_[x, y, rng.normal(1.0, 1.0, 35)],
        "group": np.repeat(["A", "B", "C"], 35),
    })
    _assert_frame(pg.pairwise_tests(data=df, dv="score", between="group", padjust="holm"))


def test_anova_family() -> None:
    rng = _rng()
    df = pd.DataFrame({
        "score": np.r_[rng.normal(0, 1, 30), rng.normal(0.5, 1, 30), rng.normal(1, 1, 30)],
        "group": np.repeat(["A", "B", "C"], 30),
    })
    _assert_frame(pg.anova(data=df, dv="score", between="group", detailed=True))
    _assert_frame(pg.welch_anova(data=df, dv="score", between="group"))

    ids = np.arange(36)
    rm = pd.DataFrame({
        "id": np.repeat(ids, 3),
        "condition": np.tile(["pre", "mid", "post"], len(ids)),
    })
    rm["score"] = rng.normal(0, 1, len(rm)) + rm["condition"].map({"pre": 0, "mid": 0.2, "post": 0.5}).to_numpy()
    _assert_frame(pg.rm_anova(data=rm, dv="score", within="condition", subject="id", detailed=True))

    mixed = rm.copy()
    group_map = {i: ("control" if i < 18 else "treatment") for i in ids}
    mixed["group"] = mixed["id"].map(group_map)
    mixed["score"] += (mixed["group"].eq("treatment") & mixed["condition"].eq("post")).astype(float) * 0.4
    _assert_frame(pg.mixed_anova(data=mixed, dv="score", within="condition", between="group", subject="id"))


def test_correlations() -> None:
    rng = _rng()
    n = 70
    x = rng.normal(size=n)
    z = rng.normal(size=n)
    y = 0.35 * x + 0.25 * z + rng.normal(size=n)
    df = pd.DataFrame({"x": x, "y": y, "z": z})
    _assert_frame(pg.corr(x=df["x"], y=df["y"]))
    _assert_frame(pg.partial_corr(data=df, x="x", y="y", covar="z"))
    _assert_frame(pg.pairwise_corr(data=df, columns=["x", "y", "z"], padjust="holm"))

    rm = pd.DataFrame({
        "id": np.repeat(np.arange(25), 3),
        "x": rng.normal(size=75),
    })
    rm["y"] = 0.3 * rm["x"] + rng.normal(size=75)
    _assert_frame(pg.rm_corr(data=rm, x="x", y="y", subject="id"))


def test_regression_mediation() -> None:
    rng = _rng()
    n = 90
    x1 = rng.normal(size=n)
    x2 = rng.normal(size=n)
    y = 0.5 * x1 - 0.2 * x2 + rng.normal(size=n)
    df = pd.DataFrame({"outcome": y, "x1": x1, "x2": x2})
    _assert_frame(pg.linear_regression(df[["x1", "x2"]], df["outcome"]))

    logits = -0.1 + 0.8 * x1 - 0.5 * x2
    p = 1 / (1 + np.exp(-logits))
    binary = rng.binomial(1, p)
    _assert_frame(pg.logistic_regression(df[["x1", "x2"]], binary, remove_na=False))

    med = pd.DataFrame({"x": x1})
    med["m"] = 0.5 * med["x"] + rng.normal(size=n)
    med["y"] = 0.3 * med["x"] + 0.6 * med["m"] + rng.normal(size=n)
    _assert_frame(pg.mediation_analysis(data=med, x="x", m="m", y="y", n_boot=100, seed=42), min_rows=4)


def test_reliability_power() -> None:
    rng = _rng()
    trait = rng.normal(size=60)
    items = pd.DataFrame({f"item{i}": trait + rng.normal(scale=0.6, size=60) for i in range(1, 6)})
    alpha, ci = pg.cronbach_alpha(data=items)
    _assert_finite([alpha, *ci])

    targets = np.repeat(np.arange(20), 3)
    raters = np.tile(["r1", "r2", "r3"], 20)
    true_score = np.repeat(rng.normal(size=20), 3)
    ratings = true_score + rng.normal(scale=0.3, size=60)
    icc_df = pd.DataFrame({"target": targets, "rater": raters, "rating": ratings})
    _assert_frame(pg.intraclass_corr(data=icc_df, targets="target", raters="rater", ratings="rating"))

    _assert_finite([
        pg.power_ttest(d=0.5, n=None, power=0.8, alpha=0.05),
        pg.power_ttest2n(nx=30, ny=35, d=0.5, alpha=0.05),
        pg.power_anova(eta_squared=0.06, k=3, n=None, power=0.8, alpha=0.05),
        pg.power_rm_anova(eta_squared=0.06, m=3, n=None, power=0.8, alpha=0.05),
        pg.power_corr(r=0.3, n=None, power=0.8, alpha=0.05),
    ])


def test_nonparametric() -> None:
    rng = _rng()
    x = rng.normal(0.2, 1.0, 30)
    y = rng.normal(0.8, 1.1, 30)
    _assert_frame(pg.mwu(x, y))
    _assert_frame(pg.wilcoxon(x, y))

    df = pd.DataFrame({
        "score": np.r_[x, y, rng.normal(1.2, 1.0, 30)],
        "group": np.repeat(["A", "B", "C"], 30),
    })
    _assert_frame(pg.kruskal(data=df, dv="score", between="group"))

    ids = np.arange(20)
    rm = pd.DataFrame({
        "id": np.repeat(ids, 3),
        "cond": np.tile(["t1", "t2", "t3"], len(ids)),
    })
    rm["score"] = rng.normal(0, 1, len(rm)) + rm["cond"].map({"t1": 0, "t2": 0.2, "t3": 0.5}).to_numpy()
    _assert_frame(pg.friedman(data=rm, dv="score", within="cond", subject="id"))
    rm["passed"] = (rng.random(len(rm)) > 0.5).astype(int)
    _assert_frame(pg.cochran(data=rm, dv="passed", within="cond", subject="id"))


def test_categorical() -> None:
    rng = _rng()
    df = pd.DataFrame({
        "group": rng.choice(["A", "B", "C"], 150),
        "response": rng.choice(["yes", "no"], 150),
    })
    _expected, _observed, stats = pg.chi2_independence(data=df, x="group", y="response")
    _assert_frame(stats)

    paired = pd.DataFrame({
        "before": rng.integers(0, 2, 80),
        "after": rng.integers(0, 2, 80),
    })
    _obs, mcnemar = pg.chi2_mcnemar(data=paired, x="before", y="after")
    _assert_frame(mcnemar)

    _assert_finite(pg.power_chi2(dof=1, w=0.3, n=100, alpha=0.05))


def test_bayesian() -> None:
    rng = _rng()
    x = rng.normal(0.2, 1.0, 30)
    y = rng.normal(0.8, 1.0, 30)
    tt = pg.ttest(x, y)
    _assert_finite(pg.bayesfactor_ttest(float(tt["T"].iloc[0]), 30, 30))
    _assert_finite(pg.bayesfactor_pearson(0.3, 60))
    _assert_finite(pg.bayesfactor_binom(55, 100, 0.5))


def test_multivariate() -> None:
    rng = _rng()
    x = rng.normal(0.0, 1.0, (40, 3))
    y = rng.normal(0.5, 1.0, (45, 3))
    _assert_frame(pg.multivariate_ttest(x, y))

    df = pd.DataFrame(np.vstack([x, y]), columns=["v1", "v2", "v3"])
    df["group"] = ["A"] * 40 + ["B"] * 45
    _assert_frame(pg.box_m(df, dvs=["v1", "v2", "v3"], group="group"))

    hz = pg.multivariate_normality(x, alpha=0.05)
    _assert_finite(hz.pval)

    flags = pg.madmedianrule(df["v1"].to_numpy())
    if flags.dtype != bool:
        raise AssertionError("madmedianrule should return a boolean mask")


def test_static_budget(max_skill_bytes: int) -> None:
    skill_files = sorted((PLUGIN_ROOT / "skills").glob("*/SKILL.md"))
    too_large = [(path.name, path.stat().st_size) for path in skill_files if path.stat().st_size > max_skill_bytes]
    if too_large:
        raise AssertionError(f"skill files exceed {max_skill_bytes} bytes: {too_large}")

    required_refs = [
        "workflow-index.md",
        "supervision-gates.md",
        "intake-checklist.md",
        "test-scenarios.md",
        "pingouin-api-quickref.md",
        "apa-output-template.md",
    ]
    missing = [name for name in required_refs if not (PLUGIN_ROOT / "references" / name).is_file()]
    if missing:
        raise AssertionError(f"missing references: {missing}")


def test_routing_matrix() -> None:
    workflow_index = (PLUGIN_ROOT / "references" / "workflow-index.md").read_text(encoding="utf-8")
    missing = [skill for _, skill in ROUTING_SCENARIOS if skill not in workflow_index]
    if missing:
        raise AssertionError(f"routing index missing skills: {sorted(set(missing))}")


def test_main_entry_contract() -> None:
    main_skill = (PLUGIN_ROOT / "skills" / "pingouin-stat" / "SKILL.md").read_text(encoding="utf-8")
    approval_skill = (PLUGIN_ROOT / "skills" / "pg-analysis-approval" / "SKILL.md").read_text(encoding="utf-8")
    required_main = ["Intake", "Route", "Approve", "Organize", "Word/docx", "PDF", "LaTeX"]
    missing_main = [item for item in required_main if item not in main_skill]
    if missing_main:
        raise AssertionError(f"pingouin-stat missing contract terms: {missing_main}")
    required_approval = ["APPROVED", "APPROVED_WITH_NOTES", "REVISE", "BLOCKED", "S0", "S5"]
    missing_approval = [item for item in required_approval if item not in approval_skill]
    if missing_approval:
        raise AssertionError(f"pg-analysis-approval missing labels/gates: {missing_approval}")


TESTS: list[tuple[str, Callable[[], None]]] = [
    ("signatures", test_signatures),
    ("mean_tests", test_mean_tests),
    ("anova_family", test_anova_family),
    ("correlations", test_correlations),
    ("regression_mediation", test_regression_mediation),
    ("reliability_power", test_reliability_power),
    ("nonparametric", test_nonparametric),
    ("categorical", test_categorical),
    ("bayesian", test_bayesian),
    ("multivariate", test_multivariate),
    ("routing_matrix", test_routing_matrix),
    ("main_entry_contract", test_main_entry_contract),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-skill-bytes", type=int, default=3600)
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    args = parser.parse_args()

    results = []
    all_tests = TESTS + [("static_budget", lambda: test_static_budget(args.max_skill_bytes))]
    for name, fn in all_tests:
        try:
            fn()
        except Exception as exc:  # noqa: BLE001 - quality script should report all failures.
            results.append({"name": name, "status": "fail", "error": str(exc)})
        else:
            results.append({"name": name, "status": "pass"})

    if args.json:
        print(json.dumps({"pingouin": pg.__version__, "results": results}, indent=2))
    else:
        print(f"Pingouin {pg.__version__}")
        for result in results:
            suffix = f" - {result['error']}" if result["status"] == "fail" else ""
            print(f"{result['status'].upper():4} {result['name']}{suffix}")

    if any(result["status"] == "fail" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
