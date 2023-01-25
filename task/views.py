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

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .tasks import send_mail_on_status_change


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    pagination_class = StandartResultSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return super().get_serializer_class()

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
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if request.user != task.owner:
            raise PermissionDenied()
        task.is_completed = True
        task.save()

        owner_id = task.owner_id

        send_mail_on_status_change.delay(str(owner_id), pk)

        serializer = self.serializer_class(instance=task)
        return Response({
            'executed': serializer.data
        })


@receiver(signal=pre_save, sender=Task)
def on_status_change(instance, **kwargs):
    owner_id, pk, is_completed_new = instance.owner_id, instance.pk, instance.is_completed
    is_completed_old = Task.objects.get(id=pk).is_completed
    if is_completed_old != is_completed_new:
        send_mail_on_status_change.delay(instance.owner_id, instance.pk, is_completed_new)
