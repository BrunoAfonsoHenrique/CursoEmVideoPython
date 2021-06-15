for cont in range(0, 5):
    valor = int(input('Digite um numero:  '))

    if cont == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')