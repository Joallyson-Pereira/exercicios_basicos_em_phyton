import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m            Par ou Ímpar?\033[m')
print('\033[1;30m-=\033[m'*20)

try:
    num = int(input(f'\033[1;33mPor favor informe um número inteiro: \033[m'))
    print()
    time.sleep(1)
    if num % 2 == 0:
        print(f'\033[33m{num} é PAR.')
    else:
        print(f'\033[33m{num} é ÍMPAR.')
    print()
    print('\033[1;30m-=\033[m' * 20)
    print('\033[1;30m             >> FIM <<\033[m')
    
except:
    print('\033[1;31m[ERRO] \nVerifique os valores informados e tente novamente.')