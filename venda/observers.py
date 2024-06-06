from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Funcionario

class FuncionarioObserver:
    def __init__(self):
        post_save.connect(self.notificar, sender=Funcionario)

    def notificar(self, sender, instance, created, **kwargs):
        if created:
            print(f'Novo funcionário criado: {instance.nome}')

# Inicialização do observer
funcionario_observer = FuncionarioObserver()
