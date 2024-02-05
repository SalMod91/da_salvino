from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Configuration for the 'menu' app with BigAutoField as default ID field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
