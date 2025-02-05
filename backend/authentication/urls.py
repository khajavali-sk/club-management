from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('signup/', student_signup, name='signup'),
    path('', student_signup, name='signup'),
    # path('validate-signup/', validate_signup, name='validate-signup'),
    # path('validate-field/', validate_field, name='validate-field'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-club-admin/', create_club_admin, name='create_club_admin'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('club-admin-dashboard/', club_admin_dashboard, name='club_admin_dashboard'),
    path('super-admin-dashboard/', super_admin_dashboard, name='super_admin_dashboard'),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('signup_success/', signup_success, name='signup_success'),
    path('student_signup/', student_signup, name='signup_success'),
]



