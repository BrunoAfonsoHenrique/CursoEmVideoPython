n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 < n2:
    while n1 <= n2:
        print('{}'.format(n1), end=' - ')
        n1 += 1
else:
    print('O primeiro valor é maior que o segundo: INVALIDO!!!')
print('FIM')