from django.shortcuts import render
from django.views.generic import TemplateView
from staff_portal.models import Ingredient, IngredientCategory

class IngredientsPage(TemplateView):
    """
    A class-based view for rendering the ingredients page using Django's class TemplateView.
    Enables the Template to display dynamic data.
    """

    # Specifies the template to be used when rendering this view
    template_name = "ingredients.html"

    def get_context_data(self, **kwargs):
        """
        Overriding the get_context_data for rendering the template
        with dynamic data.
        It retrieves the context from its parent class (TemplateView) and
        customizes its content with the ingredient categories and ingredients.
        """
        # Calls the get_context_data method from its parent class, "TemplateView"
        context = super().get_context_data(**kwargs)
        
        # Creating an empty dictionary to hold categories and their ingredients
        categorized_ingredients = {}

        # Retrieve all categories
        categories = IngredientCategory.objects.all()

        # Iterate over each category and retrieve its ingredients
        # For each category, filter the ingredients from the database that belong to that category
        # and store them in the categorized_ingredients dictionary with the category name as the key
        for category in categories:
            ingredients = Ingredient.objects.filter(
                category=category
            # Orders ingredients alphabetically by name
            ).order_by('name')
            categorized_ingredients[category.name] = ingredients

        # Add categorized ingredients dictionary to the context dictionary
        context['categorized_ingredients'] = categorized_ingredients

        # Returns the context dictionary wich now includes the 'categorized_ingredients'
        return context