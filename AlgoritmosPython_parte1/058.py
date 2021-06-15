frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ','')
inverso = ''
for cont in range(len(junto) - 1, -1, -1):
    inverso += junto[cont]
print('O inverso da palavra {} é {}'.format(frase, inverso))
if frase == inverso:
    print('É palindromo.')
else:
    print('Não é palindromo')