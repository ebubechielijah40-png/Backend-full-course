# Style Guide

Every file in this repository — course-level docs, weekly READMEs, and
lessons — follows these rules.

## Language

- Use simple, plain English. Short sentences beat long ones.
- Explain any technical term the first time it's used in a given file,
  even if it was explained in an earlier file. Don't assume a student
  remembers a term from three weeks ago without a reminder.
- Never use an abbreviation without spelling it out on first use in that
  file (e.g. "HyperText Transfer Protocol (HTTP)").
- Avoid unnecessary academic language. Say "this saves the list to a
  file" rather than "this facilitates the persistence of the collection."

## Structure

- Prefer practical explanation over theory. If a concept doesn't help the
  student build or understand something they're about to build, cut it.
- Every section should do one of two things: help the student build
  something, or help them understand something necessary for building.
  Sections that exist only to make a document look thorough are removed.
- Keep theoretical sections short. A concept gets a few sentences of
  "what" and "why," then an example — not pages of background.

## Explaining code

For every non-trivial piece of example code:

- Explain **why** the code is being written this way, not just what it
  does line by line.
- Explain **what the code does**, in plain terms, before or after showing
  it — never leave a code block to speak entirely for itself.
- Include **common mistakes** a student is likely to make with this
  concept, and what the resulting error usually looks like.
- Show **commands exactly** as they should be typed, including flags,
  in a fenced code block — never paraphrase a command.

## Assumptions

- Do not assume the learner knows a hidden prerequisite. If a lesson
  needs something from an earlier week, name it explicitly ("recall from
  Week 1 that...") rather than assuming it's remembered.
- Do not introduce a concept before it's needed just because it's related
  to the topic. If it isn't used in that week's project, it doesn't
  belong in that week.

## What to avoid

- Long lists of trivia or "fun facts" about a technology.
- Padding a document to make the repository look more comprehensive —
  every file should be as long as it needs to be and no longer.
- Multiple files repeating the same explanation. If two files need to
  reference the same idea, one should explain it and the other should
  link to it.
