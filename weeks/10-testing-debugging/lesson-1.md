# Lesson 1 — Why and How to Test; Unit Tests for Models

## Why automated tests

Manual testing (Weeks 3–9's "How to test it manually" checklists) works,
but doesn't scale — every change means re-clicking through the same
checklist by hand, and it's easy to forget a case. An **automated test**
runs the same check every time, in seconds, and never forgets an edge
case once it's written.

## Django's TestCase

```python
# tasks/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Task

class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="sam", password="pass123")

    def test_task_string_representation(self):
        task = Task.objects.create(title="Write report", owner=self.user)
        self.assertEqual(str(task), "Write report")

    def test_task_defaults_to_not_completed(self):
        task = Task.objects.create(title="New task", owner=self.user)
        self.assertFalse(task.completed)
```

`setUp` runs before every test method, giving each one a clean starting
point — this matters because tests shouldn't depend on each other's
leftover data. Django's `TestCase` also wraps each test in a transaction
that's rolled back afterward, so tests never leave data behind for the
next one.

Run tests with:

```
python3 manage.py test
```

**Task:** Add a test confirming a `Category`'s `str()` returns its name.

**Common error:** `assertEqual(str(task), "Write report")` failing
because you compared to the wrong value is the test doing its job —
resist the urge to "fix" a failing test by changing its expectation
without first checking whether the *code* is actually wrong.

## Checkpoint

Why does each test method get a fresh `self.user` from `setUp` instead
of creating one user once for the whole test file? (So tests don't
depend on order or leftover state from each other — each test should be
runnable on its own.)
