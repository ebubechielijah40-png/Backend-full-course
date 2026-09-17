# Lesson 2 — Token Authentication in DRF

## Enabling token authentication

```python
# settings.py
INSTALLED_APPS += ["rest_framework.authtoken"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}
```

Run `migrate` again (this adds a token table). Each user gets a token
that acts like a password substitute for API requests — the client
sends it in an `Authorization` header instead of logging in with a
session every time.

## A login endpoint

DRF ships a ready-made view for exchanging credentials for a token:

```python
# accounts/api_urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
]
```

```
curl -X POST http://localhost:8000/api/login/ -d "username=sam&password=a-real-password"
# {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}
```

The client stores this token and sends it on future requests:

```
curl http://localhost:8000/api/loans/ -H "Authorization: Token 9944b09..."
```

**Common error:** `401 Unauthorized` on an authenticated endpoint
usually means the `Authorization` header is missing, misspelled (it must
be exactly `Token <value>`, not `Bearer <value>` for DRF's default token
auth), or the token itself is wrong.

## Checkpoint

Why does the client send a token instead of the username and password on
every request? (So the actual password is only ever transmitted once, at
login — the token can be revoked independently without changing the
password.)
