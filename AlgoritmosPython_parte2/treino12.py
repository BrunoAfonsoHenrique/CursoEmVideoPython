numeros = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-' * 45)
print('-'*45)
print(f'Lista original: {numeros}')
print(f'Lista contendo os elementos pares: {pares}')
print(f'Lista contendo os elementos impares: {impares}')
