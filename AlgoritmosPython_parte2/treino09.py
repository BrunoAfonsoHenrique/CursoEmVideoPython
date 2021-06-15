numeros = list()
cont = 0
while True:
    if cont == 0:
        v = int(input('Digite um valor numerico: '))
        numeros.append(v)
    else:
        if v not in numeros:
            numeros.append(v)
        else:
            print('AVISO: Valor já consta inserido na lista. Não será adicionado!')
    cont += 1
    contibuar = ' '
    while contibuar not in 'SN':
        contibuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if contibuar == 'N':
        break
    v = int(input('Digite um valor numerico: '))
print(f'Lista: {numeros}')
numeros.sort()
print(f'Lista em ordem crescente: {numeros}')