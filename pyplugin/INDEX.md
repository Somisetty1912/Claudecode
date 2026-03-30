# PyPlugin Documentation Index

Welcome to PyPlugin! This document helps you find what you need.

---

## 📋 Documentation Files

### **README.md** — Complete Reference Guide
**Read this for:** Full documentation of everything in the plugin

**Contains:**
- Complete agent documentation (12 agents)
- Complete command documentation (5 commands)
- Complete skill documentation (11 skills)
- Hook system and trigger conditions
- Usage examples and workflows
- Plugin architecture
- Contributing guidelines

**Start here if:** You want comprehensive understanding of the plugin

**Sections:**
- [Quick Start](README.md#quick-start)
- [Agents](README.md#agents)
- [Commands / Skills](README.md#commands--skills)
- [Hooks](README.md#hooks)
- [Usage Examples](README.md#usage-examples)

---

### **QUICK_REFERENCE.md** — Fast Lookup Guide
**Read this for:** Quick answers, copy-paste snippets, common tasks

**Contains:**
- TL;DR for fastest operations
- Agent reference table
- Command reference table
- Skill reference table
- Hook triggers at a glance
- Common workflows
- Setup checklist
- Troubleshooting

**Start here if:** You need quick answers or copy-paste commands

**Perfect for:**
- Quick command lookup: [Agent Reference](QUICK_REFERENCE.md#agent-reference)
- Common workflows: [Common Workflows](QUICK_REFERENCE.md#common-workflows)
- Copy-paste snippets: [Quick Copy-Paste Snippets](QUICK_REFERENCE.md#quick-copy-paste-snippets)

---

### **GETTING_STARTED.md** — Step-by-Step Tutorial
**Read this for:** Learning how to use the plugin practically

**Contains:**
- Your first 10 minutes with examples
- Common tasks with step-by-step guides
- Project setup examples
- Terminal integration
- Agent communication patterns
- File naming conventions
- Troubleshooting common issues
- Best practices
- Next steps

**Start here if:** You're new to the plugin or want hands-on examples

**Perfect for:**
- First project: [Your First 10 Minutes](GETTING_STARTED.md#your-first-10-minutes)
- Common tasks: [Common Tasks](GETTING_STARTED.md#common-tasks)

---

## 🚀 Quick Start Paths

### Path 1: I Just Want to Use It (5 minutes)

1. Read: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. Try: [Your First 10 Minutes](GETTING_STARTED.md#your-first-10-minutes)
3. Generate: `/generate-endpoint users`

**Result:** Working API endpoint!

---

### Path 2: I Want to Understand Everything (30 minutes)

1. Read: [README.md - Quick Start](README.md#quick-start)
2. Scan: [Agent Overview](README.md#agents)
3. Scan: [Command Overview](README.md#commands--skills)
4. Learn: [GETTING_STARTED.md](GETTING_STARTED.md)

**Result:** Complete understanding of the plugin

---

### Path 3: I Have a Specific Task (varies)

**Building an API from scratch:**
- [GETTING_STARTED.md - Your First 10 Minutes](GETTING_STARTED.md#your-first-10-minutes)
- [QUICK_REFERENCE.md - Build CRUD API Fast](QUICK_REFERENCE.md#build-crud-api-fast)

**Adding authentication:**
- [GETTING_STARTED.md - Task 1: Add Authentication](GETTING_STARTED.md#task-1-add-authentication)
- [README.md - auth-implementation-patterns](README.md#6-auth-implementation-patterns--authentication--authorization)

**Reviewing code before deployment:**
- [QUICK_REFERENCE.md - Production Deployment Checklist](QUICK_REFERENCE.md#production-deployment-checklist)
- [README.md - security-auditor](README.md#11-security-auditor--security-vulnerability-auditing)

**Fixing a bug:**
- [GETTING_STARTED.md - Task 3: Fix Performance Issue](GETTING_STARTED.md#task-3-fix-performance-issue)
- [README.md - bug-hunter](README.md#11-security-auditor--security-vulnerability-auditing)

**Cleaning up code:**
- [QUICK_REFERENCE.md - Code Cleanup & Refactor](QUICK_REFERENCE.md#code-cleanup--refactor)
- [README.md - refactor-cleaner](README.md#10-refactor-cleaner--dead-code--dependency-cleanup)

---

## 📚 Agent Guide

### Which Agent Should I Use?

| Need | Agent | Time | Docs |
|------|-------|------|------|
| Architecture design | `@architect` | 10-20 min | [README → architect](README.md#1-architect--system-design-specialist) |
| Plan feature | `@planner` | 10 min | [README → planner](README.md#8-planner--feature--refactoring-planning) |
| Security check | `@security-auditor` | 5 min | [README → security-auditor](README.md#11-security-auditor--security-vulnerability-auditing) |
| Code review | `@code-reviewer` | 10 min | [README → code-reviewer](README.md#4-code-reviewer--comprehensive-code-review) |
| Python review | `@python-reviewer` | 5 min | [README → python-reviewer](README.md#9-python-reviewer--python-code-review) |
| Database review | `@db-reviewer` | 10 min | [README → db-reviewer](README.md#5-db-reviewer--database-design--query-review) |
| Find bugs | `@bug-hunter` | 10 min | [README → bug-hunter](README.md#8-planner--feature--refactoring-planning) |
| Test strategy | `@tdd-guide` | 15 min | [README → tdd-guide](README.md#12-tdd-guide--test-driven-development-guide) |
| Learn library | `@docs-lookup` | 5 min | [README → docs-lookup](README.md#7-docs-lookup--documentation--api-reference) |
| Update docs | `@doc-updater` | 5 min | [README → doc-updater](README.md#6-doc-updater--documentation--codemap-generator) |
| Fix build error | `@build-error-resolver` | 2 min | [README → build-error-resolver](README.md#2-build-error-resolver--typescript--build-error-fixer) |
| Remove duplicates | `@code-deduplicator` | 10 min | [README → code-deduplicator](README.md#3-code-deduplicator--code-cleanup--consolidation) |

---

## 🛠️ Command Guide

### Which Command Should I Use?

| Need | Command | Time | Docs |
|------|---------|------|------|
| Create database model | `/generate-model User` | 1 min | [README → generate-model](README.md#3-generate-model--sqlalchemy-model--migration--schemas) |
| Create migration | `/generate-migration` | 1 min | [README → generate-migration](README.md#2-generate-migration--alembic-migration-generator) |
| Create API endpoints | `/generate-endpoint users` | 2 min | [README → generate-endpoint](README.md#4-generate-endpoint--complete-router--service--tests) |
| Create tests | `/generate-test path/to/file.py` | 2 min | [README → generate-test](README.md#1-generate-test--pytest-test-file-generator) |
| Review code | `/review-module path/to/file.py` | 5 min | [README → review-module](README.md#5-review-module--comprehensive-code-review) |

---

## 🎯 Skill Guide

### Skills (Auto-Activate Based on Context)

| Skill | When It Activates | Docs |
|-------|---|------|
| python-best-practices | .py files, Python code | [README](README.md#1-python-best-practices--python-coding-standards) |
| fastapi-patterns | FastAPI routes, routers | [README](README.md#2-fastapi-patterns--fastapi-architecture) |
| sqlalchemy-patterns | SQLAlchemy models | [README](README.md#3-sqlalchemy-patterns--sqlalchemy-2x-async-orm) |
| architecture | System design questions | [README](README.md#4-architecture--system-design--patterns) |
| backend-patterns | Python backends | [README](README.md#5-backend-patterns--python-backend-architecture) |
| auth-implementation | Auth systems | [README](README.md#6-auth-implementation-patterns--authentication--authorization) |
| frontend-dev-guidelines | React components | [README](README.md#7-frontend-dev-guidelines--senior-frontend-standards) |
| frontend-patterns | React/Next.js | [README](README.md#8-frontend-patterns--react--nextjs-patterns) |
| bug-hunter | Debugging | [README](README.md#11-bug-hunter--debugging-specialist) |
| mcp-server-patterns | MCP servers | [README](README.md#10-mcp-server-patterns--mcp-server-development) |

---

## 🔧 Hook Guide

### What Hooks Do

| Hook | When | What | Docs |
|------|------|------|------|
| pre-commit-check | Before git commit | Runs flake8 + mypy | [README → pre-commit-check](README.md#1-pre-commit-check--pre-commit-linting--type-checking) |
| post-write-lint | After Write/Edit | Auto-formats code | [README → post-write-lint](README.md#2-post-write-lint--auto-lint-after-file-writes) |

**Manual runs:**
```bash
# Check code before commit
bash pyplugin/hooks/pre-commit-check.sh app/

# Check specific file
bash pyplugin/hooks/pre-commit-check.sh app/services/user.py
```

**Setup:**
- [GETTING_STARTED.md - Terminal Integration](GETTING_STARTED.md#terminal-integration)
- [README.md - Setting Up Hooks](README.md#setting-up-hooks)

---

## 📖 Learning Paths

### Path 1: FastAPI REST API Expert (1-2 hours)

1. **Learn the basics** (15 min)
   - [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
   - [GETTING_STARTED.md - Your First 10 Minutes](GETTING_STARTED.md#your-first-10-minutes)

2. **Generate your first API** (15 min)
   - `/generate-model User`
   - `/generate-endpoint users`
   - `/generate-test app/routers/users.py`

3. **Learn patterns** (30 min)
   - [README → fastapi-patterns](README.md#2-fastapi-patterns--fastapi-architecture)
   - [README → backend-patterns](README.md#5-backend-patterns--python-backend-architecture)

4. **Build complex features** (30 min)
   - Use `@architect` for design
   - Use `@planner` for planning
   - Use `/generate-*` for code
   - Use `@code-reviewer` for feedback

---

### Path 2: Secure API Developer (1 hour)

1. **Learn security** (15 min)
   - [README → security-auditor](README.md#11-security-auditor--security-vulnerability-auditing)
   - [README → auth-implementation-patterns](README.md#6-auth-implementation-patterns--authentication--authorization)

2. **Generate secure code** (20 min)
   - `/generate-model User`
   - `/generate-endpoint auth`
   - `@security-auditor app/routers/auth.py`

3. **Review before deploy** (20 min)
   - [QUICK_REFERENCE.md - Production Deployment Checklist](QUICK_REFERENCE.md#production-deployment-checklist)
   - Run all checks

4. **Deploy** (5 min)
   - `git commit && git push`

---

### Path 3: Code Quality Master (2 hours)

1. **Learn tools** (30 min)
   - [README → code-reviewer](README.md#4-code-reviewer--comprehensive-code-review)
   - [README → python-reviewer](README.md#9-python-reviewer--python-code-review)
   - [README → db-reviewer](README.md#5-db-reviewer--database-design--query-review)

2. **Review existing code** (30 min)
   - `@code-reviewer app/`
   - `@python-reviewer app/`
   - `@db-reviewer app/models/`

3. **Fix issues** (30 min)
   - Address feedback
   - Use `/generate-test` for missing tests
   - Use `@code-deduplicator` for cleanup

4. **Verify** (15 min)
   - `@code-reviewer app/` again
   - `bash pyplugin/hooks/pre-commit-check.sh app/`

---

## 🗂️ File Structure Reference

```
pyplugin/
├── README.md                    ← Complete reference
├── QUICK_REFERENCE.md          ← Fast lookup
├── GETTING_STARTED.md          ← Step-by-step tutorial
├── INDEX.md                    ← You are here
│
├── .claude-plugin/
│   └── plugin.json             ← Plugin metadata
│
├── agents/                      ← AI workers (12 files)
│   ├── architect.md
│   ├── build-error-resolver.md
│   ├── code-deduplicator.md
│   ├── code-reviewer.md
│   ├── db-reviewer.md
│   ├── doc-updater.md
│   ├── docs-lookup.md
│   ├── planner.md
│   ├── python-reviewer.md
│   ├── refactor-cleaner.md
│   ├── security-auditor.md
│   └── tdd-guide.md
│
├── commands/                    ← Code generators (5 files)
│   ├── generate-test.md
│   ├── generate-migration.md
│   ├── generate-model.md
│   ├── generate-endpoint.md
│   └── review-module.md
│
├── hooks/                       ← Event triggers (4 files)
│   ├── pre-commit-check.sh
│   ├── pre-commit-check.yaml
│   ├── post-write-lint.sh
│   └── post-write-lint.yaml
│
└── skills/                      ← Pattern guides (13 folders)
    ├── architecture/            ← System design
    ├── auth-implementation-patterns/  ← Auth patterns
    ├── backend-patterns/        ← Python backends
    ├── bug-hunter/              ← Debugging
    ├── fastapi-patterns/        ← FastAPI
    ├── frontend-design/         ← UI design
    ├── frontend-developer/      ← React
    ├── frontend-dev-guidelines/ ← Frontend standards
    ├── frontend-patterns/       ← React patterns
    ├── frontend-slides/         ← Presentations
    ├── mcp-server-patterns/     ← MCP servers
    ├── python-best-practices/   ← Python standards
    └── sqlalchemy-patterns/     ← SQLAlchemy
```

---

## ❓ FAQ

### "Where do I start?"
1. Read [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (5 minutes)
2. Follow [GETTING_STARTED.md - Your First 10 Minutes](GETTING_STARTED.md#your-first-10-minutes)
3. Try `/generate-endpoint users`

### "How do I generate a complete API?"
1. `/generate-model User`
2. `/generate-endpoint users`
3. `/generate-test app/routers/users.py`

**Total time: 5 minutes** ✓

### "How do I use agents?"
- Syntax: `@agent-name [context]`
- Example: `@architect We need microservices for 100K users`
- See [QUICK_REFERENCE.md - Agent Reference](QUICK_REFERENCE.md#agent-reference)

### "How do I use commands?"
- Syntax: `/command-name arguments`
- Example: `/generate-endpoint users`
- See [QUICK_REFERENCE.md - Command Reference](QUICK_REFERENCE.md#command-reference)

### "How do I enable hooks?"
1. Make scripts executable: `chmod +x pyplugin/hooks/*.sh`
2. Add to settings.json: `"hooks": {"enabled": true, "directory": "pyplugin/hooks"}`
3. See [GETTING_STARTED.md - Terminal Integration](GETTING_STARTED.md#terminal-integration)

### "What model does each agent use?"
See [QUICK_REFERENCE.md - Models Used](QUICK_REFERENCE.md#models-used)

### "I found a bug, what do I do?"
1. Check [GETTING_STARTED.md - Common Issues & Solutions](GETTING_STARTED.md#common-issues--solutions)
2. Check [README.md - Troubleshooting](README.md#troubleshooting)
3. Report via `https://github.com/anthropics/claude-code/issues`

---

## 🎓 Documentation Hierarchy

```
You are here → INDEX.md (this file)
         ↓
         ├─→ QUICK_REFERENCE.md ← Start if you need answers NOW
         ├─→ GETTING_STARTED.md ← Start if you're learning
         └─→ README.md ← Start if you want EVERYTHING
```

---

## 🔗 Quick Navigation

### Common Tasks
- [Build CRUD API](QUICK_REFERENCE.md#build-crud-api-fast)
- [Add authentication](GETTING_STARTED.md#task-1-add-authentication)
- [Deploy safely](QUICK_REFERENCE.md#production-deployment-checklist)
- [Review code](QUICK_REFERENCE.md#review-pr-before-merge)
- [Find bugs](README.md#bug-hunter)

### Common Commands
- [/generate-endpoint](README.md#4-generate-endpoint--complete-router--service--tests)
- [/generate-test](README.md#1-generate-test--pytest-test-file-generator)
- [/generate-model](README.md#3-generate-model--sqlalchemy-model--migration--schemas)
- [/generate-migration](README.md#2-generate-migration--alembic-migration-generator)
- [/review-module](README.md#5-review-module--comprehensive-code-review)

### Common Agents
- [@architect](README.md#1-architect--system-design-specialist)
- [@security-auditor](README.md#11-security-auditor--security-vulnerability-auditing)
- [@code-reviewer](README.md#4-code-reviewer--comprehensive-code-review)
- [@python-reviewer](README.md#9-python-reviewer--python-code-review)
- [@planner](README.md#8-planner--feature--refactoring-planning)

---

## 💡 Pro Tips

1. **Start with `/generate-endpoint`** — Fastest way to get working code
2. **Always run `@security-auditor`** before deploying
3. **Use `@architect`** for big decisions
4. **Run `bash pyplugin/hooks/pre-commit-check.sh app/`** before committing
5. **Read QUICK_REFERENCE.md** if you get stuck

---

## 📞 Support

- **Plugin Help:** Use `/help` command in Claude Code
- **Report Issues:** https://github.com/anthropics/claude-code/issues
- **Questions:** Check [README.md - FAQ](README.md#faq)

---

**Last Updated:** 2026-03-30
**Version:** 1.1.0

**Happy coding! 🚀**
