def maior(*m):

    print('-='*30)
    print('Analisando os valores passados...')
    if len(m) > 1:
        for cont in range(0, len(m)):
            print(f'{m[cont]}', end=' ')
        print(f'Foram informados {len(m)} valores ao todo.')
    else:
        if m[0] == 0:
            for cont in range(0, len(m)):
                print(f'Foram informados 0 valores ao todo.')
        else:
            print(f'{m[0]}', end=' ')
            print(f'Foram informados {len(m)} valores ao todo.')
    print(f'O maior valor informado foi {max(m)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)