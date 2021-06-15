print('<<< Tabuada >>>\n')

num= int(input('Digite um numero para ver a tabuada respectiva: '))

print('{} X {:2} = {}'.format(num, 1, num * 1))
print('{} X {:2} = {}'.format(num, 2, num * 2))
print('{} X {:2} = {}'.format(num, 2, num * 3))
print('{} X {:2} = {}'.format(num, 4, num * 4))
print('{} X {:2} = {}'.format(num, 5, num * 5))
print('{} X {:2} = {}'.format(num, 6, num * 6))
print('{} X {:2} = {}'.format(num, 7, num * 7))
print('{} X {:2} = {}'.format(num, 8, num * 8))
print('{} X {:2} = {}'.format(num, 9, num * 9))
print('{} X {:2} = {}'.format(num, 10, num * 10))

print('\n\nUsando o laço while\n')

cont = 1
while cont <= 10:
    print('{} X {:2} = {:2}'.format(num, cont, num * cont))

    cont = cont + 1


