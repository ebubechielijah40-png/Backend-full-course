"""
Debugging Exercise 1 — Broken ownership check

To reproduce: replace tasks/api_views.py's TaskDetailView._get_owned_task
method with the version below, then run:
    python3 manage.py test tasks

Expected result: test_other_user_cannot_view_task and
test_other_user_cannot_delete_task should FAIL.

The bug: this version fetches the task but never checks it belongs to
the requesting user before returning it — any authenticated user can
view or delete any task by guessing its ID.
"""

def _get_owned_task(self, request, pk):
    from django.shortcuts import get_object_or_404
    from .models import Task
    task = get_object_or_404(Task, pk=pk)
    return task  # BUG: no ownership check before returning
