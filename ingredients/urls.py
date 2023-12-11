"""
URL to render the menu page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IngredientsPage.as_view(), name='ingredients')
]