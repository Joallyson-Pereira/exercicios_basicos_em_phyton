import math
import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m           Raiz ou quadrado?\033[m')
print('\033[1;30m-=\033[m'*20)
try:
    num = float(input('\033[1;33mPor favor, informe um número real: \033[m'))
    print()
    time.sleep(1)
    if num > 0:
        raiz = math.sqrt(num)
        print(f'\033[33mA raiz quadrada de {num} é {raiz:.1f} .')
    else:
        potencia = num ** 2
        print(f'\033[33m{num} ao quadrado é igual a {potencia:.1f} .')
    print()
    print('\033[1;30m-=\033[m' * 20)
    print('\033[1;30m             >> FIM <<\033[m')
    
    
except:
    print('\033[1;31m[ERRO] \nVerifique os valores informados e tente novamente.')