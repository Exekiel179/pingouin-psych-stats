# Exposure and Progressive Disclosure Policy

This document describes what an agent may surface by default and what it should load only when needed.

## Surface Tiers

### Tier 0: Discovery metadata (always exposed)

- `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` manifest metadata.
- `SKILL.md` frontmatter (`name`, `description`) for skill matching.
- `agents/openai.yaml` display names, short descriptions, and default prompts.
- Command frontmatter under `commands/`.

Keep Tier 0 concise. Do not place statistical procedures, long examples, or safety essays in descriptions.

### Tier 1: Selected entry instructions (trigger-gated)

Load only the `SKILL.md` for the selected entry or specialist skill. Entry skills must provide routing and stop conditions, not duplicate the full API reference.

### Tier 2: Conditional references (on demand)

Load references only for the current task:

- Intake or ambiguous request: `intake-checklist.md`, `workflow-index.md`.
- Archive or reproducibility request: `archive-contract.md` and `scripts/init_analysis_run.py`.
- Sequential run request: `workflow-contract.md`.
- Pingouin code optimization or API review: `pingouin-optimization.md`.
- Assumption/approval question: `supervision-gates.md`.
- Concrete code generation: `pingouin-api-quickref.md`.
- APA prose or tables: `apa-output-template.md`.
- Plugin architecture or routing question: this file and `MODE_REGISTRY.md`.

### Tier 3: Execution-only resources (do not narrate by default)

- `scripts/` are deterministic helpers and quality checks.
- `assets/` are reusable output assets.
- `benchmark/` prompts, fixtures, and scores are evaluation material, not evidence for a user's data.

## Non-Disclosure Rules

- Do not dump all skills, references, or benchmark prompts into an ordinary analysis response.
- Do not expose internal test fixtures as if they were user data or published validation evidence.
- Do not claim a hidden reference was consulted unless it was actually loaded.
- If the user asks how the plugin is organized, summarize the tiers and link to this policy rather than pasting every internal file.
