---
name: backend-patterns
description: Python backend architecture patterns for FastAPI, SQLAlchemy 2.x async, Pydantic v2, Redis, and Celery. Covers API design, repository/service layers, caching, auth, rate limiting, background jobs, and structured logging. Activates on repository, service layer, middleware, rate limit, cache, background job, JWT, RBAC keywords.
---

# Python Backend Patterns

## Trigger Conditions

Automatically activate this skill when:
- Designing or structuring a FastAPI application (routers, services, repositories)
- User mentions "repository pattern", "service layer", "middleware", "dependency injection"
- Implementing caching (Redis, cache-aside), rate limiting, or background jobs
- Adding authentication (JWT), authorization (RBAC), or permission checks
- Setting up structured logging, request ID propagation, or error handlers
- Asking about N+1 queries, transactions, or query optimization with SQLAlchemy

---

## API Design Patterns

### RESTful Resource Structure (FastAPI)

```python
# ✅ Resource-based routers
# GET    /markets           - list
# GET    /markets/{id}      - get one
# POST   /markets           - create
# PUT    /markets/{id}      - replace
# PATCH  /markets/{id}      - update
# DELETE /markets/{id}      - delete

from fastapi import APIRouter, Query

router = APIRouter(prefix="/markets", tags=["markets"])

@router.get("/")
async def list_markets(
    status: str | None = Query(None),
    sort: str = Query("volume"),
    limit: int = Query(20, le=100),
    offset: int = Query(0),
) -> list[MarketOut]:
    return await market_service.list(status=status, sort=sort, limit=limit, offset=offset)
```

### Repository Pattern

```python
# Abstract data access — decouples business logic from ORM details
from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class MarketRepository(ABC):
    @abstractmethod
    async def find_all(self, filters: MarketFilters | None = None) -> list[Market]: ...
    @abstractmethod
    async def find_by_id(self, id: int) -> Market | None: ...
    @abstractmethod
    async def create(self, data: CreateMarketDTO) -> Market: ...
    @abstractmethod
    async def update(self, id: int, data: UpdateMarketDTO) -> Market: ...
    @abstractmethod
    async def delete(self, id: int) -> None: ...

class SQLAlchemyMarketRepository(MarketRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def find_all(self, filters: MarketFilters | None = None) -> list[Market]:
        stmt = select(Market)
        if filters and filters.status:
            stmt = stmt.where(Market.status == filters.status)
        if filters and filters.limit:
            stmt = stmt.limit(filters.limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def find_by_id(self, id: int) -> Market | None:
        return await self.session.get(Market, id)
```

### Service Layer Pattern

```python
# Business logic separated from data access
class MarketService:
    def __init__(self, repo: MarketRepository) -> None:
        self.repo = repo

    async def search_markets(self, query: str, limit: int = 10) -> list[Market]:
        embedding = await generate_embedding(query)
        results = await self._vector_search(embedding, limit)
        ids = [r.id for r in results]
        markets = await self.repo.find_by_ids(ids)
        score_map = {r.id: r.score for r in results}
        return sorted(markets, key=lambda m: score_map.get(m.id, 0))

    async def _vector_search(self, embedding: list[float], limit: int) -> list[SearchResult]:
        ...
```

### Dependency Injection (FastAPI)

```python
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

async def get_market_service(
    session: AsyncSession = Depends(get_db),
) -> MarketService:
    repo = SQLAlchemyMarketRepository(session)
    return MarketService(repo)

@router.get("/{market_id}")
async def get_market(
    market_id: int,
    service: MarketService = Depends(get_market_service),
) -> MarketOut:
    market = await service.get_by_id(market_id)
    if not market:
        raise HTTPException(status_code=404, detail="Market not found")
    return MarketOut.model_validate(market)
```

### Middleware Pattern

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time, logging

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start
        logging.info(
            "request",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "duration_ms": round(duration * 1000, 2),
            },
        )
        return response

app.add_middleware(RequestLoggingMiddleware)
```

---

## Database Patterns

### Query Optimization

```python
# ✅ GOOD: select only needed columns
stmt = select(Market.id, Market.name, Market.status, Market.volume).where(
    Market.status == "active"
).order_by(Market.volume.desc()).limit(10)

