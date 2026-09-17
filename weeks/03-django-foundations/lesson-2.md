# Lesson 2 — Templates and Dynamic HTML

## Why templates instead of `HttpResponse` strings

Returning raw HTML strings from a view doesn't scale — real pages are
long, and mixing HTML with Python logic gets unreadable fast. Django's
**template** system lets you write HTML in its own file, with small bits
of dynamic logic and variables inserted where needed.

```python
# pages/views.py
from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {"name": "Eli"})
```

```html
<!-- pages/templates/pages/home.html -->
<h1>Welcome, {{ name }}</h1>
```

`{{ name }}` inserts the `name` variable passed from the view. This
matters because it separates *what the page contains* (the view's data)
from *how it looks* (the template's HTML).

**Common error:** `TemplateDoesNotExist` almost always means the
template file is in the wrong folder — Django looks inside
`<app>/templates/<app>/` by convention; double-check the path matches
exactly.

## Template inheritance

Repeating the same header/footer HTML in every template is exactly the
kind of repetition functions solved for Python code in Week 1 —
templates solve it with **inheritance**:

```html
<!-- pages/templates/pages/base.html -->
<html>
<body>
  <nav><a href="/">Home</a> | <a href="/about/">About</a></nav>
  {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- pages/templates/pages/home.html -->
{% extends "pages/base.html" %}
{% block content %}
  <h1>Welcome, {{ name }}</h1>
{% endblock %}
```

**Guided activity:** Convert your `about` and `contact` templates to
extend `base.html` the same way.

## Passing lists of data

A view can pass any Python data structure, including a list of
dictionaries — the exact shape from Week 1's expense tracker — and a
template can loop over it:

```python
def projects(request):
    project_list = [
        {"title": "Expense Tracker", "year": 2026},
        {"title": "Request Inspector", "year": 2026},
    ]
    return render(request, "pages/projects.html", {"projects": project_list})
```

```html
{% for project in projects %}
  <li>{{ project.title }} ({{ project.year }})</li>
{% endfor %}
```

**Common error:** `{{ project.title }}` (dot notation), not
`{{ project["title"] }}` — Django templates use dots for both dictionary
keys and object attributes, deliberately hiding that distinction.

## Checkpoint

Why does template inheritance matter for a multi-page site? (It avoids
repeating shared HTML like navigation in every single template — one
change to `base.html` updates every page that extends it.)

## Independent challenge

Add a `projects` page listing at least three of your own projects (real
or invented) using a `for` loop in the template, extending `base.html`.
