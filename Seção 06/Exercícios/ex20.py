count_numbers, count_even = 0, 0
print('\033[1:31mEnter "1000" to stop\033[m\n')
while True:
    n = int(input('Enter an integer: '))
    count_numbers += 1
    if n % 2 == 0:
        count_even += 1
    if n == 1000:
        break

print(f'\nNumber of data read: \033[1:33m{count_numbers}\033[m')
print(f'Number of even values: \033[1:32m{count_even}\033[m')
