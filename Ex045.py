from time import sleep
from random import randint
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opcões:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogadaJogador = int(input('Qual sua jogada: '))
jogadaComputador = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('=-'*20)
print('Jogada do Jogador: {}'.format(jogadas[jogadaJogador]))
print('Jogada do Computador: {}'.format(jogadas[jogadaComputador]))
print('=-'*20)

if jogadaComputador == 0 and jogadaJogador == 0:
    print('EMPATE')
elif jogadaComputador == 0 and jogadaJogador == 1:
    print('VITÓRIA do Jogador')
elif jogadaComputador == 0 and jogadaJogador == 2:
    print('VIÓRIA do Computador')
elif jogadaComputador == 1 and jogadaJogador == 0:
    print('VIÓRIA do Computador')
elif jogadaComputador == 1 and jogadaJogador == 1:
    print('EMPATE')
elif jogadaComputador == 1 and jogadaJogador == 2:
    print('VITÓRIA do Jogador')
elif jogadaComputador == 2 and jogadaJogador == 0:
    print('VITÓRIA do Jogador')
elif jogadaComputador == 2 and jogadaJogador == 1:
    print('VIÓRIA do Computador')
elif jogadaComputador == 2 and jogadaJogador == 2:
    print('EMPATE') 