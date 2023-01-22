employees = {}
for i in range(1, 6):
    profession = input(f"\nProfissão do {i}º funcionário: ").strip().title()
    years_of_service = int(input(f"Anos de seviço do {i}º funcionário: "))
    employees[i] = {"profissão": profession, "anos de serviço": years_of_service}

with open("emp.txt", "w", encoding="utf-8") as f:
    for k, v in employees.items():
        f.write(f"{k}.º Funcionário:\n"
                f"\t\tProfissão: {v['profissão']}\n"
                f"\t\tAnos de serviço: {v['anos de serviço']}\n\n")
