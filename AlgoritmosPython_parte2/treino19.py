numeros = [[], []]
for cont in range(1, 8):
    v = int(input(f'Digite um valor na {cont}º posição: '))
    if v % 2 == 0:
        numeros[0].append(v)
    else:
        numeros[1].append(v)
print(f'Lista completa: {numeros}')
numeros[0].sort()
print(f'Pares: {numeros[0]}')
numeros[1].sort()
print(f'Ímpares: {numeros[1]}')