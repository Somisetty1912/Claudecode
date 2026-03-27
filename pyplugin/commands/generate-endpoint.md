---
name: generate-endpoint
description: Generate router + schemas + service + test for a resource/method
usage: /generate-endpoint <resource> <method>
---

# Generate FastAPI Endpoint

Generate a complete FastAPI endpoint implementation for the given resource and HTTP method.

## Arguments
- `$ARGUMENTS` — format: `<resource> <method>` (e.g. `order POST` or `user GET`)

## What to generate

Parse $ARGUMENTS to extract `resource` (e.g. `order`) and `method` (e.g. `POST`, `GET`, `PUT`, `DELETE`, `PATCH`).

Generate the following files, inferring paths from the existing project structure:

### 1. Router (`app/routers/<resource>s.py` or equivalent)
- `APIRouter` with appropriate prefix and tags
- Route handler using `async def`
- Dependency injection via `Depends()` for DB session and any auth
- Proper status codes (`status_code=201` for POST, etc.)
- Docstring on the route function

### 2. Schemas (`app/schemas/<resource>.py` or equivalent)
- Pydantic `BaseModel` for request body (e.g. `OrderCreate`, `OrderUpdate`)
- Pydantic `BaseModel` for response (e.g. `OrderResponse`, `OrderListResponse`)
- Use `model_config = ConfigDict(from_attributes=True)` (Pydantic v2)
- Include field validators where appropriate

### 3. Service (`app/services/<resource>_service.py` or equivalent)
- Pure async function(s) containing business logic
- Takes `db: AsyncSession` as first argument
- Raises `HTTPException` with meaningful status codes on failure
- No direct DB queries in the router — all DB access through the service

### 4. Test (`tests/test_<resource>_<method>.py` or equivalent)
- `pytest` + `httpx.AsyncClient` fixture
- Happy path test
- Error case test (e.g. 404, 422 validation error)
- Uses `pytest.mark.asyncio`

## Rules
- Follow the `fastapi-patterns` skill if active
- Use type hints everywhere
- No `Any` types
- Async throughout — never use sync DB calls
- Add the new router to `app/main.py` (or wherever routers are registered) if it doesn't already exist
- Print a summary of files created/modified at the end
