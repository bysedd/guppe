worked_days = int(input('Worked days: '))

if worked_days > 31:
    print('You really worked hard this month.')

else:
    net_salary = worked_days * 30.0
    gross_salary = net_salary - net_salary * 0.08

    print(f"\033[1:36mNet salary: R${net_salary:.2f}\033[m")
    print(f"\033[1:32mGross salary: R${gross_salary:.2f}\033[m")
