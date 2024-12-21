from django.apps import AppConfig


class NotionAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notion_app'

    def ready(self):
        import notion_app.signals_hendlers
