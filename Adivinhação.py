import random

def jogar():

    print('****************************')
    print('Jogo de adivinhação!')
    print('****************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100
    print('Qual Nível de dificuldade?')
    print('(1) Facíl (2) Médio (3) Difícil')

    nivel = int(input('Defina um Nível: '))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print('Tentativa {} de {}.'.format(rodada, total_de_tentativas))
        
        chute = int(input('Digíte um número entre 1 e 100: '))
        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print('Você digítou o número:', chute)

        if(acertou):
            print('você acertou e fez {} Pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('você errou! O seu chute foi maior do que o número secreto.')
            elif(menor):
                print('você errou! O chute foi menor do que o número secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    print('Fim do Jogo')   

if(__name__ =="_main_"):
    jogar()