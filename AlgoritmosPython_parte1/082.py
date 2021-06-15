v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('-=' * 20)
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    op = int(input('>>>>> Qual é sua opção? '))
    if op == 1:
        print('A soma entre {} + {} = {}'.format(v1, v2, v1+v2))
    elif op == 2:
        print('A multiplicação entre {} X {} = {}'.format(v1, v2, v1 * v2))
    elif op == 3:
        maior = v1
        if v2 > maior:
            maior = v2
        print('O maior número entre os digitados é: {}'.format(maior))
    elif op == 4:
        print('Informe os numeros novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op >= 6:
        print('Opção digitada é invalida!!!')
print('Fim da execução!!!')