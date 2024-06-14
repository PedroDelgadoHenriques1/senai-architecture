from django.urls import path
from .views import login_view, cadastro_produto_view, listar_produtos_view, cadastrar_fabricante_view, listar_fabricantes_view, cadastrar_grupo, listar_grupos, cadastrar_subgrupo, listar_subgrupos, lancamento_vendas_view, visualizar_vendas_view, sucesso_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro_produto/', cadastro_produto_view, name='cadastro_produto'),
    path('listar_produtos/', listar_produtos_view, name='listar_produtos'),
    path('cadastrar_fabricante/', cadastrar_fabricante_view, name='cadastrar_fabricante'),
    path('listar_fabricantes/', listar_fabricantes_view, name='listar_fabricantes'),
    path('cadastrar_grupo/', cadastrar_grupo, name='cadastrar_grupo'),
    path('listar_grupos/', listar_grupos, name='listar_grupos'),
    path('cadastrar_subgrupo/', cadastrar_subgrupo, name='cadastrar_subgrupo'),
    path('listar_subgrupos/', listar_subgrupos, name='listar_subgrupos'),
    path('lancamento_vendas/', lancamento_vendas_view, name='lancamento_vendas'),
    path('visualizar_vendas/', visualizar_vendas_view, name='visualizar_vendas'),
    path('sucesso/', sucesso_view, name='sucesso'),
]
