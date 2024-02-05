"""
URL to render the menu page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuPage.as_view(), name='menu')
]
