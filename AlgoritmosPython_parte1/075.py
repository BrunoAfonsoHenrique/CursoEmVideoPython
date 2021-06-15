from math import factorial
x = int(input('Digite um numero: '))
soma = 0
for cont in range(1, 10+1):
    y = (x ** cont) / factorial(cont)
    soma = soma + y
print('Soma = {:.2f}'.format(soma))