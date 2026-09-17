# Project: Task Manager API — Tests and Debugging

## Problem
The Week 9 Task Manager API works, but "works" was only ever verified
manually, and manual verification doesn't scale or catch regressions.

## Purpose
Apply automated testing to a real project students already understand,
then practice systematic debugging on real (not hypothetical) failures.

## Requirements
- A test suite covering: model behavior, each API endpoint's success
  case, each endpoint's key failure cases (validation error, not found,
  permission denied).
- At least one test that would fail against an unfixed bug the
  instructor introduces.

## Features
- Uses Django's `TestCase` and DRF's API test client.
- Tests run independently of manually-entered data (using test
  fixtures/setup, not the developer's own manually-created records).

## Expected user behavior
Not applicable — this project is developer-facing (tests), not
user-facing.

## Database requirements
Same schema as Week 9, exercised through Django's isolated test
database.

## Models / Relationships / API / Authentication / Validation requirements
Reused directly from Week 9 — no changes to the application's design.

## Expected final result
A passing test suite for the correct version of the project, and a
demonstrated ability to find and fix bugs in instructor-provided broken
versions, using the test suite and tracebacks (not guesswork).

## Difficulty
Moderate — one new skill (testing) applied to a known project, plus
debugging practice.

## Estimated time
Spans all three Week 10 sessions.

## Prerequisite knowledge
A working Week 9 Task Manager API.

## Skills tested
Writing meaningful tests, using tracebacks and test failures to isolate
bugs.

## How to run it

```
cd task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py test tasks
```

All 15 tests should pass.

## How to use the debugging exercises

`broken_versions/` contains two documented, verified bugs:

- `bug_1_ownership.py` — breaks the ownership check (2 tests fail).
- `bug_2_filter.py` — breaks the completed-status filter (1 test fails
  with an unhandled error, not just a wrong result).

Each file shows exactly which method to replace in
`task_manager/tasks/api_views.py` and which test(s) should fail as a
result — instructors should apply one, have students diagnose and fix
it using the test suite and traceback, then revert to the working
version before applying the next.

## Common errors

- A "passing" test that never actually asserts anything (e.g. missing
  an `assertEqual` call) — always confirm a new test fails first against
  intentionally broken code before trusting that it passes for the right
  reason.

## Complete code

See `task_manager/tasks/tests.py` for the full suite.
