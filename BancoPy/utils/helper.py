from datetime import date, datetime


def date_para_str(data: date, /) -> str:
    """
    Converte uma data para string no formato dd/mm/aaaa
    :param data: Data a ser convertida
    :return: Data no formato dd/mm/aaaa
    """
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str, /) -> date:
    """
    Converte uma string no formato dd/mm/aaaa para data
    :param data: String no formato dd/mm/aaaa
    :return: Data
    """
    return datetime.strptime(data, '%d/%m/%Y').date()


def formatar_moeda(valor: float, /) -> str:
    """
    Formata um valor monetário para reais com duas casas decimais e separador de milhar
    :param valor: Valor a ser formatado
    :return: Valor formatado
    """
    return f'R$ {valor:,.2f}'


def formatar_cpf(cpf: str, /) -> str:
    """
    Formata um CPF no formato xxx.xxx.xxx-xx
    :param cpf: CPF a ser formatado
    :return: CPF formatado
    """
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
