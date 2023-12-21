from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomStaffUser

class StaffUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomStaffUser
        fields = ('username',)
