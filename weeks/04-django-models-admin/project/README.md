# Project: Database-Backed Blog

## Problem
The Week 3 site has no real data behind it — content is hardcoded in
view functions, which doesn't scale past a few pages.

## Purpose
Introduce models, migrations, and the admin site by solving that real
limitation.

## Requirements
- A `Post` model with fields for title, body, publish date, and an
  author `ForeignKey` (to Django's built-in `User` model).
- Migrations generated and applied.
- Posts manageable through the Django admin.
- A list page and a detail page for posts, rendered from the database
  instead of hardcoded data.

## Features
- Admin-based create/edit/delete of posts.
- List view ordered by publish date.
- Detail view showing a single post's full content and author.

## Expected user behavior
A staff user adds/edits posts through the admin; a visitor sees them on
the public site immediately, no code changes required.

## Database requirements
A single-table (plus the built-in `User` table) schema is enough this
week — one real `ForeignKey` relationship (post → author).

## Models / Relationships
`Post.author` → `User` (`ForeignKey`, descriptive use only — deep
relationship querying is Week 6's focus).

## API / Authentication / Validation requirements
Not applicable this week — the admin site is the only management
interface.

## Expected final result
The Week 3 site, now reading and displaying real, admin-managed data.

## Difficulty
Moderate — the first time data outlives a single request.

## Estimated time
Spans all three Week 4 sessions.

## Prerequisite knowledge
Week 3's Django project.

## Skills tested
Model definition, migrations, admin configuration, querying models in
views/templates.

## How to run it

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Visit `/admin/` to add posts, then `/` to see them listed and `/<id>/`
for a single post's detail page.

## How to test it manually

Add two or three posts through the admin, confirm they appear on the
list page (newest first), confirm each detail page shows the right
content, and confirm visiting a nonexistent post ID returns a proper
`404` instead of a crash.

## Common errors

- Admin page not showing the `Post` model — confirm `admin.site.register
  (Post)` is in `blog/admin.py`.
- `relation "blog_post" does not exist` — migrations weren't run; run
  `python3 manage.py migrate`.

## Complete code

See the `blog_site/` and `blog/` folders in this directory.
