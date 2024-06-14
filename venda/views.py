import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Produto, Fabricante, Grupo, Subgrupo, Venda
from .forms import ProdutoForm, FabricanteForm, GrupoForm, SubgrupoForm, LancamentoVendasForm
import plotly.express as px
import plotly.graph_objs as go
from django.shortcuts import get_object_or_404

def login_view(request):
    if request.method == 'POST':
        login_ = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, login=login_, password=password)
        if user is not None:
            login(request, user)
            return redirect('venda')  # Substitua 'home' pelo nome da sua URL de destino
        else:
            messages.error(request, 'Login ou senha incorretos')
    return render(request, 'venda/login.html')

def cadastro_produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'venda/cadastro_produto.html', {'form': form})

def listar_produtos_view(request):
    produtos = Produto.objects.all()
    return render(request, 'venda/listar_produtos.html', {'produtos': produtos})

def cadastrar_fabricante_view(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fabricantes')
    else:
        form = FabricanteForm()
    return render(request, 'venda/cadastrar_fabricante.html', {'form': form})

def listar_fabricantes_view(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'venda/listar_fabricantes.html', {'fabricantes': fabricantes})

def cadastrar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'venda/cadastrar_grupo.html', {'form': form})

def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'venda/listar_grupos.html', {'grupos': grupos})

def cadastrar_subgrupo(request):
    if request.method == 'POST':
        form = SubgrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_subgrupos')
    else:
        form = SubgrupoForm()
    return render(request, 'venda/cadastrar_subgrupo.html', {'form': form})

def listar_subgrupos(request):
    subgrupos = Subgrupo.objects.all()
    return render(request, 'venda/listar_subgrupos.html', {'subgrupos': subgrupos})

def lancamento_vendas_view(request):
    if request.method == 'POST':
        form = LancamentoVendasForm(request.POST)
        if form.is_valid():
            produto_id = form.cleaned_data['produto'].id  # Obtenha o ID do produto
            quantidade_vendida = form.cleaned_data['quantidade_vendida']
            
            try:
                produto = Produto.objects.get(pk=produto_id)
            except Produto.DoesNotExist:
                # Lógica de tratamento se o produto não existir
                return render(request, 'venda/lancamento_vendas.html', {'form': form, 'erro': 'Produto não encontrado.'})
            
            # Verifica se há estoque suficiente
            if quantidade_vendida <= produto.quantidade:
                # Calcula o valor total da venda
                valor_venda_total = produto.preco_venda * quantidade_vendida
                
                # Atualiza a quantidade vendida e subtrai do estoque
                produto.quantidade -= quantidade_vendida
                produto.save()
                
                # Implemente aqui a lógica de registro da venda, se necessário
                
                return redirect('venda:lancamento_vendas')
            else:
                # Retorne uma mensagem de erro caso não haja estoque suficiente
                return render(request, 'venda/lancamento_vendas.html', {'form': form, 'erro': 'Estoque insuficiente.'})
    else:
        form = LancamentoVendasForm()
    
    return render(request, 'venda/lancamento_vendas.html', {'form': form})

def visualizar_vendas_view(request):
    # Lógica para obter os dados para o gráfico de barras
    # Exemplo de dados fictícios
    dados = {
        'data_hora': ['2024-01-01', '2024-02-01', '2024-03-01'],
        'quantidade_comprada_total': [500, 600, 700],
        'quantidade_vendida_total': [400, 550, 600]
    }
    
    vendas = pd.DataFrame(dados)
    
    fig_barras = px.bar(vendas, x='data_hora', y=['quantidade_comprada_total', 'quantidade_vendida_total'], 
                        title='Quantidade Comprada e Vendida Total Mensal')
    
    graph_barras = fig_barras.to_html(full_html=False, default_height=500, default_width=700)
    
    return render(request, 'venda/visualizar_vendas.html', {'graph_barras': graph_barras})

def sucesso_view(request):
    return render(request, 'venda/sucesso.html')