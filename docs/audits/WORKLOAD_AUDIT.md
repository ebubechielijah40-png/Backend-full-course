# Workload Audit

For every week, this audit answers: can this realistically be taught in
3 sessions of 3–4 hours, with students actually practicing rather than
watching? Where a week was originally overloaded, the scope was reduced
here rather than the documentation simply shortened.

Each week is checked against the same eight questions from the course
design brief. Only findings that changed the design are noted; a week
with no note passed all eight checks as originally scoped.

## Week 1 — Python Foundations

- **Fits 3 sessions?** Yes — Basics/Data, Functions/Control Flow/Errors,
  and Files/JSON/Classes are natural session boundaries, each with a
  matching project stage.
- **Hidden prerequisites?** None — this is the first week.
- **Too much theory / too much coding?** Balanced; every concept maps to
  a concrete step in the Expense Tracker.
- **Reduction made:** advanced OOP (inheritance, dunder methods,
  properties) was deliberately excluded from Lesson 3 — a beginner class
  with attributes and methods is sufficient for this stage, matching the
  brief's instruction not to turn it into an advanced OOP lesson.

## Week 2 — Web and HTTP Fundamentals

- **Fits 3 sessions?** Yes, once scoped to *reading and understanding*
  HTTP rather than building a real web framework from scratch.
- **Hidden prerequisites?** Relies on Week 1's functions and file I/O for
  the "Request Inspector" script — no new dependency.
- **Reduction made:** building a from-scratch multi-threaded web server
  was excluded; Python's built-in single-threaded HTTP server is enough
  to demonstrate the concepts and keeps Week 2 from turning into a
  networking course.

## Week 3 — Django Foundations

- **Fits 3 sessions?** Yes, when scoped to URLs/views/templates/settings
  only — models are deliberately deferred to Week 4.
- **Hidden prerequisites?** Needs Week 2's HTTP/status-code vocabulary,
  which is already taught by this point.
- **Reduction made:** database models were moved out of Week 3 entirely
  (into Week 4) to avoid introducing migrations, the ORM, and templates
  in the same week.

## Week 4 — Django Models and Admin

- **Fits 3 sessions?** Yes.
- **Hidden prerequisites?** Needs Week 3's project/app/URL/template
  knowledge, already established.
- **Note:** `ForeignKey` is introduced only at a descriptive level here
  (e.g. "a post has one author") — full relationship querying is
  deliberately deferred to Week 6, after SQL (Week 5) gives students the
  underlying concept first.

## Week 5 — SQL and PostgreSQL

- **Fits 3 sessions?** Yes, when scoped to a single small schema (2–3
  tables) rather than a large one.
- **Hidden prerequisites?** None new — this week intentionally steps
  outside Django to isolate SQL as its own skill.
- **Reduction made:** database normalization theory beyond first/second
  normal form basics was excluded — enough to design a sensible schema,
  not a full database-theory treatment.

## Week 6 — Django ORM

- **Fits 3 sessions?** Yes, because Week 5 already did the hard
  conceptual work (relational thinking); this week is largely translation
  into Django syntax plus `select_related`/`prefetch_related` at an
  introductory level only.
- **Hidden prerequisites?** Needs Week 4 (models/migrations) and Week 5
  (relational thinking, SQL) — both already taught.
- **Reduction made:** query optimization beyond `select_related`/
  `prefetch_related` (e.g. raw SQL escape hatches, query plan analysis)
  was excluded as out of scope for this course (see `COURSE_SPEC.md`).

## Week 7 — REST APIs with DRF

- **Fits 3 sessions?** Yes, scoped to one resource type at a time.
- **Hidden prerequisites?** Needs Week 6's ORM fluency — confirmed
  already established by this point.
- **Reduction made:** DRF viewsets/routers (a more "magic" shortcut) were
  excluded in favor of explicit `APIView`-based endpoints first, so
  students see exactly what each endpoint does before any abstraction is
  introduced — viewsets can be introduced later by an instructor as an
  optional extension, not a required outcome.

## Week 8 — Authentication and Permissions

- **Fits 3 sessions?** Yes.
- **Hidden prerequisites?** Needs Week 7's API skeleton to attach
  authentication to.
- **Reduction made:** OAuth2/social login and JWT-based auth were
  excluded — token or session authentication (built into DRF) is
  sufficient to teach the concept without adding a large new topic.

## Week 9 — Complete Backend Project

- **Fits 3 sessions?** Yes — this week deliberately introduces no new
  concepts, only integration, which keeps the cognitive load lower than
  a concept-introducing week even though the project is larger.
- **Hidden prerequisites?** Explicitly requires Weeks 3–8 in full — this
  is by design (see `COURSE_ROADMAP.md`) and is the reason this week
  exists before testing/security/deployment.
- **Note:** guidance is intentionally reduced here per
  `TEACHING_GUIDE.md`; this is a pacing decision, not scope creep.

## Week 10 — Testing and Debugging

- **Fits 3 sessions?** Yes, when scoped to testing the Week 9 project
  rather than a new one — no new application to build from scratch.
- **Hidden prerequisites?** Needs a working Week 9 project to test and
  debug; a student without one needs remediation before this week (see
  `ASSESSMENT.md`).
- **Reduction made:** test coverage tooling, mocking libraries, and
  performance testing were excluded — functional correctness testing is
  the target skill.

## Week 11 — Security, Deployment, and Git/GitHub

- **Fits 3 sessions?** Yes, when scoped to one deployment target chosen
  in advance by the instructor, not a comparison of several platforms.
- **Hidden prerequisites?** Needs a working, tested Week 9/10 project.
- **Reduction made:** containerization (Docker) and CI/CD pipelines were
  excluded as out of scope for this course (see `COURSE_SPEC.md`);
  deployment is direct-to-platform.

## Week 12 — Independent Capstone

- **Fits 3 sessions?** Yes, by design — the capstone spec
  (`capstone/README.md`) is sized to be buildable by a student working
  independently within 9–12 hours, based on the combined scope of Weeks
  6–9's projects (which were each built with more guidance in less time).
- **Hidden prerequisites?** Every prior week — this is the intended
  culmination, not a gap.

## Overall conclusion

No week required documentation-only shortening; every overload found
during design was resolved by removing a topic or feature from scope
(noted above), consistent with the instruction not to solve overload by
making documentation shorter.
