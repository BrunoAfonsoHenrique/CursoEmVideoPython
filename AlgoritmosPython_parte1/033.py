vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Velocidade acima do limite permitido. Você foi multado(a).')
    print('O valor da multa é de R${}'.format(multa))
else:
    print('Velocidade esta dentro do limite de 80km/h.')