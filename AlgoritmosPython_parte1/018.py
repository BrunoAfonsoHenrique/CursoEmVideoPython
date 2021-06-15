dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

km = float(input('Digite a quantidade de KM rodados: '))

preco = ((dias * 60) + (km * 0.15))

print('Total a pagar é de R${:.2f}'.format(preco))

