# Lesson 2 — ORM CRUD and Filtering

## Create, read, update, delete

Using the Django shell (`python3 manage.py shell`):

```python
from catalog.models import Author, Book

# Create
author = Author.objects.create(name="Octavia Butler")
book = Book.objects.create(title="Kindred", author=author, available=False)

# Read
Book.objects.all()
Book.objects.get(id=1)
Book.objects.filter(available=True)

# Update
book.available = True
book.save()

# Delete
book.delete()
```

This matters because it's the exact same four operations as Week 5's SQL
— `INSERT`, `SELECT`, `UPDATE`, `DELETE` — just expressed in Python
instead.

**Task:** Reproduce Week 5's sample data (two authors, three books, two
borrowers, one loan) using ORM calls instead of SQL `INSERT` statements.

## Filtering

`QuerySet` filtering builds a `WHERE` clause:

```python
Book.objects.filter(available=True)
Book.objects.filter(author__name="Octavia Butler")
```

`author__name` (double underscore) reaches across the relationship —
this is the ORM equivalent of Week 5's `JOIN ... WHERE authors.name = ...`.

**Common error:** `Book.objects.get(available=True)` raises
`MultipleObjectsReturned` if more than one row matches — `.get()` is only
for fetching exactly one, known row (e.g. by `id`); use `.filter()` when
more than one result is possible.

## Checkpoint

What does the double-underscore in `author__name` let you do?
(Filter based on a field of a related model, without writing a manual
join.)
