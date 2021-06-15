numeros = list()
for cont in range(0, 5):
    v = int(input('Numero: '))

    if cont == 0 or v > numeros[-1]:
        numeros.append(v)
    else:
        cont2 = 0
        while cont2 <= len(numeros):
            if v <= numeros[cont2]:
                numeros.insert(cont2, v)
            break
        cont2 += 1
print(numeros)