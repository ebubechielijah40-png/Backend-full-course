# Lesson 3 — Related Queries and Reading Generated SQL

## Traversing relationships

```python
# All books by a specific author
author = Author.objects.get(name="Octavia Butler")
author.books.all()

# All books currently on loan, with borrower info (like Week 5's 3-table JOIN)
from catalog.models import Loan
Loan.objects.select_related("book", "borrower").all()
```

`select_related` tells Django to fetch related rows in the same query
(a SQL `JOIN`) instead of a separate query per related object — this
matters for performance once there's real data, and it's the ORM
equivalent of the multi-table `JOIN` from Week 5.

`prefetch_related` does the equivalent for the "many" side of a
relationship (e.g. fetching an author along with *all* their books
efficiently):

```python
Author.objects.prefetch_related("books").all()
```

## Reading the generated SQL

You can see exactly what SQL a queryset produces:

```python
print(Book.objects.filter(available=True).query)
```

This matters because it turns the ORM from "trust it blindly" into
"verify what it's actually doing" — the same habit of not treating a
tool as magic that Week 2's raw HTTP server and Week 5's raw SQL both
built.

**Debugging activity:** A student's page is very slow once there are
many books. They're doing `for book in Book.objects.all(): print(book.
author.name)`. What's likely wrong? (Each loop iteration triggers a
*separate* query to fetch that book's author — called the "N+1 query
problem." Using `Book.objects.select_related("author")` fetches
everything in one query instead.)

## Checkpoint

When would you reach for `select_related` versus `prefetch_related`?
(`select_related` for a `ForeignKey`/one-to-one, where a SQL `JOIN`
fetches the related row directly; `prefetch_related` for the "many" side
of a relationship, fetched as a separate, optimized follow-up query.)

## Independent challenge

Rebuild every query from Week 5's `queries.sql` using the ORM instead —
see `project/README.md` — and for at least two of them, print
`.query` to confirm the generated SQL matches what you'd expect.
