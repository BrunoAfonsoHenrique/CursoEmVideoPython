dados = list()
lista = list()
qtd_pessoas = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'Dados: {lista}')
print(f'Quantidade de pessoas castradas: {len(lista)}')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')