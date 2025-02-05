from django import forms
from .models import Event,Registration, Team

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'venue', 'custom_fields']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }




class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['event', 'is_team', 'reminder_time']
        widgets = {
            'reminder_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'event', 'members']
