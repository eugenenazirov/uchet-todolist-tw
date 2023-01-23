from django.db import models
from django.conf import settings


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
