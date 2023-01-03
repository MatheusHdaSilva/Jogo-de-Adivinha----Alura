print('****************************')
print('Jogo de adivinhação!')
print('****************************')

numerosecreto = 42

chute = int(input('Digíte seu número: '))
print('Você digítou o número:', chute)

if(numerosecreto == chute):
    print('você acertou')
else:
    print('você errou')

print('Fim do Jogo')