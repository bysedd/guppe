from computador import Computador
from equipamento import Equipamento
from testa_equipamento import TestaEquipamento

if __name__ == '__main__':
    testa_equipamento = TestaEquipamento(nome='Dell G15', preco=8849.00,
                                         cpu='i7-12700H', cores=14, threads=20, gpu='RTX 3060')
    testa_equipamento.main()

    testa_equipamento.computador.preco = 8549.99

    print('-' * 50)
    testa_equipamento.computador.exibe()
