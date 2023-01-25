from pessoa import Pessoa


class TestaPessoa:
    """
    Classe TestaPessoa

    Atributos:
        pessoa: Pessoa

    Métodos:
        __init__: None
    """

    def __init__(self, codigo: int, nome: str, idade: int):
        """
        Construtor da classe TestaPessoa
        :param codigo: Código da pessoa
        :param nome: Nome da pessoa
        :param idade: Idade da pessoa
        """
        self.pessoa = Pessoa(codigo, nome, idade)
