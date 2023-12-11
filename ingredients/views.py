from django.shortcuts import render
from django.views.generic import TemplateView

class IngredientsPage(TemplateView):
    """
    View for ingredients page
    """
    template_name = "ingredients.html"
