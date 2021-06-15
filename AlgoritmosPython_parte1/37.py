a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#saída
print('---' * 20)
print('\nPrimeiro valor: {}'.format(a))
print('Segundo valor: {}'.format(b))
print('Terceiro valor: {}'.format(c))
print('>>> O maior valor é: {}'.format(maior))
print('>>> O menor valor é: {}'.format(menor))

