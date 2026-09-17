# Week 4 — Django Models and Admin

## What students already know

A working multi-page Django site (Week 3): project/app structure, URLs,
views, templates.

## What they need to learn this week

- Model classes and field types.
- Migrations: generating and applying them.
- The Django admin site: registering and managing models.
- Rendering model data (querysets) inside templates.
- `ForeignKey` at a descriptive level only ("a post has one author") —
  full relationship querying is deferred to Week 6, after SQL (Week 5).

## What they will build

Turns the Week 3 site into a database-backed **Blog**: posts stored as
model instances, managed through the Django admin, and rendered on the
site's pages.

## Concepts necessary to build it

Week 3's routing/views/templates — this week is additive to that project,
not a new one.

## What should NOT be taught yet

- SQL syntax directly (Week 5) — the admin and ORM basics here are used
  without students needing to see raw SQL yet.
- Multi-table relationship queries (Week 6) — one simple `ForeignKey`
  (post → author) is enough this week.
- REST APIs.

## What the three sessions accomplish

1. Models and fields.
2. Migrations and the admin site.
3. Rendering model data in templates.

## What the project accomplishes

Gives students their first real, persistent, database-backed web
application.

## Practical skill at week's end

Can design a simple model, migrate it, manage its data through the
admin, and display it on a page.

---

**Status:** blueprint and project specification complete. Lessons not
yet written.