# ❌ BAD: loads entire ORM object when you only need a few fields
result = await session.execute(select(Market))
```

### N+1 Prevention

```python
from sqlalchemy.orm import selectinload, joinedload

# ❌ BAD: N+1 — accessing market.creator inside loop triggers lazy loads
markets = (await session.execute(select(Market))).scalars().all()
for market in markets:
    print(market.creator.name)  # N extra queries

# ✅ GOOD: eager load relationships up front
stmt = select(Market).options(selectinload(Market.creator))
markets = (await session.execute(stmt)).scalars().all()
for market in markets:
    print(market.creator.name)  # no extra queries

# ✅ GOOD: batch fetch by IDs when ORM relationship isn't an option
creator_ids = [m.creator_id for m in markets]
creators = (
    await session.execute(select(User).where(User.id.in_(creator_ids)))
).scalars().all()
creator_map = {u.id: u for u in creators}
```

### Transaction Pattern

```python
from sqlalchemy.ext.asyncio import AsyncSession

async def create_market_with_position(
    session: AsyncSession,
    market_data: CreateMarketDTO,
    position_data: CreatePositionDTO,
) -> Market:
    async with session.begin():           # commits on exit, rolls back on exception
        market = Market(**market_data.model_dump())
        session.add(market)
        await session.flush()             # get market.id without committing

        position = Position(market_id=market.id, **position_data.model_dump())
        session.add(position)
    return market
```

---

## Caching Strategies

### Redis Cache-Aside Pattern

```python
import json
from redis.asyncio import Redis

class CachedMarketRepository(MarketRepository):
    def __init__(self, base: MarketRepository, redis: Redis) -> None:
        self._base = base
        self._redis = redis

    async def find_by_id(self, id: int) -> Market | None:
        key = f"market:{id}"
        cached = await self._redis.get(key)
        if cached:
            return Market.model_validate_json(cached)

        market = await self._base.find_by_id(id)
        if market:
            await self._redis.setex(key, 300, market.model_dump_json())
        return market

    async def invalidate(self, id: int) -> None:
        await self._redis.delete(f"market:{id}")
```

### Function-Level Cache Decorator

```python
import functools, hashlib, json
from collections.abc import Callable

