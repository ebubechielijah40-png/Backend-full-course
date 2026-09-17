# Project: Library Catalog API + Accounts

## Problem
The Week 7 API is open to anyone — there's no concept of who owns what,
which is unrealistic for any real application.

## Purpose
Add real authentication and ownership-based permissions to an API
students already understand.

## Requirements
- User registration and login endpoints.
- Token or session authentication (DRF built-in) required for write
  operations.
- A borrower-facing feature (e.g. "my loans") scoped to the logged-in
  user only.
- Permission checks preventing a user from modifying another user's
  records.

## Features
- Registration, login, and "who am I" endpoints.
- Write operations (create/update/delete) require authentication.
- Read operations may remain public, per instructor's choice, matching
  the Library Catalog's real-world behavior (anyone can browse, only
  logged-in users manage loans).

## Expected user behavior
An anonymous user can browse the catalog; a logged-in user can manage
only their own loan records; attempts to modify another user's record
are rejected with a 403.

## Database requirements
Adds a relationship between `User` and the loan-tracking model from
Week 6, if not already present.

## Models / Relationships
`Loan.borrower` → `User`.

## API requirements
Reuses Week 7's endpoints; adds auth-required variants for
loan-management endpoints.

## Authentication requirements
DRF token or session authentication; ownership-based permission class.

## Validation requirements
Reused from Week 7; extended to reject actions on records the user
doesn't own.

## Expected final result
A working API where authentication and per-user permissions are
enforced correctly and verifiably.

## Difficulty
Moderate — one new concept (auth/permissions) added to a known base.

## Estimated time
Spans all three Week 8 sessions.

## Prerequisite knowledge
Week 7's full API.

## Skills tested
Authentication setup, permission classes, ownership checks.

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
curl -X POST http://localhost:8000/api/register/ -d "username=sam&password=SamPass123"
curl -X POST http://localhost:8000/api/login/ -d "username=sam&password=SamPass123"
# use the returned token:
curl http://localhost:8000/api/loans/ -H "Authorization: Token <token>"
curl -X POST http://localhost:8000/api/loans/ -H "Authorization: Token <token>" -H "Content-Type: application/json" -d '{"book": 1, "loaned_on": "2026-09-01"}'
```

Confirm: an unauthenticated loan request returns `401`; a user only ever
sees their own loans on `GET /api/loans/`; deleting another user's loan
returns `403`; deleting your own returns `204`.

## Common errors

- `ImportError` mentioning `rest_framework.authtoken.authentication` —
  in current DRF versions, `TokenAuthentication` lives in
  `rest_framework.authentication`, not the `authtoken` subpackage; check
  your installed DRF version's docs if this changes again.
- `AttributeError: 'User' object has no attribute 'borrower'` — the
  user has no linked `Borrower` row; this is created automatically by
  `RegisterView`, so this usually means a user was created some other
  way (e.g. `createsuperuser`).

## Complete code

See `library_api/accounts/` and the loan-related additions in
`library_api/catalog/`.
