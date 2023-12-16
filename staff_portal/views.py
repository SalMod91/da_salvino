from django.shortcuts import render
from django.views.generic import TemplateView

class StaffPortalPage(TemplateView):
    """
    View for ingredients page
    """
    template_name = "staff_portal.html"
