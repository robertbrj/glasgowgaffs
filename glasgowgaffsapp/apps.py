from django.apps import AppConfig


class GlasgowgaffsappConfig(AppConfig):
    """
        App configuration class for the glasgowgaffsapp Django application
        sets the default auto field type and app name
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "glasgowgaffsapp"
