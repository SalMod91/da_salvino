from django.shortcuts import render
from django.views.generic import TemplateView

class MenuPage(TemplateView):
    """
    View for menu page
    """
    template_name = "menu.html"
