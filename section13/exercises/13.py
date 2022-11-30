from phonenumbers import format_number, PhoneNumberFormat, parse, NumberParseException

arquivo = "nome-telefone.txt"

with open(arquivo, "a") as f:
    while True:
        try:
            nome = input("Nome: ").strip().title()
            telefone = format_number(parse(input("Telefone: ").strip(), "BR"), PhoneNumberFormat.INTERNATIONAL)
            f.write(f"{nome:<40} {telefone}\n")
            print()
        except NumberParseException:
            break
