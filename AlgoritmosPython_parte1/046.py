print('\033[1;31m <<< Calculo de IMC >>>\033[m\n')

peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[1;35mAbaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('\033[1;34mPeso ideal.')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSobrepeso')
elif imc >= 30 and imc <= 40:
    print('\033[1;31mObesidade')
else:
    print('\033[1;31mObesidade mórbida.')