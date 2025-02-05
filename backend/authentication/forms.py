from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentProfile, ClubAdminProfile
from clubs.models import Club

class StudentSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    branch = forms.CharField(max_length=50, required=True)
    roll_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'  # Students only
        if commit:
            user.save()
            StudentProfile.objects.create(
                user=user,
                branch=self.cleaned_data['branch'],
                roll_number=self.cleaned_data['roll_number']
            )
        return user

class ClubAdminCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    club = forms.ModelChoiceField(queryset=Club.objects.filter(clubadminprofile__isnull=True), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            password=self.cleaned_data['password'],
            role='club_admin'
        )
        ClubAdminProfile.objects.create(user=user, club=self.cleaned_data['club'])
        return user


# class UserLoginForm(forms.ModelForm):
