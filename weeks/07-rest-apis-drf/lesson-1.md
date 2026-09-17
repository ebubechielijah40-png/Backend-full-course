# Lesson 1 — What REST Is, Installing DRF, Serializers

## What REST is, practically

A **REST API** exposes your data over HTTP using consistent conventions:
each resource (e.g. "books") has a URL, and the HTTP method (Week 2)
determines the action — GET to read, POST to create, PUT/PATCH to
update, DELETE to remove. This matters because it means a client (a
mobile app, a frontend, another service) can predict how your API
behaves without reading custom documentation for every single endpoint.

## Installing Django REST Framework

```
pip install djangorestframework
```

Add `"rest_framework"` to `INSTALLED_APPS`.

## Serializers

A **serializer** converts a model instance to JSON (for responses) and
JSON back into validated Python data (for incoming requests) — the API
equivalent of Django's forms, and the layer where Lesson 3's validation
lives.

```python
# catalog/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "available"]
```

`ModelSerializer` generates fields automatically from the model — this
matters because it avoids re-declaring every field by hand for the
common case.

**Task:** Write a `AuthorSerializer` for the `Author` model with `id`
and `name` fields.

**Common error:** forgetting to add a field to `fields` means it simply
won't appear in the API response or be accepted on input — not an error,
just silently missing, which is often more confusing than a crash.

## Checkpoint

What does a serializer do in each direction — model to JSON, and JSON to
model? (Converts a model instance into JSON for a response, and
validates and converts incoming JSON into Python data for creating or
updating a model instance.)
