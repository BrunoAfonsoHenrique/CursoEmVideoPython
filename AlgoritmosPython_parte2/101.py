num = cont = 1
while num >= 1:
    print('-='*35)
    num = int(input('Quer ver a tabuada de qual valor \033[31m(numero negativo para encerrar)\033[m? '))
    if num <= 0:
        break
    while cont <= 10:
        r = num * cont
        print(f'{num} X {cont} = {r}')
        cont += 1
    cont = 1
print('Programa Tabuada finalizado!!!')