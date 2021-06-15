from math import sqrt, floor

num = int(input('Digite um numero: '))

raiz = sqrt(num)

print('A raiz de {} é igual a {:.3f}'.format(num, floor(raiz)))

