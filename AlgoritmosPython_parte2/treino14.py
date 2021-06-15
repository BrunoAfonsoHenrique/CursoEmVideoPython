pessoas = list()
dados = list()
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))

    dados.append(nome)
    dados.append(peso)

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])

    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi de {maior} das pessoas: ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor} das pessoas: ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')