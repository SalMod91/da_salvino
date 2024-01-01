from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import StaffUserCreationForm
from .forms import CustomPasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.models import CustomStaffUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def staff_portal(request):

    login_form = AuthenticationForm()
    signup_form = StaffUserCreationForm()
    password_change_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

    if request.method == 'POST':
        if 'submit_login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_approved:
                        login(request, user)
                        messages.success(request, f"You have successfully logged in as {username}.")
                        return redirect('staff_portal') 
                    else:
                        messages.error(request, "Approval pending. Please wait for a manager to approve your account.")

        elif 'submit_signup' in request.POST:
            signup_form = StaffUserCreationForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Registration successful! Your account is pending approval.")
                return redirect('staff_portal')
            else:
                messages.error(request, "Invalid registration details.")
        
        elif 'action' in request.POST and request.POST['action'] == 'logout':
            logout(request)
            messages.success(request, "You have been successfully logged out.")
            return redirect('staff_portal')
        
        elif 'change_password' in request.POST:
            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, f"Password for {user.username} changed successfully.")
                return redirect('staff_portal')
            else:
                messages.error(request, "Error changing password.")

    return render(request, 'staff_portal.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'password_change_form': password_change_form,
})
