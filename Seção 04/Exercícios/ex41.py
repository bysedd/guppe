money_per_hour = float(input('Money for working hours: \033[1:36mR$\033[m'))
month_hours = int(input('Hours worked in the month: '))
net_salary = month_hours * money_per_hour
gross_salary = net_salary + net_salary * 0.10

print(f'Amount to be paid to the employee: \033[1:32mR${gross_salary:.2f}\033[m')
