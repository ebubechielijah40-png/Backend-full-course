from django.urls import path
from .api_views import (
    BookListCreateView, BookDetailView,
    AuthorListCreateView, AuthorDetailView,
    LoanListCreateView, LoanDetailView,
)

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListCreateView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("loans/", LoanListCreateView.as_view(), name="loan-list"),
    path("loans/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
]
