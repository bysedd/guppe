def comer(comida: str, saudavel: bool) -> tuple:
    """
    Comer uma comida
    :param comida: O que comer
    :param saudavel: Se a comida é saudável ou não
    :return: Uma tupla com a comida e a saúde
    """
    final = f'Estou comendo {comida} porque '
    final += 'quero manter a forma.' if saudavel else 'nós só vivamos uma vez.'
    return comida, final


def dormir(horas: int) -> str:
    """
    Dormir por um número de horas
    :param horas: Número de horas para dormir
    :return: Uma ‘string’ com a mensagem
    """
    if horas > 8:
        return 'Dormi muito! Estou atrasado para o trabalho!'
    return f'Continuo cansado após dormir por {horas} horas.'


def engracado(pessoa: str) -> bool:
    """
    Verificar se uma pessoa é engraçada
    :param pessoa: Nome da pessoa
    :return: Verdadeiro se a pessoa for engraçada
    """
    pessoa = pessoa.strip().title()
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False


def par_impar(numero: int) -> str:
    """
    Verificar se um número é par ou ímpar
    :param numero: Número a ser verificado
    :return: Uma ‘string’ com a mensagem
    """
    if numero % 2 == 0:
        return f'{numero} é par.'
    return f'{numero} é ímpar.'


def flutuante(numero) -> bool:
    """
    Verificar se um número é flutuante
    :param numero: Número a ser verificado
    :return: Verdadeiro se o número for flutuante
    """
    # Converter o número para float
    try:
        numero = float(numero)
        # Verificar se o número é flutuante
        if isinstance(numero, float) or numero.is_integer():
            return True
        return False
    except ValueError:
        return False
