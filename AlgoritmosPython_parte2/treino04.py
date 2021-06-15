valores = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais valor: ')),
        int(input('Digite o ultimo valor: ')))
print('-'*45)
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição: {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Os numeros pares são:', end=' ')
for cont in valores:
    if cont % 2 == 0:
        print(f'{cont}', end=' ')
