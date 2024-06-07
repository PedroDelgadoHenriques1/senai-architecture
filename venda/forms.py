from django import forms
from .models import Produto, Fabricante


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_custo', 'preco_vendas', 'peso', 'quantidade_comprado', 'quantidade_vendida', 'fabricante', 'grupo', 'subgrupo']



class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome_fantasia', 'razao_social', 'cnpj', 'endereco', 'telefone', 'email', 'vendedor']
