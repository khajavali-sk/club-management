from django.db import models
from clubs.models import Club
from authentication.models import StudentProfile

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    created_by = models.ForeignKey(Club, on_delete=models.CASCADE)  
    custom_fields = models.JSONField(default=dict)  # Example: {"ppt_required": true, "github_link": true}

    def __str__(self):
        return self.name


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    is_team = models.BooleanField(default=False)
    reminder_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.username} registered for {self.event.name}"


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    leader = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="team_leader")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    members = models.ManyToManyField(StudentProfile, related_name="team_members")

    def __str__(self):
        return f"{self.team_name} - {self.event.name}"
