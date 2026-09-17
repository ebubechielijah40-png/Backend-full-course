# Lesson 1 — User Accounts, Registration, Login

## Authentication vs. authorization

**Authentication** answers "who are you?" (logging in). **Authorization**
answers "are you allowed to do this?" (permissions). This distinction
matters because a user can be correctly authenticated (they proved who
they are) and still be denied a specific action — the two checks are
independent.

## Django's built-in User model

Django ships with a `User` model (`django.contrib.auth.models.User`)
covering username, password (hashed automatically), and email. Register
a user via the ORM, but never store a raw password directly:

```python
from django.contrib.auth.models import User
User.objects.create_user(username="sam", password="a-real-password")
```

`create_user` hashes the password; assigning `user.password = "..."`
directly would store it in plain text, which is a serious security
mistake covered further in Week 11.

## A registration endpoint

```python
# accounts/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                {"error": "username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "username already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        User.objects.create_user(username=username, password=password)
        return Response(status=status.HTTP_201_CREATED)
```

**Task:** Write this view, route it at `/api/register/`, and test it
with `curl`.

## Checkpoint

Why does `create_user` exist instead of just using `User.objects.create
(username=..., password=...)` directly? (`create_user` hashes the
password correctly; a direct `create()` call would store the raw
password as plain text.)
