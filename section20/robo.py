class Robo:
    def __init__(self, nome: str, bateria: int = 100, habilidades: list = []):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def bateria(self) -> int:
        return self.__bateria
    
    @property
    def habilidades(self) -> list:
        return self.__habilidades
    
    def carregar(self) -> None:
        self.__bateria = 100

    def dizer_nome(self) -> str:
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BEEP BEEP. EU SOU {self.nome.upper()}'
        return 'Bateria fraca. Por favor, recarregue e tente novamente.'

    def aprender_habilidade(self, nova_habilidade: str, custo: int) -> str:
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'Habilidade {nova_habilidade} adquirida com sucesso.'
        return 'Bateria insuficiente. Por favor, recarregue e tente novamente.'
