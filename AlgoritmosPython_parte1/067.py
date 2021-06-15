print('Programa estacionamento')
print('-='*20)
h_entrada = int(input('Digite a hora de entrada: '))
h_saida = int(input('Digite a hora de saida: '))

if h_entrada >= 8 and h_entrada <= 18:
    if h_saida >= 8 and h_saida <= 18:
        permanencia = h_saida - h_entrada

        if permanencia == 1:
            pag = 8
        elif permanencia == 2:
            pag = 15
        elif permanencia >= 3:
            pag = 5 * permanencia

        print('O valor a ser pago é R${:.2f}'.format(pag))
else:
    print('Hora inválida')