# Getting Started with PyPlugin

A step-by-step guide to use the pyplugin in your Python project.

---

## Your First 10 Minutes

### Minute 1-2: Generate a Database Model

```bash
/generate-model User
```

**What happens:**
- Creates `app/models/user.py` with SQLAlchemy model
- Generates Pydantic schemas (UserCreate, UserResponse)
- Creates Alembic migration file

**Output:**
```
✓ Generated app/models/user.py
✓ Generated app/schemas/user.py
✓ Generated alembic/versions/xxx_create_users_table.py

Model includes: id, email, created_at, updated_at
Schemas: UserCreate, UserUpdate, UserResponse
```

### Minute 3-4: Generate API Endpoints

```bash
/generate-endpoint users
```

**What happens:**
- Creates FastAPI router with CRUD operations
- Generates service layer with business logic
- Includes error handling and validation

**Output:**
```
✓ Generated app/routers/users.py
✓ Generated app/services/user_service.py

Endpoints:
  POST   /users              → create_user
  GET    /users/{id}         → get_user
  PUT    /users/{id}         → update_user
  DELETE /users/{id}         → delete_user
```

### Minute 5-8: Generate Tests

```bash
/generate-test app/routers/users.py
```

**What happens:**
- Creates comprehensive pytest file
- Includes fixtures (db_session, client)
- Tests for happy path, edge cases, error handling

**Output:**
```
✓ Generated tests/test_users.py

Test cases:
  ✓ Happy path: 4 tests
  ✓ Edge cases: 5 tests
  ✓ Error handling: 3 tests
  Total: 12 tests

Ready to run: pytest tests/test_users.py
```

### Minute 9-10: Security & Code Review

```bash
@security-auditor app/routers/users.py
```

**What happens:**
- Scans for security vulnerabilities
- Checks for hardcoded secrets
- Validates authentication patterns

**Output:**
```
## Security Audit Report

✅ No critical issues
⚠️  Consider: Add rate limiting to /users endpoint
ℹ️  Info: Use bcrypt for password hashing
```

**Result:** You now have a complete, tested, secure API endpoint! 🎉

---

## Common Tasks

### Task 1: Add Authentication

**Goal:** Add JWT token authentication

**Steps:**
```bash
# 1. Design the auth system
@architect
Need JWT authentication with refresh tokens and role-based access

# 2. Generate auth service
/generate-model User

# 3. Create auth endpoints
/generate-endpoint auth

# 4. Review security
@security-auditor app/routers/auth.py

# 5. See examples
@docs-lookup
Show JWT patterns with FastAPI

# 6. Generate tests
/generate-test app/services/auth_service.py
```

**Time:** ~15 minutes

---

### Task 2: Build Admin Dashboard API

**Goal:** Create admin-only endpoints for user management

**Steps:**
```bash
# 1. Plan the structure
@planner
Build admin dashboard API with user/role management

# 2. Generate models
/generate-model Role
/generate-model Permission

# 3. Create admin endpoints
/generate-endpoint admin/users
/generate-endpoint admin/roles

# 4. Add tests
/generate-test app/routers/admin_users.py
/generate-test app/routers/admin_roles.py

# 5. Review and secure
@security-auditor app/routers/admin/
@code-reviewer app/services/

# 6. Document
@doc-updater
```

**Time:** ~20 minutes

---

### Task 3: Fix Performance Issue

**Goal:** Optimize slow database queries

**Steps:**
```bash
# 1. Analyze database
@db-reviewer app/models/

# Diagnoses:
# - N+1 queries
# - Missing indexes
# - Inefficient relationships

# 2. Review the service
@code-reviewer app/services/user_service.py

# Suggests:
# - Query optimization
# - Caching strategies
# - Index recommendations

# 3. Implement fix
# (Claude Code helps you apply suggestions)

# 4. Test changes
/generate-test app/services/user_service.py

# 5. Verify
@security-auditor
```

**Time:** ~30 minutes

