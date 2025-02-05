from django.db import models

# Create your models here.
from events.models import Registration

class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.registration.student.user.username} - {self.registration.event.name}"
