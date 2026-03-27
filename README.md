# claude-fastapi-kit

A portable `.claude/` toolkit for Python/FastAPI projects. Drop it into any project — new or existing — and immediately get slash commands, auto-activated skills, subagents, and linting hooks.

---

## Folder Structure

```
claude-fastapi-kit/
│
├── .claude/
│   ├── settings.json                        ← permissions, hooks, env vars
│   ├── commands/
│   │   ├── generate-endpoint.md
│   │   ├── generate-model.md
│   │   ├── generate-migration.md
│   │   ├── generate-test.md
│   │   └── review-module.md
│   ├── skills/
│   │   ├── python-best-practices/SKILL.md
│   │   ├── fastapi-patterns/SKILL.md
│   │   └── sqlalchemy-patterns/SKILL.md
│   └── agents/
│       ├── security-auditor.yaml
│       ├── db-reviewer.yaml
│       └── test-coverage.yaml
│
├── hooks/
│   ├── post-write-lint.sh                   ← runs black+isort+flake8 on every .py write
│   └── pre-commit-check.sh                  ← flake8+mypy gate before commit
│
├── .claude-plugin/
│   └── plugin.json                          ← install manifest for claude plugin install
│
├── .pre-commit-config.yaml
├── marketplace.json
└── README.md
```

---

## What's Included

### Slash Commands (`.claude/commands/`)

| Command | What It Generates |
|---|---|
| `/generate-endpoint <resource> <method>` | Router + Pydantic schemas + service layer + pytest file |
| `/generate-model <ModelName>` | SQLAlchemy model + Alembic migration stub + Pydantic schemas |
| `/generate-migration <description>` | Alembic `upgrade()` + `downgrade()` migration file |
| `/generate-test <module_path>` | pytest file with fixtures, happy path, error cases |
| `/review-module <file_path>` | Code review: types, async, error handling, OWASP security |

### Auto-Activated Skills (`.claude/skills/`)

| Skill | Activates When |
|---|---|
| `python-best-practices` | Any `.py` file — type hints, async rules, import style |
| `fastapi-patterns` | `APIRouter`, `Depends`, router, endpoint keywords |
| `sqlalchemy-patterns` | model, migration, `Base`, `Column`, `relationship` keywords |

### Subagents (`.claude/agents/`)

| Agent | Invoke With | Purpose |
|---|---|---|
| `security-auditor` | `@security-auditor` | OWASP API Top 10, injection, secrets, FastAPI-specific vulns |
| `db-reviewer` | `@db-reviewer` | N+1 queries, missing indexes, unsafe Alembic migrations |
| `test-coverage` | `@test-coverage` | Coverage gap matrix + concrete test stubs |

### Hooks (`hooks/`)

| Hook | Trigger | What It Does |
|---|---|---|
| `post-write-lint.sh` | After every `Write`/`Edit` on a `.py` file | Runs `black` + `isort` (auto-fix), then `flake8` (warnings) |
| `pre-commit-check.sh` | Before git commit | Runs `flake8` + `mypy` — blocks commit on failure |

---

## Installation

### Option A: New project from template

```bash
git clone https://github.com/kaushal/claude-fastapi-kit my-new-api
cd my-new-api
```

### Option B: Add to an existing project via plugin

```bash
cd your-existing-api/
claude plugin install github:kaushal/claude-fastapi-kit
```

This copies `.claude/commands/`, `.claude/skills/`, `.claude/agents/`, `hooks/`, and `.pre-commit-config.yaml` into your project. Your existing `.claude/settings.json` is deep-merged — not overwritten.

### Set up pre-commit hooks (optional but recommended)

```bash
pip install pre-commit black isort flake8 mypy
pre-commit install
```

---

## Adding This to the Marketplace

To make this plugin available for `claude plugin install` in any repo:

1. Push to GitHub: `github.com/kaushal/claude-fastapi-kit`
2. The `marketplace.json` + `.claude-plugin/plugin.json` are automatically picked up
3. Anyone installs it with:
   ```bash
   claude plugin install github:kaushal/claude-fastapi-kit
   ```

The `plugin.json` `install.copy` block controls exactly what gets copied into the target project:
- `.claude/commands/` → commands available as `/generate-*`, `/review-*`
- `.claude/skills/` → auto-activated skill context
- `.claude/agents/` → `@agent-name` subagents
- `hooks/` → lint scripts wired via `settings.json`

---

## Daily Workflow

```
# New feature
/generate-model Order
/generate-endpoint order POST
/generate-migration add-orders-table

# Before PR
@security-auditor
@db-reviewer
@test-coverage

# Fill gaps
/generate-test app/routers/orders.py
/review-module app/services/order_service.py
```

---

## Requirements

```bash
pip install black isort flake8 mypy pytest pytest-asyncio httpx alembic
```

Hooks emit a warning (non-blocking) if a tool is missing — they never hard-fail on missing tooling.

---

## Permissions

Pre-authorized in `.claude/settings.json`:

| Allowed | Denied |
|---|---|
| `black`, `isort`, `flake8`, `pytest`, `alembic` | `rm -rf` |
