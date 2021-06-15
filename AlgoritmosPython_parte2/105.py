print('-'*35)
print('{:^35}'.format('LOJAS ECONOMICA: FILIAL DOIS'))
print('-'*35)

total = qtd_prod = cont = menor = 0
continuar = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))

    total += preco

    if preco > 1000:
        qtd_prod += 1

    cont += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja coninuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('-'*35)
print(f'O total é: R${total:.2f}')
print(f'Quantidade de produtos que custa mais de R$1000,00: {qtd_prod}')
print(f'Nome do produto mais barato: {barato}')
