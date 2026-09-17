# 12-Week Roadmap

## Progression at a glance

```
Python
  ↓
Web / HTTP
  ↓
Django (project, URLs, views, templates, admin)
  ↓
SQL / PostgreSQL
  ↓
Django ORM (models talk to the database)
  ↓
REST APIs (Django REST Framework)
  ↓
Authentication & permissions
  ↓
Complete backend (everything combined into one real project)
  ↓
Testing & debugging (applied to that backend)
  ↓
Security & Deployment / Git (that backend goes live)
  ↓
Independent capstone (built from a spec, with minimal help)
```

Each arrow is a real dependency: a later week could not be taught without
the one above it. No week is "bonus" or "extra" — removing one would break
the chain (see `docs/audits/DIFFICULTY_PROGRESSION_AUDIT.md`).

---

## Week 1 — Python Foundations for Backend Development

- **Sessions:** 1) Python Basics and Data 2) Functions, Decisions, Loops
  and Errors 3) Files, JSON, Virtual Environments and Basic Classes
- **Main concepts:** variables and types, collections, control flow,
  functions, exceptions, file I/O, JSON, venv/pip, basic classes
- **Main practical work:** build a command-line Expense Tracker in stages
- **Project:** Command-Line Expense Tracker
- **Capability at week's end:** can write a small, working, organized
  Python program that persists data to a file and handles bad input

## Week 2 — Web and HTTP Fundamentals

- **Sessions:** 1) How the web works (client/server, request/response)
  2) HTTP in detail (methods, status codes, headers, URLs) 3) Serving
  dynamic content and inspecting real traffic
- **Main concepts:** client/server model, HTTP methods, status codes,
  headers, query strings vs. body, a minimal Python web server
- **Main practical work:** inspect real requests/responses with browser
  dev tools and a CLI HTTP client; extend Week 1's Python skills to build
  a tiny script that serves plain-text/HTTP responses
- **Project:** "Request Inspector" — a small script that logs and
  explains incoming HTTP requests
- **Capability at week's end:** can read any HTTP request/response and
  explain what it means; understands why Django exists

## Week 3 — Django Foundations

- **Sessions:** 1) Django project/app structure, URLs, views 2) Templates
  and dynamic HTML 3) Settings, static files, connecting the pieces
- **Main concepts:** `django-admin`, project vs. app, URL routing, view
  functions, templates and template variables, settings module
- **Main practical work:** build a multi-page Django site with routed
  views and templates
- **Project:** Personal Portfolio / Blog site (static content, no
  database models yet beyond what Django ships with)
- **Capability at week's end:** can create a Django project from scratch
  and serve multiple routed, templated pages

## Week 4 — Django Models and Admin

- **Sessions:** 1) Models and fields 2) Migrations and the admin site
  3) Rendering model data in templates
- **Main concepts:** model classes, field types, migrations, the Django
  admin, `ForeignKey` at an introductory level, querysets in templates
- **Main practical work:** turn the Week 3 site into a database-backed
  site (e.g. blog posts stored as model instances)
- **Project:** Blog with database-backed posts, managed through Django
  admin
- **Capability at week's end:** can design a simple model, migrate it,
  manage its data through admin, and display it on a page

## Week 5 — SQL and PostgreSQL

- **Sessions:** 1) Relational databases and PostgreSQL setup 2) `SELECT`,
  `WHERE`, `INSERT`, `UPDATE`, `DELETE` 3) `JOIN`s and multi-table queries
- **Main concepts:** tables, rows, columns, primary/foreign keys,
  normalization at a beginner level, SQL syntax, joins
- **Main practical work:** design and query a small multi-table schema
  directly in SQL (outside Django), against a real PostgreSQL database
- **Project:** "Library Catalog" SQL project — schema design plus a set
  of required queries against it
- **Capability at week's end:** can design a small relational schema and
  write correct multi-table SQL queries against it, independent of Django

## Week 6 — Django ORM

- **Sessions:** 1) Connecting Django to PostgreSQL, model relationships
  2) ORM queries (create, read, update, delete, filtering) 3) Related
  queries and reading the SQL the ORM generates
