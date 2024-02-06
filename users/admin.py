from django.contrib import admin
from .models import CustomStaffUser

# Register the model with the admin site to make it accessible
# in the Django admin interface
admin.site.register(CustomStaffUser)
