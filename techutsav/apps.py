from django.apps import AppConfig


class TechutsavConfig(AppConfig):
    name = 'techutsav'
    def ready(self):
        import techutsav.signals
