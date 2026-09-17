# Project: Task Manager API

## Problem
Students have only ever extended one application (the Library Catalog)
across several weeks. They need to prove they can start from a written
spec on a new domain and combine every skill themselves.

## Purpose
The first full independence checkpoint: build a complete, authenticated
CRUD backend from a spec, with reduced step-by-step guidance.

## Requirements (given to students as the written spec)
- Users can register and log in.
- A user can create, view, update, and delete their own tasks.
- Each task has a title, description, due date, and completion status.
- Tasks support an optional `category` (a related model, one-to-many
  from category to tasks).
- A user cannot see or modify another user's tasks.
- All endpoints return correct status codes and validation errors.

## Features
- Full CRUD for `Task` and `Category`.
- Filtering tasks by category and by completion status.
- Ownership-based permissions, as taught in Week 8.

## Expected user behavior
A registered user manages only their own tasks and categories through
the API; all other users' data is inaccessible to them.

## Database requirements
Two related tables: `Category` (one) to `Task` (many), plus `Task.owner`
→ `User`.

## Models / Relationships
`Task.category` (`ForeignKey`, nullable), `Task.owner` (`ForeignKey` to
`User`).

## API requirements
Full CRUD for both resources, following Week 7's conventions.

## Authentication requirements
Same as Week 8: required for write access, ownership-enforced.

## Validation requirements
Required fields, valid due-date format, valid category reference.

## Expected final result
A complete, working, authenticated Task Manager API, built primarily by
the student from the spec above.

## Difficulty
High relative to prior weeks — first time combining every skill on a new
domain with reduced guidance — but achievable, since no single skill is
new.

## Estimated time
Spans all three Week 9 sessions.

## Prerequisite knowledge
Everything from Weeks 3–8.

## Skills tested
Specification reading, model design, ORM usage, API design, auth and
permissions — combined, independently.

## How to run it

```
cd task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## How to test it manually

Register two users, log in as each, create categories and tasks as one
user, and confirm: the other user cannot see or modify them (`403`);
filtering by `?category=` and `?completed=true` both work; a blank
title or an invalid category ID returns `400`; unauthenticated access
returns `401`.

## Common errors

- `403` on your own task — check the `owner` field actually got set to
  `request.user` on creation (`serializer.save(owner=request.user)`),
  not left for the client to supply.
- Category filter returning nothing unexpectedly — remember
  `request.query_params.get("category")` returns a string; comparing it
  to an integer field works in Django's ORM automatically, but printing
  it while debugging will show a string, which can be confusing.

## Complete code

See the `task_manager/` folder in this directory — `tasks/` for the
core models/API, `accounts/` reused from Week 8 for registration/login.
