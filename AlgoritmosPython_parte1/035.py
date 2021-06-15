km = float(input('Digite a distância da viagem em KM: '))

if km <= 200:
    preco = 0.50 * km
else:
    preco = 0.45 * km

print('O preço da passagem é R${}'.format(preco))