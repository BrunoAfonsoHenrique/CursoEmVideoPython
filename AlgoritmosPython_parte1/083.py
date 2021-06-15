'''
from math import factorial
num = int(input('Digite um numero para ver o fatorial: '))
f = factorial(num)
print('O fatorial de {} é: {}'.format(num, f))
'''

num = int(input('Digite um numero para ver o fatorial: '))
cont = num; fat = 1
while cont > 0:
    fat *= cont
    cont -= 1
print('O fatorial de {} = {}'.format(num, fat))

