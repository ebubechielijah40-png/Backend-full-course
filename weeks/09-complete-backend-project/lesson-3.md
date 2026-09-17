# Lesson 3 — Adding Auth and Finishing the Feature Set

Add authentication and ownership permissions exactly as in Week 8:
require login for write operations, and scope every queryset to
`request.user` so a user only ever sees and modifies their own tasks.

**Guided activity:** Reuse Week 8's registration/login endpoints
directly (copy `accounts/` from the Week 8 project) rather than
rewriting them — this is exactly the kind of reuse `CONTRIBUTING.md`
and the course's difficulty-progression audit are built around.

**Task:** Finish every requirement in `project/README.md`, then run
through its full manual test checklist yourself before considering the
project done.

**Independent challenge:** Without being told which one, find and fix
at least one gap in your own implementation by testing it as if you
were an unfriendly user: try creating a task with an invalid category
ID, try accessing another (test) user's task directly by ID, and try
omitting a required field. Each should fail with a sensible error, not
a crash.

## Checkpoint

What is this week actually testing, given that it introduces no new
syntax? (Whether you can combine everything from Weeks 3–8 on an
unfamiliar problem with less guidance than before — the course's first
real independence checkpoint.)
