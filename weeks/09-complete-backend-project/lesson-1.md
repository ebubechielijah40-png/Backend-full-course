# Lesson 1 — Planning from a Written Spec

This week introduces no new syntax. The skill being taught is reading a
specification and turning it into a plan *before* writing code — exactly
what a professional developer does before starting a real task.

## Reading the spec

Read the full Task Manager API specification in `project/README.md`
before writing anything. As you read, identify:

- **Resources** (nouns): what models does this need? (Here: `Task` and
  `Category`.)
- **Relationships**: how do they connect? (A `Task` belongs to one
  `Category`; a `Task` belongs to one owning `User`.)
- **Actions** (verbs): what can a user do to each resource? This becomes
  your list of endpoints.
- **Rules**: what must always be true? (A user can only see/modify their
  own tasks — this becomes a permission check, exactly like Week 8's
  loans.)

**Task:** Before looking at any reference solution, write out your own
plan: a list of models with their fields, and a list of endpoints with
their HTTP methods, based only on `project/README.md`.

## Guided activity

Compare your plan against a partner's (or, working alone, against the
project README's own requirements list again after an hour away from
it). Where they differ, ask: does the spec actually require this, or did
I add something it didn't ask for? (Recall `STYLE_GUIDE.md`'s and
`COURSE_SPEC.md`'s repeated point: don't add scope the spec doesn't
call for.)

## Checkpoint

Why is planning before coding especially important once a project has
more than one model? (Because the models' relationships constrain how
the API and permissions must be structured — getting the relationship
wrong early is expensive to unwind later, exactly as Week 5–6 emphasized
for database design.)
