print('****************************')
print('Jogo de adivinhação!')
print('****************************')

numerosecreto = 42

chute = int(input('Digíte seu número: '))

acertou = chute == numerosecreto
maior = chute > numerosecreto
menor = chute < numerosecreto

print('Você digítou o número:', chute)

if(acertou):
    print('você acertou')
else:
    if(maior):
        print('você errou! O seu chute foi maior do que o número secreto.')
    elif(menor):
        print('você errou! O chute foi menor do que o número secreto.')

print('Fim do Jogo')