---

### Task 4: Prepare for Deployment

**Goal:** Ensure code is production-ready

**Checklist:**
```bash
# 1. Security scan
@security-auditor

# 2. Code quality
@code-reviewer app/

# 3. Python standards
@python-reviewer app/services/ app/routers/

# 4. Database
@db-reviewer app/models/

# 5. Tests
/generate-test app/services/core_service.py

# 6. Documentation
@doc-updater

# 7. Clean up dead code
@refactor-cleaner

# 8. Run pre-commit checks
bash pyplugin/hooks/pre-commit-check.sh app/

# If all green → ready to deploy! 🚀
```

**Time:** ~45 minutes

---

## Project Setup Examples

### Example 1: FastAPI REST API

**Initial Setup:**
```bash
# Create project structure
mkdir app/{models,routers,schemas,services}
mkdir tests
mkdir alembic/versions

# 1. Create database models
/generate-model User
/generate-model Post

# 2. Create API endpoints
/generate-endpoint users
/generate-endpoint posts

# 3. Create tests
/generate-test app/routers/users.py
/generate-test app/routers/posts.py

# 4. Review everything
@code-reviewer app/
@security-auditor app/

# 5. Document
@doc-updater
```

**Files Created:**
- ✓ SQLAlchemy models
- ✓ Pydantic schemas
- ✓ FastAPI routers
- ✓ Service layer
- ✓ Pytest tests
- ✓ Migrations

---

### Example 2: Add to Existing Project

**Steps:**
```bash
# 1. Install plugin (see Installation above)

# 2. Review existing code
@code-reviewer app/services/

# 3. Identify issues
@python-reviewer app/

# 4. Generate missing tests
/generate-test app/services/existing_service.py

# 5. Remove duplicates
@code-deduplicator src/

# 6. Clean up
@refactor-cleaner

# 7. Update documentation
@doc-updater
```

---

## Terminal Integration

### Using with Git

**Pre-commit hook:**
```bash
# Install
cp pyplugin/hooks/pre-commit-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Now automatic on: git commit
# Runs: flake8 + mypy
```

**Before committing:**
```bash
# Manual run
bash pyplugin/hooks/pre-commit-check.sh app/

# Output:
# [pre-commit-check] flake8: passed
# [pre-commit-check] mypy: passed
# Ready to commit!
```

### Using with Testing

**Run tests for generated code:**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_users.py

# Run with coverage
pytest --cov=app tests/

# Watch mode (auto-rerun on changes)
pytest-watch
```

### Using with Database

**Apply migrations:**
```bash
# Create migration
/generate-migration add_user_roles create_table

# Apply to database
alembic upgrade head

# Rollback if needed
alembic downgrade -1
```

---

## Agent Communication Patterns

### Pattern 1: Ask → Plan → Execute

```bash
# Step 1: Ask agent to help design
@architect
Should we use REST or GraphQL?

# Agent responds with comparison, trade-offs, recommendation

# Step 2: Plan implementation
@planner
Implement GraphQL API with authentication

# Agent provides step-by-step plan

# Step 3: Execute plan
# Use /generate-* commands from the plan

# Step 4: Verify
@code-reviewer
```

---

### Pattern 2: Review → Fix → Verify

```bash
# Step 1: Get feedback
@code-reviewer app/services/

# Identifies issues: type hints, patterns, performance

# Step 2: Fix issues
# Edit files based on feedback

# Step 3: Verify fix
@python-reviewer app/services/

# Confirms issues are resolved
```

---

### Pattern 3: Plan → Generate → Test → Deploy

```bash
# Step 1: Plan
@planner
Add payment processing feature

# Step 2: Generate code
/generate-endpoint payments
/generate-model Payment

# Step 3: Test thoroughly
/generate-test app/routers/payments.py
@tdd-guide app/services/payment_service.py

# Step 4: Security check
@security-auditor app/routers/payments.py

# Step 5: Final review
@code-reviewer app/services/payment_service.py

