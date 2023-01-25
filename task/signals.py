from django.dispatch import receiver
from django.db.models.signals import pre_save
from task.tasks import send_mail_on_status_change
from task.models import Task


@receiver(signal=pre_save, sender=Task)
def on_status_change(instance, **kwargs):
    owner_id, pk, is_completed_new = instance.owner_id, instance.pk, instance.is_completed
    is_completed_old = Task.objects.get(id=pk).is_completed
    if is_completed_old != is_completed_new:
        send_mail_on_status_change.delay(instance.owner_id, instance.pk, is_completed_new)
