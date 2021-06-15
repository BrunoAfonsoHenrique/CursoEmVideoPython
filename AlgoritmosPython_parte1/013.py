'''
Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

Considere: R$1,00 = RS5,53
'''

reais = float(input('Quantos reais você tem em sua carteira: '))

dolares = reais / 5.53

print('\nVocê pode comprar \033[4;35mRS{:.2f}\033[m dólares.'.format(dolares))