# Step 6: Deploy
# git commit and push
```

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Claude Code | Alt+C |
| Submit message | Enter |
| New line | Shift+Enter |
| Clear chat | /clear |
| View help | /help |
| Reload plugin | Reload in VS Code/settings |

---

## File Naming Conventions

### Models
```
app/models/user.py       → class User
app/models/product.py    → class Product
```

### Routers
```
app/routers/users.py     → router = APIRouter(prefix="/users")
app/routers/auth.py      → router = APIRouter(prefix="/auth")
```

### Services
```
app/services/user_service.py      → async def create_user()
app/services/auth_service.py      → async def authenticate()
```

### Schemas
```
app/schemas/user.py      → UserCreate, UserResponse
app/schemas/product.py   → ProductCreate, ProductResponse
```

### Tests
```
tests/test_users.py      → class TestCreateUser, TestGetUser
tests/test_auth.py       → class TestLogin, TestLogout
```

---

## Common Issues & Solutions

### Issue: "Agent not responding"

**Solution:**
```bash
# Make sure you use @ syntax
@architect          # ✓ Correct
architect           # ✗ Wrong

# Provide context
@architect          # ✗ Too vague
@architect We need microservices for 10K users  # ✓ Clear
```

---

### Issue: "Command not found"

**Solution:**
```bash
# Use / for commands
/generate-test file.py          # ✓ Correct
generate-test file.py           # ✗ Wrong

# Provide arguments
/generate-model                 # ✗ Missing argument
/generate-model User            # ✓ Clear
```

---

### Issue: "Import errors after generation"

**Solution:**
```bash
# Generated files need proper imports

# Make sure you have __init__.py files
touch app/__init__.py
touch app/models/__init__.py
touch app/routers/__init__.py
touch app/services/__init__.py
touch tests/__init__.py

# Install dependencies
pip install fastapi sqlalchemy pydantic pytest httpx
```

---

### Issue: "Tests failing after generation"

**Solution:**
```bash
# Check database is set up
# Check pytest is installed
pip install pytest pytest-asyncio pytest-mock

# Run specific test
pytest tests/test_users.py -v

# Check fixtures are working
pytest --fixtures

# Run with more verbose output
pytest tests/test_users.py -vv --tb=short
```

---

## Best Practices

### ✓ Do

- **Start with `/generate-model`** when adding a new resource
- **Always review** generated code before using in production
- **Run `@security-auditor`** before deploying
- **Generate tests** alongside code
- **Update docs** with `@doc-updater` after changes
- **Use `@architect`** for major decisions
- **Enable hooks** for automatic formatting

### ✗ Don't

- Don't skip security review before deployment
- Don't rely solely on generated code without understanding it
- Don't ignore type errors from mypy
- Don't commit without running pre-commit checks
- Don't manually edit generated migration files (create new ones instead)
- Don't ignore test failures
- Don't skip code review

---

## Performance Tips

### Fast Path (5 minutes)
```bash
# Just generate code
/generate-model User
/generate-endpoint users
/generate-test app/routers/users.py
```

### Production Path (30 minutes)
```bash
# Full review and security
/generate-model User
/generate-endpoint users
/generate-test app/routers/users.py
@security-auditor app/routers/users.py
@code-reviewer app/routers/users.py
@doc-updater
```

---

## Next Steps

1. **Install plugin** (see Installation)
2. **Generate your first endpoint** (`/generate-endpoint`)
3. **Review the code** (`@code-reviewer`)
4. **Run tests** (`pytest`)
5. **Check security** (`@security-auditor`)
6. **Deploy with confidence!** 🚀

---

## Get Help

- **Quick questions:** `/help`
- **Learn about agents:** Type `@` and see suggestions
- **Learn about commands:** Type `/` and see suggestions
- **Documentation:** See `README.md` for full guide
- **Quick reference:** See `QUICK_REFERENCE.md`

---

**Happy coding! 🎉**
