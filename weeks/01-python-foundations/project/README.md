# Project: Command-Line Expense Tracker

## Project description

A command-line Python program for tracking personal expenses: add them,
list them, see totals, filter by category, delete one, and have them
saved automatically so they're still there the next time you run the
program.

## Problem being solved

Tracking a handful of expenses in your head or on paper doesn't scale
and doesn't let you ask questions like "how much did I spend on food
this month?" This project solves that with a small, reliable program —
and, not incidentally, is a working miniature of what every backend
application does: take input, apply rules to it, store it, and answer
questions about it later.

## What the application does

On startup, it loads any previously saved expenses from
`expenses.json`. It then shows a menu, repeating until the user chooses
to exit:

1. Add an expense
2. List all expenses
3. View total spending
4. Filter by category
5. Delete an expense
6. Exit

Every add or delete is saved to `expenses.json` immediately, so no
change is ever lost even if the program is closed unexpectedly.

## Features

- Add an expense (name, amount, category, date)
- List all expenses
- View total spending
- Filter expenses by category
- Delete an expense by name
- Save expenses to JSON
- Load expenses from JSON
- Handle invalid input (bad numbers, empty names, negative amounts)
- Handle a missing or empty data file
- Exit safely

## User interaction flow

```
Expense Tracker
1. Add an expense
2. List all expenses
3. View total spending
4. Filter by category
5. Delete an expense
6. Exit

Choose an option (1-6):
```

