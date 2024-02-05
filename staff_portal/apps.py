from django.apps import AppConfig


class StaffLoginConfig(AppConfig):
    """
    Configuration for the 'staff_portal' app with BigAutoField
    as default ID field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff_portal'
