from django.shortcuts import render
from django.views.generic import TemplateView
from staff_portal.models import Pizza, Ingredient

class MenuPage(TemplateView):
    """
    A class-based view for rendering the ingredients page using Django's class TemplateView.
    Enables the Template to display dynamic data.
    """

    # Specifies the template to be used when rendering this view
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        """
        Overriding the get_context_data for rendering the template
        with dynamic data.
        It retrieves the context from its parent class (TemplateView) and
        customizes its content with the Pizza model.
        """

        # Calls the get_context_data method from its parent class, "TemplateView"
        context = super().get_context_data(**kwargs)
        
        # Retrieve all pizza items
        pizzas = Pizza.objects.order_by('name')
        # Add pizzas to the context
        context['pizzas'] = pizzas

        # Retrieve "Pizza Dough", "Tomato Sauce" and "Mozzarella" ingredients if they exist
        pizza_dough = Ingredient.objects.filter(name="Pizza Dough").first()
        tomato_sauce = Ingredient.objects.filter(name="Tomato Sauce").first()
        mozzarella = Ingredient.objects.filter(name="Mozzarella").first()

        # Add additional context for Pizza Dough, Tomato Sauce and Mozzarella
        context['pizza_dough_id'] = pizza_dough.id if pizza_dough else None
        context['tomato_sauce_id'] = tomato_sauce.id if tomato_sauce else None
        context['mozzarella_id'] = mozzarella.id if mozzarella else None

        # Returns the context dictionary wich now includes the Pizza model
        return context