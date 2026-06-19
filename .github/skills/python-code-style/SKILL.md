---
name: python-code-style
description: Expert skill for Python code style refactoring, Ruff compliance, and type-hint/readability improvements without behavior changes.
---

# Python Code Style Expert

## Purpose
Use this skill when the user asks to improve Python readability, consistency, naming, formatting, typing clarity, doc quality, or lint compliance.

This skill focuses on code quality and maintainability, not feature changes.

## When To Use
- Refactor code style without changing behavior.
- Fix Ruff findings (`ruff check`).
- Make code pass strict typing expectations when issues are style/type-hint related.
- Improve naming, function signatures, comments, and docstrings.
- Align tests and source files with the repository conventions.

## When Not To Use
- Building new product features.
- Large architecture rewrites unrelated to style.
- Performance optimization that changes algorithmic behavior unless explicitly requested.

## Repository Context
- Project root uses a flat module layout (no `src/` package structure).
- Prefer repository-local Python: `.venv/bin/python`.
- Main style tools in this repo:
	- `.venv/bin/python -m ruff check .`
	- `.venv/bin/python -m mypy .`
	- `.venv/bin/python -m pytest`

## Core Principles
1. Preserve behavior first.
2. Keep diffs small and targeted.
3. Prefer explicit, descriptive names.
4. Add types when they improve clarity and satisfy strict checks.
5. Keep comments concise and useful.
6. Respect file-local style and existing language (English/French mix is acceptable in this repo).

## Style Checklist

### Naming
- Use `snake_case` for functions, variables, and parameters.
- Avoid single-letter names except conventional short loop counters.
- Prefer domain names over generic placeholders (`items`, `customers`, `total`, etc.).

### Function Signatures
- Add type annotations to function parameters and return values.
- Prefer concrete return types where known (`list[int]`, `Iterator[Customer]`, etc.).
- Keep signatures simple and intention-revealing.

### Control Flow And Readability
- Flatten unnecessary nesting when possible.
- Prefer straightforward loops and conditionals.
- Keep functions focused on one clear responsibility.

### Comments And Docstrings
- Add docstrings for public functions/modules when useful.
- Explain intent and constraints, not obvious syntax.
- Keep wording concise and accurate.

### Imports
- Remove unused imports.
- Keep import order Ruff-compatible.
- Avoid wildcard imports.

## Workflow
1. Read the target file(s) and identify style issues.
2. Apply minimal edits preserving behavior.
3. Run focused checks on changed files first.
4. If requested, run broader checks across the repo.
5. Report what changed, what was validated, and any residual risks.

## Command Playbook
Use these commands from repository root:

```bash
.venv/bin/python -m ruff check <file.py>
.venv/bin/python -m ruff check <file.py> --fix
.venv/bin/python -m mypy <file.py>
.venv/bin/python -m pytest <target_test.py>
```

If `ruff` is not available directly in shell, always use:

```bash
.venv/bin/python -m ruff ...
```

## Output Contract
When applying this skill, provide:
1. A concise summary of style issues fixed.
2. The files touched.
3. Validation commands run and their outcomes.
4. Any remaining non-style blockers (if present).

## Guardrails
- Do not change public behavior unless user explicitly requests it.
- Do not mass-reformat unrelated files.
- Do not silence lint/type errors with broad ignores unless justified and requested.
- Prefer explicit fixes over disabling rules.
