import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Testes para a classe Calculator
    """

    def setUp(self) -> None:
        # Dificuldade de 1 a 4
        self.calculator = Calculator(4)

    def test_dificuldade(self) -> None:
        self.assertGreaterEqual(self.calculator.dificuldade, 1)
        self.assertLessEqual(self.calculator.dificuldade, 4)

    def test_valor1(self) -> None:
        self.assertGreaterEqual(self.calculator.valor1, 0)
        self.assertLessEqual(self.calculator.valor1, 100000)

    def test_valor2(self) -> None:
        self.assertGreaterEqual(self.calculator.valor2, 0)
        self.assertLessEqual(self.calculator.valor1, 100000)

    def test_operacao(self) -> None:
        self.assertIn(self.calculator.operacao, (1, 2, 3))

    def test_checar_resultado(self) -> None:
        self.assertTrue(self.calculator.checar_resultado(self.calculator.resultado))


if __name__ == '__main__':
    unittest.main()
