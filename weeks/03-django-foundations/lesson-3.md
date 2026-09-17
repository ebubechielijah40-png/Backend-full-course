# Lesson 3 — Settings, Static Files, and Assembling the Site

## The settings module

`portfolio_site/settings.py` configures the whole project: installed
apps, database connection (Week 4 onward), allowed hosts, and more. For
now, the two settings worth understanding are `INSTALLED_APPS` (every
app must be listed here to be recognized) and `DEBUG` (leave `True`
during development — you'll learn why it must be `False` in production
in Week 11).

## Static files

**Static files** are things like CSS and images that don't change per
request. Django serves them through a `static` folder and the
`{% load static %}` template tag:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'pages/style.css' %}">
```

Place the file at `pages/static/pages/style.css`. This matters because
without it, your pages have no styling — the convention keeps static
files organized per-app the same way templates are.

**Common error:** CSS changes not appearing after editing the file
usually means the browser is caching the old version — hard-refresh
(Ctrl+Shift+R / Cmd+Shift+R) before assuming your code is wrong.

## Assembling the full site

**Guided activity:** Together, confirm all pages (`home`, `about`,
`contact`, `projects`) share the same navigation via `base.html`, and at
least one page uses a static CSS file for basic styling.

**Debugging activity:** A student reports `/about/` gives a `404` even
though the view and template both exist and look correct. What's the
most likely cause to check first? (The URL pattern for `about` was
never added to `pages/urls.py`, or `pages.urls` was never included in
the project's `urls.py` — always check the URL wiring before assuming
the view or template is broken.)

## Checkpoint

What must you do to a new app before Django will recognize it?
(Add it to `INSTALLED_APPS` in `settings.py`.)

## Independent challenge

Finish the full site (see `project/README.md`): four routed, templated
pages sharing one layout, with at least basic CSS applied.
