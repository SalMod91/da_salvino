from django.contrib import admin
from .models import Ingredient, IngredientCategory, Pizza


class IngredientAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Ingredient model.

    Provides a configuration for what attributes in the Ingredient
    model are shown in the admin interface.
    """
    # Specify the fields to be displayed in the list view in the Django admin
    list_display = (
        'name',
        'category',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by'
    )

    # Fields that should be read-only in the admin form.
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    # Custom save method to automatically set created_by and updated_by fields
    def save_model(self, request, obj, form, change):
        # If the object is being created (does not have PK)
        if not obj.pk:
            # Set created_by to the current user
            obj.created_by = request.user
        # Set updated_by to the current user
        obj.updated_by = request.user
        # Call the superclass method to handle the actual saving
        super().save_model(request, obj, form, change)


class PizzaAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Pizza model.

    Provides a configuration for what attributes in the Pizza
    model are shown in the admin interface.
    """
    # Specify the fields to be displayed in the list view in the Django admin
    list_display = (
        'name',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by'
    )

    # Fields that should be read-only in the admin form.
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    # Custom save method to automatically set created_by and updated_by fields
    def save_model(self, request, obj, form, change):
        # If the object is being created (does not have PK)
        if not obj.pk:
            # Set created_by to the current user
            obj.created_by = request.user
        # Always set updated_by to the current user
        obj.updated_by = request.user
        # Call the superclass method to handle the actual saving
        super().save_model(request, obj, form, change)


# Register the models with the admin site to make them accessible
# in the Django admin interface
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientCategory)
admin.site.register(Pizza, PizzaAdmin)
