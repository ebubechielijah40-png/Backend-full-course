# Lesson 2 — Environment Variables, Production Settings, and Deployment

## Reading configuration from the environment

Beyond `SECRET_KEY` and `DEBUG`, production settings typically move the
database connection to environment variables too:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
```

A `.env` file (never committed — add it to `.gitignore`) holds these
locally; the hosting platform sets the real values through its own
configuration in production.

## Deploying

Deployment steps are specific to whichever host you choose (see
`project/README.md` for this project's chosen target). In general, every
platform needs:

- A way to install dependencies (`requirements.txt`, already maintained
  since Week 3).
- A **start command** telling the platform how to run your app (usually
  something like `gunicorn myproject.wsgi`, using a production-grade
  server instead of `manage.py runserver`, which isn't meant for real
  traffic).
- The environment variables from above, set through the platform's
  dashboard or CLI, not committed to the repository.
- Migrations run against the production database (`python3 manage.py
  migrate`), usually as a one-time or automatic deploy step.

**Task:** Install `gunicorn` (`pip install gunicorn`), add it to
`requirements.txt`, and confirm it can serve your Task Manager locally:
`gunicorn myproject.wsgi`.

## Checkpoint

Why shouldn't `manage.py runserver` be used to serve real production
traffic? (It's a development-only server — not built for the
performance, concurrency, or security hardening a real production server
like Gunicorn provides.)
