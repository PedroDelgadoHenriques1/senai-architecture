from django.urls import path
from .views import login_view, cadastro_produto_view, listar_produtos_view, cadastrar_fabricante_view, listar_fabricantes_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro_produto/', cadastro_produto_view, name='cadastro_produto'),
    path('listar_produtos/', listar_produtos_view, name='listar_produtos'),
    path('cadastrar_fabricante/', cadastrar_fabricante_view, name='cadastrar_fabricante'),
    path('listar_fabricantes/', listar_fabricantes_view, name='listar_fabricantes'),
]
