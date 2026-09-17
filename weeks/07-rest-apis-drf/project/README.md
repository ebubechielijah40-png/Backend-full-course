# Project: Library Catalog API

## Problem
The Library Catalog only exists inside the Django shell/admin — nothing
else can talk to it.

## Purpose
Expose the same data as a real REST API, connecting Week 2's HTTP
knowledge to a practical, working use.

## Requirements
- DRF installed and configured.
- Serializers for `Author` and `Book` (at minimum).
- Endpoints: list and create (`/books/`), retrieve/update/delete
  (`/books/<id>/`), same pattern for `Author`.
- Input validation with clear error responses (e.g. missing required
  field, invalid type).

## Features
- Correct status codes: 200 (success), 201 (created), 400 (validation
  error), 404 (not found).
- Filtering the book list by author via a query parameter.

## Expected user behavior
A client (tested via `curl`/Postman/browser) can list, view, create,
update, and delete books and authors, and receives clear errors for bad
input.

## Database requirements
Same schema as Week 6.

## Models / Relationships
Reused directly from Week 6.

## API requirements
Full CRUD for `Book`, at least list/retrieve for `Author`.

## Authentication requirements
None yet — endpoints are open. Deferred to Week 8.

## Validation requirements
Required fields enforced; sensible error messages for invalid input.

## Expected final result
A working, testable REST API for the Library Catalog.

## Difficulty
Moderate — new framework (DRF) built on already-familiar models.

## Estimated time
Spans all three Week 7 sessions.

## Prerequisite knowledge
Week 6's models and ORM fluency; Week 2's HTTP fluency.

## Skills tested
Serialization, endpoint design, validation, status codes.

## How to run it

```
cd library_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## How to test it manually

```
curl -X POST http://localhost:8000/api/authors/ -H "Content-Type: application/json" -d '{"name": "Octavia Butler"}'
curl -X POST http://localhost:8000/api/books/ -H "Content-Type: application/json" -d '{"title": "Kindred", "author": 1, "available": true}'
curl http://localhost:8000/api/books/
curl http://localhost:8000/api/books/1/
curl "http://localhost:8000/api/books/?author=1"
curl -X PUT http://localhost:8000/api/books/1/ -H "Content-Type: application/json" -d '{"title": "Kindred", "author": 1, "available": false}'
curl -X DELETE http://localhost:8000/api/books/1/
```

Confirm: creation returns `201`, list/retrieve return `200`, a blank
title returns `400` with a clear error, a nonexistent book returns
`404`, and delete returns `204`.

## Common errors

- `Book.DoesNotExist` unhandled (500 error) — check the view uses
  `get_object_or_404`, not a bare `Book.objects.get(pk=pk)`.
- `django.core.exceptions.ImproperlyConfigured` mentioning
  `rest_framework` — confirm it's installed and listed in
  `INSTALLED_APPS`.

## Complete code

See `library_api/catalog/serializers.py`, `api_views.py`, and
`api_urls.py`.
