---
name: review-module
description: Comprehensive code review with SOLID/design patterns/DRY/type safety scoring and ratings
usage: /review-module <file_path> [--module] [--scope path/to/module]
---

# Code Quality Review Module

Perform a thorough code review of the given file or module, covering SOLID principles, design patterns, DRY violations, error handling, type safety, and async correctness.

## Arguments
- `$ARGUMENTS` — path to file or module to review (e.g. `app/models/user.py` or `sample_app/`)
- `--module` — review entire module/directory instead of single file
- `--scope` — analyze violations across module scope (show duplications, patterns)

## Review process

Read the file(s) at `$ARGUMENTS` in full. Then produce a comprehensive review report with these sections:

---

## 📋 Review Report Sections

### 1. SOLID Principles Analysis

Score each principle on 0-10 scale:

#### **S — Single Responsibility Principle (SRP)**
- Each class has one reason to change
- Methods focused on single task
- Violations: God classes, mixed concerns, multiple responsibilities
- **Scoring:** 10 = each class has 1 clear responsibility; 0 = god class mixing everything

#### **O — Open/Closed Principle (OCP)**
- Classes open for extension, closed for modification
- Use inheritance/composition/strategy instead of editing code
- Violations: Long if/elif chains requiring edits for new behavior
- **Scoring:** 10 = extensible without source edits; 0 = must edit source for each new case

#### **L — Liskov Substitution Principle (LSP)**
- Derived classes usable in place of base class
- Subclass respects contracts of parent
- Violations: Subclass narrows interface, breaks expected behavior
- **Scoring:** 10 = all subtypes are true substitutes; 0 = subclass violates parent contract

#### **I — Interface Segregation Principle (ISP)**
- Clients depend on specific interfaces, not fat ones
- Don't force classes to implement unused methods
- Violations: Large interfaces with methods not all implementations need
- **Scoring:** 10 = focused interfaces; 0 = bloated interface with NotImplementedError in subclasses

#### **D — Dependency Inversion Principle (DIP)**
- Depend on abstractions, not concrete implementations
- Inject dependencies, don't create them internally
- Violations: Hard-coded concrete classes, global state, no injection
- **Scoring:** 10 = full DI with abstractions; 0 = hard-coded dependencies everywhere

**SOLID Summary:** Average score of 5 principles (0-10 each)
- **9-10:** Excellent architecture
- **7-8:** Good design, minor issues
- **5-6:** Adequate, refactoring needed
- **3-4:** Poor design, significant debt
- **0-2:** Anti-patterns throughout

---

### 2. Design Patterns Analysis

Identify patterns **used correctly**, **missing**, or **misused**:

#### Common Patterns to Audit:
- **Factory/Builder:** Creating complex objects
- **Repository:** Data access layer abstraction
- **Service:** Business logic encapsulation
- **Dependency Injection:** Passing dependencies vs. creating them
- **Strategy:** Behavior variations without if/elif chains
- **Observer:** Event handling or notifications
- **Decorator:** Cross-cutting concerns (logging, caching, auth)
- **Adapter:** Integrating incompatible interfaces

**Report format:**
```
✓ USED CORRECTLY: [Pattern] at <location> — <brief description>
✗ MISSING: [Pattern] should be used for <use case>
⚠ MISUSED: [Pattern] at <location> — problem description
```

---

### 3. DRY (Don't Repeat Yourself) Analysis

Detect code duplication:

#### DRY Violations to Flag:
- **Duplicated logic:** Same code in 2+ places
- **Duplicated validation:** Email checks, input validation
- **Duplicated queries:** Same SQL/ORM patterns
- **Duplicated error handling:** Identical try/except blocks
- **Duplicated formatting:** Multiple currency formatters, report builders
- **Duplicated constants:** Magic numbers/strings in multiple files

**Scoring (0-10):**
- **9-10:** No significant duplication
- **7-8:** Minimal duplication, mostly isolated
- **5-6:** Moderate duplication (2-3 copies of common patterns)
- **3-4:** Significant duplication (4+ copies), poor abstraction
- **0-2:** Severe duplication throughout codebase

**Report format:**
```
[DRY: HIGH] Duplicated email sending logic
Locations: models/user.py:36-45, services/order.py:26-35, services/order.py:66-75
Occurrences: 3 copies
Fix: Extract to EmailService class
```

---

### 4. Type Safety Analysis

#### Missing/Incorrect Types:
- Missing annotations (function args, return types, class attributes)
- Use of `Any` — flag every occurrence and suggest concrete type
- Incorrect or overly broad types
- Missing `Optional` / `Union` where `None` is possible
- Bare `dict`, `list` instead of `Dict[K,V]`, `List[T]`

**Scoring (0-10):**
- **9-10:** Full type coverage, no `Any`, generic types properly parameterized
- **7-8:** Most functions typed, occasional `Any` usage justified
- **5-6:** ~50% coverage, some loose typing
- **3-4:** Sparse typing, frequent `Any` usage
- **0-2:** No type hints, or all `Any`

