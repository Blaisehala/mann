from django.apps import AppConfig


class MannConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mann'


    def ready(self):
        import mann.signals
