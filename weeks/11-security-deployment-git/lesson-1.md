# Lesson 1 — Common Backend Security Mistakes

## Secrets don't belong in source control

A `SECRET_KEY` or database password committed to Git is compromised the
moment the repository is pushed anywhere — including a private repo,
since access can change. Fix: read secrets from **environment
variables**, never hardcode them.

```python
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"
```

**Task:** Move your Task Manager's `SECRET_KEY` out of `settings.py`
into an environment variable, and confirm the app still runs locally
after setting it in your shell (`export DJANGO_SECRET_KEY=...`).

## `DEBUG = False` in production

Django's debug page shows a full traceback, including source code and
settings, to anyone who triggers an error — invaluable in development,
a serious information leak in production. Always set `DEBUG = False`
for anything real users can reach, and configure `ALLOWED_HOSTS`
explicitly once you do (Django refuses all requests without it).

**Common error:** forgetting to set `ALLOWED_HOSTS` after turning
`DEBUG` off causes Django to reject every request with a `400 Bad
Request` — this is Django protecting you from a different attack (HTTP
Host header spoofing), not a bug.

## Input validation and permission checks, revisited

Weeks 7–9's validation and ownership checks *are* security features, not
just correctness features — a missing `if task.owner != request.user`
check is a real vulnerability (any user could modify anyone's data), not
just a bug that produces a wrong answer.

## Checkpoint

Why is a hardcoded secret in a private GitHub repo still a risk?
(Repository access, or the repo's visibility itself, can change later —
a secret that was ever committed should be treated as exposed and
rotated, not just "probably fine because it's private.")
