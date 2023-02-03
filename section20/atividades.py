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
