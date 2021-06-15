l1 = int(input('Digite o primeiro lado do triangulo: '))
l2 = int(input('Digite o primeiro lado do triangulo: '))
l3 = int(input('Digite o primeiro lado do triangulo: '))

if l1 ** 2 == l2 ** 2 + l3 ** 2:
    print('Triangulo retângulo')
elif l1 ** 2 > l2 ** 2 + l3 ** 2:
    print('Triangulo obtusangulo')
else:
    print('Triangulo acutangulo')