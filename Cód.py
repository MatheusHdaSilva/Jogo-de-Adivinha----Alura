print('****************************')
print('Jogo de adivinhação!')
print('****************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}.'.format(rodada, total_de_tentativas))
    chute = int(input('Digíte seu número: '))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print('Você digítou o número:', chute)

    if(acertou):
        print('você acertou')
    else:
        if(maior):
            print('você errou! O seu chute foi maior do que o número secreto.')
        elif(menor):
            print('você errou! O chute foi menor do que o número secreto.')
    rodada = rodada + 1

    print('Fim do Jogo')