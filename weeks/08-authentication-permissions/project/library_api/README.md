# Project: Library Catalog (Django ORM)

## Problem
Students can now write SQL directly (Week 5) but haven't yet connected
that skill back to Django, where they'll actually work day to day.

## Purpose
Rebuild the exact same schema and queries from Week 5 as Django models
and ORM calls, making the translation concrete rather than abstract.

## Requirements
- Django models matching the Week 5 schema (`Author`, `Book`,
  `Borrower`, a loan-tracking model or `ManyToManyField` as appropriate).
- Migrations applied against a real PostgreSQL database.
- ORM equivalents of every required Week 5 query, including at least two
  queries using `select_related`/`prefetch_related` across the
  relationship.

## Features
- Create, read, update, and delete for each model via the ORM (in a
  script or Django shell — no API yet, that's Week 7).
- At least one query that traverses the relationship (e.g. "all books
  currently borrowed by a given borrower").

## Expected user behavior
Not applicable — interacted with via the Django shell/scripts, not a UI.

## Database requirements
Same schema as Week 5, now Django-managed.

## Models / Relationships
`Book.author` (`ForeignKey`), plus a loan/borrowing relationship
expressed as either a `ManyToManyField` with a through-model or a
separate `Loan` model with two `ForeignKey`s — instructor's choice based
on what best matches the Week 5 schema used.

## API / Authentication / Validation requirements
Not applicable this week — deferred to Week 7.

## Expected final result
Every Week 5 SQL query has a working ORM equivalent, and the student can
show the generated SQL for each to confirm they match.

## Difficulty
Moderate — mostly translation of already-understood concepts into new
syntax.

## Estimated time
Spans all three Week 6 sessions.

## Prerequisite knowledge
Week 5's schema and SQL fluency; Week 4's model/migration basics.

## Skills tested
Model relationships, ORM CRUD, related-data queries, reading generated
SQL.

## How to run it

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py shell < orm_queries.py
```

(This project uses SQLite by default for simplicity; switch
`DATABASES` in `library_project/settings.py` to PostgreSQL, per
Lesson 1, to match the production setup used from here on.)

## How to test it manually

Run `orm_queries.py` and confirm its output matches Week 5's
`queries.sql` results for the same sample data (same books, same
authors, same active loan).

## Common errors

- `django.db.utils.OperationalError` when switching to PostgreSQL —
  check the database exists (`createdb library_catalog`) and the
  credentials in `settings.py` are correct.

## Complete code

See the `library_project/` and `catalog/` folders, plus
`orm_queries.py`, in this directory.
