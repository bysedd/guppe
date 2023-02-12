from models.calculator import Calculator


def jogar(pontos: int = 0) -> None:
    continuar: bool = True
    while continuar:
        try:
            # Solicita a dificuldade do jogo
            dificuldade: int = int(input('Informe o nível de dificuldade desejado (1, 2, 3 ou 4): '))

            # Cria uma instância da classe Calculator
            calc: Calculator = Calculator(dificuldade)

            # Mostra a operação
            resultado: float = float(input(f'\n{calc.mostrar_operacao()} = '))

            if calc.checar_resultado(resultado):
                # Adiciona um ponto
                pontos += 1
        except ValueError as e:
            # Mostra o erro
            print(f'{e!r}\n')
        else:
            # Mostra a pontuação atual
            print(f'Você tem {pontos} ponto(s).')

            # Verifica se o usuário deseja continuar no jogo
            continuar: bool = input('Deseja continuar no jogo? (S/N) ').upper() == 'S'
            print()

    # Mostra a pontuação final
    print(f'Você finalizou o jogo com {pontos} ponto(s).')
    print('Até a próxima!')


if __name__ == '__main__':
    jogar()
