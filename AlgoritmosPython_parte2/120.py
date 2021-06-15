matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero na posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            soma3 += matriz[linha][coluna]
        if linha == 1:
            maior = matriz[1][coluna]
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
print('-='*35)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
print('-='*35)
print(f'A soma dos elementos pares da matriz é: {soma}')
print(f'A soma dos elementos da erceira coluna é: {soma3}')
print(f'O maior elemento da segunda linha é: {maior}')