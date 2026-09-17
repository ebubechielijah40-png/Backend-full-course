"""
Debugging Exercise 2 — Broken completed filter

To reproduce: replace the `completed` filtering block inside
TaskListCreateView.get in tasks/api_views.py with the version below,
then run:
    python3 manage.py test tasks

Expected result: test_filter_by_completed should FAIL — not with a
wrong result, but with an unhandled ValidationError ("'true' value must
be either True or False"), because the string "true" is passed straight
into a BooleanField filter instead of being converted to an actual
Python bool first.

The bug: comparing/filtering with the raw query string directly instead
of converting it — `completed.lower() == "true"` (a real boolean) is
what belongs here, not the raw string.
"""

def get(self, request):
    from .models import Task
    tasks = Task.objects.filter(owner=request.user)

    category_id = request.query_params.get("category")
    if category_id:
        tasks = tasks.filter(category_id=category_id)

    completed = request.query_params.get("completed")
    if completed is not None:
        tasks = tasks.filter(completed=completed)  # BUG: string, not bool

    from .serializers import TaskSerializer
    from rest_framework.response import Response
    return Response(TaskSerializer(tasks, many=True).data)
