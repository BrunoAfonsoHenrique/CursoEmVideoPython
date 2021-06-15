num = qtd = soma = 0
while num != 999:
    num = int(input('Digite um numero (999 para parar): '))
    if num == 999:
        break
    qtd += 1
    soma += num
print(f'Soma entre os {qtd} valores é: {soma} ')
