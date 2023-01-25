"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula


                      classe
------------------------------------------------
/                                              /
/ atributos | métodos | herança | polimorfismo /
------------------------------------------------

# Relembrando Atributos/Métodos Privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado __falar(self)

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados do usuário.

# Testando
conta1 = Conta('Geek', 150.0, 1500.0)
print(conta1.__dict__)
conta1.extrato()
print(conta1._Conta__titular)  # Name Mangling
conta1._Conta__titular = 'Angelina'
print(conta1.__dict__)

conta1.depositar(150)
print(conta1.__dict__)
conta1.sacar(200)
print(conta1.__dict__)

"""


class Conta:
    contador: int = 400

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.numero: int = Conta.contador
        self.__titular: str = titular
        self.__saldo: float = saldo
        self.__limite: float = limite
        self.__taxa: float = 1.05
        Conta.contador += 1

    def extrato(self) -> None:
        print(f'Saldo de R${self.__saldo} do titular {self.__titular} com limite de R${self.__limite}')

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
            print(f'Valor de R${valor} depositado com sucesso')
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor: float) -> None:
        if valor > 0:
            if valor - self.__saldo > self.__limite:
                print('O valor ultrapassa o limite')
            elif valor > self.__saldo:
                print('Saldo insuficiente')
            else:
                self.__saldo -= valor
                print(f'Valor de R${valor} sacado com sucesso')
        else:
            print('O valor precisa ser positivo')

    def transferir(self, valor: float, conta_destino) -> None:
        if valor > 0:
            if valor - self.__saldo > self.__limite:
                print('O valor ultrapassa o limite')
            elif valor > self.__saldo:
                print('Saldo insuficiente')
            else:
                self.__saldo -= valor * self.__taxa
                conta_destino.__saldo += valor
                print(f'Valor de R${valor} transferido com sucesso')
        else:
            print('O valor precisa ser positivo')


# Testando
conta1 = Conta('Angelina', 150.0, 1500.0)
conta1.extrato()

conta2 = Conta('Felicity', 300.0, 2000.0)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
