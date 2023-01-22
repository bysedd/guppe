class Pessoa:
    nome: str = 'Felippe'
    endereco: str = 'Rua 1'
    telefone: str = '123456789'

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')


pessoa = Pessoa()
pessoa.imprimir()
