# Project: Library Catalog (SQL)

## Problem
Students have only ever touched relational data through Django's admin
and ORM, which hides the actual SQL. They need direct, unhidden fluency
before trusting the ORM's abstraction in Week 6.

## Purpose
Build genuine SQL and relational-design skill, independent of Django.

## Requirements
- Design a schema of at least three related tables (e.g. `authors`,
  `books`, `borrowers`, with a borrowing/loan table linking books and
  borrowers).
- Correct primary and foreign keys.
- A required set of queries (provided in the lesson) covering `SELECT`,
  `WHERE`, `INSERT`, `UPDATE`, `DELETE`, and at least two multi-table
  `JOIN` queries.

## Features
Not applicable in the usual sense — this is a schema-plus-queries
project, not an application with a UI.

## Expected user behavior
Not applicable — this project is run directly against PostgreSQL via
`psql` or a SQL client, not through an interface.

## Database requirements
A real, running PostgreSQL database created for this project.

## Models / Relationships
Expressed as SQL `CREATE TABLE` statements with foreign key constraints,
not Django models — deliberately, to isolate the concept.

## API / Authentication / Validation requirements
Not applicable this week.

## Expected final result
A working schema populated with sample data, and correct results from
every required query.

## Difficulty
Moderate — new syntax, but concepts (tables/relationships) were already
seen informally via the Week 4 admin site.

## Estimated time
Spans all three Week 5 sessions.

## Prerequisite knowledge
General problem-solving; no Django knowledge is used or needed.

## Skills tested
Schema design, primary/foreign keys, `SELECT`/`INSERT`/`UPDATE`/`DELETE`,
multi-table `JOIN`s.

## How to run it

```
createdb library_catalog
psql library_catalog -f schema.sql
psql library_catalog -f queries.sql
```

## How to test it manually

Run each query in `queries.sql` individually (via `psql` or a GUI
client) and confirm the results match what the schema's sample data
implies — e.g. query 1 should show all three books with their correct
authors; query 4 should show exactly one active loan.

## Common errors

- `relation "authors" does not exist` — `schema.sql` wasn't run first,
  or was run against the wrong database.
- `insert or update on table "books" violates foreign key constraint` —
  an `author_id` was used that doesn't exist in `authors` yet; insert
  authors before books that reference them.

## Complete code

See `schema.sql` and `queries.sql` in this folder.
