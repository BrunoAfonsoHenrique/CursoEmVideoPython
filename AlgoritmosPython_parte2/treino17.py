principal = [[], []]

for cont in range(0, 7):
    v = int(input('Digite um numero: '))
    if v % 2 == 0:
        principal[0].append(v)
    else:
        principal[1].append(v)
print('-'*45)
print(f'Lista principal: {principal}')
print(f'Lista com elementos pares: {principal[0]}')
print(f'Lista com elementos impares: {principal[1]}')