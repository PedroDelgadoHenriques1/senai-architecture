from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Produto, Fabricante, Grupo, Subgrupo, Venda
from .forms import ProdutoForm, FabricanteForm, GrupoForm, SubgrupoForm, LancamentoVendasForm
import plotly.express as px
import plotly.graph_objs as go

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
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']
            if produto.quantidade >= quantidade:
                valor_venda = produto.preco_venda * quantidade
                venda = Venda(produto=produto, quantidade=quantidade, valor_venda=valor_venda)
                venda.save()
                produto.quantidade -= quantidade
                produto.save()
                return render(request, 'venda/sucesso.html', {'produto': produto, 'quantidade': quantidade})
            else:
                messages.error(request, 'Quantidade insuficiente em estoque')
    else:
        form = LancamentoVendasForm()
    
    return render(request, 'venda/lancamento_vendas.html', {'form': form})

def visualizar_vendas_view(request):
    vendas = Venda.objects.all()
    produtos = Produto.objects.all()

    fig_linha = px.line(vendas, x='data_hora', y=['valor_venda'], title='Valor Venda Total Mensal')
    fig_barras = px.bar(produtos, x='id', y=['quantidade'], title='Quantidade Vendida Total Mensal')
    fig_dispersao = px.scatter(vendas, x='data_hora', y='valor_venda', title='Percentual de Lucro Mensal')

    top_produtos = produtos.order_by('-quantidade')[:3]
    fig_pizza = px.pie(top_produtos, names='nome', values='quantidade', title='Top 3 Produtos Mais Vendidos')

    grupos = produtos.values('grupo').annotate(total_vendido=models.Sum('quantidade')).filter(total_vendido__gte=1000)
    fig_barras_linha = go.Figure()
    fig_barras_linha.add_trace(go.Bar(x=[grupo['grupo'] for grupo in grupos], y=[grupo['total_vendido'] for grupo in grupos], name='Quantidade Vendida'))

    produtos_estoque_baixo = produtos.filter(quantidade__lt=10).order_by('-quantidade')

    return render(request, 'venda/visualizar_vendas.html', {
        'fig_linha': fig_linha.to_html(),
        'fig_barras': fig_barras.to_html(),
        'fig_dispersao': fig_dispersao.to_html(),
        'fig_pizza': fig_pizza.to_html(),
        'fig_barras_linha': fig_barras_linha.to_html(),
        'produtos_estoque_baixo': produtos_estoque_baixo,
    })

def sucesso_view(request):
    return render(request, 'venda/sucesso.html')