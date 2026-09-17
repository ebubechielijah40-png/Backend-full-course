# Lesson 3 — Systematic Debugging on Real, Injected Bugs

## Reading a traceback

A traceback lists, from top to bottom (or bottom to top, depending on
where you look first), the chain of function calls that led to an error,
ending with the actual exception. The most useful habit: **read the
bottom line first** (what went wrong), then look at the last line of
*your own* code in the traceback (not Django's internals) — that's
almost always where the real problem is.

## Isolating a bug with a minimal reproduction

When something breaks, don't guess — reduce the problem:

1. Find the smallest input that triggers the bug (one specific task, not
   "the whole app is broken").
2. Remove unrelated code/steps until only what's needed to reproduce it
   remains.
3. Write a failing test that reproduces it (Lesson 2's tools) — now
   you'll know for certain when it's actually fixed, and it stays fixed.

**Debugging activity:** Your instructor will provide 1–2 versions of the
Task Manager API with a deliberately introduced bug (see
`project/README.md` for the process). For each: read the failing
behavior or traceback, form a hypothesis about the cause *before*
changing anything, test the hypothesis, then fix it — and write a test
that would have caught it.

**Guided activity:** Together, work through one injected bug end to end,
narrating each step above out loud.

## Checkpoint

Why write a test *after* fixing a bug, not just fix it and move on?
(So the same bug can't silently come back later without being noticed —
this is exactly what "regression" means, and it's what a test suite
protects against.)

## Independent challenge

Write your own test suite for the Task Manager API covering at least:
model behavior, one success case and one failure case per endpoint, and
the ownership/permission checks — see `project/README.md` for the full
required coverage.
