import unittest
from produto import Produto


class TestProduto(unittest.TestCase):
    def setUp(self) -> None:
        self.produto = Produto('Camiseta', 50)

    def test_id(self) -> None:
        self.assertEqual(self.produto.id, 1)

    def test_nome(self) -> None:
        # Verificando o nome do produto
        self.assertEqual(self.produto.nome, 'Camiseta')

        # Alterando o nome do produto e verificando se foi alterado
        self.produto.nome = 'Camisa'
        self.assertEqual(self.produto.nome, 'Camisa')

    def test_preco(self) -> None:
        # Verificando o preço do produto
        self.assertEqual(self.produto.preco, 50)

        # Alterando o preço do produto e verificando se foi alterado
        self.produto.preco = 100
        self.assertEqual(self.produto.preco, 100)


if __name__ == '__main__':
    unittest.main()
