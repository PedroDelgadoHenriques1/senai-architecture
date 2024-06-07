from django.contrib import admin
from .models import Funcionario
from .models import Produto, Fabricante, Grupo, Subgrupo


admin.site.register(Funcionario)
admin.site.register(Produto)
admin.site.register(Fabricante)
admin.site.register(Grupo)
admin.site.register(Subgrupo)
