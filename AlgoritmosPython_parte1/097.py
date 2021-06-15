#Inicialização das variáveis
qtd_criancas = qtd_adolescentes = qtd_adultos = total_pessoas = 0
qtd_classe_a = qtd_classe_b = qtd_classe_c = qtd_classe_d = 0
per_classe_a = per_classe_b = per_classe_c = per_classe_d = 0
porcentagem_criancas = porcentagem_adolescentes = porcentagem_adultos = 0
qtd_mulheres = qtd_homens = 0
#FIM
print('-='*25)
idade = int(input('Digite a idade [idade negativa para encerrar]: '))
while idade > 0:
    sexo = input('Digite o sexo [F/M]: ').upper().strip()

    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite o sexo [F/M]: ').upper().strip()

    sal_min = int(input('Quantidade de salários minimos: '))

#Calculo do total de Homens e Mulheres
    if sexo == 'F':
        qtd_mulheres += 1
    else:
        if sexo == 'M':
            qtd_homens += 1
#FIM

#Quantidade e porcentagem de crianças, adolescentes e adultos
    if idade <= 12:
        qtd_criancas += 1
    elif idade >= 13 and idade <= 20:
        qtd_adolescentes += 1
    elif idade > 20:
        qtd_adultos += 1

    total_pessoas += 1

    porcentagem_criancas = (100 * qtd_criancas) / total_pessoas
    porcentagem_adolescentes = (100 * qtd_adolescentes) / total_pessoas
    porcentagem_adultos = (100 * qtd_adultos) / total_pessoas
#FIM

#Percentual e quantidade de pessoas das Classes A, B, C e D
    if sal_min > 20: #Classe A
        qtd_classe_a += 1
    elif sal_min >= 10: #Classe B
        qtd_classe_b += 1
    elif sal_min >= 5: #Classe C
        qtd_classe_c += 1
    else:  #Classe D
        qtd_classe_d += 1

    per_classe_a = (100 * qtd_classe_a) / total_pessoas
    per_classe_b = (100 * qtd_classe_b) / total_pessoas
    per_classe_c = (100 * qtd_classe_c) / total_pessoas
    per_classe_d = (100 * qtd_classe_d) / total_pessoas

    print('-='*25)
    idade = int(input('Digite a idade [idade negativa para encerrar]: '))

#FIM

#Exibição Final / Resultados finais
print('-='*45)
print('Quantidade de crianças: {} -- Porcentagem de crianças: {:.2f}'.format(qtd_criancas, porcentagem_criancas))
print('Quantidade de adolescentes: {} -- Porcentagem de adolescentes: {:.2f}'.format(qtd_adolescentes, porcentagem_adolescentes))
print('Quantidade de adultos: {} -- Porcentagem de adultos: {:.2f}'.format(qtd_adultos, porcentagem_adultos))
print('-='*45)
print('Quantidade de habitantes da classe A: {} -- Porcentagem de Habitantes da classe A: {:.2f}'.format(qtd_classe_a, per_classe_a))
print('Quantidade de habitantes da classe B: {} -- Porcentagem de Habitantes da classe B: {:.2f}'.format(qtd_classe_b, per_classe_b))
print('Quantidade de habitantes da classe C: {} -- Porcentagem de Habitantes da classe C: {:.2f}'.format(qtd_classe_c, per_classe_c))
print('Quantidade de habitantes da classe D: {} -- Porcentagem de Habitantes da classe D: {:.2f}'.format(qtd_classe_d, per_classe_d))
print('-='*45)
print('Total de pessoas {}'.format(total_pessoas))
print('Total de Mulheres: {}'.format(qtd_mulheres))
print('Total de Homens: {}'.format(qtd_homens))