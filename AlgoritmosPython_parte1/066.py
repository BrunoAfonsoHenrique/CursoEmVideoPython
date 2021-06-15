print('\033[33m-='*12)
print('   Controle de caixa   ')
print('\033[33m-=\033[m'*12)
qtd_dias = int(input('Digite o numero de dias de hospedagem do cliente: '))
print('-='*30)
total = qtd_dias * 95.0
if qtd_dias < 10:
    valor_final = (95.0 - (95.0 * 15 / 100)) * qtd_dias
    taxa = '15%'
    valor_desc = total - valor_final

elif qtd_dias == 10:
    valor_final = (95.0 - (95.0 * 10 / 100)) * qtd_dias
    valor_desc = total - valor_final
    taxa = '10%'
else:
    valor_final = (95.0 - (95.0 * 5 / 100)) * qtd_dias
    valor_desc = total - valor_final
    taxa = '5%'

print('Quantidade de dias da hospedagem: {}'.format(qtd_dias))
print('Valor a pagar sem desconto: R${:.2f}'.format(total))
print('Taxa de desconto sobre a diaria: {}'.format(taxa))
print('Valor do desconto total: R${:.2f}'.format(valor_desc))
print('Total a pagar: R${:.2f}'.format(valor_final))