The user types a number, the program performs that action (asking for
further input if needed — e.g. the expense's name and amount), then the
menu is shown again.

## Data structure

Each expense is a dictionary:

```python
{
    "name": "Coffee",
    "amount": 4.50,
    "category": "Food",
    "date": "2026-09-01",
}
```

All expenses together are a list of these dictionaries — the exact
structure taught in Lesson 1 and saved as JSON in Lesson 3.

## Required functions

| Function | Purpose |
|---|---|
| `load_expenses(filename)` | Load expenses from a JSON file, or return `[]` if missing/empty/invalid |
| `save_expenses(expenses, filename)` | Write the expense list to a JSON file |
| `add_expense(expenses, name, amount, category, date)` | Add a validated new expense |
| `list_expenses(expenses)` | Print every expense |
| `calculate_total(expenses)` | Return the sum of all amounts |
| `find_expenses_by_category(expenses, category)` | Return matching expenses |
| `delete_expense(expenses, name)` | Remove the first matching expense, return whether one was found |
| `prompt_for_amount()` | Repeatedly ask for input until a valid, non-negative number is given |
| `run()` | The main menu loop tying everything together |

## File structure

```
project/
├── README.md            ← this file
├── requirements.txt      ← no external packages needed for Week 1
└── expense_tracker.py    ← the complete application
```

`expenses.json` is created automatically the first time an expense is
added — it isn't part of the repository itself, since it's user data
generated at runtime.

---

## Step-by-step build process

This is how the project is built across Week 1's three sessions —
follow it in order rather than jumping to the finished code.

### Stage 1 — Represent one expense

**What we're adding:** a single Python dictionary representing one
expense.
**Why:** before handling many expenses, confirm the shape of one is
right.
**What changes:** nothing in a file yet — this is explored directly, as
in Lesson 1.
**Code:**
```python
expense = {"name": "Coffee", "amount": 4.50, "category": "Food", "date": "2026-09-01"}
```
**How to run it:** paste it into a Python file and `print(expense)`.
**How to verify:** the printed dictionary matches what you typed.
**What could go wrong:** mismatched quotes or a missing comma between
keys causes a `SyntaxError` — Python will point at the line.

### Stage 2 — Represent multiple expenses

**What we're adding:** a list holding several expense dictionaries.
**Why:** a real tracker needs more than one expense.
**What changes:** wrap several Stage 1-style dictionaries in a list
called `expenses`.
**Code:**
```python
expenses = [
    {"name": "Coffee", "amount": 4.50, "category": "Food", "date": "2026-09-01"},
    {"name": "Bus pass", "amount": 25.00, "category": "Transport", "date": "2026-09-02"},
]
```
**How to verify:** `print(len(expenses))` shows `2`.
**What could go wrong:** a missing comma between dictionaries in the
list causes a `SyntaxError`.

### Stage 3 — Display expenses

**What we're adding:** the `list_expenses()` function.
**Why:** printing expenses by hand doesn't scale; a function that loops
through any list of expenses does.
**Which function:** `list_expenses(expenses)` — see the finished code in
`expense_tracker.py` for the exact version, which also handles the
empty-list case added in a later stage.
**How to run it:** call `list_expenses(expenses)` after Stage 2's list.
**How to verify:** every expense prints, one per line.
**What could go wrong:** forgetting to loop (`for expense in
expenses:`) and instead trying to print the whole list's fields at once
causes a `TypeError`, since a list itself has no `"name"` key.

### Stage 4 — Add a new expense

**What we're adding:** the `add_expense()` function (without validation
yet — that's Stage 10).
**Why:** expenses need to come from user input, not be hardcoded.
**Which function:** `add_expense(expenses, name, amount, category,
date)` appends a new dictionary to the list.
**How to verify:** call it, then call `list_expenses(expenses)` and
confirm the new expense appears.
**What could go wrong:** forgetting that lists are mutable — if you
`return` a *new* list instead of mutating `expenses` with `.append()`,
the caller's original list won't actually change unless they reassign
it. This project deliberately mutates the list in place to avoid that
confusion.

### Stage 5 — Calculate totals

**What we're adding:** the `calculate_total()` function.
**Why:** users need to know how much they've spent overall.
**Which function:** `calculate_total(expenses)`, looping and summing
`expense["amount"]`.
**How to verify:** compare the function's result to adding the amounts
yourself by hand for a small test list.
**What could go wrong:** starting the running total at `0` (an `int`)
instead of `0.0` still works in Python (`int` and `float` mix freely in
arithmetic), but starting it as a string `"0"` would cause a
`TypeError` the first time a number is added to it.

### Stage 6 — Filter by category

**What we're adding:** the `find_expenses_by_category()` function.
**Why:** users need to answer questions like "how much did I spend on
food?" which requires isolating a category first.
**Which function:** `find_expenses_by_category(expenses, category)`,
returning a new list of matches (case-insensitive, so "food" and "Food"
both match).
**How to verify:** filter a test list and confirm only matching entries
come back.
**What could go wrong:** comparing categories with `==` directly (not
`.lower()` on both sides) means "Food" and "food" won't match, which
will surprise users who don't type consistently.

### Stage 7 — Delete an expense

**What we're adding:** the `delete_expense()` function.
**Why:** users need to correct mistakes without editing the file by
hand.
**Which function:** `delete_expense(expenses, name)`, returning `True`
if something was removed, `False` otherwise, so the caller can give
correct feedback either way.
**How to verify:** delete an existing name (confirm `True` and the list
shrinks) and a nonexistent name (confirm `False` and nothing changes).
**What could go wrong:** modifying a list with `.remove()` while
looping over that same list with a plain `for` loop can skip elements
in some cases; this project's loop returns immediately after the first
match, which avoids the problem, but it's worth knowing why looping and
mutating the same list at once is generally risky.

### Stage 8 — Save data to JSON

**What we're adding:** the `save_expenses()` function.
**Why:** without this, every stage above is lost the moment the program
ends.
**Which function:** `save_expenses(expenses, filename)`, using
`json.dump(expenses, file, indent=2)`.
**How to verify:** call it, then open the resulting `.json` file in a
text editor and confirm it's readable and matches your data.
**What could go wrong:** forgetting `indent=2` still works, but produces
one unreadable line of JSON — harmless functionally, just harder for a
human to check by eye.

### Stage 9 — Load data from JSON

**What we're adding:** the `load_expenses()` function.
**Why:** saved data is only useful if the program reads it back on
startup.
**Which function:** `load_expenses(filename)`, using `json.load`.
**How to verify:** save some expenses, restart your Python session
(or script), load them, and confirm they match.
**What could go wrong:** trying to load before any file has ever been
saved raises `FileNotFoundError` — handled properly in the next stage.

### Stage 10 — Handle invalid input

**What we're adding:** validation inside `add_expense()`
(`ValueError` for an empty name or a negative amount), a
missing/empty/invalid-file check inside `load_expenses()`, and the
`prompt_for_amount()` helper that keeps asking until it gets a valid
number.
**Why:** a real application must not crash because of bad input — it
should say what's wrong and let the user try again.
**Which functions change:** `add_expense()`, `load_expenses()`, and the
new `prompt_for_amount()`.
**How to verify:** try adding an expense with a negative amount or an
empty name (both should raise a clear error, caught and shown nicely by
the menu loop); try loading before `expenses.json` exists (should
return `[]`, not crash); try typing a non-numeric amount at the
`prompt_for_amount()` prompt (should re-ask rather than crash).
**What could go wrong:** catching `Exception` broadly instead of the
specific `ValueError`/`FileNotFoundError`/`json.JSONDecodeError` would
hide real bugs along with expected bad input — this project deliberately
catches only the specific errors it expects.

### Stage 11 — Organize the code

**What we're adding:** nothing new functionally — this stage groups the
functions above into clear sections (persistence, core operations,
input helpers, menu/main loop) and adds the `run()` function and the
`if __name__ == "__main__":` guard, matching the final
`expense_tracker.py`.
**Why:** a program that works but reads as one long, unorganized script
is hard to maintain — the same reasoning covered in Lesson 2 for why
functions matter.
**How to verify:** the program behaves identically to before this stage;
only its internal organization changed.
**What could go wrong:** nothing behavior-related — this is a pure
refactor. If behavior does change during a refactor like this, that's a
sign something was accidentally altered, not just moved.

### Stage 12 — Review and improve the application

**What we're adding:** the manual test pass described below, confirming
every feature and edge case actually works together in the finished
`expense_tracker.py`.
**Why:** individually-tested functions can still fail once combined —
this stage catches that.
**How to verify:** follow "How to test it manually" below in full.
**What could go wrong:** skipping this stage is how small integration
bugs (for example, a menu option calling the wrong function) reach
students undetected.

---

## Complete code

The finished, working application is `expense_tracker.py` in this same
folder. It matches every stage above — read it alongside the stages if
you want to see exactly where each piece landed.

## How to run it

```
python3 expense_tracker.py
```

## How to test it manually

Work through this checklist against the running program:

1. Run it for the first time (no `expenses.json` yet) — the menu should
   appear with no error.
2. Add an expense — confirm option 2 (list) shows it.
3. Add two more expenses in different categories.
4. Check the total (option 3) matches the sum by hand.
5. Filter by one of the categories you used (option 4) — confirm only
   matching expenses appear.
6. Delete one expense by name (option 5) — confirm it's gone from the
   list.
7. Try deleting a name that doesn't exist — confirm you get a clear
   message, not a crash.
8. Try adding an expense with a non-numeric amount — confirm it
   re-prompts instead of crashing.
9. Exit (option 6), then run the program again — confirm your remaining
   expenses are still there (this is the persistence check).
10. Manually empty `expenses.json` (make it a blank file) and run the
    program again — confirm it starts with no expenses instead of
    crashing.

## Common errors

- **`FileNotFoundError` on first run:** shouldn't happen — `load_expenses`
  checks for the file's existence first. If you see this, check that
  you're running the exact code in `expense_tracker.py`, not a partial
  copy missing that check.
- **`KeyError: 'amount'`:** usually means `expenses.json` was hand-edited
  and a key is missing or misspelled — delete the file and let the
  program recreate it.
- **Menu accepts a number but does nothing:** check the menu-loop's
  `if`/`elif` chain for a typo in the expected choice string (e.g.
  comparing to `"1 "` with a trailing space instead of `"1"`).

## Possible improvements

(Not required for Week 1 — listed for students who finish early or want
to keep exploring.)

- Sort expenses by date or amount before listing them.
- Support editing an existing expense instead of only deleting it.
- Add a monthly summary (total per month).
- Store the currency symbol as a setting instead of hardcoding `$`.

## Final checklist

- [ ] All 12 build stages completed and each verified individually.
- [ ] Every feature in "Features" above works when tested manually.
- [ ] All 10 items in "How to test it manually" pass.
- [ ] The program never crashes on invalid input during manual testing.
- [ ] `expenses.json` is created automatically and updates immediately
      after every add or delete.
- [ ] The code is organized into the functions listed in "Required
      functions," not one long unstructured script.
