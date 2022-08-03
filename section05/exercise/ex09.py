salary = float(input('Employee salary: R$'))
loan = float(input('Loan: R$'))

if salary * 0.2 < loan:
    print('\033[0:31mLoan not granted\033[m')
else:
    print('\033[0:32mLoan granted\033[m')
