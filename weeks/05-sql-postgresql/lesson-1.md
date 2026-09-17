# Lesson 1 — Relational Databases and PostgreSQL Setup

## What a relational database is

A **relational database** stores data in tables (rows and columns), with
explicit relationships between tables via keys. This matters because
it's the standard, reliable way backend applications store structured
data that needs to stay consistent — Django's ORM (Week 6 onward) is
just a convenient way to generate the SQL this week teaches directly.

## Why step outside Django this week

Weeks 3–4 used the Django admin to manage data without seeing any SQL.
This week deliberately removes that convenience so you understand what's
actually happening underneath — the same reason Week 2 built a raw HTTP
server before trusting Django's routing.

## Setting up PostgreSQL

Install PostgreSQL for your OS, then create a database and connect to
it:

```
createdb library_catalog
psql library_catalog
```

**Common error:** `psql: error: connection to server ... failed` usually
means the PostgreSQL service isn't running — start it with your OS's
service manager (e.g. `brew services start postgresql` on macOS,
`sudo service postgresql start` on Linux).

## Primary and foreign keys, briefly

A **primary key** uniquely identifies a row in its own table (usually an
auto-incrementing `id`). A **foreign key** is a column in one table that
refers to a primary key in another, expressing a relationship (e.g. a
book's `author_id` refers to a row in the `authors` table).

## Checkpoint

Why does a foreign key matter, rather than just repeating the author's
name as text in every book row? (It avoids duplicating and potentially
mis-typing the same data repeatedly, and lets you change an author's
details in one place.)
