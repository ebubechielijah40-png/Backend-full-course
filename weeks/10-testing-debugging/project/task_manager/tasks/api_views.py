from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer


class CategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(CategorySerializer(Category.objects.all(), many=True).data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)

        category_id = request.query_params.get("category")
        if category_id:
            tasks = tasks.filter(category_id=category_id)

        completed = request.query_params.get("completed")
        if completed is not None:
            tasks = tasks.filter(completed=(completed.lower() == "true"))

        return Response(TaskSerializer(tasks, many=True).data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def _get_owned_task(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.owner != request.user:
            return None
        return task

    def get(self, request, pk):
        task = self._get_owned_task(request, pk)
        if task is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(TaskSerializer(task).data)

    def patch(self, request, pk):
        task = self._get_owned_task(request, pk)
        if task is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self._get_owned_task(request, pk)
        if task is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
