# Week 7 — REST APIs with Django REST Framework

## What students already know

A working Django app with models and ORM fluency, using the Library
Catalog domain (Week 6).

## What they need to learn this week

- What REST is, at a practical level.
- Installing and configuring Django REST Framework (DRF).
- Serializers: converting model instances to/from JSON.
- List, retrieve, create, update, delete endpoints, one resource at a
  time.
- Input validation and correct status codes for success and failure.

## What they will build

The **Library Catalog API** — the same data from Weeks 5–6, now exposed
as a REST API instead of server-rendered pages.

## Concepts necessary to build it

Week 2's HTTP fluency (methods, status codes) and Week 6's ORM/model
fluency — both reused directly.

## What should NOT be taught yet

- Authentication and permissions (Week 8) — endpoints are open for now.
- DRF viewsets/routers — explicit `APIView`-based endpoints are used
  first so students see exactly what each endpoint does before any
  shortcut abstraction.

## What the three sessions accomplish

1. What REST is; installing DRF; writing serializers.
2. List, retrieve, create, update, delete endpoints.
3. Validation and error responses.

## What the project accomplishes

Turns an already-understood application into an API, connecting Week 2's
HTTP knowledge to a real, practical use.

## Practical skill at week's end

Can build a working CRUD REST API for a model with correct validation
and status codes.

---

**Status:** blueprint and project specification complete. Lessons not
yet written.
