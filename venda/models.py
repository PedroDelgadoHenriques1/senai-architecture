from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
