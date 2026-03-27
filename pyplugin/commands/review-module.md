---
name: review-module
description: Code review types, async, error handling, OWASP security
usage: /review-module <file_path>
---

# Review FastAPI Module

Perform a thorough code review of the given file, covering types, async correctness, error handling, and security.

## Arguments
- `$ARGUMENTS` — path to the file to review (e.g. `app/routers/orders.py`)

## Review process

Read the file at `$ARGUMENTS` in full. Then produce a structured review report with the following sections:

---

### 1. Type Safety
- Missing type annotations (function args, return types, class attributes)
- Use of `Any` — flag every occurrence and suggest a concrete type
- Incorrect or overly broad types
- Missing `Optional` / `Union` where `None` is possible

### 2. Async Correctness
- Sync DB calls inside `async def` (e.g. using `session.execute()` without `await`)
- Blocking I/O in async context (file reads, `requests.*`, `time.sleep`)
- Missing `await` on coroutines
- Incorrect use of `asyncio.run()` inside a running event loop

### 3. Error Handling
- Bare `except:` or `except Exception:` without re-raise or logging
- Missing `HTTPException` raises for expected failure cases (404, 403, 422)
- Swallowed exceptions
- Inconsistent error response shapes

### 4. Security
- SQL injection risk (raw string interpolation in queries)
- Missing authorization checks (routes that should require auth but don't use `Depends`)
- Exposed secrets or credentials in code
- Unvalidated user input passed directly to the filesystem or shell
- OWASP API Top 10 issues: mass assignment, excessive data exposure, broken object-level authorization

### 5. FastAPI Best Practices
- Business logic in route handlers (should be in service layer)
- N+1 query patterns in routes or services
- Missing `response_model` on route decorators
- Incorrect use of `BackgroundTasks` (blocking work in background tasks)

---

## Output format

For each issue found:
```
[SEVERITY: HIGH|MEDIUM|LOW] <file>:<line> — <issue description>
Suggested fix: <one-line fix or code snippet>
```

End with a **Summary** table:
| Category | Issues Found |
|---|---|
| Type Safety | N |
| Async | N |
| Error Handling | N |
| Security | N |
| FastAPI Patterns | N |

If no issues are found in a category, say "✓ Clean".
