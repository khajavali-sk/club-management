from django import forms
from .models import CustomSubmission

class CustomSubmissionForm(forms.ModelForm):
    class Meta:
        model = CustomSubmission
        fields = ['event', 'field_name', 'field_value']
