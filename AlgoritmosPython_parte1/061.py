n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 % n2 == 0:
    print('{} é multiplo de {}'.format(n1, n2))
else:
    print('{} não é multiplo de {}'.format(n1, n2))