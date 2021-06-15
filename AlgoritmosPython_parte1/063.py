a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a == b or a == c or b == c:
    print('Valores iguais para os termos não é permitido.')
else:
    if a > b and b > c:
        print('{} {} {}'.format(a, b, c))
    elif a > c and c > b:
        print('{} {} {}'.format(a, c, b))
    elif b > a and a > c:
        print('{} {} {}'.format(b, a, c))
    elif b > c and c > a:
        print('{} {} {}'.format(b, c, a))
    elif c > a and a > b:
        print('{} {} {}'.format(c, a, b))
    elif c > b and b > a:
        print('{} {} {}'.format(c, b, a))

print('FIM !!!')