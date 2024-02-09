from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from allauth.account.models import EmailAddress
from django.contrib import admin
from .models import CustomStaffUser

# Register the model with the admin site to make it accessible
# in the Django admin interface
admin.site.register(CustomStaffUser)

# Unregister the auth and sites models from the Admin interface
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)