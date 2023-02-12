from BancoPy.models.cliente import Cliente
from BancoPy.utils import helper
from random import randint


class Conta:
    """
    Classe que representa uma conta bancária.
    """
    contador: int = 1001

    def __init__(self, codigo: int = None, *, cliente: Cliente, saldo: float = 0, limite: float = 0):
        self.__codigo: int = Conta.contador if not codigo else codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = randint(1300, 3600) if not saldo else saldo
        self.__limite: float = randint(5000, 10000) if not limite else limite
        self.__historico: list = []
        Conta.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def limite(self) -> float:
        return self.__limite

    @property
    def historico(self) -> list:
        return self.__historico

    def depositar(self, valor: float) -> None:
        self.__saldo += valor
        self.historico.append(f'Depósito de {helper.formatar_moeda(valor)}')

    def sacar(self, valor: float) -> bool:
        if self._pode_sacar(valor):
            self.__saldo -= valor
            self.__historico.append(f'Saque de {helper.formatar_moeda(valor)}')
            return True
        else:
            print('O valor solicitado excede o limite da conta!')
            return False

    def transferir(self, valor: float, destino: 'Conta') -> bool:
        if self._pode_sacar(valor):
            self.sacar(valor)
            destino.depositar(valor)
            self.historico.append(f'Transferência de {helper.formatar_moeda(valor)} para a conta {destino.codigo}')
            return True
        else:
            print(f'O valor solicitado excede o limite da conta {self.codigo}')

    def _pode_sacar(self, valor: float) -> bool:
        if valor > self.limite or valor <= 0 or self.saldo <= 0 or self.saldo < valor:
            return False
        return True

    def __str__(self) -> str:
        return f'Número da conta: {self.codigo}\n' \
               f'Cliente: {self.cliente.nome}\n' \
               f'Saldo: {helper.formatar_moeda(self.saldo)}\n' \
               f'Limite: {helper.formatar_moeda(self.limite)}'

    def __repr__(self) -> None:
        # Mostra o histórico de transações da conta
        print([transacao for transacao in self.historico])


if __name__ == '__main__':
    conta: Conta = Conta(cliente=Cliente(
        nome='Geek University',
        cpf='123.456.789-00',
        email='geekuni@gmail.com',
        data_nascimento='01/01/2000')
    )
    print(conta, '\n')

    conta.__repr__()
