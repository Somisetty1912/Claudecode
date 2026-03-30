# Claude Code Python Development Toolkit

A comprehensive, production-ready toolkit for Python, FastAPI, and full-stack development using Claude Code. This repository contains both the main `.claude/` configuration directory and the reusable `pyplugin/` plugin for installing into other projects.

**Last Updated:** 2026-03-30

---

## What This Is

This is a dual-purpose toolkit:

1. **Root `.claude/` directory** — Full toolkit ready to use with Claude Code in this repository
2. **`pyplugin/` directory** — Portable plugin you can install into any Python project via `claude plugin install`

Both contain:
- **12 specialized agents** for architecture, planning, security, testing, and code quality
- **5 commands** for generating endpoints, models, migrations, and tests
- **13 skills** providing context on Python, FastAPI, frontend, architecture, and more
- **Hooks** for automatic linting and formatting with ruff, flake8, and pre-commit

---

## Quick Start

### Using This Repository

```bash
# Clone the repository
git clone https://github.com/kaushal/claude-code-python-toolkit
cd claude-code-python-toolkit

# Open in Claude Code
# All agents and skills are immediately available
@architect
/generate-endpoint users
@security-auditor
```

### Using as a Plugin in Your Project

```bash
cd your-existing-python-project/
claude plugin install github:kaushal/claude-code-python-toolkit/pyplugin
```

This installs:
- 12 agents (`@architect`, `@security-auditor`, etc.)
- 5 commands (`/generate-endpoint`, `/generate-test`, etc.)
- 13 skills for Python, FastAPI, frontend development, and more
- Linting and formatting hooks

Then use immediately:
```bash
@architect Design our API
/generate-endpoint users POST
@security-auditor
```

---

## What You Get

### Agents (12 specialized AI workers)

Invoke with `@agent-name [context]`

| Agent | Specialization | When to Use |
|-------|---|---|
| `@architect` | System design, scalability, architecture decisions | Planning major features or refactoring |
| `@planner` | Implementation planning, breaking down tasks | Need detailed steps before coding |
| `@security-auditor` | OWASP Top 10, injection, auth, FastAPI security | Security reviews, before deployment |
| `@code-reviewer` | Comprehensive code quality, patterns, best practices | PR reviews, code quality checks |
| `@python-reviewer` | Type hints, async/await, error handling | Python-specific code issues |
| `@db-reviewer` | Schema design, N+1 queries, indexes, migrations | Database optimization |
| `@tdd-guide` | Test-driven development methodology | Writing tests first |
| `@build-error-resolver` | Build errors, TypeScript compilation | Fixing build failures |
| `@code-deduplicator` | Finding and removing duplicate code | Reducing code duplication |
| `@refactor-cleaner` | Dead code, tech debt, cleanup | Removing obsolete code |
| `@doc-updater` | Documentation generation and updates | Keeping docs in sync |
| `@docs-lookup` | Learning new libraries, finding APIs | Need examples or API docs |

**Example Usage:**
```
@architect
We're scaling from 1K to 100K users. Should we use microservices?

@security-auditor app/routes/auth.py
Find OWASP vulnerabilities in our authentication

@db-reviewer
Optimize our user queries - they're slow
```

### Commands (5 generators)

Use with `/command-name [args]`

| Command | Generates | Example |
|---------|-----------|---------|
| `/generate-endpoint <resource> [method]` | FastAPI router + Pydantic models + service layer + tests | `/generate-endpoint users POST` |
| `/generate-model <ModelName>` | SQLAlchemy model + migration + Pydantic schemas | `/generate-model Order` |
| `/generate-migration <description>` | Alembic migration with upgrade/downgrade | `/generate-migration add_user_email_index` |
| `/generate-test <module_path>` | pytest file with fixtures, happy paths, error cases | `/generate-test app/services/order.py` |
| `/review-module <file_path>` | Code review covering types, async, errors, security | `/review-module app/routers/auth.py` |

**Example Workflow:**
```
# Create a new Order resource (5 minutes, fully tested)
/generate-model Order
/generate-migration create_orders_table
/generate-endpoint order POST
/generate-test app/routers/orders.py
@security-auditor app/routers/orders.py
```

