#!/usr/bin/env python3
"""Emit compact Pingouin analysis templates."""

from __future__ import annotations

import argparse
import textwrap


TEMPLATES = {
    "screen": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        print(df.info())
        print(df.describe(include="all"))
        print(df.isna().mean().sort_values(ascending=False).head(20))

        # Edit variable names before running.
        print(pg.normality(data=df, dv="score", group="group").round(3))
        print(pg.homoscedasticity(data=df, dv="score", group="group").round(3))
    """,
    "ttest": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        x = df.loc[df["group"].eq("A"), "score"]
        y = df.loc[df["group"].eq("B"), "score"]

        res = pg.ttest(x, y, paired=False, alternative="two-sided",
                       correction="auto", confidence=0.95).round(3)
        pg.print_table(res)
    """,
    "pairwise": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        res = pg.pairwise_tests(data=df, dv="score", between="group",
                                parametric=True, padjust="holm",
                                effsize="hedges").round(3)
        pg.print_table(res)
    """,
    "anova": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        aov = pg.anova(data=df, dv="score", between="group", detailed=True).round(3)
        pg.print_table(aov)

        posthoc = pg.pairwise_tests(data=df, dv="score", between="group",
                                    padjust="holm", effsize="hedges").round(3)
        pg.print_table(posthoc)
    """,
    "rm-anova": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data_long.csv")
        aov = pg.rm_anova(data=df, dv="score", within="condition",
                          subject="id", detailed=True).round(3)
        pg.print_table(aov)

        posthoc = pg.pairwise_tests(data=df, dv="score", within="condition",
                                    subject="id", padjust="holm",
                                    effsize="hedges").round(3)
        pg.print_table(posthoc)
    """,
    "mixed-anova": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data_long.csv")
        aov = pg.mixed_anova(data=df, dv="score", within="time",
                             between="group", subject="id").round(3)
        pg.print_table(aov)

        posthoc = pg.pairwise_tests(data=df, dv="score", within="time",
                                    between="group", subject="id",
                                    padjust="holm", effsize="hedges").round(3)
        pg.print_table(posthoc)
    """,
    "corr": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        res = pg.corr(x=df["x"], y=df["y"], method="pearson",
                      alternative="two-sided").round(3)
        pg.print_table(res)
    """,
    "partial-corr": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        res = pg.partial_corr(data=df, x="x", y="y",
                              covar=["age", "baseline"],
                              method="pearson").round(3)
        pg.print_table(res)
    """,
    "regression": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv").dropna(subset=["outcome", "x1", "x2"])
        res = pg.linear_regression(df[["x1", "x2"]], df["outcome"],
                                   add_intercept=True).round(3)
        pg.print_table(res)
    """,
    "logistic": """
        import pandas as pd
        import pingouin as pg

        vars_needed = ["binary_outcome", "x1", "x2"]
        df = pd.read_csv("data.csv").dropna(subset=vars_needed)
        res = pg.logistic_regression(df[["x1", "x2"]], df["binary_outcome"],
                                     remove_na=False).round(3)
        pg.print_table(res)
    """,
    "mediation": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("data.csv")
        res = pg.mediation_analysis(data=df, x="x", m="mediator", y="outcome",
                                    covar=None, n_boot=5000, seed=42).round(3)
        pg.print_table(res)
    """,
    "reliability": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("items.csv")
        items = df[["item1", "item2", "item3", "item4"]]
        alpha, ci = pg.cronbach_alpha(data=items)
        print({"cronbach_alpha": round(alpha, 3), "ci95": ci})
    """,
    "icc": """
        import pandas as pd
        import pingouin as pg

        df = pd.read_csv("ratings_long.csv")
        res = pg.intraclass_corr(data=df, targets="target",
                                 raters="rater", ratings="rating").round(3)
        pg.print_table(res)
    """,
    "power": """
        import pingouin as pg

        n = pg.power_ttest(d=0.5, n=None, power=0.80,
                           alpha=0.05, contrast="two-samples")
        print({"required_n_per_group": n})
    """,
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(TEMPLATES))
    args = parser.parse_args()
    print(textwrap.dedent(TEMPLATES[args.kind]).strip())


if __name__ == "__main__":
    main()
