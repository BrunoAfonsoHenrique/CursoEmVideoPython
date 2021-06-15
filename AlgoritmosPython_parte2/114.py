valores = list()

while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
    else:
        print('Valor já consta na lista.')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break
valores.sort()
print(f'Lista em ordem crescente: {valores}')