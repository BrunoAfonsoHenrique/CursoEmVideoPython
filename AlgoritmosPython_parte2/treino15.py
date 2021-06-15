principal = list()
temp = list()
while True:
    numero = int(input('Digite um numero:  '))
    temp.append(numero)

    if len(principal) == 0:
        maior = menor = temp[0]
    else:
        if temp[0] > maior:
            maior = temp[0]
        if temp[0] < menor:
            menor = temp[0]

    principal.append(temp[:])

    temp.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Lista: {principal}')
print(f'O maior valor da lista é: {maior}')
print(f'O menor valor da lista é: {menor}')