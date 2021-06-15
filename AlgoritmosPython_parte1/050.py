from time import sleep

print('\033[33m<<< Contagem Regressiva >>>\033[m')

for cont in range(10, -1, -1):
    sleep(1)
    print(cont, end='  ')
print('\n\033[33mFIM')