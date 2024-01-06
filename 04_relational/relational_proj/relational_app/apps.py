from django.apps import AppConfig


class RelationalAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "relational_app"
