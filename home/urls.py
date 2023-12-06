"""
URL to render the home page
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home')
]