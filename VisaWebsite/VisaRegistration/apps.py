from django.apps import AppConfig


class VisaregistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VisaRegistration'

    def ready(self):
        import VisaRegistration.signals