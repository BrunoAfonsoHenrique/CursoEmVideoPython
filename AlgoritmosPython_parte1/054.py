soma = 0
qtd = 0
for cont in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
        qtd += 1
print('Você informou {} numeros pares e a soma deles é {}'.format(qtd, soma))