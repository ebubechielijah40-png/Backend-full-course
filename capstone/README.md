# Capstone Project

## Problem

You have been given a short written specification for a backend
application you have not seen before (the instructor selects or writes
the specific spec at Week 12 — it should be similar in size and shape to
the Week 9 Task Manager API, but a different domain, e.g. a simple
booking system, a recipe box, an event RSVP tracker).

## Purpose

To demonstrate, independently, everything this course has taught: data
modeling, the Django ORM, a REST API, authentication and permissions,
automated tests, and a live deployment — built from a specification
rather than from step-by-step instructions.

## Requirements

- The instructor provides a written spec describing at least two related
  resources (e.g. "recipes" and "ingredients," or "events" and
  "RSVPs") with a real relationship between them (one-to-many or
  many-to-many).
- The student produces:
  - Django models matching the spec, with migrations.
  - A REST API covering list, retrieve, create, update, and delete for
    each resource, with correct validation and status codes.
  - User accounts, with permissions so users can only modify their own
    data.
  - An automated test suite covering the core behavior.
  - A live deployment of the finished application.
  - A README explaining what was built and how to run it.

## Features

Defined by the specific spec given at teaching time; must include, at
minimum, the CRUD-plus-auth feature set above. Instructors should not
make the spec larger than the Week 9 project — the capstone tests
independence, not increased scope.

## Expected user behavior

A user should be able to register, log in, create and manage their own
records for the given domain, and be prevented from modifying another
user's records.

## Database requirements

At least two related tables, matching the models above, in PostgreSQL.

## Models / relationships

Defined by the specific spec; must include at least one `ForeignKey` or
`ManyToManyField` relationship exercised by the API.

## API requirements

Full CRUD for each resource, following the same conventions taught in
Week 7 (status codes, validation, response shape).

## Authentication requirements

Same conventions as Week 8: authenticated write access, ownership-based
permissions.

## Validation requirements

Reject invalid input with clear, correctly-coded error responses (as
practiced in Week 7).

## Expected final result

A deployed, authenticated, tested REST API matching the given spec, with
its source and commit history on GitHub.

## Difficulty

High relative to any single prior week, by design — but achievable,
because it only recombines skills already individually demonstrated in
Weeks 1–11 (see `docs/audits/DIFFICULTY_PROGRESSION_AUDIT.md`).

## Estimated time

Approximately 9–12 classroom hours (Week 12's three sessions), sized
against the Week 9 project, which covered similar scope with more
guidance in less time.

## Prerequisite knowledge

Every learning outcome in `LEARNING_OUTCOMES.md`.

## Skills tested

Independent specification reading, data modeling, API design,
authentication, testing, debugging, and deployment — used together
without step-by-step instructions (Stage 3 of `AI_USAGE_POLICY.md`).
