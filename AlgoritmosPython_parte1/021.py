cat_opo = float(input('Digite o comprimento do cateto oposto: '))

cat_adj = float(input('Digite o comprimento do cateto adjacente: '))

from math import pow

soma = (pow(cat_opo, 2) + pow(cat_adj, 2))

from math import sqrt

hip = sqrt(soma)

print('\nCateto oposto = {}\nCateto adjacente = {}\nHipotenusa = {:.2f}'.format(cat_opo, cat_adj, hip))

'''
from math import hypot
hip = hypot(cat_opo, cat_adj)
'''