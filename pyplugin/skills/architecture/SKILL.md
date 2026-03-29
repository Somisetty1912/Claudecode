---
name: architecture
description: "Comprehensive architecture skill for system design, decisions, patterns (Clean, Hexagonal, DDD), ADRs, and architectural reviews. Use when designing systems, making tech decisions, or analyzing architecture."
---

# Architecture: Design, Decisions & Patterns

Master comprehensive system design covering decision-making, proven patterns (Clean Architecture, Hexagonal, Domain-Driven Design), Architecture Decision Records (ADRs), and architectural reviews.

## When to Use This Skill

- Making significant architecture decisions (monolith vs microservices, SQL vs NoSQL, event-driven)
- Evaluating trade-offs between design options
- Designing new systems or refactoring existing ones
- Documenting decisions with Architecture Decision Records (ADRs)
- Reviewing system architecture for scalability, maintainability, security
- Establishing architecture standards and patterns for teams
- Analyzing distributed systems, microservices boundaries, data flow

## When NOT to Use This Skill

- Writing implementation code (use language/framework skills instead)
- Simple bug fixes or localized refactoring
- Minor implementation details
- Single-file or single-component changes

---

## Core Principle

**"Simplicity is the ultimate sophistication."**

- Start simple; add complexity only when proven necessary
- You can always add patterns later
- Removing complexity is much harder than adding it
- Choose patterns that fit your team's expertise

---

## Part 1: Architecture Decision-Making

### Discovery Phase

Before choosing architecture, understand:

1. **Functional Requirements**
   - What does the system do?
   - Who are the users?
   - What are the core workflows?

2. **Non-Functional Requirements**
   - Scale: users, transactions, data volume
   - Performance: latency, throughput targets
   - Availability: uptime, failover needs
   - Security: compliance, sensitive data
   - Maintainability: team size, skill level

3. **Constraints**
   - Timeline and budget
   - Existing infrastructure
   - Team expertise
   - Organizational boundaries

### Trade-Off Analysis Framework

Every architecture decision involves trade-offs. Document them:

```
Decision: Should we use microservices or monolith?

Option A: Monolith
Pros: Simple to develop, single deployment, easier debugging, lower ops overhead
Cons: Tight coupling, scaling limitations, technology lock-in, deploys affect all features

Option B: Microservices
Pros: Independent scaling, technology diversity, parallel development, fault isolation
Cons: Network complexity, eventual consistency, harder debugging, DevOps overhead

Our Choice: Monolith (for now)
Why: Team of 5, new product, simpler to iterate. Can decompose to microservices later.
```

**Key Decision Criteria:**
- Reversibility: Can we change this later?
- Team fit: Does our team have expertise?
- Operational burden: Can we maintain it?
- Business impact: How does it affect time-to-market?

---

## Part 2: Architecture Patterns

### Clean Architecture (Uncle Bob)

