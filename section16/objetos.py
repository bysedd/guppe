"""
POO - Objetos

Objetos ≥ São instâncias da classe. Ou seja, após o mapeamento do objeto real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de
uma classe do tipo definido na classe.

# Instanciando objetos
lamp1: Lampada = Lampada('branca', 110, 60)
lamp1.ligar_desligar()
print(lamp1.checa_lampada())

nome: str = 'Felippe'
sobrenome: str = 'Andrade'
email: str = 'felippe@gmail.com'
senha: str = '12345678'
user: Usuario = Usuario(nome, sobrenome, email, senha)
print(user.__dict__)
print(type(user))
"""


class Lampada:
    def __init__(self, cor: str, voltagem: int, luminosidade: int):
        self.__cor: str = cor
        self.__voltagem: int = voltagem
        self.__luminosidade: int = luminosidade
        self.__ligada: bool = False

    def checa_lampada(self):
        return 'Lâmpada ligada' if self.__ligada else 'Lâmpada desligada'

    def ligar_desligar(self):
        self.__ligada = not self.__ligada


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.__nome: str = nome.strip().title()
        self.__cpf: str = cpf

    def diz_oi(self):
        print(f'Olá, eu sou o cliente {self.__nome}')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite: int, saldo: int, cliente: Cliente):
        self.__numero: int = ContaCorrente.contador + 1
        self.__limite: int = limite
        self.__saldo: int = saldo
        self.__cliente: Cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostrar_cliente(self):
        print(f'Cliente: {self.__cliente.__dict__}')


class Usuario:
    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        from passlib.hash import pbkdf2_sha256 as crypt

        self.__nome: str = nome.strip().title()
        self.__sobrenome: str = sobrenome.strip().title()
        self.__email: str = email
        self.__senha: str = crypt.hash(senha, rounds=200000, salt_size=16)


cc: ContaCorrente = ContaCorrente(5000, 20000, Cliente('Felippe', '123.456.789-00'))
cc.mostrar_cliente()
cc._ContaCorrente__cliente.diz_oi()
