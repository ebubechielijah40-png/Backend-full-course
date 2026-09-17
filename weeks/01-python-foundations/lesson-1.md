# Lesson 1 — Python Basics and Data

By the end of this lesson you'll be able to represent one expense (a
name, an amount, a category, and a date) and a list of many expenses,
using Python's built-in data types.

## What Python is, and how to run a file

Python is a programming language: a precise, limited form of English-like
text that a program called an **interpreter** reads and carries out, one
instruction at a time.

You write Python code in a plain text file ending in `.py`, then run it
from a terminal:

```
python3 my_program.py
```

**Task:** Create a file called `hello.py` containing exactly one line:

```python
print("Hello, backend developer")
```

Run it with `python3 hello.py`. You should see the text printed in your
terminal.

**Common error:** `python3: can't open file 'hello.py': No such file or
directory` means your terminal isn't in the same folder as the file. Use
`cd` to move into that folder first, or run `ls` (Mac/Linux) or `dir`
(Windows) to check what's actually there.

## Variables and names

A **variable** is a name that points to a value stored in memory. You
create one by writing a name, `=`, then a value.

```python
expense_name = "Coffee"
```

This is useful because it lets your program refer to a value by a
meaningful name instead of retyping the value everywhere.

Python variable names can use letters, numbers, and underscores, but
can't start with a number, and are case-sensitive (`total` and `Total`
are different names). By convention, Python variable names are written
in `lower_case_with_underscores` — use that style throughout this course.

**Task:** Create variables for one expense: `expense_name`, `amount`,
`category`, `date`. Print each one on its own line.

**Common error:** `NameError: name 'exspense_name' is not defined`
usually means a typo — Python variable names must match exactly,
including spelling.

## Strings, integers, floats, booleans, and None

These are the basic types of value a variable can hold.

- **Strings** (`str`) are text, written in quotes: `"Coffee"`. Useful for
  names, categories, and anything read as text.
- **Integers** (`int`) are whole numbers: `5`. Useful for counts.
- **Floats** (`float`) are numbers with a decimal point: `4.50`. Useful
  for money amounts, since expenses rarely round to whole numbers.
- **Booleans** (`bool`) are `True` or `False`. Useful for yes/no
  questions, like "has this expense been paid?"
- **`None`** represents "no value at all" — different from `0` or an
  empty string. Useful for a value that might not exist yet, like a
  receipt image that hasn't been added.

```python
expense_name = "Coffee"      # str
amount = 4.50                 # float
is_recurring = False          # bool
receipt_file = None           # nothing yet
```

You can check any value's type with `type()`:

```python
print(type(amount))   # <class 'float'>
```

**Common error:** `4.50` and `"4.50"` look similar but are different
types — one is a number you can do math with, the other is text. Mixing
them up causes errors you'll see shortly.

**Checkpoint:** Without running it, what type is `amount` in
`amount = 12`? (Answer: `int`, not `float` — there's no decimal point.)

## Basic operators and comparisons

**Arithmetic operators** (`+`, `-`, `*`, `/`) work on numbers the way
you'd expect, and also let `+` join (concatenate) strings:

```python
total = 4.50 + 3.25         # 7.75
greeting = "Hello, " + "Eli"  # "Hello, Eli"
```

**Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) compare two
values and produce a boolean. This is useful for checking conditions,
like whether an expense is over a budget limit:

```python
is_expensive = amount > 100   # False, since amount is 4.50
```

**Common error:** using a single `=` (assignment) when you meant `==`
(comparison) is one of the most common mistakes in any language. `if
amount = 100:` is a `SyntaxError` in Python — Python catches this one for
you, but it's still worth knowing why.

## Input, output, and type conversion

`print()` shows a value. `input()` asks the user to type something and
always returns it as a string, even if they type a number:

```python
amount_text = input("Enter the amount: ")
amount = float(amount_text)   # convert the text to a number
```

This matters because you can't do math on a string — `"4.50" + 1` raises
an error, while `float("4.50") + 1` works correctly.

**Task:** Write a small script that asks the user for an expense name
and an amount (as text), converts the amount to a `float`, and prints a
sentence combining both, e.g. `You spent 4.5 on Coffee`.

**Common error:** `ValueError: could not convert string to float:
'four fifty'` happens when a user types something that isn't a valid
number. You'll handle this properly with error handling in Lesson 2 —
for now, just know why it happens.

## Lists

