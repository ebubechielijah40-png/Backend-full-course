# Project: Task Manager API — Deployed

## Problem
A backend that only runs on a student's own machine hasn't actually
shipped anything.

## Purpose
Take the tested Week 10 project through a security review and a real
deployment, with a proper Git/GitHub history.

## Requirements
- Secrets (database credentials, secret key) moved to environment
  variables, not committed to source control.
- `DEBUG=False` and `ALLOWED_HOSTS` configured correctly for production.
- A `.gitignore` excluding secrets and local artifacts.
- A real commit history reflecting the project's development (not a
  single "final commit").
- Deployed to a live host, backed by a production PostgreSQL database.

## Features
Not applicable — this stage is operational, not feature-adding.

## Expected user behavior
The same Task Manager API behavior as Weeks 9–10, now reachable over the
public internet.

## Database requirements
A production PostgreSQL instance provided by the chosen host.

## Models / API / Authentication / Validation requirements
Unchanged from Weeks 9–10.

## Expected final result
A live URL serving the working, tested Task Manager API, with its
history on GitHub and no secrets committed to the repository.

## Difficulty
Moderate — mostly configuration and process, not new application logic.

## Estimated time
Spans all three Week 11 sessions.

## Prerequisite knowledge
A working, tested Week 10 project.

## Skills tested
Security review, environment configuration, deployment, Git/GitHub
workflow, log-based debugging of deployment failures.

## How to run it

Locally (development):
```
cd task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Production-style, locally, to test hardened settings before deploying:
```
export DJANGO_SECRET_KEY="a-real-random-value"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
python3 manage.py check --deploy
gunicorn task_manager_site.wsgi
```

Deploying to a live host (steps vary by provider — this project's
`Procfile` targets a Heroku-style platform): push the repository,
set the environment variables from `.env.example` in the platform's
dashboard, and let the `release` step in the `Procfile` run migrations
automatically.

## How to test it manually

Run `python3 manage.py check --deploy` and read every warning — this
project intentionally still shows a few (e.g. HTTPS-related settings
that only matter once real SSL is in place) so you practice reading and
judging them, not just clearing every warning blindly. Then repeat
Week 9 and 10's manual/automated tests against the hardened settings to
confirm nothing broke, and finally against the live deployed URL once
it's up.

## Common errors

- `400 Bad Request` after setting `DEBUG=False` — `DJANGO_ALLOWED_HOSTS`
  wasn't set to include the host you're requesting from.
- `KeyError` on `DB_NAME`/`DB_USER`/etc. — these are only required once
  you intend to use PostgreSQL; for local SQLite development, leave them
  unset entirely (the settings fall back to SQLite automatically).

## Complete code

See `task_manager/task_manager_site/settings.py` for the
environment-based configuration, and `Procfile` /
`.env.example` in this folder for deployment configuration.
