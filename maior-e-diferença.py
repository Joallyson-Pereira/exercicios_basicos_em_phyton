import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m       Qual o maior e a diferença?\033[m')
print('\033[1;30m-=\033[m'*20)
try:
    num1 = float(input('\033[1;33mPor favor informe um número real: \033[m'))
    print()
    time.sleep(1)
    num2 = float(input('\033[1;33mInforme mais um: \033[m'))
    print()
    time.sleep(1)
    if num1 == num2:
        print('\033[1;30mNão existe maior valor, os dois são iguais.\033[m')
    elif num1 > num2:
        print(f'\033[30mO maior valor informado foi {num1}\033[m')
        print(f'\033[30mA diferença entre {num1} e {num2} é {num1-num2}\033[m')
    elif num2 > num1:
        print(f'\033[30mO maior valor informado foi {num2}\033[m')
        print(f'\033[30mA diferença entre {num2} e {num1} é {num2 - num1}\033[m')
    print()
    print('\033[1;30m-=\033[m' * 20)
    print('\033[1;30m               >> FIM <<')
except:
    print('\033[1;31m[ERRO] Verifique os valores que foram informados e tente novamente.\033[m')
    
