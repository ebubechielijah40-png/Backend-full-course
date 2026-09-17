# Lesson 1 — Models and Fields

## Why models

Week 3's `projects` page had project data hardcoded directly in the
view — fine for three items, unworkable for real content that changes
often and should be editable without touching code. A Django **model**
is a Python class that represents a database table: each attribute is a
column, each instance is a row.

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_at = models.DateField()
```

`CharField` needs a `max_length`; `TextField` is for longer text with no
length limit. This matters because Django uses the field type to decide
both the database column type and the validation applied to it.

**Task:** Add a `Post` model with `title`, `body`, and `published_at`
fields to a new `blog` app (created the same way as Week 3's `pages`
app).

**Common error:** forgetting `max_length` on a `CharField` raises
`TypeError: __init__() missing 1 required positional argument`.

## Checkpoint

Why is a model a better fit than a hardcoded Python list for blog posts
that change often? (Because the data can be added, edited, and deleted
without touching the code — the whole point of persistence, from
Week 1's file-based version, now backed by a real database.)
