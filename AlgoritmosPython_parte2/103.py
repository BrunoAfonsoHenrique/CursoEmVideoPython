qtd_18 = qtd_h = qtd_20 = 0
while True:
    print('--' * 15)
    print('CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo [F/M] ? ')).upper().strip()[0]
    if idade >= 18:
        qtd_18 += 1
    if sexo == 'M':
        qtd_h += 1
    if sexo == 'F' and idade < 20:
        qtd_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Quantidade de pesssoas maiores de 18 anos: {qtd_18}')
print(f'Quantidade de homens cadastrados: {qtd_h}')
print(f'Quantidade de mulheres com menos de 20 anos: {qtd_20}')