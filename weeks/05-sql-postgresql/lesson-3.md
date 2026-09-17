# Lesson 3 — JOINs and Multi-Table Queries

## Why JOIN

`books.author_id` only stores a number — to see the author's actual
name alongside each book, you need to combine data from both tables.
That's what `JOIN` does.

```sql
SELECT books.title, authors.name
FROM books
JOIN authors ON books.author_id = authors.id;
```

This reads as: "combine each book with the author row whose `id`
matches the book's `author_id`."

**Task:** Fix the Lesson 2 debugging query using a join:
```sql
SELECT books.title
FROM books
JOIN authors ON books.author_id = authors.id
WHERE authors.name = 'Octavia Butler';
```

## Joining a third table

The Library Catalog project adds a `borrowers` table and a `loans` table
connecting borrowers to books:

```sql
CREATE TABLE borrowers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    borrower_id INTEGER REFERENCES borrowers(id),
    loaned_on DATE NOT NULL
);
```

A query spanning all three tables — "which borrower currently has each
book" — joins twice:

```sql
SELECT books.title, borrowers.name, loans.loaned_on
FROM loans
JOIN books ON loans.book_id = books.id
JOIN borrowers ON loans.borrower_id = borrowers.id;
```

**Common error:** joining on the wrong columns (e.g. `books.id =
borrowers.id`, which are unrelated) produces rows that look plausible
but are meaningless — always join on the actual foreign key
relationship, not just any two ID columns.

## Checkpoint

In plain English, what does `JOIN books ON loans.book_id = books.id` do?
(It attaches each loan row to the specific book it refers to, by
matching the loan's `book_id` to that book's `id`.)

## Independent challenge

Using the three-table schema above, write a query listing every book
currently on loan, along with the borrower's name — see
`project/README.md` for the full required query set.
