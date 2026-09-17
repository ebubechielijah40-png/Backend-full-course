# Project: Personal Portfolio / Blog Site

## Problem
A student needs a real, multi-page site to anchor Django's project/app/
URL/view/template concepts to something concrete.

## Purpose
Give students a complete Django site before any database concept is
introduced, so routing and templating are learned in isolation first.

## Requirements
- A Django project with at least one app.
- At least three routed pages (e.g. home, about, contact/portfolio
  listing) using URL routing and view functions.
- Templates with dynamic variables (not hardcoded HTML).
- Basic static file usage (CSS).

## Features
- Shared page layout via template inheritance.
- At least one page that receives and displays dynamic context data
  (e.g. a list of project names passed from the view, hardcoded in the
  view for now — no database yet).

## Expected user behavior
A visitor can navigate between pages using links and see content that
was rendered by Django, not static HTML files.

## Database requirements
None yet — deferred to Week 4.

## Models / API / Authentication / Validation requirements
Not applicable this week.

## Expected final result
A running Django site with multiple working, templated, styled pages.

## Difficulty
Low-to-moderate — mostly new framework conventions, not new logic.

## Estimated time
Spans all three Week 3 sessions.

## Prerequisite knowledge
Week 2's request/response model.

## Skills tested
Django project/app structure, URL routing, view functions, template
rendering.

## How to run it

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Visit `http://localhost:8000/`, `/about/`, `/contact/`, and `/projects/`.

## How to test it manually

Confirm all four pages load with a `200` status and share the same
navigation bar from `base.html`. Confirm the projects page lists all
three sample projects via the template's `{% for %}` loop.

## Common errors

- `TemplateDoesNotExist` — check the template is at
  `pages/templates/pages/<name>.html`, matching the app-namespaced
  convention.
- `NoReverseMatch` on `{% url 'about' %}` — check `pages/urls.py` has a
  `name="about"` on that path, and that `pages.urls` is included in the
  project's `urls.py`.

## Complete code

See the `portfolio_site/` and `pages/` folders in this directory.
