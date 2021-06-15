print('\n========== LOJAS BRUNOS ==========')

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print('=' * 32)
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor = preco - (preco * 10 / 100)
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
elif opcao == 3:
    valor = preco
    parcelas = valor / 2
    print('\033[1;33mSerá pago 2X de R${:.2f}\033[m'.format(parcelas))
elif opcao == 4:
    qtd_parcelas = int(input('Quantas parcelas? '))
    valor = preco + (preco * 20 / 100)
    parcelas = valor / qtd_parcelas
    print('\033[1;33mSua compra será parcelada em {}X de R${:.2f}\033[m'.format(qtd_parcelas, parcelas))
else:
    valor = preco
    print('Forma de pagamento inválida.')

print('''\033[1;33mO preço da compra é R$ {:.2f} e o valor total a pagar será de R${:.2f}. \033[1;33m'''.format(preco, valor))

