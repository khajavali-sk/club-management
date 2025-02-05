from django.contrib import admin
from .models import StudentProfile, User, ClubAdminProfile

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)

admin.site.register(StudentProfile)

admin.site.register(ClubAdminProfile)


