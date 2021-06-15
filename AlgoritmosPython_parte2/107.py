num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
dig = 0
cont = ' '
while True:
    dig = int(input('Digite um numero entre 0 e 20: '))
    while dig < 0 or dig > 20:
        dig = int(input('Tente novamente. Digite um numero entre 0 e 20: '))

    print(f'Você digitou o numero {num[dig]}')

    print('-' * 40)
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break

    print('-' * 40)

print('Fim da execução!!!')