def cached(ttl: int = 300, key_prefix: str = ""):
    def decorator(fn: Callable):
        @functools.wraps(fn)
        async def wrapper(*args, redis: Redis, **kwargs):
            raw_key = f"{key_prefix}:{fn.__name__}:{args}:{sorted(kwargs.items())}"
            cache_key = hashlib.sha256(raw_key.encode()).hexdigest()
            hit = await redis.get(cache_key)
            if hit:
                return json.loads(hit)
            result = await fn(*args, **kwargs)
            await redis.setex(cache_key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator
```

---

## Error Handling Patterns

### Custom Exception Hierarchy

```python
class AppError(Exception):
    status_code: int = 500
    detail: str = "Internal server error"

class NotFoundError(AppError):
    status_code = 404
    def __init__(self, resource: str, id: int | str):
        self.detail = f"{resource} {id} not found"

class PermissionError(AppError):
    status_code = 403
    detail = "Insufficient permissions"

class ValidationError(AppError):
    status_code = 422
```

### Global Exception Handler

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": exc.detail},
    )

@app.exception_handler(Exception)
async def unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
    logging.exception("Unhandled error", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error"},
    )
```

### Retry with Exponential Backoff

```python
import asyncio
from collections.abc import Callable, Awaitable
from typing import TypeVar

T = TypeVar("T")

async def with_retry(
    fn: Callable[[], Awaitable[T]],
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> T:
    last_error: Exception
    for attempt in range(max_retries):
        try:
            return await fn()
        except Exception as exc:
            last_error = exc
            if attempt < max_retries - 1:
                await asyncio.sleep(base_delay * (2 ** attempt))
    raise last_error

# Usage
data = await with_retry(lambda: fetch_from_api())
```

---

## Authentication & Authorization

### JWT Validation Dependency

```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel

bearer_scheme = HTTPBearer()

class TokenPayload(BaseModel):
    sub: str          # user id
    email: str
    role: str

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> TokenPayload:
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.JWT_SECRET,
            algorithms=["HS256"],
        )
        return TokenPayload(**payload)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Usage
@router.get("/me")
async def get_me(user: TokenPayload = Depends(get_current_user)) -> UserOut:
    ...
```

### Role-Based Access Control

```python
from enum import StrEnum

class Role(StrEnum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"

ROLE_PERMISSIONS: dict[Role, set[str]] = {
    Role.ADMIN:     {"read", "write", "delete", "admin"},
    Role.MODERATOR: {"read", "write", "delete"},
    Role.USER:      {"read", "write"},
}

def require_permission(permission: str):
    async def dependency(user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
        if permission not in ROLE_PERMISSIONS.get(Role(user.role), set()):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return Depends(dependency)

# Usage
@router.delete("/{market_id}")
async def delete_market(
    market_id: int,
    user: TokenPayload = require_permission("delete"),
) -> None:
    await market_service.delete(market_id)
```

---

## Rate Limiting

### Redis Sliding Window Rate Limiter

```python
import time
from redis.asyncio import Redis
from fastapi import Request, HTTPException

class RateLimiter:
    def __init__(self, redis: Redis, max_requests: int, window_seconds: int) -> None:
        self.redis = redis
        self.max_requests = max_requests
        self.window = window_seconds

    async def check(self, identifier: str) -> None:
        key = f"rate:{identifier}"
        now = time.time()
        window_start = now - self.window

        pipe = self.redis.pipeline()
        pipe.zremrangebyscore(key, "-inf", window_start)
        pipe.zadd(key, {str(now): now})
        pipe.zcard(key)
        pipe.expire(key, self.window)
        *_, count, _ = await pipe.execute()

        if count > self.max_requests:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

limiter = RateLimiter(redis_client, max_requests=100, window_seconds=60)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = request.client.host
    await limiter.check(ip)
    return await call_next(request)
```

---

## Background Jobs

### Celery Task Pattern

```python
from celery import Celery

celery_app = Celery("worker", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery_app.task(bind=True, max_retries=3, default_retry_delay=60)
def index_market(self, market_id: int) -> None:
    try:
        market = db_sync.get(Market, market_id)
        vector_index.upsert(market_id, build_embedding(market))
    except Exception as exc:
        raise self.retry(exc=exc)

# Dispatch from FastAPI without blocking
@router.post("/")
async def create_market(data: CreateMarketIn, session=Depends(get_db)) -> MarketOut:
    market = await market_service.create(session, data)
    index_market.delay(market.id)        # fire-and-forget
    return MarketOut.model_validate(market)
```

### asyncio Background Task (lightweight, in-process)

```python
import asyncio
from collections.abc import Coroutine

class BackgroundTaskQueue:
    def __init__(self) -> None:
        self._queue: asyncio.Queue[Coroutine] = asyncio.Queue()
        self._task: asyncio.Task | None = None

    def start(self) -> None:
        self._task = asyncio.create_task(self._worker())

    async def enqueue(self, coro: Coroutine) -> None:
        await self._queue.put(coro)

    async def _worker(self) -> None:
        while True:
            coro = await self._queue.get()
            try:
                await coro
            except Exception:
                logging.exception("Background task failed")
            finally:
                self._queue.task_done()

task_queue = BackgroundTaskQueue()

@app.on_event("startup")
async def startup() -> None:
    task_queue.start()
```

---

## Logging & Monitoring

### Structured JSON Logging

```python
import logging, sys
from pythonjsonlogger import jsonlogger

def configure_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        jsonlogger.JsonFormatter(
            fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
    )
    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(logging.INFO)

logger = logging.getLogger(__name__)

logger.info(
    "Fetching markets",
    extra={"request_id": request_id, "method": "GET", "path": "/api/markets"},
)
```

### Request ID Propagation

```python
import uuid
from contextvars import ContextVar
from fastapi import Request

request_id_var: ContextVar[str] = ContextVar("request_id", default="")

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        req_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request_id_var.set(req_id)
        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        return response

def get_request_id() -> str:
    return request_id_var.get()
```

---

**Choose the simplest pattern that fits.** Repository + service layers pay off with multiple data sources or complex business logic — not for trivial CRUD.
