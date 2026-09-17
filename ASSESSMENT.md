# Assessment

Assessment in this course is practical: it measures what a student can
build, fix, and explain — not what they can recall. No assessment in this
course is primarily multiple-choice.

## Assessment types

### 1. Weekly practical checks

At the end of each week, each student demonstrates their working project
and makes one small, unseen change to it live (e.g. "add a new field,"
"filter by a different condition," "fix this one failing case"). This
takes 5–10 minutes per student and directly checks that week's learning
outcomes (see `LEARNING_OUTCOMES.md`).

### 2. Project assessments

Every week's project is assessed as a whole against:

- Does it meet the functional requirements in the project spec?
- Does it handle the invalid/edge cases the spec calls for?
- Is the code organized the way that week's lessons taught (functions,
  models, etc. — not just "does it happen to work")?

### 3. SQL assessment (Week 5)

A short set of query-writing tasks against a known schema, completed live
or in-session, without an ORM: given requirements in plain English,
write correct SQL, including at least one multi-table join.

### 4. API assessment (Weeks 7–9)

Using a running API the student built, verify:

- Correct status codes for success, validation failure, not-found, and
  permission-denied cases.
- Correct response bodies for list/retrieve/create/update/delete.
- The student can explain why a given endpoint is designed the way it is.

### 5. Testing / debugging assessment (Week 10)

Given a codebase with a known number of injected bugs (not disclosed in
advance), the student locates and fixes them within a session, and adds
at least one new automated test that would have caught one of them.

### 6. Final capstone (Week 12)

See `capstone/README.md` for the full specification. Assessed against
every learning outcome in `LEARNING_OUTCOMES.md` simultaneously, with the
independence level described in `AI_USAGE_POLICY.md` (Stage 3).

## Rating scale

Used consistently across all assessment types above.

### Excellent

- Meets all functional requirements without prompting.
- Handles edge cases and invalid input correctly.
- Code is organized clearly (sensible functions/models/structure).
- Student can explain every part of their own code, including why it was
  built that way, not just what it does.

### Competent

- Meets the core functional requirements.
- Handles most, but not necessarily every, edge case.
- Code is reasonably organized, with minor issues (e.g. some repetition,
  a slightly awkward structure) that don't affect correctness.
- Student can explain what their code does and can explain most of the
  reasoning behind it with minor prompting.

### Needs improvement

- Meets some but not all core functional requirements, or meets them with
  significant help during the assessment.
- Struggles with edge cases or invalid input.
- Code organization actively makes the feature harder to extend or debug.
- Student can describe what the code is supposed to do but struggles to
  explain how it does it.

### Not yet competent

- Does not meet the core functional requirements even with help during
  the assessment.
- Cannot explain their own code's behavior.
- Indicates the student needs to revisit this week's material before
  moving on — flag for instructor follow-up rather than progressing them
  to the next week's project with a missing foundation.

## How ratings are used

A rating of "needs improvement" or lower on a given week's practical
check should trigger a short, targeted follow-up (extra practice on the
specific weak point, not a repeat of the whole week) before that student
moves into a week that depends heavily on it — particularly before
Weeks 6, 7, 9, and 12, which each depend directly on multiple prior weeks.
