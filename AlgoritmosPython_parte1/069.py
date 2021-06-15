qtd = int(input('Digite a quantidade da mercadoria: '))
if qtd < 1000:
    preco_unitario = 100
elif qtd >= 1000 and qtd < 5000:
    preco_unitario = 90
elif qtd >= 500 and qtd < 10000:
    preco_unitario = 82
elif qtd >= 10000 and qtd < 50000:
    preco_unitario = 75
elif qtd >= 50000:
    preco_unitario = 70
print('-='*30)
print('Preço unitário: R${:.2f}'.format(preco_unitario))
print('Valor total da compra: R${:.2f}'.format(preco_unitario * qtd))