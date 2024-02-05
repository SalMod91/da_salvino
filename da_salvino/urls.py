"""
URL configuration for da_salvino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from staff_portal.views import (
    create_ingredient, manage_ingredients,
    create_menu_item, manage_menu_items
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('ingredients/', include('ingredients.urls')),
    path('staff_portal/', include('staff_portal.urls')),
    path('add_ingredient', create_ingredient, name='add_ingredient'),
    path('manage_ingredients', manage_ingredients, name='manage_ingredients'),
    path('add_menu_item', create_menu_item, name='add_menu_item'),
    path('manage_menu_items', manage_menu_items, name='manage_menu_items')
]
