def contador(*num):
    for v in num:
        print(f'{v}', end=' ')

    print(f' >>> total de numeros = {len(num)}')


contador(2, 1, 3)
contador(8, 0)
contador(4, 4, 7, 6, 2)