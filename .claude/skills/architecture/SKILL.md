---
name: architecture
description: "Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Architecture Decision Framework

> "Requirements drive architecture. Trade-offs inform decisions. ADRs capture rationale."

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `context-discovery.md` | Questions to ask, project classification | Starting architecture design |
| `trade-off-analysis.md` | ADR templates, trade-off framework | Documenting decisions |
| `pattern-selection.md` | Decision trees, anti-patterns | Choosing patterns |
| `examples.md` | MVP, SaaS, Enterprise examples | Reference implementations |
| `patterns-reference.md` | Quick lookup for patterns | Pattern comparison |

---

## 🔗 Related Skills

| Skill | Use For |
|-------|---------|
| `@[skills/database-design]` | Database schema design |
| `@[skills/api-patterns]` | API design patterns |
| `@[skills/deployment-procedures]` | Deployment architecture |

---

## Core Principle

**"Simplicity is the ultimate sophistication."**

- Start simple
- Add complexity ONLY when proven necessary
- You can always add patterns later
- Removing complexity is MUCH harder than adding it

---

## Validation Checklist

Before finalizing architecture:

- [ ] Requirements clearly understood
- [ ] Constraints identified
- [ ] Each decision has trade-off analysis
- [ ] Simpler alternatives considered
- [ ] ADRs written for significant decisions
- [ ] Team expertise matches chosen patterns

## When to Use This Skill

- Making significant architecture decisions (SQL vs NoSQL, monolith vs microservices)
- Evaluating trade-offs between design options
- Documenting decisions with Architecture Decision Records (ADRs)
- Analyzing system design and scalability
- Planning technical direction for a feature/system

## When NOT to Use This Skill

- Writing code (use pattern skills instead)
- Simple bug fixes or refactoring
- Minor implementation details
- UI/UX design decisions

## Keywords That Should Trigger This Skill

- "architecture decision", "ADR", "architectural"
- "trade-off", "design choice"
- "scalability", "system design"
- "monolith", "microservices", "event-driven"
- "database choice", "SQL vs NoSQL"
