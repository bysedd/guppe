import unittest
from atividades import comer, dormir


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


if __name__ == '__main__':
    unittest.main()
