def formata_moeda(valor: float) -> str:
    """
    Formata um valor float para moeda brasileira
    :param valor: Valor a ser formatado
    :return: Valor formatado
    """
    return f'R$ {valor:,.2f}'
