# Lesson 2 — Migrations and the Admin Site

## Migrations

A model is just a Python class until Django translates it into an
actual database table — that translation is a **migration**.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

`makemigrations` looks at your models and writes a migration file
describing the change; `migrate` applies it to the actual database.
Run both every time you add or change a model.

**Common error:** forgetting `makemigrations` before `migrate` means
Django has nothing new to apply — if a model change doesn't seem to take
effect, this is the first thing to check.

## The Django admin

Django ships with a ready-made admin site for managing model data,
enabled by registering a model:

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Create a superuser to log in, then visit `/admin/`:

```
python3 manage.py createsuperuser
```

This matters because it gives you (or a non-technical content owner) a
working interface to manage data with zero custom code — exactly the
kind of thing a framework should provide for free.

**Guided activity:** Register `Post`, create a superuser, and add two
posts through the admin interface.

**Task:** Add an `author` field to `Post` as a `ForeignKey` to Django's
built-in `User` model (`from django.contrib.auth.models import User`),
run the migration, and confirm the admin lets you pick an author when
creating a post.

**Common error:** adding a required `ForeignKey` to a model that already
has rows in the database will prompt you for a default value during
`makemigrations` — for a learning project this is fine to answer with a
placeholder, but it's worth understanding *why* Django asks (existing
rows need some value for the new required column).

## Checkpoint

What command turns a model change into an actual database update, and
in what order do you run the two migration commands? (`makemigrations`
then `migrate`.)
