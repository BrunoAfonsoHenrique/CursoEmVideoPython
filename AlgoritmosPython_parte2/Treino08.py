numeros = list()
maior = menor = 0
for cont in range(0, 5):
    v = int(input(f'Digite um valor numerico na posição {cont}: '))
    numeros.append(v)

    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print(f'>>> O maior valor digitado foi {maior} nas posições: ', end='')
for p, c in enumerate(numeros):
    if numeros[p] == maior:
        print(f'{p}...', end='')
print(f'\n>>> O menor valor digitado foi {menor} nas posições: ', end='')
for p, c in enumerate(numeros):
    if numeros[p] == menor:
        print(f'{p}...', end='')