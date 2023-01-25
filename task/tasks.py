from django.contrib.auth import get_user_model
from todolist.celery import app
from django.core.mail import send_mail
from task.models import Task


@app.task
def send_mail_on_status_change(owner_id, task_id, new_status):
    """
    Task for sending an email when model field was changed
    """
    task = Task.objects.get(id=task_id)
    new_status, old_status = ('completed', 'not completed') if new_status else ('not completed', 'completed')
    user = get_user_model().objects.get(id=owner_id)

    subject = 'Your task {} status has been changed'.format(task_id)
    message = 'Dear {},\n\nYour task "{}" status has been changed\n\n'.format(user.username, task.title) + \
              'from "{}" to "{}".'.format(old_status, new_status) + \
              "If it wasn't you, please, check your account security settings."
    mail_sent = send_mail(subject,
                          message,
                          'admin@todolist.com',
                          [user.email])
    return mail_sent
