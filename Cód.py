import random


print('****************************')
print('Jogo de adivinhação!')
print('****************************')

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3
rodada = 1

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
        print('você acertou')
        break
    else:
        if(maior):
            print('você errou! O seu chute foi maior do que o número secreto.')
        elif(menor):
            print('você errou! O chute foi menor do que o número secreto.')

    print('Fim do Jogo')