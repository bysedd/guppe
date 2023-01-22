# coding=utf-8
from functions import print_formatado, error_message


class CadastroDeAlunos:
    def __init__(self):
        self.arquivo = "cadastro-de-alunos.txt"
        self.encoding = "utf-8"

    def cadastro(self):
        from datetime import date
        print_formatado("Cadastro de alunos")
        self.exists()

        if self.ler_arquivo():
            alunos = self.ler_arquivo()
        else:
            alunos = {}
        ano_minimo, ano_atual = 1907, date.today().year

        while True:
            try:
                qtd = int(input("Quantos alunos serão cadastrados? "))
                if qtd <= 0:
                    raise ValueError
                i = 1

                while i <= qtd:
                    try:
                        print_formatado(f"{i}.º aluno")
                        m = int(input("Digite o número da matrícula: "))
                        s = input("Digite o sobrenome: ").strip().title()
                        if not s or len(s) < 3 or not s.isalpha():
                            raise ValueError
                        n = int(input("Digite o ano de nascimento: "))
                        if n > ano_atual or n < ano_minimo:
                            raise ValueError
                    except ValueError:
                        print(error_message("Preencha todos os campos com um valor válido"))
                    else:
                        alunos[len(alunos) + i] = {"matricula": m, "sobrenome": s, "ano de nascimento": n}
                        i += 1

                self.registrar(alunos)
                print_formatado("Programa encerrado")
                break
            except ValueError:
                print(error_message("Digite um número válido"))

    def registrar(self, dados: dict):
        with open(self.arquivo, "w", encoding=self.encoding) as f:
            for k, v in dados.items():
                f.write(f"{v['matricula']},{v['sobrenome']},{v['ano de nascimento']}\n")

    def ler_arquivo(self):
        alunos = {}
        with open(self.arquivo, encoding=self.encoding) as f:
            for i, linha in enumerate(f.readlines()):
                linha = linha.split("\n")[0].split(",")
                m, s, n = linha
                alunos[i + 1] = {"matricula": int(m), "sobrenome": s, "ano de nascimento": int(n)}
        return alunos

    def exists(self):
        """
        Cria o arquivo se ele não existir no diretório atual.
        :return: None
        """
        import os
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding=self.encoding):
                pass


cda = CadastroDeAlunos()
cda.cadastro()
