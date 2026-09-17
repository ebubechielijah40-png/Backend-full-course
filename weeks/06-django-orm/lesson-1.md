# Lesson 1 — Connecting Django to PostgreSQL, Model Relationships

## Configuring a real database connection

By default, Django uses SQLite (a simple file-based database) — fine for
learning, but real projects use PostgreSQL. Update `DATABASES` in
`settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "library_catalog",
        "USER": "postgres",
        "PASSWORD": "yourpassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

You'll also need `pip install psycopg2-binary`, the PostgreSQL driver
Django uses underneath.

**Common error:** `django.db.utils.OperationalError: could not connect
to server` means either PostgreSQL isn't running, or the
host/port/credentials don't match your actual setup.

## Rebuilding the Week 5 schema as models

The exact schema from Week 5 becomes:

```python
# catalog/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=200)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loaned_on = models.DateField()
```

Notice this is the same relationships as the SQL schema — `author_id`
became `author = models.ForeignKey(Author, ...)`. `related_name="books"`
lets you go from an author back to their books as `author.books.all()`.

**Task:** Create these four models in a new `catalog` app, then run
`makemigrations` and `migrate`.

## Checkpoint

What SQL concept does Django's `ForeignKey` field correspond to
directly? (A foreign key column with a `REFERENCES` constraint.)
