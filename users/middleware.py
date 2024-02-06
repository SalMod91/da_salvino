from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.contrib.auth import logout
from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.shortcuts import redirect
from datetime import timedelta
import datetime


class AutoLogoutMiddleware:
    """
    Middleware to automatically log out users
    after a certain period of inactivity.
    """
    def __init__(self, get_response):
        """
        Initialize the middleware.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request, checking for user inactivity
        and performing auto-logout if necessary.
        """
        if request.user.is_authenticated:
            # Get the timestamp of the last activity from the session
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            last_activity = request.session.get('last_activity', None)
            if last_activity:
                # Convert last_activity string to datetime for comparison
                last_activity = datetime.datetime.strptime(
                    last_activity, '%Y-%m-%d %H:%M:%S')
                if (datetime.datetime.now() - last_activity).seconds > 180:
                    logout(request)
                    # Redirect to login page or wherever you want
                    # return redirect('staff_portal/')
                    return redirect('/staff_portal/')
            # Update last_activity time in session
            request.session['last_activity'] = current_time

        response = self.get_response(request)
        return response
