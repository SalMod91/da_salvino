"""
URL to render the ingredients page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IngredientsPage.as_view(), name='ingredients')
]
