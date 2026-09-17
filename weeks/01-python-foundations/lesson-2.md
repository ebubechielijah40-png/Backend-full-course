# Lesson 2 — Functions, Decisions, Loops and Errors

By the end of this lesson, the expense data from Lesson 1 will be
managed by real functions — `add_expense()`, `list_expenses()`,
`calculate_total()`, `find_expenses_by_category()`, and
`delete_expense()` — instead of one-off lines of code, and your program
will survive bad input instead of crashing.

## `if`, `elif`, `else`

An `if` statement runs code only when a condition is true. This is
useful anywhere your program needs to behave differently depending on
data — for example, warning about an unusually large expense.

```python
amount = 150
if amount > 100:
    print("This is a large expense.")
elif amount > 50:
    print("This is a moderate expense.")
else:
    print("This is a small expense.")
```

Only one branch runs — Python checks them in order and stops at the
first true condition.

**Common error:** forgetting the colon (`:`) at the end of the `if` line,
or mismatched indentation inside the block — Python uses indentation
(consistently 4 spaces) to know what's inside the `if`.

## `for` loops

A `for` loop runs a block of code once for each item in a collection.
This is exactly what you need to go through every expense instead of
indexing them one at a time by hand:

```python
expenses = [
    {"name": "Coffee", "amount": 4.50, "category": "Food"},
    {"name": "Bus pass", "amount": 25.00, "category": "Transport"},
]

for expense in expenses:
    print(expense["name"], expense["amount"])
```

Each time through the loop, `expense` is the next dictionary in the
list.

**Task:** Using the `expenses` list you built in Lesson 1's independent
challenge, write a `for` loop that prints every expense's name and
amount on its own line.

## `while` loops, `break`, and `continue`

A `while` loop repeats as long as a condition stays true — useful for
something like a menu that keeps asking the user for a choice until they
choose to quit:

```python
running = True
while running:
    choice = input("Type 'quit' to stop: ")
    if choice == "quit":
        running = False
```

`break` exits a loop immediately; `continue` skips to the next round of
the loop without finishing the current one:

```python
for expense in expenses:
    if expense["amount"] == 0:
        continue   # skip zero-amount expenses
    print(expense["name"])
```

**Common error:** a `while True:` loop with no way to become false and
no `break` inside it runs forever — if your program seems frozen, this
is the first thing to check (press Ctrl+C to stop it).

## Functions

A **function** is a named, reusable block of code. This matters a great
deal in backend development: without functions, every time you want to
"add an expense," you'd retype the same steps, and fixing a bug would
mean fixing it in every copy. With a function, you fix the logic once,
in one place, and every part of the program that calls it is fixed
automatically. This also makes code far easier to debug — if adding an
expense is broken, you know exactly which function to look at.

```python
def add_expense(expenses, name, amount, category, date):
    new_expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date,
    }
    expenses.append(new_expense)
```

`expenses`, `name`, `amount`, `category`, and `date` are **parameters** —
values the function needs to do its job, supplied when it's called:

```python
expenses = []
add_expense(expenses, "Coffee", 4.50, "Food", "2026-09-01")
```

### Return values

A function can send a value back to whoever called it, using `return`:

```python
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total

total_spent = calculate_total(expenses)
```

### Default parameters

A parameter can have a default value, used if the caller doesn't supply
one:

```python
def add_expense(expenses, name, amount, category, date="unknown"):
    ...
```

Now `add_expense(expenses, "Coffee", 4.50, "Food")` works without
specifying a date.

### Scope, at a beginner level

A variable created inside a function only exists inside that function —
this is called its **scope**. This is why `total` inside
`calculate_total()` doesn't clash with any variable named `total`
elsewhere in your program; each function has its own private space for
the variables it creates.

**Guided activity:** Together, write `list_expenses(expenses)`, a
function that loops through `expenses` and prints each one, and
`find_expenses_by_category(expenses, category)`, a function that
returns a new list containing only expenses matching that category.

**Task:** Write `delete_expense(expenses, name)`, a function that
removes the first expense whose name matches, and returns `True` if it
found and removed one, `False` if it didn't. Hint: loop through
`expenses`, check each `expense["name"]`, and use `expenses.remove(...)`
when you find a match — then `return` immediately.

**Common error:** a function that computes a value but never uses
`return` gives back `None` to the caller — if `print(calculate_total(
expenses))` shows `None`, check that every path through the function
ends in a `return` statement.

## `try`, `except`, `else`, `finally`

Some operations can fail in ways your program should survive rather than
crash on — like converting user-typed text to a number. A `try` block
lets you attempt something risky and handle the failure gracefully:

```python
try:
    amount = float(input("Enter the amount: "))
except ValueError:
    print("That's not a valid number. Please try again.")
else:
    print(f"Got a valid amount: {amount}")
finally:
    print("Done processing this input.")
```

- The `except` block runs only if the `try` block raised that specific
  error.
- The `else` block runs only if the `try` block succeeded with no error.
- The `finally` block always runs, whether there was an error or not —
  useful for cleanup code that must happen either way.

This matters for backend development specifically because a real
application must never crash just because a user typed something
unexpected — it needs to respond sensibly instead.

### Raising exceptions

You can also raise an error deliberately, when your own code detects a
problem:

```python
def add_expense(expenses, name, amount, category, date):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    ...
```

This stops the function immediately and signals exactly what went
wrong, which is more useful to whoever calls the function than letting
it silently store bad data.

**Debugging activity:** This function is supposed to safely convert
user input to a float, returning `None` on invalid input, but it has a
bug — find and fix it:

```python
def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None
    print("Converted successfully")
```

(The bug: the `print` after `return` in the `try` block never runs,
since `return` exits the function immediately — the line is dead code
and should either be removed or moved before the `return`.)

## Modules and imports

A **module** is a file of Python code you can reuse in another file with
`import`. Python's standard library ships with many useful modules —
for example, `json` (used in Lesson 3):

```python
import json
```

This matters because it means you don't have to write everything from
scratch — much of what a backend needs (working with dates, files, data
formats) is already available once you `import` it.

## Checkpoint

1. What's the difference between `break` and `continue`?
2. Why does using functions make a program easier to debug?
3. What's the difference between `except` and `finally`?

(Answers: 1 — `break` exits the loop entirely, `continue` skips to the
next iteration. 2 — because each piece of logic exists in one place, so
a bug only needs to be fixed once, and you know exactly which function
to check. 3 — `except` runs only if that specific error occurred;
`finally` always runs regardless.)

## Independent challenge

Combine everything from this lesson: write a small menu-driven loop
(using `while`) that lets a user repeatedly choose to add an expense,
list all expenses, see the total, or quit — using the functions you
wrote in this lesson, and using `try`/`except` so an invalid amount
doesn't crash the program.
