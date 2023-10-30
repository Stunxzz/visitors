from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


class VisitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visit.visitor'

    def ready(self):
        import visit.visitor.signals