**Report format:**
```
[TYPE: HIGH] Missing type annotations
File: models/user.py:15
Code: def create_user(self, name, email, password, role):
Fix: def create_user(self, name: str, email: str, password: str, role: str) -> bool:
```

---

### 5. Error Handling Analysis

#### Issues to Flag:
- Bare `except:` or `except Exception:` without re-raise or logging
- Swallowed exceptions (no log, no re-raise)
- Missing context managers for resources (files, connections, sockets)
- No `HTTPException` for expected failure cases (404, 403, 422)
- Inconsistent error response shapes
- No validation before unsafe operations

**Scoring (0-10):**
- **9-10:** All exceptions logged/handled, context managers used, validation present
- **7-8:** Most paths handled, occasional gaps
- **5-6:** Basic try/except, some swallowing
- **3-4:** Many bare excepts, silent failures
- **0-2:** Exception handling absent or broken

**Report format:**
```
[ERROR: CRITICAL] Bare except with swallowed exception
File: models/user.py:32
Code: except: pass
Fix: except sqlite3.Error as e:
     logger.error(f"Failed to create user: {e}")
     raise
```

---

### 6. Security & OWASP

- SQL injection (raw string interpolation in queries)
- Missing authorization checks (routes without auth `Depends`)
- Exposed secrets or credentials in code
- Unvalidated user input to filesystem/shell
- Weak cryptography (MD5, SHA1 for security)
- OWASP API Top 10: mass assignment, excessive data exposure, broken object-level authorization

---

### 7. FastAPI/Async Best Practices (if applicable)

- Sync DB calls inside `async def` (missing `await`)
- Blocking I/O in async context (file reads, `requests.*`, `time.sleep`)
- Missing `response_model` on routes
- Business logic in handlers (should be in services)
- N+1 queries
- Incorrect `asyncio.run()` usage inside event loop

---

## Output Format

### Issue Reports
For each issue found:
```
[SEVERITY: CRITICAL|HIGH|MEDIUM|LOW] <file>:<line> — <category> — <issue>
Code: <problematic code snippet>
Fix: <suggested fix>
```

### Summary Scorecard

```
╔════════════════════════════════════════════════════════════════╗
║                    CODE QUALITY SCORECARD                      ║
╠════════════════════════════════════════════════════════════════╣
║ SOLID Principles              [█████░░░░] 5.2/10  (Needs work) ║
║ Design Patterns               [███░░░░░░] 3/10    (Missing)    ║
║ DRY Code                      [██░░░░░░░] 2/10    (High dup)   ║
║ Type Safety                   [██████░░░] 6/10    (Gaps)       ║
║ Error Handling                [░░░░░░░░░] 1/10    (Critical)   ║
║ Security & OWASP              [███░░░░░░] 3/10    (Issues)     ║
╠════════════════════════════════════════════════════════════════╣
║ OVERALL RATING                [███░░░░░░] 3.5/10  🔴 BLOCK     ║
╚════════════════════════════════════════════════════════════════╝

Detailed Breakdown:
| Category | Score | Issues | Severity |
|----------|-------|--------|----------|
| SOLID Principles | 5.2/10 | SRP ✗, OCP ✗, DIP ✗ | HIGH |
| Design Patterns | 3/10 | Missing: Repository, Service, Strategy | HIGH |
| DRY Violations | 2/10 | 3× email sending, 4× email validation | CRITICAL |
| Type Safety | 6/10 | 14+ missing annotations | HIGH |
| Error Handling | 1/10 | 6 bare excepts, 0 logging | CRITICAL |
| Security | 3/10 | Weak crypto (MD5), hardcoded secrets | CRITICAL |
```

### Violations Summary
| Category | Total | Unresolved |
|----------|-------|-----------|
| Type Safety Issues | 14 | 14 |
| DRY Violations | 8 | 8 |
| Error Handling | 6 | 6 |
| SOLID Violations | 4 | 4 |
| Design Pattern Gaps | 5 | 5 |
| Security Issues | 3 | 3 |

### Approval Decision
- **🟢 APPROVE** — Score ≥8, <3 CRITICAL issues, all security passed
- **🟡 APPROVE WITH CAUTION** — Score 6-7, some MEDIUM issues, security OK
- **🔴 REQUEST CHANGES** — Score 4-5, multiple HIGH issues, some security
- **🚫 BLOCK** — Score <4, CRITICAL issues, security failures, or error handling broken

---

## Review Checklist

- [ ] SOLID principles scored (S/O/L/I/D)
- [ ] Design patterns identified (used/missing/misused)
- [ ] DRY violations detected with locations
- [ ] Type safety gaps listed with line numbers
- [ ] Error handling reviewed (logging, specificity, re-raise)
- [ ] Security issues flagged (crypto, secrets, injection, auth)
- [ ] Async correctness verified (if applicable)
- [ ] Overall score calculated
- [ ] Approval decision stated with justification
