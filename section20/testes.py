import unittest
from atividades import *


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self) -> None:
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            ('quiabo', 'Estou comendo quiabo porque quero manter a forma.')
        )

    def test_comer_gostosa(self) -> None:
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            ('pizza', 'Estou comendo pizza porque nós só vivamos uma vez.')
        )

    def test_dormir_pouco(self) -> None:
        """Testando o retorno da função dormir com pouco sono"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas.'
        )

    def test_dormir_muito(self) -> None:
        """Testando o retorno da função dormir com muito sono"""
        self.assertEqual(
            dormir(horas=10),
            'Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_engracado(self) -> None:
        """Testando o retorno da função engracado com pessoas engraçadas"""
        # self.assertEqual(engracado('Felippe'), True)
        self.assertFalse(engracado('Sérgio'), False)
        self.assertTrue(engracado('Jim Carrey'), True)

    def test_par_impar(self) -> None:
        """Testando o retorno da função par_impar"""
        self.assertNotEqual(par_impar(3), '3 é par.')
        self.assertEqual(par_impar(4), '4 é par.')

    def test_flutuante(self) -> None:
        """Testando o retorno da função flutuante"""
        self.assertIs(flutuante('3.5'), True)
        self.assertIsNot(flutuante('abc'), True)

        self.assertIn(flutuante('3.5'), (True, False))

        self.assertIsInstance(flutuante('157.'), bool)
        self.assertNotIsInstance(flutuante('abc'), (set, tuple, list, dict, str))


if __name__ == '__main__':
    unittest.main()