### Skills (13 knowledge bases)

Auto-activated context that appears when relevant keywords are detected.

| Skill | Keyword Triggers | Provides |
|-------|---|---|
| **python-best-practices** | `.py`, `import`, `def`, `class` | Type hints, async rules, error handling |
| **fastapi-patterns** | `APIRouter`, `Depends`, `FastAPI`, `endpoint` | Route patterns, dependency injection, middleware |
| **sqlalchemy-patterns** | `Base`, `Column`, `relationship`, `Session` | ORM patterns, query optimization, migrations |
| **architecture** | `design`, `pattern`, `scalability`, `refactor` | Architecture patterns, trade-off analysis |
| **auth-implementation-patterns** | `auth`, `JWT`, `OAuth`, `permission` | Authentication/authorization playbooks |
| **bug-hunter** | `bug`, `debug`, `error`, `fail`, `exception` | Systematic debugging methodology |
| **backend-patterns** | `backend`, `api`, `service`, `middleware` | Backend architecture and patterns |
| **frontend-patterns** | `React`, `Vue`, `component`, `state` | Component patterns, state management |
| **frontend-dev-guidelines** | `frontend`, `UI`, `component`, `styling` | Component development, styling, performance |
| **frontend-design** | `design`, `UI/UX`, `accessibility`, `responsive` | Design systems, accessibility, responsive design |
| **frontend-developer** | `frontend`, `TypeScript`, `JavaScript` | Frontend best practices |
| **mcp-server-patterns** | `MCP`, `server`, `protocol` | Model Context Protocol implementations |
| **fastapi-patterns** | `FastAPI`, `router`, `endpoint` | FastAPI-specific patterns |

---

## Directory Structure

### Root `.claude/` Directory

```
.claude/
├── settings.json                    ← Permissions, hooks, environment
├── agents/                          ← 12 markdown-based agent definitions
│   ├── architect.md
│   ├── planner.md
│   ├── security-auditor.md
│   ├── code-reviewer.md
│   ├── python-reviewer.md
│   ├── db-reviewer.md
│   ├── tdd-guide.md
│   ├── build-error-resolver.md
│   ├── code-deduplicator.md
│   ├── refactor-cleaner.md
│   ├── doc-updater.md
│   └── docs-lookup.md
├── commands/                        ← 5 command definitions
│   ├── generate-endpoint.md
│   ├── generate-model.md
│   ├── generate-migration.md
│   ├── generate-test.md
│   └── review-module.md
├── skills/                          ← 13 contextual knowledge bases
│   ├── python-best-practices/
│   ├── fastapi-patterns/
│   ├── sqlalchemy-patterns/
│   ├── architecture/
│   ├── auth-implementation-patterns/
│   ├── bug-hunter/
│   ├── backend-patterns/
│   ├── frontend-patterns/
│   ├── frontend-dev-guidelines/
│   ├── frontend-design/
│   ├── frontend-developer/
│   ├── mcp-server-patterns/
│   └── ...
└── hooks/                           ← Auto-formatting and linting
    ├── post-write-lint.sh
    └── pre-commit-check.sh
```

### `pyplugin/` Directory (Portable)

```
pyplugin/
├── README.md                        ← Plugin documentation (53KB)
├── INDEX.md                         ← Documentation index
├── QUICK_REFERENCE.md               ← Fast lookup guide
├── GETTING_STARTED.md               ← Step-by-step tutorial
├── .claude-plugin/
│   └── plugin.json                  ← Installation manifest
├── agents/                          ← Same 12 agents as root
├── commands/                        ← Same 5 commands as root
├── skills/                          ← Same 13 skills as root
└── hooks/                           ← Same linting/formatting hooks
```

---

## Installation

### Option 1: Use This Repository Directly

```bash
git clone https://github.com/kaushal/claude-code-python-toolkit my-project
cd my-project
# Start using immediately with Claude Code
```

### Option 2: Install as Plugin (Recommended for Existing Projects)

