class Pessoa:
    """
    Classe Pessoa

    Atributos:
        codigo: int
        nome: str
        idade: int

    Métodos:
        exibe: None
    """

    def __init__(self, codigo: int, nome: str, idade: int):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def exibe(self, num: int = 0) -> None:
        """
        Exibe os dados da pessoa
        :param num: 1 - Exibe idade, 0 - Não exibe idade.
        :return: None
        """
        print(f'Código: {self.codigo}')
        print(f'Nome: {self.nome}')
        if num == 1:
            print(f'Idade: {self.idade}')
        print('-' * 20)
