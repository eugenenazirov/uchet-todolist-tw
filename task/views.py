from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task.models import Task
from task.permissions import IsOwnerOrReadOnly
from task.serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    @action(methods=['post'], detail=True)
    def execute(self, request, pk):
        task = get_object_or_404(self.queryset, pk=pk)
        task.is_completed = True
        task.save()

        serializer = self.serializer_class(instance=task)
        return Response({
            'executed': serializer.data
        })
