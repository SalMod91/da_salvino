from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_portal, name='staff_portal'),
    path('add_ingredient', views.create_ingredient, name='add_ingredient'),
]