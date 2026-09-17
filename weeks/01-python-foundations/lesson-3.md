# Lesson 3 — Files, JSON, Virtual Environments and Basic Classes

By the end of this lesson, the expense tracker will save its data to a
file and load it back — meaning your expenses survive closing and
reopening the program, which is the first real step toward the
persistent storage every backend application needs.

## Why applications need to save data

Right now, everything the expense tracker knows lives in a Python
variable, which exists only in your computer's memory while the program
is running. **Data in memory disappears the moment the program stops.**
A real application — including every Django app you'll build starting
Week 3 — needs **persistence**: a way to save data somewhere that
survives the program ending, so it's there again next time. This week,
"somewhere" is a file; from Week 4 onward, it will be a database, but
the underlying need is identical.

## Reading and writing files

Python opens files with the built-in `open()` function, and the safest
way to use it is with a `with` block, which automatically closes the
file when you're done, even if an error happens partway through:

```python
# Writing to a file (overwrites it if it already exists)
with open("notes.txt", "w") as file:
    file.write("First expense: Coffee, 4.50\n")

# Reading a file
with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)
```

`"w"` mode overwrites the file; `"a"` mode appends to the end instead.

**Common error:** `FileNotFoundError: [Errno 2] No such file or
directory: 'notes.txt'` happens when you try to *read* a file that
doesn't exist yet. Writing with `"w"` mode creates the file if it's
missing, but reading never does.

## JSON

**JSON** (JavaScript Object Notation) is a text format for structured
data that looks almost exactly like Python dictionaries and lists. It's
useful because it's a standard way to save structured data to a file (or
send it over a network, which you'll do starting Week 2) that many
languages, not just Python, can read.

Python's built-in `json` module converts between Python objects and
JSON text:

- `json.dumps(data)` — converts a Python object to a JSON **string**.
- `json.loads(text)` — converts a JSON string back to a Python object.
- `json.dump(data, file)` — converts a Python object and writes it
  directly to an open file.
- `json.load(file)` — reads JSON directly from an open file and converts
  it to a Python object.

```python
import json

expenses = [
    {"name": "Coffee", "amount": 4.50, "category": "Food", "date": "2026-09-01"},
]

# Save to a file
with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=2)

# Load from a file
with open("expenses.json", "r") as file:
    loaded_expenses = json.load(file)

print(loaded_expenses)
```

The `indent=2` argument makes the saved file human-readable, with proper
line breaks and spacing — worth doing for any file a person might open
directly.

**Task:** Save the `expenses` list you built in Lesson 1 to a file called
`expenses.json` using `json.dump`, then write separate code that loads it
back into a new variable and prints it, confirming the data matches.

**Common error:** `json.decoder.JSONDecodeError` when loading usually
means the file is empty or contains invalid JSON (for example, if a
previous save was interrupted). This is exactly why the project handles
a missing or empty file as a special case — see the project README.

**Guided activity:** Together, wrap the save code in a function
`save_expenses(expenses, filename)` and the load code in a function
`load_expenses(filename)` that returns an empty list if the file doesn't
exist yet (hint: use `try`/`except FileNotFoundError` from Lesson 2).

## Virtual environments and pip

A **virtual environment** is an isolated space for a Python project's
installed packages, separate from your system's Python and from other
projects. This matters because different projects often need different
versions of the same package, and without isolation, installing one
project's requirements can silently break another's.

Create and activate one (macOS/Linux):

```
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```
python -m venv venv
venv\Scripts\activate
```

Once activated, your terminal prompt usually shows `(venv)`. From here,
`pip` — Python's package installer — installs packages only into this
environment:

```
pip install requests
```

Week 1's project doesn't need any external packages, so you won't
install anything yet, but you should still create the habit now: every
project from here on, including every Django project starting Week 3,
begins with a fresh virtual environment.

**Common error:** running `pip install` without activating the virtual
environment first installs the package globally instead — if a later
`import` fails inside your project, check whether your virtual
environment is actually activated (look for `(venv)` in your prompt).

## Basic classes

A **class** is a template for creating objects that bundle related data
(**attributes**) and behavior (**methods**) together. Everything you've
built so far — a dictionary with `name`, `amount`, `category`, `date` —
works fine, and a class isn't always a better choice. A class is worth
it once an object has behavior of its own, not just data. For example,
if you want an expense to know how to describe itself:

```python
class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def describe(self):
        return f"{self.name}: ${self.amount} ({self.category}) on {self.date}"
```

`__init__` is a special method that runs automatically when you create a
new `Expense`, setting up its attributes. `self` refers to the specific
object being created or used — it's how a method reaches its own
attributes.

```python
coffee = Expense("Coffee", 4.50, "Food", "2026-09-01")
print(coffee.name)          # "Coffee"
print(coffee.describe())    # "Coffee: $4.5 (Food) on 2026-09-01"
```

This is not a required change to the Week 1 project — dictionaries
remain perfectly correct throughout this course's Python-only projects.
It's shown here only so a class's basic shape (attributes plus methods)
is familiar before Week 4, where Django models — which are classes — are
introduced.

**Common error:** forgetting `self` as the first parameter of a method
causes `TypeError: describe() takes 0 positional arguments but 1 was
given` — Python automatically passes the object itself as the first
argument to every method, so `self` must always be there to receive it.

## Checkpoint

1. Why does an application need to save data to a file (or database)
   instead of just keeping it in a variable?
2. What does `json.dump()` do, compared to `json.dumps()`?
3. What's the difference between an attribute and a method on a class?

(Answers: 1 — because data in memory disappears when the program stops;
a file/database survives the program ending. 2 — `json.dump()` writes
directly to an open file; `json.dumps()` returns a JSON string you'd
have to write yourself. 3 — an attribute is a piece of data stored on
the object; a method is a function defined on the class that can act on
that data.)

## Independent challenge

Extend your menu-driven program from Lesson 2 so that:

- On startup, it loads expenses from `expenses.json` if the file exists,
  or starts with an empty list if it doesn't.
- Every time an expense is added or deleted, it immediately saves the
  updated list back to `expenses.json`.
- Test it by adding an expense, closing the program, and reopening it —
  the expense should still be there.

This is, functionally, the complete Week 1 project — see `project/README.md`
for the full staged build if you want to compare your approach.
