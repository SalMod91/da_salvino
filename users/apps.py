from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration for the 'user' app with BigAutoField
    as default ID field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
