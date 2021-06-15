'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

valores.sort()
print(f'{valores}')
'''

valores = list()
for cont in range(0, 5):
    v = int(input('Digite um valor: '))

    if cont == 0 or v > valores[-1]:
        valores.append(v)
    else:
        cont2 = 0
        while cont2 < len(valores):
            if v <= valores[cont2]:
                valores.insert(cont2, v)
                break
            cont2 += 1
print(valores)

