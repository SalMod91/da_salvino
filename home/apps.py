from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the 'home' app with BigAutoField as default ID field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
