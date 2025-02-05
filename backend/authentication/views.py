from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, aauthenticate
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from .forms import StudentSignupForm
from .models import User, StudentProfile, ClubAdminProfile
from clubs.models import Club
from events.models import Event, Registration


# ✅ Student Signup View (Email Verification Enabled)
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Email verification required
            user.save()

            # Send Verification Email
            current_site = get_current_site(request)
            subject = "Verify Your Email"
            message = render_to_string('email_verification.html', {
    'user': user,
    'domain': current_site.domain,
    'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),  # Fix variable name
    'token': default_token_generator.make_token(user),
})


            try:
                send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=message, fail_silently=False)
            except Exception as e:
                return HttpResponse(f"Error sending email: {e}")

            return redirect('signup_success')  # Redirect after successful signup

    else:
        form = StudentSignupForm()

    return render(request, 'signup.html', {'form': form})

# ✅ Signup Success Page
def signup_success(request):
    return render(request, 'signup_success.html')










# ✅ Email Verification View
def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse("Invalid verification link.")

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('student_dashboard')
    
    return HttpResponse("Verification link is invalid or expired.")


# # ✅ User Login View (With Role-Based Redirection)
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect_based_on_role(user)
        else:
            print("Authentication failed. Check credentials.",username+password)
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# # ✅ Role-Based Redirection
def redirect_based_on_role(user):
    if user.role == 'student':
        return redirect('student_dashboard')
    elif user.role == 'club_admin':
        return redirect('club_admin_dashboard')
    elif user.role == 'super_admin':
        return redirect('super_admin_dashboard')
    return redirect('login')  # Default to login if role is missing


# # ✅ User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')


# # ✅ Student Dashboard
def student_dashboard(request):
    student = getattr(request.user, 'studentprofile', None)
    registered_events = Registration.objects.filter(student=student) if student else []
    return render(request, 'student_dashboard.html', {'student': student, 'registered_events': registered_events})


# # ✅ Club Admin Dashboard
def club_admin_dashboard(request):
    pass
#     if not hasattr(request.user, 'clubadminprofile'):
#         return HttpResponseForbidden("You are not authorized to access this page.")

#     club_admin = request.user.clubadminprofile
#     club_events = Event.objects.filter(created_by=club_admin.club)

#     return render(request, 'club_admin_dashboard.html', {'club_admin': club_admin, 'club_events': club_events})


# # ✅ Super Admin Dashboard
def super_admin_dashboard(request):
    pass
#     total_users = User.objects.count()
#     total_clubs = Club.objects.count()
#     club_admins = User.objects.filter(role="club_admin")
#     return render(request, 'super_admin_dashboard.html', {'total_users': total_users, 'total_clubs': total_clubs, 'club_admins': club_admins})


# # ✅ Only Super Admins Can Create Club Admins
def is_super_admin(user):
    pass
#     return user.is_authenticated and user.role == 'super_admin'

# @user_passes_test(is_super_admin)
def create_club_admin(request):
    pass
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         club_id = request.POST['club']

#         if User.objects.filter(email=email).exists():
#             return render(request, 'create_club_admin.html', {'clubs': Club.objects.all(), 'error': 'Email already registered'})

#         user = User.objects.create_user(username=username, email=email, password=password, role='club_admin')
#         ClubAdminProfile.objects.create(user=user, club_id=club_id)
#         return redirect('super_admin_dashboard')

#     return render(request, 'create_club_admin.html', {'clubs': Club.objects.all()})



