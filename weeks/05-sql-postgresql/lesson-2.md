# Lesson 2 — SELECT, WHERE, INSERT, UPDATE, DELETE

## Creating a table

```sql
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER REFERENCES authors(id),
    available BOOLEAN DEFAULT TRUE
);
```

`SERIAL PRIMARY KEY` auto-generates a unique, increasing ID.
`REFERENCES authors(id)` makes `author_id` a foreign key, so the
database itself rejects a book referencing an author that doesn't exist.

## INSERT

```sql
INSERT INTO authors (name) VALUES ('Octavia Butler');
INSERT INTO books (title, author_id) VALUES ('Kindred', 1);
```

## SELECT and WHERE

```sql
SELECT * FROM books;
SELECT title FROM books WHERE available = TRUE;
SELECT * FROM books WHERE author_id = 1;
```

`WHERE` filters rows — this matters because without it, every query
returns the entire table, which is rarely what you want once a table has
real amounts of data.

**Task:** Write a query returning only books published by author ID 1
that are currently available.

## UPDATE and DELETE

```sql
UPDATE books SET available = FALSE WHERE id = 1;
DELETE FROM books WHERE id = 1;
```

**Common error:** running `UPDATE` or `DELETE` without a `WHERE` clause
changes or removes *every* row in the table — always double-check the
`WHERE` clause before running either, especially against real data.

**Debugging activity:** This query is meant to find books by "Octavia
Butler" but returns nothing — find the bug:
```sql
SELECT * FROM books WHERE author_id = 'Octavia Butler';
```
(The bug: `author_id` is a numeric foreign key, not the author's name —
this query needs to join against `authors` and filter on `name`, which
Lesson 3 covers.)

## Checkpoint

What's the risk of running `DELETE FROM books;` with no `WHERE` clause?
(It deletes every row in the table, not just one.)
