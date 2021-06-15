num = int(input('Digite um numero: '))
total = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m',end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} \033[m'.format(cont), end=' ')
print('\nO numero {} foi divisivel {} vezes\033[m'.format(num, total))

if total == 2:
    print('É primo.')
else:
    print('Não é primo.')