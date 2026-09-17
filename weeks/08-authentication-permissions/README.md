# Week 8 — Authentication and Permissions

## What students already know

A working, open (unauthenticated) REST API for the Library Catalog
(Week 7).

## What they need to learn this week

- Django's built-in user model; registration and login.
- The difference between authentication and authorization.
- DRF authentication classes (token or session authentication).
- Permission classes and object-level, ownership-based access control.

## What they will build

**Library Catalog API + Accounts**: the same API from Week 7, now
requiring accounts, with users only able to modify their own records.

## Concepts necessary to build it

Week 7's API endpoints, extended rather than rebuilt.

## What should NOT be taught yet

- OAuth2, social login, or JWT — token/session authentication (built
  into DRF) is sufficient to teach the concept.
- The larger integration project (Week 9) — this week stays scoped to
  auth on the existing API.

## What the three sessions accomplish

1. User accounts, registration, login.
2. Token/session authentication in DRF.
3. Permissions and object-level access control.

## What the project accomplishes

Adds the single most common missing piece of a "toy" API — real access
control — to a project students already understand.

## Practical skill at week's end

Can add real authentication and per-user permissions to an existing API.

---

**Status:** blueprint and project specification complete. Lessons not
yet written.
