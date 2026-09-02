from random import randint
from time import sleep
print('...JOGO DO ADIVINHA...')
numeroDoComputador = randint(0,5)
numeroDigitadoPeloUsuariio = int(input('Pensei em um número entre 0 e 5 adivinhe qual é ele: '))
print('PROCESSANDO...')
sleep(2)
if numeroDigitadoPeloUsuariio == numeroDoComputador:
    print('Você ganhou o.o')
else:
    print('Você perdeu o número era {}'.format(numeroDoComputador))
