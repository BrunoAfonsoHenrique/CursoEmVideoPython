valor= input('Digite um valor: ')

print('O tipo primitivo desse valor é', type(valor)) #Verifique o tipo primitivo

print('É letra?', valor.isalpha()) #Verifique se todos os caracteres do texto são letras

print('É alfanumérico?', valor.isalnum()) #Verifique se todos os caracteres do texto são alfanuméricos

print('É numérico?',valor.isnumeric()) #Verifique se todos os caracteres do texto são numéricos

print('É maiúsculo?', valor.isupper()) #Verifique se todos os caracteres do texto estão em maiúsculas

print('É ASCII?', valor.isascii()) #Verifique se é uma string está em ASCII ou não

print('É decimal?', valor.isdecimal()) #Verifique se todos os caracteres no objeto Unicode são decimais

print('É digito?', valor.isdigit()) #Verifique se todos os caracteres do texto são dígitos

print('Tem identificador válido?', valor.isidentifier()) #Verifique se a string é um identificador válido

print('É minusculo?', valor.islower()) #Verifique se todos os caracteres do texto estão em minúsculas

print('Todos os caracteres podem ser impressos?',valor.isprintable()) #Verifique se todos os caracteres do texto podem ser impressos

