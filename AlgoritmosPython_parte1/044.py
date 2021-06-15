from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))

idade = (date.today().year - ano_nasc)

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')