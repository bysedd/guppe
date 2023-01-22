class Pessoa:
    def __init__(self, nome: str, endereco: str, telefone: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')


pessoa = Pessoa('Felippe', 'Rua 1', '123456789')
pessoa.imprimir()
