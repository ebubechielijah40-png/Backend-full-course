# Lesson 1 — Django Project and App Structure, URLs, and Views

## Why a framework instead of the Week 2 server

Week 2's server worked, but you had to handle routing, headers, and
responses entirely by hand. **Django** is a web framework: it provides
routing, request/response objects, templates, and (from Week 4) a
database layer, so you focus on your application's logic instead of
re-solving problems every backend needs. Everything Django does under
the hood is the same request → response cycle from Week 2 — just with
far more built in.

## Creating a project and an app

A Django **project** is the overall configuration; an **app** is a
self-contained piece of functionality inside it (e.g. "blog," "accounts").
A project can contain several apps.

```
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject portfolio_site .
python3 manage.py startapp pages
```

Add `"pages"` to `INSTALLED_APPS` in `portfolio_site/settings.py` so
Django knows the app exists.

**Common error:** running `django-admin startproject` inside a folder
that already has files can create confusingly nested folders — run it in
an empty project directory, with the trailing `.` so Django doesn't
create an extra nested folder.

## URLs and views

A **view** is a function that takes a request and returns a response —
exactly Week 2's mental model. A **URL pattern** connects a path to a
view.

```python
# pages/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my portfolio")
```

```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

```python
# portfolio_site/urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
]
```

Run the development server and visit the page:

```
python3 manage.py runserver
```

**Task:** Add a second view, `about`, returning a short bio, routed at
`/about/`.

**Common error:** `404` on a URL you just added usually means the app's
`urls.py` wasn't included in the project's `urls.py`, or a typo in the
path string.

## Checkpoint

What's the difference between a Django project and a Django app?
(A project is the overall site configuration; an app is one
self-contained piece of functionality inside it.)

## Independent challenge

Add a third view and URL, `contact`, and confirm all three pages
(`/`, `/about/`, `/contact/`) load correctly.
