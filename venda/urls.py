from django.urls import path
from .views import login_view, cadastro_produto_view, listar_produtos_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro_produto/', cadastro_produto_view, name='cadastro_produto'),
    path('produtos/', listar_produtos_view, name='listar_produtos'),
]
