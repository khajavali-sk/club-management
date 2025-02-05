
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)

# Custom User Model (Without AbstractUser)
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('club_admin', 'Club Admin'),
        ('super_admin', 'Super Admin'),
    )
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)  # Required for login
    is_staff = models.BooleanField(default=False)  # Needed for Django admin

    objects = UserManager()  # Set the custom manager

    USERNAME_FIELD = 'username'  # Define primary login field
    REQUIRED_FIELDS = ['email']  # Other required fields

    def __str__(self):
        return f"{self.username} ({self.role})"

















# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

# # Custom User Model
# class User(AbstractUser):
#     USERNAME_FIELD = 'username'  # Ensures authentication uses username
#     REQUIRED_FIELDS = ['email']

#     ROLE_CHOICES = (
#         ('student', 'Student'),
#         ('club_admin', 'Club Admin'),
#         ('super_admin', 'Super Admin'),
#     )
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, unique=True, null=True, blank=True)


#     # Define related_name for the groups and user_permissions fields to avoid clashes
#     groups = models.ManyToManyField(
#         Group,
#         related_name='authentication_user_set',  # Custom reverse accessor name
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='authentication_user_permissions_set',  # Custom reverse accessor name
#         blank=True
#     )

#     def __str__(self):
#         return f"{self.username} ({self.role})"

# Student Profile Model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"

# Club Admin Profile Model
class ClubAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.user.role != 'club_admin':
            raise ValueError("Only users with role 'club_admin' can be assigned to a club.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Admin of {self.club.name}"


# # class Registration(models.Model):
# #     student = models.ForeignKey(User, on_delete=models.CASCADE)  # Delete registrations if user is deleted
# #     event = models.ForeignKey(Event, on_delete=models.CASCADE)
