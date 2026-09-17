# Week 1 — Python Fundamentals for Backend Development

## What you're learning

This week teaches just enough Python to start building real
applications: variables and data types, collections (lists,
dictionaries, tuples, sets), control flow (`if`, loops), functions,
error handling, working with files and JSON, virtual environments, and
basic classes.

## Why Python for backend development

Backend development means writing the code that runs on a server:
storing data, applying business rules, and responding to requests. Python
is one of the most common languages for this because it's readable,
has a huge set of libraries, and — most importantly for this course —
it's what Django (which you'll start in Week 3) is built on. Everything
you learn this week is code you will keep writing, just inside a bigger
framework, for the rest of the course.

## What you will build

A **Command-Line Expense Tracker**: a program that lets you add
expenses, list them, see your total spending, filter by category, delete
one, and save/load everything to a file so your data survives closing
the program. See `project/README.md` for the full specification and
build process.

## What you should already know

Nothing about Python. You should be comfortable opening a terminal and
running a command someone gives you exactly as written — that's the only
assumption this week makes.

## What you'll know by the end

You'll be able to write a Python program with multiple functions, that
stores structured data in memory, handles bad input without crashing,
and saves/loads that data from a file — the same shape of thing a real
backend does, just without a network or a database yet.

## The three-session structure

1. **Lesson 1 — Python Basics and Data.** Variables, types, and
   collections. You'll represent a single expense, then several.
2. **Lesson 2 — Functions, Decisions, Loops and Errors.** You'll turn
   Lesson 1's data-handling code into reusable functions, and make the
   program handle bad input instead of crashing.
3. **Lesson 3 — Files, JSON, Virtual Environments and Basic Classes.**
   You'll make the tracker's data persist across runs, and see one way a
   class can simplify what you've already built.

## How to run the code

You need Python 3 installed. Check with:

```
python3 --version
```

Any code example in a lesson is run the same way: save it in a file
ending in `.py`, then run:

```
python3 filename.py
```

## How to use the project

The project folder (`project/`) is the expense tracker you'll build
across all three sessions. Its `README.md` explains the whole build,
stage by stage, with the reasoning behind each stage — read the stage
you're currently working on, don't skip ahead. `expense_tracker.py`
holds the finished, working version to check your own code against, and
`requirements.txt` lists what to install (nothing external is required
for Week 1 — the standard library is enough, so this file will stay
mostly empty, but it establishes the habit for later weeks).

## Expected amount of practice

Plan to spend at least as much time typing and running code yourself as
you spend reading. Every lesson section that says "your turn" is not
optional — the checkpoints assume you did it.

## Common setup problems

- **`python3: command not found`** (Windows): try `python` instead of
  `python3`. Some Windows installs only register the `python` command.
- **`SyntaxError` right after saving a file**: check for a missing colon
  (`:`) at the end of an `if`, `for`, `while`, `def`, or `class` line —
  by far the most common first mistake.
- **Nothing happens when you run the file**: make sure you saved it, and
  that you're running it from the same folder it's saved in (or using
  the correct path).
