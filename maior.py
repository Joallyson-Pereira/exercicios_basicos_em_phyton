import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m       Analisando qual é o maior\033[m')
print('\033[1;30m-=\033[m'*20)
try:
    num1 = float(input('\033[1;33mPor favor, informe um número real: \033[m'))
    print()
    time.sleep(1)
    num2 = float(input('\033[1;33mPor favor, informe mais um número: \033[m'))
    print()
    time.sleep(1)
    print('\033[1;30m-=\033[m' * 20)
    print(f'\033[1;30mVocê informou os valores: {num1} e {num2}\033[m')
    if num1 == num2:
        print('\033[1;30mNão existe maior valor, os dois são iguais.\033[m')
    elif num1 > num2:
        print(f'\033[1;34{num1} foi o maior valor que você informou.m')
    else:
        print(f'\033[1;34m{num2} foi o maior valor que você informou.\033[m')
    print()
    print('\033[1;30m-=\033[m'*20)
    print('\033[1;30m               >> FIM <<')
    
    
except:
    print('\033[1;31m[ERRO] Verifique os valores que foram informados e tente novamente.\033[m')