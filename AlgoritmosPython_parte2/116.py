numeros = list()

while True:
    n = int(input('Digite um numero:'))

    numeros.append(n)

    cotinuar = ' '
    while cotinuar not in 'SN':
        cotinuar = str(input('Deseja continuara? [S/N] ')).strip().upper()[0]
    if cotinuar == 'N':
        break

print(f'Quantidade de numeros digitados: {len(numeros)}')

numeros.sort(reverse=True)
print(f'Lista em ordem decrescente: {numeros}')

if 5 in numeros:
    print('O valor 5 esta na lista.')
else:
    print('O valor 5 não foi inserido na lista.')