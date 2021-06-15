valor = float(input('Qual o valor da casa? '))

salario = float(input('Qual o salário do comprador? '))

anos = int(input('Quantos anos para pagar? '))

prestacao = valor / (anos * 12)

print('Para pegar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, prestacao))
if prestacao > (salario * 30 / 100):
    print('\033[1;31mEmpréstimo NEGADO!')
else:
    print('\033[1;32mEmpréstimo APROVADO!')