from random import randint


class Calculator:
    def __init__(self, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = soma, 2 = subtração, 3 = multiplicação
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def valor1(self) -> float:
        return self.__valor1

    @property
    def valor2(self) -> float:
        return self.__valor2

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def resultado(self) -> float:
        return self.__resultado

    @property
    def _gerar_valor(self) -> float:
        match self.dificuldade:
            case 1:
                return randint(0, 10)
            case 2:
                return randint(0, 100)
            case 3:
                return randint(0, 1000)
            case 4:
                return randint(0, 10000)
            case _:
                return randint(0, 100000)

    @property
    def _operador(self) -> str:
        match self.operacao:
            case 1:
                return '+'
            case 2:
                return '-'
            case 3:
                return '*'

    @property
    def _gerar_resultado(self) -> float:
        return eval(self.mostrar_operacao())

    def checar_resultado(self, resultado: float) -> bool:
        if certo := resultado == self.resultado:
            print('Resposta correta!')
        else:
            print('Resposta errada!', end=' -> ')
            # Mostra o resultado
            print(f'{self.valor1} {self._operador} {self.valor2} = {self.resultado}')
        # Retorna se está certo ou não
        return certo

    def mostrar_operacao(self) -> str:
        return f'{self.valor1} {self._operador} {self.valor2}'

    def __str__(self) -> str:
        match self.operacao:
            case 1:
                operacao = 'Somar'
            case 2:
                operacao = 'Diminuir'
            case 3:
                operacao = 'Multiplicar'
            case _:
                operacao = 'Operação desconhecida'

        return f'{self.valor1: } \n' \
               f'{self.valor2: } \n' \
               f'{self.dificuldade: } \n' \
               f'{operacao: } \n' \
