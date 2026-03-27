# Generate Alembic Migration

Generate an Alembic migration file with `upgrade()` and `downgrade()` for a described schema change.

## Arguments
- `$ARGUMENTS` — plain-English description of the migration (e.g. `add-orders-table`, `add-status-column-to-users`, `drop-legacy-tokens-table`)

## What to generate

Parse $ARGUMENTS to derive a short slug for the filename (kebab-case).

### Migration file (`alembic/versions/<timestamp>_<slug>.py`)

Generate a complete Alembic migration file:

```python
"""<slug>

Revision ID: <generate a random 12-char hex string>
Revises: <detect the current head revision, or leave as placeholder>
Create Date: <today's date>
"""
from alembic import op
import sqlalchemy as sa

revision = '<hex>'
down_revision = '<parent_or_None>'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # TODO: implement based on description
    pass


def downgrade() -> None:
    # TODO: implement based on description
    pass
```

Then, based on the description, fill in the `upgrade()` and `downgrade()` bodies:

- **add-*-table**: `op.create_table(...)` / `op.drop_table(...)`
- **add-*-column**: `op.add_column(...)` / `op.drop_column(...)`
- **drop-*-table**: `op.drop_table(...)` / recreate in downgrade
- **rename-*-column**: `op.alter_column(old, new=new)` / reverse
- **add-index-***: `op.create_index(...)` / `op.drop_index(...)`
- **add-fk-***: `op.create_foreign_key(...)` / `op.drop_constraint(...)`

## Rules
- Always implement `downgrade()` — never leave it as a no-op unless the operation is truly irreversible (and add a comment explaining why)
- Use `sa.text()` for raw SQL only when no alembic op exists
- Follow the `sqlalchemy-patterns` skill if active
- Print the generated file path and a one-line summary of what it does
