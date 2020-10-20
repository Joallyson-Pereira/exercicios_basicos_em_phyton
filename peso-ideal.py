import time
print('\033[1;30m-=\033[m'*20)
print('\033[1;30m               PESO IDEAL\033[m')
print('\033[1;30m-=\033[m'*20)
try:
    sexo = str(input('\033[1;33mPor favor, informe o seu sexo [M/F]: \033[m')).upper().strip()
    if sexo not in 'MF':
        print('\033[1;31mERRO, Informe um sexo válido!\033[m')
    else:
        print()
        time.sleep(1)
        nome = str(input('\033[1;33mComo você se chama? \033[m')).strip()
        print()
        time.sleep(1)
        print(f'\033[1;30mOlá {nome}, é um prazer te conhecer!')
        altura = float(input('\033[1;30mQual é a sua altura em centímetros? \033[m'))
        print()
        time.sleep(1)
        for c in range(0,3):
            print('\033[1;30m.\033[m', end='')
            time.sleep(0.4)
        if sexo == 'M':
            ideal = (altura-100) * 0.9
        else:
            ideal = (altura - 100) * 0.85
        print()
        time.sleep(1)
        print(f'\033[1;33m{nome} o seu peso ideal, de acordo com padrões determinados pela OMS, é de: {ideal:.2f} Kg.\033[m')
        print()
except:
    print('\033[1;31m[ERRO] Verifique os valores que foram informados e tente novamente.\033[m')
finally:
    print('\033[1;30m-=\033[m' * 20)
    print('\033[1;30m               >> FIM <<')
    
    
    