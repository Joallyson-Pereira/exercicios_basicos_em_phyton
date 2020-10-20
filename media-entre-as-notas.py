import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m          Média entre as notas\033[m')
print('\033[1;30m-=\033[m'*20)

try:
    nota1 = float(input('\033[1;33mPor favor, informe a sua primeira nota: \033[m'))
    print()
    time.sleep(1)
    if nota1 > 10 or nota1<0:
        print('\033[1;31m[ERRO] \nSua nota precisa ser um valor entre 0 e 10.\033[m')
    else:
        nota2 = float(input('\033[1;33mPor favor informe mais uma nota: \033[m'))
        print()
        time.sleep(1)
        if nota2 > 10 or nota2 < 0:
            print('\033[1;31m[ERRO] \nSua nota precisa ser um valor entre 0 e 10.\033[m')
        else:
            print(f'\033[30mA média entra as notas {nota1} e {nota2} é igual a {(nota1+nota2)/2}')
            print()
        print('\033[1;30m-=\033[m' * 20)
        print('\033[1;30m               >> FIM <<')

except:
    print('\033[1;31m[ERRO] Verifique os valores que foram informados e tente novamente.\033[m')