"""
ORM queries — Library Catalog
Week 6 project — Backend Development with Python & Django

Reproduces every query from Week 5's queries.sql using the Django ORM
instead of raw SQL, against the same sample data.

Run it with:
    python3 manage.py shell < orm_queries.py
"""

from catalog.models import Author, Book, Borrower, Loan

# --- Seed the same sample data as Week 5's schema.sql -----------------
Author.objects.all().delete()
Book.objects.all().delete()
Borrower.objects.all().delete()
Loan.objects.all().delete()

butler = Author.objects.create(name="Octavia Butler")
le_guin = Author.objects.create(name="Ursula K. Le Guin")

kindred = Book.objects.create(title="Kindred", author=butler, available=False)
parable = Book.objects.create(title="Parable of the Sower", author=butler, available=True)
left_hand = Book.objects.create(title="The Left Hand of Darkness", author=le_guin, available=True)

sam = Borrower.objects.create(name="Sam Rivera")
jordan = Borrower.objects.create(name="Jordan Lee")

Loan.objects.create(book=kindred, borrower=sam, loaned_on="2026-09-01")

print("\n--- Seed data created ---")

# 1. Every book with its author's name (JOIN)
print("\n1. Books with authors:")
for book in Book.objects.select_related("author").all():
    print(f"   {book.title} — {book.author.name}")

# 2. Only available books
print("\n2. Available books:")
for book in Book.objects.filter(available=True):
    print(f"   {book.title}")

# 3. All books by a specific author (JOIN + WHERE)
print("\n3. Books by Octavia Butler:")
for book in Book.objects.filter(author__name="Octavia Butler"):
    print(f"   {book.title}")

# 4. Every book currently on loan, with the borrower's name (3-table JOIN)
print("\n4. Active loans:")
for loan in Loan.objects.select_related("book", "borrower").all():
    print(f"   {loan.book.title} -> {loan.borrower.name} on {loan.loaned_on}")

# 5. Mark a book as unavailable (UPDATE)
parable.available = False
parable.save()
print(f"\n5. Marked '{parable.title}' unavailable: {not parable.available == True}")

# 6. Add a new loan (INSERT)
Loan.objects.create(book=parable, borrower=jordan, loaned_on="2026-09-10")
print("\n6. New loan added for Parable of the Sower -> Jordan Lee")

# 7. Return a book: delete its loan record and mark it available again
Loan.objects.filter(book=kindred, borrower=sam).delete()
kindred.available = True
kindred.save()
print("\n7. Kindred returned and marked available again")

# 8. Count how many books each author has written (JOIN + GROUP BY)
from django.db.models import Count
print("\n8. Book counts by author:")
for author in Author.objects.annotate(book_count=Count("books")):
    print(f"   {author.name}: {author.book_count}")

# Show the generated SQL for two queries, to compare against Week 5's SQL
print("\n--- Generated SQL (query 1) ---")
print(Book.objects.select_related("author").all().query)

print("\n--- Generated SQL (query 3) ---")
print(Book.objects.filter(author__name="Octavia Butler").query)
