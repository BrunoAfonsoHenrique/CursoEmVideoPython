'''
lista1 = list()
lista2 = list()
lista3 = list()
while True:
    v = int(input('Digite um valor: '))
    lista1.append(v)
    if v % 2 == 0:
        lista2.append(v)
    else:
        lista3.append(v)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Lista com todos os elementos: {lista1}')
print(f'Lista com elementos pares somente: {lista2}')
print(f'Lista com elementos impares somente: {lista3}')
'''
lista1 = list()
lista2 = list()
lista3 = list()

while True:
    lista1.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
for p, v in enumerate(lista1):
    if v % 2 == 0:
        lista2.append(v)
    else:
        lista3.append(v)
print(f'Lista com todos os elementos: {lista1}')
print(f'Lista com elementos pares somente: {lista2}')
print(f'Lista com elementos impares somente: {lista3}')
