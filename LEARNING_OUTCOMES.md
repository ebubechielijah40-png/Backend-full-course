# Learning Outcomes

These outcomes are written to be checkable against real work a student
produces — not against what they can recite. Each one maps to specific
weeks (noted in brackets) and is assessed practically (see `ASSESSMENT.md`).

## Python

- Write, run, and debug a Python script from the command line. `[W1]`
- Use variables, strings, numbers, booleans, lists, dictionaries, tuples,
  and sets to represent real data. `[W1]`
- Organize code into functions with parameters, return values, and
  sensible default values. `[W1]`
- Use `if`/`elif`/`else`, `for`, and `while` correctly, including `break`
  and `continue`. `[W1]`
- Handle errors with `try`/`except`/`else`/`finally` and raise exceptions
  deliberately. `[W1]`
- Read from and write to files, including JSON files, to persist data
  between program runs. `[W1]`
- Create and use a Python virtual environment and install packages with
  `pip`. `[W1]`
- Write a basic class with attributes and methods, and explain when a
  class is a better fit than a plain dictionary. `[W1]`

## Web / HTTP

- Explain what a client, a server, and a request/response cycle are. `[W2]`
- Read an HTTP request and response, including method, path, headers,
  status code, and body. `[W2]`
- Explain the difference between GET, POST, PUT/PATCH, and DELETE, and
  choose the correct one for a given action. `[W2]`
- Serve a basic dynamic web response and inspect it with browser dev
  tools and a command-line HTTP client. `[W2]`

## Django

- Create a Django project and configure at least one application inside
  it. `[W3]`
- Define URL routes and connect them to view functions or classes. `[W3]`
- Use Django templates to render dynamic HTML. `[W3]`
- Use the Django admin site to manage application data. `[W4]`
- Configure Django settings for a real project (apps, database,
  environment-based configuration). `[W3, W11]`

## SQL / PostgreSQL

- Explain what a relational database is and why backend applications use
  one. `[W5]`
- Write `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements. `[W5]`
- Write SQL queries involving multiple related tables, using `JOIN`. `[W5]`
- Design a normalized table structure for a given problem, including
  primary and foreign keys. `[W5]`

## Django ORM

- Create relational models and generate/apply migrations. `[W4, W6]`
- Perform create, read, update, and delete operations through the ORM. `[W6]`
- Express one-to-many and many-to-many relationships in Django models and
  query across them. `[W6]`
- Read the SQL a given ORM query produces, to explain what it does. `[W6]`

## REST APIs

- Build REST API endpoints for a resource, covering list, retrieve,
  create, update, and delete. `[W7]`
- Serialize and deserialize model data using Django REST Framework. `[W7]`
- Validate incoming API data and return clear, correct error responses. `[W7]`
- Design a sensible URL and status-code scheme for a small API. `[W7, W9]`

## Authentication

- Implement user registration and login for an API. `[W8]`
- Implement authentication and permissions so that users can only modify
  their own data. `[W8]`
- Explain the difference between authentication and authorization. `[W8]`

## Testing

- Write automated tests for models, views, and API endpoints. `[W10]`
- Use test failures and tracebacks to locate and fix a bug systematically,
  rather than by guesswork. `[W2, W10]`
- Explain what a given test is checking and why it matters. `[W10]`

## Security

- Identify and avoid common backend security mistakes (hardcoded secrets,
  missing input validation, exposing debug mode, weak permission checks).
  `[W11]`
- Configure environment variables and secrets correctly for a deployed
  application. `[W11]`

## Git / GitHub

- Use Git to track changes to a real project (init, add, commit, branch,
  merge). `[W1–W12, ongoing]`
- Push a project to GitHub and write a clear commit history and README. `[W3, W11]`

## Deployment

- Deploy a Django application to a live hosting environment, including
  a production database and environment configuration. `[W11]`
- Diagnose and fix a basic deployment failure using logs. `[W11]`

## Independent development

- Build a backend application from a written specification with
  significantly reduced guidance. `[W9]`
- Build a backend application from a written specification independently,
  applying every prior outcome above, for the final capstone. `[W12]`
