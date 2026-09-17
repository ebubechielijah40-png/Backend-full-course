"""
Command-Line Expense Tracker
Week 1 project — Backend Development with Python & Django

A small command-line application that lets you add, list, total,
filter, and delete expenses, saving them to a JSON file so they persist
between runs.

Run it with:
    python3 expense_tracker.py
"""

import json
import os

DATA_FILE = "expenses.json"


# ---------------------------------------------------------------------
# Persistence: loading and saving expenses
# ---------------------------------------------------------------------

def load_expenses(filename=DATA_FILE):
    """Load expenses from a JSON file.

    Returns an empty list if the file doesn't exist yet, or if it
    exists but is empty or contains invalid JSON (e.g. from an
    interrupted save).
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print(f"Warning: {filename} contained invalid data. Starting fresh.")
        return []


def save_expenses(expenses, filename=DATA_FILE):
    """Save the given list of expenses to a JSON file."""
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=2)


# ---------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------

def add_expense(expenses, name, amount, category, date):
    """Add a new expense to the list. Raises ValueError for bad input."""
    if not name.strip():
        raise ValueError("Expense name cannot be empty")
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    expenses.append({
        "name": name,
        "amount": amount,
        "category": category,
        "date": date,
    })


def list_expenses(expenses):
    """Print every expense. Prints a message if there are none."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} — ${expense['amount']:.2f} "
              f"({expense['category']}) on {expense['date']}")


def calculate_total(expenses):
    """Return the sum of all expense amounts."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


def find_expenses_by_category(expenses, category):
    """Return a new list containing only expenses matching the category
    (case-insensitive)."""
    return [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def delete_expense(expenses, name):
    """Remove the first expense whose name matches (case-insensitive).

    Returns True if an expense was removed, False if none matched.
    """
    for expense in expenses:
        if expense["name"].lower() == name.lower():
            expenses.remove(expense)
            return True
    return False


# ---------------------------------------------------------------------
# Input helpers (keep invalid input from crashing the program)
# ---------------------------------------------------------------------

def prompt_for_amount():
    """Ask the user for an amount, repeating until it's a valid,
    non-negative number."""
    while True:
        text = input("Amount: ")
        try:
            amount = float(text)
        except ValueError:
            print("That's not a valid number. Try again, e.g. 4.50")
            continue

        if amount < 0:
            print("Amount cannot be negative. Try again.")
            continue

        return amount


# ---------------------------------------------------------------------
# Menu and main program loop
# ---------------------------------------------------------------------

MENU_TEXT = """
Expense Tracker
1. Add an expense
2. List all expenses
3. View total spending
4. Filter by category
5. Delete an expense
6. Exit
"""


def run():
    expenses = load_expenses()

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Expense name: ").strip()
            amount = prompt_for_amount()
            category = input("Category: ").strip()
            date = input("Date (e.g. 2026-09-01): ").strip()
            try:
                add_expense(expenses, name, amount, category, date)
                save_expenses(expenses)
                print("Expense added.")
            except ValueError as error:
                print(f"Could not add expense: {error}")

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total spending: ${total:.2f}")

        elif choice == "4":
            category = input("Category to filter by: ").strip()
            matches = find_expenses_by_category(expenses, category)
            list_expenses(matches)

        elif choice == "5":
            name = input("Name of expense to delete: ").strip()
            if delete_expense(expenses, name):
                save_expenses(expenses)
                print("Expense deleted.")
            else:
                print("No expense found with that name.")

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    run()
