from django.apps import AppConfig


class IngredientsConfig(AppConfig):
    """
    Configuration for the 'ingredients' app with BigAutoField as default ID field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ingredients'
