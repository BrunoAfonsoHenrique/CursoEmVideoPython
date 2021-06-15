from math import radians,sin,cos,tan

angulo = float(input('Digite o ângulo que você deseja: '))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tag = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tag))