- **Main concepts:** `ForeignKey`/`ManyToManyField` in depth, ORM CRUD,
  `QuerySet` filtering, `select_related`/`prefetch_related` at an
  introductory level, viewing generated SQL
- **Main practical work:** rebuild the Week 5 schema as Django models
  against a real PostgreSQL database, then query it through the ORM
- **Project:** Library Catalog, rebuilt as a Django app
- **Capability at week's end:** can model a relational problem in Django
  and perform correct related-data queries through the ORM

## Week 7 — REST APIs with Django REST Framework

- **Sessions:** 1) What REST is, installing DRF, serializers 2) List,
  retrieve, create, update, delete endpoints 3) Validation and error
  responses
- **Main concepts:** REST principles, serializers, `APIView`/generic
  views, status codes for APIs, input validation
- **Main practical work:** expose the Library Catalog as a REST API
- **Project:** Library Catalog API (same data, now API-driven)
- **Capability at week's end:** can build a working CRUD REST API for a
  model with correct validation and status codes

## Week 8 — Authentication and Permissions

- **Sessions:** 1) User accounts, registration, login 2) Token/session
  authentication in DRF 3) Permissions and object-level access control
- **Main concepts:** Django's user model, authentication vs.
  authorization, DRF authentication classes, permission classes,
  object ownership checks
- **Main practical work:** add accounts to the Library Catalog API so
  users can only modify their own records
- **Project:** Library Catalog API + Accounts
- **Capability at week's end:** can add real authentication and
  per-user permissions to an existing API

## Week 9 — Complete Backend Project

- **Sessions:** 1) Planning from a written spec 2) Building models, ORM,
  and API together 3) Adding auth and finishing the feature set
- **Main concepts:** no new syntax — this week is integration: taking a
  written specification and combining models, ORM, REST API, and auth
  into one coherent backend, with reduced step-by-step guidance
- **Main practical work:** build a new, larger application ("Task
  Manager API") from a written spec, reusing everything from Weeks 3–8
- **Project:** Task Manager API
- **Capability at week's end:** can take a written spec and build a
  complete, authenticated CRUD backend with moderate independence

## Week 10 — Testing and Debugging

- **Sessions:** 1) Why and how to test; unit tests for models 2) Testing
  views and API endpoints 3) Systematic debugging on real, injected bugs
- **Main concepts:** Django's test framework, `TestCase`, API test
  clients, reading tracebacks, isolating a bug with a minimal
  reproduction, print/debugger-based debugging
- **Main practical work:** write an automated test suite for the Task
  Manager API, then debug a set of deliberately broken versions of it
- **Project:** Task Manager API — test suite + debugging exercises
- **Capability at week's end:** can write meaningful automated tests and
  debug an unfamiliar failure systematically

## Week 11 — Security, Deployment, and Git/GitHub

- **Sessions:** 1) Common backend security mistakes and how to avoid
  them 2) Environment variables, production settings, and deployment
  3) Git/GitHub workflow for a real project, deploying and verifying
- **Main concepts:** secrets management, `DEBUG=False`, `ALLOWED_HOSTS`,
  basic input-validation/security review, environment configuration,
  Git branching basics, deploying to a live host, reading deploy logs
- **Main practical work:** harden and deploy the Task Manager API; put
  its full history on GitHub with a real commit log
- **Project:** Task Manager API — deployed, on GitHub
- **Capability at week's end:** can take a working local backend and
  ship it to a live, reasonably secure deployment

## Week 12 — Independent Capstone

- **Sessions:** 1) Reading the capstone spec, planning models and API
  2) Independent build time 3) Independent build time, testing, and
  deployment
- **Main concepts:** none new — every prior outcome, applied with
  Stage 3 (independent) AI usage rules (see `AI_USAGE_POLICY.md`)
- **Main practical work:** build, test, and deploy an original backend
  application from a written specification, largely unassisted
- **Project:** Capstone Project (see `capstone/README.md`)
- **Capability at week's end:** demonstrated, independent ability to
  build and ship a backend application — the target outcome of the
  entire course
