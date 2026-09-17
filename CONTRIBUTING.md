# Contributing to This Course

This file explains how to add or change content in this repository
without breaking its structure or progression.

## Before changing anything

1. Read `COURSE_ROADMAP.md` to understand how the week you're touching
   depends on earlier weeks and feeds into later ones.
2. Read that week's `README.md` for its blueprint (what's assumed known,
   what's new, what must NOT be taught yet).
3. Read `STYLE_GUIDE.md`. All course documentation, new or edited, must
   follow it.

## Adding or editing a lesson

- A lesson file must, for every concept it introduces: explain what it
  is, explain why it's useful, show a working example, give the student
  a task, note common errors, and end with a checkpoint (see
  `weeks/01-python-foundations/lesson-1.md` for the reference format).
- Every code example must actually run. Run it yourself before
  committing it.
- Do not add a concept to a lesson unless that week's project uses it.
  If you think a concept is missing, check whether it belongs in a
  different week instead of adding it here.

## Adding or editing a project

- Follow the specification format used by existing project `README.md`
  files: problem, purpose, requirements, features, data structures,
  build stages, complete code, how to run/test it, common errors,
  possible improvements, checklist.
- Build large projects in the same incremental stages the lessons
  teach — don't hand students a finished project with no build path.
- Keep the project's scope realistic for the available session time. If
  in doubt, re-run the checks in `docs/audits/WORKLOAD_AUDIT.md` against
  the new content.

## Changing the roadmap

Any change to what's taught in one week can affect every later week,
because later weeks assume specific prior knowledge (see the dependency
chain in `COURSE_ROADMAP.md`). If you move, add, or remove a concept:

1. Update that week's `README.md` (and `LEARNING_OUTCOMES.md` if a
   measurable outcome changes).
2. Check every later week that assumed the old version of that concept.
3. Re-run the workload and difficulty-progression audits in `docs/audits/`
   for the affected weeks.

## Keep documentation lean

Don't duplicate explanations across files (per `STYLE_GUIDE.md`) and
don't add a file "for completeness" if it doesn't help a student build
or an instructor teach. If you're unsure whether new content earns its
place, ask whether removing it would make the course worse — if not,
leave it out.
