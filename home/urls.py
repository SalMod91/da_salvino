"""
URL to render the home page
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home')
]