A **list** holds an ordered collection of values, written in square
brackets. Useful for holding many expenses.

```python
categories = ["Food", "Transport", "Food", "Entertainment"]
```

Access an item by its **index** (position), starting at `0`:

```python
first_category = categories[0]   # "Food"
```

Change an item by assigning to its index:

```python
categories[1] = "Rideshare"
```

Add an item to the end with `.append()`:

```python
categories.append("Utilities")
```

**Task:** Create a list called `expense_names` with at least three
expense names. Print the second one using indexing. Append a fourth
name.

**Common error:** `IndexError: list index out of range` happens when you
ask for an index that doesn't exist — remember a list of 3 items has
valid indexes `0`, `1`, and `2`, not `3`.

## Dictionaries

A **dictionary** holds key–value pairs, written in curly braces. This is
the natural way to represent *one* expense with named fields, instead of
remembering "position 0 is the name, position 1 is the amount":

```python
expense = {
    "name": "Coffee",
    "amount": 4.50,
    "category": "Food",
    "date": "2026-09-01",
}
```

Access a value by its key:

```python
print(expense["amount"])   # 4.50
```

Change a value by assigning to its key, and add a new key the same way:

```python
expense["amount"] = 5.00
expense["paid"] = True
```

**Task:** Create a dictionary representing one expense with all four
fields (name, amount, category, date). Print its category. Add a new
key called `"notes"` with any text value.

**Common error:** `KeyError: 'amount'` happens when the key doesn't
exist — check spelling and that you used the same key when creating and
reading the dictionary.

## Tuples

A **tuple** is like a list, but it can't be changed after it's created
(it's *immutable*), written in parentheses. Useful for values that
shouldn't accidentally change, like a fixed pair of coordinates or a
fixed set of allowed categories you don't want a bug to modify by
mistake:

```python
allowed_categories = ("Food", "Transport", "Entertainment", "Utilities")
```

Indexing works the same as with lists (`allowed_categories[0]`), but
`allowed_categories[0] = "Rent"` raises a `TypeError`, because tuples
can't be modified.

**Common error:** forgetting the trailing comma in a one-item tuple —
`(1)` is just the number `1` in parentheses, not a tuple. You need
`(1,)`.

## Sets

A **set** holds unique, unordered values, written in curly braces (like
a dictionary, but with values, not pairs). Useful for finding the
distinct categories used across many expenses, with duplicates removed
automatically:

```python
categories_used = {"Food", "Transport", "Food", "Food"}
print(categories_used)   # {"Food", "Transport"} — duplicates removed
```

Sets don't support indexing, since they have no fixed order.

**Checkpoint:** Given `["Food", "Food", "Transport"]`, what would
`set(["Food", "Food", "Transport"])` contain? (Answer: `{"Food",
"Transport"}` — two unique values.)

## Putting it together: a list of expense dictionaries

The natural way to represent *many* expenses is a list of dictionaries —
this is exactly the structure the Week 1 project uses:

```python
expenses = [
    {"name": "Coffee", "amount": 4.50, "category": "Food", "date": "2026-09-01"},
    {"name": "Bus pass", "amount": 25.00, "category": "Transport", "date": "2026-09-02"},
]
```

You can access the second expense's amount with `expenses[1]["amount"]`
— first index into the list, then into the dictionary.

**Guided activity:** Together, build this exact `expenses` list with two
entries, then print the name and category of each one using indexing and
key access.

**Debugging activity:** This code has a bug — find it before running it,
then run it to confirm:

```python
expenses = [
    {"name": "Coffee", "amount": 4.50, "category": "Food"}
]
print(expenses[0]["Amount"])
```

(The bug: the key is `"amount"`, lowercase, not `"Amount"` — dictionary
keys are case-sensitive, so this raises a `KeyError`.)

## Checkpoint

Without running any code, answer:

1. What's the difference between a list and a tuple?
2. How would you access the category of the first expense in a list
   called `expenses`?
3. What does `set([1, 1, 2, 3])` contain?

(Answers: 1 — a list can be changed after creation, a tuple can't. 2 —
`expenses[0]["category"]`. 3 — `{1, 2, 3}`.)

## Independent challenge

Build a list of at least four expense dictionaries by hand (name,
amount, category, date for each). Then, without using a loop yet
(that's Lesson 2), print:

- The total number of expenses, using `len(expenses)`.
- The category of the most expensive one you can find just by looking
  at your own data and indexing directly to it.
