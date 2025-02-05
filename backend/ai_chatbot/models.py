from django.db import models

# Create your models here.
from authentication.models import StudentProfile

class ChatQuery(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.student.user.username if self.student else 'Guest'}"
