from django.db import models

# Create your models here.
from events.models import Event
from authentication.models import StudentProfile

class CustomSubmission(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)  # Example: "ppt_link", "github_repo"
    field_value = models.TextField()  # Stores URL or uploaded file reference

    def __str__(self):
        return f"{self.student.user.username} - {self.field_name} for {self.event.name}"
