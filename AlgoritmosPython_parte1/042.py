from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year

idade = (ano_atual - ano_nasc)

if idade < 18:
    anos_faltantes = (18 - idade)
    print('\033[1;31mVai ainda se alistar ao serviço militar. Falta ainda {} anos.'.format(anos_faltantes))
elif idade == 18:
    print('\033[1;31mÉ hora de se alistar ao serviço militar.')
else:
    anos_passados = (idade - 18)
    print('\033[1;31mJá passou do tempo de alistamento. Já passsou {} anos.'.format(anos_passados))
