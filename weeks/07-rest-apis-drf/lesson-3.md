# Lesson 3 — Validation and Error Responses

## Handling a missing object correctly

Use `get_object_or_404` (from Week 4) — DRF understands it and converts
it into a proper JSON `404` response instead of a crash:

```python
from django.shortcuts import get_object_or_404

class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return Response(BookSerializer(book).data)
```

## Validation

`serializer.is_valid()` checks incoming data against the model's field
rules (required fields, types, lengths) automatically. Add custom checks
with a `validate_<field>` method:

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "available"]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank")
        return value
```

When validation fails, `serializer.errors` gives a clear, field-by-field
JSON error response — this matters because a client needs to know
*which* field was wrong, not just that something was.

**Debugging activity:** A `POST` to `/books/` with `{"title": "", "author":
1}` returns `201 Created` with an empty title saved. What's missing?
(The view isn't checking `serializer.is_valid()` before saving, or the
serializer has no validation on `title` at all — an empty `CharField` is
allowed by default unless `blank=False` is enforced or a custom
validator is added.)

## Checkpoint

What's the difference in meaning between a `400` and a `404` response?
(`400` means the client sent invalid data; `404` means the requested
resource doesn't exist at all.)

## Independent challenge

Finish the full Library Catalog API (see `project/README.md`): CRUD for
both `Book` and `Author`, with validation and correct status codes for
every case, tested with `curl`.
