from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

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


class CategoryModelTests(TestCase):
    def test_category_string_representation(self):
        category = Category.objects.create(name="Work")
        self.assertEqual(str(category), "Work")


class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="sam", password="pass123")
        self.other_user = User.objects.create_user(username="jordan", password="pass123")
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name="Work")

    def test_create_task(self):
        response = self.client.post("/api/tasks/", {"title": "New task"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().owner, self.user)

    def test_cannot_create_task_with_blank_title(self):
        response = self.client.post("/api/tasks/", {"title": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_task_with_invalid_category(self):
        response = self.client.post("/api/tasks/", {"title": "Bad", "category": 999})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_only_sees_own_tasks(self):
        Task.objects.create(title="Mine", owner=self.user)
        Task.objects.create(title="Not mine", owner=self.other_user)
        response = self.client.get("/api/tasks/")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Mine")

    def test_filter_by_completed(self):
        Task.objects.create(title="Done", owner=self.user, completed=True)
        Task.objects.create(title="Not done", owner=self.user, completed=False)
        response = self.client.get("/api/tasks/?completed=true")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Done")

    def test_filter_by_category(self):
        other_category = Category.objects.create(name="Home")
        Task.objects.create(title="Work task", owner=self.user, category=self.category)
        Task.objects.create(title="Home task", owner=self.user, category=other_category)
        response = self.client.get(f"/api/tasks/?category={self.category.id}")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Work task")

    def test_owner_can_view_own_task(self):
        task = Task.objects.create(title="Mine", owner=self.user)
        response = self.client.get(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_cannot_view_task(self):
        task = Task.objects.create(title="Not mine", owner=self.other_user)
        response = self.client.get(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_other_user_cannot_delete_task(self):
        task = Task.objects.create(title="Not mine", owner=self.other_user)
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Task.objects.filter(id=task.id).exists())

    def test_owner_can_delete_own_task(self):
        task = Task.objects.create(title="Mine", owner=self.user)
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_owner_can_update_own_task(self):
        task = Task.objects.create(title="Mine", owner=self.user)
        response = self.client.patch(f"/api/tasks/{task.id}/", {"completed": True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_unauthenticated_request_is_rejected(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
