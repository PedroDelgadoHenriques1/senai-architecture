from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class FuncionarioManager(BaseUserManager):
    def create_user(self, login, nome, email, password=None):
        if not login:
            raise ValueError('Funcionários devem ter um login')
        if not email:
            raise ValueError('Funcionários devem ter um email')
        funcionario = self.model(
            login=login,
            nome=nome,
            email=self.normalize_email(email),
        )
        funcionario.set_password(password)
        funcionario.save(using=self._db)
        return funcionario

    def create_superuser(self, login, nome, email, password=None):
        funcionario = self.create_user(
            login,
            nome,
            email,
            password=password,
        )
        funcionario.is_admin = True
        funcionario.save(using=self._db)
        return funcionario

class Funcionario(AbstractBaseUser):
    login = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = FuncionarioManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

class Fabricante(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    vendedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_fantasia

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default='Descrição padrão')  # Adicionando um valor padrão

    def __str__(self):
        return self.nome

class Subgrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(default='Descrição padrão')  # Adicionando um valor padrão
    

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_vendas = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=3)
    quantidade_comprado = models.PositiveIntegerField()
    quantidade_vendida = models.PositiveIntegerField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
