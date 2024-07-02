from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from projects.models import Task

class Command(BaseCommand):
    help = 'Send reminder emails for tasks due today'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        tasks_due_today = Task.objects.filter(due_date=today)

        for task in tasks_due_today:
            assignee_profile = task.assignee.profile
            subject = f"Reminder: Task '{task.title}' is due today!"
            message = f"Dear {assignee_profile.name},\n\nThis is a reminder that your task '{task.title}' is due today ({task.due_date}). Please ensure you complete it on time."
            recipient_list = [assignee_profile.email]

        send_mail(
            subject,
            message,
            "Aakash0213lama@gmail.com",
            recipient_list,
            fail_silently=False,
        )

        self.stdout.write(self.style.SUCCESS('Successfully sent reminder emails.'))
