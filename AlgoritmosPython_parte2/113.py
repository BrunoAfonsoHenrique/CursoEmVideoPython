valores = list()
maior = menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))

    if cont == 0:
        maior = menor = valores[0]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-'*30)
print(f'A lista é: {valores}')
print('-'*30)

print(f'O maior valor é {maior} nas posições ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')

print(f'\nO menor valor é {menor} nas posições ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
