temp = list()
lista_final = list()
maior = menor = 0
while True:
    nome = str(input('Digine o nome: '))
    peso = float(input('Digite o peso: '))

    temp.append(nome)
    temp.append(peso)

    if len(lista_final) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista_final.append(temp[:])

    temp.clear()
    print('--' * 25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('--' * 25)
print('-='*25)
print(f'Quantidade de pessoas cadastradas: {len(lista_final)}')
print('As pessoas mais pesadas são: ', end='')
for p in lista_final:
    if p[1] == maior:
        print(f'{p[0]} ', end=' ')
print('\nAs pessoas mais leves são: ', end='')
for p in lista_final:
    if p[1] == menor:
        print(f'{p[0]} ', end=' ')
print('-=' * 25)


