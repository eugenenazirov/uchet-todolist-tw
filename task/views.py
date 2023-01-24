from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from task.models import Task
from task.paginations import StandartResultSetPagination
from task.permissions import IsOwnerOrReadOnly
from task.serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    pagination_class = StandartResultSetPagination

    def get_queryset(self):
        """
        Get queryset for current user
        :return: QuerySet
        """
        return Task.objects.filter(owner=self.request.user)

    @action(methods=['post'], detail=True)
    def execute(self, request, pk):
        """
        Execute endpoint allows POST requests to change task status.
        This operation available for task owner user only.
        """
        task = get_object_or_404(self.queryset, pk=pk)
        if request.user != task.owner:
            raise PermissionDenied()
        task.is_completed = True
        task.save()

        serializer = self.serializer_class(instance=task)
        return Response({
            'executed': serializer.data
        })
