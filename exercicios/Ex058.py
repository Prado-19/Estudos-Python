from random import randint
num_sorteado = randint(0, 10)
qtd_tentativas = 1
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
num_chutado = int(input('Qual o seu palpite: '))
while num_chutado != num_sorteado:
    if num_chutado < num_sorteado:
        print('Mais...')
    else:
        print('Menos...')
    qtd_tentativas += 1
    num_chutado = int(input('Qual o seu palpite: '))
print('Você ACERTOU com {} tentativas, PARABÉNS'.format(qtd_tentativas))
