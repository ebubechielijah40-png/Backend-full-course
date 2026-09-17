# Week 6 — Django ORM

## What students already know

Direct SQL fluency against a real schema (Week 5) and basic Django
models/migrations (Week 4).

## What they need to learn this week

- Connecting Django to PostgreSQL for real.
- `ForeignKey` and `ManyToManyField` in depth.
- ORM CRUD operations and `QuerySet` filtering.
- `select_related` / `prefetch_related` at an introductory level.
- Reading the SQL a given ORM query produces.

## What they will build

The **Library Catalog**, rebuilt as Django models against a real
PostgreSQL database, queried through the ORM instead of raw SQL.

## Concepts necessary to build it

Week 5's schema and relational thinking (reused directly — same domain,
same tables) plus Week 4's model/migration basics.

## What should NOT be taught yet

- REST APIs (Week 7).
- Query optimization beyond `select_related`/`prefetch_related` (raw SQL
  escape hatches, query plan analysis) — out of scope for this course.

## What the three sessions accomplish

1. Connecting Django to PostgreSQL; modeling the Week 5 relationships.
2. ORM CRUD and filtering.
3. Related queries and reading generated SQL.

## What the project accomplishes

Directly connects SQL (Week 5) to the Django ORM by rebuilding the exact
same schema, so the translation is concrete, not abstract.

## Practical skill at week's end

Can model a relational problem in Django and perform correct
related-data queries through the ORM.

---

**Status:** blueprint and project specification complete. Lessons not
yet written.
