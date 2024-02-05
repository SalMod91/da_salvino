from django.contrib import admin
from .models import Ingredient, IngredientCategory, Pizza

# Register the models with the admin site to make them accessible
# in the Django admin interface
admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(Pizza)
