# Lesson 2 — Testing Views and API Endpoints

## DRF's API test client

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="sam", password="pass123")
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        response = self.client.post("/api/tasks/", {"title": "New task"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_cannot_create_task_with_blank_title(self):
        response = self.client.post("/api/tasks/", {"title": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_see_others_tasks(self):
        other_user = User.objects.create_user(username="jordan", password="pass123")
        Task.objects.create(title="Jordan's task", owner=other_user)
        response = self.client.get("/api/tasks/")
        self.assertEqual(len(response.data), 0)

    def test_unauthenticated_request_is_rejected(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

`force_authenticate` logs in a test client as a given user without
needing a real login request — useful for testing endpoints in
isolation. This matters because it turns every "How to test it manually"
checklist item from Weeks 7–9 into something that runs automatically,
every time, forever.

**Task:** Add a test confirming that a second user gets a `403` when
trying to `DELETE` the first user's task (Week 9's ownership check).

**Common error:** forgetting `force_authenticate` and getting an
unexpected `401` on every test — a good reminder that authentication is
checked on every request, tests included.

## Checkpoint

Why is `test_user_cannot_see_others_tasks` a more important test than
`test_create_task`? (Both matter, but the ownership test protects
against a security bug — data leaking between users — which is a far
more serious failure than a broken create feature.)
