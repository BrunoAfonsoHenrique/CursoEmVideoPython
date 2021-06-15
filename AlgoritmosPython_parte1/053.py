num = int(input('Digite um numero par ver a tabuda correspondente: '))
for cont in range(1, 11):
    print('{:2} X {:2} = {:2}'.format(num, cont, num * cont))