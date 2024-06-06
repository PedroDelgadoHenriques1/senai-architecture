from django.apps import AppConfig

class VendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'venda'

    def ready(self):
        from . import observers  # Importa o módulo para inicializar o observer
