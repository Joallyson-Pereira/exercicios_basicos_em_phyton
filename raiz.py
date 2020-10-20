import math
import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m       Calculando a raiz quadrada\033[m')
print('\033[1;30m-=\033[m'*20)
try:
    num = float(input('\033[1;33mPor favor, informe um número real (não negativo): \033[m'))
    print()
    time.sleep(1)
    raiz = math.sqrt(num)
    if num >= 0:
        print(f'\033[1;30mA raiz quadrada de {num} é {raiz:.2f}')
        print()
        print('\033[1;30m-=\033[m'*20)
        print('\033[1;30m             >> FIM <<\033[m')
    else:
        print('\033[1;31m[ERRO] \nInforme um número positivo\033[m')
except:
    print('\033[1;31m[ERRO] \nVerifique os valores informados e tente novamente.')