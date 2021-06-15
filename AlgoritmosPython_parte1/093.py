senha = 'W'
s = 0
while s != senha:
    s = input('Digite a senha[caractere]: ').upper().strip()
    if s == senha:
        print('>>>Acesso liberado')
    else:
        print('>>>Acesso negado')