Layers with dependency flowing inward (inner layers don't depend on outer):

```
┌────────────────────────────────┐
│  Frameworks & Drivers (UI, DB) │
├────────────────────────────────┤
│  Interface Adapters            │
│  (Controllers, Repositories)   │
├────────────────────────────────┤
│  Application Business Rules    │
│  (Use Cases, Services)         │
├────────────────────────────────┤
│  Entities (Core Business Logic)│
└────────────────────────────────┘
```

**Benefits:**
- Testable without frameworks
- Business logic independent of technology
- Easy to swap implementations (mock for testing)

**Example Structure:**
```
app/
├── domain/           # Entities, business rules
├── use_cases/        # Application workflows
├── adapters/         # Repositories, controllers
└── infrastructure/   # Database, config, logging
```

### Hexagonal Architecture (Ports & Adapters)

Core domain surrounded by ports (interfaces) and adapters (implementations).

```
┌──────────────────────────────────┐
│   Adapters (HTTP, Queue, etc)   │
├──────────────────────────────────┤
│  Ports (Interfaces)              │
├──────────────────────────────────┤
│  Domain Core (Business Logic)    │
├──────────────────────────────────┤
│  Ports (Interfaces)              │
├──────────────────────────────────┤
│   Adapters (DB, Email, etc)     │
└──────────────────────────────────┘
```

**Benefits:**
- Technology-agnostic core
- Swap implementations for testing
- Clear input/output boundaries

### Domain-Driven Design (DDD)

Organize around business domains, not technical layers.

**Strategic:**
- **Bounded Contexts**: Separate models for different domains
- **Ubiquitous Language**: Shared terminology with business
- **Context Mapping**: How domains relate

**Tactical:**
- **Entities**: Objects with identity (User, Order)
- **Value Objects**: Immutable, defined by attributes (Email, Money)
- **Aggregates**: Consistency boundaries (Order aggregate includes OrderItem)
- **Repositories**: Data access abstraction per aggregate
- **Domain Events**: Things that happened (OrderCreated, PaymentProcessed)

---

## Part 3: Architecture Decision Records (ADRs)

### Why Write ADRs?

ADRs capture the "why" behind decisions, helping future developers understand context without meeting you.

### When to Write an ADR

| Write ADR | Skip ADR |
|-----------|----------|
| New framework adoption | Minor version upgrades |
| Database technology choice | Bug fixes |
| API design approach | Implementation details |
| Security architecture | Configuration tweaks |
| Integration patterns | Routine maintenance |

### ADR Template (Minimal)

```markdown
# ADR-001: Use PostgreSQL for Primary Database

## Status
Accepted

## Context
System needs to store orders with strong consistency requirements. Team has PostgreSQL expertise.

## Decision
Use PostgreSQL 15 with async connection pooling.

## Consequences
**Positive:** ACID transactions, team familiar, mature ecosystem
**Negative:** Vertical scaling limits, need PgBouncer for connection pooling

## Related Decisions
- ADR-002: Redis for caching (complements this)
- ADR-005: Search architecture (may change if full-text search inadequate)
```

### ADR Lifecycle

```
Proposed → Accepted → Deprecated → Superseded
             ↓
          Rejected
```

Use `Supersedes` when decisions change:
```
ADR-020: Deprecate MongoDB in Favor of PostgreSQL (Supersedes ADR-003)
```

---

## Part 4: Architectural Review

### Review Checklist

When reviewing architecture (yours or others'):

**Quality Attributes**
- [ ] Scalability: Can it handle 10x load? 100x?
- [ ] Reliability: How do failures cascade?
- [ ] Maintainability: Can a new team member understand it?
- [ ] Security: What are the attack surfaces?
- [ ] Testability: Can we test critical paths in isolation?

**Design Principles**
- [ ] Single Responsibility: Each component has one reason to change
- [ ] Loose Coupling: Components can change independently
- [ ] High Cohesion: Related functionality grouped together
- [ ] DRY: No duplication of business logic
- [ ] No overengineering: Complexity justified

**Distributed Systems**
- [ ] Service boundaries clear: Each service has well-defined responsibility
- [ ] Data consistency strategy: Chosen pattern (strong/eventual)
- [ ] Resilience: Circuit breakers, timeouts, retries documented
- [ ] Monitoring: Observable (logs, metrics, traces)

**Technology Fit**
- [ ] Team expertise: Can the team build and maintain this?
- [ ] Ecosystem: Good tooling, active community?
- [ ] Maturity: Stable or cutting-edge? Acceptable risk level?

### Red Flags

⚠️ **Common Architecture Smells:**
- "We'll refactor this later" (rarely happens)
- Tight coupling between services (defeats microservice benefit)
- No circuit breakers in distributed calls (cascading failures)
- Database per microservice with shared tables (data coupling)
- Mixing concerns in single layer (authentication in business logic)
- No observability (metrics, logs, traces) planned upfront

---

## Part 5: Pattern Selection Decision Tree

```
Does the system have complex business logic?
├─ NO → Start with simple monolith (Layered Architecture)
└─ YES → Does it span multiple domains?
   ├─ NO → Monolith with Clean Architecture
   └─ YES → Will teams work independently?
      ├─ NO → Modular monolith (packages with clear boundaries)
      └─ YES → Microservices (with caution!)

Microservices? Verify:
✓ Team can manage operational complexity (logging, tracing, deployment)
✓ Service boundaries are clear (not shared tables, loose coupling)
✓ Benefits (independent scaling, deployment, teams) outweigh overhead
```

---

## Part 6: Common Architecture Patterns Reference

| Pattern | Use When | Challenges |
|---------|----------|-----------|
| **Layered (3-tier)** | Simple CRUD apps | Tight coupling, scaling limits |
| **Clean/Hexagonal** | Complex logic, testability important | More files, learning curve |
| **Event-Driven** | Real-time, decoupling, event audit needed | Eventual consistency, debugging |
| **CQRS** | Complex queries different from writes | Schema duplication, consistency |
| **Saga** | Distributed transactions across services | Compensating transactions complex |
| **Database per Service** | Service independence | Distributed transactions harder |

---

## Best Practices

### Do's
- **Write ADRs early** — Before implementation starts
- **Question assumptions** — Why this pattern? Can simpler work?
- **Involve the team** — Architecture is a team decision
- **Plan for evolution** — Systems change; plan for it
- **Document trade-offs** — Honest pros/cons help future decisions

### Don'ts
- **Don't over-engineer** — Complexity you don't need
- **Don't change accepted ADRs** — Supersede with new ones
- **Don't hide failures** — Rejected decisions are valuable data
- **Don't assume expertise** — Teach the team, don't assume knowledge
- **Don't skip monitoring** — Unobservable systems are disasters

---

## Related Skills

Works well with:
- `@python-best-practices` — Implementation standards
- `@fastapi-patterns` — API design
- `@sqlalchemy-patterns` — Database patterns
- `@backend-patterns` — Integration patterns
- For code review: `@bug-hunter`
