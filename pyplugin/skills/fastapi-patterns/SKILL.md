---
name: fastapi-patterns
description: FastAPI architecture patterns for routers, dependency injection, response models, and service layer separation. Activates on APIRouter, Depends, router, endpoint keywords.
---

# FastAPI Patterns

## Trigger Conditions

Automatically activate this skill when:
- Writing or modifying FastAPI routers or endpoints
- The user mentions "APIRouter", "Depends", "router", "endpoint", "dependency injection", or "response_model"
- Creating a new FastAPI route, service layer, or API schema

---

## Project Structure

Enforce separation of concerns:

```
app/
  routers/      ← HTTP layer only: parse request, call service, return response
  services/     ← business logic: orchestrates DB calls, raises HTTPException
  models/       ← SQLAlchemy ORM models
  schemas/      ← Pydantic request/response models
  dependencies/ ← reusable Depends() factories
  core/         ← config, security, lifespan
```

**Rule**: No SQLAlchemy queries in routers. No `HTTPException` in models. Business logic lives in services.

## Router Pattern

```python
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user
from app.schemas.order import OrderCreate, OrderResponse
from app.services import order_service

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> OrderResponse:
    """Create a new order for the current user."""
    return await order_service.create(db, payload, owner_id=current_user.id)
```

**Always set `response_model`** — prevents accidental data leakage.

## Dependency Injection

- Use `Depends()` for: DB sessions, current user, pagination params, feature flags
- Dependency functions should be `async` if they do I/O
- Use `Annotated` for cleaner signatures (FastAPI 0.95+):

```python
from typing import Annotated
from fastapi import Depends

DbSession = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int, db: DbSession, user: CurrentUser) -> OrderResponse:
    ...
```

## Service Layer

```python
# app/services/order_service.py
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.order import Order
from app.schemas.order import OrderCreate

async def create(db: AsyncSession, payload: OrderCreate, owner_id: int) -> Order:
    order = Order(**payload.model_dump(), owner_id=owner_id)
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def get_or_404(db: AsyncSession, order_id: int) -> Order:
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order
```

## Pydantic Schemas (v2)

```python
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime

class OrderBase(BaseModel):
    item_name: str
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
```

- Always use `model_config = ConfigDict(from_attributes=True)` on response models
- Use `field_validator` and `model_validator` instead of `@validator` (Pydantic v2)
- Never expose internal fields (passwords, tokens) in response models

## Error Handling

Use a consistent error format via an exception handler in `app/core/exceptions.py`:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

async def app_exception_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message, "code": exc.code},
    )
```

Register in `app/main.py`:
```python
app.add_exception_handler(AppError, app_exception_handler)
```

## Pagination

Use a reusable dependency:

```python
from fastapi import Query
from typing import Annotated

def pagination_params(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> dict[str, int]:
    return {"skip": skip, "limit": limit}
```

## Background Tasks

`BackgroundTasks` is for fast, non-critical fire-and-forget work (e.g. sending an email).
- Never put long-running or blocking work in `BackgroundTasks` — use Celery or ARQ
- Always pass dependencies explicitly to background functions (don't capture `db` from the request scope — it closes after the response)

## Lifespan (not deprecated `startup`/`shutdown`)

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await db_pool.connect()
    yield
    # shutdown
    await db_pool.disconnect()

app = FastAPI(lifespan=lifespan)
```
