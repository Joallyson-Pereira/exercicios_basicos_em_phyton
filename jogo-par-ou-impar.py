import random
import time

#O try "pede" para o computador "tentar" executar o código:
try:
    vitoria = '\033[1;33mVitórias\033[m'
    derrota = '\033[1;31mDerrotas\033[m'
    
    numVitPC = 0
    numVitUS = 0
    
    numDerPC = 0
    numDerUS = 0
    print('\033[1;30m-=\033[m'*20)
    print('\033[1;30m            JOGO DO PAR OU ÍMPAR\033[m')
    print('\033[1;30m-=\033[m'*20)
    while True:
        option = str(input('\n\033[1;33mVocê escolhe Par ou Ímpar [P/I]: \033[m')).upper().strip()
        
        #Validação para que o programa não continue, caso o usuário informe uma opção inválida:
        if option != 'P' and option != 'I':
            while option != 'P' and option != 'I':
                print('\033[1;31mERRO\nInforme uma opção válida [S/N]\033[m')
                option = str(input('\n\033[1;33mVocê escolhe Par ou Ímpar [P/I]: \033[m')).upper().strip()
    
        #Opção que o computador irá escolher:
        numPc = random.randint(1, 11)
        
        #Simulação de carregamento de informação:
        print()
        time.sleep(1)
        for c in range(0,3):
            print('\033[1;30m. \033[m',end='')
            time.sleep(0.4)
        time.sleep(1)
        
        print('\n\033[30mO PC escolheu um número!\033[m')
        numUs = int(input('\033[33mEscolha um também: '))
        
        #Soma entre a escolha do PC e a escolha do usuário:
        soma = numPc + numUs
        
        #Resultado da soma:
        if soma % 2 == 0:
            resultado = 'Par'
        else:
            resultado = 'Ímpar'
            
        # Simulação de carregamento de informação:
        time.sleep(1)
        for c in range(0, 3):
            print('\033[1;30m. \033[m', end='')
            time.sleep(0.4)
        time.sleep(1)
        
        #Resultado a ser mostrado ao usuário
        print()
        print(f'\033[30mVocê escolheu {numUs} e o PC escolheu {numPc} a soma é igual a {soma}')
        if option in 'P' and resultado == 'Par' or option in 'I' and resultado == 'Ímpar':
            print(f'\033[33mO resultado da soma é {resultado}, VOCÊ GANHOU!!')
            numVitUS += 1
            numDerPC +=1
        elif option in 'P' and resultado == 'Ímpar' or option in 'I' and resultado == 'Par':
            print(f'\033[31mO resultado da soma é {resultado}, você perdeu :(\033[m')
            numDerUS += 1
            numVitPC += 1
        
        #Validação se o usuário quer continuar ou não:
        print()
        pergunta = str(input('\033[30mQuer continuar brincando? [S/N] \033[m')).upper().strip()
        if pergunta != 'S' and pergunta != 'N':
            while pergunta != 'S' and pergunta != 'N':
                print('\033[1;31mERRO\nInforme uma opção válida [S/N]\033[m')
                print()
                pergunta = str(input('\033[30mQuer continuar brincando? [S/N] \033[m')).upper().strip()
        
        #Caso a resposta for não, o código mostra as estatísticas de dá um break no final, caso a resposta seja sim, o bloco abaixo, não é executado:
        if pergunta in 'N':
            for c in range(0, 3):
                print('\033[1;30m. \033[m', end='')
                time.sleep(0.4)
            time.sleep(1)
            print()
            print('\033[1;30m-=\033[m' * 20)
            print(f'\033[1;30m{"ESTATÍSTICAS":^40}\033[m')
            print('\033[1;30m-=\033[m' * 20)
            print(f'{" " * 15} {vitoria}      {derrota}')
            print('\033[1;30m--\033[m' * 20)
            print(f'\033[30mPC{" "*17}{numVitPC}             {numDerPC}')
            print(f'\033[30mVocê{" " * 15}{numVitUS}             {numDerUS}')
            print('\033[1;30m--\033[m' * 20)
            break

        print('\033[1;30m-=\033[m'*20)
        
#Caso ocorra algum erro com o código, será mostrada uma mensagem de erro personalizada, utilizando-se o parâmetro except:
except:
    print('\033[1;31m[ERRO] \n Algo de errado não está certo\033[m')
    
#O parâmetro finally determina o que irá ocorrer no final, independente se o código der problema ou não:
finally:
    print('\033[1;30m               >> FIM <<')