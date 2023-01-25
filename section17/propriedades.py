"""
POO - Propriedades - Properties

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos
são conhecidos por getters e setters, onde os getters retornam o valor do atributo
e os setters alteram o valor do mesmo.


class Conta:
    contador = 0
    
    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self) -> str:
        return f'Saldo de ${self.__saldo} do(a) cliente {self.__titular}'

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor            
    
    def sacar(self, valor: float) -> None:
        self.__saldo -= valor
    
    def transferir(self, valor: float, destino) -> None:
        self.__saldo -= valor
        destino.__saldo += valor
    
    def get_numero(self) -> int:
        return self.__numero
    
    def get_titular(self) -> str:
        return self.__titular
    
    def set_titular(self, titular: str) -> None:
        self.__titular = titular
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def get_limite(self) -> float:
        return self.__limite
    
    def set_limite(self, limite: float):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é ${soma}')

print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

"""


class Conta:
    contador = 0

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def titular(self) -> str:
        return self.__titular

    @titular.setter
    def titular(self, titular: str) -> None:
        print(f'O titular foi alterado de {self.titular} para {titular}')
        self.__titular = titular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, limite: float) -> None:
        print(f'O limite foi alterado de ${self.limite} para ${limite} do(a) cliente {self.titular}')
        self.__limite = limite

    @property
    def extrato(self) -> str:
        return f'Saldo de ${self.saldo} do(a) cliente {self.titular}'

    @property
    def valor_total(self) -> float:
        return self.saldo + self.limite

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float) -> None:
        self.__saldo -= valor

    def transferir(self, valor: float, destino) -> None:
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato)
print(conta2.extrato)

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é ${soma}')

conta1.limite = 76543

print(conta1.valor_total)
print(conta2.valor_total)
