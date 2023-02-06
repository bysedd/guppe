"""
Unittest - Antes e após hooks

----
hooks são os testes em si. Ou seja, a execução dos testes.
----

setup() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados.

tearDown() -> é executado após cada método de teste. É útil para excluir dados ou fechar conexões
com bancos de dados.


"""

import unittest


class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp() é executado antes do teste
        # tearDown() é executado após o teste
        pass

    def test_segundo(self):
        # setUp() é executado antes do teste
        # tearDown() é executado após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
