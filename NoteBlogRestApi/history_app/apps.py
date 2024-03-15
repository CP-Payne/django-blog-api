from django.apps import AppConfig


class HistoryAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "history_app"

    def ready(self):
        import history_app.signals  # Import signals to connect them  # noqa: F401

