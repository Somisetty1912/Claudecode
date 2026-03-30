# PyPlugin: Claude Code Python Development Plugin

A comprehensive Claude Code plugin that provides specialized agents, commands, and skills for Python and full-stack development. This plugin extends Claude Code with intelligent automation for code generation, testing, architecture design, security auditing, and best practices enforcement.

**Version:** 1.1.0
**Author:** JJS
**Repository:** pyplugin

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Agents](#agents)
3. [Commands / Skills](#commands--skills)
4. [Hooks](#hooks)
5. [Usage Examples](#usage-examples)
6. [Plugin Architecture](#plugin-architecture)
7. [Contributing](#contributing)

---

## Quick Start

### For New Projects

1. **Copy the plugin** to your Claude Code plugins directory
2. **Configure hooks** (optional, see [Hooks](#hooks))
3. **Start invoking agents** using `@agent-name` syntax
4. **Use commands** with `/command-name` syntax

### Example Usage

```bash
# Use an agent to design architecture
@architect

# Generate a complete endpoint (router + service + tests)
/generate-endpoint

# Run security audit on your codebase
@security-auditor

# Generate tests for a module
/generate-test app/services/user_service.py
```

---

## Agents

Agents are autonomous AI workers that specialize in specific tasks. They can be invoked individually to handle complex, multi-step work.

### How to Invoke Agents

```bash
# In Claude Code chat
@agent-name [additional context]

# Examples:
@architect
@security-auditor [specify files or directories to audit]
@planner [describe the feature]
```

**Agent Invocation Syntax:**
- `@agent-name` — Invokes the agent with default instructions
- `@agent-name [context]` — Provides additional context or files
- Agents work best with detailed descriptions of what you need

---

### 1. **architect** — System Design Specialist

**Role:** Plans and designs system architecture for new features, scalability, and technical decisions.

**When to Use:**
- Planning a major new feature (affects multiple systems)
- Choosing between technology options (microservices vs monolith, SQL vs NoSQL)
- Refactoring large systems and assessing impact
- Addressing scalability bottlenecks
- Establishing patterns for code consistency
- Tech debt assessment and remediation

**What It Does:**
- Analyzes existing codebase architecture
- Evaluates trade-offs between design options
- Recommends patterns and best practices
- Identifies scalability bottlenecks
- Creates architecture diagrams and proposals
- Ensures consistency across your codebase

**Workflow:**
1. Understands the current landscape (reads key files, maps patterns)
2. Clarifies functional and non-functional requirements
3. Proposes design with trade-off analysis
4. Documents decisions with pros/cons/alternatives

**Output You Gain:**
- Architecture diagrams (ASCII or Mermaid)
- Component responsibility mapping
- Technology recommendations
- Scalability assessment
- Architecture Decision Records (ADRs)

**Model:** Claude Opus 4.6 (highest capability)

**Invoke With:**
```bash
@architect
# Provide context about what you're building:
# - Current architecture limitations
# - Expected scale (users, requests, data volume)
# - Technology preferences or constraints
# - Team expertise
```

**Example:**
```
@architect
We're building a real-time collaboration tool. Currently have a
monolith in Python. Need to handle 10K+ concurrent users.
Expected to scale to 100K users in 2 years.
```

---

### 2. **build-error-resolver** — TypeScript & Build Error Fixer

**Role:** Diagnoses and fixes build errors, TypeScript type errors, and compilation issues.

**When to Use:**
- Build fails with unclear error messages
- TypeScript type checking fails
- Compilation errors in any language
- Configuration errors preventing builds
- Dependency conflicts

**What It Does:**
- Identifies root causes of build failures
- Fixes type errors with minimal changes
- Resolves dependency conflicts
- Updates configurations as needed
- Provides explanations of what went wrong

**Output You Gain:**
- Fixed code with minimal diffs
- Explanation of the error and fix
- Prevention tips for similar errors

**Model:** Claude Haiku 4.5

**Invoke With:**
```bash
@build-error-resolver
# Just run your build and let it fail, then invoke the agent
```

**Example:**
```
# After build fails:
@build-error-resolver

# Agent will:
# 1. Read build logs
# 2. Identify type/config issues
# 3. Apply fixes to get build green
```

---

### 3. **code-deduplicator** — Code Cleanup & Consolidation

**Role:** Removes duplicate code, consolidates similar functions, and cleans up redundancy.

**When to Use:**
- Code duplication across modules
- Similar functions that could be merged
- Copy-paste code that should be abstracted
- Consolidating repeated patterns
- Dead code removal

**What It Does:**
- Finds duplicate code patterns
- Identifies candidates for consolidation
- Refactors duplicates into reusable functions
- Removes dead/unused code
- Improves code maintainability

**Output You Gain:**
- Consolidated, DRY codebase
- New utility/helper functions
- Removed redundant code
- Maintainability improvements

**Model:** Claude Haiku 4.5

**Invoke With:**
```bash
@code-deduplicator [file_or_directory]
```

**Example:**
```
@code-deduplicator src/

# Agent will scan src/, find duplicates, and propose consolidation
```

---

### 4. **code-reviewer** — Comprehensive Code Review

**Role:** Reviews code for quality, SOLID principles, design patterns, type safety, and performance.

**When to Use:**
- Before merging pull requests
- Reviewing critical code paths
- Assessing design pattern usage
- Checking for SOLID principle violations
- Performance concerns
- Testing adequacy

**What It Does:**
- Analyzes code structure and organization
- Checks SOLID principles compliance
- Identifies design pattern opportunities
- Assesses type safety and error handling
- Reviews test coverage
- Suggests improvements with explanations

**Output You Gain:**
- Detailed code review feedback
- Suggested improvements
- SOLID/DRY/Performance scores
- Risk assessment

**Model:** Claude Opus 4.6

**Invoke With:**
```bash
@code-reviewer [files_or_paths]
```

**Example:**
```
@code-reviewer src/services/auth_service.py

# Agent provides comprehensive review with scores and suggestions
```

---

### 5. **db-reviewer** — Database Design & Query Review

**Role:** Reviews database schema, queries, migrations, and performance.

**When to Use:**
- Designing new database schemas
- Reviewing ORM queries for N+1 issues
- Migration strategy assessment
- Index optimization
- Query performance problems
- Database architecture decisions

**What It Does:**
- Analyzes schema design
- Identifies N+1 query problems
- Suggests index strategies
- Reviews migration scripts
- Checks for data consistency issues
- Recommends query optimizations

**Output You Gain:**
- Schema improvement suggestions
- Query optimization recommendations
- Index strategy
- Performance improvements
- Migration fixes

**Model:** Claude Sonnet 4.6

**Invoke With:**
```bash
@db-reviewer [models_or_migrations]
```

**Example:**
```
@db-reviewer app/models/

# Agent reviews all models and finds optimization opportunities
```

---

### 6. **doc-updater** — Documentation & Codemap Generator

**Role:** Keeps documentation and architectural codemaps in sync with code.

**When to Use:**
- After significant code changes
- Creating architectural documentation
- Updating README and guides
- Generating codemaps of system
- Documenting new features
- Keeping docs in sync with code

**What It Does:**
- Generates architectural codemaps
- Updates README files from code
- Creates module documentation
- Generates dependency diagrams
- Extracts and documents APIs
- Maintains documentation freshness

**Output You Gain:**
- Updated README.md
- Architectural codemaps
- API documentation
- Dependency diagrams
- Module guides

**Model:** Claude Haiku 4.5

**Invoke With:**
```bash
@doc-updater
```

**Example:**
```
@doc-updater

# Agent generates:
# - docs/CODEMAPS/INDEX.md
# - docs/CODEMAPS/backend.md
# - Updated README.md
```

---

### 7. **docs-lookup** — Documentation & API Reference

**Role:** Fetches current documentation, libraries, frameworks, and provides up-to-date examples.

**When to Use:**
- Learning a new library
- Looking up API documentation
- Needing current code examples
- Checking framework features
- Understanding best practices for a tool

**What It Does:**
- Fetches current documentation
- Provides up-to-date code examples
- Explains framework features
- Shows best practices
- Compares options

**Output You Gain:**
- Current documentation
- Working code examples
- Best practice guidance
- Feature comparisons

**Model:** Claude Opus 4.6

**Invoke With:**
```bash
@docs-lookup
# Ask about a library or framework:
# How do I use FastAPI dependency injection?
# Show examples of SQLAlchemy async patterns
```

**Example:**
```
@docs-lookup
How do I use SQLAlchemy 2.x async sessions?

# Agent fetches latest SQLAlchemy docs and provides working examples
```

---

### 8. **planner** — Feature & Refactoring Planning

**Role:** Plans implementation strategies for complex features and refactoring tasks.

**When to Use:**
- Planning a new feature implementation
- Large refactoring efforts
- Complex multi-step changes
- Architectural changes
- Unclear implementation strategy

**What It Does:**
- Analyzes the codebase
- Identifies affected areas
- Plans step-by-step implementation
- Considers technical trade-offs
- Suggests file changes and new structures
- Estimates scope and dependencies

**Output You Gain:**
- Detailed implementation plan
- Step-by-step instructions
- File structure recommendations
- Risk assessment
- Timeline understanding

**Model:** Claude Opus 4.6

**Invoke With:**
```bash
@planner [feature_description]
```

**Example:**
```
@planner
Add JWT authentication to the FastAPI app.
Current state: basic token-based auth.
Need: refresh tokens, role-based access control.
```

---

### 9. **python-reviewer** — Python Code Review

**Role:** Reviews Python code for quality, type safety, async correctness, and best practices.

**When to Use:**
- Reviewing Python modules
- Checking type hints and type safety
- Async/await correctness
- Error handling patterns
- Best practices compliance
- Code quality assessment

**What It Does:**
- Analyzes Python code structure
- Checks type hints completeness
- Validates async/await usage
- Reviews error handling
- Assesses best practices compliance
- Identifies antipatterns

**Output You Gain:**
- Python-specific feedback
- Type safety recommendations
- Async pattern corrections
- Best practices suggestions
- Quality score

**Model:** Claude Sonnet 4.6

**Invoke With:**
```bash
@python-reviewer [python_files]
```

**Example:**
```
@python-reviewer app/services/

# Agent reviews all Python files in services and provides detailed feedback
```

---

### 10. **refactor-cleaner** — Dead Code & Dependency Cleanup

**Role:** Identifies and removes unused code, dead imports, and unused dependencies.

**When to Use:**
- Cleaning up after large refactors
- Removing obsolete code
- Eliminating unused dependencies
- Dead import removal
- Codebase maintenance
- Technical debt reduction

**What It Does:**
- Runs dead code analysis tools (knip, depcheck, ts-prune)
- Identifies unused imports, variables, functions
- Finds unused dependencies
- Suggests removals safely
- Refactors to remove dead code
- Cleans up configuration

**Output You Gain:**
- Cleaner codebase
- Removed dead code
- Smaller dependency tree
- Better maintainability

**Model:** Claude Haiku 4.5

**Invoke With:**
```bash
@refactor-cleaner
```

**Example:**
```
@refactor-cleaner

# Agent finds and removes:
# - Unused imports
# - Dead functions
# - Unused variables
# - Unused dependencies
```

---

### 11. **security-auditor** — Security Vulnerability Auditing

**Role:** Audits Python/FastAPI code for security vulnerabilities and OWASP Top 10 issues.

**When to Use:**
- Before deploying to production
- During code review
- After adding new authentication/authorization
- When handling sensitive data
- Regular security checkups
- Before opening source code

**What It Does:**
- Scans for hardcoded secrets and credentials
- Finds injection vulnerabilities (SQL, command, SSRF)
- Checks FastAPI-specific security issues
- Reviews deserialization safety
- Audits dependencies for known vulnerabilities
- Validates crypto usage (bcrypt, argon2, etc)

**Security Issues Checked:**
- ✓ Hardcoded API keys, tokens, passwords
- ✓ SQL injection and raw SQL queries
- ✓ Command injection via subprocess
- ✓ SSRF vulnerabilities
- ✓ Insecure deserialization (pickle, yaml)
- ✓ Missing CORS validation
- ✓ Overly permissive authentication
- ✓ Vulnerable dependencies
- ✓ Weak cryptography
- ✓ Information leakage in responses

**Output You Gain:**
- Security audit report (Critical/High/Medium/Low)
- Line-by-line vulnerability details
- Remediation guidance
- Dependency vulnerability list
- Risk assessment

**Model:** Claude Sonnet 4.6 (specialized for security)

**Invoke With:**
```bash
@security-auditor
# Or specify files/directories:
@security-auditor [files_or_dirs]
```

**Example:**
```
@security-auditor app/routers/ app/services/

# Agent scans specified directories and:
# 🔴 Reports critical security issues
# 🟠 Lists high-risk vulnerabilities
# 🟡 Suggests medium-priority fixes
# 🟢 Notes low-priority improvements
```

---

### 12. **tdd-guide** — Test-Driven Development Guide

**Role:** Guides test-driven development with test generation, testing strategies, and coverage.

**When to Use:**
- Starting a new feature with TDD
- Writing tests before implementation
- Improving test coverage
- Setting up test infrastructure
- Learning TDD patterns
- Validating test strategy

**What It Does:**
- Plans testing strategy
- Generates test cases
- Guides red-green-refactor cycle
- Reviews test coverage
- Suggests test improvements
- Validates edge cases

**Output You Gain:**
- Comprehensive test suite
- Test strategy documentation
- Coverage reports
- Edge case identification
- TDD guidance

**Model:** Claude Opus 4.6

**Invoke With:**
```bash
@tdd-guide [module_or_feature]
```

**Example:**
```
@tdd-guide app/services/payment_service.py

# Agent:
# 1. Reads the module
# 2. Plans test cases (happy path, edge cases, errors)
# 3. Generates pytest file with fixtures and tests
# 4. Validates coverage
```

---

## Commands / Skills

Commands (CLI-style) are quick operations that generate code or perform specific tasks. Skills provide interactive guidance and patterns for specific technologies.

### How to Invoke Commands

```bash
# In Claude Code chat
/command-name [arguments]

# Examples:
/generate-test app/services/user_service.py
/generate-endpoint
/generate-model
/generate-migration
/review-module app/services/
```

**Syntax:**
- `/command-name` — Runs the command with default settings
- `/command-name [args]` — Passes arguments to the command
- Commands may prompt for additional input

---

### 1. **generate-test** — Pytest Test File Generator

**What It Does:**
Generates comprehensive pytest test files for Python modules with fixtures, happy paths, and error cases.

**Arguments:**
- `module_path` — Path to the Python module to test (e.g., `app/services/user_service.py`)

**What Gets Generated:**
1. **Fixtures** — Reusable test setup (db_session, client, factories)
2. **Happy Path Tests** — Valid inputs, expected outputs
3. **Edge Case Tests** — Boundary values, empty input, None values
4. **Error Case Tests** — Invalid inputs, exceptions, validation failures
5. **Async Tests** — Marked with `@pytest.mark.asyncio` if needed
6. **FastAPI Tests** — Full route testing with AsyncClient

**Test Structure:**
```python
# Fixtures
@pytest.fixture
async def db_session():
    """SQLAlchemy async session"""

@pytest.fixture
async def client():
    """FastAPI test client"""

# Test Classes
class TestFunctionName:
    async def test_happy_path(self):
        """Test valid inputs"""

    async def test_edge_case_empty(self):
        """Test boundary conditions"""

    async def test_error_missing_field(self):
        """Test error handling"""
```

**Output You Gain:**
- Complete test file in `tests/test_*.py`
- Pytest fixtures and conftest snippets
- Happy path, edge cases, and error tests
- Async support with `pytest-asyncio`
- Coverage summary

**Terminal Usage:**
```bash
# Generate tests for a service
/generate-test app/services/user_service.py

# Generate tests for a router
/generate-test app/routers/orders.py

# Generate tests for a utility module
/generate-test app/utils/helpers.py
```

**Example Output:**
```
✓ Generated tests/test_user_service.py
  - 12 test cases created
  - Functions covered: create_user, get_user, update_user, delete_user
  - Functions skipped: _validate_email (private), __init__ (dunder)
  - Fixtures: db_session, client, make_user
  - Async tests: 8 (marked with @pytest.mark.asyncio)

Happy path tests: 4
Edge case tests: 5
Error handling tests: 3
```

**Rules:**
- All tests have type hints
- Tests use specific exception types (not bare `Exception`)
- Imports organized (stdlib → third-party → local)
- Fixtures reused, no code duplication
- External dependencies mocked, internal functions tested with real DB
- Tests grouped in classes per function

---

### 2. **generate-migration** — Alembic Migration Generator

**What It Does:**
Generates Alembic migration files for database schema changes.

**Arguments:**
- `migration_name` — Descriptive name (e.g., `add_user_roles_table`)
- `migration_type` — Type of change: `create_table`, `add_column`, `drop_column`, `add_index`, `custom`

**What Gets Generated:**
1. **Migration file** — `alembic/versions/xxxx_migration_name.py`
2. **Upgrade function** — Apply the schema change
3. **Downgrade function** — Rollback the schema change
4. **Type hints** — Proper typing for all operations

**Migration Template:**
```python
from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    """Apply schema changes"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    """Rollback schema changes"""
    op.drop_table('users')
```

**Output You Gain:**
- Ready-to-run migration file
- Valid upgrade/downgrade functions
- Proper SQLAlchemy syntax
- Can be applied with `alembic upgrade head`

**Terminal Usage:**
```bash
# Create table migration
/generate-migration add_users_table create_table

# Add column migration
/generate-migration add_role_to_users add_column

# Add index migration
/generate-migration index_users_email add_index

# Custom migration
/generate-migration rename_columns custom
```

**Example Output:**
```
✓ Generated alembic/versions/202401_add_users_table.py
  - Upgrade function: creates table 'users'
  - Downgrade function: drops table 'users'
  - Columns: id, email, created_at, updated_at
  - Ready to run: alembic upgrade head
```

---

### 3. **generate-model** — SQLAlchemy Model + Migration + Schemas

**What It Does:**
Generates a complete ORM model with Alembic migration stub and Pydantic schemas.

**Arguments:**
- `model_name` — Name of the model (e.g., `User`, `Product`)
- `fields` — Fields and types (e.g., `id:int, email:str, created_at:datetime`)

**What Gets Generated:**
1. **SQLAlchemy Model** — ORM class with columns, relationships, methods
2. **Pydantic Schemas** — CreateSchema, UpdateSchema, ResponseSchema
3. **Alembic Migration** — Database table creation
4. **Type Hints** — Full type annotations

**Model Template:**
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="author")
```

**Pydantic Schemas:**
```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
```

**Output You Gain:**
- SQLAlchemy model with relationships
- Create, Update, Response Pydantic schemas
- Migration file ready to apply
- Type hints throughout
- Validation rules in schemas

**Terminal Usage:**
```bash
# Generate User model
/generate-model User

# Generate with fields
/generate-model Product "id:int, name:str, price:float, stock:int"

# Generate with relationships
/generate-model Order "id:int, user_id:int, total:float, items:relationship"
```

**Example Output:**
```
✓ Generated app/models/user.py
✓ Generated app/schemas/user.py
✓ Generated alembic/versions/202401_create_users_table.py

Model: User
  - Columns: id, email, created_at, updated_at
  - Relationships: posts
  - Methods: get_by_email, create, update, delete

Schemas: UserCreate, UserUpdate, UserResponse
  - Validations configured
  - Example values included
```

---

### 4. **generate-endpoint** — Complete Router + Service + Tests

**What It Does:**
Generates a complete FastAPI endpoint with router, service layer, tests, and Pydantic schemas.

**Arguments:**
- `resource_name` — Resource name (e.g., `users`, `products`, `orders`)
- `methods` — HTTP methods (GET, POST, PUT, DELETE, PATCH)

**What Gets Generated:**
1. **APIRouter** — FastAPI routes with proper status codes
2. **Service Layer** — Business logic separation
3. **Pydantic Schemas** — Request/response models
4. **Tests** — Comprehensive pytest tests
5. **Database Layer** — Repository or DAL pattern

**Generated Structure:**
```
app/
├── routers/
│   └── users.py          # APIRouter with all endpoints
├── services/
│   └── user_service.py   # Business logic
├── schemas/
│   └── user.py           # Pydantic models
└── tests/
    └── test_users.py     # Full test coverage
```

**Router Template:**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    """Create a new user"""
    return await user_service.create_user(db, user_data)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    """Get user by ID"""
    user = await user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

**Output You Gain:**
- Complete CRUD endpoints
- Service layer with business logic
- Pydantic schemas with validation
- Full test coverage
- Error handling and proper status codes
- Dependency injection setup
- Documentation and examples

**Terminal Usage:**
```bash
# Generate basic CRUD for users
/generate-endpoint users

# Generate specific methods
/generate-endpoint products GET,POST,PUT,DELETE

# Generate with nested resources
/generate-endpoint orders/items
```

**Example Output:**
```
✓ Generated app/routers/users.py
✓ Generated app/services/user_service.py
✓ Generated app/schemas/user.py
✓ Generated tests/test_users.py

Endpoints created:
  POST   /users              → create_user
  GET    /users/{user_id}    → get_user
  PUT    /users/{user_id}    → update_user
  DELETE /users/{user_id}    → delete_user

Tests: 16 test cases (happy path, edge cases, errors)
Methods: GET, POST, PUT, DELETE
Status Codes: 200, 201, 400, 404, 422
```

---

### 5. **review-module** — Comprehensive Code Review

**What It Does:**
Performs in-depth code review with SOLID principles, design patterns, async correctness, type safety, and error handling analysis.

**Arguments:**
- `module_path` — Path to module to review (e.g., `app/services/auth.py`)

**Review Dimensions:**
- **SOLID Principles** — Single responsibility, Open/Closed, Liskov, Interface, Dependency
- **Design Patterns** — Observer, Factory, Singleton, Strategy, etc.
- **Type Safety** — Type hints completeness, generic types, type narrowing
- **Async Correctness** — Proper async/await, no blocking calls, concurrent patterns
- **Error Handling** — Specific exceptions, error context, recovery strategies
- **Code Quality** — DRY principle, naming, function length, complexity
- **Performance** — N+1 queries, inefficient algorithms, caching opportunities
- **Testing** — Testability, mock points, coverage strategy

**Review Output:**
```
Code Review Report: app/services/auth.py

SOLID Principles:        ████████░ 80/100
Design Patterns:         ███████░░ 70/100
Type Safety:             ██████░░░ 60/100
Async Correctness:       ████████░ 80/100
Error Handling:          ███████░░ 70/100
Code Quality:            █████░░░░ 50/100
Performance:             ███████░░ 70/100

Overall Score: 70/100

Issues Found:
  🔴 Critical: Missing type hints on 5 functions
  🟠 High: N+1 query in list_users function
  🟡 Medium: Long function (67 lines) - should split
  🟢 Low: Naming could be clearer in 2 places
```

**Output You Gain:**
- Detailed review feedback with scores
- Specific issues with line numbers
- Actionable improvement suggestions
- Architectural pattern recommendations
- Risk assessment
- Priority-based issues (Critical/High/Medium/Low)

**Terminal Usage:**
```bash
# Review a service
/review-module app/services/user_service.py

# Review a router
/review-module app/routers/auth.py

# Review entire package
/review-module app/services/
```

**Example Output:**
```
✓ Reviewed app/services/user_service.py (187 lines)

🔴 Critical Issues (1):
  L45: Type hints missing on create_user() function
       Fix: Add proper return type annotation

🟠 High Issues (2):
  L67: N+1 query in get_user_posts()
       Fix: Use relationship loading strategy or explicit join
  L102: Missing error handling for database connection
       Fix: Catch specific SQLAlchemy exceptions

🟡 Medium Issues (3):
  L34: Function too long (56 lines) - should be split
  L78: Overly broad exception catching
  L145: Missing docstring

Recommendations:
  - Use dependency injection for db session
  - Add logging for debugging
  - Extract validation logic to separate function
  - Consider pagination for list operations
```

---

## Skills

Skills provide interactive, in-depth guidance for specific technologies and patterns. They're not commands—they're learning resources and pattern libraries.

### How to Use Skills

Skills are triggered when you work with specific technologies:

```bash
# These automatically activate relevant skills:
# - Writing .py files → python-best-practices
# - Creating React components → frontend-patterns
# - Building FastAPI → fastapi-patterns
# - Using SQLAlchemy → sqlalchemy-patterns

# Or explicitly invoke:
I need help with authentication patterns
# → auth-implementation-patterns skill loads

Tell me about FastAPI best practices
# → fastapi-patterns skill loads
```

---

### 1. **python-best-practices** — Python Coding Standards

**When It Activates:**
- Writing or modifying any `.py` file
- Mentions of "type hints", "async", "error handling", "function", "class"
- Generating Python modules

**Core Rules:**

**Type Hints (Non-Negotiable)**
```python
# Bad
def process(items, config=None):
    return results

# Good
def process(items: list[str], config: Config | None = None) -> list[Result]:
    return results
```
- Every function parameter and return type must be annotated
- No `Any` — use specific types or TypeVar
- Use `X | None` instead of `Optional[X]` (Python 3.10+)
- Use `list[T]`, `dict[K, V]` instead of `List`, `Dict`

**Async Rules**
```python
# Bad
def get_user(user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

# Good
async def get_user(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```
- Use `async def` for all I/O-bound functions
- Always `await` coroutines
- Use `httpx.AsyncClient` (not `requests`)
- Use `asyncio.sleep()` (not `time.sleep()`)
- Use `AsyncSession` (not sync SQLAlchemy)

**Error Handling**
```python
# Bad
try:
    result = await process(data)
except:
    pass

# Good
try:
    result = await process(data)
except ValidationError as e:
    logger.error("Validation failed for item %s: %s", item_id, e)
    raise
```
- Never bare `except:` or broad `except Exception:`
- Catch specific exception types
- Use custom exception classes inheriting from `AppError`
- Include context in error messages (item IDs, operations)

**Code Organization**
- Imports: stdlib → third-party → local (blank lines between)
- No wildcard imports (`from module import *`)
- Max function length: ~40 lines of logic
- Use dataclasses/Pydantic for structured data
- Functions do one thing
- Use `__all__` for public APIs

**Naming**
- `snake_case` for functions, variables, modules
- `PascalCase` for classes
- `SCREAMING_SNAKE_CASE` for constants
- Prefix private with `_`
- Avoid abbreviations (`db`, `id`, `url` OK; `usr`, `cfg` not OK)

---

### 2. **fastapi-patterns** — FastAPI Architecture

**When It Activates:**
- Writing FastAPI routers, dependencies, endpoints
- Mentions of "APIRouter", "Depends", "route", "endpoint"
- Building FastAPI applications

**Key Patterns:**

**Router Organization**
```python
# app/routers/users.py
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, user)
```

**Dependency Injection**
```python
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def get_current_user(token: str = Depends(HTTPBearer())) -> User:
    return decode_token(token)

@router.get("/profile")
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user
```

**Response Models**
- Always define `response_model`
- Use Pydantic schemas
- Don't leak internal fields
- Use specific status codes (201 for POST, etc)

**Error Handling**
```python
from fastapi import HTTPException

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = await user_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user
```

---

### 3. **sqlalchemy-patterns** — SQLAlchemy 2.x Async ORM

**When It Activates:**
- Writing models, migrations, queries
- Mentions of "model", "migration", "Base", "Column", "relationship"
- Using SQLAlchemy ORM

**Model Definition**
```python
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")
```

**Async Queries**
```python
from sqlalchemy import select

async def get_user(db: AsyncSession, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

async def list_users(db: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.created_at.desc()).limit(10)
    result = await db.execute(stmt)
    return result.scalars().all()
```

**Relationships**
```python
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
```

**Migrations with Alembic**
```bash
# Create migration
alembic revision --autogenerate -m "Add user roles"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

### 4. **architecture** — System Design & Patterns

**When It Activates:**
- Planning new systems or major features
- Making technology choices
- Discussing microservices, databases, caching
- Architectural reviews

**Key Concepts:**

**Clean Architecture**
```
Entities (Core Business Logic)
  ↑ (dependencies point inward)
Application Business Rules (Use Cases, Services)
  ↑
Interface Adapters (Controllers, Repositories)
  ↑
Frameworks & Drivers (UI, DB, Web)
```

**Hexagonal Architecture**
```
Adapters (HTTP, Queues, etc)
  ↓
Ports (Interfaces)
  ↓
Domain Core (Business Logic)
  ↓
Ports (Interfaces)
  ↓
Adapters (DB, Email, etc)
```

**Architecture Decision Records (ADRs)**
```markdown
# ADR-001: Use PostgreSQL for Primary Database

## Status
Accepted

## Context
System needs strong consistency for financial transactions.

## Decision
Use PostgreSQL 15 with async connection pooling.

## Consequences
**Positive:** ACID transactions, team expertise, mature ecosystem
**Negative:** Vertical scaling limits, connection pooling overhead
```

**Design Patterns**
- **Repository Pattern**: Abstract data access
- **Service Layer**: Business logic separation
- **Dependency Injection**: Loose coupling
- **Event-Driven**: Async operations and decoupling
- **CQRS**: Separate read/write models

---

### 5. **backend-patterns** — Python Backend Architecture

**When It Activates:**
- Building Python backend services
- Repository/service layer design
- Caching strategies
- Rate limiting
- Background jobs with Celery
- Structured logging

**Patterns Covered:**
- Repository pattern for data access
- Service layer for business logic
- Redis caching strategies
- Rate limiting with Redis
- Celery for background tasks
- Structured logging with Python logging
- Error handling patterns
- Dependency injection

---

### 6. **auth-implementation-patterns** — Authentication & Authorization

**When It Activates:**
- Implementing auth systems
- JWT, OAuth, session-based auth
- Role-based access control
- Multi-factor authentication

**Patterns Covered:**
- JWT tokens (access + refresh)
- OAuth 2.0 flows
- Session-based authentication
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- Password hashing (bcrypt, argon2)
- MFA strategies
- Token refresh strategies
- Secure cookie handling

---

### 7. **frontend-dev-guidelines** — Senior Frontend Standards

**When It Activates:**
- Building React components
- Next.js applications
- Component architecture
- Data fetching and mutations
- Performance optimization

**Covers:**
- TypeScript standards
- Component patterns
- File organization
- Data fetching strategies
- State management
- Performance optimization
- Styling approaches
- Error/loading states
- Routing patterns
- Accessibility standards

---

### 8. **frontend-patterns** — React & Next.js Patterns

**When It Activates:**
- Creating React components
- Using hooks
- State management
- Memoization
- Code splitting
- Performance optimization

**Patterns:**
- Component composition
- Custom hooks
- Context API
- Memoization with React.memo and useMemo
- Code splitting and lazy loading
- Error boundaries
- Suspense patterns
- Form handling
- Animation patterns

---

### 9. **bug-hunter** — Systematic Bug Finding & Fixing

**When It Activates:**
- Debugging issues
- Tracing symptoms to root cause
- Preventing regressions

**Process:**
1. **Symptom Analysis** — What's broken?
2. **Root Cause Tracing** — Why is it broken?
3. **Impact Assessment** — What else might be affected?
4. **Fix Implementation** — What's the minimum fix?
5. **Regression Prevention** — How to prevent recurrence?
6. **Testing** — Verify the fix works

---

### 10. **mcp-server-patterns** — MCP Server Development

**When It Activates:**
- Building MCP servers
- Creating tools and resources
- Pydantic validation
- HTTP vs stdio transports

**Covers:**
- MCP server setup
- Tool definitions
- Resource management
- Prompt templates
- Pydantic validation
- Error handling
- Transport configuration

---

### 11. **bug-hunter** — Debugging Specialist

**When It Activates:**
- Investigating bugs
- Tracing failures
- Understanding error symptoms

**Methodology:**
- Symptom analysis
- Root cause identification
- Hypothesis testing
- Fix verification
- Regression prevention
- Test case creation

---

## Hooks

Hooks are automated triggers that run scripts when specific events occur. They enable CI/CD-like automation within Claude Code.

### Hook System

Hooks in this plugin use Claude Code's hook system, which is configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "enabled": true,
    "directory": "pyplugin/hooks"
  }
}
```

---

### 1. **pre-commit-check** — Pre-Commit Linting & Type Checking

**Type:** Pre-commit hook
**Event:** Before git commit
**Files:** `pyplugin/hooks/pre-commit-check.sh`

**What It Does:**
- Runs flake8 (linting)
- Runs mypy (type checking)
- Blocks commit if checks fail
- Provides clear failure messages

**Tools Used:**
- **flake8** — PEP 8 compliance, code quality
- **mypy** — Static type checking with strict settings

**Configuration:**
```bash
# Runs flake8 with:
flake8 --max-line-length=88 --extend-ignore=E203,W503 <target>

# Runs mypy with:
mypy \
  --ignore-missing-imports \
  --disallow-untyped-defs \
  --disallow-any-generics \
  --warn-return-any \
  --no-error-summary \
  <target>
```

**Triggered When:**
- Running `git commit` (if configured in .git/hooks)
- Manually: `bash pyplugin/hooks/pre-commit-check.sh [path]`
- Can check specific file or entire project

**Example Usage:**
```bash
# Check entire project
bash pyplugin/hooks/pre-commit-check.sh .

# Check specific directory
bash pyplugin/hooks/pre-commit-check.sh app/services/

# Check specific file
bash pyplugin/hooks/pre-commit-check.sh app/services/user_service.py

# Output:
# [pre-commit-check] Running pre-commit checks on: app/services/
# [pre-commit-check] Running flake8...
# [pre-commit-check] flake8: passed
# [pre-commit-check] Running mypy...
# [pre-commit-check] mypy: passed
# [pre-commit-check] All checks passed.
```

**Exit Codes:**
- `0` — All checks passed
- `1` — One or more checks failed

**Setup in Git:**
```bash
# Install pre-commit hook
ln -s pyplugin/hooks/pre-commit-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

### 2. **post-write-lint** — Auto-Lint After File Writes

**Type:** Post-write hook
**Event:** After Write or Edit tool use
**Files:**
- `pyplugin/hooks/post-write-lint.yaml` (hook configuration)
- `pyplugin/hooks/post-write-lint.sh` (script)

**What It Does:**
- Automatically runs linting and formatting
- Fixes code style issues after writing
- Ensures consistency without manual invocation

**Trigger Configuration:**
```yaml
---
name: post-write-lint
description: Run linting and formatting on write/edit operations
event: PostToolUse           # Triggered after tool use
matcher: Write|Edit          # Matches Write or Edit tools
command: bash hooks/post-write-lint.sh ${file}
---
```

**Parameters:**
- `${file}` — Path to the file that was just modified

**Triggered When:**
- File is created with Write tool
- File is edited with Edit tool
- Automatically runs without user action

**Example Behavior:**
```
User: [uses Write tool to create app/services/user_service.py]
  ↓
Hook detects PostToolUse event with Write matcher
  ↓
Hook executes: bash hooks/post-write-lint.sh app/services/user_service.py
  ↓
Script runs formatters and linters on the file
  ↓
File automatically formatted and fixed
  ↓
User sees formatted, lint-free code immediately
```

**What The Script Does:**
```bash
# Typical post-write-lint.sh:
# 1. Run black (Python formatter) on ${file}
# 2. Run ruff (fast linter) with fixes
# 3. Run isort (import sorting)
# 4. Print summary of changes
```

**Benefits:**
- No manual linting needed
- Consistent code style across team
- Catches issues immediately
- Speeds up development workflow

---

### How Hooks Work in Claude Code

**Hook Lifecycle:**

1. **Define Hook** — Create `.yaml` or `.sh` file in `pyplugin/hooks/`
2. **Configure** — Add to `settings.json` hooks directory
3. **Trigger** — Specific event occurs (pre-commit, post-write, etc)
4. **Execute** — Hook script runs automatically
5. **Report** — Results shown to user (if configured)

**Hook Event Types:**

| Event | Trigger | Use Case |
|-------|---------|----------|
| `PreToolUse` | Before tool runs | Validation, setup |
| `PostToolUse` | After tool completes | Cleanup, formatting |
| `PreCommit` | Before git commit | Linting, tests |
| `PostCommit` | After git commit | Notifications, logs |
| `FileModified` | File changed | Sync, rebuild |

**Hook Syntax:**

```yaml
---
name: hook-name
description: What this hook does
event: EventType
matcher: "pattern|regex"
command: bash script.sh ${file} ${arg}
environment:
  VAR_NAME: value
---
# Optional documentation
```

**Available Variables:**
- `${file}` — File path that triggered the hook
- `${tool}` — Tool name that triggered it
- `${args}` — Arguments passed to the tool
- `${event}` — Event type that triggered it

---

### Setting Up Hooks

**Step 1: Configure in settings.json**
```json
{
  "hooks": {
    "enabled": true,
    "directory": "pyplugin/hooks"
  }
}
```

**Step 2: Verify Hook Files Exist**
```bash
ls -la pyplugin/hooks/
# Should show:
# - pre-commit-check.sh
# - post-write-lint.sh
# - post-write-lint.yaml
# - pre-commit-check.yaml (if applicable)
```

**Step 3: Make Scripts Executable**
```bash
chmod +x pyplugin/hooks/*.sh
```

**Step 4: Test Hook**
```bash
# Test pre-commit hook manually
bash pyplugin/hooks/pre-commit-check.sh app/

# Should output:
# [pre-commit-check] Running pre-commit checks on: app/
# [pre-commit-check] flake8: passed
# [pre-commit-check] mypy: passed
```

---

## Usage Examples

### Example 1: Build a Complete Feature with TDD

**Task:** Add user authentication to FastAPI app

**Workflow:**
```bash
# 1. Plan the implementation
@planner
Add JWT authentication with refresh tokens and RBAC

# 2. Guide test-driven development
@tdd-guide app/services/auth_service.py
# Agent generates test file with fixtures and test cases

# 3. Generate the service
/generate-model User

# 4. Generate authentication endpoints
/generate-endpoint auth

# 5. Review the code
@python-reviewer app/services/auth_service.py

# 6. Security audit
@security-auditor app/routers/auth.py

# 7. Update documentation
@doc-updater
```

---

### Example 2: Refactor Large Codebase

**Task:** Improve code quality and remove duplication

**Workflow:**
```bash
# 1. Identify issues
@code-reviewer app/

# 2. Find and consolidate duplicates
@code-deduplicator src/

# 3. Clean up dead code
@refactor-cleaner

# 4. Run comprehensive review
@python-reviewer app/services/ app/routers/

# 5. Update documentation
@doc-updater
```

---

### Example 3: Secure Production Deployment

**Task:** Ensure code is secure before deploying

**Workflow:**
```bash
# 1. Audit for vulnerabilities
@security-auditor app/

# 2. Review database layer
@db-reviewer app/models/

# 3. Review authentication
@code-reviewer app/routers/auth.py

# 4. Generate tests
/generate-test app/services/auth_service.py

# 5. Final code review
/review-module app/services/auth_service.py

# 6. Deploy with confidence
# ... push to production
```

---

### Example 4: Quick Code Generation

**Task:** Generate CRUD API for users

**Terminal Usage:**
```bash
# 1. Generate user model
/generate-model User

# 2. Create migration
/generate-migration create_users_table create_table

# 3. Generate endpoints
/generate-endpoint users

# 4. Generate tests
/generate-test app/routers/users.py

# Result:
# - app/models/user.py (SQLAlchemy model)
# - app/routers/users.py (FastAPI endpoints)
# - app/services/user_service.py (business logic)
# - app/schemas/user.py (Pydantic models)
# - tests/test_users.py (pytest tests)
# - alembic/versions/...py (database migration)
```

---

### Example 5: Interactive Feature Planning

**Task:** Design new real-time notification system

**Workflow:**
```bash
# 1. Design architecture
@architect
We need a real-time notification system.
Expected: 10K+ notifications/minute
Latency: <100ms delivery
Persistence: 30-day retention
Scale: Upgrade from 10K to 100K users in 6 months

# Agent provides:
# - Architecture diagram
# - Technology recommendations
# - Scalability plan
# - Trade-off analysis

# 2. Plan implementation
@planner
Implement WebSocket support for real-time notifications using FastAPI

# Agent provides:
# - Step-by-step plan
# - Files to create/modify
# - Dependencies needed
# - Risk assessment

# 3. Review design
@code-reviewer [generates files based on plan]

# 4. Security audit
@security-auditor [files generated]
```

---

## Plugin Architecture

### Directory Structure

```
pyplugin/
├── README.md (this file)
├── .claude-plugin/
│   └── plugin.json                 # Plugin metadata
├── agents/                         # Autonomous agents
│   ├── architect.md               # System design specialist
│   ├── build-error-resolver.md    # Build error fixer
│   ├── code-deduplicator.md       # Duplicate code removal
│   ├── code-reviewer.md           # Code quality review
│   ├── db-reviewer.md             # Database review
│   ├── doc-updater.md             # Documentation generator
│   ├── docs-lookup.md             # API documentation lookup
│   ├── planner.md                 # Implementation planning
│   ├── python-reviewer.md         # Python code review
│   ├── refactor-cleaner.md        # Dead code cleanup
│   ├── security-auditor.md        # Security auditing
│   └── tdd-guide.md               # Test-driven development
├── commands/                       # Quick code generation
│   ├── generate-test.md           # Pytest generator
│   ├── generate-migration.md      # Alembic migration
│   ├── generate-model.md          # SQLAlchemy model
│   ├── generate-endpoint.md       # FastAPI endpoint
│   └── review-module.md           # Code review
├── hooks/                          # Automated triggers
│   ├── pre-commit-check.sh        # Pre-commit linting
│   ├── pre-commit-check.yaml      # Hook config
│   ├── post-write-lint.sh         # Auto-formatting
│   └── post-write-lint.yaml       # Hook config
└── skills/                         # Technology patterns
    ├── architecture/              # System design patterns
    ├── auth-implementation-patterns/  # Auth patterns
    ├── backend-patterns/          # Python backend patterns
    ├── bug-hunter/                # Debugging specialist
    ├── fastapi-patterns/          # FastAPI architecture
    ├── frontend-design/           # Frontend design system
    ├── frontend-developer/        # React components
    ├── frontend-dev-guidelines/   # Frontend standards
    ├── frontend-patterns/         # React patterns
    ├── frontend-slides/           # Presentation builder
    ├── mcp-server-patterns/       # MCP server building
    ├── python-best-practices/     # Python standards
    └── sqlalchemy-patterns/       # SQLAlchemy patterns
```

### How Components Interact

```
User Request
  ↓
Claude Code Harness
  ↓
┌─────────────────────────────┐
│    Plugin Router            │
├─────────────────────────────┤
│ • Agents (@agent-name)      │
│ • Commands (/command-name)  │
│ • Skills (auto-trigger)     │
│ • Hooks (events)            │
└─────────────────────────────┘
  ↓
Agent/Command/Skill Execution
  ↓
Tools (Read, Write, Edit, Bash, Grep, Glob)
  ↓
Output to User
```

---

### Configuration

**settings.json Integration:**
```json
{
  "plugins": [
    {
      "name": "pyplugin",
      "path": "/home/kaushal/Claudecode/pyplugin",
      "enabled": true
    }
  ],
  "hooks": {
    "enabled": true,
    "directory": "pyplugin/hooks"
  }
}
```

**Environment Setup:**
```bash
# Install dependencies (for hooks)
pip install flake8 mypy black ruff isort

# Make hooks executable
chmod +x pyplugin/hooks/*.sh

# Optional: Set up pre-commit git hook
ln -s pyplugin/hooks/pre-commit-check.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

## Contributing

### Adding a New Agent

1. Create `agents/your-agent.md`:
```yaml
name: your-agent
description: One-line description of what it does

model: claude-opus-4-6  # or claude-sonnet-4-6

system_prompt: |
  You are a specialist in [domain].

  ## Your Role
  [What you do]

  ## Workflow
  [Steps you follow]

tools:
  - read_file
  - write_file
  - bash

tool_permissions:
  bash:
    allow:
      - "command-you-allow"
    deny:
      - "command-you-deny"

invoke_with: "@your-agent"
```

2. Document it in this README under [Agents](#agents)

---

### Adding a New Command

1. Create `commands/your-command.md`:
```yaml
---
name: your-command
description: One-line description
usage: /your-command <argument>
---

# What It Does
[Detailed explanation]

## Arguments
- `$ARGUMENTS` — Argument description

## Example Output
[Expected output]
```

2. Document it in this README under [Commands / Skills](#commands--skills)

---

### Adding a New Skill

1. Create `skills/your-skill/SKILL.md`:
```markdown
---
name: your-skill
description: One-line description
---

# Skill Documentation

## When to Use
[When this skill is relevant]

## Core Content
[Patterns, guides, best practices]

## Related Skills
[Other relevant skills]
```

2. Add supporting resources in `skills/your-skill/resources/`

3. Document it in this README

---

## Troubleshooting

### Hooks Not Running

**Problem:** Post-write hooks not executing

**Solution:**
1. Check `settings.json` has hooks enabled
2. Verify hook directory path is correct
3. Ensure scripts are executable: `chmod +x pyplugin/hooks/*.sh`
4. Check hook file has proper YAML format

### Agent Not Responding

**Problem:** Agent doesn't activate

**Solution:**
1. Use correct syntax: `@agent-name [context]`
2. Provide context about what you need
3. Check agent file exists in `pyplugin/agents/`
4. Agent files should have `invoke_with:` field

### Commands Not Found

**Problem:** `/command-name` not recognized

**Solution:**
1. Use correct syntax: `/command-name arguments`
2. Verify command file exists in `pyplugin/commands/`
3. Commands need `usage:` field in frontmatter
4. Ensure plugin is loaded in settings

---

## FAQ

**Q: Can I use this plugin in multiple repositories?**
A: Yes! Use symlinks or copy the entire plugin directory to each repo's `.claude/plugins/` directory.

**Q: How do I customize agent behavior?**
A: Edit the `system_prompt` field in the agent's `.md` file, then reload Claude Code.

**Q: Can I add new hooks?**
A: Yes! Create a new `.sh` script and `.yaml` config in `pyplugin/hooks/`, then reference in `settings.json`.

**Q: Which model should I choose for my agent?**
A: Use `claude-opus-4-6` for complex reasoning, `claude-sonnet-4-6` for balanced performance, `claude-haiku-4-5` for quick/simple tasks.

**Q: How do I see hook output?**
A: Hooks print to console/terminal. Check your Claude Code output panel or terminal.

**Q: Can I chain agents together?**
A: Yes! Run agents sequentially or in parallel based on your workflow needs.

---

## Support & Feedback

- **Report Issues:** github.com/anthropics/claude-code/issues
- **Plugin Help:** Use `/help` command in Claude Code
- **Feedback:** Report via Claude Code issue tracker

---

## License

This plugin is part of the Claude Code project.

---

**Last Updated:** 2026-03-30
**Version:** 1.1.0
**Maintained By:** JJS
