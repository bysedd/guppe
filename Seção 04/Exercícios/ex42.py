base_salary = float(input('Base salary: R$'))
salary = base_salary + base_salary * 0.05
salary -= base_salary * 0.07

print(f'Total salary: \033[0:36mR${salary:.2f}\033[m')
