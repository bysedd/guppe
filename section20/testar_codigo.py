"""
Por que testar nosso código?

Testes automatizados!


          Aplicação web
---------------------------------
/      frontend e backend       /
---------------------------------
/     testes automatizados      /
---------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código em produção;
    - Testes garantem que novas funcionalidades da sua aplicação não quebrem funcionalidades antigas;
    - Testes garantem que bugs (problemas) que foram corrigidos continuam anteriormente corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs (problemas) no código;
    - Testes garantem que a desempenho da sua aplicação não seja comprometida com novas funcionalidades;

TDD (Test Driven Development) - Desenvolvimento Guiado por Testes

Com TDD, é utilizado estágios de desenvolvimento:
    - Primeiro escrevemos nossos testes;
    - Então escrevemos o código mínimo suficiente para fazer o teste passar, ou seja, executar com sucesso;
    - Então refatoramos o código para realizar a funcionalidade e testamos novamente;
    - Visto que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;

    - Red: escrever um teste que falha;
    - Green: escrever o código mínimo suficiente para fazer o teste passar;
    - Refactor: refatorar o código e testar novamente para garantir que o teste ainda passe;

"""


class Gato:
    """
    Classe que representa um gato
    """
    def __init__(self, nome: str):
        """
        Construtor da classe Gato
        :param nome: Nome do gato
        """
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    def miar(self) -> str:
        """
        Retorna o som de um gato miando
        :return: Som de um gato miando
        """
        return f'{self.nome} está miando...'


felix = Gato('Felix')
print(felix.miar())
print(felix.nome)
