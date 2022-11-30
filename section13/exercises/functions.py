def get_idade(data_de_nascimento: str = "01/06/2005"):
    """
    Converte a data de nascimento em idade (anos)
    :param data_de_nascimento: Deve ter o seguinte formato: dia/mes/ano
    :return: Retorna a idade
    """
    from datetime import date
    dia, mes, ano = data_de_nascimento.split("/")
    return (date.today() - date(day=int(dia), month=int(mes), year=int(ano))).days // 365


def str_to_bin(string: str = "Hello World!"):
    """
    Converte um tipo em outro.
    :param string: string
    :return: binário
    """
    binario = ""
    for i in string:
        binario += bin(ord(i))[2::]
    return binario


def float_to_bin(decimal: float = 7):
    """
    Convete um número flutuante para um binário.
    :param decimal: número com ponto flutuante
    :return: binário
    """
    decimal = str(decimal).split(".")
    binario = ""
    for numero in decimal:
        binario += f"{bin(int(numero))}"
        if "0b" in binario:
            binario = binario.replace("0b", "")
    return binario
