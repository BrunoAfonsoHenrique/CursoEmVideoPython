v1 = int(input('Digite o primeiro valor: '))

v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('O \033[1;31mprimeiro\033[m valor é maior.')
elif v2 > v1:
    print('O \033[1;31msegundo\033[m valor é maior.')
else:
    print('\033[1;31mNão existe\033[m valor maior, os dois são iguais.')