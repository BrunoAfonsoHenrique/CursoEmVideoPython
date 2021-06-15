num = qtd = soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        qtd = qtd + 1
        soma = soma + num
print('Você digitou {} números e a soma entre eles é {}.'.format(qtd, soma))
