# Teaching Guide

This document explains how to actually run a session using this
repository. It assumes no other documentation.

## Before a session

1. Read that week's `README.md` in full — it tells you what students
   already know, what's new, and what NOT to teach yet. Do not skip the
   "what should NOT be taught yet" section; teaching ahead of schedule is
   the most common way a course like this breaks down.
2. Read the lesson file(s) for that session yourself and run every code
   example before class, on a clean environment if possible. If an
   example doesn't run cleanly for you, it won't for a student.
3. Know which stage of the project the students should reach by the end
   of the session. Sessions run behind if this isn't decided in advance.

## How to teach a concept

Use this order for every new concept, matching the lesson structure:

1. **Say what it is**, in one or two plain sentences.
2. **Say why it's useful**, ideally by pointing at a real problem the
   project has (not a hypothetical one).
3. **Show it working**, live, typed in front of students — not pasted.
   Typing it live, including small mistakes, shows students what using
   the tool actually looks like.
4. **Hand it to them**, with a task that uses the concept immediately.

## How to demonstrate code

- Type it, don't paste it. Narrate what you're typing and why.
- Deliberately make a small, realistic mistake occasionally (a typo, a
  missing colon) and show how the error message points at it. This is
  more valuable than a perfect demonstration.
- Keep demonstrations short — a few minutes. If a demonstration is
  running long, stop and let students try what you've shown so far.

## When students should code themselves

Students should have their hands on the keyboard for the majority of
every session. As a rough guide: after any demonstration longer than 5
minutes, there should be a hands-on task before the next demonstration.
The lesson files are structured this way already — follow the sequence
of demonstration → guided task → independent task as written.

## How to use debugging exercises

Debugging exercises give students code that is close to correct but
broken in a specific way. Run them like this:

1. Give students the broken code and the expected behavior — not the bug.
2. Let them try for a fixed amount of time (5–10 minutes) before offering
   any hint.
3. If a hint is needed, point at *where* to look ("check what this
   function returns"), not *what* is wrong.
4. Reveal the fix only after most students have found it or the time box
   has run out, and explain why it was wrong, not just what the fix is.

## How to check understanding

- Use the checkpoint in each lesson as a real checkpoint: ask students to
  answer it, or do the small task it describes, before moving on.
- Prefer asking a student to explain a line of their own code over asking
  a yes/no question — it's much harder to fake.
- Watch for students who complete tasks quickly by copying a nearby
  example without adapting it; ask them to change one detail (a variable
  name, a condition) on the spot to confirm they understand it.

## How to handle students who are ahead

- Point them at the "independent challenge" section included in every
  lesson before giving them unrelated extra material — it's designed to
  extend the same concept, not introduce a new one.
- Ask them to help a nearby struggling student explain (not do) the fix.
  This reinforces their own understanding.
- Never let a fast student pull the whole class ahead of schedule; keep
  the group moving at the pace the median student needs.

## How to handle students who are struggling

- Isolate exactly which step is failing — most struggle is with one small
  step, not the whole concept. Ask them to run the last thing that worked.
- Re-explain using a smaller, more concrete example than the lesson's,
  ideally with numbers/data they suggest themselves.
- If a student is stuck for more than ~10 minutes without progress,
  simplify the immediate task rather than letting frustration build —
  they can return to the full task once the smaller version works.

## How to gradually reduce guidance

The course is deliberately structured to reduce hand-holding over its
12 weeks:

- **Weeks 1–4:** heavy demonstration, step-by-step tasks, solutions
  available if a hint doesn't resolve it within a few minutes.
- **Weeks 5–8:** shorter demonstrations, tasks stated as goals rather
  than steps, hints required before solutions are given.
- **Week 9:** a full written spec, minimal step-by-step guidance,
  instructor available for questions but not proactively directing.
- **Weeks 10–11:** same as Week 9, plus real (not simulated) failures to
  diagnose.
- **Week 12:** a spec and a deadline; instructor answers only clarifying
  questions about the spec, not implementation questions.

Do not shortcut this by giving Week 9-level independence in Week 3, and
do not keep giving Week 3-level guidance in Week 9 — both break the
progression described in `docs/audits/DIFFICULTY_PROGRESSION_AUDIT.md`.

## How to prevent students from simply copying code

- Ask "why" questions about code a student just wrote or pasted, chosen
  at random — not just at the end of a task.
- Require a small, unannounced variation on every guided task (different
  field name, different condition) so an unmodified copy visibly fails.
- In debugging exercises, remove comments from any code you hand out so
  students can't pattern-match a fix from a comment.
- Treat AI-assisted work the same way: per `AI_USAGE_POLICY.md`, a
  student should always be able to explain code they produced with AI
  help, in their own words, on request.

## How to use the projects

- Each week's project is the spine of the week — lessons exist to make
  the project possible, not the other way around. If a lesson concept
  isn't used in that week's project, ask whether it belongs in this week
  at all.
- Build the project incrementally across the week's three sessions
  exactly as staged in the project's own documentation — don't let
  students jump ahead to later stages before earlier ones work.
- At the end of each week, the project should be fully working. A
  partially working project at week's end is a signal to review that
  week's pacing (see `docs/audits/WORKLOAD_AUDIT.md`).

## How to conduct practical assessments

See `ASSESSMENT.md` for the full rubric. In session terms:

- Assess by watching students run and modify their own code, not by
  reading it silently after the fact.
- Ask students to make a small, specified change live and observe how
  they approach it (where they look, what they try first).
- Never assess with a written quiz as the primary method — a student who
  can't yet build the feature but can describe it is "needs improvement,"
  not "competent."
