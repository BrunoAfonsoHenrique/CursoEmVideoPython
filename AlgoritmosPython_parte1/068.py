print('-='*25)
qtd = int(input('Digite a quantidade de produtos comprados: '))
print('-='*25)
preco = 75.00
total = qtd * preco

if qtd > 10:
    total_desc = total - (total * 10 / 100)
elif qtd > 40:
    total_desc = total - (total * 15 / 100)
elif qtd > 100:
    total_desc = total - (total * 25 / 100)

valor_descontado = total - total_desc
print('Valor total sem desconto: R${:.2f}'.format(total))
print('Valor abatido: R${:.2f}'.format(valor_descontado))
print('Valor final a ser pago: {:.2f}'.format(total_desc))