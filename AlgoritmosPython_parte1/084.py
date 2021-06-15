num = int(input('Digite um numero para ver o fatorial: '))
cont = num; fat = 1
for cont in range(cont, 0, -1):
    fat *= cont
print('O fatorial de {} = {}'.format(num, fat))