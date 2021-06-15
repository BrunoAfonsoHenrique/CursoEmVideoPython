n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
resto = 1
print('MDC({},{})'.format(n1, n2), end='')
while resto != 0:
        resto = n1 % n2
        if resto == 0:
            mdc = n2
        else:
            resto = n1 % n2
            n1 = n2
            n2 = resto
            mdc = n2
print(' =', mdc)