# PyPlugin Quick Reference Guide

## TL;DR - Common Commands

### Code Generation (Fastest Way)

```bash
# Generate CRUD API in seconds
/generate-model User              # SQLAlchemy model
/generate-migration create_users  # Database migration
/generate-endpoint users          # FastAPI routes
/generate-test app/routers/users.py  # Tests

# Results: Complete API ready to use!
```

---

## Agent Reference

| Agent | Use When | Command |
|-------|----------|---------|
| `@architect` | Planning new features, system design | Needs 5+ minute conversation |
| `@planner` | Planning implementation steps | Need detailed plan before coding |
| `@security-auditor` | Before deployment, code review | Security concerns |
| `@code-reviewer` | PR review, code quality check | Need comprehensive feedback |
| `@python-reviewer` | Python-specific issues | Type hints, async, errors |
| `@db-reviewer` | Database schema, query optimization | SQL/ORM concerns |
| `@tdd-guide` | Test-driven development | Writing tests first |
| `@build-error-resolver` | Build/TypeScript errors | Compilation fails |
| `@code-deduplicator` | Remove duplicate code | Code cleanup |
| `@refactor-cleaner` | Dead code removal | Technical debt |
| `@doc-updater` | Update documentation | Docs out of sync |
| `@docs-lookup` | Learn new libraries | Need API docs/examples |

**How to invoke:** `@agent-name [context]`

**Example:**
```
@architect
We need real-time notifications, expected 100K users
```

---

## Command Reference

| Command | Purpose | Arguments |
|---------|---------|-----------|
| `/generate-test` | Create pytest file | `path/to/module.py` |
| `/generate-migration` | Create Alembic migration | `migration_name` |
| `/generate-model` | Create SQLAlchemy model | `ModelName` |
| `/generate-endpoint` | Create FastAPI endpoints | `resource_name` |
| `/review-module` | Code quality review | `path/to/module.py` |

**How to invoke:** `/command-name arguments`

**Example:**
```bash
/generate-test app/services/auth.py
/generate-endpoint users
/review-module app/services/
```

---

## Skill Reference

| Skill | Activates When | Use For |
|-------|---|---------|
| `python-best-practices` | Writing .py files | Type hints, async, errors |
| `fastapi-patterns` | Writing FastAPI routes | Router organization, deps |
| `sqlalchemy-patterns` | Writing models/queries | ORM patterns, migrations |
| `architecture` | Designing systems | Patterns, trade-offs |
| `backend-patterns` | Building backends | Repos, services, caching |
| `auth-implementation-patterns` | Building auth | JWT, OAuth, RBAC |
| `bug-hunter` | Debugging | Finding root causes |
| `frontend-*` | Building React apps | Components, state, hooks |

**Skills activate automatically** when you work with related code or ask related questions.

---

## Hook Triggers

### pre-commit-check

**When:** Before you commit code to git
**What:** Runs flake8 (lint) + mypy (type check)
**Stop commit if:** Type errors or style violations found
**Manual run:** `bash pyplugin/hooks/pre-commit-check.sh app/`

### post-write-lint

**When:** After you Write/Edit a file
**What:** Auto-formats and fixes code style
**Result:** File is automatically fixed, you see clean code immediately

---

## Common Workflows

### Add Feature (Complete to Deploy)

```bash
# 1. Plan it
@planner
Feature: Add user roles and permissions

# 2. Design architecture
@architect
How should we structure RBAC?

# 3. Generate code
/generate-model Role
/generate-endpoint roles
/generate-test app/routers/roles.py

# 4. Review & secure
@code-reviewer app/routers/roles.py
@security-auditor app/routers/roles.py

# 5. Update docs
@doc-updater
```

### Fix Production Bug

```bash
# 1. Understand bug
@bug-hunter
Auth token expiration doesn't work correctly

# 2. Review the code
@code-reviewer app/services/auth_service.py

# 3. Generate tests (if missing)
/generate-test app/services/auth_service.py

# 4. Security check
@security-auditor app/

# 5. Verify fix
@python-reviewer app/services/auth_service.py
```

### Code Cleanup & Refactor