```bash
cd your-existing-python-project/
claude plugin install github:kaushal/claude-code-python-toolkit/pyplugin
```

The plugin installer will:
- Copy all agents, commands, and skills
- Merge hooks into your `.claude/settings.json`
- Preserve your existing configuration

### Option 3: Manual Installation

```bash
# Copy the pyplugin directory to your project
cp -r pyplugin/ your-project/.claude/plugins/

# Or create a symlink
ln -s /path/to/claude-code-python-toolkit/pyplugin your-project/.claude/plugins/pyplugin
```

---

## Configuration

### Permissions (in `.claude/settings.json`)

Pre-authorized tools:
- `black`, `isort`, `flake8`, `pytest`, `alembic` — Code quality and testing
- `ruff format` and `ruff check` — Fast Python linting and formatting

Blocked operations:
- `rm -rf` — Prevents accidental destructive commands

### Hooks

Automatically triggered after code edits:

1. **ruff format** — Auto-formats Python code
2. **ruff check --fix** — Auto-fixes linting issues
3. **flake8** — Linting warnings (non-blocking)
4. **best-practices check** — Detects common mistakes
5. **pre-commit** — Full pre-commit hook suite

All hooks are optional and non-blocking unless explicitly configured.

---

## Usage Examples

### Example 1: Build a Complete API Endpoint (15 minutes)

```bash
# Design the API
@architect
We need a user management API. Scale requirements: 10K concurrent users.

# Generate the data model
/generate-model User

# Create the database migration
/generate-migration create_users_table

# Generate the REST endpoint
/generate-endpoint user POST

# Generate comprehensive tests
/generate-test app/routers/user.py

# Security audit before deployment
@security-auditor app/routers/user.py

# Result: Production-ready endpoint with tests and documentation
```

### Example 2: Optimize Database Performance

```bash
# Let DB reviewer analyze your queries
@db-reviewer app/models/

# Review findings and implement recommendations
/generate-migration add_user_email_index

# Verify security implications
@security-auditor
```

### Example 3: Refactor Existing Code

```bash
# Find duplicate code
@code-deduplicator

# Get refactoring plan
@planner
Consolidate our 3 user service implementations into one

# Remove dead code
@refactor-cleaner app/services/

# Comprehensive review
@code-reviewer app/services/
```

### Example 4: Plan and Implement a Feature

```bash
# Create detailed implementation plan
@planner
Add OAuth2 Google login to our API

# Review architecture
@architect
Does OAuth2 change our service architecture?

# Generate auth implementation
/generate-endpoint auth/google POST

# Implement with guidance
@security-auditor
Check our OAuth2 implementation for vulnerabilities

# Test thoroughly
/generate-test app/routers/auth/google.py
```

---

## Documentation

This repository includes comprehensive documentation:

- **`pyplugin/README.md`** — Complete reference (53KB)
  - Full agent descriptions with examples
  - All commands with use cases
  - Skill activation rules
  - Hook system details
  - Contributing guidelines

- **`pyplugin/QUICK_REFERENCE.md`** — Fast lookup guide
  - TL;DR for each agent
  - Command cheat sheet
  - Common workflows
  - Troubleshooting

- **`pyplugin/GETTING_STARTED.md`** — Step-by-step tutorial
  - 5-minute installation
  - Your first 10 minutes
  - Common tasks with examples
  - Best practices
  - File naming conventions

- **`pyplugin/INDEX.md`** — Documentation navigation
  - Which document to read for different needs
  - Learning paths for different skill levels

---

## Project Structure & Recent Changes

### Recent Additions (as of 2026-03-30)

1. **Expanded Agent Suite**
   - Added `@code-deduplicator` for removing duplicate code
   - Added `@refactor-cleaner` for dead code removal
   - Added `@doc-updater` for keeping documentation in sync
   - Added `@docs-lookup` for learning new libraries

2. **Enhanced Skills**
   - Added `architecture/` skill with pattern library
   - Added `auth-implementation-patterns/` with playbooks
   - Added `bug-hunter/` for systematic debugging
   - Added `backend-patterns/` for service architecture
   - Added `frontend-*` skills for full-stack work
   - Added `mcp-server-patterns/` for MCP implementations

