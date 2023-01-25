from pessoa import Pessoa
from testa_pessoa import TestaPessoa

if __name__ == '__main__':
    tp1 = TestaPessoa(1, 'João', 20)
    tp1.pessoa.exibe()
    tp1.pessoa.exibe(1)

    tp2 = TestaPessoa(2, 'Maria', 30)
    tp2.pessoa.exibe(1)
