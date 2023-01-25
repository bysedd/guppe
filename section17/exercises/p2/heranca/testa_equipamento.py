from computador import Computador
from equipamento import Equipamento


class TestaEquipamento:
    def __init__(self, nome: str, preco: float, cpu: str, cores: int, threads: int, gpu: str) -> None:
        self.__equipamento = Equipamento(nome, preco)
        self.__computador = Computador(nome, preco, cpu, cores, threads, gpu)

    @property
    def equipamento(self) -> Equipamento:
        return self.__equipamento

    @property
    def computador(self) -> Computador:
        return self.__computador

    def main(self):
        print('Equipamento:')
        self.equipamento.exibe()
        print('\nComputador:')
        self.computador.exibe()
