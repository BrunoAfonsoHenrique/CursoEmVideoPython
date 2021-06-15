dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))

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
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Dados: {pessoas}')
print(f'Quantidade de pessoas castradas: {len(pessoas)}')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
