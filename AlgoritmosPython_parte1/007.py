'''
nome = input('Qual o seu nome: ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor:'))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1 ** n2

print('Soma é \033[31m{}\033[m, produto é \033[31m{}\033[m, divisão é \033[31m{:.3f}\033[m'.format(s, m, d), end=' ')
print(', divisão inteira \033[31m{}\033[m, e potência \033[31m{}\033[m'.format(di, e))


