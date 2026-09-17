# Lesson 2 — List, Retrieve, Create, Update, Delete Endpoints

## Explicit APIView endpoints

DRF's `APIView` gives you direct control over each HTTP method on an
endpoint — used here instead of viewsets/routers so every endpoint's
behavior is visible, not generated:

```python
# catalog/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return Response(BookSerializer(book).data)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```python
# catalog/api_urls.py
from django.urls import path
from .api_views import BookListCreateView, BookDetailView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
```

Notice `many=True` on the list serializer, versus a single instance on
the detail serializer — a common early mistake is forgetting `many=True`
and getting a confusing serialization error on a queryset.

**Task:** Write the equivalent `AuthorListCreateView` and
`AuthorDetailView`.

**Common error:** `Book.objects.get(pk=pk)` raises
`Book.DoesNotExist` (an unhandled 500 error) if the ID doesn't exist —
Lesson 3 fixes this with proper error handling.

## Checkpoint

Why does `POST` return `201 Created` while `GET` returns `200 OK`?
(`201` specifically communicates that a new resource was created, which
is more informative to a client than a generic success code.)
