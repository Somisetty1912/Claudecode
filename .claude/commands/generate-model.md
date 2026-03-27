---
name: generate-model
description: Generate SQLAlchemy model + Alembic migration stub + Pydantic schemas
usage: /generate-model <ModelName>
---

# Generate SQLAlchemy Model

Generate a complete SQLAlchemy model with Alembic migration stub and Pydantic schemas.

## Arguments
- `$ARGUMENTS` — the model name in PascalCase (e.g. `Order`, `UserProfile`)

## What to generate

Parse $ARGUMENTS to extract `name` (e.g. `Order`). Derive snake_case (`order`) and plural (`orders`) forms automatically.

### 1. SQLAlchemy Model (`app/models/<name_snake>.py` or equivalent)
- Inherit from the project's `Base` (find it — typically `app/database.py` or `app/db/base.py`)
- `__tablename__` = snake_case plural (e.g. `orders`)
- Standard audit columns: `id` (UUID or Integer, check existing models), `created_at`, `updated_at`
- Add 3–5 placeholder columns with appropriate types and comments to guide the developer
- `__repr__` method
- Relationships: add a commented-out example relationship stub

### 2. Alembic Migration Stub (`alembic/versions/<timestamp>_add_<name_snake>_table.py`)
- Generate a valid migration file with `upgrade()` and `downgrade()`
- `upgrade()`: `op.create_table(...)` with all columns from the model
- `downgrade()`: `op.drop_table(...)`
- Use `alembic.op` and `sqlalchemy` column types to match the model

### 3. Pydantic Schemas (`app/schemas/<name_snake>.py` or equivalent)
- `<Name>Base` — shared fields
- `<Name>Create(Base)` — fields required at creation (no id/timestamps)
- `<Name>Update(Base)` — all fields Optional for partial updates
- `<Name>Response(Base)` — includes id, created_at, updated_at; `model_config = ConfigDict(from_attributes=True)`

## Rules
- Follow the `sqlalchemy-patterns` and `python-best-practices` skills if active
- Use type hints everywhere; no bare `Column` without a Python type annotation
- Import the model in `app/models/__init__.py` (or equivalent) so Alembic can detect it
- Print a summary of files created/modified at the end
