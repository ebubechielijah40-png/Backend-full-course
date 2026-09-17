# Course Specification

## Course name

**Backend Development with Python & Django**

## Duration and schedule

- **Length:** 12 weeks
- **Frequency:** 3 teaching days per week
- **Session length:** 3–4 hours per day
- **Total classroom hours:** approximately 108–144 hours

## Target learner

Someone who:

- Can use a computer comfortably (files, folders, a text editor, a terminal
  at a basic level).
- Has little or no prior programming experience, **or** has dabbled in
  programming but has never built a real application.
- Wants a practical, job-relevant path into backend web development.

This course is not aimed at experienced developers switching languages —
it starts from the beginning of Python.

## Prerequisites

- Comfortable typing commands into a terminal (no prior command-line
  expertise required, but willingness to use one is required).
- A computer capable of running Python 3 and PostgreSQL.
- Basic English reading ability, since all documentation, error messages,
  and most technical resources are in English.

No prior programming, Python, or web development knowledge is assumed.

## Technology stack

- **Language:** Python 3
- **Web framework:** Django
- **API layer:** Django REST Framework
- **Database:** PostgreSQL
- **Version control:** Git and GitHub
- **Testing:** Python's `unittest` / Django's test framework
- **Deployment:** a single modern PaaS target (e.g. Railway, Render, or
  Fly.io — the specific provider is an instructor choice made in Week 11
  based on what is free/available at teaching time)

## Course philosophy

1. **Build before you theorize.** Every concept is introduced because a
   project needs it, not because a curriculum outline says it should exist.
2. **Reuse, don't discard.** Concepts from earlier weeks are deliberately
   reused in later weeks so students strengthen old skills while learning
   new ones, rather than treating each week as an isolated topic.
3. **Small, complete projects beat large, incomplete ones.** Every project
   is finished, working, and testable — never a fragment.
4. **Independence is the product.** The purpose of the course is not
   "knowing about Django" — it is being able to sit down with a written
   specification and build the backend for it, using documentation,
   debugging skills, and (appropriately) AI tools.

## What this course does NOT attempt to teach

- Frontend frameworks (React, Vue, etc.) — only enough HTML/HTTP to
  understand what a backend is serving.
- Advanced/enterprise Django (custom middleware internals, multi-database
  routing, async Django, caching architecture).
- Microservices, message queues, or distributed systems.
- Advanced or "clever" object-oriented design patterns.
- Computer science theory (algorithms, complexity analysis, data structure
  internals) beyond what's needed to use Python's built-in collections
  correctly.
- DevOps in depth (Docker, Kubernetes, CI/CD pipelines) — deployment is
  covered at a basic, single-service level only.
- Mobile development.

These are reasonable next steps *after* this course, not part of it.

## Expected graduate ability

By the end of the course, a graduate should be able to:

- Take a written specification for a small backend application and build
  it independently, including data models, business logic, an API, tests,
  and a basic deployment.
- Read Django and DRF documentation to solve a new problem without being
  shown the answer first.
- Debug an application by reading error messages and tracebacks rather
  than guessing.
- Explain the tradeoffs of the database and API design choices they make.
- Use AI tools productively as an aid, without depending on them for
  problems they are capable of solving alone.

## Teaching methodology

Every session mixes short explanation with immediate, hands-on practice.
No session is lecture-only. Instructors demonstrate a concept in small
steps, then hand control back to students to apply it themselves, with
guidance decreasing over the course of the 12 weeks (see
`TEACHING_GUIDE.md`).

## Assessment methodology

Assessment is practical, not written or multiple-choice. Students are
evaluated on working code, their ability to explain their own code, and
their ability to extend it under light constraints. Full detail in
`ASSESSMENT.md`.

## AI usage philosophy

AI tools are treated the way documentation, search engines, and Stack
Overflow are treated: as a real resource professional developers use, that
must be used skillfully rather than as a substitute for thinking. Use of
AI is guided in early weeks and progressively restricted, so that the
capstone project measures the student's own ability. Full detail in
`AI_USAGE_POLICY.md`.
