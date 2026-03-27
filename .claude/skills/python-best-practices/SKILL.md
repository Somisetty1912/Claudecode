---
name: python-best-practices
description: Python coding standards for type safety, async correctness, and code quality. Auto-activates on any .py file.
triggers:
  - file_extension: .py
---

# Python Best Practices

Apply these rules to every Python file you write or modify.

## Type Hints — Non-Negotiable

- Every function parameter and return type must be annotated
- No `Any` from `typing` — if you can't name the type, narrow it
- Use `X | None` (Python 3.10+) instead of `Optional[X]`
- Use `list[T]`, `dict[K, V]`, `tuple[T, ...]` — not `List`, `Dict`, `Tuple` from `typing`
- Use `TypeAlias` for complex repeated types
- Use `TypeVar` for generic functions instead of `Any`

```python
# Bad
def process(items, config=None):
    ...

# Good
def process(items: list[str], config: Config | None = None) -> list[Result]:
    ...
```

## Async Rules

- Use `async def` for all I/O-bound functions (DB, HTTP, file)
- Always `await` coroutines — never call them without await
- Never use `requests` in async code — use `httpx.AsyncClient`
- Never use `time.sleep()` — use `asyncio.sleep()`
- Never use sync SQLAlchemy session in async context — use `AsyncSession`
- Prefer `asyncio.gather()` for concurrent independent coroutines

```python
# Bad
def get_user(user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

# Good
async def get_user(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

## Error Handling

- Never use bare `except:` or `except Exception:` without re-raising or logging
- Catch specific exception types
- Use custom exception classes that inherit from a base `AppError`
- Always include context in error messages — include the relevant ID or operation

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

## Imports

- Group: stdlib → third-party → local, separated by blank lines
- No wildcard imports (`from module import *`)
- No circular imports — restructure if needed
- Import at module level — no inline imports unless for optional dependencies

## Code Structure

- Functions do one thing — if you need "and" to describe it, split it
- Max function length: ~40 lines of logic (not counting docstrings/blank lines)
- Prefer dataclasses or Pydantic models over bare dicts for structured data
- Use `__all__` in modules with a public API

## Naming

- `snake_case` for functions, variables, modules
- `PascalCase` for classes
- `SCREAMING_SNAKE_CASE` for module-level constants
- Prefix private methods/attrs with `_`
- Avoid abbreviations unless universally understood (`db`, `id`, `url` are fine; `usr`, `cfg` are not)

## Avoid List

- `global` and `nonlocal` — restructure instead
- Mutable default arguments (`def f(items=[])` → use `None` and initialize inside)
- String formatting with `%` — use f-strings
- `print()` for logging — use `logging` or `structlog`
- `assert` for runtime checks in production code — use explicit `if/raise`
