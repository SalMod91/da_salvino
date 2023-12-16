"""
URL to render the ingredients page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffPortalPage.as_view(), name='staff_portal')
]