from equipamento import Equipamento


class Computador(Equipamento):
    def __init__(self, nome: str, preco: float, cpu: str, cores: int, threads: int, gpu: str) -> None:
        super().__init__(nome, preco)
        self.__cpu = cpu
        self.__nucleos = cores
        self.__threads = threads
        self.__gpu = gpu

    @property
    def cpu(self) -> str:
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu: str) -> None:
        self.__cpu = cpu

    @property
    def nucleos(self) -> int:
        return self.__nucleos

    @nucleos.setter
    def nucleos(self, nucleos: int) -> None:
        self.__nucleos = nucleos

    @property
    def threads(self) -> int:
        return self.__threads

    @threads.setter
    def threads(self, threads: int) -> None:
        self.__threads = threads

    @property
    def gpu(self) -> str:
        return self.__gpu

    @gpu.setter
    def gpu(self, gpu: str) -> None:
        self.__gpu = gpu

    def exibe(self) -> None:
        super().exibe()
        print(f'CPU: {self.cpu} | Cores/Threads: {self.nucleos}/{self.threads}')
        print(f'GPU: {self.gpu}')
