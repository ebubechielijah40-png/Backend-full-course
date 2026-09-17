# Lesson 3 — Permissions and Object-Level Access Control

## Requiring authentication for write operations

```python
from rest_framework.permissions import IsAuthenticated

class LoanListCreateView(APIView):
    def get(self, request):
        ...  # open to everyone

    def post(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        ...
```

More commonly, set `permission_classes` at the class level and only
require it where it matters, or check `request.user.is_authenticated`
directly inside a method for finer control per HTTP method.

## Object-level (ownership) permissions

Authentication alone doesn't stop User B from editing User A's loan —
you need an explicit ownership check:

```python
class LoanDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        loan = get_object_or_404(Loan, pk=pk)
        if loan.borrower.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

This matters because "logged in" and "allowed to touch this specific
record" are different checks — skipping the second is one of the most
common real-world API security mistakes (see Week 11).

**Debugging activity:** An API correctly requires login to delete a
loan, but any logged-in user can delete *any* loan, not just their own.
What check is missing? (An ownership comparison — the view checks
`IsAuthenticated` but never compares `loan.borrower.user` to
`request.user`.)

## Checkpoint

What's the difference between a `401` and a `403` response?
(`401` means "you're not authenticated at all"; `403` means "you're
authenticated, but not allowed to do this specific thing.")

## Independent challenge

Finish "Library Catalog API + Accounts" (see `project/README.md`):
registration, login, and loan endpoints where a user can only view and
manage their own loans.