```bash
# 1. Find issues
@code-reviewer app/

# 2. Remove duplicates
@code-deduplicator src/

# 3. Clean dead code
@refactor-cleaner

# 4. Final review
@python-reviewer app/

# 5. Update docs
@doc-updater
```

### Build CRUD API Fast

```bash
/generate-model Product
/generate-migration create_products
/generate-endpoint products
/generate-test app/routers/products.py

# Takes 2-3 minutes, gives you:
# ✓ Database model
# ✓ Migration
# ✓ API routes (GET, POST, PUT, DELETE)
# ✓ Services & schemas
# ✓ Complete tests
```

---

## Invoke Syntax

### Agents (AI Workers)
```bash
@agent-name [optional context]

# Examples:
@architect
@security-auditor app/routers/
@planner Add OAuth authentication
```

### Commands (Code Generation)
```bash
/command-name [arguments]

# Examples:
/generate-test app/services/user.py
/generate-endpoint products
/review-module app/
```

### Skills (Pattern Guides)
```bash
# Activate automatically when you:
# - Write .py files → python-best-practices
# - Create FastAPI route → fastapi-patterns
# - Define SQLAlchemy model → sqlalchemy-patterns

# Or ask about them:
# "Tell me about FastAPI best practices"
# → fastapi-patterns skill loads
```

---

## Output Examples

### Agent Output
```
## Architecture Recommendation

### Component Design
[Diagram and description]

### Trade-off Analysis
[Pros/cons comparison]

### Scalability Plan
[Growth strategy]

### Implementation Roadmap
[Step-by-step plan]
```

### Command Output
```
✓ Generated app/models/user.py
✓ Generated app/routers/users.py
✓ Generated app/services/user_service.py
✓ Generated app/schemas/user.py
✓ Generated tests/test_users.py
✓ Generated alembic/versions/...py

Summary:
- 5 files created
- CRUD operations: GET, POST, PUT, DELETE
- 12 test cases
- Ready to use!
```

### Skill Output
```
# Python Best Practices Guide

## Type Hints
Every function must have type annotations...

## Async Rules
Always await coroutines...

## Error Handling
Catch specific exceptions...
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent doesn't respond | Use `@agent-name` syntax, provide context |
| Command not found | Use `/command-name arguments` syntax |
| Hooks not running | Check `settings.json`, run `chmod +x pyplugin/hooks/*.sh` |
| Plugin not loading | Verify path in settings, reload Claude Code |
| Model not generating | Provide `ModelName` to `/generate-model` |
| Tests failing | Check module path exists, run `/generate-test module.py` again |

---

## Models Used

| Agent | Model | Speed | Best For |
|-------|-------|-------|----------|
| architect | Opus 4.6 | Slow | Complex design decisions |
| code-reviewer | Opus 4.6 | Slow | Deep code analysis |
| security-auditor | Sonnet 4.6 | Medium | Balanced security audit |
| db-reviewer | Sonnet 4.6 | Medium | Database optimization |
| python-reviewer | Sonnet 4.6 | Medium | Python-specific review |
| build-error-resolver | Haiku 4.5 | Fast | Quick error fixes |
| doc-updater | Haiku 4.5 | Fast | Fast doc generation |
| code-deduplicator | Haiku 4.5 | Fast | Quick cleanup |

---

## Full Documentation

See `README.md` for complete documentation including:
- Detailed agent descriptions
- Full command specifications
- Skill documentation
- Hook configuration
- Architecture details
- Contributing guide

---

## Quick Copy-Paste Snippets

### Setup Python Backend
```bash
# 1. Create model
/generate-model User

# 2. Add auth routes
/generate-endpoint auth

# 3. Generate tests
/generate-test app/routers/auth.py

# 4. Review security
@security-auditor
```

### Review PR Before Merge
```bash
@code-reviewer [changed-files]
@security-auditor [changed-files]
@python-reviewer [changed-files]
/review-module [main-service]
```

### Production Deployment Checklist
```bash
@security-auditor
@code-reviewer app/
@db-reviewer app/models/
/review-module app/services/
@doc-updater
# Then: git commit and deploy
```

---

**Pro Tip:** Start with `/generate-endpoint` to scaffold APIs, then use `@agent-name` for complex decisions.
