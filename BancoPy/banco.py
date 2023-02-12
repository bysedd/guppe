from typing import List
from time import sleep
import pickle

from models.cliente import Cliente
from models.conta import Conta
from utils import helper


class Banco:
    contas: List[Conta] = []
    tracos: str = '=' * 50
    FILE: str = 'data/contas.pickle'

    def __init__(self) -> None:
        Banco.contas = self._carregar_contas()

    def menu(self) -> None:
        print(self.tracos)
        print('Python ATM'.center(50))
        print(self.tracos)

        print('1 - Criar conta\n'
              '2 - Efetuar saque\n'
              '3 - Efetuar depósito\n'
              '4 - Efetuar transferência\n'
              '5 - Listar contas\n'
              '6 - Sair')

        opcao: int = int(input('Escolha uma opção: '))
        print(self.tracos)
        
        match opcao:
            case 1:
                self.criar_conta()
            case 2:
                self.efetuar_saque()
            case 3:
                self.efetuar_deposito()
            case 4:
                self.efetuar_transferencia()
            case 5:
                self.listar_contas()
            case 6:
                self._salvar_contas()
                raise SystemExit('Saindo do sistema...')
            case _:
                print('Opção inválida!')
                sleep(1)

    def criar_conta(self) -> None:
        print('Criar conta'.center(50))
        print(self.tracos)

        # Solicita os dados do cliente
        _codigo = self._get_contador_contas()
        _nome: str = input('Nome: ').strip().title()
        _cpf: str = helper.formatar_cpf(input('CPF (raw): '))
        _email: str = input('E-mail: ')
        _data_nascimento: str = input('Data de nascimento (dd/mm/yyyy): ')

        # Cria o objeto e adiciona na lista de contas
        cliente: Cliente = Cliente(
            codigo=_codigo,
            nome=_nome,
            cpf=_cpf,
            email=_email,
            data_nascimento=_data_nascimento
        )
        conta: Conta = Conta(codigo=_codigo, cliente=cliente)
        self.contas.append(conta)

        # Salva as contas no arquivo
        with open(self.FILE, 'wb') as file:
            pickle.dump(self.contas, file)

        print(self.tracos)
        print('Conta criada com sucesso!')
        print(self.tracos)
        sleep(1)

    def efetuar_saque(self) -> None:
        if len(self.contas) > 0:
            numero: int = int(input('Número da conta: '))
            conta: Conta = self._buscar_conta(numero)

            print(self.tracos)
            if conta:
                # Exibir conta sem mostrar o número
                print(conta.__str__())
                print(self.tracos)

                valor: float = float(input('Valor do saque: '))

                if conta.sacar(valor):
                    print('Saque efetuado com sucesso!')
            else:
                print(f'Conta com número {numero} não encontrada!')
        else:
            print('Ainda não existem contas cadastradas!')

        print(self.tracos)
        sleep(1)

    def efetuar_deposito(self) -> None:
        if len(self.contas) > 0:
            numero: int = int(input('Número da conta: '))
            conta: Conta = self._buscar_conta(numero)

            print(self.tracos)
            if conta:
                valor: float = float(input('Valor do depósito: '))
                conta.depositar(valor)

                print('Depósito efetuado com sucesso!')
            else:
                print(f'Conta com número {numero} não encontrada!')
        else:
            print('Ainda não existem contas cadastradas!')

        print(self.tracos)
        sleep(1)

    def efetuar_transferencia(self) -> None:
        if len(self.contas) >= 2:
            numero: int = int(input('Número da conta: '))
            conta: Conta = self._buscar_conta(numero)

            print(self.tracos)
            if conta:
                numero: int = int(input('Número da conta destino: '))
                conta_destino: Conta = self._buscar_conta(numero)

                if conta_destino:
                    valor: float = float(input('Valor da transferência: '))
                    conta.transferir(valor, conta_destino)

                    if conta.transferir(valor, conta_destino):
                        print('Transferência efetuada com sucesso!')
                else:
                    print(f'Conta com número {numero} não encontrada!')
            else:
                print(f'Conta com número {numero} não encontrada!')
        elif len(self.contas) == 1:
            print('É necessário ter mais de uma conta cadastrada!')
        else:
            print('Ainda não existem contas cadastradas!')

        print(self.tracos)
        sleep(1)

    def listar_contas(self) -> None:
        if len(self.contas) > 0:
            print('Listar contas'.center(50))
            print(self.tracos)

            for conta in self.contas:
                print(conta)
                print(self.tracos)
                sleep(1)
        else:
            print('Ainda não existem contas cadastradas!')
            print(self.tracos)
            sleep(1)

    def _buscar_conta(self, numero: int) -> Conta:
        for conta in self.contas:
            if conta.codigo == numero:
                return conta

    def _carregar_contas(self) -> List[Conta]:
        try:
            with open(self.FILE, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def _salvar_contas(self) -> None:
        with open(self.FILE, 'wb') as file:
            pickle.dump(self.contas, file)

    def _get_contador_contas(self) -> int:
        return Conta.contador + len(self.contas)


if __name__ == '__main__':
    banco: Banco = Banco()

    while True:
        try:
            banco.menu()
        except (ValueError, TypeError) as e:
            print(f'\033[31m{e}\033[m')
            sleep(1)
