matriz = [[0, 0,  0], [0, 0,  0], [0, 0,  0]]
soma = soma3 = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero na posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            soma3 += matriz[linha][coluna]
        if linha == 1:
            maior = matriz[1][coluna]
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]

print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda colina é: {maior}')