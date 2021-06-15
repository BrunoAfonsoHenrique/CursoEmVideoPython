numeros = list()

while True:
    v = int(input('Digite um numero: '))
    numeros.append(v)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Quantidade de numeros digitados: {len(numeros)}')
numeros.sort(reverse=True)
print(f'A ordem decrescente dos numeros é: {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')