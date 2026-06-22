# Strict Real-Paper Benchmark

This subset contains tasks that have both downloaded local data files and local analysis scripts.

Run a smoke test:

```powershell
powershell -ExecutionPolicy Bypass -File benchmark\scripts\run_strict_real_paper_benchmark.ps1 -Condition both -Limit 2
```

Score outputs:

```powershell
python benchmark\scripts\score_strict_real_paper_outputs.py --condition both
```

The strict prompts require the model to inspect local files and identify one concrete target analysis from the original scripts. This is stronger than the source-linked candidate benchmark, but numeric gold values still need optional human freezing if publication-grade exact scoring is required.
