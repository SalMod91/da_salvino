from django.contrib import admin
from .models import Ingredient, IngredientCategory

admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
