from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(TaskSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "deadline", "is_completed")
