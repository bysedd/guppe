import unittest
from robo import Robo


class RoboTestes(unittest.TestCase):
    def setUp(self) -> None:
        self.robo = Robo('C3PO')
    
    def test_carregar(self) -> None:
        self.robo.carregar()
        self.assertEqual(100, self.robo.bateria)
    
    def test_dizer_nome(self) -> None:
        self.assertEqual('BEEP BEEP BEEP. EU SOU C3PO', self.robo.dizer_nome())
    
    def test_aprender_habilidade(self) -> None:
        self.assertEqual('Habilidade força adquirida com sucesso.', self.robo.aprender_habilidade('força', 10))
        self.assertIn('força', self.robo.habilidades)
        self.assertEqual(90, self.robo.bateria)
    
    def test_dizer_nome_apos_aprender_habilidade(self) -> None:
        self.robo.aprender_habilidade('força', 10)
        self.assertEqual('BEEP BEEP BEEP. EU SOU C3PO', self.robo.dizer_nome())
    
    def test_aprender_habilidade_sem_bateria(self) -> None:
        self.assertEqual(
            'Bateria insuficiente. Por favor, recarregue e tente novamente.',
            self.robo.aprender_habilidade('teleporte', 200)
        )
        self.assertNotIn('teleporte', self.robo.habilidades)
        self.assertEqual(100, self.robo.bateria)
    
    def test_dizer_nome_sem_bateria(self) -> None:
        for _ in range(101):
            self.robo.dizer_nome()
        self.assertEqual('Bateria fraca. Por favor, recarregue e tente novamente.', self.robo.dizer_nome())

    def tearDown(self) -> None:
        # remove o objeto criado no setUp
        del self.robo


if __name__ == '__main__':
    unittest.main()
