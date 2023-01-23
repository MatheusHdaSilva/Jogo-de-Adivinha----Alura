print('****************************')
print('Jogo de adivinhação!')
print('****************************')

numerosecreto = 42

chute = int(input('Digíte seu número: '))
print('Você digítou o número:', chute)

if(numerosecreto == chute):
    print('você acertou')
else:
    if(chute > numerosecreto):
        print('você errou! O seu chute foi maior do que o número secreto.')
    elif(chute < numerosecreto):
        print('você errou! O chute foi menor do que o número secreto.')

print('Fim do Jogo')