numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quize', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
continuar = ''
while True:
    dig = int(input('Digite um numero entre 0 e 20: '))
    while dig < 0 or dig > 20:
        dig = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Numero digitado: {numeros[dig]}')
    print('-'*30)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('-' * 30)
print('-'*30)
print('Fim da execução!')

