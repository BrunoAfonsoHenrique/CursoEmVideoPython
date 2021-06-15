r1 = float(input('Primeiro segmento do triangulo: '))
r2 = float(input('Segundo segmento do triangulo: '))
r3 = float(input('Terceiro segmento do triangulo: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Os segmentos podem formar um triangulo.\n')

    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Os segmentos não podem formar um triangulo.')