from django.apps import AppConfig


class LearnCachingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "learn_caching"

    def ready(self):
        import learn_caching.signals
