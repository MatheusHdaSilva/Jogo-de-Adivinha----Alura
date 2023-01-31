print('****************************')
print('ESCOLHA O SEU JOGO!')
print('****************************')

import Forca
import Adivinhação

print ('escolha seu jogo') 
print ('(1) forca (2) adivinhação')

Jogo = int(input('Qual o jogo? '))

if (Jogo == 1):
   print ("jogando forca") 
   Forca.jogar()

elif(Jogo == 2): 
   print("jogando adivinhação")
   Adivinhação.jogar()