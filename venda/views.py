from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ProdutoForm
from .models import Produto

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