3. **Improved Documentation**
   - Added `pyplugin/README.md` (53KB comprehensive guide)
   - Added `pyplugin/QUICK_REFERENCE.md` (fast lookup)
   - Added `pyplugin/GETTING_STARTED.md` (tutorial)
   - Added `pyplugin/INDEX.md` (navigation guide)

4. **Hook System Improvements**
   - Switched from black/isort to ruff for faster formatting
   - Added ruff check --fix for auto-fixing
   - Added best-practices checker for async/await issues
   - Added pre-commit integration

### Git History
- **a4211ef** — Skills (latest commit)
- **803db7a** — All skills
- **7fb4fdf** — MD files for agents
- **33eade1** — Plugin structure
- **ccdba27-0cd9e42** — Plugin development

---

## Requirements

### Python Tools (Optional but Recommended)

```bash
pip install ruff flake8 mypy pytest pytest-asyncio httpx alembic
```

- **ruff** — Fast Python linter and formatter
- **flake8** — Code style checking
- **mypy** — Static type checking
- **pytest** — Testing framework
- **alembic** — Database migrations
- **httpx** — HTTP client for testing

### Pre-commit (Optional but Recommended)

```bash
pip install pre-commit
pre-commit install
```

All hooks emit warnings if tools are missing — they never hard-fail. The plugin works fine without these tools; they just enhance the development experience.

---

## Plugin Manifest

The `pyplugin/.claude-plugin/plugin.json` file controls installation:

```json
{
  "install": {
    "copy": [
      { "from": "agents/", "to": ".claude/agents/" },
      { "from": "commands/", "to": ".claude/commands/" },
      { "from": "skills/", "to": ".claude/skills/" },
      { "from": "hooks/", "to": ".claude/hooks/" }
    ]
  }
}
```

When you run `claude plugin install github:kaushal/claude-code-python-toolkit/pyplugin`, this manifest controls what gets copied.

---

## Workflow Examples

### Daily Development

```
Morning: @architect to design features
Afternoon: /generate-endpoint, /generate-test for implementation
Evening: @code-reviewer and @security-auditor before PR
```

### Before Deployment

```
@security-auditor [your-app/]
@db-reviewer [your-app/models/]
@code-reviewer [your-app/]
# Fix issues, run tests, deploy
```

### Code Cleanup Sprint

```
@code-deduplicator
@refactor-cleaner
@code-reviewer
# Apply recommendations incrementally
```

---

## Troubleshooting

### Agents Not Appearing

- Check that `.claude/agents/` contains agent markdown files
- Restart Claude Code
- Verify `settings.json` doesn't have conflicting agent definitions

### Hooks Not Running

- Verify hooks are enabled in `settings.json`
- Check that Python files have `.py` extension
- Review `/home/kaushal/Plugins/logs/hook_trigger.log` for errors

### Commands Not Working

- Ensure you're using `/command-name` (slash prefix)
- Check that `command-name.md` exists in `.claude/commands/`
- Verify file path arguments are correct

### Plugin Installation Failed

```bash
# Check plugin directory exists
ls -la pyplugin/.claude-plugin/

# Verify plugin.json is valid
cat pyplugin/.claude-plugin/plugin.json

# Try manual installation
cp -r pyplugin/* your-project/.claude/
```

---

## Contributing

Contributions are welcome! Areas for improvement:

- Additional skills for other frameworks (Django, FastAPI-specific patterns)
- New agents for specific domains
- Enhanced documentation and examples
- Hook optimizations
- Bug reports and feature requests

---

## License

This toolkit is provided as-is for use with Claude Code and Anthropic's Claude models.

---

## Support

For issues, questions, or feature requests:
- Review documentation in `pyplugin/` directory
- Check troubleshooting section above
- Consult `pyplugin/QUICK_REFERENCE.md` for quick answers

---

**Last Updated:** 2026-03-30 | **Version:** 1.1.0 | **Status:** Stable
