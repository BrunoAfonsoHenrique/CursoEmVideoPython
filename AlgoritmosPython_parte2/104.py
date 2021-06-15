print('-'*40)
print('{:^40}'.format('LOJAS ECONOMIA ECONOMICA'))
print('-'*40)

total = qtd_prod = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    qtd_prod = 0
    if preco > 1000:
        qtd_prod += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        print('-' * 40)
    if continuar == 'N':
        break

print(f'Total da compra: R${total:.2f}')
print(f'Temos {qtd_prod} produto(s) custando mais de R$1000,00 reais')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')