num = [16, 8, 2, 5, 1, 6, 7]
print(num)
print(num[0])

print('-'*60) #-------------------------------------------------------------

lanche = ['Hamburguer', 'Cerveja', 'Pizza', 'Pudim']
print(lanche)
lanche[2] = 'Bolo'
print(lanche)

print('-'*60) #-------------------------------------------------------------
lanche = ['Hamburguer', 'Cerveja', 'Pizza', 'Pudim']
print(lanche)

lanche.append('Vinho')
print(lanche)

lanche.insert(1, 'Cachorro-quente')
print(lanche)

print('-'*60)#-------------------------------------------------------------
lanche = ['Hamburguer', 'Cerveja', 'Pizza', 'Pudim']
print(lanche)

del lanche[3]
print(lanche)

lanche.pop(1)
print(lanche)

lanche.remove('Pizza')
print(lanche)

print('-'*60)#-------------------------------------------------------------
lanche = ['Hamburguer', 'Cerveja', 'Pizza', 'Pudim']
print(lanche)

for cont in lanche:
    print(cont, end=' ')

print('\n')
print('-'*60)#-------------------------------------------------------------
lanche = ['Hamburguer', 'Cerveja', 'Pizza', 'Pudim']
print(lanche)

if 'Pizza' in lanche:
    lanche.remove('Pizza')
print(lanche)

print('-'*60)#-------------------------------------------------------------
valores = list(range(0, 7))
print(valores)

print(valores[3])

print('-'*60)#-------------------------------------------------------------
valores = [6, 8, 6, 4, 2, 1, 0, 3, 9]
print(valores)

valores.sort()
print(valores)

valores.sort(reverse= True)
print(valores)

tamanho = len(valores)
print(tamanho)

print('-'*60)#-------------------------------------------------------------
lista = [6, 8, 6, 4, 2, 1, 0, 3, 9]
print(lista)
if 7 in lista:
    lista.remove(7)
else:
    print('O valor 7 não esta na lista.')

