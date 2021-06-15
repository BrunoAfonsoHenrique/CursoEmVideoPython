x = float(input('Digite o pimeiro valor: '))
y = float(input('Digite o segundo valor: '))
total = 1
if x < 8 and y < 5:
    while y >= 1:
        print('{} ^ {}'.format(x, y),end=' X ')
        total *= (x**y)
        y -= 1
    print('\nValor da expressão: {}'.format(total))
else:
    print('Valores invalidos!!!')
