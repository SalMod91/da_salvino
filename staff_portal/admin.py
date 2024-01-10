from django.contrib import admin
from .models import Ingredient, IngredientCategory, Pizza

admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(Pizza)
