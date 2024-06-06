class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Configuracao(metaclass=Singleton):
    def __init__(self):
        self.parametro = 'valor padrão'

# Uso:
# config = Configuracao()
# config.parametro = 'novo valor'
# outra_config = Configuracao()
# print(outra_config.parametro)  # 'novo valor'
