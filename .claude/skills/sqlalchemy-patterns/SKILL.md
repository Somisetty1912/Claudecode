---
name: sqlalchemy-patterns
description: SQLAlchemy 2.x async ORM patterns for models, queries, relationships, and Alembic migrations. Activates on model, migration, Base, Column, relationship keywords.
triggers:
  - keyword: model
  - keyword: migration
  - keyword: Base
  - keyword: Column
  - keyword: relationship
---

# SQLAlchemy Patterns (2.x Async)

## Model Definition

Use the new `DeclarativeBase` + `Mapped` style (SQLAlchemy 2.0+):

```python
from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_name: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    owner: Mapped["User"] = relationship(back_populates="orders")

    def __repr__(self) -> str:
        return f"<Order id={self.id} item={self.item_name!r}>"
```

**Always use `Mapped[T]` + `mapped_column()`** — never bare `Column()` (SQLAlchemy 1.x style).

## Async Session Setup

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
```

## Query Patterns

```python
from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

# Fetch by primary key
async def get_by_id(db: AsyncSession, order_id: int) -> Order | None:
    return await db.get(Order, order_id)

# Fetch with filter
async def get_by_owner(db: AsyncSession, owner_id: int) -> list[Order]:
    result = await db.execute(
        select(Order)
        .where(Order.owner_id == owner_id)
        .order_by(Order.created_at.desc())
    )
    return list(result.scalars().all())

# Eager load relationships — avoid N+1
async def get_with_owner(db: AsyncSession, order_id: int) -> Order | None:
    result = await db.execute(
        select(Order)
        .options(selectinload(Order.owner))
        .where(Order.id == order_id)
    )
    return result.scalar_one_or_none()

# Bulk update
async def mark_shipped(db: AsyncSession, order_ids: list[int]) -> None:
    await db.execute(
        update(Order)
        .where(Order.id.in_(order_ids))
        .values(status="shipped")
    )
    await db.commit()
```

## N+1 Prevention Rules

- Never access a relationship attribute without eager-loading it in the query
- Use `selectinload()` for one-to-many (emits 2 queries total)
- Use `joinedload()` for many-to-one / optional (single JOIN query)
- Use `contains_eager()` when you've already joined manually
- Run queries with `echo=True` in dev to spot N+1s

## Transactions

```python
# Explicit transaction for multi-step operations
async def transfer(db: AsyncSession, from_id: int, to_id: int, amount: int) -> None:
    async with db.begin():
        from_acct = await db.get(Account, from_id, with_for_update=True)
        to_acct = await db.get(Account, to_id, with_for_update=True)
        from_acct.balance -= amount
        to_acct.balance += amount
    # commit happens automatically on context exit
```

## Alembic Migration Rules

- **Always implement `downgrade()`** — never a no-op unless truly irreversible
- Use `server_default` for column defaults, not Python-side defaults in migrations
- Add indexes explicitly: `op.create_index("ix_orders_owner_id", "orders", ["owner_id"])`
- For large tables, use `postgresql_concurrently=True` for index creation
- Add `nullable=False` columns in two steps: add nullable, backfill, then set not-null

```python
# Safe nullable=False addition
def upgrade() -> None:
    op.add_column("orders", sa.Column("status", sa.String(50), nullable=True))
    op.execute("UPDATE orders SET status = 'pending' WHERE status IS NULL")
    op.alter_column("orders", "status", nullable=False)

def downgrade() -> None:
    op.drop_column("orders", "status")
```

## Relationship Patterns

```python
# One-to-many
class User(Base):
    orders: Mapped[list["Order"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )

# Many-to-many (association table)
from sqlalchemy import Table, Column, ForeignKey

order_tags = Table(
    "order_tags",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Order(Base):
    tags: Mapped[list["Tag"]] = relationship(secondary=order_tags, back_populates="orders")
```

## Index Strategy

Add indexes for:
- All foreign key columns (SQLAlchemy does NOT auto-index FK columns)
- Columns used in `WHERE` clauses in hot paths
- Columns used in `ORDER BY` on large tables
- Composite indexes for multi-column WHERE conditions (column order matters)

```python
from sqlalchemy import Index

class Order(Base):
    __table_args__ = (
        Index("ix_orders_owner_status", "owner_id", "status"),
    )
```
