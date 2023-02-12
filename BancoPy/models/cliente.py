from datetime import date
from BancoPy.utils import helper


class Cliente:
    contador: int = 101

    def __init__(self, codigo: int = None, *, nome: str, cpf: str, email: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador if not codigo else codigo
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__email: str = email
        self.__data_nascimento: date = helper.str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def email(self) -> str:
        return self.__email

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def data_cadastro(self) -> date:
        return self.__data_cadastro

    def __str__(self) -> str:
        return f'Código: {self.codigo}\n' \
               f'Nome: {self.nome}\n' \
               f'Data de Nascimento: {helper.date_para_str(self.data_nascimento)}\n' \
               f'Data de Cadastro: {helper.date_para_str(self.data_cadastro)}'


if __name__ == '__main__':
    felicity: Cliente = Cliente(nome='Felicity Jones',
                                cpf='123.456.789-87',
                                email='felicity@gmail.com',
                                data_nascimento='02/09/1987')
    angelina: Cliente = Cliente(nome='Angelina Jolie',
                                cpf='234.567.890-78',
                                email='angelina@gmail.com',
                                data_nascimento='08/07/1978')

    print(felicity, '\n')
    print(angelina)
