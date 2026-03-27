# Generate pytest Test File

Generate a comprehensive pytest test file for an existing Python module or service.

## Arguments
- `$ARGUMENTS` — path to the module to test (e.g. `app/services/user_service.py` or `app/routers/invoices.py`)

## What to generate

Read the target module at `$ARGUMENTS`. Identify all public functions, classes, and methods (skip private/dunder methods).

### Test file (`tests/test_<module_stem>.py`)

Generate a pytest file with comprehensive test coverage:

#### Fixtures (at the top)
- `db_session` — async SQLAlchemy session fixture using `AsyncSession` + test DB URL from env
- `client` — `httpx.AsyncClient` fixture wrapping the FastAPI `app` with `ASGITransport`
- Any model factory fixtures needed (e.g. `make_user`, `make_order`) using simple dict or ORM construction
- Fixtures should be reusable and avoid repetition

#### Test cases — for each public function / class method:

1. **Happy path** — valid inputs, assert expected return value or HTTP status + response shape
2. **Edge cases** — empty input, None, zero, empty list/dict, max length, boundary values
3. **Error cases** — invalid types, missing required fields, out-of-range values, assert specific exception types

#### For async functions
- Use `@pytest.mark.asyncio` decorator
- Use `pytest-asyncio` plugin

#### For FastAPI routes
- Use `TestClient` or `AsyncClient` from `httpx`
- Test all HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Assert both status code and response body shape

#### Mocking strategy
- Mock at the boundary — mock DB session, HTTP calls, file I/O
- Use `pytest-mock`'s `mocker` fixture for external dependencies
- Prefer real test-DB calls for internal DB functions
- Use `unittest.mock.AsyncMock` or `mocker.AsyncMock` for async external calls

#### Test organization
- Group tests in a class per function/route (e.g. `class TestCreateUser:`)
- Use `pytest.mark.parametrize` for functions with multiple input variations
- Each test function name: `test_<function>_<scenario>`
  - e.g., `test_create_user_returns_created_user`
  - e.g., `test_create_user_raises_if_email_exists`

#### Assertions
- Assert both return value AND side effects (DB calls, events fired)
- Use specific assertion messages for clarity

### conftest.py snippet (if needed)

If new fixtures are required beyond the standard `db_session` and `client`, generate a `conftest.py` snippet showing how to define them.

## Examples

### Example 1: Service module
```
/generate-test app/services/user_service.py
```
Generates: `tests/test_user_service.py`

### Example 2: Router module
```
/generate-test app/routers/orders.py
```
Generates: `tests/test_orders.py`

### Example 3: Utility module
```
/generate-test app/utils/email.py
```
Generates: `tests/test_email.py`

## Expected Output

After generation, print a summary:
```
✓ Generated tests/test_user_service.py
  - 12 test cases created
  - Functions covered: create_user, get_user, update_user, delete_user
  - Functions skipped: _validate_email (private), __init__ (dunder)
  - Fixtures: db_session, make_user
  - Async tests: 8 (marked with @pytest.mark.asyncio)
```

## Rules
- Follow `python-best-practices` skill if active
- All test functions must have type hints
- No broad `except Exception` — test for specific exception types
- Imports at top, no inline imports
- Use `pytest` fixtures for all shared setup — never repeat setup code
- Mock external dependencies, not internal functions
- Print a summary: number of tests generated, functions covered, functions skipped (if any)
